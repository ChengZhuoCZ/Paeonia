# Protocol 02c — Theorem Statement Architecture

## Purpose

Turn the mathematics that has actually survived `ProofCoreGate` into the cleanest reader-facing theorem hierarchy. This is **not** a proof-discovery step and not a place to strengthen claims.

The source manuscript may contain theorem packages that reflect chronology, local notation, or engineering history. Discard that packaging. Rebuild theorem statements from the closed `MathLedger`, the final proof body, and the target audience.

## Two-layer rule

Before proof drafting, use only working semantic targets such as `CLAIM-MAIN`, `CLAIM-QUANTITATIVE`, and `CLAIM-RIGIDITY`. These are proof obligations, not publication theorem prose.

After `ProofCoreGate: PASS`, create `TheoremStatementLedger` and decide the final theorem hierarchy.

## Theorem-unit decision

A result belongs in the same theorem when:
- it uses essentially the same hypotheses and normalization;
- the stronger clause clarifies rather than obscures the main result;
- the reader benefits from seeing the conclusion as one mathematical object;
- equality or rigidity is inseparable from the sharp statement.

Split results when:
- a quantitative strengthening requires extra assumptions or notation;
- the main qualitative theorem is hidden by constants, expansions, or remainder terms;
- rigidity/equality requires an additional argument worth isolating;
- a structural theorem is reusable independently of the final global result;
- a corollary is conceptually important but logically immediate.

Do not split merely to create more named results, and do not fuse results merely to advertise one large theorem.

## Reader order

Default hierarchy when the mathematics supports it:

1. the clean qualitative or global statement the reader came for;
2. the quantitative/structural theorem that explains or strengthens it;
3. equality, rigidity, classification, or uniqueness when not already intrinsic;
4. immediate consequences.

Reader order may differ from proof chronology.

## Assumption discipline

For every theorem unit:
- list every nonstandard hypothesis required for the conclusion;
- remove assumptions used only by one proof implementation but not by the theorem itself;
- do not hide a substantive assumption behind `as above`, `under the standing assumptions`, or distant prose unless the target venue and local context make it genuinely unambiguous;
- keep parameter ranges exact;
- preserve endpoint exclusions and exceptional cases;
- distinguish hypotheses needed to *state* an object from hypotheses needed only to *prove* the result.

## Normalization discipline

Choose the normalization that makes the theorem mathematically natural and easiest to compare with the literature. When scaling or invariance makes several normalizations equivalent, state one canonical form and explain the equivalence outside the theorem if needed.

Do not let a normalization chosen for one technical lemma dictate the main theorem statement.

## Quantitative clauses

A quantitative theorem must make visible:
- the quantity being estimated;
- the parameter range;
- the norm or topology;
- constant dependence;
- remainder order and uniformity when claimed;
- whether the estimate is sharp, asymptotic, effective, or merely qualitative.

Do not bury the main conclusion under proof-only constants.

## Equality, rigidity, and classification

If equality matters, the theorem statement must identify precisely:
- the equality condition;
- the equivalence relation (rigid motion, scaling, additive constants, relabeling, symmetry group, etc.);
- whether necessity and sufficiency are both proved;
- whether classification is global or only local/conditional.

Never let the Introduction claim a rigidity/classification stronger than the formal theorem unit.

## Naming and theorem subtitles

Use descriptive theorem subtitles only when they materially help navigation among several major results. Do not add subtitles mechanically. Prefer a clean `Theorem 1.1` over a decorative title that merely repeats the conclusion.

## Integrity checks

`TheoremStatementLedger` must certify:
- no mathematical strengthening relative to closed claims;
- no dropped hypothesis;
- no parameter-range drift;
- no equality/rigidity loss;
- no theorem duplication under different names;
- no theorem fragmentation without reader benefit;
- theorem order follows reader significance rather than source numbering.

If any check fails, repair the theorem architecture, not the proof prose.
