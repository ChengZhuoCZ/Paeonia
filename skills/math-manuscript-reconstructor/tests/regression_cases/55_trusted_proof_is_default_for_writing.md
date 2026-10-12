# Case 55 — Supplied proof is trusted by default during writing

## Requirement

When the user supplies a proof and asks for manuscript writing rather than correctness verification, the skill must assume the proof is mathematically correct and reconstruct it directly.

The writing workflow must not independently search for gaps, counterexamples, or proof failures. `ProofCoreGate` checks faithful coverage and semantic preservation relative to the trusted proof source.

Correctness verification activates only when explicitly requested. Literal absent source content is `SOURCE-MISSING`, not an inferred proof gap.
