# Protocol 07a — Exact-theorem citation compression (proof-body stage)

## Purpose and authority

**Replace a proof passage with a citation only when an inspected, version-identified external theorem actually entails the whole passage being removed.** Make the resulting article shorter without weakening its theorem or concealing its own contribution. Precise attribution is part of the proof, not decorative bibliography.

This protocol turns the existing [Protocol 07, §6](07_citation_integrity.md#6-replace-repeated-proofs-by-precise-external-results) into a named *proof-core operation*, **Pass 6a**, after proof drafting and before `ProofCoreGate`. Protocol 07 remains authoritative for metadata, source/version verification and citation integrity; this document governs selection, logical coverage, replacement and downstream checking. For long proofs, perform the first candidate scan at proof-graph time, then decide/apply once actual proof text exists. Recheck affected passages after theorem renumbering and the Introduction's literature pass. Do **not** create a second research or citation-review workflow for the same source.

- **Full manuscript `RECONSTRUCT`, proof editable:** scan the substantive proof obligations once, consider verifiable prior-theorem replacements, apply those that strictly reduce repetition while preserving understanding. This is the default, not an opt-in style feature.
- **Region-level proof reconstruction or `LOCAL_POLISH`:** scan **only authorized proof paragraphs**; preserve the selected baseline and protected text. A request to polish wording alone does not authorize widespread proof deletion.
- **Introduction-only, citation-audit-only or read-only review:** do not change the proof body. For a read-only audit, list candidates, evidence and remaining doubts without calling them applied.
- **No viable source, inaccessible source, or high novel-content burden:** retain the original proof. The stage may legitimately end with zero replacements. Do not add citations to single-line elementary facts merely to satisfy a quota.

`proof_correctness_mode: trusted_source` continues to trust the supplied original proof: this is **not** an invitation to re-audit or re-prove every original step. However, a **new proposed external dependency** must be verified for identity, statement, applicability and independence before it can replace anything, even in trusted mode. If the external input remains unverified, keep the supplied argument.

## Notation crosswalk after exact-source inspection

If a verified external result uses source symbols different from the manuscript's selected canonical symbols, add a concise mapping to `NotationLedger.notation_selection.external_symbol_crosswalk` according to [Protocol 02h](02h_semantic_notation_selection.md). The mapping does not create a new proof obligation, certify an imported theorem, replace an assumption-by-assumption analysis or permit a guessed theorem locator. Retain the source version, exact locator, normalization and index conventions. If the imported result's hypotheses or conclusion are not covered, keep the unmatched argument regardless of how natural the symbol translation looks. Recheck the map after final theorem packaging.

## 1. Enumerate meaningful candidate units, not every sentence

Read the `ProofGraph` and locate distinct subclaims whose detailed proof appears to reproduce a known theorem: standard compactness, regularity, spectral, comparison, geometric, optimization, convergence or abstract-functional-analytic results; routinely repeated technical lemmas; previously proved auxiliary facts. Also identify genuine **original mechanisms**, exact quantitative improvements, sharp constants, endpoints, equality/rigidity analyses and proof-critical bridges that might not be imported.

Prioritize substantial repetitive passages, not the maximum count of cited lemmas. Start with works already cited and the targeted scholarly leads from Protocol 04u when available. Use focused outside searching to locate a **specific precise theorem** when useful; do not demand a complete literature survey for every elementary step. Do not confuse relevant *topic* or *method* with a theorem covering the exact claim.

For each serious candidate record its entire required proposition (including quantifiers, parameter dependencies, endpoint/equality conclusions and the exact downstream usage). This is the **coverage target**; its source prose length is irrelevant.

## 2. Lock the external result to a primary source and an exact locator

Before deleting a single substantive line, inspect the actual full-text primary work (published article, book, or clearly identified arXiv/author preprint) and record:

1. authors and title; DOI/stable URL or arXiv identifier;
2. **edition/publication/preprint version actually read**, e.g. `arXiv:xxxx.xxxxxv3`, including the date or version if numbers differ;
3. **the real result type and locator**: `Theorem 2.4`, `Lemma 5.1`, `Proposition 3.7`, `Corollary 6.2`; where the source is unnumbered, its actual named statement or uniquely identified statement on an exact page;
4. the full statement, not merely the abstract, an introduction's informal paraphrase, search snippet, or a citation in somebody else's paper;
5. any relevant correction, erratum, or mismatch between journal and preprint numbering.

**No inferred theorem number.** A citation to an entire paper, a section, the wrong version, a similarly titled result, or merely a proof technique is not a substitute for a precise theorem-level reference. If the original statement cannot be read, mark `RETAINED_UNVERIFIED` and keep the proof. Bibliography metadata verification, correct locator and genuine mathematical applicability are three separate checks.

When a source cites another theorem for the exact claim, prefer the original verifiable theorem or provide a precise verified chain, crediting the right contributor. Record that the imported dependency is **logically independent** of the theorem now being proved. Do not accept an external theorem whose proof depends (directly or indirectly) on the target manuscript's result as an independent justification. Be particularly cautious with contemporary preprints or two articles by the same authors.

## 3. Construct a two-sided applicability map before compression

For the external theorem `H_source ⇒ C_source` and target `H_here ⇒ C_here`, exhibit the concrete bridge

`H_here ⇒ H_source` **and** `C_source ⇒ C_here`, including any adaptation needed to turn the sourced conclusion into the exact manuscript conclusion.

Check what changes across the map (list only dimensions relevant to that claim):

| Check | Failure mode that forbids a bare citation |
| --- | --- |
| Object / operator / boundary data | A theorem for a related operator or boundary condition is invoked for a different one. |
| Domain class / geometry / dimension | Convex, smooth, star-shaped, simply connected or dimension-specific results are applied to a larger class, e.g. nonconvex simple polygons. |
| Function spaces and regularity | A smooth-input theorem is used for merely weak or nonsmooth objects without density/approximation. |
| Normalization / units / parameter range | Unit-area, sign, normalization, spectral index or allowable parameters differ with no derivation. |
| Quantifiers / uniformity / rates | A bound for each fixed `N` or `ε` is used uniformly in `N` or `ε`; a qualitative convergence is used for an explicit rate. |
| Constants / strictness / endpoints | Nonsharp constants, non-strict inequalities or missing endpoints are silently strengthened. |
| Equality / rigidity / uniqueness | A weak inequality is cited as if it also classified equality or excluded all other minimizers. |
| Independence | The alleged predecessor theorem itself assumes, quotes, or uses the manuscript's target conclusion. |

Verify assumptions *locally*: identify the line, established lemma, source hypothesis or proof within the manuscript which supplies each nonautomatic condition. If a check requires a nontrivial argument, **retain that argument** even if the remaining cited portion is long. If a claim uses a parameter-uniform theorem, inspect the actual dependence of constants. Never infer the needed dependency from the term “standard estimate.”

The chain of implications must be **mathematically explicit**; a metadata-verified theorem with unverified hypothesis transfer is insufficient. In `trusted_source` mode this is a *targeted new-dependency check*, not an independent re-examination of every original deduction.

## 4. Decide the smallest faithful replacement

- `APPLIED_DIRECT`: the exact external result implies the entire local obligation, and any source hypotheses are either already established or quickly and explicitly verified. Replace the redundant proof by an exact result citation and its application.
- `APPLIED_ADAPTED`: the external theorem implies the principal step **after** a necessary short calculation (scaling, approximation, conjugation, normalization, limiting or constraint verification). Cite it and keep the calculation.
- `APPLIED_PARTIAL`: only part of the original passage is external. Cite **that part only** and retain all unmatched estimates, rates, equality cases, uniformity or genuine innovations. Preserve the lemma label when downstream references use it.
- `RETAINED_UNVERIFIED` / `RETAINED_INAPPLICABLE`: source text, number or hypothesis map cannot be confirmed. Keep the original proof; record a candidate as unresolved, not as an applied reference.
- `RETAINED_ORIGINAL`: the proof carries a novel mechanism or a clarifying indispensable short argument. Keep it, even if a related result could also be cited.

Do not split a short accessible proof merely to grow the bibliography. **Minimize the proof burden**, not the number of lines at any cost: readers should see why a cited theorem applies and where the present paper does something new. A theorem-level citation can close a technical obligation, but it cannot replace the conceptual interface that explains the manuscript's argument.

## 5. Write the proof as a verifiable application (not a slogan)

Use the existing TeX citation convention with an **actual verified locator**, e.g. `\cite[Theorem~2.4]{VerifiedKey}` *only if* that exact number has been read in that version. This is syntax illustration, **not** an assertion that such a theorem exists. If the source has an unnumbered result, use its verified name and exact page in the optional note.

A useful prose pattern (replace placeholders with checked facts) is:

> The hypotheses of \[Author, precisely identified result\] hold here because [specific fact or earlier local lemma]. Applying the result to [translated object/parameters] gives [exact target conclusion].

For adaptation include the necessary equation(s) and give the cited conclusion and the new derived conclusion separately. For partial replacement, retain the local proof of the remaining claim after the citation. Never write only “by standard theory,” “by a classical theorem,” or a whole-paper `\cite{...}` in lieu of a substantive missing argument.

Credit the discoverer of the imported result even if the paper originally supplied a self-contained derivation. In the Introduction, adjust method/novelty language if an imported theorem changes what can legitimately be described as the paper's contribution. A verified application is not a proof of the external theorem and does not need to reproduce its proof.

## 6. Record an audit-sized dossier only for serious candidates

Use the compact [ProofCitationReplacementDossier](../schemas/proof_citation_replacement_dossier.yaml) (or an equivalent table) when there are **material replacement candidates**. Track one row per substantive unit, not one row per proof line. Fields must support:

- manuscript claim and stable location; original length/role and downstream label or equation usage;
- primary-source identifier, exact version, actual theorem/lemma/proposition/corollary or precisely located unnumbered statement;
- separate `metadata_checked`, `locator_checked`, `primary_statement_checked` flags;
- source-hypothesis ↔ manuscript-fact mapping and source-conclusion ↔ desired-conclusion mapping;
- retained adaptation/quantitative/equality/rigidity steps;
- candidate status, **applied vs merely proposed**, changed TeX location and remaining uncertainty;
- dependency independence and protected-scope check.

Use the read-only sanity checker for dossier fields when helpful:

```bash
python tools/proof_citation_dossier_audit.py --input proof_citation_replacements.yaml --strict
```

The checker can detect missing locators, versions, mapping records or invalid applied statuses; **it cannot open source papers, independently prove the implication, or certify a theorem's correct application**. Human/source-level verification is still required. Do not create empty dossiers or claim they are mathematically certified merely because the command passed.

## 7. Reconnect the proof graph and the paper

After each applied replacement, verify that:

1. every lost displayed formula, lemma label, reference anchor and subsequent dependency remains valid or is explicitly repaired;
2. the published replacement really proves **all** the local claim still stated, including needed strictness, equality, rates, limits and constants;
3. the local bibliography key resolves, the exact locator matches the cited version, and TeX builds when available;
4. the Introduction's prior-work map, method credit, proof outline, Abstract and novelty wording agree with the *new* division between imported and novel arguments;
5. the selected editing scope and protected regions were respected.

At `ProofCoreGate`, reject a purportedly completed replacement with unverified primary-source text, missing assumption transfer, an uncovered conclusion, circular citation or unresolved downstream use. Revert to the retained original proof rather than masking the failure. This does **not** turn the trusted-source fidelity gate into a global independent correctness review.

Output to the user only a compact change report unless they ask for a theorem-by-theorem audit: what was replaced, the exact result (with version), what remained original and any candidates not applied. Never report proposed/inaccessible citations as finished edits.
