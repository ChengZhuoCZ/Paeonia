# Math Manuscript Reconstructor v1.42.0 — One Unified Editorial Voice

**Single default voice; no style choices.** All authorized writing uses one formal, precise, restrained and mathematically ambitious research-paper register (English unless the output language is explicitly specified). The same voice applies to Abstract, Introduction, theorem statements and proofs; density varies only with the mathematical task. The skill resolves conflicting style advice independently using [Protocol 05p](protocols/05p_unified_manuscript_voice.md), the [house profile](profiles/unified_research_mathematics_voice.md), and the [final cross-section checklist](checklists/unified_language_style.md). It does **not** ask for a stylistic author/exemplar by default or offer multiple tones. Already user-supplied reference corpora remain optional subordinate evidence; genuine literature discovery, exact-theorem proof citations and notation audits are unchanged.

**Important:** This supersedes the historical v1.38 "ask once for an author" workflow described below. The reconstruction-versus-local-polish permission question is a separate editing-mode safeguard, not a style choice. Protected text and explicitly required target language/journal rules remain binding. No manuscript was rewritten as part of this release.

---

# Math Manuscript Reconstructor v1.41.0 — Semantic Notation Selection

**New in v1.41: symbols are chosen deliberately, not merely de-duplicated.** Protocol 02h makes Pass 5a an active, field-native symbol-selection procedure: map the real mathematical objects and their relations, honor user/domain conventions, choose readable recurring symbols on representative formulas, and record concise justifications for salient choices in the **existing** `NotationLedger.notation_selection`. It preserves the strict duplicate-symbol and plain-typography audits, the empirical Gui-corpus soft prior, and the `LOCAL_POLISH` protected-baseline policy.

The optional exact-theorem `external_symbol_crosswalk` connects v1.40 proof citation compression with consistent manuscript notation. A small read-only `tools/notation_choice_audit.py` (`--strict` for a locked new Pass 5a) catches inconsistent declared mappings; it does not judge elegance, parse all TeX semantic references, read cited source papers or certify theorem applicability. Added `checklists/notation_selection.md`, an [illustrative spectral-polygon selection](examples/notation_choice_spectral_polygon.yaml), field-conditioned examples, and notation-regression fixtures. No manuscript was rewritten as part of this skill update.

---

# Previous release: v1.40.0 — Precise Theorem-Level Proof Citation

v1.40 makes **exact-theorem proof citation compression** a formal post-draft proof-body stage, **Pass 6a**, not a passive recommendation. During authorized proof reconstruction it reviews substantial proof obligations, locates primary sources, verifies the *actual theorem/lemma/proposition number in a pinned version*, checks all assumptions and needed conclusion strength, then directly replaces duplicated derivations with a precise citation and a short mathematical application. Partially covered arguments retain the unmatched uniformity, endpoint, equality/rigidity, rate and novelty work; inaccessible or circular external results leave the original proof unchanged.

This is implemented by [Protocol 07a](protocols/07a_exact_theorem_citation_compression.md), alongside Protocol 07 citation integrity. A compact [dossier schema](schemas/proof_citation_replacement_dossier.yaml), [review checklist](checklists/exact_theorem_citation_replacement.md), and **read-only structural checker** (`tools/proof_citation_dossier_audit.py`) make replacements traceable. The checker cannot prove that a cited theorem applies. The phase is limited to editable proofs and does **not** globally audit the supplied mathematics or rewrite protected text. Later Introduction research reuses the imported dependencies and credits their authors without claiming them as this paper's innovation.

The v1.39 research-first, fair-credit and evidence-grounded grand Introduction workflow remains in place unchanged.

---

# Previous release: v1.39.0 — Research-First Introduction, Fair Credit, Grand Narrative

v1.39 preserves the v1.36 reader-first engine, the v1.37 conditional PDE architecture, and the v1.38 optional author-corpus supplement. It changes the **Introduction default** for authorized reconstruction: search and compare related mathematical papers first, assign fair and sufficient credit, then construct the broadest *evidence-grounded* programmatic narrative around the exact theorem. It does not alter protected prose or demand a full correctness audit. Author-style literature stays distinct from mathematical-priority literature.

The ordinary Introduction route is now:

`closed theorem truth → optional author-style dossier → 04u outward literature discovery and source checks → credit/frontier map → IntroductionCoreBrief → 04v earned grand-narrative test → conditional PDE extension as applicable → one selected arc → direct prose → reader/credit/program cold read → precise revision`.

The older modules remain available, but they are conditional. More internal ledgers no longer count as better writing.

## Newly default: find the scholarship, then build the story

In `RECONSTRUCT`, Protocol 04u researches the *mathematics*, not merely existing BibTeX entries. Use at least two independent discovery routes when access allows, identify origins, classical benchmarks, nearest competitors, partial and incomparable frontiers, methods, parallel work, and recently changed versions. A compact `IntroductionLiteratureDossier` records actual inspected primary sources, fair-credit assignments and unresolved priority claims. There is **no fixed reference quota**: sufficient, positive attribution matters more than either sparsity or padding. For inaccessible sources, distinguish discovery from verified theorem support; never claim a comprehensive search that did not happen.

Protocol 04v then tests a genuine parent mathematical program. When the program explains a nontrivial transition to the focal theorem, **lead from it** and show why earlier approaches stop at an exact mathematical obstruction. Thread properly credited results through that causal argument, name the conceptual turning point, and return to the program with the theorem's precise contribution and limits. If a broader story is unsupported, choose a specific direct opening rather than prestige rhetoric. Deep Grand Introduction/MathematicalStoryLedgers remain optional; the default is one dossier plus the existing core brief.

For `LOCAL_POLISH`, limit research and edits to literature/novelty language in the approved scope; do not expand the authorized region or erase effective authorial prose. For offline work, mark the research limitation, avoid unverified first/priority claims, and draft only what accessible evidence supports.

See [04u](protocols/04u_literature_discovery_and_credit.md), [04v](protocols/04v_evidence_grounded_grand_narrative.md), [new checklist](checklists/literature_credit_grand_introduction.md), and [research-source notes](references/literature_research_source_notes_v139.md).

## The controlling Introduction brief

Before drafting, record the paper in a compact `IntroductionCoreBrief`:

1. the exact mathematical question;
2. the benchmark theorem, principle, model, or conjecture;
3. the relevant pre-paper frontier—including incomparable nodes when necessary—and the exact remaining gap;
4. the main theorem at its verified scope;
5. the nonroutine obstruction;
6. the conceptual hinge and the new control it unlocks;
7. the theorem's meaning and limits;
8. the verified scholarly contributions needed for fair credit, including close predecessors and relevant parallel work (without a reference-count cap).

These are facts to compose, not eight paragraph slots. The final prose should read as a mathematical argument, not as a form converted into sentences.


## Optional author-corpus supplement

Historical v1.38 behavior asked once for an optional style reference. **Superseded in v1.42:** no author/style prompt is issued. Protocol 05o is activated only by a reference that the user has already provided.

When activated, Protocol 05o resolves the scholar's identity before retrieval and selects a balanced default corpus of four papers, using three to six when the publication record requires it. Selection is not a citation-count ranking. It combines topic proximity, evidence that a work is central to the author's program, recency, research-article genre, and sole-author or cross-collaboration control. Author-prepared preprints or accepted manuscripts are preferred for prose analysis because publisher copyediting may obscure authorial choices.

The resulting `AuthorCorpusDossier` separates:

- reproducible paper metadata, versions, locators and hashes;
- Introduction architecture and mathematical-writing habits supported across papers;
- coauthor, topic and period limitations;
- traits admitted to realization and traits rejected as unstable;
- style use from literature or citation use.

Coauthored papers provide **author-associated corpus evidence**, not proof that one person drafted a passage. Stable habits should recur across papers and, where possible, different collaborator configurations. Downloaded papers are quarantined before drafting; the final prose is composed from abstract decisions rather than remembered sentences. In `LOCAL_POLISH`, the existing manuscript remains the primary voice and the corpus may repair only an identified in-scope weakness. No volunteered style corpus, unresolved identity, weak evidence, unavailable legal full text, or forbidden browsing means immediate continuation with the single default voice, without soliciting preferences.


## Conditional PDE extension

When the theorem is genuinely PDE-governed, Protocol 04t adds only the fields needed to locate and explain it:

- equation, dimension, geometry, boundary/initial data, scaling, and operative regime;
- solution concept and convergence or regularity topology;
- a multi-axis result delta rather than a vague claim of improvement;
- result architecture: single theorem, threshold dichotomy, stratification, hierarchy, singular-limit bridge, stability closure, or solution-class separation;
- structural, technical, normalization, and proof-local assumptions, with stage dependencies when informative;
- a short causal obstruction stack and the mechanism-to-control-to-closure relation;
- separate theorem boundaries, method boundaries, known counterexamples, and open regimes.

The PDE branch does not force a long Introduction. `LOW`, `MEDIUM`, and `HIGH` explanatory burden control compression and theorem presentation; venue prestige never supplies a length target. The primary narrative arc and the theorem's branching architecture are treated as different objects.

## Choose one theorem-facing arc

Use the shortest arc that makes the theorem intelligible. Common possibilities include:

- benchmark → restriction → lost mechanism → theorem;
- conjecture → strongest frontier → missing case → theorem;
- exact problem → obstruction → theorem → conceptual hinge;
- limiting or asymptotic theory → exact finite/global gap → theorem;
- phenomenon → formulation → theorem → explanation;
- scientific model → operative regime → mathematical frontier → theorem.

For a weak or high-stakes Introduction, sketch two six-line alternatives and select one. Do not write several full versions and merge them.

## Reader-first quality contract

A specialist reading only the Introduction should be able to recover:

1. the exact problem;
2. the benchmark that makes it natural;
3. what was known before the paper;
4. what is proved here;
5. why known theory does not already prove it;
6. the central idea that makes the theorem possible;
7. what changes in the mathematical picture, together with the result's limits.

The cold read also applies five negative tests:

- **swap test:** a substantial paragraph must not remain plausible after only the subject nouns are replaced;
- **detachability test:** deleting a paragraph must remove a needed fact, relation, or inference;
- **theorem-latency test:** pre-theorem material must be indispensable, not ceremonial;
- **proof-resolution test:** the overview reveals the bottleneck but compresses bookkeeping;
- **voice test:** prose follows mathematical questions rather than ledger order or administrative transitions.

The theorem is stated as soon as it is accurately readable. Page 2 is entirely acceptable when the benchmark, restriction, exact frontier, and minimal notation are genuinely needed. It is not acceptable when detachable history or grandeur causes the delay.

## Paragraphs and literature

Paragraphs are organized by **information change**, not by one mandatory role per paragraph. Benchmark, literature, and obstruction may coexist when they establish one coherent mathematical move.

Literature is grouped by the mathematical claim it supports:

`verified status → citations → consequence for the present problem`.

Avoid author chronology, repeated statements that prior work “does not cover” the current theorem, and literature paragraphs that do not change the reader's understanding of the frontier.

## Proof overview

Explain the conceptual hinge and the few stage interfaces needed to see why the argument works. For each indispensable stage, give the available input, the operation that changes the problem, and the output that makes the next stage possible.

Do not foreground denominators, cutoffs, case names, local labels, or a section-by-section itinerary unless one of those is itself the central mathematical difficulty.

## Conditional modules

The following tools are retained but are no longer stacked by default:

- `MathematicalStoryLedger`: use when a genuine parent program or a nontrivial transition such as continuum→finite, local→global, or asymptotic→exact changes the theorem's meaning.
- `ScientificContextLedger`: use when a model, physical mechanism, scaling, or regime is mathematically operative.
- Protocol 04p/04q deep explanation: use when a central representation or long proof cannot be understood from the compact overview.
- `NarrativeAmbitionLedger` and `EditorialImpactAudit`: use for verified conjecture resolutions, classifications, first global results, sharp theorems, or a demonstrated under-positioning defect.
- `IntroductionNarrativeLedger` and `IntroductionParagraphPlan`: use only for unusually complex multi-theorem, literature-heavy, or long model-driven Introductions.
- Narrative amplification: off by default; use only to repair a specific, evidence-backed under-positioning problem.

Optional modules may add depth. They may not override the core brief, theorem indispensability, swap test, or reader contract.

## Writing modes

Before a new writing task, ask whether the user wants full reconstruction or local polishing unless the choice is already explicit.

- `RECONSTRUCT`: rebuild the authorized region from the mathematics and verified literature. Existing prose can supply facts, terminology, citations to verify, and authorial priorities, but not a compulsory paragraph sequence.
- `LOCAL_POLISH`: preserve the selected draft's effective voice and sequence; make only demonstrated, scope-bound repairs.

Mode and editable scope are binding throughout continuation.

## Default interaction: arrange, then write — full-manuscript reconstruction

When the supplied proof is trusted mathematical input, the ordinary workflow is:

1. recover theorem semantics and the dependency structure;
2. resolve writing mode and scope, and fix the single Protocol 05p editorial voice automatically—do not ask for a style selection;
3. only if the user has already supplied a style-author or exemplar reference, resolve identity, retrieve and version-lock a legal representative corpus, distill compatible habits, and quarantine source prose;
4. choose the writing order and stable notation;
5. write and check the proof body;
6. reconstruct theorem statements;
7. search and verify related mathematical papers beyond inherited citations (04u), record fair credit and prior-frontier comparisons;
8. build `IntroductionCoreBrief`, apply the earned programmatic-grand-narrative test (04v), activate the conditional PDE extension when applicable, and select one arc;
9. draft the Introduction directly, using only admissible abstract corpus traits;
10. run the reader/credit/program contract, overlap check when applicable, and factuality/citation checks;
11. write the Abstract under Protocol 04s;
12. finish with authorial, notation, LaTeX, and requested editorial audits.

A full proof verification is not silently added to a writing task.

## Preserved capabilities

The v1.36 simplification, v1.37 PDE specialization, and v1.38 author-corpus supplement do not remove the package's other systems:

- trusted-proof and opt-in proof-verification modes;
- theorem and notation architecture;
- source-independent reconstruction;
- citation inventory and exact theorem/lemma replacement under Protocol 07;
- authorial naturalization without random synonym rotation;
- paragraph, section, and whole-paper style diagnostics;
- scientific-context research when the model-to-mathematics chain is genuinely relevant;
- behavioral and contract-consistency tests.

The historical grand-narrative, scientific-context, mathematical-story, and style modules remain as conditional resources. Their release notes describe why they were introduced; Protocol 04 now governs whether they should be used.

## Trusted proof mode

```yaml
proof_correctness_mode: trusted_source
independent_correctness_audit: false
mathematical_repair_authorized: false
```

Switch to `verify_proof` only when the user asks to check correctness, find gaps, referee the argument, stress-test a step, or repair mathematics.

## Release validation

Run from the package root:

```bash
python tests/run_release_suite.py
```

The suite checks package contracts and declared behavioral fixtures. It does not certify the mathematical correctness of arbitrary manuscripts or guarantee literary quality. Actual Introduction evaluation still requires theorem-aware editorial judgment and comparison on representative papers.
