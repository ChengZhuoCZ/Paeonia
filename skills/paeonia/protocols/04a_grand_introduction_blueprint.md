# Protocol 04a — Grand Mathematical Introduction Blueprint


> **Optional extended module.** Protocol 04 is authoritative. Use this blueprint only for an unusually complex, literature-heavy, or genuinely program-level Introduction. An ordinary Introduction uses `IntroductionCoreBrief` and does not require an `IntroductionNarrativeLedger`, scale label, theorem ladder, adjacent-problem bridge, or macro–micro–macro arc.

## Purpose

Build the Introduction only after the proof core is closed and the theorem frame is semantically stable. The goal is not to make the prose sound grand. The goal is to locate the exact theorem inside a larger mathematical landscape without overstating what has been proved.

This protocol produces an internal `IntroductionNarrativeLedger`. It contains no publication prose. If a source manuscript already contains an Introduction, extract only claims, terminology, citation candidates, and facts to verify; do not preserve its prose or paragraph sequence. Final Introduction prose will be reconstructed from scratch.

## 1. Select the introduction scale

Choose one of:

- `STANDARD` — a focused technical contribution, local refinement, or paper whose context is already standard to its intended audience;
- `EXPANSIVE` — a substantial new method, a significant strengthening, or a paper connecting several established strands;
- `GRAND` — a theorem resolving or materially advancing a classical conjectural line, a global classification/rigidity result, a new framework with broader reach, or a result whose significance is best understood through a larger historical and conceptual arc.
- `GRAND_PLUS` — exceptional, evidence-supported program-level positioning: for example a verified conjecture resolution, complete global classification, closure of the last major range of a program, first genuinely global theorem after a substantial partial theory, or a method with clear structural reach beyond the focal problem.

Scale is determined by the mathematics and verified literature. It is never selected to imitate a reference Introduction. When this optional extended route is triggered by a real positioning problem, final scale selection may be audited in `NarrativeAmbitionLedger` via Protocol 04h. Build `MathematicalStoryLedger` via Protocol 04n only when an operative parent program or scale/category transition is needed; an `EXPANSIVE`, `GRAND`, or `GRAND_PLUS` label alone is not a sufficient trigger.

## 2. Fix the audience and opening budget

Record the intended research audience before deciding how much background belongs in the Introduction. For a specialist audience, standard PDE/spectral definitions, routine functional analysis, and notation dictionaries should be compressed or moved to the body unless they are needed to state the focal problem or explain the new mechanism. **Scientific or physical context is decided separately by Protocol 04k.** Do not suppress scientifically operative model background merely because the intended reader is an expert.

Choose an opening function from `CANONICAL_PRINCIPLE`, `PARENT_PROGRAM`, `CANONICAL_PROBLEM`, `LANDMARK_RESULT`, `CONJECTURE`, `STRUCTURAL_TENSION`, `LIMITING_THEOREM_AND_FINITE_GAP`, `PARALLEL_EXTREMAL_FAMILY`, `PHENOMENON`, `PHYSICAL_ORIGIN`, `SCIENTIFIC_MODEL`, or `DISCRETE_CONTINUUM_TENSION`. The last three require a supported `ScientificContextLedger`. The opening must create a concrete mathematical stake and a directional pull toward the focal theorem.

## 3. Build the narrative geometry

For `EXPANSIVE`, `GRAND`, or `GRAND_PLUS`, prefer a conditional macro–micro–macro movement:

1. `MACRO` — identify the parent mathematical program or canonical principle, not merely the field name;
2. `NARROWING` — move through the relevant classical axis, conjectural axis, or modern best-known result;
3. `FOCAL_POINT` — state the exact problem and expose the principal theorem as soon as it is readable;
4. `RE_EXPANSION` — explain the theorem's conceptual, methodological, or neighboring-problem significance;
5. `MECHANISM` — compress the finished proof into a mathematical mechanism chain.

Omit any stage that has no real mathematical work to do.

## 4. Build the ProblemTensionMap

Record:

- `desired_statement` — what one would like to prove;
- `natural_route` — the most natural prior method or comparison principle;
- `failure` — where that route stops;
- `structural_obstruction` — the mathematical reason for failure;
- `replacement_viewpoint` — the representation, variable, compactness principle, reduction, or engine introduced in this paper;
- `payoff` — which formerly inaccessible step becomes possible.

The Introduction should never use generic difficulty claims when the obstruction can be stated mathematically.

## 5. Build the ResultHierarchy

Classify the closed results by reader-facing role rather than proof chronology:

- `motivating_conjecture_or_problem`;
- `first_structural_result`;
- `quantitative_engine`;
- `main_global_result`;
- `rigidity_or_equality`;
- `corollaries_or_extensions`.

Not every paper has all roles. The theorem ladder should reflect cognitive importance, not the order in which lemmas were discovered or proved.

## 6. Build the LiteratureLandscape

Every cited work used in the Introduction must have a narrative role:

- `ORIGIN`;
- `CLASSICAL_LANDMARK`;
- `CONJECTURE`;
- `BEST_PRIOR_RESULT`;
- `ADJACENT_BREAKTHROUGH`;
- `TECHNICAL_PRECURSOR`;
- `NUMERICAL_EVIDENCE`;
- `LOCAL_RESULT`;
- `GLOBAL_RESULT`;
- `FAILED_OR_INSUFFICIENT_ROUTE`.

For each item record the exact verified claim and why it belongs at this point in the story. Chronological bibliography dumps are forbidden.

## 7. Adjacent-problem bridges

Use a neighboring problem only if it sharpens the current paper's position. Record:

- shared structure;
- known result on the neighboring problem;
- methodological relation;
- decisive difference;
- relevance to the current theorem.

Delete an adjacent-problem excursion that does not change the reader's understanding of the present obstruction, theorem, or method.

## 8. Proof mechanism narrative

Build a short mechanism chain from the closed proof graph. Prefer mathematical transformations and reductions, for example:

`geometric normalization → fixed-domain pullback → symmetry reduction → spectral/variational reduction → quantitative estimate → rigidity/endgame`.

The actual chain must be induced by the target proof. Do not copy a mechanism sequence from any reference paper.

## 9. Repetition policy for the main result

The principal result may appear in three distinct functions:

- `ORIENTATION` — a concise conceptual summary;
- `FORMAL_STATEMENT` — the exact theorem;
- `INTERPRETATION` — what the theorem means for the surrounding problem.

Literal restatement after the formal theorem is forbidden.

## 10. Mathematical-story branch

When the theorem-facing arc depends on an operative parent program or scale/category transition, apply `protocols/04n_mathematical_story_discovery.md` before any extended paragraph planning. Build `MathematicalStoryLedger` independently of the scientific-context decision.

The story ledger must identify, when supported:

- the focal theorem, focal problem, parent program, and canonical principle;
- the primary structural archetype such as continuum→finite complexity, limit→exact finite, local→global, qualitative→quantitative, or symmetry→rigidity;
- the exact scale transition and why it is not routine;
- the mathematical ancestry needed to make the theorem's position visible;
- the theorem's consequence for the parent program.

A paper with rich scientific context may still fail this branch if its mathematical ancestry remains invisible. A pure-math paper may satisfy it with no scientific context at all.

## 11. Scientific-context branch

Before finalizing the ledger, apply `protocols/04k_scientific_context_research.md` whenever the theorem or focal model has a genuine scientific lineage. Scientific context depth is independent of Introduction scale. A `GRAND_PLUS` pure-math paper may have `NONE`; a mathematically narrower model paper may have `PHYSICS_LED`.

When triggered, the `ScientificContextLedger` becomes an input to paragraph planning through `protocols/04l_scientific_context_integration.md`.

## 12. Output

Produce `IntroductionNarrativeLedger` only for the extended route. Produce `MathematicalStoryLedger` when its trigger is present. Use Protocol 04d and `IntroductionParagraphPlan` only when multiple theorem, literature, or model threads make direct composition unreliable. Otherwise return to Protocol 04 and draft directly from `IntroductionCoreBrief`. No final Introduction prose is written in this protocol.
