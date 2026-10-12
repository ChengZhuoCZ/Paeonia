# Protocol 02a — Proof-Body-First Composition

## Constitutional rule

The proof body is the first manuscript prose drafted. Everything before it is an internal mathematical artifact, not publication prose.

The skill distinguishes:

- **internal claim specification**: exact semantic target such as `CLAIM-MAIN`; allowed before proof drafting;
- **proof-core prose**: the first publication-style prose; required before front matter;
- **final theorem framing**: theorem names, displayed statements, corollary packaging; finalized only after proof closure;
- **front matter**: title prose, abstract, introduction, literature narrative, roadmap; written after `ProofCoreGate: PASS`.

The final PDF may present theorem statements and the introduction before the proofs. The rule concerns composition order, not reading order.

## Proof-first sequence

1. Lock `MathLedger` and semantic checksums relative to the trusted source claims.
2. Fix the single voice under Protocol 05p, without user style-selection questions. Apply Protocol 05o only if a user-selected author or style corpus has already been supplied; if activated, resolve identity, legally retrieve and version-lock sources, create `AuthorCorpusDossier`, and treat it as subordinate abstract style evidence only.
3. If a style corpus is supplied or acquired, distill `LanguageStyleLedger` and `MathematicalWritingStyleLedger`, then quarantine the corpus. This is internal analysis, not manuscript prose.
4. Build `ProofGraph` from genuine mathematical dependencies.
5. Create a `ProofBodyBlueprint` containing only proof-bearing units, then actively select field-native and structural notation using Protocol 02h / Pass 5a; record salient decisions in `NotationLedger`, before publication proof prose.
6. Draft foundational proof units from the leaves of the graph using the abstract style ledgers.
7. Draft intermediate mechanisms and transfer statements.
8. Draft the global assembly / main proof.
9. Carry through the source-supplied equality, rigidity, endpoint, compactness, and constant-dependence branches to their stated closure.
10. Run `ProofCoreGate`.
11. Only after `PASS`, synthesize final theorem packaging and manuscript front matter.

## Why this order is mandatory

Writing the introduction first creates three recurring risks:

- the manuscript promises a stronger theorem than the proof closes;
- the proof is forced into a prematurely chosen narrative architecture;
- novelty and mechanism claims are inferred from intention rather than from the completed argument.

Proof-first composition reverses this dependency: the front matter summarizes a mathematical object that already exists.

## ProofBodyBlueprint fields

```yaml
principal_claims:
proof_nodes:
proof_edges:
leaf_inputs:
external_dependencies:
decisive_mechanisms:
case_splits:
parameter_regimes:
equality_rigidity_path:
endpoint_path:
constant_dependency_path:
appendix_candidates:
known_blockers:
```

## Drafting rule inside the proof core

For each proof unit:

1. identify the local target;
2. expose the decisive mathematical move when non-obvious;
3. introduce only the notation needed for that move;
4. execute estimates/constructions in dependency order;
5. explain why a displayed relation advances the proof;
6. branch only when the mathematics genuinely branches;
7. close the exact target and propagate any equality information.

Do not write a miniature introduction before every lemma.

## Exact-theorem citation compression before ProofCoreGate

Run **Pass 6a / Protocol 07a** on substantive repeated proof obligations in the editable proof body. The result is a shorter *but fully supported* proof, or retention of the original argument when no verified exact external theorem applies. Do not treat a citation to an abstract, whole paper or uninspected lemma number as coverage; keep the assumption-to-conclusion mapping and any unmatched estimates.

## ProofCoreGate

In the default `trusted_source` mode, `PASS` means that every principal proof path supplied by the source has been faithfully reconstructed through its stated closure. Use source-relative statuses such as:

- `TRUSTED-SOURCE-CLOSED`;
- `TRUSTED-SOURCE-EXTERNAL-INPUT`;
- `USER-AUTHORIZED-ASSUMPTION` when the requested paper explicitly treats it as an assumption.

Do not downgrade a source step to `MATHEMATICAL-CHECK`, `HEURISTIC`, or `UNVERIFIED-STANDARD` merely because the skill has not independently re-proved it. `SOURCE-MISSING` is a blocker only when the underlying source content is literally unavailable.

If the user explicitly requests `verify_proof`, use the stricter independent-validity gate: principal paths must be proved, verified externally, or explicitly assumed, and unresolved `MATHEMATICAL-CHECK` items block front matter.

Before `PASS`, do not draft final-form Abstract or Introduction.
