# Protocol 01a — Trusted-Proof Direct Writing Mode

## Default rule

For an ordinary manuscript-writing request based on a proof supplied by the user, treat the supplied proof as **mathematically correct, complete for its intended claim, and admissible for reconstruction**.

This is the default `proof_correctness_mode: trusted_source`.

The skill's task is then to:

1. recover the theorem, assumptions, definitions, normalizations, dependencies, and proof mechanisms actually present in the supplied material;
2. choose a clean writing order;
3. design stable notation;
4. reconstruct the proof as publication prose;
5. package theorem statements and front matter from that trusted proof.

Do **not** independently re-prove the argument, search for counterexamples, run a hostile correctness audit, or stop because a step looks difficult or unfamiliar.
Do not independently search for proof gaps during ordinary writing.

## What Trusted-Proof Mode checks

Trusted-Proof Mode still checks **fidelity**, not validity:

- no supplied hypothesis is dropped;
- no conclusion is strengthened;
- parameter ranges and normalizations are preserved;
- every proof branch present in the source is represented in the reconstructed proof;
- equality, rigidity, endpoint, and constant-dependence information supplied by the source is not lost;
- notation is coherent;
- the reconstructed prose does not invent mathematical content absent from the source.

These are reconstruction checks. They are not an independent correctness verdict on the source proof.

## ProofCoreGate semantics in Trusted-Proof Mode

`ProofCoreGate: PASS` means:

> the reconstructed proof faithfully and completely realizes the trusted source argument for the stated claims.

It does **not** mean:

> the skill independently verified every mathematical step from first principles.

A source-specified external mathematical input may be treated as valid for proof reconstruction. Bibliographic metadata, priority claims, theorem numbering, and literature-history statements remain subject to citation/fact verification when they are used in the manuscript.

## Source absence is not a proof defect

Trusted proof does not authorize invention. If the supplied material literally omits required source content—for example a missing displayed formula, missing page, broken attachment, or an undefined reference whose content is unavailable—mark it `SOURCE-MISSING` rather than `MATHEMATICAL-CHECK`.

Do not fill such missing content from general knowledge unless the user explicitly asks for expansion or repair.

## When correctness verification turns on

Switch from `trusted_source` to `verify_proof` only when the user explicitly asks to:

- check correctness;
- find gaps or errors;
- referee the proof;
- stress-test assumptions;
- verify a delicate step;
- repair an incorrect or incomplete proof;
- certify mathematical validity independently of the supplied source.

In `verify_proof` mode, apply the full mathematical-integrity, gap-handling, adversarial-referee, and repair protocols.

## Priority rule

When ordinary writing instructions conflict with correctness-audit machinery, `trusted_source` wins unless the user explicitly requested verification.
