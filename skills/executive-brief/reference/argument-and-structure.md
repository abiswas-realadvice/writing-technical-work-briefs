# Argument and structure

How to frame the brief as a decision interface, close the expert-to-executive abstraction gap, and build page one so the argument is visible before the reader reaches a single paragraph of prose.

## The brief is a decision interface

A technical report answers: what did we examine, how did we examine it, what did we find? An executive brief answers: given what we now know, what should this group understand, decide, fund, stop, accept, or monitor? Arrange evidence around the decision, not around the order the analysis was performed.

Three layers, not three ranks of importance — routes for different reader needs:

1. **Decision surface** — conclusion, decision, recommendation, tradeoffs, owner, timing, consequence of delay.
2. **Explanation layer** — the minimum mechanism and evidence required to understand why the recommendation follows.
3. **Assurance layer** — methods, definitions, assumptions, detailed tables, diagnostics, sources, reproducibility material.

A CEO can act from the surface; a CFO can test the economics; a risk leader can inspect the assumptions; a technical owner can reproduce the analysis. This is why "cut 70% of the words" is usually bad editing advice — it treats all detail as excess. Better editing asks where each piece belongs, whether it changes the decision, and whether it must appear at the moment of the claim.

## Design for three reading speeds

The document must stay coherent read at three speeds, because executives scan, select, return, and challenge rather than reading once linearly.

- **Ten seconds** — subject, governing conclusion, requested action, scale of consequence, any status label that changes interpretation. Test: a generic title like "Risk Model Update" fails; "Release controls reduce modeled exposure, but the closing decision remains unresolved" passes.
- **Two minutes** — why it matters now, the operating mechanism, the evidence class, main options and tradeoffs, the recommendation. A single concrete example often supplies the missing bridge.
- **Fifteen minutes** — a skeptical reader can inspect definitions, comparators, uncertainty, assumptions, sensitivities, implementation constraints, and sources without discovering the headline meant something narrower than it appeared to.

Editing test: print only titles, leads, charts, and bold text — does the ten-second story hold? Read only the first paragraph of each section — does the two-minute logic hold? Then challenge every number and causal verb — does the fifteen-minute evidence survive?

## Why technically correct briefs still fail

Most weak briefs aren't wrong in one dramatic way — they impose small translation costs until the reader loses the thread.

| Failure | What the reader experiences | Repair |
|---|---|---|
| Chronology-first | "When will this get to the point?" | Lead with conclusion and decision; move history to context |
| Abstraction-first | "I cannot picture what is happening" | Start with one operational case, then name the pattern |
| Method-first | "Why do I need to know this?" | State consequence before method; layer assurance |
| Number without comparator | "Is that large, good, or actionable?" | Add baseline, target, prior period, or alternative |
| Model output as forecast | "Is this expected to happen?" | Label scenario, assumptions, range, and intended use |
| Control mapped as risk closed | "So the issue is gone?" | Separate coverage, effectiveness, adoption, residual risk |
| Role analysis as people judgment | "Are individuals being evaluated?" | State unit of analysis and limits explicitly |
| Dense but decorative graphics | "Where do I look?" | Give each visual one question and one reading path |
| Caveat in appendix | "The headline overstates the evidence" | Attach qualification to the claim |
| Version narrative on page one | "Why am I reading an internal argument?" | Separate model lineage from publication identity |

The root cause: the document reflects the structure of the work (discover, classify, model, validate, revise) rather than the structure of the reader's decision.

## Expertise creates an abstraction gap

Experts compress concrete operations into categories and frameworks; a new executive reader sees labels whose contents aren't yet available. Abstraction should follow orientation, not replace it. Climb a four-rung ladder:

1. **Instance** — "A closing date changes after the report is approved."
2. **Mechanism** — "The approval remains attached to the record unless the change invalidates it."
3. **Pattern** — "Date-dependent approvals can become stale without visible failure."
4. **Decision** — "Require automatic invalidation before release, or accept the residual risk."

A glossary does not create a mental model by itself. Put a concrete case in the body; use the glossary for repeat reference.

### The concrete-first translation loop

The most reliable explanatory unit for complex technical work:

**Actual process** (what is a person or system trying to do?) → **Potential failure** (what specific event, not category, could happen?) → **Detection or control** (what would reveal, prevent, or contain it, and at what point?) → **Business consequence** (what changes in money, time, service, risk, capacity, compliance, or strategic option value?) → **Executive choice** (what must this audience decide or authorize?)

Use one representative case before a register of hundreds. The case is not proof of prevalence — portfolio evidence supplies that. Its job is to make the mechanism intelligible. If the author cannot connect a control to an event or an event to a consequence, the problem is not prose, it is analysis.

### Give abstraction a budget

An abstraction is any label asking the reader to retrieve a definition or infer a mechanism ("risk class," "process dependency," "maturity," "agentic workflow"). On the first two pages:

- Introduce no more than three essential named constructs.
- For each, give a plain-language meaning and one concrete instance.
- Delay taxonomies that don't change the immediate decision.
- Reuse the same term; don't alternate synonyms to sound varied.
- Remove internal field names, model variables, code names, and scoring labels unless the audience must act on them.

**Substitution test:** underline every abstract noun in a draft. Could the sentence name an actor, action, object, or consequence instead? *"Operationalization of the control architecture enables improved risk disposition"* → *"The release gate stops the file until the required review is recorded."* The rewrite carries more operational information with fewer interpretive steps.

## A model version is not a publication edition

Analytical lineage and audience-facing identity are different axes. Conflating them makes a first public-facing brief open with an internal audit argument the audience can't yet parse.

| Axis | Example | What it controls |
|---|---|---|
| Analytical generation | Model M3 | Method, data, assumptions, reproducibility |
| Publication edition | Executive brief E1 | Audience-facing narrative and design |
| Release status | Wednesday meeting draft | Governance, approval, permitted use |

Cover line example: **Executive brief · first edition · based on model M3 · meeting draft**. A small version table can preserve analytical history without demanding the opening — unless the decision itself concerns methodology. Treat audience change (new readers, new claims, new consequences) as a major release even when the underlying model is unchanged; conversely a model refresh doesn't always need a new publication edition if the decision and conclusions are unaffected.

## Write the decision question first

Before drafting, complete: **At this meeting, we need [decision owner] to decide whether to [action] by [date], because [consequence].** If you can't complete it, the brief isn't scoped yet.

Classify every intended outcome — don't soften an approval ask into "discussion" to reduce friction, and don't ask approval for a vague direction when the real choice is a resource commitment:

| Type | Reader action | Wording |
|---|---|---|
| Decide | Choose or approve | "Approve option B and its funding envelope" |
| Direct | Set a boundary or priority | "Direct the team to make release gating mandatory" |
| Discuss | Surface judgment before a later decision | "Discuss acceptable residual exposure" |
| Note | Acquire shared awareness | "Note the measured adoption gap" |
| Endorse | Signal support; formal authority lies elsewhere | "Endorse the implementation sequence" |

A sound question defines the decision object, authority, time horizon, and boundary. "Agree on what we are building" is directionally useful but incomplete; "Approve mandatory release and closing gates for the first launch, with the sixteen uncovered scenarios assigned to named owners before go-live" is testable.

## Page one is a contract with the reader

1. **Message title** — a sentence stating the governing conclusion.
2. **Decision and timing** — exact action required, by whom, when.
3. **Why now** — the event, deadline, threshold, or change that makes delay consequential.
4. **Three proof points** — the minimum evidence supporting the conclusion.
5. **Material uncertainty** — the limitation that could alter magnitude, ranking, or implementation.
6. **Next action** — owner, milestone, proof of completion.

Don't spend page one proving how much work occurred. "We analyzed 205 risks" is evidence of scope, not a conclusion. "Sixteen material scenarios have no software control and require an owner or explicit acceptance" is decision-relevant. Likewise, "what changed since the last model" belongs on page one only when the reader saw the earlier model, the change affects the decision, or trust requires immediate disclosure.

## Use message headlines to carry the logic

A topic heading names a subject ("Control effectiveness"). A message headline states what the reader should understand ("The recommendation depends more on control effectiveness than on event frequency"). The latter turns headings into a visible argument: a scanning reader reconstructs the logic without reading every paragraph, the author is forced to choose the claim each page makes, and reviewers can challenge the assertion directly.

**Headline tests:**
- Does it contain a verb?
- Does it state one claim, not a topic plus a subtitle's worth of qualifications?
- Is the evidence state honest ("the model indicates" vs. "operations data show")?
- Does it avoid unsupported superlatives ("transformational," "best-in-class")?
- Would a skeptical executive know what to challenge?

Weak: "Simulation Results." Better: "Across tested scenarios, the release gate changes the direction of exposure; the size depends on unmeasured control effectiveness."

## Give motivation its own section when it changes comprehension

Motivation answers three questions a conclusion alone can't: why was this work necessary, why is the current framing right, why does action matter now. A dedicated section belongs in the main narrative when: the audience lacks the operational context that made the problem visible; the work challenges an established mental model or role boundary; ordinary metrics hide the failure mode; timing is driven by an irreversible event or threshold; or the method is unusual enough that readers need to know why a simpler approach would corrupt the answer.

Four moves, kept distinct from history:

1. **Present state** — what people currently see or believe.
2. **Hidden tension** — what that view misses.
3. **Consequence** — what becomes possible or dangerous because of the gap.
4. **Purpose** — what the analysis was designed to clarify.

Test: remove the section. If the reader can still understand why the decision exists and why now, motivation may be redundant. If the recommendation becomes arbitrary, the section is doing real work.

## Sequence the story around consequence

Pyramid (answer, then reasons, then evidence) is excellent for scanability. Situation–complication–question–answer is excellent when the audience needs a reason to care. Combine them for technical executive briefs:

1. Answer and ask 2. Consequence 3. Concrete mechanism 4. Evidence 5. Options and tradeoffs 6. Uncertainty and reversibility 7. Execution

Don't manufacture drama — the "complication" may simply be a decision deadline or a capacity mismatch. A narrative is a causal and decision sequence, not a theatrical arc.

## Show options as real choices

Don't present a false menu where only one option is viable, and don't hide the tradeoffs that make alternatives attractive. Use a decision table with consistent criteria reflecting the actual decision (economics, risk, time to value, customer impact, legal constraints, feasibility, organizational capacity, reversibility):

| Option | What changes | Value | Exposure | Cost and capacity | Reversibility | Recommendation |
|---|---|---|---|---|---|---|
| A | ... | ... | ... | ... | ... | ... |

Include the cost of delay when material, and the cost of acting (migration disruption, review burden, false positives, capacity diverted). A weighted score can conceal contested judgments — show the weights and test whether a small change flips the recommendation.

## Separate fact, interpretation, and recommendation

An executive sentence often compresses several epistemic moves. Make them visible:

- **Fact** — "Twenty-nine event frequencies were measured in historical records."
- **Method** — "The remaining frequencies were derived by grouping risks with measured anchors."
- **Result** — "Under the stated control assumptions, modeled exposure declines in the release scenario."
- **Interpretation** — "The direction suggests release gating is a high-leverage control."
- **Recommendation** — "Implement the gate before launch and measure its actual effectiveness."

Collapsed into "The new system eliminates most risk," a sentence overstates causality, control effectiveness, and implementation status at once. During review, for each headline ask: what kind of statement is this, what evidence supports it, what inference connects evidence to meaning, what value judgment connects meaning to recommendation, what could falsify or reverse it?

## Govern document identity and change

Naming pattern: **[Subject] · [artifact type] · [publication edition] · based on [analysis generation] · [status] · [date]**

Example: *Workflow exposure · executive decision brief · E1.0 · based on model M3.2 · meeting draft · 2026-09-23*

Maintain a compact change table (audience, decision date, publication owner, analytical owner, evidence cutoff, current status, material change). Avoid filenames like `final_v3_revised_FINAL2`; a common vocabulary, sortable date, explicit owner, and revision status reduce ambiguity. Carry the version table inside the file so identity survives download or renaming.
