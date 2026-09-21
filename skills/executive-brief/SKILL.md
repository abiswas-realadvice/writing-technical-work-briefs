---
name: executive-brief
description: Turns dense technical work (models, architecture, risk registers, simulations, workforce analysis, process/ops studies) into decision-ready executive briefs, memos, pre-reads, and slide decks, and reviews or scores existing briefs for decision-readiness.
when_to_use: Use when writing, drafting, or converting a technical report/analysis into an executive brief, board paper, decision memo, or slide deck; when asked to make something "more executive," "less technical," or "decision-ready"; when structuring a recommendation with options and tradeoffs; when reviewing, auditing, or scoring a draft brief; or when checking a brief's design and accessibility (heading hierarchy, color contrast, chart construction, table formatting).
---

# Executive brief writing and review

Source: `field-guide/Technical-Work-Executive-Decisions.pdf` (also `.docx`), a 94-page field guide this skill distills. Consult the source document directly for nuance, citations, or a passage that feels compressed here.

## The standard

An executive brief is a **decision interface**, not a miniature technical report. It answers: given what we now know, what should this group understand, decide, fund, stop, accept, or monitor? The governing standard is **compression without distortion** — reduce what the reader must hold in mind while preserving the distinctions that could change the decision (observed vs. modeled, correlation vs. causation, committed vs. proposed, coverage vs. effectiveness, workload vs. headcount).

Three qualities must all be present, or the brief is incomplete:

- **Legibility** — the reader can form an accurate mental model quickly.
- **Fidelity** — material qualifications and provenance survive compression.
- **Consequence** — the analysis is arranged around the actual choice in front of the organization, not the order in which the work was performed.

## Workflow

Work through these in order. Each step links to a reference file — read it when you reach that step, not all up front.

1. **Name the decision.** Complete: "At this meeting, we need [decision owner] to decide whether to [action] by [date], because [consequence]." Classify the ask as Decide / Direct / Discuss / Note / Endorse. If you can't complete the sentence, the brief isn't scoped yet. → [reference/argument-and-structure.md](reference/argument-and-structure.md)

2. **Choose the artifact.** One-page brief, five-page paper, ten-slide deck, long-form report, or dashboard — pick by reading condition, not by habit. → [reference/design-and-visuals.md](reference/design-and-visuals.md#choose-the-artifact-for-the-reading-condition), templates in [reference/templates.md](reference/templates.md)

3. **Build the argument.** Page-one contract (message title → decision → why now → three proof points → material uncertainty → next action), sentence headlines that carry logic, motivation only when it changes comprehension, options as real choices, fact/interpretation/recommendation kept separate. → [reference/argument-and-structure.md](reference/argument-and-structure.md)

4. **Build the evidence.** Label every important claim's evidence state (observed / measured / estimated / modeled / assumed / inferred / recommended). Frame every important number (counted what, out of what, over what period, compared with what, produced how, how uncertain). Match causal verbs to the study design. Separate probability from confidence. Separate control coverage from effectiveness. → [reference/evidence-and-uncertainty.md](reference/evidence-and-uncertainty.md)

5. **Write with precision.** Actor + action + evidence + boundary for every consequential sentence. Modal verbs as governance signals (must/will/should/may). Jargon translated, not banned. Caveats placed next to the claim they change, not exiled to an appendix. Workforce and sensitive claims written without implying judgment of people. → [reference/precision-language.md](reference/precision-language.md)

6. **Apply a domain pattern, if one fits.** Architecture/platform, AI/data products, simulation/scenario, risk registers, workflows/operating models, workforce/role design each have a required-elements checklist and a characteristic language trap. → [reference/domain-patterns.md](reference/domain-patterns.md)

7. **Design the reading experience.** Visible hierarchy, restrained typography, WCAG-compliant color and contrast, the right graphic for the question, honest chart construction, tables built for lookup. This is the part with objectively checkable rules — see **Design-element checking** below. → [reference/design-and-visuals.md](reference/design-and-visuals.md)

8. **Self-check before calling it done.** Run the deterministic design checker (below), then walk the final release checklist and, for anything release-bound, the 100-point rubric. Any zero in decision, evidence integrity, or material uncertainty blocks release regardless of total score. → [reference/checklist-and-rubric.md](reference/checklist-and-rubric.md)

## Ten principles (fast recall)

| Principle | Test |
|---|---|
| Decision before document | Can a reader state the decision in one sentence? |
| Concrete before abstract | Is there one real operational example before the framework? |
| Conclusion before chronology | Does page one say what the analysis means now? |
| Business consequence before mechanism | Does each technical claim connect to money, time, risk, capacity, quality, or strategic option value? |
| Evidence state before precision | Can the reader tell what was observed, calculated, modeled, or assumed? |
| Comparator before magnitude | Does every important number have a baseline, target, prior period, or alternative? |
| Caveat at point of use | Is the important limitation visible where the claim is made? |
| One visual, one question | Can the chart's purpose be said aloud in one sentence? |
| Layering instead of deletion | Can a skeptical reader reach the method without forcing everyone through it? |
| Ownership after decision | Are owner, timing, dependencies, and proof of completion explicit? |

Applied together, not in isolation: "be concise" without evidence labels creates false certainty; "show your work" without hierarchy buries the decision; "use plain language" without preserving technical distinctions makes the brief easier to read and less true.

## Quick reference

When a draft is too technical, don't start by deleting detail:

1. Write the decision. 2. Write the motivation in four sentences. 3. Choose one operational example. 4. Draw the translation chain (mechanism → operational behavior → business consequence → decision). 5. Label every important claim by evidence state. 6. Add comparator, denominator, time, and uncertainty. 7. Build the options table. 8. Put the material caveat beside the conclusion. 9. Move method and inventory to assurance. 10. Rewrite headings as assertions. 11. Choose each visual by the question. 12. Separate control coverage from effectiveness. 13. Separate role value from headcount and people from process. 14. Give the artifact independent publication identity. 15. Inspect the rendered file and rehearse the decision.

## Design-element checking

Typography, color, contrast, chart construction, and table formatting are the part of this guide that can be checked by code instead of judgment. When you produce a brief as a **self-contained HTML file** (the required format for anything where visual design matters — a one-page brief, five-page paper, or slide deck), run the bundled checker against it before calling the work done:

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/check_brief_design.py" path/to/brief.html
```

It checks WCAG contrast ratios, heading hierarchy, alt text, table alignment, chart-spec completeness (including zero-baseline bar axes), color-alone status encoding, body text size, source/status footer presence, and color palette restraint — see [reference/design-and-visuals.md](reference/design-and-visuals.md#the-html-authoring-convention) for the authoring convention the checker expects (design tokens in `:root`, a `chart` class with a `data-chart-spec` JSON attribute, a `num` class for right-aligned numeric table cells, `status-*` classes that always carry visible text). This applies equally to a one-page brief and to a short multi-page report (five-page paper, long-form report): wrap each page in its own `class="page"` section and the heading check runs per page instead of over the whole document. Start new briefs from [assets/one-page-brief-template.html](assets/one-page-brief-template.html) for a single page, or [assets/five-page-brief-template.html](assets/five-page-brief-template.html) for a short multi-page report — both already follow the convention and pass every check.

The checker deliberately does **not** try to grade the things that need judgment — whether a headline states the right claim, whether a causal verb matches the evidence, whether a caveat is placed well. Use the reference files and the rubric for those; use the script only for the mechanically checkable subset.

## Reference files

- [reference/argument-and-structure.md](reference/argument-and-structure.md) — the decision interface, reading speeds, the abstraction gap, page-one contract, headlines, motivation, sequencing, options, document identity
- [reference/evidence-and-uncertainty.md](reference/evidence-and-uncertainty.md) — evidence-state vocabulary, framing numbers, baselines, causal language, uncertainty types, probability vs. confidence, model reporting, sensitivity, coverage vs. effectiveness
- [reference/precision-language.md](reference/precision-language.md) — sentence tests, nominalizations, modal verbs, jargon, caveat placement, precision matching, workforce and sensitive claims
- [reference/design-and-visuals.md](reference/design-and-visuals.md) — hierarchy, typography, color/WCAG, chart selection and construction, tables, diagrams, the HTML authoring convention
- [reference/domain-patterns.md](reference/domain-patterns.md) — shift by executive lens, and patterns for architecture, AI/data, simulation, risk, workflows, workforce
- [reference/production-and-review.md](reference/production-and-review.md) — gated production workflow, 48-hour rescue, using AI as an accelerator, four independent reviews, the skeptical-reader pass, meeting design, release governance
- [reference/templates.md](reference/templates.md) — one-page brief template, five-page paper architecture, ten-slide deck architecture, fill-in template, assurance appendix template
- [reference/checklist-and-rubric.md](reference/checklist-and-rubric.md) — final release checklist, the 100-point rubric, rewrite examples, glossary
