# Protocol 04k — Scientific and Physical Context Research

## Purpose

Decide whether the Introduction needs external scientific context and, when it does, research that context deeply enough that the mathematics is situated inside the model rather than decorated with generic motivation.

This protocol produces `ScientificContextLedger`. It is independent of `NarrativeAmbitionLedger`: mathematical grandeur and scientific-context depth are separate axes.

## 1. Trigger the research pass

Run this pass when the focal theorem, equation, functional, boundary condition, scaling, or geometric quantity has a genuine scientific lineage or interpretation that materially helps answer at least one of:

- why this mathematical object was introduced;
- which observable or mechanism the equation models;
- why the parameter range, scaling, or constraint is natural;
- which phenomenon corresponds to the mathematical regime;
- why the theorem matters beyond the formal statement;
- why a classical mathematical-physics problem acquired its present form.

Do not infer that scientific context is needed merely because a PDE appears.

## 2. Select context depth

Choose one of:

- `NONE` — scientific context is absent, speculative, or irrelevant to the theorem;
- `ORIGIN_BRIEF` — a physical/scientific origin or interpretation is useful, but one compact paragraph or bridge is enough;
- `SUBSTANTIAL` — model origin, mechanism, parameter meaning, or physical regimes are needed to make the mathematical question legible;
- `PHYSICS_LED` — the paper is best entered from the scientific phenomenon/model, with the mathematics emerging from that context;
- `INTERDISCIPLINARY_LED` — multiple scientific domains or modeling levels are essential to the paper's position.

Audience specialization does **not** determine this value. A specialist PDE audience may still need substantial physical context when that context carries the problem's scientific meaning.

## 2a. Select research breadth

Context depth controls prose importance; research breadth controls how much external evidence must be gathered before drafting. Record one of:

- `COMPACT` — one or two authoritative anchors are enough for a brief origin/interpretation;
- `TRIANGULATED` — use independent source roles and more than one source type so that model origin, mechanism, scaling, and rigorous mathematics are not all inherited from a single secondary account;
- `DEEP` — treat the scientific lineage as a small research problem of its own: inspect canonical/original sources, authoritative reviews, model-reduction/scaling literature, rigorous mathematical bridge papers, and modern scientific work when it affects the theorem's interpretation. Reconcile notation, normalization, and parameter conventions before writing.

Default mapping:

- `NONE` → no research breadth;
- `ORIGIN_BRIEF` → `COMPACT`;
- `SUBSTANTIAL` → at least `TRIANGULATED`;
- `PHYSICS_LED` / `INTERDISCIPLINARY_LED` → normally `DEEP`.

Do not enforce an arbitrary citation count. Breadth is sufficient only when independent evidence closes the model-to-mathematics chain needed by the Introduction.

## 3. Build a context research dossier

Do not stop at the first convenient source. For `SUBSTANTIAL`, `PHYSICS_LED`, or `INTERDISCIPLINARY_LED`, cover the relevant evidence roles:

- `MODEL_ORIGIN` — original model, canonical monograph, or historical source;
- `MECHANISM` — authoritative explanation of the physical/biological mechanism;
- `REGIME_OR_SCALING` — why the parameter/scaling/limit is natural;
- `MATH_BRIDGE` — rigorous mathematical literature connecting the model to the analytic problem;
- `MODERN_CONTEXT` — later physical/scientific developments, experiments, or applications, only when they matter to the present theorem.

A role may be supported by several sources. The goal is triangulation, not a fixed citation count.
For `TRIANGULATED`/`DEEP`, record source type or family (original/canonical science, review/monograph, mathematical-physics bridge, modern scientific source, experimental source when relevant) and avoid letting one secondary source silently support every role.

Prefer, in order:
1. original or canonical scientific sources;
2. authoritative books/reviews/surveys;
3. rigorous mathematical-physics bridge papers;
4. high-quality modern scientific sources for current relevance.

Avoid using tertiary summaries as the sole support for nontrivial scientific claims.

## 4. Map model language to mathematics

Record explicitly:

- scientific object or observable;
- mathematical variable/function/domain/operator;
- parameter meaning and units or dimensionless role when relevant;
- boundary/initial condition meaning;
- distinguished scales or asymptotic regimes;
- conserved/monotone quantities if they drive the mathematics;
- the exact theorem feature that corresponds to a scientific statement.

If this map cannot be made, reduce context depth. Vague physical association is not enough.

## 5. Separate lineage from interpretation

Three claims require different evidence:

- `ORIGIN`: the equation/problem historically arose from a model;
- `INTERPRETATION`: a mathematical quantity represents a scientific observable;
- `CONSEQUENCE`: the theorem has a scientifically meaningful implication.

Do not turn an origin claim into a consequence claim. A theorem about a mathematical model does not automatically prove a statement about an experiment or physical system.

## 6. Context factuality ceiling

For every scientifically loaded statement, record:

- evidence anchor;
- strongest allowed wording;
- stronger wording that is not justified;
- whether the statement is historical, modeling, mathematical, or experimental.

Examples:
- allowed: `the first Dirichlet eigenvalue gives the squared fundamental frequency in the ideal membrane model`;
- forbidden: `the theorem determines the optimal real membrane` unless the modeling assumptions justify that conclusion.

## 7. Research stopping rule

Stop when the dossier explains the complete chain needed by the Introduction:

`phenomenon/origin → model → mathematical structure → relevant regime → prior mathematical frontier → present theorem → calibrated scientific interpretation`.

Do not continue collecting background that has no route back to the focal theorem.

## 8. Output

Produce `ScientificContextLedger`. No publication prose is written in this protocol.
