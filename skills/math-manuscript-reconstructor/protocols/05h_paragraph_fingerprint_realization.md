# Protocol 05h — Paragraph-Level Fingerprint Realization

## Purpose

Realize mathematics-driven paragraph boundaries and local prose density after semantics are locked. The `ProofGraph` and active mathematical obligations are mandatory inputs. A `ParagraphFingerprintLedger`, when available from a style corpus, is an optional abstract prior; without one, the universal rules in this protocol remain fully active. This pass changes paragraph boundaries and density only when the target proof graph permits it.

## 1. Paragraph-boundary question

Before every paragraph break ask:

> What mathematical state changed here?

A break should normally have a concrete answer: obligation, method, regime, legality, auxiliary-return, equality, substantial display consequence, conceptual pause, or closure.

If no answer exists, review whether the break is cosmetic fragmentation.

## 2. Paragraph-merge question

For adjacent paragraphs ask:

> Are these two paragraphs performing the same mathematical job under the same active hypotheses?

If yes, prefer merging unless a display or a genuine cognitive boundary makes separation clearer.

Do not merge across:
- a new assumption/regime;
- a nontrivial limit/interchange justification;
- a switch of proof mechanism;
- an equality/rigidity audit;
- return from an auxiliary lemma;
- a new local proof obligation.

## 3. Role-sensitive realization

### ROUTINE
Compress. One mathematical motion may occupy one or two sentences, often with a display. Do not pad for rhythm.

### STRUCTURAL
State the reduction or mechanism once, then execute it. Avoid a second paragraph that merely re-announces the same plan.

### DELICATE
Thicken locally. Put the exact permission, uniformity, topology, endpoint, or parameter dependence where it is used. Do not scatter the justification across later paragraphs.

### BRIDGE
Give the obstruction and the replacement tool together whenever possible. The paragraph should explain *why the proof changes mode*.

### SURPRISING
Permit a concise interpretive sentence only when it changes how the next argument is read.

### CLOSURE
Contract. Once the obligation is closed, stop unless equality/rigidity or an immediate corollary is a new obligation.

## 4. Opening discipline

Prefer openings that attach directly to mathematics:
- current object;
- active estimate;
- concrete operation;
- hypothesis/reason;
- exact local goal;
- obstruction/consequence.

Review paragraphs beginning with document administration such as repeated `We now`, `We next`, `The next step`, or `We proceed` when the phrase can be removed without losing a mathematical relation.

## 5. Internal movement discipline

A paragraph should usually have one dominant movement. If it contains two unrelated movements, split at the mathematical transition. If it has no movement beyond announcing future work, delete or merge it.

## 6. Display placement

A display may sit:
- inside the same paragraph when it executes the current motion;
- at a paragraph boundary when it closes one obligation and creates another.

Never create a paragraph break solely to make the page look varied.

## 7. Role-transition sanity check

After drafting a proof, inspect the abstract role sequence. Healthy sequences are driven by the proof graph and may contain long `ROUTINE` runs with occasional `STRUCTURAL`, `DELICATE`, or `BRIDGE` interruptions.

Flag for review, but do not automatically rewrite:
- every proof repeating the same role sequence;
- every paragraph having the same sentence count;
- every delicate issue compressed to routine length;
- every routine manipulation expanded to a full explanatory paragraph;
- a bridge with no stated obstruction;
- a closure followed by generic recap.

## 8. Numerical non-target rule

Never target source medians, variances, role proportions, or transition frequencies. Those measurements are diagnostic evidence only.

`ParagraphFingerprintLedger` must be implemented as **conditional editorial decisions**, not as a style score to optimize.

## 9. Cold-author compatibility

Run this pass before `COLD_AUTHOR`. Cold-author compression may merge or delete paragraphs, but it must preserve the mathematical reason for each retained boundary. Re-run paragraph-fingerprint audit after compression.

## 10. Gate

`PARAGRAPH-FINGERPRINT-FIDELITY: PASS` requires:
- paragraph boundaries have mathematical reasons;
- role-sensitive density remains visible;
- paragraph openings are not dominated by administrative signposting;
- delicate legality is locally thick enough to audit;
- routine prose is not padded for symmetry;
- no numerical style matching or source paragraph template reuse occurred.
