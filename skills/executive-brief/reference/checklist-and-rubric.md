# Checklist, rubric, and rewrite examples

Use the checklist before any release. Use the rubric to score a draft or settle a disagreement about whether it's ready. Any zero in decision, evidence integrity, or material uncertainty blocks release regardless of total score — don't optimize the score mechanically; a polished 92 with an incorrect denominator is worse than an honest 78 with a visible limitation.

## Rewrite example: model output to decision claim

**Before:** "Version 3 derives all unmeasured rates using the process score selected through leave-one-out testing. The model produces materially worse outcomes than version 2, but directionality holds across seeds and rate bands."

**Why it fails for a first public-facing brief:** It begins with internal lineage, assumes the reader understands the scoring system, uses "worse" without defining the business consequence, and doesn't say what action follows. It also risks treating a model comparison as the meeting's purpose.

**After:** "The tested release controls reduce modeled exposure across the plausible input range, but the exact size is uncertain because control effectiveness has not been measured. Approve the release and closing gates, assign owners to the uncovered scenarios, and instrument bypasses and caught defects after launch." (The supporting method then says: unmeasured event frequencies were derived from measured anchors; input and seed ranges were tested; the direction held; fine-grained ranking did not.)

**What changed:** publication decision replaced version history as the lead; technical method became assurance rather than motivation; modeled status and dominant uncertainty are visible; the action, owner category, and measurement plan are explicit; the analytical generation can still be identified in the document metadata.

## Rewrite example: roles to capacity decision

**Before:** "The model supports five hires, ranked by measured impact. The closing coordinator reduces unsafe closings by 27.8 points and requires 0.7 FTE."

**Why it is corrupting:** The analysis tests role patterns in a simulation; it does not directly measure hiring outcomes. "Measured impact" can be confused with observed production impact. The FTE is a workload estimate, not a headcount requirement. The sentence omits that role reliability is set by the model, and the possibility of combining, assigning, sourcing, or redesigning work.

**After:** "Five role capabilities survived the defined evidence and refutation tests. In the current-state scenario, dedicated closing ownership produces the largest modeled safety effect. The associated workload is estimated at roughly 0.7 FTE, so the executive choice is how to supply that capability — assignment, combination with legal operations, external support, process redesign, or hire. The simulation does not predict incidents or evaluate individuals."

**What changed:** capability preceded title; modeled effect replaced "measured impact"; workload separated from staffing; alternatives became visible; the privacy and performance boundary moved into the main claim.

## Final release checklist

**Decision and narrative**
- The decision, authority, timing, and consequence are explicit.
- Motivation explains why the work and why now without becoming project history.
- One concrete example precedes the main abstraction.
- Options and the cost of delay are visible.
- The recommendation follows from stated criteria.

**Evidence and language**
- Important claims are labeled observed, measured, estimated, modeled, assumed, inferred, or recommended.
- Denominators, time periods, baselines, and units are clear.
- Causal verbs match the method.
- Probability and confidence are not conflated.
- Caveats sit next to the claims they change.
- Coverage, implementation, operation, effectiveness, and residual risk are distinct.
- Workforce claims distinguish role, workload, capacity, headcount, and individual performance.

**Design and access**
- Each page or slide has one job and a message title.
- Charts match the relationship and include source, scope, and uncertainty.
- Tables are ordered, aligned, and readable.
- Color is not the only signal; contrast and alt text are adequate.
- The document works at ten-second, two-minute, and fifteen-minute speeds.
- Every rendered page has been inspected.

**Governance**
- Publication edition, analysis generation, status, and evidence cutoff are correct.
- Named owners approved technical, business, and release content.
- Distribution and privacy boundaries are correct.
- The meeting decision and follow-up measure have a record location.

## The 100-point executive-brief rubric

Score each criterion 0–5. A score of 3 means usable, 4 means strong, 5 means exemplary. **Any zero in Decision, Evidence integrity, or Material uncertainty is a release blocker regardless of total.**

Present this as what it is: a synthesis created for the field guide, not an external or industry standard (the same is true of the seven-state evidence vocabulary). Its value is in forcing a consistent, domain-by-domain look at a draft; don't cite it to a reader as an authority, and don't let a high score substitute for the release blockers above.

| Domain | Criterion | Points |
|---|---|---|
| Decision | Exact action, authority, timing, and boundary | 5 |
| Decision | Recommendation and real alternatives | 5 |
| Decision | Consequence of action and delay | 5 |
| Motivation | Why the work exists and why now | 5 |
| Translation | Concrete mechanism before abstraction | 5 |
| Translation | Technical → operational → business chain | 5 |
| Structure | Answer-first, coherent page sequence | 5 |
| Structure | Layered executive and assurance paths | 5 |
| Evidence | Claim states and provenance | 5 |
| Evidence | Baselines, denominators, scope, and time | 5 |

Subtotal: 50 points.

| Domain | Criterion | Points |
|---|---|---|
| Evidence | Causal and inferential discipline | 5 |
| Uncertainty | Material uncertainty and sensitivity | 5 |
| Language | Actors, verbs, modals, and definitions | 5 |
| Language | Sensitive and workforce claims bounded | 5 |
| Graphics | Correct form, honest scale, useful annotation | 5 |
| Design | Hierarchy, density, typography, and consistency | 5 |
| Access | Contrast, non-color cues, alt text, navigation | 5 |
| Execution | Owner, dependencies, milestones, measures | 5 |
| Governance | Version identity, status, approvals, privacy | 5 |
| Resilience | Survives skeptical reading and forwarding | 5 |

Subtotal: 50 points. **Total: 100.**

**Interpretation:**
- **90–100** — decision-ready and durable
- **80–89** — strong; repair the lowest domain before release
- **70–79** — usable only with an active presenter; revise
- **Below 70** — not ready for executive reliance

## Glossary

- **Abstraction budget** — an editorial limit on unfamiliar constructs introduced before the reader has a concrete anchor.
- **Analytical generation** — the version of a model, dataset, method, or calculation independent of the audience-facing publication.
- **Assurance layer** — methods, diagnostics, assumptions, detailed tables, sources, and reproducibility material supporting the executive surface.
- **Baseline** — the reference state against which a result is compared; may be observed or modeled and should be labeled accordingly.
- **Confidence** — strength of the analytical basis for a judgment, distinct from the probability assigned to the event.
- **Control coverage** — mapping of a control to a risk; not proof that the control exists, operates, or works.
- **Decision interface** — an artifact designed to connect evidence to a specific organizational choice while preserving traceability.
- **Evidence state** — classification of a claim as observed, measured, estimated, modeled, assumed, inferred, or recommended.
- **Message headline** — a sentence title that states the page's governing assertion.
- **Modeled outcome** — a result generated under a defined model and inputs; not automatically a forecast.
- **Motivation** — the present state, hidden tension, consequence, and purpose that explain why analysis and action are needed.
- **Publication edition** — the version of the audience-facing artifact, separate from the analytical generation beneath it.
- **Residual risk** — exposure remaining after controls, considering their operation and effectiveness.
- **Role pattern** — a bundle of process ownership, judgment, credential, access, or service capabilities; not necessarily a job title or headcount unit.
- **Sensitivity analysis** — testing how outputs or decisions change as assumptions or inputs vary.
- **Structural uncertainty** — uncertainty about whether the model represents the right mechanisms or boundaries.
- **Translation chain** — technical mechanism → operational behavior → business consequence → executive decision.
- **Version status** — draft, meeting draft, approved, released, or superseded; communicates authority and permitted reliance.

## Closing principle

A durable brief does four things simultaneously: it makes the system concrete enough to picture; it makes the evidence honest enough to trust; it makes the choice explicit enough to decide; it makes the assurance path intact enough to challenge. That is compression without distortion — the difference between a technical artifact that happens to reach executives and an executive artifact worthy of technical work.
