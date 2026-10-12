# Protocol 02d — Notation Architecture

## Purpose

Design a stable symbolic language **before proof-core prose is drafted**. Notation is part of mathematical architecture: it should reduce cognitive load, reveal invariant structure, and remain stable across the proof, theorem statements, Introduction, and appendices.

## Timing

Build `NotationLedger` after `MathLedger` and `ProofGraph` are sufficiently stable, and before `ProofCore` drafting. Final editorial normalization later may repair typography or local collisions, but it should not redesign the symbol system unless upstream artifacts are invalidated.

## Active symbol selection (Protocol 02h)

Before filling canonical visible symbols, apply `protocols/02h_semantic_notation_selection.md`: use mathematical role, field conventions, a representative main theorem or active formula, and meaningful object families to choose among genuinely plausible symbols. Record short reasons for major contested choices **inside the existing** `NotationLedger.notation_selection`; do not add a second required artifact. A good audit of collisions cannot substitute for choosing a reader-natural symbol in the first place.

## Symbol discipline

Apply `protocols/02f_duplicate_symbol_audit.md` and `protocols/02e_symbol_reservation_and_plain_typography.md` as hard constraints. When several collision-free choices remain, apply the soft corpus prior in `protocols/02g_changfeng_gui_notation_prior.md` before assigning recurring symbols. Record every recurring object in `NotationLedger.canonical_objects`, then require exact visible-symbol uniqueness across those recurring objects. Local dummy variables are excluded. Keep decorative alphabets out of the default symbol system.

## Canonical-object rule

Every recurring mathematical object should have one canonical symbol in a given scope. Record:
- semantic object ID;
- canonical symbol;
- object type;
- scope;
- normalization;
- first mathematical use;
- permitted aliases, if any;
- related local/global or normalized/unnormalized versions.

Do not preserve source notation merely from familiarity. For still-undecided notation, prefer the plain semantic patterns recorded in `profiles/changfeng_gui_notation_prior.md`.

## Local/global discipline

Make global and local objects visibly distinguishable when both occur. Use a coherent convention for:
- global vs localized energies/forms;
- original vs rescaled variables;
- limiting vs finite-parameter objects;
- ambient vs restricted operators;
- exact vs approximate solutions;
- base configuration vs perturbation.

The convention should be simple enough to survive long proofs without ad hoc primes, tildes, hats, and superscripts accumulating unpredictably.

## Index architecture

Assign indices by mathematical role, not by arrival order. Distinguish, when needed:
- geometric indices;
- Fourier/spectral mode indices;
- sequence/subsequence indices;
- derivative orders;
- iteration/stage indices;
- parameter-family indices.

Avoid using the same index family for unrelated roles in overlapping passages.

## Constant architecture

Use constant families consistently. Record dependencies when they matter.

Good patterns:
- universal `c,C` when values may change and dependence is irrelevant;
- `C(d,p)` or an explicit sentence when dependence matters;
- stable named constants such as `c_*`, `C_0`, `\gamma_N` when reused structurally.

Bad patterns:
- `C_1,C_2,\dots,C_{17}` created only by chronology;
- reusing `C` first as a fixed sharp constant and later as a disposable generic constant;
- suppressing parameter dependence needed for uniformity.

## Operator and functional conventions

Fix early:
- operator typography and domains;
- inner-product conventions;
- Fourier transform normalization;
- measure normalization;
- energy/quadratic-form notation;
- derivative and variation notation;
- norm conventions;
- group/action notation when rigidity is modulo symmetries.

These are mathematical semantics, not cosmetic LaTeX choices.

## Introduction policy

Introduce notation at first mathematical need. Do not preload the paper with a symbol glossary unless the density genuinely requires one. A theorem may use notation defined immediately before it; proof-only notation should not contaminate the main statement.

## Alias policy

Aliases are allowed only when they serve a real transition, for example passing from a geometric quantity to a normalized variable. Record the bridge explicitly and retire the old alias when possible.

## Collision policy

A collision exists when one visible symbol denotes different mathematical objects in overlapping reader scope. Resolve collisions before drafting. Local dummy variables may reuse conventional letters only when no ambiguity can propagate.

## Notation-churn rule

Do not rename objects merely to imitate a reference corpus or make a later section look stylistically different. Conversely, if the proof graph reveals that source notation causes repeated translation, redesign it before prose is written.

## Final audit

After theorem packaging and editorial compression, verify:
- every major symbol has one stable meaning in scope;
- theorem notation agrees with proof notation;
- normalizations are consistent;
- local/global pairs remain distinguishable;
- constants carry the dependencies claimed;
- aliases do not survive after their bridge purpose ends;
- recurring symbols retain one active mathematical meaning in each reader-visible scope, with global assignments protected from local shadowing;
- decorative alphabets comply with the plain-typography policy;
- no font-only semantic distinctions remain;
- no internal semantic IDs appear in submission prose.
