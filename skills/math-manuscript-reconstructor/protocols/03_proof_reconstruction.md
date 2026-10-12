# Protocol 03 — Proof Reconstruction

## Principle

A proof is reconstructed around its mathematical mechanism, not around the chronological order in which the source discovered it. In ordinary `trusted_source` writing, the supplied proof is assumed correct; reconstruction does not include independent gap hunting or re-proving.

## Procedure

1. Identify the local target internally; state it in prose only when the reader needs it.
2. If the proof is non-obvious, expose the decisive invariant/estimate/compactness idea in one compact sentence.
3. Use the canonical symbols fixed in `NotationLedger`, and introduce only notation needed for that mechanism.
4. Execute constructions and estimates in dependency order.
5. After a key display, state its mathematical consequence rather than paraphrasing the formula.
6. Group routine calculations around the mechanism they support.
7. Make all genuine branch points explicit; do not create artificial numbered steps.
8. Track the source-supplied exact assumptions at the point of use.
9. Track equality through every inequality when rigidity matters.
10. End with the actual closure step, not a generic recap.

## Compression rule

A calculation may be compressed only if a specialist can reconstruct it from named standard facts or if the omitted algebra is genuinely routine and no sharp constant/equality information depends on it.

## Citation-compression after proof-core drafting

After the proof core has been written, before `ProofCoreGate`, apply [Protocol 07a](07a_exact_theorem_citation_compression.md) to material duplicated proof obligations in **authorized editable scope**. A primary-text-verified external theorem with an exact result locator can replace the portion it actually establishes; keep any unmatched rate, equality case, quantitative constant, bridge or new idea. This phase is not an independent correctness audit of trusted user proof content. Do not replace with an inaccessible or merely similar reference.

## Appendix rule

Move material to an appendix only when it is technically bulky and conceptually secondary. Do not exile a decisive mechanism merely to shorten the main text.

## Composition order

This protocol is invoked during `ProofCoreDrafting`, before final theorem packaging, Introduction, and Abstract. See `02a_proof_first_composition.md`.
