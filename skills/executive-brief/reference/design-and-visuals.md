# Design and visuals

Design gives the argument sequence, relative weight, and navigability. A beautiful page that misstates hierarchy is a reasoning error rendered attractively.

## Choose the artifact for the reading condition

The same analysis should not be poured unchanged into every format.

| Format | Best use | Reader behavior | Design priority |
|---|---|---|---|
| One-page brief | Narrow decision; senior alignment | Scan and discuss | Exact ask, tradeoff, owner |
| Five-page paper | Moderate complexity; pre-read | Selective reading | Narrative continuity, evidence labels |
| Ten-slide deck | Facilitated meeting | Listen and glance | One assertion and visual per slide |
| Long-form report | Durable reference and assurance | Search and revisit | Navigation, definitions, provenance |
| Dashboard | Repeated monitoring | Compare over time | Stable measures, thresholds, exceptions |

A deck is not a paginated report with larger type. A pre-read must stand alone; a live deck can rely on spoken transitions but not to correct a misleading graphic. Create a **content spine** — decision, motivation, mechanism, evidence, options, uncertainty, next step — then adapt expression to the medium; this preserves meaning without forcing identical pages. If the artifact will circulate beyond the meeting, design for the absent presenter: definitions, sources, qualifications, and status labels must survive forwarding and screenshotting. Format templates live in [templates.md](templates.md).

## Create a visible hierarchy

A reader should identify page purpose, governing claim, evidence, and qualification before reading prose. Use four consistent levels: (1) page title or message headline, (2) lead sentence or decision statement, (3) evidence modules — paragraphs, chart, table, or diagram, (4) source and qualification notes.

Alignment is a stronger organizer than decoration — use a stable grid, consistent left edge, intentional column widths, repeated spacing. Proximity should indicate relationship: the caveat sits near the claim, the label near the value, the source near the figure. Whitespace is not unused space; it separates semantic groups and makes priority visible — add content only if it changes understanding or action. Avoid a wall of equally weighted cards: card grids make every item look equivalent and force the reader to invent sequence. Use them only for genuinely parallel categories; for an argument, use a clear top-to-bottom path.

## Use typography to reduce search

Typography should signal hierarchy with as few variables as possible.

- Use one highly legible family, or a restrained two-family system.
- Use size, weight, and spacing before introducing many colors.
- Keep body text around 10–12 points in print, depending on typeface and measure.
- Use sentence case; reserve all caps for short labels.
- Keep line length moderate and left alignment consistent.
- Use tabular numerals in financial and comparison tables.
- Avoid underlining except for links.
- Make source notes readable — if a qualification matters, it cannot be microscopic.

Use bold to expose structure, not to create a second hidden document inside every paragraph — a page where half the text is bold has no hierarchy. For tables, align text left and numbers right; align decimals when precision is meaningful; use enough cell padding to separate rows; repeat header rows across pages; avoid vertical text and diagonal labels. Test the exported PDF at normal zoom, not only in the authoring application — fonts can substitute, lines can reflow, footnotes can become unreadable after rendering.

## Use color as a secondary channel

Color should encode status, category, or emphasis only when the same meaning is also available through label, position, pattern, or shape (WCAG 2.2: color must not be the sole means of conveying information).

- Use a neutral foundation and one primary accent.
- Reserve alert colors for actual alert meaning.
- Do not use red and green alone for bad and good.
- Keep category colors stable across pages.
- Use direct labels so legends are not the only key.
- Check contrast in grayscale and under common color-vision simulations.
- Avoid saturated backgrounds behind long text.

For text, aim for at least **4.5:1 contrast**; large text (≥18pt, or ≥14pt bold) may use **3:1**. For lines, icons, and graphical controls, maintain sufficient non-text contrast (3:1). Accessibility improves executive usability too: alt text forces the author to state the visual's intended takeaway, horizontal labels reduce decoding, consistent navigation helps readers find assurance quickly, and a chart that remains intelligible without hue is more robust in print, projection, and screenshotting.

**Using an organization's real brand, not a placeholder.** The tokens and palette in this skill's HTML template are a neutral placeholder, meant to be swapped for whichever brand the brief actually belongs to — never invent a palette when an authoritative one exists. If a dedicated brand-system skill or design-tokens source is available in the environment (for RealAdvice specifically, the `realadvice-brand-system` skill has the reconciled color/type/logo facts, and `design-tokens` can install them as CSS custom properties), pull the real hex values and font stack from there rather than re-deriving them from a brand PDF or asset folder by hand — a brand guide's own tables can disagree with themselves (a transcribed hex that doesn't match its stated RGB, for instance), and a dedicated, already-reconciled skill is a more reliable source than a fresh read of the source document. Whichever palette is used, real or placeholder, the checker's WCAG contrast and palette-restraint rules still apply exactly as written above — a brand color that fails 4.5:1 is still a real accessibility problem, not an exception.

## Choose a graphic by the question

Don't begin with "which chart looks impressive?" Begin with the relationship the reader must see.

| Question | Strong default | Use with care |
|---|---|---|
| Which is larger? | Sorted horizontal bar or dot plot | Pie, bubble, area |
| How did it change over time? | Line chart | Bars for many series |
| How far from target? | Dot or bar with reference line | Gauge |
| What is the distribution? | Histogram, box, strip, interval plot | Average alone |
| How do two measures relate? | Scatterplot | Dual-axis chart |
| What composes the whole? | Stacked bar; simple pie for few categories | Treemap for close comparison |
| Where does work or risk flow? | Process diagram, Sankey when volume matters | Decorative arrows |
| What is exact? | Table | Chart with many value labels |

Judgments based on position along a common scale are generally more accurate than judgments of angle or area — use bars and dots when exact comparison matters; don't ask executives to compare bubble areas for a funding decision.

## Give every chart a complete argument

A decision-grade chart needs more than marks on axes. Include: a message title stating the main pattern; a subtitle with measure, population, geography/scope, and time period; labeled axes and units; a meaningful comparator, target, or reference line when relevant; concise annotations placed near the data; evidence-state and uncertainty notes; a specific source and cutoff date; an accessible description or underlying table.

Start quantitative axes at zero for bars unless a break is clearly signaled and justified. For lines, a nonzero range may be appropriate, but make the scale honest and visible. Avoid 3D, shadows, heavy gridlines, and needless markers. Make titles describe the finding, not the topic: "Exceptions by month" becomes "Exceptions doubled after the policy change, then stabilized" — and if the evidence can't support that causal implication, write "Exceptions doubled after the policy change; the chart does not establish why."

## Show uncertainty only when it changes interpretation

Uncertainty can improve accuracy and still harm comprehension if it answers a question the reader isn't asking. Choose the display by decision need:

| Decision need | Useful display |
|---|---|
| Compare estimates whose ranges overlap | Dot-and-interval plot |
| Show forecast or scenario path | Line with shaded range |
| Test a threshold | Estimate and interval against reference line |
| Show outcome distribution | Histogram or quantile plot |
| Show assumption influence | Ranked sensitivity bars |
| Show discrete futures | Small-multiple scenarios |

Show uncertainty when it could fundamentally change interpretation; omit it when consistently tiny and immaterial. Prefer shaded bands or range plots over hard-to-read error-bar conventions. Always define what the range is (across samples, seeds, parameter values, scenarios, or posterior uncertainty) — two ranges in one cell (seed variability and parameter bands) can be truthful and unreadable; prefer a main visual for the decision-relevant range and a separate assurance table for the rest. If uncertainty is so large that no comparison is meaningful, the honest graphic may be a scenario table or a statement that the evidence does not support ranking.

## Use tables for exact lookup and multidimensional comparison

Tables are often the right executive visual when exact values, definitions, or several attributes matter simultaneously.

- Put the comparison dimension in columns and the items in rows.
- Order rows by decision priority, magnitude, or natural sequence.
- Keep units in headers rather than repeating them in every cell.
- Align numbers right and text left.
- Use restrained row shading and visible but light borders.
- Highlight one or two decision-relevant cells; don't heat-map everything.
- Explain blanks, zeros, dashes, and "not applicable."
- Do not mix denominators silently.

Replace a massive evidence table on the executive surface with a summary table plus a linked appendix. A useful hybrid is a **chart-table**: a small bar or dot for pattern plus an aligned value column for precision — use it only if rendering stays sharp and accessible. For risk registers, don't present 200 rows as if senior attention should be uniform; show the portfolio pattern, decision tiers, uncovered items, unstable rankings, and owner gaps, and retain the complete register in assurance.

## Use diagrams for structure, sequence, and dependency

Diagrams are strongest when they reduce search by placing related elements together, and weakest when they decorate a simple list with boxes and arrows.

- **Process diagrams** for sequence, handoffs, gates, and loops.
- **System diagrams** for boundaries, interfaces, and data movement.
- **Decision trees** for conditional policy or escalation.
- **State diagrams** for status changes and invalidation.
- **Roadmaps** for time, dependencies, and release stages.
- **Swimlanes** for ownership across functions.

Keep the diagram's question in the title. Use a stable reading direction, limit crossing lines, label arrows with actions (not merely connections), and make the exception path visible when it's the source of risk. Distinguish current, committed, and proposed states through both style and label. Don't use a large architecture diagram as a test of audience seriousness — create an executive view with only the components needed to explain consequence, and link to the engineering view.

## The HTML authoring convention

Typography, color, chart construction, and table formatting are the part of this guide that can be checked by code instead of judgment — `scripts/check_brief_design.py` does that for any brief authored as a **self-contained HTML file** that follows this convention. The convention is deliberately simple (flat CSS, presentational classes, no nesting or cascade tricks) so a small script can check it without a real browser, and it applies the same way to a one-page brief, a five-page paper, or a long-form report — the difference is only whether the document is one implicit page or several explicit ones (see **Pages**, below). Start from [assets/one-page-brief-template.html](assets/one-page-brief-template.html) for a single-page brief, or [assets/five-page-brief-template.html](assets/five-page-brief-template.html) for a short multi-page report; both already follow it.

- **Design tokens.** Declare colors as custom properties in a single `:root { --name: #hex; ... }` block inside one `<style>` element. Reference them elsewhere with `var(--name)`.
- **Contrast pairs.** Any CSS rule where contrast matters must declare `color` and `background-color` together in the *same* rule (resolve to hex, don't split them across a cascade the checker can't resolve). Add `font-size` (in `pt`) and `font-weight` on that rule if the text qualifies for the WCAG large-text exception (≥18pt, or ≥14pt and bold).
- **Body text size.** Declare the base size on `body { font-size: <N>pt; }` with `N` between 10 and 12 — one size for the whole document, however many pages it has.
- **Pages.** A one-page brief needs no special markup — the whole document is treated as a single implicit page. A multi-page artifact (five-page paper, long-form report) wraps each page in its own top-level `<section class="page" id="...">` (siblings, not nested), matching the guide's "each page answers one executive question" — each page then carries its own message-headline `<h1>`, checked independently.
- **Headings.** Within each page (the whole document, or each `class="page"` section — see **Pages**), exactly one `<h1>`; never skip a level (an `<h3>` needs an `<h2>` before it somewhere earlier in that same page); sentence case (only short labels of three words or fewer may be set in capitals).
- **Links.** Only anchor-related selectors (`a`, `a:hover`, `a:visited`, `a:focus`) may declare `text-decoration: underline`.
- **Images and SVGs.** Every `<img>` carries an `alt` that states the takeaway; a purely decorative image gets `alt=""` *and* `role="presentation"` (or `aria-hidden="true"`) so the choice is explicit. Every inline `<svg>` that isn't `aria-hidden="true"` has an accessible name — a `<title>` child (pair it with `aria-labelledby`), or `aria-label`.
- **Tables.** Every `<table>` has a `<thead>` with at least one `<th>`. Give numeric columns' `<td>` cells `class="num"` (paired with a `.num { text-align: right; font-variant-numeric: tabular-nums; }` rule); leave text columns unclassed for left alignment.
- **Charts.** Wrap each chart in an element carrying `class="chart"` with a `data-chart-spec` attribute holding a JSON object with non-empty `title`, `source`, and `evidenceState` strings. For `"type": "bar"`, set `"axis": {"start": 0}` unless the break is deliberate, in which case set `"axis": {"brokenAxisJustified": "<why>"}` with a real explanation.
- **Status indicators.** Any element whose class matches `status-*` must carry non-empty visible text — never a colored dot alone.
- **Source line.** End the document with a `<footer>` (or an element `id="source-line"`) naming the source and evidence cutoff — one is enough for the whole document, however many pages it has; the guide's own advice is to repeat only the status labels a page needs to avoid being misread in isolation, not the full source line on every page.
- **Palette restraint.** Keep the document to at most six distinct accent *hue families* across the `<style>` block, `--` custom properties, and inline styles. Tints and shades of one hue count as one family (a purple ramp for severity is one accent, not four), and grayscale is the neutral foundation, not an accent — so the budget is genuinely about how many different hues compete for attention.

Run the checker after producing or editing the file:

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/check_brief_design.py" path/to/brief.html
```

It reports one `PASS`/`FAIL` line per rule and exits non-zero if anything fails. It intentionally does not attempt the judgment calls in the rest of this file — whether a chart title states a finding, whether a comparator is the *right* one, whether a diagram's reading direction is genuinely stable. Those stay reviewed by a person (or by Claude reading this guide), not by the script.
