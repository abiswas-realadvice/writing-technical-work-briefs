# Evidence and uncertainty

Evidence becomes executive-grade when its state, boundary, comparator, and uncertainty are visible without turning the brief into a methods paper.

## Use an evidence-state vocabulary

Create a small controlled vocabulary and apply it consistently. This is a practical synthesis, not a universal standard — define it explicitly the first time you use it in a document.

| State | Meaning | Safe verbs |
|---|---|---|
| Observed | Directly seen in records, interviews, logs, or events | occurred, recorded, reported |
| Measured | Quantified from defined data and method | was, averaged, increased |
| Estimated | Calculated from incomplete information using a stated method | is estimated, likely falls |
| Modeled | Produced by a model under specified structure and inputs | model indicates, scenario yields |
| Assumed | Set for analysis without direct measurement | assumes, holds constant |
| Inferred | Reasoned from evidence but not directly observed | suggests, is consistent with |
| Recommended | A judgment about action | recommend, should, propose |

Labels prevent a common slide-level distortion: formatting makes all numbers look equally factual. A historical rate, an analyst-set parameter, a simulated outcome, and a management target may all appear as bold percentages — without labels the reader supplies an evidentiary status, usually stronger than intended. Put the label where the number appears: **14% measured**, **6–18% derived estimate**, **10% modeled outcome**, **84% assumed control effectiveness**. A global footnote ("some figures are modeled") is inadequate. The label must correspond to a defined method in the assurance layer and stay stable across the document.

## Give every important number a frame

A number is decision-ready only when the reader can answer six questions:

1. **What is counted?** Event, case, person, transaction, day, dollar, or model run.
2. **Out of what?** The denominator or eligible population.
3. **Over what period?** Snapshot, month, rolling year, or full history.
4. **Compared with what?** Baseline, target, prior period, peer, or alternative.
5. **How was it produced?** Measured, estimated, modeled, or assumed.
6. **How uncertain is it?** Sampling, parameter, measurement, or structural uncertainty.

Unframed: "Risk falls from 84% to 10%." Framed: "In the 500-deal scenario, the share of engaged synthetic deals released with at least one unresolved modeled problem falls from 84% in the baseline configuration to 10% in the on-release configuration; the result is directional and depends on assumed control effectiveness." The executive surface can shorten this — "Modeled unresolved-release exposure falls materially in the tested scenario" — provided the chart subtitle and note preserve population, comparator, and assumption.

Use fixed denominators when comparing groups; if one row is "of all cases" and another "of completed cases," make the distinction visually unavoidable. Use absolute numbers alongside percentages when scale matters — a 50% improvement from two cases to one is not the same management problem as from 20,000 to 10,000.

## Baselines determine meaning

"Faster," "safer," "higher," and "reduced" are incomplete without a baseline. Choose the baseline that corresponds to the decision, not the one producing the strongest contrast.

| Decision | Useful baseline | Common trap |
|---|---|---|
| Replace a process | Current-state performance | Comparing only with an idealized no-control case |
| Fund a capability | Best feasible alternative | Comparing with doing nothing when a cheaper alternative exists |
| Launch a model | Human or existing-system benchmark | Comparing with a weak historical average |
| Add capacity | Demand and service target | Treating current headcount as the workload baseline |
| Accept risk | Risk tolerance and residual exposure | Showing gross risk only |

State whether the baseline is observed or constructed — a simulation baseline is still modeled even if it represents the current configuration. When rates are small, show natural frequencies ("3 in 1,000" alongside "0.3%"). When time horizons differ, normalize or display both. Keep the baseline consistent across headline, chart, and recommendation — silent shifts (current state in one chart, prior model in another, target in a third) force the reader to reconstruct a moving reference frame.

## Control causal language

Executives act differently on "causes," "is associated with," "contributes to," and "is consistent with." Treat causal verbs as evidence-bearing choices.

| Evidence situation | Prefer | Avoid |
|---|---|---|
| Randomized or strong quasi-experimental design | caused, increased, reduced | — |
| Observational relationship with adjustment | was associated with, predicts within this sample | caused |
| Mechanistic evidence plus observational pattern | likely contributes to, is a plausible driver | proves |
| Scenario model | the model produces, under these assumptions | will deliver, prevents |
| Expert judgment | we assess, we recommend | the data show |

Statistical significance does not establish practical importance, causation, or truth. For operational work, a causal chain (with each link marked observed, assumed, or inferred) is often more useful than a single coefficient. If a control is modeled as reducing delay, don't say it "proved" it will reduce incidents — say the scenario shows what would follow *if* the control operates at the assumed rate, then specify how post-launch measurement will test that assumption. Qualification need not weaken language: "The experiment reduced median handling time by 18%" is stronger and more precise than "results seem promising."

## Name the uncertainty that matters

"Uncertain" is not one condition:

| Type | Source | Typical treatment |
|---|---|---|
| Variability | Random variation in events or populations | Distribution, percentile, range |
| Parameter uncertainty | Inputs are estimated imprecisely | Confidence or credible interval; sensitivity |
| Measurement uncertainty | Data or definitions imperfectly capture the construct | Quality note, validation, alternate measure |
| Structural uncertainty | Model omits or simplifies mechanisms | Competing models, scenarios, limitation statement |

A narrow numerical interval can coexist with low confidence in the model form — the two are different problems. Don't place every uncertainty in the headline: surface the one that could change the decision. If all plausible values lead to the same action, say the direction is robust and move detailed ranges to assurance. If plausible values reverse the recommendation, uncertainty is part of the decision and belongs on the executive surface. Avoid false precision — "22%" from a sparse class may imply more resolution than the evidence supports; "approximately 20%, with a plausible range of 8–59%" communicates center and width honestly.

## Separate probability from confidence

Probability answers *how likely is the proposition or event?* Confidence answers *how strong is the basis for that probability judgment?* They are independent axes:

- **High probability, low confidence** — a volatile market event judged likely from sparse and conflicting indicators.
- **Low probability, high confidence** — a well-measured, rare mechanical failure.
- **High probability, high confidence** — a repeated operational condition supported by stable records.
- **Low probability, low confidence** — a novel scenario with little data and uncertain mechanism.

Use probability words only if the organization defines them — don't let "likely" mean 55% to one team and 90% to another. A useful confidence sentence explains the basis and the missing information: "Moderate confidence: the direction is supported by process evidence and repeated scenarios, but control effectiveness has not been measured in production. Confidence would increase after three months of instrumentation and exception review." This is more informative than a color-coded "amber" badge because it says why confidence is limited and what would change it.

## Report models as conditional arguments

A model is an organized "if–then" statement. For any simulation, forecast, optimization, or AI model, state:

- **Purpose** — decision support, exploration, prioritization, prediction, or control.
- **Unit and population** — what entities, events, and period are represented.
- **Inputs** — which are measured, estimated, derived, or assumed.
- **Mechanism** — the few rules that drive the result.
- **Outputs** — what the model produces and what it does not.
- **Validation** — back-tests, holdouts, benchmarks, expert review, or none.
- **Uncertainty** — sampling, parameter, and structural limits.
- **Use boundary** — decisions the model can and cannot support.
- **Monitoring** — what will be measured after deployment.

Unsafe headline: "The model predicts a 90% reduction." Safer: "Under the tested control assumptions, the model indicates a large reduction; the magnitude will remain unverified until production effectiveness is measured."

## Use sensitivity to expose decision dependence

Sensitivity analysis isn't a ritual appendix — its executive purpose is to answer *which uncertain inputs could change the decision?* Start with decision thresholds.

| Finding | Executive interpretation | Action |
|---|---|---|
| Direction holds; magnitude varies | Choice is robust, benefits uncertain | Proceed with measurement plan |
| Ranking changes within range | Priorities are unstable | Avoid false ordering; group or stage |
| One input dominates | Decision depends on a specific unknown | Instrument or pilot that variable |
| Many interactions dominate | Model is structurally fragile | Use scenarios; reduce claim strength |
| Plausible range crosses tolerance | Risk acceptance is required | Escalate explicitly |

Avoid the "tornado chart of everything" — rank parameters by effect on the decision outcome and explain the top few. If many risks share the same derived rate, the model may not support a fine-grained rank; present a tier or set rather than inventing order.

## Coverage is not effectiveness

Risk and control briefs frequently collapse four different ideas into one:

1. **Coverage** — a control is mapped to a risk or failure mode.
2. **Implementation** — the control exists in the released process or system.
3. **Operation** — people and systems actually use it as intended.
4. **Effectiveness** — it prevents, detects, or contains the event at a measured rate.
5. **Residual risk** — exposure that remains after control operation.

"189 of 205 risks have a mapped control" is a coverage claim — it does not mean 189 risks are closed. "Implemented" is not the same as adopted, and adopted is not the same as effective. Use a control statement with all relevant qualifiers: "A release gate is implemented and mapped to 22 failure modes. Its production effectiveness is not yet measured; scenario results assume 84% operation. Instrument bypasses, holds, overrides, and caught defects after launch." This wording doesn't undermine the control — it turns uncertainty into a measurement plan.

## Build a one-page model surface

When a model materially shapes a decision, include a compact model surface before the detailed method:

| Element | One-line answer |
|---|---|
| Decision supported | Which control and staffing sequence to approve |
| What is represented | Synthetic cases moving through a defined workflow |
| What is observed | Selected historical event rates and conversion patterns |
| What is derived | Rates for unmeasured failure modes from measured anchors |
| What is assumed | Control effectiveness, delays, and severity weights |
| What is produced | Comparative scenario outcomes, not forecasts |
| What is robust | Direction of improvement across tested ranges |
| What is fragile | Exact magnitude and fine-grained ranking |
| What happens next | Instrument production controls and recalibrate |

This surface lets an executive challenge the right thing instead of debating simulation counts when the dominant unknown is an assumed control effect. "We ran 5,000 simulations" sounds impressive but doesn't repair a misspecified model or unmeasured input — more runs reduce Monte Carlo noise, not structural uncertainty.

## Make provenance visible but quiet

Credibility depends on traceability; readability depends on not forcing every reader through the trace. Use a provenance ladder:

1. **Inline label** for evidence state and essential boundary.
2. **Figure source line** naming the dataset, analysis, and cutoff date.
3. **Method note** defining calculation, inclusion, and exclusion.
4. **Appendix reference** with diagnostics, assumptions, and tables.
5. **Repository or record link** for authorized reviewers.

Every important claim should have a route down the ladder — the executive shouldn't have to follow it, but a reviewer shouldn't hit a dead end. Specify "as of" dates for system state, organizational data, and implementation claims: "already implemented" is perishable — say as of a named date and whether it means coded, deployed, enabled, adopted, or verified. For AI-assisted analysis, disclose the role of AI, the human owner, and the checks performed: "AI assisted drafting and analysis; the named owner validated sources, calculations, and judgments" is more informative than silence or a generic disclaimer.
