# Profile — Analysis / PDE

## Proof and theorem priorities

Prioritize:
- the governing equation or variational/free-boundary formulation at the exact level used;
- function spaces, regularity, and the precise solution concept;
- normalization, invariant quantities, and scaling or criticality;
- exact dependence of constants;
- compactness topology and weak/strong convergence distinctions;
- domain geometry, boundary and initial conditions;
- endpoint, threshold, and supercritical/subcritical regimes;
- elliptic, parabolic, dispersive, transport, or mixed estimates at the exact regularity used;
- continuation criteria, admissibility conditions, defect measures, multiplicity, and equality/rigidity mechanisms when operative.

Do not hide delicate limits under “standard compactness.” Do not let a solution-class statement migrate to a stronger admissibility class. Do not describe a method limitation as a known impossibility.

## Introduction routing

For a PDE-governed Introduction, read [Protocol 04t](../protocols/04t_pde_introduction_branch.md), [PDE Introduction Archetypes](pde_introduction_archetypes.md), and the conditional [PDE reader contract](../checklists/pde_introduction_reader_contract.md). Extend `IntroductionCoreBrief`; do not create another mandatory ledger.

The Introduction should identify only the theorem coordinates on which novelty depends:

- equation and setting;
- dimension/domain/boundary or initial data;
- scaling, threshold, or operative regime;
- data and solution class;
- topology or asymptotic mode;
- result architecture;
- exact delta from the relevant frontier.

Treat the prior frontier as partially ordered when different works improve different axes. Record incomparable frontier nodes rather than manufacturing a linear ranking. A statement such as “the strongest previous result” is admissible only when one result genuinely dominates the relevant alternatives.

## Result architecture

Distinguish:
- one principal theorem;
- threshold or dichotomy;
- regular/singular or generic/anomalous stratification;
- estimate-to-application hierarchy;
- singular-limit bridge;
- stability/scattering closure;
- solution-class separation or nonuniqueness.

Choose theorem cadence by prerequisite burden. Use a short exact theorem early when the objects are standard; define blow-ups, strata, threshold objects, admissibility classes, or cross-field dictionaries first when they are needed to read the statement.

## Assumption discipline

Classify nonstandard assumptions as structural, technical, normalization, or proof-local. State where an assumption enters when that location changes how the theorem is interpreted. Do not label an assumption technical without evidence from the argument or surrounding theory.

## Mechanism discipline

Use a causal obstruction stack with no more layers than the reader needs:

1. failure of the benchmark theory;
2. failure of nonlinear/global closure;
3. endpoint, top-order, concentration, resonance, boundary, defect, multiplicity, or rigidity obstruction.

For a decisive formula or change of variables, explain its original PDE meaning, the adverse effect it reveals, the control it creates, and the closure step that uses that control.

## Scope boundary discipline

Separate:
- theorem boundary;
- method boundary;
- known counterexample or instability;
- open regime.

For global existence, connect the a priori estimate to the continuation criterion. For stability/scattering, connect linear behavior to nonlinear closure and the final topology. For singular limits, state topology and relevant defect/multiplicity control. For nonuniqueness, state the exact weak/admissible class. For regularity, expose the singular-set or stratification conclusion and its optimality boundary.

## Plain symbol discipline

Apply `profiles/plain_symbol_discipline.md`. In particular, check recurring canonical symbols for duplicates and avoid decorative script/fraktur notation.
