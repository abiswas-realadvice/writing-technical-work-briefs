# Domain patterns

Different technical genres fail in different ways. The decision interface stays stable, but the translation bridge and required caveats change.

## Shift emphasis by executive lens

| Audience | Primary question | Evidence they will test | Failure to avoid |
|---|---|---|---|
| CEO or board | Does this change strategic risk or option value? | Materiality, alternatives, ownership | Operational detail without strategic consequence |
| CFO | What are economics, sensitivity, and downside? | Baseline, cash timing, assumptions | Benefits without cost or range |
| COO | Can the operation execute reliably? | Flow, capacity, controls, service levels | System design without operating ownership |
| Strategy | What changes the portfolio choice? | Scenarios, competitive logic, reversibility | Trend summary without choice |
| Risk or legal | What is the claim boundary and residual exposure? | Definitions, provenance, controls, uncertainty | "Covered" presented as "closed" |
| CIO or CTO | What changes architecture, delivery, and reliability? | Dependencies, maturity, migration, observability | Executive simplification that erases constraints |
| People leader | What capabilities and capacity are required? | Workload, role design, privacy, alternatives | Role patterns turned into judgments of people |

Don't create seven unrelated stories — keep one governing conclusion and adjust the path into it. A decision meeting with multiple functions benefits from a shared page one followed by lens-specific evidence. When audiences disagree, identify whether the conflict concerns facts, model assumptions, risk tolerance, or values; better formatting can't resolve a disagreement about acceptable exposure, but it can make the disagreement explicit.

## Pattern for architecture and platform change

**Executive question:** Which business capability, risk, cost, or speed constraint changes if we alter the architecture?

Start with a concrete transaction or service journey; show where the current architecture creates delay, fragility, duplicated control, or strategic lock-in; then show the proposed boundary change and its consequence.

Required elements: current constraint and affected business process; target capability, not merely target technology; migration sequence and coexistence period; dependencies and irreversible choices; reliability, security, data, and operating-model implications; cost range and cost of delay; decision and guardrails.

**Useful visual:** two small system views — current and target — with only decision-relevant components, plus a migration roadmap. **Required caveat:** architecture diagrams express intended structure, not proof of performance or adoption. **Language trap:** "modernization enables scalability" → "Separating the intake service lets the team scale document processing independently and reduces deployment coupling; the benefit depends on completing data-contract migration."

## Pattern for AI and data products

**Executive question:** For which decision or task does the system improve value, and under what governance boundary?

Show the user, task, input, output, human decision, and failure consequence. Separate model quality from product value and production reliability.

Required elements: intended users and prohibited uses; data provenance and representativeness; baseline and evaluation metric tied to the task; performance by material segment, not average alone; human oversight and override path; error costs, monitoring, drift, privacy, and security; deployment status and evidence cutoff; fallback when the model is unavailable or uncertain.

**Useful visual:** decision flow with human and model roles, followed by a threshold or segment-performance chart. **Required caveat:** benchmark performance does not establish business impact; a pilot association does not establish durable causal value.

## Pattern for simulation and scenario analysis

**Executive question:** Which decision remains preferred across plausible futures, and which assumptions could reverse it?

Don't lead with run count. Lead with the decision, modeled system, and comparison. Explain one simulated entity moving through the mechanism before presenting aggregate outcomes.

Required elements: purpose (exploration, prioritization, capacity, or prediction); synthetic versus observed populations; calibration targets and evidence states of inputs; scenario definitions and paired comparison design; output denominator and time horizon; stochastic, parameter, and structural uncertainty; validation and sensitivity; statements the model does not support.

**Useful visual:** small-multiple scenario comparison with an interval against a decision threshold. **Required caveat:** repeated runs reduce simulation noise; they do not make hand-set assumptions measured or turn a scenario into a forecast. If role effects are simulated, state whether the role changes event occurrence, detection, delay, impact, or all four — a modeled decrease in late discovery does not prove prevention.

## Pattern for risk registers and controls

**Executive question:** Which exposures require a build decision, an owner and procedure, explicit acceptance, or further evidence?

Avoid starting with the full register. Begin with the process, one representative failure, the portfolio pattern, and the decision categories.

Required elements: risk event written as cause–event–consequence; severity distinct from likelihood; measured, estimated, or assumed likelihood; existing and proposed controls; coverage, implementation, operation, and effectiveness status; residual exposure and risk owner; review date and acceptance authority.

**Useful visual:** lifecycle or process heat strip showing where material risks concentrate, plus a disposition table for uncovered items. **Required caveat:** a mapped control does not remove a risk — a risk register demonstrates enumerated coverage, not completeness of all possible failure modes. Avoid multiplying ordinal scores as though the result were a physical quantity; a priority index can organize attention, but its weights are judgments and its fine ranking may be unstable — show tiers and sensitivity when the distinction matters.

## Pattern for workflows and operating models

**Executive question:** Where does work wait, fail, loop, or lose ownership — and which intervention changes the outcome?

Start with an end-to-end customer or transaction path; mark work, wait, decision, handoff, rework, and gate; then connect the pattern to service, revenue, risk, or capacity.

Required elements: unit of flow and start/end boundary; volume and demand pattern; elapsed time versus touch time; queue, handoff, and rework points; owner versus actual actor; exception path and escalation; technology and human control interaction; leading and lagging measures.

**Useful visual:** swimlane with wait and rework highlighted, followed by a before/after measure chart. **Required caveat:** activity logs may not represent effort; absence of a logged action is not proof the action did not happen elsewhere. Don't confuse automation with elimination of work — a gate can move effort earlier, expose latent demand, and create a queue; show the operator and service level the automation requires.

## Pattern for workforce and role design

**Executive question:** What capability and capacity does the process require, and what is the best way to supply it?

Organize the brief around capability gaps, not proposed job titles — a title is one implementation choice.

Required elements: process need and consequence if unowned; required judgment, credential, access, and service level; demand volume, variability, and peak pattern; work estimate with assumptions; current capacity and single-point dependencies; alternatives (redesign, automate, assign, cross-train, outsource, combine, hire); privacy boundary and unit of analysis; measures after implementation.

**Useful visual:** capability-to-process matrix plus a demand/capacity range — not a ranking of people. **Required caveat:** modeled role impact does not equal headcount; estimated FTE does not establish a full-time hire; work rows are not hours; concentration is not performance. When two partial role loads sum to roughly one FTE, don't combine them automatically — test whether credentials, timing peaks, segregation of duties, and service context are compatible. Conversely, don't split one coherent transaction lane merely because the taxonomy names two roles.

## Technical pattern quick matrix

| Work type | Concrete anchor | Executive visual | Must-label uncertainty | Decision form |
|---|---|---|---|---|
| Architecture | One transaction across systems | Current/target boundary | Migration and performance | Approve sequence and guardrails |
| AI or model | User task and failure | Human–model decision flow | Data, segments, drift | Pilot, deploy, restrict, or stop |
| Simulation | One synthetic case | Scenario interval comparison | Inputs and model form | Choose robust option or measure first |
| Risk | One cause–event–consequence | Process exposure and disposition | Likelihood and effectiveness | Build, assign, accept, or monitor |
| Operations | One case through handoffs | Swimlane and delay | Log completeness, demand | Redesign flow and ownership |
| Workforce | One unowned judgment | Capability and capacity | Workload and privacy | Assign, combine, source, or hire |

This is a navigation tool, not a substitute for judgment. Some projects span several patterns — a workflow simulation with a hiring recommendation needs both the simulation and workforce caveats. When patterns overlap, preserve the claim boundary from each; the combined brief should not inherit the strongest-sounding conclusion from one method and apply it to another question.
