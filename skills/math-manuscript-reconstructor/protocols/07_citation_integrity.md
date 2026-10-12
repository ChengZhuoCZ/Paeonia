# Protocol 07 — Reference verification and citation integrity

## Scope and routing

**Discovery is not verification.** For an authorized Introduction reconstruction, [Protocol 04u](04u_literature_discovery_and_credit.md) first searches for *additional* relevant articles, their contribution roles, and exact prior-frontier competitors. This Protocol 07 then verifies their identities, versions, locators, and the specific claims they support. Running `citation_inventory.py`, or checking every source already in a `.bib`, **does not show that essential outside sources were discovered or credited**. [Protocol 04v](04v_evidence_grounded_grand_narrative.md) uses only the verified research to construct the broader story. For `LOCAL_POLISH`, confine discovery/verification and edits to the approved literature/novelty claims.

Run this workflow when reference verification is requested, and for references added or changed during writing. An explicit all-reference audit covers every bibliography entry, including uncited entries. A notation-only edit need not trigger a fresh literature audit. Reuse evidence when the source version and cited claim are unchanged; recheck affected claims after substantive edits. Preserve the selected writing mode and protected regions. A request to check references is read-only unless correction is also authorized.

Maintain one `CitationLedger`, or a simple table, with a row per entry and separate location notes when the same work serves different claims. Separate **metadata**, **locator**, and **claim-support** results. An existing source may have wrong metadata, a misplaced locator, or an unsupported use; do not collapse these into one `verified` label.

## 1. Inventory the actual manuscript

For TeX and BibTeX sources, run the read-only helper with actual file paths:

```bash
python tools/citation_inventory.py --tex paper.tex --output citation_inventory.json
python tools/citation_inventory.py --tex main.tex --tex sections/intro.tex --bib references.bib --output citation_inventory.json --strict
```

The tool reads only explicitly supplied files, never executes TeX or fetches URLs, and reports declared but unscanned inputs or bibliographies. Add those files explicitly and rerun when they belong to the manuscript. Relative declarations are resolved beside their source file; check root-document-relative paths and TeX search paths manually. Do not scan a `.bib` and its generated `.bbl` as independent definitions of the same bibliography. Custom macros, conditional TeX, bibliography inheritance and Biber-generated entries require manual inspection; coverage notes are part of the result.

The inventory records definitions, citation locations and optional notes, undefined keys, duplicate definitions, uncited entries, and `nocite` inclusion. Nested citations inside citation notes are counted. Comments and common verbatim environments are excluded. `--strict` fails on mechanical errors or unresolved coverage, not on uncited entries alone.

For PDF-only work, extract entries and locations, then inspect rendered pages for ambiguous OCR. Do not guess author names, symbols or page digits.

**Inventory success is not source verification.** Review fields start as `not_checked`; the tool does not certify source existence, metadata or claim support. An undefined key is not a fabricated paper; an uncited entry is not automatically irrelevant; `nocite{*}` is not an in-text discussion.

## 2. Verify each source and its bibliographic record

Use the journal/publisher, DOI landing page and registry, official preprint archive, or an author/institutional copy. A snippet or another paper's bibliography may locate a source but cannot certify a disputed detail. Open the record and, where needed, the work itself. If access is unavailable, report what was confirmed and what remains unresolved.

Check authors, title, journal/series, year, volume/issue, pages or article number, edition, DOI and arXiv identifier/version as applicable. Follow identifiers and match their destination to the cited work; a syntactically valid DOI is insufficient. Preserve accented names and meaningful mathematical notation.

Distinguish journal year from online-first/digitization date, original edition from reprint, and valid parallel pagination. A preprint and a published version may have different titles and lemma numbers. Record the version actually used rather than silently combining their metadata and locators.

Check the official record for a correction, withdrawal, retraction or replacement when relevant. A publisher's correction is not automatically a retraction. Identify whether the notice affects printing/metadata or the cited assertion; do not infer an effect absent from the notice.

## 3. Verify locators and the use of the source

Classify each use:

- **DEPENDENCY:** an external result used in a proof.
- **BACKGROUND:** orientation or a literature pointer.
- **COMPARISON:** a relationship with another result or method.
- **PRIORITY:** historical or novelty attribution.

For a dependency, open the relevant theorem, lemma, section or pages. Check the object, hypotheses, normalization, range, estimate direction and conclusion actually needed. Identify what the manuscript derives in addition. A correct book citation does not automatically justify every local estimate. Flag an unresolved applicability step separately from a bibliographic error; reference checking is not a full proof audit.

Verify every explicit locator against the cited version. Where numbering differs, use a verified stable section/page locator or identify the version; never guess a replacement lemma number. For background, verify the topic without requiring it to prove the current theorem. For comparison, distinguish exact specialization, analogy and prospective extension. Priority claims require evidence beyond a related title or failed search.

Review the adjacent sentence. Similar words may refer to different objects: an eigenvalue gap and a coercive defect bound, for example, are not interchangeable. A citation group still requires an appropriate role for each member. Results for a restricted class or another functional cannot be presented as resolving the full problem.

## 4. Repair proportionately, within scope

A peripheral background source may need only a short literature pointer. Explain an operative connection when its correspondence helps the reader understand the proof. Honor grouping and brevity preferences without implying an unsupported dependency.

Do not automatically insert uncited entries into the Introduction, delete them, or use `nocite` to hide missing discussion. Inclusion/removal must have a supported purpose within the editing scope. If the user wants every entry cited but an existing sentence cannot support the placement, explain the mismatch and propose the smallest adequate wording, grouping or note.

When correction is authorized, amend verified metadata and locators first. For protected prose, prefer permitted citation-only repairs; adding explanation requires scope that permits it. Preserve unrelated wording. Recheck affected keys and uses, compile modified TeX when available, and inspect relevant layout. Compilation does not resolve source applicability.

## 5. Report evidence and uncertainty

For each entry record: key/number; original and corrected entry if applicable; source URL and version; evidence location; manuscript locations and roles; separate metadata/locator/claim-support statuses; proposed/applied correction. Use statuses such as `verified`, `mismatch`, `not_applicable` and `not_verified`, with reasons. Identify uncited entries and inaccessible or unreadable sources distinctly.

For a complete audit, report the bibliography size, entries examined, and unresolved findings. Say “not verified” rather than “invented” when verification fails. If metadata match but applicability remains open, report both. Never claim all references checked after only inventorying keys or checking a sample.

For routine writing, keep the ledger internal unless requested or a material unresolved finding needs attention. Keep audit markers outside publication prose.

## 6. Replace repeated proofs by precise external results

**Default during authorized proof reconstruction; scoped during local proof polishing.** The systematic candidate review, precise-source mapping, status decisions, actual proof rewriting and post-replacement integrity checks now belong to [Protocol 07a — exact-theorem citation compression](07a_exact_theorem_citation_compression.md), executed as **Pass 6a** before `ProofCoreGate`.

A citation can replace a passage only if the full text of a primary-source **exact theorem, lemma, proposition, corollary or precisely located unnumbered result** has been inspected, its actual version and locator are verified, the local hypotheses imply the sourced assumptions, and its conclusion implies *all* parts of the removed passage. Never guess a theorem number, import a claim from an abstract, or silently strengthen constants, uniformity, strictness or equality. Keep necessary adaptations and unmatched steps, including the manuscript's own explanatory bridge. A potential reference that cannot be verified remains a candidate **not an applied replacement**.

The ordinary `CitationLedger` handles metadata, version, locator and claim-support distinctions. For material proof replacement candidates, use the compact `ProofCitationReplacementDossier` or an equivalent table as directed in Protocol 07a. The optional dossier checker detects missing fields only; it cannot validate mathematical entailment. `LOCAL_POLISH`, Introduction-only and read-only scopes retain their original authorization limits. Reconcile any applied changes with the proof graph, labels, Intro/Abstract credit and bibliography before declaring completion.
