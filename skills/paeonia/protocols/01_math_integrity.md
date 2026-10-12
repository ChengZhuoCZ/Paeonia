# Protocol 01 — Mathematical Integrity and Semantic Fidelity

## Default composition mode

For ordinary writing from a user-supplied proof, use `proof_correctness_mode: trusted_source`.

In this mode, the proof's mathematical validity is accepted as an input assumption. This protocol protects **semantic fidelity**: the reconstructed paper must say exactly what the trusted proof says, without strengthening, weakening, dropping hypotheses, or changing normalizations.

Independent correctness verification is **not** performed unless the user explicitly requests `verify_proof` behavior.

## Semantic invariants

For every major claim preserve:
- ambient space/domain;
- dimension;
- regularity class;
- normalization;
- quantifiers;
- parameter ranges;
- hypotheses;
- conclusion;
- uniqueness/equality classification;
- constant dependence;
- asymptotic regime;
- topology/norm of convergence when applicable.

## Dangerous editorial substitutions

Never silently replace:
- “for sufficiently large N” by “for all N”;
- “there exists c(N)>0” by “there exists an absolute c>0”;
- “subsequence” by “sequence”;
- “weak convergence” by “strong convergence”;
- `O(N^{-3})` by `o(N^{-3})`;
- non-strict by strict inequality;
- local minimizer by global minimizer;
- formal expansion by a stronger theorem than the source states.

## Trusted-source handling

In `trusted_source` mode:
- do not independently search for proof gaps;
- do not re-prove compressed or difficult steps;
- do not classify a step as heuristic merely because the model cannot verify it quickly;
- do not emit `MATHEMATICAL-CHECK` for mathematical validity;
- accept source-specified mathematical external inputs as valid for reconstruction;
- use `SOURCE-MISSING` only when the source literally lacks content needed to reproduce what it refers to.

Trusted-source mode does not authorize inventing absent mathematics.

## Explicit verification mode

Only when the user explicitly requests correctness checking, gap finding, referee simulation, mathematical repair, or independent verification, switch to `proof_correctness_mode: verify_proof`.

Then use exactly one of:
- `MATHEMATICAL-CHECK: unresolved`;
- `MATHEMATICAL-CHECK: repaired` with a separate justified derivation;
- `MATHEMATICAL-CHECK: external input required`.

Polish never upgrades the status of a claim.
