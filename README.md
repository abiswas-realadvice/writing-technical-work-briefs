# writing-technical-work-briefs

A field guide for turning dense technical work into decision-ready executive briefs, packaged as a Claude Code skill and plugin — `technical-work-briefs` — with a deterministic checker for the parts of the guide that are objectively, mechanically checkable.

## What's here

```text
field-guide/           the source document (docx + pdf, same content)
.claude-plugin/        plugin.json + marketplace.json — this repo installs as a plugin
skills/executive-brief/
  SKILL.md             entry point: workflow, principles, quick reference
  reference/           8 files distilling the guide (argument, evidence, language,
                        design, domain patterns, production/review, templates, rubric)
  assets/               working HTML templates: one-page brief and five-page paper
  scripts/              check_brief_design.py — the deterministic design checker
tests/                  unit tests for the checker (fixtures + unittest, zero deps, zero cost)
evals/                  claude plugin eval suite (exercises the skill live; costs a model call)
```

### The source document

`field-guide/Technical-Work-Executive-Decisions.{docx,pdf}` is a 94-page field guide — the same content in two formats. `skills/executive-brief/reference/` distills its operative content (tables, rules, templates, checklists, examples) into eight topic files; go back to the source document for full narrative context, citations, or anything that reads as compressed.

### The skill

`skills/executive-brief/SKILL.md` teaches Claude to write or review an executive brief: name the decision, choose the right artifact, build the argument (page-one contract, message headlines, motivation, options), label evidence state and uncertainty honestly, write with precision (modal verbs, jargon, caveat placement), apply a domain pattern if one fits (architecture, AI/data, simulation, risk, workflows, workforce), and design the reading experience — then self-check against the bundled checklist and 100-point rubric before calling it done.

### The deterministic design checker

Typography, color contrast, chart construction, and table formatting are the part of the guide that can be checked by code instead of judgment. When the skill produces a brief as a self-contained HTML file (following the authoring convention in [`reference/design-and-visuals.md`](skills/executive-brief/reference/design-and-visuals.md#the-html-authoring-convention)), it runs:

```bash
python3 skills/executive-brief/scripts/check_brief_design.py path/to/brief.html
```

It checks 13 rules — WCAG contrast ratios, heading hierarchy, accessible names for images and inline SVGs, table header rows and numeric alignment, chart-spec completeness, zero-baseline bar axes, color-alone status encoding, body text size, a source/status footer, and palette restraint (counted as accent *hue families*, so a brand's tint ramp is one color, not five) — and exits non-zero if anything fails. It does **not** try to check the things that need judgment (whether a headline states the right claim, whether a causal verb matches the evidence); those stay with the reference files, the checklist, and the rubric.

It's built for real-world HTML, not just its own templates: it reads every `<style>` block, strips comments and `@import` lines, resolves a simplified CSS cascade (inline styles, specificity, inheritance, `:root` resets, `rem`/`px`/`%` units), and applies HTML's implied-end-tag rules so markup that omits `</td>` or `</li>` still parses into the right structure. The limits of that simplification are documented at the top of the script.

This isn't one-pager-only. The heading-hierarchy rule is page-aware: with no `class="page"` element, the whole document is one implicit page (a one-page brief); with one or more `<section class="page">` elements, each is checked independently for its own message-headline `<h1>` and heading order, which is how the guide's five-page paper and long-form report architectures actually work — one sentence headline per page, not one for the whole artifact. `skills/executive-brief/assets/one-page-brief-template.html` and `skills/executive-brief/assets/five-page-brief-template.html` both follow the convention and pass every check.

## Tests

Two different things are both called "tests" here, deliberately kept separate:

**`tests/` — the actual deterministic test suite.** Zero dependencies (Python stdlib only), zero network access, zero API cost, runs in milliseconds. It proves the checker script is correct: both real templates (one-page and five-page) and two `good-*` fixtures of ordinary real-world CSS must pass every rule, and fourteen `bad-*` fixtures each deliberately violate exactly one rule (or, for the multi-page case, a rule scoped to one specific page) and must trip it. It runs in CI on every push and pull request ([`.github/workflows/tests.yml`](.github/workflows/tests.yml)) across Python 3.10–3.13.

```bash
python3 -m unittest discover -s tests -v
# or, if you have pytest:
pytest tests/
```

**`evals/` — a `claude plugin eval` suite.** This exercises the skill live: it prompts Claude (with the plugin loaded) to write a brief and to review one, and grades the results with deterministic graders (`regex`, `tool_used`, `file_exists` — no LLM judge, so grading itself is free). Unlike `tests/`, each run costs a real model call to *generate* the brief being graded, so results aren't as reproducible as `tests/` and it isn't free. Run it from the plugin root once you're ready to spend the API usage:

```bash
claude plugin eval . --allow-tools Write Bash
```

(`--allow-tools Write Bash` is required because a case's own `allowed_tools` frontmatter can only grant read-only tools; `Write` and `Bash` have to come from the command line.) Add `--case writes-one-page-brief --runs 1 --ablation none` while iterating on a single case to keep cost down.

## Installing the plugin

This repo is both the plugin and its own marketplace (`.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json`), so it installs the same way in any project, including this one.

**Try it locally, without installing anything** (loads it for one session):

```bash
claude --plugin-dir /path/to/writing-technical-work-briefs
```

**Install it into another project, at the project level** (shared with everyone who works in that repo), from inside a Claude Code session in that project:

```text
/plugin marketplace add abiswas-realadvice/writing-technical-work-briefs
/plugin install technical-work-briefs@technical-work-briefs
```

Choose **Project** scope when prompted — that writes the enablement to that project's `.claude/settings.json` so it's shared with collaborators. (Use a local path instead of the GitHub shorthand — `/plugin marketplace add /path/to/writing-technical-work-briefs` — if this repo hasn't been pushed yet.)

**Or pre-configure it for a team**, without anyone running the commands above: commit this to the target project's `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "technical-work-briefs": {
      "source": { "source": "github", "repo": "abiswas-realadvice/writing-technical-work-briefs" }
    }
  },
  "enabledPlugins": {
    "technical-work-briefs@technical-work-briefs": true
  }
}
```

Once a collaborator trusts that project's folder, Claude Code registers the marketplace automatically; each person still runs `claude plugin install technical-work-briefs@technical-work-briefs` once themselves (enabling a plugin from an external source in a project's settings doesn't silently install it for everyone — each person's own machine needs the install step).

Either way, the skill activates automatically when a request matches (drafting or reviewing an executive brief, decision memo, or slide deck), or manually via `/technical-work-briefs:executive-brief`.
