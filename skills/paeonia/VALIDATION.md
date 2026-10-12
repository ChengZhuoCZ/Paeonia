# v1.42.1 — Paeonia rename validation

- **Identity:** skill frontmatter and manifest use `paeonia`; the directory and archive root are `paeonia/`; UI display name and documentation title are **Paeonia**. All version metadata is `1.42.1`.
- **Checks run:** skill-creator quick validator passed; the v1.42 contract passed all 23 checks; contract consistency passed with 48 artifacts, 22 gates and 214 behavioral fixtures.
- **Scope preservation:** all manuscript-writing protocols, helper tools, schemas and behavioral fixtures are byte-identical to the preceding v1.42.0 source. The existing v1.42 contract now permits consistent patch releases.
- **Packaging:** both internal SHA-256 manifests were regenerated; all 740 entries were checked. The ZIP integrity check passed and all 742 archived files were compared byte-for-byte with the source directory. The distribution checksum is supplied separately.
- **Limits:** the full historical release suite was not rerun for this rename. These checks establish naming, metadata and package consistency; they do not independently assess manuscript quality, mathematical correctness or cited-theorem applicability.

# v1.42 validation scope

The new single-voice specification is checked structurally for path integration, automatic conflict resolution, no unsolicited author/style-choice prompt, local-polish preservation, and consistency across the former style-realization protocols. Behavioral fixtures check explicit editorial decisions rather than actual full-model writing. Read-only corpus and citation machinery remains subject to its prior tests. A formal automated test cannot certify the quality of a real mathematical manuscript; final judgment is a coherent text-level cold read.


# Validation — v1.41.0

- **Scope:** active field-native mathematical symbol selection (Protocol 02h) built into existing Pass 5a and NotationLedger; protected-region and original theorem meaning unchanged.
- **Checks:** new v1.41 contract (23 checks), new structural decision checks (20 ordinary + four strict-path), and 200 executable good/bad behavioral cases passed; 48 artifact and 22 gate contracts passed. Legacy tests were rerun individually or in bounded groups.
- **Monolithic suite:** the single `run_release_suite.py` invocation timed out while executing legacy programs, so it is **not** reported as a one-command PASS.
- **Limits:** neither editor-quality nor cited-theorem applicability can be certified by a symbol checker. No particular article or outside mathematical theorem was rewritten/verified. See `validation/notation_selection_v141.md`.

# Validation — v1.40.0

- **Scope:** formal default proof Pass 6a for precise theorem-level citation replacement, with source-version and assumption/conclusion checks, scope-preserving fallback, conditional dossier and structural checker.
- **Constituent tests:** legacy compatibility and new v1.40 contract pass; 186 executable good/bad regression fixtures pass; schema/checker unit tests pass; contract compiler reports 48 registered artifacts, 22 gates and 186 behavior cases.
- **Monolithic runner:** attempted but interrupted by execution-time timeout. Constituent test runs (not a completed monolithic run) are the release evidence.
- **Limits:** no future theorem-number lookup or logical implication is certified by the static checker, and no actual manuscript was edited in this development task. See `validation/exact_theorem_citation_v140.md`.

# Validation — v1.39.0

- **Scope:** instruction, schema, fixture and routing upgrade for literature-first Introduction reconstruction, fair credit, and evidence-supported grand mathematical narratives.
- **Structural tests:** the v1.39 contract passed (15 checks); all 172 good/bad behavior fixtures passed and 172 legacy regression cases were covered. `test_contract_consistency.py` passed: 47 artifacts, 22 gates, 172 fixtures. Earlier v1.36–v1.38 contracts passed after the version-floor compatibility update. Other existing compatibility/test-tool/notation/writing-mode/citation tests were executed in bounded groups and passed. The monolithic `run_release_suite.py` attempt was interrupted by the execution-time limit after earlier batches had passed; no claim is made that the monolithic run completed as a single process.
- **External sources checked for workflow design:** SIAM author ethics and SIADS Introduction instructions, Oxford research-writing guidance, AMS MathSciNet description, Crossref metadata API, OpenAlex citation-graph documentation, and arXiv version citation guidance. These establish procedural reference practice, **not** the completeness of a future mathematical paper's actual bibliography.
- **Behavioral limit:** the fixtures encode accepted and rejected decisions. They are not a live end-to-end literature search for an identified theorem, independent historian's priority audit, automated mathematical-theorem comparison, or blind study of Introduction quality.
- **Preservation:** v1.38's optional author-style evidence is still separate from research literature. `LOCAL_POLISH` remains bounded and preserves effective source prose. Full-manuscript proof-body-first drafting remains intact.
- **Release artifact checks:** UTF-8 Markdown links, YAML/JSON parsing, Python compilation, archive payload hashes, and roundtrip integrity are recorded by the packaging verification performed for this release.

# Validation — v1.38.0

The author-corpus supplement passed all 33 constituent release programs when executed in bounded groups, including legacy compatibility, 162 executable behavioral fixtures, writing-mode routing, gate-repair consistency, proof-explanation tests, citation-inventory tests, and the v1.36–v1.38 contracts. Contract compilation reports 29 canonical states, 46 artifacts, 22 gates, 162 behavioral fixtures, and no errors or warnings. YAML/JSON parsing, Python compilation, relative Markdown-link checks, and archive payload verification were also run for the release candidate. Details and limitations are recorded in `validation/author_corpus_supplement_v138.md`.

The release validates the interaction, identity, acquisition, attribution, selection, quarantine, and application contracts. No author was supplied for this skill-development task, so no live author corpus was downloaded and no claim is made that the rules infer an individual's unique writing style. The suite also does not certify mathematical correctness or guarantee literary quality.

# Validation — v1.37.0

The conditional PDE Introduction architecture passed the complete 32-program release suite in bounded batches, including all compatibility contracts, 154 executable behavioral fixtures, writing-mode routing, gate-repair consistency, proof-explanation tests, citation-inventory tests, and the new v1.37 contract. Contract compilation reports 29 canonical states, 45 artifacts, 22 gates, 154 behavioral fixtures, and no errors or warnings. YAML/JSON parsing, Python compilation, relative Markdown-link checks, and archive payload verification also passed. Details and limitations are recorded in `validation/pde_introduction_v137.md`.

The corpus review is qualitative and theorem-aware. It demonstrates that the new rules match several important PDE Introduction architectures; it does not prove that every generated Introduction will have top-journal literary quality, and it does not certify mathematical correctness of a manuscript. No manuscript was rewritten in this release.

# Validation — v1.36.0

The reader-first Introduction redesign passed the 31-program release suite, including all legacy compatibility checks and five new behavioral cases. Contract compilation reports 29 states, 45 artifacts, 22 gates, 143 executable behavioral fixtures, and no errors or warnings. YAML/JSON parsing, Python compilation, and relative-link checks also passed. Details and limits are recorded in `validation/introduction_reader_first_v136.md`.

These checks validate package contracts and selected semantic decisions; they do not certify the literary quality of every generated Introduction. No manuscript rewrite, blind reader study, or mathematical-proof certification is claimed for this release.

# Validation — v1.35.0

Instruction-only proof-replacement update. Package validation and the limits of review are recorded in validation/proof_replacement_v135.md. No new proof replacement, external theorem verification or manuscript compilation is claimed. Earlier tool and article checks remain historical.

# Validation — v1.34.0

Reference-checking workflow and executable inventory update. Current checks and their limits are recorded in validation/citation_inventory_v134.md. The current manuscript is used only as a local inventory sample; its external references are not newly verified by that run. Prior audit evidence and manuscript compilation remain historical.

# Validation — v1.33.1

Instruction consolidation and retention routing after a same-agent application that retained the v132 manuscript byte for byte. No manuscript recompile, new PDF layout validation or independent reader study is claimed. Current package checks are in validation/abstract_calibration_v133.md; earlier full-suite and document checks remain historical.

# Validation — v1.33.0

Pre-application instruction consolidation. The actual retained or edited candidate will be recorded after application. Historical runs below remain historical.

# Validation — v1.32.1

Instruction-only refinement after a continuing same-agent application on the same abstract. Current focused package and manuscript checks are recorded in validation/abstract_calibration_v132.md. Earlier full-suite runs are historical; no new independent reader test or full-proof audit is claimed.

# Validation — v1.32.0

Initial instruction refinement, saved before the next manuscript candidate. Earlier applications and test runs below are historical.

# Validation — v1.31.1

Instruction-only refinement after the recorded v1.31.0 application. Same-agent, context-aware comparison of a reference, trial and selected abstract with 112, 141 and 124 whitespace-separated words respectively (these are descriptive counts, not quality scores). Four of six reference sentences are retained verbatim. Two Introduction fragments clarify source-backed proof operations. All other manuscript content is preserved. Package and artifact checks are recorded in validation/abstract_calibration_v131.md; they do not certify proof correctness, blind generation or independent comprehension. Historical test results below remain historical.

# Validation — v1.31.0

Pre-application instruction revision. The manuscript application and comparison will be recorded separately; no independent reader test or proof certification is claimed.

# Validation — v1.30.1

Instruction-only selection-policy patch. Frontmatter and contract consistency checked; archive payload hashes verified. The v1.30.0 full-suite run below remains historical. No new independent behavioral evaluation or manuscript rewriting is claimed for this skill patch.

# Validation — v1.30.0

- Release suite: PASS, 29 programs, including 14 new executable writing-mode tests. See `validation/release_suite_v130.log`.
- Skill Creator quick validation: PASS.
- New tests check local editing without proof-gate/checksum prerequisites, full-paper local polishing, selected-region reconstruction, legacy compatibility, conflicting mode/scope rejection, read-only workflows, and refusal of advice that would expand bounded work.
- Two historical heading-based tests were updated because their unconditional ban on preservation/from-source polishing conflicts with the newly requested mode. They now check the actual distinction in planner output; semantic and reconstruction checks remain active.
- Modes and boundaries are planner metadata, not file locks. Natural-language routing and preservation of real authorial prose still require editorial judgment and an actual document diff. These tests do not establish prose quality, independent reader comprehension, or mathematical correctness.
- Only the skill package is changed. No article is revised and no installed skill is overwritten.

# Validation — v1.29.0

The actual application of released v1.28 produced a byte-identical manuscript candidate. Its reader-inference answers, rejected edits, reference comparison and frozen hashes are recorded in `validation/preserved_intro_replay_v129.md`. No manuscript was recompiled or re-exported because its bytes did not change. Prior PDF layout checks remain historical, not a new check in this release.

This small replay-workflow and profile update receives frontmatter, contract-consistency, proof-explanation, changed-link, version and archive-integrity checks. Earlier full-suite results remain historical. The repeated same-agent application is not independent evidence of reader comprehension or general writing quality.

# Validation — v1.28.0

A narrow instruction refinement after an actual application of released v1.27. The candidate and comparison are recorded in `validation/preserved_intro_replay_v128.md`; the candidate was frozen before the instruction change. This is same-agent, context-aware work with one edited sentence, not a blind or independent reader test.

Current validation covers frontmatter, existing contract-consistency and proof-explanation tests, changed links and version metadata, and archive checksums. Prior full-suite and corpus work below remain historical. The companion trial preserves the rest of the manuscript, compiles to 64 pages, and receives layout inspection. No proof certification or general prose-quality guarantee is implied.

# Validation — v1.27.0

Instruction and case-profile update. The actual current-skill application and comparison are recorded in `validation/preserved_intro_replay_v127.md`; the generated candidate precedes the instruction change. It is a same-agent, context-aware local revision, not independent full-Introduction generation or a reader study. Current checks cover frontmatter, existing contract consistency and proof-explanation tests, changed Markdown links, release version consistency, and archive integrity. Earlier complete release-suite results below are historical and were not repeated for this instruction-only change.

The companion manuscript trial preserves the accepted first three source pages and the entire proof body; only three fourth-page fragments differ. TeX compilation and PDF layout checks establish artifact integrity, not mathematical correctness or future skill quality. The ten-paper Naber corpus is retained; no new corpus download or literary attribution is claimed in this release.

# Validation — v1.26.0

Instruction-only update. Current validation checks frontmatter, changed relative links, version consistency, existing contract consistency and proof-explanation tests, and archive checksums. `validation/conceptual_bridge_review_v126.md` records same-agent editorial decisions and negative-transfer cases; it is not a blind generation or independent reader test. Older full-suite results below remain historical. No claim is made that these checks predict future prose quality. Manuscript v126 and earlier delivered articles remain unchanged.

# Validation — v1.25.0

This is an instruction-only extension of the referee protocol. Skill frontmatter, the changed relative links, the existing proof-explanation dependency test, version consistency, and archive checksums are checked. Earlier release-suite results below remain historical. No independent behavioral evaluation or mathematical audit is claimed. The subsequent manuscript application checks original proof preservation and an explicit source mapping for any new introductory restatement.

# Validation — v1.24.0

The present change concerns instructions and a case study. Validation covers skill metadata, modified relative links, the existing proof-explanation dependency test, and archive checksums. The reviewer case was assessed by the same agent that edited the manuscript; no independent referee or complete proof audit is claimed. Previous release-suite results below remain historical and are not a new v1.24 run. The new archive uses one top-level skill folder containing SKILL.md; earlier flat-layout notes describe earlier releases only.

# Validation — v1.23.1

Focused editorial instruction patch. Prior validation below refers to v1.23.0; no new independent-reader experiment is claimed. Package metadata and checksums are regenerated for this release.

# Validation — v1.23.0

## Current release

- Existing complete release suite: PASS, 28 programs; raw log in `validation/release_suite_v123.log`.
- Skill Creator quick validation: PASS.
- Twelve concrete editorial alternatives reviewed manually; decisions and reasons in `validation/editorial_decision_review_v123.md`. This is a same-agent qualitative review, not an independent reader test or an automated behavioral score.
- Changes concern explanatory decisions, supported authorial judgment, and contextual research. Existing validator code and mathematical-preservation contracts are retained.
- Three primary-source locations were inspected for the connection dossier. It distinguishes standard frameworks, the dossier's own normalized specialization, methodological correspondence, and the target paper's remaining obligations.
- The ten-paper Naber inventory and prior corpus observations are retained from v1.22. No new ten-paper download or independent corpus evaluation is claimed in this release.

## Scope of evidence

The release suite checks executable compatibility and existing declared-decision fixtures. The prose cases expose consequential choices, including overexpansion, unsupported adjectives, false norm identification, and false novelty from unequal weights. Neither establishes that future prose will be understood by every reader. Protocol 04q requires text-level justification and an honest statement of the actual evaluation mode.

The user requested a skill update. Previously delivered manuscript TeX/PDF files are unchanged. No installed skill or external configuration was modified.

## Packaging

The archive has SKILL.md at its root, preserving the original flat .skill layout. SHA256SUMS.txt covers every payload file except itself and excludes Python caches. The package is reopened after creation and its payload checksums verified. Relative links in changed Markdown and YAML parsing are checked before packaging.
