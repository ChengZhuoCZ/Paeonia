# Protocol 04t — PDE Introduction Branch

## Purpose and trigger

Use this branch when the paper's main result is governed by a partial differential equation, a free-boundary or geometric-PDE problem, a PDE limit, or a PDE-based stability/regularity mechanism. Do not trigger it merely because an equation appears in an otherwise non-PDE paper.

This protocol does **not** add another mandatory ledger. It conditionally extends `IntroductionCoreBrief` with the smallest PDE-specific map needed to make the theorem readable. Populate only fields that change theorem interpretation. The ordinary path remains one selected narrative arc followed by direct prose.

## 1. Establish the theorem coordinates

Before deciding paragraph order, locate the theorem in the relevant PDE regime space. Record, as applicable:

- the governing equation or variational/free-boundary formulation;
- dimension, domain or ambient geometry, and boundary or initial conditions;
- normalization, invariant quantities, and scaling or criticality;
- data class, size, symmetry, sign, or geometric assumptions;
- the solution concept and the topology in which existence, convergence, stability, or uniqueness is asserted;
- the conclusion type: regularity, partial regularity, global existence, uniqueness, nonuniqueness, scattering, blow-up, stability, asymptotics, classification, or singular limit.

The Introduction need not display all of these items. It must expose the coordinates on which the new theorem differs from the known theory. A reader should not have to infer the solution class, regime, or topology from the proof body.

## 2. Replace the linear frontier with a result-delta map

PDE frontiers are often only partially ordered. One prior theorem may allow rougher data but impose symmetry; another may remove symmetry in a subcritical regime; a third may reach the endpoint for a weaker solution class. Do not force these into a false sentence about the single “strongest previous result.”

Build a compact result-delta map over the applicable axes:

- dimension or geometry;
- parameter, exponent, scaling, or endpoint;
- data size or regularity;
- symmetry, sign, monotonicity, or structural assumptions;
- boundary or forcing class;
- solution concept;
- qualitative conclusion;
- quantitative rate, dimension estimate, sharp constant, or optimality.

State the exact change made by the paper. When frontier results are incomparable, identify the two or three nodes needed to locate the theorem and say why they are incomparable. Avoid “improves,” “extends,” or “generalizes” unless the improved axis and retained hypotheses are explicit.

## 3. Identify the result architecture

Choose the mathematical shape of the result before choosing theorem cadence:

- `SINGLE_RESULT`: one principal statement with subordinate consequences;
- `THRESHOLD_OR_DICHOTOMY`: behavior changes across a critical value, ground state, norm, or sign condition;
- `STRATIFICATION_OR_PARTIAL_REGULARITY`: the conclusion has regular, singular, generic, anomalous, or dimensional branches;
- `RESULT_HIERARCHY`: an a priori estimate, compactness theorem, or structural theorem feeds a later geometric or dynamical result;
- `SINGULAR_LIMIT_BRIDGE`: a PDE object converges to a geometric, variational, or physical object and multiplicity, defect, or topology matters;
- `SOLUTION_CLASS_SEPARATION`: existence, uniqueness, or nonuniqueness depends decisively on admissibility or the chosen weak/strong class;
- `STABILITY_OR_SCATTERING`: linear behavior, nonlinear closure, and asymptotic state must be distinguished.

This architecture is independent of the narrative arc. A paper may use one arc while stating several branches. Do not flatten a dichotomy, stratification, or two-level contribution into a generic “main theorem.”

## 4. Choose the theorem-presentation mode

Use the earliest mode that preserves accuracy and readability:

- `DIRECT_PRECISE`: state the full theorem after the equation and minimal notation;
- `MODEL_THEN_PRECISE`: first define the blow-up, stratum, threshold object, admissible solution class, or limiting object on which the theorem depends;
- `INFORMAL_THEN_PRECISE`: give a mathematically faithful orientation theorem before a long exact statement whose hypotheses require setup;
- `RESULT_FAMILY`: announce the hierarchy or branching logic, then state the component theorems in reader order.

The mode follows prerequisite burden, not journal prestige or page count. A short PDE Introduction may be entirely adequate. A delayed theorem is justified only by definitions, regime coordinates, or cross-field dictionary needed to understand it.

## 5. Classify assumptions by role

For each nonstandard assumption, record one of:

- `STRUCTURAL`: intrinsic to the phenomenon or theorem as presently formulated;
- `TECHNICAL`: used by the method and plausibly removable;
- `NORMALIZATION`: fixes invariance or presentation but does not reduce the mathematical class;
- `PROOF_LOCAL`: needed only at a specific compactness, rigidity, endpoint, or top-order step.

Explain an assumption in the Introduction when its role changes the scope or interpretation of the theorem. When a major assumption is used only in one proof stage, say so if that fact is mathematically informative. Do not call an assumption technical merely because the authors hope to remove it.

## 6. Use a causal obstruction stack

The generic `nonroutine_obstruction` field may be expanded into at most three causally ordered layers:

1. **benchmark failure** — why standard elliptic, parabolic, dispersive, variational, or compactness theory does not decide the problem;
2. **closure failure** — why the linear, formal, local, or approximate mechanism does not survive the nonlinear or global argument;
3. **terminal failure** — the endpoint, top-order, concentration, defect, multiplicity, resonance, boundary, or rigidity issue that still blocks closure.

For each retained layer, identify the operation that resolves it and the output passed to the next layer. Do not list every technical difficulty. A long proof may still have only one Introduction-level obstruction.

## 7. Connect mechanism to a decisive control

When a formula, change of variables, monotonicity quantity, modulus, profile, or compactness principle is central, explain four things:

1. its meaning in the original PDE variables;
2. the adverse term, scale, resonance, concentration, or loss it reveals;
3. the estimate or structural control it creates;
4. how that control enters the closure step.

Include at most the formulas needed to make this relation visible. A formula dump is not a mechanism explanation. Conversely, do not replace a decisive sign, critical denominator, threshold identity, or monotonicity law by a technique label.

## 8. Select the relevant PDE proof interfaces

The proof overview should expose only the interfaces used by this theorem. Typical interfaces include:

- local theory → continuation criterion → global a priori bound;
- linear mechanism → nonlinear bootstrap → asymptotic closure;
- concentration compactness → critical element → rigidity;
- blow-up analysis → profile classification → stratification or dimension estimate;
- approximate solution → stability theorem → limiting dynamics;
- compactness topology → defect or multiplicity control → identification of the limit;
- low-order coercivity → top-order estimate → regularity recovery;
- transport estimate ↔ elliptic/parabolic inversion;
- construction → admissibility check → separation of solution classes.

Name a standard interface without expanding it when it is routine for the intended audience. Open the interface at which the paper contributes new mathematics.

## 9. Separate four kinds of boundary

After the theorem, distinguish as applicable:

- **theorem boundary:** a regime not covered by the statement;
- **method boundary:** a regime the argument cannot presently reach;
- **known obstruction:** a counterexample, instability, or failure of the desired conclusion;
- **open regime:** a case not decided by the paper or by known negative results.

Do not describe a method limitation as a theorem limitation, or an open case as a known obstruction. This distinction is often more informative than a generic paragraph of future work.

## 10. Dual-audience bridge

For geometric PDE, mathematical physics, fluid mechanics, or singular-limit papers with two natural audiences, build a minimal object dictionary:

`PDE object ↔ geometric/physical/variational object ↔ theorem-level relation`.

Explain only the correspondence needed for the result. Do not write two separate mini-surveys. State what the PDE framework gains, what extra burden it introduces, and which topology, multiplicity, or index notion transports information across the bridge.

## 11. Explanatory burden, not target length

Classify the Introduction's burden as:

- `LOW`: one equation/regime, one theorem, one mechanism, little new notation;
- `MEDIUM`: several theorem axes, one nonstandard object, or a two-stage closure;
- `HIGH`: a branching theorem, several incomparable frontiers, a new solution class or object dictionary, or a multi-layer nonlinear mechanism.

This classification chooses compression, theorem mode, and proof-overview depth. It does not impose a word count. Strong journals publish both very short and very long PDE Introductions because the explanatory burden differs.

## 12. Conditional reader checks

In addition to Protocol 04f, apply only the checks relevant to the paper:

- Can the reader state the equation, regime, solution class, and conclusion at the axes where novelty occurs?
- Is the result delta explicit rather than summarized by a prestige verb?
- Are incomparable prior frontiers kept incomparable?
- Is each emphasized assumption classified and, when useful, tied to the stage where it is used?
- Does a stability or scattering Introduction explain the linear-to-nonlinear bridge?
- Does a global-existence Introduction connect the a priori estimate to the continuation criterion?
- Does a singular-limit Introduction state the topology and address defect or multiplicity when relevant?
- Does a nonuniqueness Introduction distinguish the constructed solution class from stronger admissible classes?
- Does a regularity Introduction state the singular-set, stratum, or optimality architecture rather than only a headline regularity exponent?

Repair the earliest failed inference. Do not add every item above to every PDE Introduction.
