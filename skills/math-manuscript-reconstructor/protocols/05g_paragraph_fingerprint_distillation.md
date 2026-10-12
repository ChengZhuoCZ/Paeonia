# Protocol 05g — Paragraph-Level Author Fingerprint Distillation

For Introduction/outline work, [Protocol 04p](../protocols/04p_reformulation_and_proof_explanation.md) qualifies research compression: retain necessary explanations of novel objects, reformulation gains, and proof dependencies.

## Purpose

This protocol extracts **paragraph-scale mathematical exposition decisions** from a user-supplied style corpus. It does not copy paragraph templates, preserve source paragraph boundaries, or optimize toward a numerical authorship signature.

The output is `ParagraphFingerprintLedger`, a third style layer alongside `LanguageStyleLedger` and `MathematicalWritingStyleLedger`.

## 1. Unit of analysis

A paragraph is treated as a **semantic work unit**, not a block of a target length. For every sampled paragraph, identify only abstract features:

- mathematical role: `ROUTINE`, `STRUCTURAL`, `DELICATE`, `SURPRISING`, `BRIDGE`, `CLOSURE`;
- local proof obligation;
- reason a paragraph boundary exists;
- opening mode;
- display adjacency pattern;
- explicitness load;
- internal movement;
- closing/handoff mode;
- relation to the next paragraph.

Never store source sentences, distinctive phrases, or full source paragraph skeletons.

## 2. Boundary-reason taxonomy

Record whether stable paragraph boundaries tend to occur at genuine mathematical events:

- `OBLIGATION_SHIFT` — the proof starts a new sub-obligation;
- `METHOD_SHIFT` — a different tool or representation becomes necessary;
- `REGULARITY_SHIFT` — smooth/model case gives way to rough/general case;
- `REGIME_SHIFT` — parameter, sign, scale, or geometric regime changes;
- `LEGALITY_CHECK` — limit/interchange/compactness/uniformity needs its own justification;
- `AUXILIARY_RESULT_RETURN` — the argument returns from a lemma to the main line;
- `DISPLAY_CONSEQUENCE` — a substantial display changes the state of the proof;
- `EQUALITY_RIGIDITY` — sharpness/equality propagation becomes the new obligation;
- `CONCEPTUAL_PAUSE` — a short interpretation reduces later cognitive load;
- `CLOSURE` — the mathematical obligation ends.

A new paragraph is **not** justified merely because the preceding paragraph is long.

## 3. Merge taxonomy

Record when the corpus tends to keep material in one paragraph:

- consecutive routine manipulations serving one obligation;
- a short setup followed immediately by its display and consequence;
- a one-step application whose hypotheses are already active;
- symmetric/parallel calculations with no new condition;
- closure that needs no interpretive afterword.

This becomes a merge policy, not a paragraph-length target.

## 4. Opening-mode extraction

Classify paragraph openings by function:

- `OBJECT_LED` — begins from the mathematical object/fact already in play;
- `ACTION_LED` — begins with a concrete mathematical operation;
- `PREMISE_LED` — begins from a reason or hypothesis;
- `GOAL_LED` — begins from the exact local obligation/reduction;
- `CONTRAST_BRIDGE` — names the failure/change forcing a new method;
- `CONSEQUENCE_LED` — begins from what the preceding paragraph earned;
- `RETURN_LED` — returns from an auxiliary argument;
- `META_LED` — administrative signposting.

The fingerprint should prefer functional openings over `META_LED` openings when the corpus supports that behavior.

## 5. Internal paragraph movement

For each role, extract common abstract movements, for example:

- `ROUTINE`: action → display/estimate → immediate consequence;
- `STRUCTURAL`: local goal → reduction/mechanism → new state;
- `DELICATE`: issue → permission/estimate → limit/compactness conclusion;
- `BRIDGE`: obstruction → replacement tool → resumed main line;
- `SURPRISING`: result → concise interpretation → return;
- `CLOSURE`: final implication → stop.

Do not save exact sentence order from a source paragraph. Save only the movement class.

## 6. Role-pressure profile

Aggregate paragraph size and sentence-count statistics **by role**, because the important signal is asymmetry.

Allowed evidence:
- medians/quantiles;
- ratios such as `delicate_median / routine_median`;
- role-transition counts;
- one-paragraph-proof fraction;
- paragraph-count distribution by proof.

Forbidden use:
- generating paragraphs to hit a median word count;
- forcing a target variance;
- changing mathematics to match a role distribution;
- using a classifier score as an authorship detector.

Statistics are evidence that a policy exists; they are not the policy.

## 7. Paragraph-transition graph

Build an aggregate directed graph between paragraph roles. Use it to identify stable proof rhythm, for example:

`STRUCTURAL → ROUTINE`, `ROUTINE ↔ DELICATE`, `BRIDGE → ROUTINE`, `ROUTINE → CLOSURE`.

Interpretation matters more than frequency. The graph is used to notice that a difficult proof may contain long stretches of routine motion interrupted by thicker legality or bridge paragraphs.

Never reproduce a source proof's exact role sequence as a template.

## 8. Burstiness as mathematical load

Extract whether the corpus alternates between thin and thick paragraphs according to proof pressure. Record:

- routine compression;
- thickening near nontrivial legality/parameter choices;
- short paragraphs after a difficult estimate when the consequence is immediate;
- whether interpretive pauses are rare and purposeful;
- whether closure typically contracts.

Call this `mathematical_burstiness`. It is not random sentence/paragraph variation.

## 9. Display adjacency

For displays, classify surrounding prose:

- setup before display;
- no setup when formula is self-evident from the active sentence;
- direct mathematical consequence after display;
- local legality after display when needed;
- forbidden restatement of the display in words.

Paragraph boundaries around displays should follow the change in proof obligation, not typography alone.

## 10. Stratified evidence

Sample across at least:
- short proofs;
- long proofs;
- approximation arguments;
- contradiction arguments;
- parameter splits;
- technical estimates;
- equality/rigidity arguments when available;
- theorem-to-lemma and lemma-to-mainline returns.

A paragraph trait receives `strong` support only when it survives across distinct mathematical functions.

## 11. Research projection

When the style corpus is pedagogical but the target is a research article:

- keep paragraph boundary logic;
- keep local obstruction and legality paragraphs;
- keep load-driven asymmetry;
- compress reader coaching, examples, exercises, and elementary reminders;
- do not import textbook-length conceptual pauses wholesale.

Invariant: **retain paragraph decisions caused by mathematics; compress paragraph decisions caused by pedagogy.**

## 12. Independence

The fingerprint is successful only if a new manuscript can realize similar paragraph-scale decision rules with independently generated prose and independently chosen paragraph boundaries.

Run source/style overlap audit after realization. A paragraph fingerprint is not permission to reconstruct a source paragraph sequence.
