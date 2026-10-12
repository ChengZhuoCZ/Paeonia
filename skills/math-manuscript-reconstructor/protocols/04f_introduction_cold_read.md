# Protocol 04f — Introduction Cold Read and Reader Contract

## Purpose

Evaluate the frozen Introduction from the reader's side. The mathematics and theorem statement are fixed. Repair the earliest missing inference rather than automatically adding context, literature, stages, or adjectives.

## 1. Seven-question reader contract

Read only the Introduction. The intended specialist should be able to answer:

1. What is the exact mathematical problem?
2. What benchmark, theorem, model, or conjecture makes it natural?
3. What was the strongest relevant position before this paper?
4. What exactly remained unknown?
5. What exactly does the present theorem prove?
6. Why is it not a routine consequence of the benchmark theory?
7. What central idea makes the result possible, and what changes in the mathematical picture?

The answers need not occupy separate paragraphs. If an answer can be supplied only from the proof body or from the evaluator's prior knowledge, the Introduction has not yet supplied it.

## 2. First-page and theorem-latency test

Check whether the exact problem and narrowing direction appear before generic exposition becomes long. The theorem should appear as soon as it is accurately readable; page 2 is entirely natural when benchmark, restriction, frontier, and minimal notation genuinely require it.

For every pre-theorem paragraph ask:

> Which fact needed to understand the statement or its significance disappears if this paragraph is removed?

Delete, merge, or move any paragraph whose answer is merely `history`, `importance`, `breadth`, or `atmosphere` without a theorem-facing relation.

## 3. Swap test

Mentally replace the paper-specific nouns by generic placeholders. Flag a paragraph that would remain plausible for many unrelated papers.

Repair generic paragraphs with a non-transferable mathematical relation: the exact restriction, missing implication, lost structure, endpoint, equality case, scale change, or new control.

## 4. Paragraph-removal and question-chain test

The legacy **Paragraph-removal test** is retained here as the detachability component of the broader question-chain test.

For each paragraph ask:

- What new inference does it enable?
- What mathematical question does its ending leave for the next paragraph?
- Does the next paragraph answer that question or change the same object?

Administrative transitions do not repair a missing relation. An effective paragraph may integrate several functions; do not split it merely to enforce one role per paragraph.

## 5. Literature test

Each citation cluster must establish a benchmark, frontier, obstruction, precursor, or neighboring result that changes the present problem. Compress author chronology and repeated `does not cover our case` statements. State positively what prior work proves and identify the exact gap once.

## 6. Theorem and interpretation test

Check that orientation, formal statement, and interpretation do different work. The strongest theorem must not be buried beneath secondary refinements. Post-theorem prose should explain a non-obvious consequence, exact strength, or change in viewpoint rather than translate the display into English.

## 7. Proof-resolution test

The proof overview should expose the conceptual hinge and the few stage interfaces needed to understand why the argument closes. Remove bookkeeping, section-by-section narration, proof-local labels, routine case lists, and technical names that do not explain their output.

Do not compress away:

- the original meaning of a new representation;
- the operation at the bottleneck;
- the control it unlocks;
- the remaining global, nonlinear, endpoint, or rigidity step.

Apply Protocol 04q only when the proof route remains nonroutine after this compact test.

### 7A. Conditional PDE cold read

When Protocol 04t is active, use only the applicable items in `checklists/pde_introduction_reader_contract.md`. At minimum, verify that the reader can recover every theorem coordinate on which novelty depends, the exact multi-axis result delta, the role of emphasized assumptions, and the interface that closes the PDE argument. Distinguish theorem boundaries, method boundaries, known counterexamples, and open regimes.

Genre-specific checks are conditional: global-existence papers should link the a priori quantity to the continuation criterion; stability/scattering papers should link the linear mechanism to nonlinear closure and the final topology; singular-limit papers should name topology and relevant defect/multiplicity control; nonuniqueness papers should preserve the exact solution/admissibility class; regularity papers should expose the branch or singular-set architecture. Do not penalize a paper for omitting an irrelevant coordinate.

## 8. Voice and ending test

Read the first and last sentence of every paragraph in sequence. They should form a coherent mathematical argument, not a sequence of ledger labels or generic importance claims.

The Introduction may end with the conceptual proof overview, a brief organization paragraph when navigation is genuinely useful, or a tightly connected consequence/open direction. Do not append a ceremonial summary duplicating the Abstract.

## 9. Output

Return the revised Introduction and `Introduction Reader Contract Audit`. Record:

- the seven recoverable answers;
- any earliest missing inference;
- paragraphs removed or merged;
- any factuality or scope limit that must remain explicit;
- when the PDE branch is active, any unresolved theorem coordinate, result-delta axis, assumption role, closure interface, or typed boundary.

Do not report numeric style scores or claim that a static detector certifies prose quality.
