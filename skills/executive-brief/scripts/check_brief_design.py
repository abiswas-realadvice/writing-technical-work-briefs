#!/usr/bin/env python3
"""Deterministically check a brief's HTML against the field guide's design rules.

Checks only the "design element" rules from reference/design-and-visuals.md
that are objectively, mechanically checkable: heading hierarchy (per page),
sentence-case headings, image alt text, WCAG text contrast, underline usage,
table header rows and numeric-column alignment, chart-spec completeness and
zero-baseline bar axes, color-alone status encoding, body text size, a
source/status footer, and color palette restraint.

It deliberately does not (and cannot) check whether a headline states the
right claim, whether a causal verb matches the evidence, or any other rule
in the guide that needs judgment rather than measurement.

This is a small, self-contained tool with no third-party dependencies. To
check contrast and font size on real-world CSS (not just documents authored
to this repo's own convention), it resolves a *simplified* cascade: for each
text-bearing element it checks the element's own inline style="..." first
(inline always wins, as in real CSS), then the matching <style>-block rules,
ranked by a (ids, classes, types) specificity approximation and source
order, and inherits color/background/font-size up the tree the way a
browser would. Deliberate, documented limits of that simplification:
  - selectors: type, class, id, "*", descendant ("A B") and child ("A > B")
    combinators only. A rule using "+", "~", attribute selectors, or any
    ":pseudo-class" is skipped for cascade purposes (never wins a match).
  - no "!important", no <style> media queries or other @-rules (stripped
    before parsing).
  - colors must be hex (#rgb/#rrggbb, resolved through var(--token) chains)
    or one of a small set of named CSS colors; rgb()/hsl()/etc. are not
    understood, and an element using one is silently skipped for contrast.
  - lengths: pt, px, rem, em, and % are converted to points; em is treated
    as relative to the resolved root font size rather than the parent's
    (a simplification -- true em inheritance would need a full cascade).

Usage:
    python3 check_brief_design.py path/to/brief.html [--json]

Exit codes: 0 = every rule passed, 1 = at least one rule failed,
2 = the file could not be read or parsed.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from dataclasses import dataclass, field
from html.parser import HTMLParser

VOID_ELEMENTS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}
HEADING_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6"}
TEXT_BEARING_TAGS = {
    "p", "span", "div", "li", "td", "th", "h1", "h2", "h3", "h4", "h5", "h6",
    "a", "figcaption", "label", "button", "dt", "dd", "caption", "summary",
    "blockquote", "strong", "em", "b", "i", "small", "legend",
}
NUMERIC_RE = re.compile(r"^\(?-?\$?\d[\d,]*(\.\d+)?%?\)?$")
STATUS_CLASS_RE = re.compile(r"^status-[\w-]+$")
HEX_RE = re.compile(r"#[0-9a-fA-F]{3,6}\b")
NAMED_COLORS = {
    "white": "#ffffff", "black": "#000000", "red": "#ff0000", "green": "#008000",
    "blue": "#0000ff", "gray": "#808080", "grey": "#808080", "silver": "#c0c0c0",
    "yellow": "#ffff00", "orange": "#ffa500", "purple": "#800080", "navy": "#000080",
    "teal": "#008080", "maroon": "#800000", "olive": "#808000", "lime": "#00ff00",
    "aqua": "#00ffff", "fuchsia": "#ff00ff",
}


# --------------------------------------------------------------------------
# Minimal HTML tree
# --------------------------------------------------------------------------

class Node:
    __slots__ = ("tag", "attrs", "content", "parent")

    def __init__(self, tag, attrs):
        self.tag = tag
        self.attrs = dict(attrs)
        self.content = []  # list[str | Node]
        self.parent = None

    def text(self):
        parts = []
        for item in self.content:
            parts.append(item if isinstance(item, str) else item.text())
        return "".join(parts)

    def own_text(self):
        return "".join(item for item in self.content if isinstance(item, str))

    def classes(self):
        return self.attrs.get("class", "").split()

    def is_descendant_of(self, ancestor_tag):
        p = self.parent
        while p is not None:
            if p.tag == ancestor_tag:
                return True
            p = p.parent
        return False


def walk(node):
    for item in node.content:
        if isinstance(item, Node):
            yield item
            yield from walk(item)


class TreeBuilder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root", {})
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        node.parent = self.stack[-1]
        self.stack[-1].content.append(node)
        if tag not in VOID_ELEMENTS:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        self.stack[-1].content.append(data)


# --------------------------------------------------------------------------
# CSS parsing: flat declaration blocks, resolved against :root tokens
# --------------------------------------------------------------------------

def extract_style_block(html_text):
    m = re.search(r"<style[^>]*>(.*?)</style>", html_text, re.DOTALL | re.IGNORECASE)
    return m.group(1) if m else ""


def parse_root_tokens(css_text):
    tokens = {}
    m = re.search(r":root\s*\{([^}]*)\}", css_text, re.DOTALL)
    if not m:
        return tokens
    for decl in m.group(1).split(";"):
        decl = decl.strip()
        if not decl or ":" not in decl:
            continue
        prop, _, value = decl.partition(":")
        prop = prop.strip()
        if prop.startswith("--"):
            tokens[prop] = value.strip()
    return tokens


def resolve_value(value, tokens, _depth=0):
    if _depth > 10:
        return value
    m = re.match(r"var\(\s*(--[\w-]+)\s*(?:,\s*(.*))?\)", value.strip())
    if not m:
        return value
    name, fallback = m.group(1), m.group(2)
    if name in tokens:
        return resolve_value(tokens[name], tokens, _depth + 1)
    if fallback:
        return resolve_value(fallback.strip(), tokens, _depth + 1)
    return value


def parse_rules(css_text, tokens):
    """Flat, source-order list of (selector_text, {prop: resolved_value}).

    No nesting, no nested nesting of @-rules -- @media/@keyframes/etc. are
    stripped first, so a rule inside one is simply absent, not misparsed.
    A plain-color `background` shorthand is also exposed as
    `background-color` so ordinary shorthand usage still resolves.
    """
    body = re.sub(r":root\s*\{[^}]*\}", "", css_text, flags=re.DOTALL)
    body = re.sub(r"@[^{;]*\{(?:[^{}]|\{[^{}]*\})*\}", "", body, flags=re.DOTALL)
    rules = []
    for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", body, re.DOTALL):
        selector = m.group(1).strip()
        rules.append((selector, _parse_declarations(m.group(2), tokens)))
    return rules


def _parse_declarations(decl_text, tokens):
    decls = {}
    for decl in decl_text.split(";"):
        decl = decl.strip()
        if not decl or ":" not in decl:
            continue
        prop, _, value = decl.partition(":")
        decls[prop.strip()] = resolve_value(value.strip(), tokens)
    if "background-color" not in decls and "background" in decls:
        bg_value = decls["background"].strip()
        if re.match(r"^#[0-9a-fA-F]{3,6}$", bg_value):
            decls["background-color"] = bg_value
    return decls


def parse_inline_style(style_attr, tokens):
    """A node's own style="..." attribute, parsed the same way as a stylesheet
    declaration block. Inline styles win over every stylesheet rule regardless
    of specificity (real CSS semantics, minus !important), so computed_property
    checks these before matching any <style> rule."""
    if not style_attr:
        return {}
    return _parse_declarations(style_attr, tokens)


# --------------------------------------------------------------------------
# Simplified selector matching, specificity, and cascade resolution
# --------------------------------------------------------------------------

def tokenize_selector(selector_part):
    s = re.sub(r"\s*>\s*", " > ", selector_part.strip())
    return [tok for tok in s.split(" ") if tok]


_COMPOUND_RE = re.compile(r"^([a-zA-Z][\w-]*|\*)?((?:\.[\w-]+)*)((?:#[\w-]+)?)$")


def compound_matches(token, node):
    if ":" in token or "[" in token:
        return False  # pseudo-classes / attribute selectors: not matched, documented limitation
    m = _COMPOUND_RE.match(token)
    if not m:
        return False
    tag, classes_str, id_str = m.groups()
    if tag and tag != "*" and node.tag != tag:
        return False
    if id_str and node.attrs.get("id") != id_str[1:]:
        return False
    if classes_str:
        required = re.findall(r"\.([\w-]+)", classes_str)
        node_classes = set(node.classes())
        if not all(c in node_classes for c in required):
            return False
    return True


def selector_matches_node(tokens, node):
    if not tokens or "+" in tokens or "~" in tokens:
        return False
    if not compound_matches(tokens[-1], node):
        return False
    i = len(tokens) - 2
    current = node
    while i >= 0:
        if tokens[i] == ">":
            i -= 1
            if i < 0:
                return False
            current = current.parent
            if current is None or not compound_matches(tokens[i], current):
                return False
            i -= 1
        else:
            tok = tokens[i]
            current = current.parent
            found = False
            while current is not None:
                if compound_matches(tok, current):
                    found = True
                    break
                current = current.parent
            if not found:
                return False
            i -= 1
    return True


def specificity(selector_part):
    ids = len(re.findall(r"#[\w-]+", selector_part))
    classes = len(re.findall(r"\.[\w-]+", selector_part))
    types = len(re.findall(r"(?:^|[\s>])([a-zA-Z][\w-]*)", selector_part))
    return (ids, classes, types)


def computed_property(node, rules, css_tokens, prop, default=None, cache=None):
    """The cascade-resolved value of `prop` on `node`: its own inline
    style="..." if set (inline always wins, matching real CSS semantics
    minus !important), else the highest-specificity/latest-in-source
    matching stylesheet rule, else the same lookup on the parent (covers
    both true CSS inheritance, e.g. color, and "shows through a transparent
    element" for background-color), else `default`."""
    if cache is None:
        cache = {}
    chain = []
    current = node
    while current is not None:
        key = (id(current), prop)
        if key in cache:
            result = cache[key]
            break
        chain.append(current)
        inline_decls = parse_inline_style(current.attrs.get("style", ""), css_tokens)
        if prop in inline_decls:
            result = inline_decls[prop]
            break
        best = None
        for order_index, (selector, decls) in enumerate(rules):
            if prop not in decls:
                continue
            for part in selector.split(","):
                part = part.strip()
                if not part or ":" in part or "[" in part:
                    continue
                sel_tokens = tokenize_selector(part)
                if sel_tokens and selector_matches_node(sel_tokens, current):
                    rank = (specificity(part), order_index)
                    if best is None or rank >= best[0]:
                        best = (rank, decls[prop])
                    break
        if best is not None:
            result = best[1]
            break
        current = current.parent
    else:
        result = default
    for n in reversed(chain):
        cache[(id(n), prop)] = result
    return result


# --------------------------------------------------------------------------
# Units and color math
# --------------------------------------------------------------------------

_LENGTH_RE = re.compile(r"^(-?[\d.]+)\s*(pt|px|rem|em|%)$")


def parse_length_to_px(value, root_px=16.0):
    if not value:
        return None
    m = _LENGTH_RE.match(value.strip())
    if not m:
        return None
    num, unit = float(m.group(1)), m.group(2)
    if unit == "px":
        return num
    if unit == "pt":
        return num * 96.0 / 72.0
    if unit in ("rem", "em"):  # em treated as relative to root -- see module docstring
        return num * root_px
    if unit == "%":
        return (num / 100.0) * root_px
    return None


def px_to_pt(px):
    return px * 72.0 / 96.0


def resolve_root_px(rules):
    for selector, decls in rules:
        parts = [p.strip() for p in selector.split(",")]
        if "html" in parts and "font-size" in decls:
            px = parse_length_to_px(decls["font-size"], root_px=16.0)
            if px is not None:
                return px
    return 16.0


def normalize_hex(value):
    h = value.strip().lstrip("#").lower()
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return "#" + h


def hex_to_rgb(value):
    m = HEX_RE.search(value or "")
    if not m:
        return None
    h = m.group(0).lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        return None
    try:
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    except ValueError:
        return None


def resolve_color_to_rgb(value):
    if not value:
        return None
    named = NAMED_COLORS.get(value.strip().lower())
    if named:
        return hex_to_rgb(named)
    return hex_to_rgb(value)


def relative_luminance(rgb):
    def channel(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = rgb
    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)


def contrast_ratio(fg_value, bg_value):
    fg, bg = resolve_color_to_rgb(fg_value), resolve_color_to_rgb(bg_value)
    if fg is None or bg is None:
        return None
    l1, l2 = relative_luminance(fg), relative_luminance(bg)
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def is_grayscale(hex_value, tolerance=8):
    rgb = hex_to_rgb(hex_value)
    if rgb is None:
        return False
    return max(rgb) - min(rgb) <= tolerance


def is_large_text(font_size, font_weight, root_px=16.0):
    px = parse_length_to_px(font_size, root_px=root_px) if font_size else None
    if px is None:
        return False
    pt = px_to_pt(px)
    bold = bool(font_weight) and font_weight.strip() in ("bold", "bolder", "700", "800", "900")
    return pt >= 18 or (pt >= 14 and bold)


# --------------------------------------------------------------------------
# Rule results
# --------------------------------------------------------------------------

@dataclass
class RuleResult:
    rule_id: str
    title: str
    passed: bool
    details: list = field(default_factory=list)


# --------------------------------------------------------------------------
# Individual rules (DES-1 .. DES-13)
# --------------------------------------------------------------------------

def get_pages(root, all_nodes):
    """A multi-page artifact (five-page paper, long-form report) wraps each
    page in an element with class="page", each carrying its own message-
    headline <h1> -- the guide's multi-page architectures call for one
    sentence headline per page, not one for the whole document. A one-page
    brief needs no such wrapper: with no class="page" element present, the
    whole document is treated as a single implicit page, so the one-page
    convention keeps working unchanged."""
    pages = [n for n in all_nodes if "page" in n.classes()]
    return pages if pages else [root]


def check_heading_hierarchy(root, all_nodes):
    details = []
    for page in get_pages(root, all_nodes):
        label = "the document" if page is root else f"page {page.attrs.get('id') or '(unlabeled)'}"
        headings = [n for n in walk(page) if n.tag in HEADING_TAGS]
        h1_count = sum(1 for h in headings if h.tag == "h1")
        if h1_count != 1:
            details.append(f"{label}: expected exactly one <h1>, found {h1_count}")
        seen_max = 0
        for h in headings:
            level = int(h.tag[1])
            if level > seen_max + 1:
                snippet = h.text().strip()[:40]
                details.append(f"{label}: <{h.tag}> ({snippet!r}) follows level {seen_max} with no intervening <h{seen_max + 1}>")
            seen_max = max(seen_max, level)
    return RuleResult("DES-1", 'Each page (class="page", or the whole document if there is none) has exactly one <h1> and no skipped heading levels', not details, details)


def check_sentence_case_headings(all_nodes):
    details = []
    for h in [n for n in all_nodes if n.tag in HEADING_TAGS]:
        text = h.text().strip()
        letters = re.sub(r"[^A-Za-z]", "", text)
        if len(text.split()) > 3 and letters and letters.isupper():
            details.append(f"<{h.tag}> is set in all caps: {text[:50]!r}")
    return RuleResult("DES-2", "Headings use sentence case (short labels may be capitals)", not details, details)


def check_alt_text(all_nodes):
    details = []
    for img in [n for n in all_nodes if n.tag == "img"]:
        if not img.attrs.get("alt", "").strip():
            details.append(f"<img src={img.attrs.get('src', '(no src)')!r}> has no non-empty alt text")
    return RuleResult("DES-3", "Every image has non-empty alt text", not details, details)


def check_contrast(all_nodes, rules, css_tokens, root_px):
    cache = {}
    seen = {}
    for n in all_nodes:
        if n.tag not in TEXT_BEARING_TAGS or not n.own_text().strip():
            continue
        color = computed_property(n, rules, css_tokens, "color", "#000000", cache)
        bg = computed_property(n, rules, css_tokens, "background-color", "#ffffff", cache)
        ratio = contrast_ratio(color, bg)
        if ratio is None:
            continue
        font_size = computed_property(n, rules, css_tokens, "font-size", None, cache)
        font_weight = computed_property(n, rules, css_tokens, "font-weight", None, cache)
        large = is_large_text(font_size, font_weight, root_px)
        threshold = 3.0 if large else 4.5
        key = (color.strip().lower(), bg.strip().lower(), large)
        entry = seen.setdefault(key, {"ratio": ratio, "threshold": threshold, "count": 0, "tag": n.tag, "example": n.own_text().strip()[:40]})
        entry["count"] += 1
    details = []
    for (color, bg, large), info in sorted(seen.items(), key=lambda kv: kv[1]["ratio"]):
        if info["ratio"] < info["threshold"]:
            note = " (large text)" if large else ""
            plural = "s" if info["count"] != 1 else ""
            details.append(
                f"{color} on {bg} is {info['ratio']:.2f}:1, below {info['threshold']:.1f}:1{note}"
                f" -- {info['count']} element{plural}, e.g. <{info['tag']}> {info['example']!r}"
            )
    return RuleResult("DES-4", "Text/background pairs meet WCAG contrast (4.5:1, or 3:1 for large text)", not details, details)


def is_anchor_selector(selector_part):
    part = selector_part.strip()
    if not part:
        return False
    return bool(re.search(r"(?:^|[\s>+~])a(?:[.:#][\w-]+)*$", part))


def check_underline(rules):
    details = []
    for selector, decls in rules:
        if "underline" not in decls.get("text-decoration", ""):
            continue
        parts = [p.strip() for p in selector.split(",")]
        if not all(is_anchor_selector(p) for p in parts):
            details.append(f"'{selector}' declares text-decoration: underline but is not a link selector")
    return RuleResult("DES-5", "Underline is reserved for links", not details, details)


def check_tables(all_nodes):
    align_details = []
    header_details = []
    tables = [n for n in all_nodes if n.tag == "table"]
    for i, table in enumerate(tables, start=1):
        label = table.attrs.get("id") or f"table #{i}"
        has_header = any(
            n.tag == "thead" and any(c.tag == "th" for c in walk(n))
            for n in walk(table)
        )
        if not has_header:
            header_details.append(f"{label} has no <thead> with <th> header cells")

        body_rows = [n for n in walk(table) if n.tag == "tr" and not n.is_descendant_of("thead")]
        columns = {}
        for row in body_rows:
            cells = [c for c in row.content if isinstance(c, Node) and c.tag in ("td", "th")]
            for idx, cell in enumerate(cells):
                columns.setdefault(idx, []).append(cell)
        for idx, cells in columns.items():
            texts = [(c, c.text().strip()) for c in cells]
            nonempty = [(c, t) for c, t in texts if t]
            if not nonempty:
                continue
            numeric = [t for _, t in nonempty if NUMERIC_RE.match(t)]
            if len(numeric) / len(nonempty) >= 0.6:
                missing = [c for c, t in nonempty if "num" not in c.classes()]
                if missing:
                    align_details.append(
                        f"{label} column {idx + 1} is numeric but {len(missing)} of {len(nonempty)} cell(s) lack class=\"num\""
                    )
    return (
        RuleResult("DES-6", "Numeric table columns are marked for right alignment (class=\"num\")", not align_details, align_details),
        RuleResult("DES-7", "Every table has a <thead> with <th> header cells", not header_details, header_details),
    )


def check_charts(all_nodes):
    spec_details = []
    axis_details = []
    charts = [n for n in all_nodes if "chart" in n.classes()]
    for i, chart in enumerate(charts, start=1):
        label = chart.attrs.get("id") or f"chart #{i}"
        raw = chart.attrs.get("data-chart-spec")
        if not raw:
            spec_details.append(f"{label} has no data-chart-spec attribute")
            continue
        try:
            spec = json.loads(raw)
        except json.JSONDecodeError as exc:
            spec_details.append(f"{label} data-chart-spec is not valid JSON ({exc})")
            continue
        for f in ("title", "source", "evidenceState"):
            if not str(spec.get(f, "")).strip():
                spec_details.append(f"{label} spec is missing non-empty '{f}'")
        if spec.get("type") == "bar":
            axis = spec.get("axis") or {}
            justified = str(axis.get("brokenAxisJustified", "")).strip()
            if axis.get("start") != 0 and not justified:
                axis_details.append(f"{label} is a bar chart whose axis does not start at 0 and has no brokenAxisJustified explanation")
    return (
        RuleResult("DES-8", "Every chart has a complete data-chart-spec (title, source, evidenceState)", not spec_details, spec_details),
        RuleResult("DES-9", "Bar chart axes start at zero unless explicitly justified", not axis_details, axis_details),
    )


def check_status_text(all_nodes):
    details = []
    for n in all_nodes:
        if any(STATUS_CLASS_RE.match(c) for c in n.classes()) and not n.text().strip():
            details.append(f"<{n.tag} class={n.attrs.get('class')!r}> conveys status by color alone (no visible text)")
    return RuleResult("DES-10", "Status indicators carry visible text, not color alone", not details, details)


def check_body_font_size(all_nodes, rules, css_tokens, root_px):
    details = []
    body_node = next((n for n in all_nodes if n.tag == "body"), None)
    if body_node is None:
        details.append("no <body> element found")
        return RuleResult("DES-11", "Body text is set 10-12pt", False, details)
    value = computed_property(body_node, rules, css_tokens, "font-size", None)
    if value is None:
        details.append("no font-size resolves for <body> (declare one on body, html, or a rule that matches it)")
    else:
        px = parse_length_to_px(value, root_px=root_px)
        if px is None:
            details.append(f"body font-size {value!r} uses an unsupported unit (use pt, px, rem, em, or %)")
        else:
            pt = px_to_pt(px)
            if not (10 - 1e-6 <= pt <= 12 + 1e-6):
                details.append(f"body font-size resolves to {pt:.1f}pt ({value}), outside the 10-12pt range")
    return RuleResult("DES-11", "Body text is set 10-12pt (pt, px, rem, em, or % all accepted)", not details, details)


def check_footer(all_nodes):
    footers = [n for n in all_nodes if n.tag == "footer" or n.attrs.get("id") == "source-line"]
    details = []
    if not footers:
        details.append('no <footer> or id="source-line" element found')
    else:
        text = " ".join(f.text() for f in footers)
        has_keyword = re.search(r"\b(source|status|as of|cutoff)\b", text, re.IGNORECASE)
        has_date = re.search(r"\d{4}-\d{2}-\d{2}", text)
        if not text.strip():
            details.append("footer/source-line element has no text")
        elif not has_keyword and not has_date:
            details.append("footer/source-line text has no source/status/date marker")
    return RuleResult("DES-12", "A footer names the source and evidence cutoff", not details, details)


def check_palette(tokens, rules, max_colors=6):
    colors = set()
    for value in tokens.values():
        for m in HEX_RE.findall(value):
            colors.add(normalize_hex(m))
    for _, decls in rules:
        for prop in ("color", "background-color", "border-color"):
            if prop in decls:
                for m in HEX_RE.findall(decls[prop]):
                    colors.add(normalize_hex(m))
    nongray = sorted(c for c in colors if not is_grayscale(c))
    details = []
    if len(nongray) > max_colors:
        details.append(f"{len(nongray)} distinct non-grayscale colors declared (max {max_colors}): {', '.join(nongray)}")
    return RuleResult("DES-13", f"Color palette stays within {max_colors} non-grayscale accent colors", not details, details)


# --------------------------------------------------------------------------
# Orchestration
# --------------------------------------------------------------------------

def check(html_text):
    builder = TreeBuilder()
    builder.feed(html_text)
    all_nodes = list(walk(builder.root))

    css_text = extract_style_block(html_text)
    tokens = parse_root_tokens(css_text)
    rules = parse_rules(css_text, tokens)
    root_px = resolve_root_px(rules)

    results = [
        check_heading_hierarchy(builder.root, all_nodes),
        check_sentence_case_headings(all_nodes),
        check_alt_text(all_nodes),
        check_contrast(all_nodes, rules, tokens, root_px),
        check_underline(rules),
    ]
    results.extend(check_tables(all_nodes))
    results.extend(check_charts(all_nodes))
    results.append(check_status_text(all_nodes))
    results.append(check_body_font_size(all_nodes, rules, tokens, root_px))
    results.append(check_footer(all_nodes))
    results.append(check_palette(tokens, rules))
    return results


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("path", help="HTML file to check")
    parser.add_argument("--json", action="store_true", help="emit a JSON report instead of text")
    args = parser.parse_args(argv)

    path = pathlib.Path(args.path)
    if not path.is_file():
        print(f"error: {path} not found", file=sys.stderr)
        return 2
    try:
        html_text = path.read_text(encoding="utf-8")
        results = check(html_text)
    except Exception as exc:  # noqa: BLE001 - report and exit, don't crash the caller
        print(f"error: could not check {path}: {exc}", file=sys.stderr)
        return 2

    all_passed = all(r.passed for r in results)

    if args.json:
        payload = {
            "result": "PASS" if all_passed else "FAIL",
            "rules": [
                {"id": r.rule_id, "title": r.title, "passed": r.passed, "details": r.details}
                for r in results
            ],
        }
        print(json.dumps(payload, indent=2))
    else:
        for r in results:
            print(f"{'PASS' if r.passed else 'FAIL'} {r.rule_id}  {r.title}")
            for d in r.details:
                print(f"     - {d}")
        passed_count = sum(1 for r in results if r.passed)
        print()
        print(f"RESULT: {'PASS' if all_passed else 'FAIL'} ({passed_count}/{len(results)} rules passed)")

    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
