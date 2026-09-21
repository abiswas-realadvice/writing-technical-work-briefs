# Format templates

Section-by-section architectures for the five artifact types, plus two fill-in templates. A working HTML implementation of the one-page brief is at [assets/one-page-brief-template.html](assets/one-page-brief-template.html).

## One-page decision brief template

**Header** — Message title: the governing conclusion in one sentence. Add owner, date, status, and evidence cutoff in small type.

**Decision** — One sentence with decision maker, action, boundary, and timing. Separate approve, direct, discuss, and note.

**Motivation** — Two or three sentences: present state, hidden tension, consequence, purpose. Omit if shared context makes it redundant.

**Evidence** — Three proof points. Each should include evidence state and comparator. Use one chart or a compact table only if it makes the relationship faster to grasp.

**Options and recommendation** — Show two or three real choices with the tradeoff that matters. State the recommendation and why it dominates under the stated priorities.

**Material uncertainty** — Name the one assumption, dependency, or range that could change magnitude or choice. State how it will be tested or governed.

**Next step** — Owner, milestone, decision date, and proof of completion.

Place a short source line at the bottom, linked to the assurance material. Do not put a miniature methodology chapter in eight-point type.

## Five-page executive paper architecture

Use five pages when the decision needs context, mechanism, and tradeoffs, but the meeting shouldn't become a methods review.

| Page | Job | Typical visual |
|---|---|---|
| 1 | Conclusion, decision, motivation, proof points | Decision summary |
| 2 | Concrete operating mechanism and scale | Process or system diagram |
| 3 | Evidence and uncertainty | Comparison chart with ranges |
| 4 | Options, economics, risk, and reversibility | Decision table |
| 5 | Recommendation, execution, measures, open issues | Roadmap or ownership table |

Attach assurance (methods, definitions, scenario inventory, sensitivity, source tables, model card, control register) rather than stretching the paper until it becomes a report. Make each page answer one executive question, and use sentence headlines so the five headlines form a coherent argument on their own. If motivation is essential, place it on page one or at the top of page two — don't create a separate three-page history before the conclusion.

## Ten-slide decision deck architecture

1. Decision and governing conclusion
2. Why this matters now
3. One concrete operational case
4. Pattern and scale across the system
5. Evidence and comparator
6. Uncertainty and sensitivity
7. Options and tradeoffs
8. Recommendation
9. Implementation, ownership, and measurement
10. Decision restated and discussion questions

A starting architecture, not a compulsory count — combine slides when the story is simple, split a slide when it asks the audience to decode two different relationships. For live presentation, the headline states the assertion and the visual supplies the evidence; avoid paragraphs that compete with the speaker, but keep essential definitions on the slide (not only in notes) if the deck will circulate. Reserve backup slides for methodology, full tables, alternative scenarios, data quality, and source detail — numbered and linked from the main deck. The main deck should not pretend uncertainty vanished because it moved to backup; surface anything that changes the recommendation or informs risk acceptance.

## Fill-in template for an executive brief

```
Message title        [Conclusion with an honest evidence verb]

Decision              [Decision owner] to [approve/direct/discuss/note]
                       [action and boundary] by [date].

Motivation             Today, [current state]. The hidden tension is
                       [mechanism or missing visibility]. It matters now
                       because [consequence/deadline]. This analysis was
                       designed to [purpose].

What the evidence says
  1. [Observed/measured finding with comparator and scope]
  2. [Modeled/estimated finding with assumption and range]
  3. [Operational mechanism connecting finding to consequence]

Options
  Option | Value | Exposure | Cost/capacity | Reversibility
  A      |       |          |               |
  B      |       |          |               |
  C      |       |          |               |

Recommendation         We recommend [option] because [decision criteria].

Material uncertainty   [What could change magnitude or choice; how it
                       will be tested]

Next action            [Owner] by [date], complete when [observable
                       condition].

Source and status      [Evidence cutoff, publication edition, analysis
                       generation, links]
```

## Assurance appendix template

**Claim ledger** — columns: Claim, State, Source, Cutoff, Owner, Material caveat. One row per important claim in the brief.

**Model or analysis card** — Purpose and decision supported; unit, population, time horizon, exclusions; inputs by evidence state; core mechanism and outputs; validation and benchmarks; uncertainty and sensitivity; intended and prohibited uses; monitoring and recalibration.

**Definitions** — Define terms whose ordinary meaning differs from project meaning. Keep each definition operational and add an example where useful.

**Change and release record** — columns: Publication edition, Analysis generation, Date, Status, Material change, Approver.

**Decision record** — Record approval, conditions, dissent, owner, due date, measurement plan, and review trigger.
