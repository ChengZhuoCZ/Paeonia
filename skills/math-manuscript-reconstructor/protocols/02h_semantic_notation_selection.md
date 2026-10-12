# Protocol 02h — Semantic Notation Selection

## Purpose: choose symbols, not just inspect symbols

This is an **active notation-design pass**. Decide *which* mathematically natural symbol should denote each important object before finalizing `NotationLedger.canonical_objects`. Existing Protocols 02d–02g settle architecture, typography, collisions and an optional empirical author-corpus prior; none alone makes the object-by-object decision. Protocol 02h fills that gap, without inventing a universal alphabet or numerical aesthetics score.

**Default activation:** in a nontrivial proof-producing `RECONSTRUCT` run, at Pass 5a after `MathLedger`/`ProofGraph` and before publication proof prose. For a requested rewrite of theorem statements or notation alone, apply only within the authorized region; in `LOCAL_POLISH`, retain clear established symbols unless a concrete ambiguity or inconsistency needs repair. For read-only review, propose a notation map but do not apply replacements. Protected passages, user-provided fixed symbols and frozen mathematics remain binding. Do not ask for an additional mode question when the writing mode and editing scope are already known.

## 1. Extract mathematical roles first

Form a compact object map from the **actual proof**, not an arbitrary letter inventory. Mark each recurring object by:

- mathematical kind: domain/configuration, unknown, operator, eigenvalue, energy/functional, admissible class, parameter, sharp constant, mode/scale, limit, perturbation, reference configuration, and equality/rigidity datum;
- level: main-theorem-visible, globally recurrent proof object, section-local object, or disposable bound/dummy variable;
- relationships: finite versus limit, reference versus perturbation, original versus normalized, physical versus Fourier variables, global versus localized, dual/primal, odd/even, vector/scalar, and ordinary versus sharp constants;
- dependencies and conventions: dimensions, parameter regimes, measure/transform normalizations, operator sign, equivalence group, and prior results the proof invokes.

Only main-theorem and recurring proof symbols normally need recorded **selection decisions**. A bound integration variable or one-use dummy does not need a ledger row or candidate tournament. Review the whole recurring-object vocabulary to prevent global duplicate meanings (Protocol 02f).

## 2. Determine convention evidence and priority

Use the following **lexicographic, evidence-sensitive priority**; do not sum arbitrary numerical weights:

1. **Semantics and hard constraints:** an unchanged theorem, user-mandated notation, exact normalizations/signs, established named constants, and collision-free recurring-object assignments. A purported notation improvement must not silently change the mathematics or invent an equivalence.
2. **Strong readership/domain convention:** the normal symbols in the pertinent mathematical subfield and the paper's focal problem, verified from trusted primary sources when a genuine ambiguity matters. A reference's variable names do not bind this paper; an established conceptual convention is stronger than personal taste.
3. **Reveal the proof's structure:** related families share a base; different species are distinguished; limits, rescalings, duals, perturbations and equality cases carry meaningful indices or modifiers; theorem statements remain readable.
4. **Continuity and translation cost:** prefer coherent, collision-free notation already present in the original proof or checked external theorem when changing it would force repeated dictionary translations or destabilize a known result.
5. **Economy in active formulas:** among equally sound candidates choose shorter, easily pronounced and recognizable symbols, with few stacked adornments, stable index conventions, easy LaTeX, and reduced rereading. Optimize a representative proof identity, not only the symbol list.
6. **Soft style prior:** Protocol 02g and the user's plain-typography house style break genuine ties only. Never reproduce a source author's exact complete symbol table.

If a favored domain convention conflicts with an explicit user-fixed symbol or a global collision, identify a second conventional alternative or a semantic qualifier and document the exception. **No arbitrary hard-coded meaning is assigned to a particular letter.** One-to-one canonical visible-symbol meaning (Protocol 02f) is blocking; readability choices are made by mathematical editorial judgment, not by an unvalidated numeric score.

## 3. Field-conditioned candidate generation

Use compact field vocabulary as **illustrations, not assignments**:

| When the mathematical role fits | Natural *candidate* forms | Watch for |
| --- | --- | --- |
| PDE domain/solution/operator | `\Omega`, `u`, `-\Delta`, `L`, `P_\alpha` | boundary condition, sign, conformal/other specialized operator convention |
| Dirichlet/Neumann eigenvalues | `\lambda_1(\Omega)`, `\mu_1(\Omega)` | field-specific index origin (0 or 1), treatment of Neumann zero mode |
| polygon and distinguished regular model | `P`, `R_N` | `P` also being a projection/operator; `R_N` radius elsewhere |
| functional, deficit, sharp constant | `F(\Omega)`, `D(\Omega)`, `c_*` | `D` derivative/operator, `C` generic constant, sharp vs mutable coefficients |
| sequence/modes/scale | `n`, `k`, `\varepsilon`, `N` | mode index vs edge count vs approximation index, cutoff scale and parameters |
| Fourier variables / curvature measure | `\widehat f(k)`, `\mu`, `\widehat\mu(k)` | Fourier normalization, transform convention, probability vs signed measure |
| Hilbert/Banach/interpolation structure | `H`, `X`, `Y`, `[H,Y]_\theta` | whether Hilbert is a distinguished endpoint, interpolation normalization |

A printed example never overrules the author's actual theorem. The symbols `P`, `D`, `\Delta`, `\mu` etc. are *not globally reserved*. A convention may differ within spectral, probabilistic, geometric and PDE subcommunities; choose the convention supported by the specific problem.

## 4. Compare candidates on real mathematical expressions

For a main object with a genuine choice, consider usually two plausible candidates (sometimes only one if domain-standard or user-mandated). Compare by **human-readable reasons** rather than fake scores:

- Will a specialist identify its type on first sight?
- Does it visually represent the relationship in the theorem or a decisive estimate?
- Will it be confused with an operator, measure, index, epsilon, or standard constant nearby?
- Does it introduce distracting primes/hats/tildes/superscript towers or multiple font alphabets?
- Is a long formula materially improved, not merely made prettier in one isolated line?
- Does its definition sit naturally before first use and survive a change of proof organization?

Choose the semantically clearest, collision-free candidate and give a **one-sentence reason** for each genuinely contested, high-salience choice. Do not produce a long exhaustive option ledger for routine notation. Do not optimize via numerical character counts, arbitrary symbol preferences, or letter-frequency imitation.

## 5. Semantic families, definitions and indexing

A symbol family should express a **proved relationship**, not a visual analogy. Examples of potentially legitimate patterns:

- `E_N` and `E_\infty` for a finite and limiting energy *when the proof actually relates them*;
- `u_\varepsilon`, `u_0` for a perturbative branch and its base point;
- `F(P)-F(R_N)` for an actual comparison and equality reference;
- `C(d,p)` for constants whose dependencies are required for a uniform theorem;
- a semantic `\perp` only for an actual projection, orthogonal component or quotient.

Distinguish exact and approximate, finite and limiting, global and local, constrained and unconstrained. Preserve index placement (`u_i`, `u^j`, `\lambda_k`) consistently; avoid reusing `N` as both polygon side count and mode number. Keep sharp named constants from being relabelled as generic changing `C`. Declare normalization once at its mathematical first use (not just in a private ledger). Standard `\mathbb R` and `\mathbb C` remain standard even if a house style prefers plain letters elsewhere; semantic `\mathcal` remains allowed by Protocol 02e.

## 6. Exact-theorem import: a verified crosswalk, not new mathematics

When Pass 6a / Protocol 07a replaces proof by an exact citation, map the cited theorem's source variables to the manuscript's canonical variables **explicitly**. Record the primary source version and *verified* theorem locator already collected by Protocol 07a, and keep a short `external_symbol_crosswalk` in `NotationLedger` when the translation is nontrivial. Check the direction of assumptions, function spaces, normalization, parameter/endpoint ranges and quantifiers: symbol renaming is not proof of a missing hypothesis or conclusion. Do not alter the cited theorem's statement or invent a locator to make a proposed symbol map look valid. If the imported notation is clearer, consider it before finalizing; a direct reference with awkward names can instead be followed by a one-line dictionary.

## 7. Output and state transition

**Inside the existing `NotationLedger`, not a second mandatory dossier**, record `notation_selection` with `stage`, `field_context`, optional `protected_symbols`, `decisions`, optional `external_symbol_crosswalk`, and `review`. Each **contested/main** decision has an `object_id`, `chosen_symbol`, brief `rationale`, `priority_basis`, and optional `alternatives_considered`. Each chosen object must exist in `canonical_objects` with the same symbol; entries referring to different canonical objects must not collide. There is no fixed number of candidate symbols and no requirement to invent alternatives for a strong convention.

Run `python tools/notation_choice_audit.py <notation-ledger.yaml> --strict` when locking Pass 5a for a new full proof reconstruction; use the non-strict legacy/read-only route only while drafting or reading older ledgers. This is a *structural declaration* audit, not mathematical evaluation. Then run `notation_architecture_audit.py`, `duplicate_symbol_audit.py` and the optional `gui_notation_prior_audit.py`. The new checker only checks declarations and crosswalk consistency; it cannot tell which notation is aesthetically or mathematically best, read referenced theorem PDFs, or certify logical implications.

**At proof-draft time:** write formulas using the selected symbols, define each at first use, and revisit only if the proof exposes a concrete conflict. **After Pass 6a:** update/verify crosswalks for new imported results. **After theorem framing and Introduction:** cold-read the main statement without proof-only baggage. **At final LaTeX audit:** check every recurring symbol, transform convention, definition and macro. Any consequential conflict rolls back to `NOTATION_ARCHITECTURE`; a local typographic repair does not authorize global renaming.

**Local-polish rule:** an authorial notation baseline is not freely replaceable; fix only the identified issue in scope, give a minimal cross-reference at its border if needed, and report unresolved out-of-scope inconsistencies without editing them.

## Explicit failure patterns

- `\lambda` denotes a spectral value in one theorem and a deformation parameter later; relabel one recurring object.
- A domain-specific symbol is replaced by an unusual letter solely because a style corpus favors it; retain the field convention.
- `\mu_1` for the first nonzero Neumann eigenvalue is silently used when the imported source numbers eigenvalues from zero; state/verify the index mapping.
- A normalization `|\Omega|=\pi` disappears after choosing `R_N` over `P_N`; keep the normalization in the theorem/definition.
- A term `u_\varepsilon` is renamed `u_0` although it is still a perturbation; represent the true mathematical state.
- A purported direct citation is treated as valid merely because `E` in the source was renamed `F` in the manuscript; validate hypotheses and conclusions under Protocol 07a.
- Proof-only auxiliaries appear throughout the first-page theorem because the symbol inventory was optimized rather than the reader's route.
