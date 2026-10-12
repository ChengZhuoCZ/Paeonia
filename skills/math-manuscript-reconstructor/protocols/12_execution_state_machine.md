# Protocol 12 — Direct Composition State Machine

Version 1.13 uses a **proof-first, trusted-proof direct-composition** state machine with early notation architecture and post-closure theorem packaging. Ordinary writing begins by understanding the mathematics, choosing a clean writing order, and drafting the proof body. Planner/governance states are optional and are used only for explicit orchestration, recovery, audit, or package-development tasks.

## Mode applicability

Resolve [writing mode and scope](00_writing_modes.md) first. The canonical sequence below is for full reconstruction. `LOCAL_POLISH` uses task setup, `EDIT`, scoped `AUDIT`, and `RELEASE`; it retains the baseline and does not execute source quarantine, proof redrafting, architecture reconstruction or new proof-closure certification. Selected-region reconstruction uses scoped extraction and composition from trusted sources without redrafting a protected proof body. Optional planning must preserve these boundaries.

## Canonical full state order

`TASK_CONTRACT → WRITING_ORDER → INGEST → EXTRACT → LEDGER_LOCK → SOURCE_QUARANTINE → STYLE_EXTRACT → PARAGRAPH_FINGERPRINT_LOCK → SECTION_FINGERPRINT_LOCK → WHOLE_PAPER_FINGERPRINT_LOCK → STYLE_QUARANTINE → PROOF_GRAPH → NOTATION_ARCHITECTURE → PROOF_CORE → PROOF_CORE_GATE → MANUSCRIPT_ARCHITECTURE → WHOLE_PAPER_NARRATIVE → SECTION_NARRATIVE → THEOREM_FRAME → INTRODUCTION_NARRATIVE → FRONTMATTER → EDIT → RESIDUE_DIAGNOSIS → AUTHORIAL_DECISION → PARAGRAPH_RHYTHM → MATHEMATICAL_TRANSITIONS → COLD_AUTHOR → AUDIT → RELEASE`

## Direct writing prelude

### TASK_CONTRACT
Record the requested deliverable, permissions, audience, source availability, style-corpus availability, proof-closure status, and `proof_correctness_mode`. Default to `trusted_source` for ordinary writing. Keep this concise and usually internal. No manuscript prose.

### WRITING_ORDER
Before drafting, infer a clean exposition order from the target mathematics. Identify definitions, genuine prerequisites, proof engines, the main proof path, and the natural location of equality/rigidity/endpoint closure.

For a substantial writing request, the user-facing output may begin with a short writing-order plan. Then continue directly into manuscript prose in the same response/workflow. Do not stop at planning unless the user asked only for an outline.

`EXECUTION_PLAN` remains available as an optional governance state only for explicit orchestration, recovery, audit, or package-development tasks.

## Optional governance states

`EXECUTION_PLAN` is a recognized optional state for explicit orchestration, recovery, audit scheduling, or package-development workflows. It is **not** part of the ordinary direct-composition path. When activated, apply `protocols/15_adaptive_research_director.md`.

## Source and proof states

### INGEST
Read mathematical sources and any already supplied style corpus. Apply the single default Protocol 05p voice without seeking stylistic choices. Protocol 05o runs only when the user has already supplied an author, exemplar or corpus; if activated, resolve identity and acquire legally accessible sources before optional abstract style extraction. **Do not ask for an author/style preference.** No drafting.

### EXTRACT
Convert mathematical sources into semantic claims and mechanisms. No prose reuse.

### LEDGER_LOCK
Lock exact theorem semantics, assumptions, ranges, constants, and equality cases relative to the supplied proof. In `trusted_source` mode do not independently diagnose mathematical validity; record only source-availability problems. In explicit `verify_proof` mode, also record unresolved mathematical issues.

### SOURCE_QUARANTINE
Mathematical sources become verification-only. Returning to source for line-by-line paraphrase is forbidden.

## Conditional style-corpus states

These states are required when a supplied style corpus is meant to influence manuscript prose. They may be skipped when no style corpus exists, but universal mathematics-driven architecture rules remain active.

### STYLE_EXTRACT
For a Protocol 05o corpus, first complete `AuthorCorpusDossier` with identity, selection, versions, hashes, attribution caveats, and scope. Perform the style extraction appropriate to the task into `LanguageStyleLedger` and `MathematicalWritingStyleLedger`; full paragraph/section/whole-paper fingerprinting is required only when scope and evidence justify it. Internal analysis only.

### PARAGRAPH_FINGERPRINT_LOCK
Extract paragraph-boundary rules, role-pressure asymmetry, opening modes, internal movement, and qualitative transitions. Numeric fitting is forbidden.

### SECTION_FINGERPRINT_LOCK
Extract section-boundary rules, theorem-latency modes, lemma-cluster grouping logic, subsection triggers/suppressors, pressure behavior, and closure modes.

### WHOLE_PAPER_FINGERPRINT_LOCK
Extract global proof-spine traits, result exposure behavior, technical-mass concentration, front-matter compression, appendix modularity, and whole-work asymmetry. Apply research projection when the corpus is expository rather than a research article.

### STYLE_QUARANTINE
The style corpus becomes verification-only. Draft from abstract traits, not source sentences.

## Proof-first manuscript states

### PROOF_GRAPH
Build the proof dependency graph and proof-body blueprint. No final-form Introduction or Abstract.

### NOTATION_ARCHITECTURE

Apply `protocols/02d_notation_architecture.md` **and Protocol 02h semantic notation selection**. From the locked mathematics and proof graph, first select symbols on field conventions, structural relationships and representative formulas, then build the existing `NotationLedger` before publication proof prose is drafted. Fix canonical symbols, normalizations, index families, operator/measure conventions, local/global pairs, and constant families. Run the notation-choice structural audit and existing collision/typography audits; no new state or dossier is created.

This state may not strengthen or alter the mathematics. If notation cannot be made coherent because two source claims use genuinely incompatible normalizations, return to `LEDGER_LOCK` rather than hiding the conflict.

### PROOF_CORE
Write the first manuscript prose: proofs and only the statements/setup needed to make those proofs intelligible.

### PROOF_CORE_GATE
After a proof core has been drafted, **Pass 6a** applies [Protocol 07a](07a_exact_theorem_citation_compression.md) to find exact prior-theorem replacements for repeated proof obligations in authorized proof regions. It checks newly imported source statement/number/version and the precise application before deleting any proof; an unavailable source leaves the trusted original proof intact. Material candidates may use `ProofCitationReplacementDossier` without changing the canonical state order or creating a new governance state.

In `trusted_source` mode, verify faithful coverage of the supplied proof paths, semantic agreement, and applicable style-source independence; do not independently re-prove them. A newly introduced external citation must cover the replaced material at full strength. In explicit `verify_proof` mode, additionally verify mathematical closure. A blocker here prevents front-matter drafting.

## Reader-facing architecture states

### MANUSCRIPT_ARCHITECTURE
Generate a fresh reader-facing paper graph around the closed proof core. This state is always mathematics-driven; a style fingerprint, when available, is only a conditional prior.

### WHOLE_PAPER_NARRATIVE
Realize the global research-paper spine. Separate main-result statement exposure from proof activation and closure. Place technical mass by proof pressure and apply the appendix modularity test.

### SECTION_NARRATIVE
Realize section architecture from target obligation families. Theorem latency follows prerequisite burden; subsections require stable internal phases.

### THEOREM_FRAME

Apply `protocols/02c_theorem_statement_architecture.md`. Build `TheoremStatementLedger` from the closed MathLedger and passed proof core. Decide theorem grouping, reader order, explicit assumptions, normalization, quantitative strengthening, and equality/rigidity clauses before Introduction prose is written.

Finalize theorem/lemma packaging and exact displayed statements by semantic checksum.

### INTRODUCTION_NARRATIVE
For reconstructed Introductions, apply Protocol 04u **after theorem framing and before prose**: build the theorem fingerprint, search outside inherited references, verify pivotal original sources and claim support, and assign fair credit. Record one `IntroductionLiteratureDossier`, with research-access limits. Apply Protocol 04v to test a source-grounded parent-program story and select its defensible scale; the extended story ledgers remain optional. In `LOCAL_POLISH`, restrict these passes to changed in-scope claims.

Build `IntroductionCoreBrief` after theorem framing. Record the exact question, benchmark, pre-paper frontier, main theorem, nonroutine obstruction, conceptual hinge, unlocked control, meaning, limits, and essential literature claims. For a PDE-governed theorem, activate Protocol 04t and add only the operative theorem coordinates, multi-axis result delta, result architecture, assumption roles, causal obstruction stack, mechanism-to-control bridge, and typed scope boundaries. Select one theorem-facing narrative arc. No final Introduction prose is written in this state.

Instantiate `IntroductionNarrativeLedger`, `MathematicalStoryLedger`, `NarrativeAmbitionLedger`, `ScientificContextLedger`, or `IntroductionParagraphPlan` only when the trigger in Protocol 04 is present. The legacy phrase “one dominant role per paragraph” means one primary information change inside the optional plan; it does not forbid integrated secondary functions.

### FRONTMATTER
Write the Introduction directly from the research-backed `IntroductionCoreBrief` and selected arc, then run the seven-question reader contract and the scholarship/credit/program questions, swap test, detachability test, theorem-latency test, proof-resolution test, and voice test. When the PDE branch is active, add only its applicable coordinate, delta, assumption, closure, topology, and boundary checks. Produce `ReaderContractAudit`. Apply narrative amplification or produce `EditorialImpactAudit` only for a recorded, evidence-backed positioning trigger. Produce `IntroductionProseAudit` only when the extended compatibility route is used. Write the Abstract after the substantive Introduction is stable. This state is inadmissible without verified proof closure, either in the current run or through a reusable validated `ProofCoreGateReport`.

## Editorial and naturalization states

### EDIT
Perform paragraph, sentence, notation, and LaTeX refinement. Re-check semantic and applicable style fidelity.

### RESIDUE_DIAGNOSIS
Run recurrence, signposting, formula-followup, rhythm, and proof-geometry diagnostics. Classify flags; do not synonymize automatically.

### AUTHORIAL_DECISION
Allocate prose density by mathematical role. Preserve delicate justifications and compress routine narration.

### PARAGRAPH_RHYTHM
Realize paragraph boundaries and role-sensitive density from target mathematical state. With a style corpus, use its fingerprint only as an abstract conditional prior.

### MATHEMATICAL_TRANSITIONS
Replace administrative continuity with explicit mathematical relations where useful. Repetition is repaired by function, not lexical rotation.

### COLD_AUTHOR
Freeze mathematics and perform a deletion-oriented pass. Remove sentences that do not state mathematics, give a mathematical reason, or supply a necessary orientation cue.

## Audit and release states

### AUDIT
Run the audits applicable to the requested deliverable. In direct-composition mode this is determined from the deliverable itself; no `ExecutionPlan` is required. In explicit orchestration/audit mode, applicability may be listed in the plan. A gate may be claimed only if its required evidence artifacts exist.

On failure, use `protocols/16_gate_repair_routing.md`; do not improvise a repair at the wrong layer.

### RELEASE
Return the requested deliverable only with accurate status. Release builds of the skill itself additionally require behavioral-regression and contract-consistency tests.

## Ordering invariants

The following are unconditional when the corresponding states occur:

- `TASK_CONTRACT` precedes `WRITING_ORDER` in ordinary writing mode.
- `LEDGER_LOCK` precedes `PROOF_GRAPH` for source-based reconstruction.
- `PROOF_GRAPH` precedes `NOTATION_ARCHITECTURE`, which precedes `PROOF_CORE` for nontrivial proof production.
- author-corpus acquisition, applicable style extraction, and quarantine precede `PROOF_CORE` when that corpus controls prose.
- `PROOF_CORE` precedes `PROOF_CORE_GATE`.
- `PROOF_CORE_GATE: PASS` precedes current-run `INTRODUCTION_NARRATIVE` and `FRONTMATTER`.
- `THEOREM_FRAME` precedes `INTRODUCTION_NARRATIVE` for substantial full-manuscript front matter.
- `MANUSCRIPT_ARCHITECTURE` precedes reader-facing whole-paper and section realization.
- `WHOLE_PAPER_NARRATIVE` precedes `SECTION_NARRATIVE` in full-manuscript reconstruction.
- semantic repairs precede stylistic repairs when both are stale.

## Rollback and invalidation

A failed gate does not merely halt. Route it through `registry/gates.yaml`.

In explicit `verify_proof` mode, a mathematical correction discovered after `LEDGER_LOCK` rolls back to `EXTRACT/LEDGER_LOCK` for affected semantic units and invalidates downstream proof and front-matter artifacts that depend on them.

A style correction discovered after `STYLE_QUARANTINE` rolls back to `STYLE_EXTRACT` unless mathematics changed.

A naturalization edit that appears to require new mathematics is not a naturalization edit; route it to the proof layer.

A repair must re-audit every gate listed by the gate registry. Stale downstream prose may not survive merely because it still reads well.
