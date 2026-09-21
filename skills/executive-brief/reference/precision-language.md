# Precision language

Language controls what a reader believes happened, how certain it is, who owns it, and whether the proposed action is optional. Small wording choices change governance.

## Treat language as an operational control

Consider four statements that sound similar in conversation but assert different levels of evidence: "The control covers the risk" (ambiguous), "The control is mapped to the risk" (a design claim), "The control is implemented for the risk" (a deployment claim), "The control reduced observed failures associated with the risk" (an outcome claim requiring measurement and a defensible comparison).

Create a small **claim lexicon** for each project — define the verbs attached to status, causality, evidence, and authority, so a reviewer can flag a word that exceeds its evidence without rewriting the paragraph.

### Four tests for every consequential sentence

1. **Actor** — who or what performs the action?
2. **Action** — what actually changes?
3. **Evidence** — what warrants the statement?
4. **Boundary** — where, when, and for whom is it true?

Before: "Improved governance will enable optimization of the workflow." After: "A named process owner will review override patterns monthly and authorize changes to the release rule." The rewrite creates accountability and an observable completion condition — plain language isn't merely style, it makes the operating model testable.

## Prefer actors and actions to nominalizations

Technical prose often turns verbs into nouns (implementation, operationalization, prioritization, reconciliation, determination), hiding the actor, timing, and standard of completion.

| Before | After |
|---|---|
| "Completion of validation will occur prior to release." | "The release service validates the record before it sends the file." |
| "Ownership assignment is required." | "The operations lead assigns an owner before launch." |
| "A determination of materiality is made." | "Legal decides whether the change is material." |
| "There was an increase in exceptions." | "Exceptions increased from 18 to 31 per week." |
| "Review enablement is in progress." | "The team has coded the review step; it has not deployed or tested it." |

Use passive voice when the actor is genuinely unknown, irrelevant, or intentionally withheld ("Three records were excluded because they lacked dates") — not to avoid ownership ("The deadline was missed" should become "The vendor delivered two days late" or "The team did not complete review by the deadline," depending on the facts). Break noun strings into a relationship: "enterprise workflow risk control effectiveness measurement plan" → "a plan to measure whether enterprise workflow controls work." Shorter isn't always clearer — "Gate works" is brief but underspecified; "The gate blocks release when clearance is absent or stale" is longer and far more precise.

## Use modal verbs as governance signals

Inconsistent modal use can turn a recommendation into a requirement, or a possibility into a promise.

| Word | Recommended use | Risk |
|---|---|---|
| Must | Mandatory requirement or necessary condition | Sounds like policy if authority is absent |
| Will | Committed future action or well-supported forecast | Often overstates an aspiration or model output |
| Should | Recommendation or expected norm | Can obscure whether compliance is optional |
| May | Permission or genuine possibility | Ambiguous between the two meanings |
| Can | Capability | Often confused with likelihood |
| Could | Plausible scenario or option | Can become vague hedging |
| Is likely to | Probability judgment with defined basis | Readers assign different probabilities |

Pair obligation with authority: "The release gate must block missing clearance under the proposed launch policy" differs from "Engineering should consider a gate." Pair future tense with status: "The team will deploy on 15 October" should mean the commitment is owned and scheduled, not merely desired. For model results prefer conditional construction ("If controls operate at the assumed rate, the scenario produces..."); for recommendations, "We recommend... because..."; for uncertainty, "The evidence suggests...; confidence is moderate because...". Don't sprinkle "may," "might," and "potentially" over weak reasoning — a useful hedge names the uncertainty source ("The ranking may change because fifteen items share the same derived input" is informative; "Results may vary" is not).

## Control jargon by translation, not prohibition

Jargon compresses shared knowledge inside a community. The executive test is whether the term saves more effort than it imposes. Keep a technical term when it's the object of the decision, when no ordinary phrase is equally precise, or when readers must use it consistently after the meeting — otherwise translate it, using: **Term — plain meaning — operational example.** "State invalidation means a later change cancels an earlier approval; for example, a new amendment forces release clearance to be repeated." Avoid definitions containing more jargon than the term, abbreviations used only two or three times, and familiar words with private meanings left unstated ("anchor," "coverage," "effective person," "engaged," "control" can all be deceptively ordinary).

### The replacement hierarchy

1. Use the ordinary word if precision is preserved.
2. Use the technical term with an inline translation if it will recur.
3. Use a compact glossary for later lookup.
4. Put field names, code labels, and taxonomies in the assurance layer.

A glossary is navigation, not absolution — if the main argument can't be understood without repeated glossary trips, the body is still too abstract.

## Place caveats where they change meaning

A caveat belongs next to a claim when it changes whether: the number is actual or conditional; the relationship is causal or associational; the result applies to the full population; the ranking is stable; implementation is complete; the recommendation depends on an unmeasured input.

Use a **claim–qualification pair**: *Claim* — "The closing coordinator produces the largest modeled reduction under the current configuration." *Qualification* — "This is a paired simulation of role reliability, not a prediction of incidents or proof of a full-time staffing requirement." The qualification sits close enough to prevent misclassification without interrupting the sentence with every methodological detail; the full method stays in assurance.

Avoid tiny-font absolution — a footnote cannot ethically repair a headline whose ordinary reading is stronger than the evidence. Don't let caveats swamp the result either: rank by decision relevance — one material limitation on the surface, secondary limits in the method note, complete assumptions in the appendix. An honest caveat often strengthens the recommendation because it reveals what management can control next: instrument the input, run a pilot, stage the decision, set a review trigger.

## Match precision to evidence

Precision has three dimensions:

- **Numeric** — don't report decimals exceeding measurement quality; use ranges, rounded values, or natural frequencies where they improve calibration; keep exact values in the data table when reproducibility requires them.
- **Categorical** — "implemented" may need to split into coded, tested, deployed, enabled, adopted, verified; "human review" may mean judgment, checklist completion, approval, or evidence capture. Name the state that matters.
- **Rhetorical** — "most," "material," "significant," "optimized," "best" need a threshold or comparator; statistical significance and business significance aren't interchangeable.

| Imprecise | More precise |
|---|---|
| "The controls close most gaps." | "Controls are mapped to 189 of 205 scenarios; effectiveness is not yet measured." |
| "Every rate is evidence-based." | "Twenty-nine rates are measured; 176 are derived from measured anchors." |
| "Five hires are needed." | "Five role patterns survived the defined tests; modeled workload estimates do not establish five full-time positions." |
| "The ranking is stable." | "The top tier persists across draws, but the order within it changes." |
| "AI improved the analysis." | "AI assisted extraction and drafting; the owner verified calculations, sources, and judgments." |

The goal isn't defensive prose — it's a sentence that cannot be read more strongly than the evidence permits.

## Write workforce findings without judging people

Workforce analysis is unusually easy to corrupt in summary because it sits near hiring, performance, privacy, and organizational politics. Separate five questions: (1) where does the process require human judgment or ownership; (2) which role capabilities address those needs; (3) what workload exists, in what pattern and seasonality; (4) how much capacity is already available; (5) what staffing, sourcing, redesign, or automation choice follows.

A role simulation can answer the first two and perhaps estimate the third — it does not automatically answer headcount. Estimated hours divided by a standard work year ignores utilization, batching, peaks, skill scarcity, service levels, and adjacent duties. Logged rows measure recorded activity, not time or effort. A concentration measure shows dependence or diffusion, not performance.

State the unit of analysis explicitly: "This analysis examines process steps, handoffs, and role classes. It does not score or rank individuals. Person-level identifiers were excluded from the decision artifact." Use role language ("a credentialed second-signature capability," not "the reviewer is failing"), process language ("81% of recorded activity is concentrated in one set of hands," not "one person controls everything"), and capacity language ("the pattern indicates a single-point dependency and an estimated 0.6 FTE of task load," not "we need one new employee"). Then show the decision alternatives: redesign, cross-train, assign, automate, outsource, combine roles, hire, or explicitly accept the gap.

## Handle sensitive claims with symmetrical rigor

Claims involving legal exposure, customer harm, employee behavior, ethics, privacy, or executive accountability attract motivated reading. Apply the same evidence standard to statements that support and challenge the preferred narrative. Use neutral construction: describe behavior and conditions, not inferred motives; distinguish a system permission from observed use of that permission; distinguish missing evidence from evidence that an action did not occur; distinguish a procedural gap from an incident; distinguish anonymized aggregate patterns from individual records; state who reviewed legally or professionally sensitive interpretations.

Unsafe: "Approvals are routinely bypassed." Safer: "The current path permits release without a recorded approval; this analysis did not measure how often staff use that path." Unsafe: "Legal failed to review amendments." Safer: "The system has no structured amendment inventory, so the record cannot establish that every executed amendment reached Legal." Neutral language is not euphemism — it makes the claim auditable and keeps a wording challenge from derailing attention from the actual control or decision.

## Edit in passes, not all at once

Trying to fix logic, evidence, wording, and layout simultaneously produces local polish over structural weakness.

| Pass | Question | Typical deletion or repair |
|---|---|---|
| Decision | What must happen? | Remove content unrelated to the authority in the room |
| Logic | Does each conclusion follow? | Add missing bridge; reorder claim and proof |
| Evidence | What kind of claim is this? | Label state, comparator, uncertainty, source |
| Abstraction | Can the reader picture it? | Add one instance; replace category with mechanism |
| Language | Can it be misread? | Fix verbs, modals, actors, denominators |
| Visual | What should the eye see first? | Remove decoration; align hierarchy |
| Skeptic | What would a resistant reader attack? | Surface assumption, tradeoff, or alternative |
| Compression | What can move down a layer? | Shift method and inventory to assurance |

Perform compression last — otherwise you may shorten an already-missing causal bridge, or delete a qualification because it looks secondary. The target is not minimum words; it is minimum avoidable interpretive work.
