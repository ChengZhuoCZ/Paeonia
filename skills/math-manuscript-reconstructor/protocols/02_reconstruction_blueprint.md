# Protocol 02 — Reconstruction Blueprint

The blueprint is a new design document created from the dependency graph **after the proof core has passed its closure gate**. It organizes the reader-facing manuscript around mathematics that has already been proved.

## Required fields

1. Reader entry point: what must be understood first?
2. Main theorem placement.
3. Minimal notation layer.
4. Core mechanisms, each with a one-sentence mathematical role.
5. Dependency DAG.
6. Candidate section architectures A and B for nontrivial papers.
7. Chosen whole-paper proof spine and why it is superior.
8. Main-result exposure mode versus proof-activation point.
9. Qualitative technical-core shape and pressure peaks.
10. Material moved to appendix, its owner/import, and modularity reason.
11. Claims merged or demoted from displayed lemmas.
12. Equality/rigidity path.
13. Mathematically justified endpoint of the paper.

## Architecture objective

Minimize the cost

`forward references + duplicated hypotheses + theorem fragmentation + notation churn + appendix jumps + duplicated theorem exposure + artificial whole-paper symmetry + bookkeeping prose`.

Do not optimize for resemblance to the source.

## Proof-first constraint

`ReconstructionBlueprint` is not allowed to dictate proof content retroactively. If the desired section architecture conflicts with the closed `ProofGraph`, change the manuscript architecture rather than forcing an artificial proof order.
