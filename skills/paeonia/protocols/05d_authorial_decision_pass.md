# Protocol 05d — Authorial Decision Pass

## Purpose

Make prose density, explicitness, and local explanation reflect mathematical importance rather than document templates.

The central rule is:

> **Do not make the prose look less generated. Make the mathematical decisions more authored.**

## 1. Classify each proof paragraph

Assign one dominant class before rewriting.

### ROUTINE
Standard algebra, substitution, one-line differentiation, direct invocation of a just-proved identity.

Default treatment: compress aggressively. Let formulas carry the work.

### STRUCTURAL
A reduction, normalization, decomposition, choice of coordinates, factorization, or proof mechanism that changes what problem is being solved.

Default treatment: one clear sentence naming the move and its purpose.

### DELICATE
A step involving nontrivial legality or uniformity: interchange of limits, compactness, endpoint behavior, parameter choice, nonvanishing denominators, equality propagation, approximation topology, weak/strong convergence, or a sharp constant.

Default treatment: explain enough for a specialist to audit the step locally.

### SURPRISING
A conclusion whose force is not obvious from the calculation: an unexpected rigidity, cancellation, localization, monotonicity, or structural interpretation.

Default treatment: one concise interpretive sentence when it reduces later cognitive load.

### BRIDGE
A transition between methods, regularity classes, scales, cases, or model/general settings.

Default treatment: state the exact obstruction in the old regime and the mechanism that makes the new regime work.

### CLOSURE
The point at which a claim, equality case, or global assembly is complete.

Default treatment: stop promptly. Do not recap unless the closure itself needs identification.

## 2. Controlled explicitness

### MUST_EXPLICIT
Write the reason when it is nontrivial and necessary for auditability:
- limit/integral or derivative/integral interchange;
- application conditions of an external theorem;
- parameter choices balancing competing errors;
- compactness extraction and topology;
- normalization dependence;
- equality or rigidity propagation;
- endpoint arguments;
- uniformity of constants;
- passage from a dense subclass to the target class when topology matters.

### MAY_BE_IMPLICIT
Usually compress when locally routine:
- one-step algebraic rearrangement;
- direct substitution;
- a differentiation whose formula is immediate;
- an identical argument in a genuinely symmetric regime;
- invocation of a result proved immediately above when no condition changes.

### SHOULD_BE_IMPLICIT
Delete explanatory prose that adds no mathematical information:
- symbol-by-symbol display paraphrase;
- elementary arithmetic not tied to a sharp constant;
- repeated definitions already active in the local context;
- repeated assertions that a standard one-line operation is simple.

## 3. Density allocation

Do not equalize paragraph size.

Preferred allocation:
- `ROUTINE`: minimal prose;
- `STRUCTURAL`: concise but explicit;
- `DELICATE`: highest justification density;
- `SURPRISING`: concise interpretation after closure of the calculation;
- `BRIDGE`: explicit obstruction/mechanism sentence;
- `CLOSURE`: shortest possible ending.

Variation must be caused by mathematical load, not randomization.

## 4. Lemma and theorem decisions

Before isolating a statement, answer: what does this separation buy the reader or the proof?

Isolate only if it:
- removes a real obstruction;
- packages a reusable mechanism;
- separates a technically different argument;
- exposes a structural fact used later;
- protects the main line from subordinate bulk.

Do not create a lemma merely to break a long page or imitate a conventional paper shape.

## 5. Authorial decision record

For substantial rewrites, maintain an internal `AuthorialDecisionReport` containing:
- passages compressed as routine;
- delicate steps deliberately expanded or preserved;
- empty signposting removed;
- lemmas merged or retained with mathematical reason;
- bridges rewritten around explicit obstructions;
- any passages kept despite recurrence because standard wording is the clearest choice.

## 6. Pass condition

`AUTHORIAL-DECISION: PASS` requires that a reader can see why prose density changes where it does. A uniform manuscript is not automatically bad, but unexplained uniformity across mathematically unequal passages triggers review.
