---
name: paeonia
description: Reconstruct mathematical manuscripts, locally polish a draft, or audit references in one consistent research-mathematics voice without offering style options. Choose field-native notation, use exact verified theorem citations where applicable, and research related mathematics before writing evidence-grounded Introductions; preserve theorem scope and protected text.
metadata:
  version: 1.42.1
  category: mathematics-writing
  status: research-grade
  entrypoint: SKILL.md
---

# Paeonia

## Unified language style — no stylistic selection (v1.42)

Use [Protocol 05p — unified manuscript voice](protocols/05p_unified_manuscript_voice.md) and its [single default profile](profiles/unified_research_mathematics_voice.md) for **every** authorized manuscript writing pass. Default to precise, restrained, mathematically ambitious research-paper English; honor an explicitly specified language or mandatory journal style. The same register spans Abstract, Introduction, theorem statements, proofs and remarks, while explanation density follows genuine mathematical difficulty. **Do not ask the user to choose a tone, style profile, exemplar author or variant.** Resolve conflicts independently using mathematical fidelity, authorized scope and requirements, field clarity, the unified house voice, then optional corpus evidence. Deliver one coherent draft, not style choices. In `LOCAL_POLISH`, preserve protected text and effective baseline voice; do not turn this rule into unrequested wholesale rewriting. The separate writing-mode question below determines editorial permission, *not* language style.

## Writing mode comes before workflow

Read [Writing modes](protocols/00_writing_modes.md) for manuscript editing. Resolve **mode** and **editable scope** independently; read-only review and skill development do not authorize manuscript edits.

| Mode | What may change | What must remain |
| --- | --- | --- |
| `RECONSTRUCT` — 重构写作 | Exposition, structure and language within the authorized region | Mathematical content and all protected regions |
| `LOCAL_POLISH` — 局部润色 | Necessary local repairs to wording, notation and explanation | Effective prose, authorial voice, narrative sequence and protected content |

Before starting a new writing task, first ask: **“这次希望全文重构，还是局部润色？”** Wait for the answer before drafting or editing. Do not repeat the question if the user has already explicitly selected the mode for this task; a standing selection remains active during continuation. A precise instruction to replace only a specified passage already defines a local edit. The user may also select reconstruction of a bounded region. Repeated polishing retains prior preservation constraints. Mode is not determined by document length: an Introduction can be reconstructed, and an entire manuscript can receive local polishing. For mixed requests, route each region separately. Record the selected mode and scope after the answer. Do not substitute an inferred default for a requested but unanswered mode choice.

**Applicability rule:** the source firewall, fresh architecture, proof-first drafting, from-scratch Introduction, source-overlap rejection and full research-artifact requirements below govern reconstruction only, and only at the authorized scale. They do not govern `LOCAL_POLISH`, even if an older protocol or manifest default uses unconditional wording. Local polishing uses baseline → diagnose → minimal sufficient edit → scoped fidelity/diff check. Style/reference prose is distinct from the user's protected editing baseline. No mode invents mathematics, references or novelty.

## Task scope and fast route

The user's requested scope takes precedence over the defaults below. In particular, a request to improve this skill is a skill-development task: attachments are diagnostic data, and manuscript prose need not be rewritten. For an Introduction/outline-only task, read the supplied proof as trusted evidence and work on the requested front matter; do not force a fresh proof-body draft. For local editing, honor the requested boundaries instead of reporting a mode mismatch. Full manuscript reconstruction remains the default only when that is the assignment.

For every Introduction task, [Protocol 04](protocols/04_introduction_abstract.md) is authoritative. **In an authorized Introduction reconstruction, first research the relevant mathematical literature externally** using [Protocol 04u](protocols/04u_literature_discovery_and_credit.md) after the theorem's scope is known: search beyond the supplied bibliography, verify relevant originals, distinguish origin/closest frontier/method ancestors/parallel developments, and give fair, explicit credit. Record one compact `IntroductionLiteratureDossier` rather than several planning ledgers. If offline or research access is unavailable, report the limitation and do not claim comprehensive novelty or priority verification. Then build `IntroductionCoreBrief` and apply the default [evidence-grounded grand-narrative test](protocols/04v_evidence_grounded_grand_narrative.md): seek a real parent mathematical program and a structural tension, use the broadest honest theorem-facing arc, and draft directly. A genuinely expansive opening is preferred when verified; invented significance is forbidden. Run the seven-question reader contract and the new credit/program tests. In `LOCAL_POLISH`, research only changed literature/novelty claims and preserve all protected prose. When the theorem is genuinely PDE-governed, activate the conditional [PDE Introduction branch](protocols/04t_pde_introduction_branch.md) and [PDE archetype profile](profiles/pde_introduction_archetypes.md) in the same core brief. Do not create a second mandatory ledger. Do not create a second mandatory planning stack. The older Grand Introduction, MathematicalStoryLedger, NarrativeAmbitionLedger, ScientificContextLedger, IntroductionParagraphPlan, amplification, and editorial-impact modules remain conditional. More planning artifacts do not imply better prose.

**Notation selection is now an explicit part of Pass 5a, not just a collision/typography audit.** Apply [Protocol 02h — semantic notation selection](protocols/02h_semantic_notation_selection.md) after the mathematical proof graph is known and before proof-core drafting. Select field-native symbols for high-salience objects, compare alternatives on real formulas, use structural symbol families, preserve correct user-fixed notation, and record only meaningful choice rationales in `NotationLedger.notation_selection`. Use [the notation-selection checklist](checklists/notation_selection.md) and the read-only structural checker, without inventing a numerical beauty ranking or a second mandatory ledger. The method stays scoped in `LOCAL_POLISH` and read-only review. After Pass 6a, recheck any exact-theorem source-to-paper symbol crosswalk against the verified external source's assumptions, endpoints and normalizations.

Style references are never a user-facing selection step. Use [Protocol 05o](protocols/05o_author_corpus_supplement.md) **only if the user has already provided a named author, exemplar or corpus for style analysis**; then verify identity and legally available versions, distill compatible abstract traits and quarantine source prose. Do not proactively ask for an author or style preference. Without a style corpus, proceed using the single Protocol 05p house voice. Mathematical literature searches for fair credit under 04u remain mandatory where applicable and must not be conflated with optional author-style retrieval.

When the user has selected prose to preserve, that text is the editing baseline, not merely a style sample. A later request to polish again does not reset this choice. Diagnose a specific remaining reader inference or fidelity issue before editing; retain passages that already work. For an explicitly requested apply–compare–adjust cycle, use the bounded replay in [Protocol 04q](protocols/04q_outline_cold_read.md), separating actual edited output from inherited prose.

For a central reformulation, a difficult proof route, or feedback that the article is flat or hard to understand, read [Protocol 04p](protocols/04p_reformulation_and_proof_explanation.md) before paragraph planning and [Protocol 04q](protocols/04q_outline_cold_read.md) before final compression. The [Naber corpus profile](profiles/naber_introduction_and_outline.md) supplies evidence-based explanatory choices. This route applies even to `STANDARD` introductions when the mechanism needs explanation. Diagnose the missing reader inference before choosing a repair. Explain why the representation meets the proof's requirements, expose the operation at the bottleneck, and research the method's nearest mathematical neighbors when broader relevance is requested. Express the supported mathematical assessment in language fitted to the actual discovery. User-supplied phrases are examples of expressive range unless exact wording is explicitly requested; they are neither required tokens nor a vocabulary to rotate. Follow Protocol 04p for choosing emphasis without flattening the contribution.

For a referee-style assessment or a request to improve this skill from a polished manuscript, read [Protocol 04r](protocols/04r_referee_perspective.md). Separate contribution positioning, reader comprehension, and reproducibility of the decisive argument. Inspect the requested scope and report concrete issues before selecting a rewrite; a reviewer perspective does not automatically launch a complete correctness audit. When revision is requested afterward, use that protocol's revision section to distinguish source-backed edits from unresolved mathematical work, and verify any introductory restatement against its source theorem.

When a user selects an Introduction as a positive writing target, or a technically complete draft obscures its main discovery, use the [conceptual-bridge profile](profiles/conceptual_bridge_introduction.md) with Protocol 04p. Learn why the example makes a relation visible, rather than copying its order or vocabulary. Compose the central mathematical explanation and then the necessary proof dependencies at an appropriate level of detail; do not turn an internal audit into the Introduction. Respect any frozen prose or page boundaries during local editing.

For abstract writing or an apply–compare–adjust cycle against a user-supplied abstract, read [Protocol 04s](protocols/04s_abstract_calibration.md). Diagnose the mathematical work performed by each sentence, preserve the exact theorem scope, and make the decisive relation legible without importing the full proof outline. Compare a frozen actual candidate with the reference before changing the skill again; a familiar preferred abstract is a calibration example, not an independent test.

For reference verification, bibliography repair, or writing that adds or changes a citation, use [Protocol 07](protocols/07_citation_integrity.md). It separates local citation inventory from verification of bibliographic metadata, version-specific locators and support for the adjacent claim. **Discovery of omitted or competing relevant scholarship is a separate Introduction obligation under Protocol 04u**; checking the manuscript's own `.bib` alone cannot fulfill it. An explicit all-reference check covers every bibliography entry, including uncited ones; a narrow edit rechecks affected references without launching an unrelated proof audit.

**Proof-citation compression is now a named stage, Pass 6a, of editable proof reconstruction.** Apply [Protocol 07a — exact-theorem citation compression](protocols/07a_exact_theorem_citation_compression.md), using [Protocol 07](protocols/07_citation_integrity.md) for source verification: systematically review substantive proof obligations, locate exact externally proved theorems/lemmas/propositions, verify the primary full-text statement and the cited version/number, map its hypotheses and conclusion to the local claim, and **replace redundant proof portions directly** only when justified. Keep every unmatched quantitative bound, parameter-uniform estimate, endpoint, equality/rigidity argument, necessary adaptation and conceptual bridge. An inaccessible theorem, invented locator or circular dependency cannot justify deletion. The stage respects authorized proof regions in `LOCAL_POLISH` and is inapplicable to Introduction-only or read-only tasks. The replacement applicability check is required even in `trusted_source` mode, without constituting an independent correctness audit of the original proof.

## Mission

Produce publication-grade mathematical exposition through the selected mode: reconstruct from mathematical sources, or improve an existing draft while preserving its successful prose.

For a full reconstruction assignment, the defining invariant is:

> **Every supplied proof, manuscript, note, LaTeX file, draft, or partial article is reference material only. The final article must be rebuilt from scratch.**

In full reconstruction, extract mathematical content, erect a source firewall, synthesize a new paper architecture, and reconstruct the exposition before language refinement. For requested polishing, targeted revision, or review, retain unaffected content and use only the relevant explanatory or diagnostic passes.

The skill is designed primarily for pure and theoretical mathematics, including analysis, PDE, geometric analysis, spectral theory, probability, combinatorics, calculus of variations, harmonic analysis, and adjacent areas.

---

## 0. Non-negotiable constitution

These rules apply within the user-selected scope. Full-reconstruction requirements, including fresh architecture and proof-body-first drafting, do not override a request for targeted polishing or review.

### C0.1 — Reference-only source rule

In full reconstruction, supplied mathematical manuscripts and proofs are evidence sources, never prose templates. In targeted revision, the supplied manuscript is also the editing baseline; preserve content outside the authorized changes.

Allowed inheritance:
- mathematical statements and logically necessary hypotheses;
- definitions and normalizations;
- valid proof mechanisms;
- identities, estimates, constructions, calculations, and case distinctions;
- equality cases, rigidity arguments, endpoint behavior, and constant dependencies;
- external theorems actually used;
- computational certificates when explicitly part of the mathematics.

Forbidden inheritance in full reconstruction:
- section order;
- subsection order;
- lemma/proposition numbering;
- proof step numbering;
- paragraph order;
- titles and subtitles;
- narrative transitions;
- prose phrasing;
- internal project labels;
- dependency-list prose;
- historical engineering scaffolding;
- old theorem grouping merely because it appeared in the source.

A full reconstruction must have a newly synthesized logical architecture. A local revision need not replace an effective architecture.

### C0.2 — Source firewall

Full reconstruction has two distinct phases; local editing and review may inspect their baseline throughout.

**Extraction phase:** inspect the source and build a mathematical ledger.

**Reconstruction phase:** draft from the ledger and a newly created architecture, not from the source prose.

After the ledger is complete, the raw source is considered quarantined. Re-open it only to verify a disputed mathematical detail, recover a missing exact formula, or check provenance. Do not resume line-by-line rewriting.

### C0.3 — No silent mathematical drift

Without explicit permission to change mathematics, never:
- alter quantifiers;
- strengthen conclusions;
- weaken hypotheses;
- change parameter ranges;
- alter equality cases;
- change normalization conventions;
- change the dependence of constants;
- replace exact identities by asymptotics or conversely;
- exchange `o`, `O`, `\lesssim`, or explicit bounds without justification;
- turn a heuristic/formal argument into a claimed rigorous proof;
- close a proof gap by invention;
- introduce a stronger external theorem than the cited input actually supplies.

In ordinary `trusted_source` writing, do not independently search for mathematical defects. A requested referee assessment may inspect selected proof interfaces and report unresolved `MATHEMATICAL-CHECK` items, with their scope and evidence. A complete correctness audit remains a separate request. Preserve the distinction between an unclear argument, a suspected issue, and a verified error.

### C0.4 — Structure follows the selected writing mode

Full reconstruction does not preserve source structure by default. If the user explicitly requests a local edit or a bounded Introduction/outline revision, honor that narrower task and retain the surrounding manuscript. Do not report `MODE_MISMATCH` merely because the requested scope is smaller than full reconstruction.

### C0.5 — No invented scholarship

Never invent references, bibliographic metadata, theorem numbers, priority claims, historical claims, or journal style requirements. Unverified items are marked `CITATION-CHECK` or `FACT-CHECK`.

### C0.6 — Preserve proof substance, not proof packaging

In reconstruction, “keep every proof detail” preserves every mathematically operative detail while permitting new exposition, grouping and local order. In local polishing, retain both the proof substance and its existing packaging except where a requested repair requires a bounded change. A verified citation-based replacement under Protocol 07 preserves substance through an exact external result and a checked application; it does not permit deletion of unmatched arguments or protected text.

### C0.7 — Proof-body-first composition

For full reconstruction, the **proof body is the first manuscript prose drafted**. An existing supplied proof suffices as the source for a bounded exposition pass; review-only work need not draft manuscript prose. Before the proof core is written, only internal research artifacts may exist: `TaskContract`, `MathLedger`, `DependencyGraph`, `ProofGraph`, semantic claim specifications, and source/style firewall reports.

In full reconstruction, do not draft final-form title prose, abstract, introduction, literature narrative, organization paragraph, or polished theorem framing before the `ProofCoreGate` has passed. Working claim specifications such as `CLAIM-MAIN` are allowed because the proof needs a precise target, but they are not publication prose.

The purpose is structural: the final claims and front matter must be induced by what the proof actually establishes, rather than forcing the proof to conform to an introduction written too early.

### C0.8 — High-intensity conditional style distillation firewall

A supplied style document is a **style corpus**, not a prose template and not an author persona. For reconstruction using a new style corpus, build the base ledgers before manuscript prose is written. Local polishing may use existing abstract observations without rebuilding all corpus ledgers; its editing baseline is not a quarantined style corpus. The base ledgers are:

- `LanguageStyleLedger`: sentence cadence, clause architecture, mathematical verb profile, first-person policy, transition semantics, certainty language, parenthetical behavior, and formula/display grammar;
- `MathematicalWritingStyleLedger`: proof openings, local goal visibility, obstruction-driven method changes, theorem/lemma insertion logic, equation/prose rhythm, justification locality, case/generality bridges, technical-estimate structure, and closure behavior.

When the corpus is large enough to support multiple mathematical functions, **global averages are insufficient**. Apply `protocols/05m_high_intensity_corpus_distillation.md` and build a `ConditionalStyleLedger` that stratifies the corpus by mathematical role, checks cross-fold stability, and records how prose changes with mathematical pressure. The target is conditional covariance—routine versus delicate proof motion, theorem lead-in versus section opening, bridge versus closure—not numerical imitation of source distributions.

Every nontrivial trait must be supported by repeated corpus evidence when the corpus is large enough. Store only aggregate counts/rates, abstract labels, and optional line/page locators—never source sentences.

Forbidden by default:
- copying distinctive sentences or paragraph skeletons;
- imitating an identifiable author's verbal tics;
- preserving source examples, historical asides, or pedagogical apparatus merely to sound similar;
- using the style corpus as a sentence bank;
- mechanically reproducing transition-word frequencies;
- inferring style from a single attractive passage when a larger corpus is available;
- using one global average to override role-conditioned evidence;
- treating source medians, variances, or fold statistics as prose targets;
- using a textbook/monograph corpus to manufacture research-priority rhetoric.

After the abstract ledgers are built, quarantine the style corpus exactly as the mathematical source is quarantined. For substantial corpora, the proof core must use the role-conditioned `ConditionalStyleLedger` via `protocols/05n_conditional_style_realization.md`; it must not flatten every paragraph toward a single global style average or look back and forth at source prose.

### C0.9 — Authorial mathematical prose, never cosmetic humanization

Naturalization must come from **mathematical decisions**, not randomness. The manuscript should vary in density, syntax, paragraph shape, and explicitness only when the mathematics gives a reason.

Required principles:
- routine mathematics is compressed;
- structural moves are named concisely;
- delicate legality, uniformity, endpoints, topology, and equality propagation are explicit;
- bridges identify the obstruction that forces a change of method;
- proof closure stops at the mathematical endpoint;
- transitions encode mathematical relations rather than document administration.

Forbidden operations:
- random synonym substitution;
- random sentence shortening or paragraph splitting;
- deliberate grammar mistakes or typos;
- fake uncertainty or fake personal voice;
- artificial colloquialism;
- random transition rotation;
- numerical optimization against an AI-detector score.

The target is `authorial_mathematical_prose`: lower template residue, higher mathematical-action density, and information rhythm explained by proof structure.


### C0.10 — Paragraph boundaries are mathematical decisions

When a style corpus is supplied, build a `ParagraphFingerprintLedger` before proof drafting. A paragraph boundary is justified by a change in mathematical state—obligation, method, regime, legality, auxiliary return, equality/rigidity, substantial display consequence, conceptual pause, or closure—not by a target length or desire for visual variety.

The skill must preserve **role-sensitive paragraph pressure**: routine passages may remain thin, while delicate legality and bridge passages thicken locally. Aggregate source paragraph lengths, role frequencies, and transition counts are evidence only and may never be optimized as generation targets. Exact source paragraph sequences and paragraph skeletons remain forbidden.

### C0.11 — Sections are obligation families, not containers

When a style corpus is supplied, build a `SectionNarrativeFingerprintLedger` before proof drafting. A section boundary must correspond to a section-scale mathematical change: a new obligation family, object/space, method family, regime/geometry, reusable engine, application phase, construction phase, or synthesis/return.

Theorem placement is conditional. The principal theorem may be `IMMEDIATE`, `MOTIVATED`, `DEVELOPED`, or `DEFERRED` according to prerequisite burden. No fixed source distance from heading to theorem may be reused.

Subsections are optional. Create them only for stable internal phases that deserve independent reader re-entry. Do not create subsections merely to break length, imitate the style corpus, or disguise proof steps.

Conceptual and technical sections form a mathematics-driven pressure wave, never a forced alternation. Source section counts, lengths, role sequences, theorem latencies, and subsection rates are evidence only and may never become generation targets.

### C0.12 — Whole-paper mass follows the proof spine

When a style corpus is supplied, build a `WholePaperNarrativeFingerprintLedger` before proof drafting. It records only abstract global decisions: when the main result becomes readable, when its proof becomes executable, how technical pressure concentrates, how front matter compresses the closed proof body, when an appendix is genuinely modular, and when the paper has mathematically ended.

The paper must not inherit or numerically fit the source corpus's chapter/section count, major-unit masses, Introduction/body ratio, appendix count, appendix size, theorem-density profile, or whole-work role sequence. For textbook/monograph corpora, perform an explicit research-article projection before using whole-work evidence.

Required principles:
- expose the main result as early as it can be stated accurately and readably;
- distinguish theorem statement exposure from proof activation and proof closure;
- let technical mass concentrate where the target proof graph is difficult;
- compress the Introduction semantically rather than by a source-derived ratio;
- keep mechanism-bearing novelty and central equality/rigidity in the reader-facing body;
- require every appendix to pass a modularity test;
- do not require a Conclusion section when the mathematics has already ended;
- permit strong global asymmetry when it is mathematically explained.

### C0.13 — Direct composition is the default

When the user supplies a proof, manuscript, note, or partial argument for reconstruction, the default workflow is deliberately simple:

1. read and extract the mathematics;
2. infer the proof dependencies and choose a clean writing order;
3. present a concise writing-order plan when useful;
4. begin drafting the proof body immediately;
5. only after the proof body is stable, write theorem framing, Introduction, and Abstract;
6. finish with style and notation audits; run correctness/referee audits only when explicitly requested.

Do **not** expose or require a Research Director, `ExecutionPlan`, gate registry, behavioral-regression harness, or package-governance machinery during an ordinary manuscript-writing request. Those mechanisms are reserved for skill development, release validation, explicit audit/recovery requests, or unusually complex multi-artifact projects.

The default interaction should feel like a mathematician receiving a proof, deciding how best to tell it, and then writing it.

### C0.14 — Internal repair routing for explicit audits

When an explicit audit, recovery, or release-validation task is requested, a blocker is actionable state, not a terminal label. Use `registry/gates.yaml` and `protocols/16_gate_repair_routing.md` to identify the owning layer, rollback point, admissible repairs, invalidated artifacts, and required re-audits.

Ordinary writing requests do not need to expose this machinery. Never repair a semantic defect at the prose layer, and never preserve downstream prose whose authoritative upstream mathematics has changed.

### C0.15 — Author-corpus learning is supplementary, attributed cautiously, and non-imitative

The skill never solicits an author or asks the user to select a language style. A supplementary author corpus may be studied only when the user has already supplied a named exemplar or reference. Otherwise use Protocol 05p and continue without optional style research. This removes the historical one-time question while retaining legal acquisition and attribution safeguards whenever an author corpus is voluntarily provided.

When an author is named:
- resolve identity before downloading, using field, affiliation, ORCID, homepage, coauthors, and publication metadata as needed;
- use legally accessible author manuscripts, arXiv versions, institutional repositories, or open journal copies; never circumvent access controls;
- select a small, balanced corpus by topic relevance, author-identified or field-recognized centrality, recency, and coauthor diversity rather than citation count or venue prestige alone;
- prefer author-prepared versions for style analysis because publisher copyediting can obscure authorial decisions;
- describe patterns from coauthored papers as **author-associated corpus evidence**, not proof that one individual wrote the passage;
- promote a habit only when it recurs across multiple papers and, where possible, more than one coauthor configuration;
- store only abstract traits, evidence locators, metadata, and hashes; never source sentences, distinctive phrases, or paragraph templates.

Protocol 05p is authoritative for style conflicts: mathematical fidelity and protected scope → explicit output-language/journal requirements and accepted local-polish baseline → field conventions and reader clarity → one unified editorial voice → compatible author-corpus evidence → cosmetics. Never request style alternatives. The corpus may refine Introduction realization, theorem cadence, literature grouping, proof-outline resolution, equation/prose interaction, transitions, and paragraph pressure. It may not alter theorem scope, manufacture novelty, inject citations automatically, or make effective prose resemble an identifiable author more closely than the mathematics warrants.

### C0.16 — Reader-first Introduction; Grand Introduction is optional mathematics-positioning

Grand Introduction is mathematics-positioning, not rhetorical inflation. In v1.36 it is also conditional rather than the ordinary composition engine.

After theorem framing, ordinary Introduction composition is governed by `protocols/04_introduction_abstract.md`. Build a compact `IntroductionCoreBrief` containing the exact question, benchmark, pre-paper frontier, main theorem, nonroutine obstruction, conceptual hinge, meaning, limits, and essential literature claims. For PDE papers, conditionally add the compact PDE extension from Protocol 04t; populate only fields that change theorem interpretation. This brief, not a stack of narrative ledgers, controls the prose.

The Introduction must make a small set of reader inferences possible:

- what the exact problem is;
- what was known and exactly what remained open;
- what the paper proves at its strongest verified scope;
- why the result is not routine;
- which idea changes the problem;
- what the theorem changes in the surrounding mathematics.

Required principles:
- choose one narrative arc from the theorem and reader burden rather than forcing macro–micro–macro geometry;
- expose the main theorem as soon as it is accurate and readable—page 2 is natural when benchmark, restriction, frontier, and minimal notation genuinely require it;
- organize literature by mathematical claim and exact frontier, not bibliography order;
- state a natural route's failure only when the proof or literature supports a concrete obstruction;
- let paragraphs integrate several functions when they perform one coherent information change;
- explain the conceptual bottleneck while compressing proof-local bookkeeping;
- use the swap test: a substantial paragraph that would fit many unrelated papers after noun substitution is too generic;
- do not add history, parent-program language, adjacent problems, theorem ladders, or re-expansion merely to increase scale.

The labels `STANDARD`, `EXPANSIVE`, `GRAND`, and exceptional `GRAND_PLUS` remain available for optional editorial positioning, but they do not determine the default composition route. The phrase “Grand Introduction” denotes an earned option, not the engine's baseline.

### C0.16a — The larger mathematical story is earned, not mandatory

Apply `protocols/04n_mathematical_story_discovery.md` and `protocols/04o_mathematical_story_integration.md`, and build `MathematicalStoryLedger` only when the theorem's meaning genuinely depends on a specific parent program or nontrivial transition such as continuum→finite complexity, local→global, qualitative→quantitative, or asymptotic→exact. A broad field name is not a story.

When triggered, select one critical story path and integrate it into the theorem narrative. No dedicated program-opening paragraph or post-theorem “return” paragraph is mandatory. The story must improve at least one of: problem legibility, frontier precision, theorem interpretation, or proof-mechanism understanding. `MATHEMATICAL-STORY-INTEGRITY` remains a conditional release blocker for Introductions that deliberately claim program-level positioning.

### C0.16b — Reformulation significance and outline comprehension

A central change of viewpoint must be explained through its original meaning, exact or approximate bridge, new capability, and remaining proof cost. An encoding alone does not explain its contribution.

For a nonroutine route, apply `protocols/04p_reformulation_and_proof_explanation.md` and `protocols/04q_outline_cold_read.md` only when the compact proof overview in Protocol 04 is insufficient. Open the conceptual bottleneck; do not reproduce every technical dependency, frequency regime, cutoff, denominator, or case label merely to demonstrate completeness.

### C0.17 — Theorem statements are reconstructed after proof closure

Formal theorem packaging is a reader-facing architecture decision, not a source-preservation task. Before `ProofCoreGate`, use semantic working claims only. After the proof core closes, build `TheoremStatementLedger` from the locked mathematics and the proof actually written.

Required principles:
- theorem grouping follows mathematical role, hypotheses, and reader benefit rather than source numbering;
- substantive hypotheses, parameter ranges, normalizations, endpoint exclusions, and exceptional cases remain exact;
- proof-only assumptions are not promoted into the theorem merely because one argument used them;
- qualitative/global conclusions should remain readable even when quantitative strengthenings require heavier notation;
- equality, rigidity, uniqueness, and classification are stated at exactly the strength proved and modulo the correct equivalence relation;
- theorem order in the paper follows reader significance, not discovery or proof chronology;
- theorem subtitles are optional and must earn their navigational value.

A theorem statement may be cleaner than any source statement, but never mathematically stronger. `THEOREM-STATEMENT-INTEGRITY` is release-blocking whenever reader-facing theorem packaging is produced.

### C0.18 — Notation is architecture, not final polish

For proof-producing tasks, build `NotationLedger` from the locked mathematics and `ProofGraph` before `ProofCore` prose. Fix canonical symbols, normalizations, index families, operator/measure conventions, local/global pairs, and constant families before long-form drafting.

Required principles:
- recurring canonical symbols are globally unique across distinct recurring objects;
- local dummy variables are excluded from the duplicate-symbol audit;
- local/global and normalized/unnormalized objects are visibly distinguishable when both occur;
- indices are assigned by mathematical role rather than chronology;
- generic constants are distinguished from structural/sharp constants;
- dependence needed for uniformity is never hidden;
- source notation has no privileged status when it causes translation debt or collision;
- proof-only notation should not contaminate the main theorem;
- final LaTeX normalization audits the architecture but does not silently redesign it.

If a structural notation problem is discovered late, roll back to `NOTATION_ARCHITECTURE` and invalidate dependent theorem/proof/front-matter artifacts.

### C0.18a — Duplicate-symbol audit and plain mathematical typography

Apply `protocols/02f_duplicate_symbol_audit.md` and `protocols/02e_symbol_reservation_and_plain_typography.md` as hard defaults, independent of style corpora. The symbol rule is deliberately simple: every recurring symbol recorded in `NotationLedger.canonical_objects` must identify only one recurring mathematical object across the manuscript. No symbol is reserved in advance. Local dummy variables are excluded from this audit.

The default alphabet is plain Roman/Greek with semantic subscripts. `\mathscr` and `\mathfrak` are forbidden by default; `\mathcal` is restrained to genuine named sets, classes, spaces, or an established field convention; `\mathbb` is restricted to standard canonical objects; boldface is semantic only. Never distinguish two mathematical objects only by changing font. Source notation and style references do not override duplicate-symbol integrity or explicit user conventions.


### C0.18c — Active field-native symbol selection (v1.41)

Apply [Protocol 02h](protocols/02h_semantic_notation_selection.md) within Pass 5a, **before** the standard collision and typography audits. The main design decision is which actual symbol best communicates a mathematical object, not merely whether a chosen symbol conflicts with another. Prefer explicit user notation and the proof's verified semantics, strong subfield conventions, meaningful families and readable theorem/formula shapes; then original-source continuity and short unobtrusive notation, with the Gui corpus as a soft tiebreaker. No fixed symbol is globally reserved. Do not force candidates or long planning ledgers for routine local variables.

`NotationLedger.notation_selection` retains only salient decisions, optional protected symbols and import crosswalks, and a focused review. `tools/notation_choice_audit.py` detects structural mismatches but cannot judge mathematical elegance or external theorem applicability. Changes made later must recheck affected main theorem, estimates, references, and macros; local polishing respects the author's baseline.

### C0.18b — Empirical Changfeng Gui corpus notation prior

Apply `protocols/02g_changfeng_gui_notation_prior.md` as a **soft empirical notation-selection prior** after duplicate-symbol integrity, explicit user requirements, field/problem conventions, and clear collision-free notation already present in the supplied proof have been considered. The evidence inventory is `profiles/changfeng_gui_notation_corpus.yaml`; it spans coauthored papers in nonlinear PDE, conformal and geometric analysis, Beckner/GJMS inequalities, fluid equations, and spectral geometry.

Promote only habits that recur across papers and mathematical contexts. The stable corpus-level signal is a strategy, not a symbol table:
- primary objects are usually named directly with ordinary Roman/Greek letters and standard field notation;
- a generic PDE domain may remain `\Omega`, while a specialized geometric object may receive a meaningful capital initial such as `T`, `Q`, or `K` when this improves readability;
- related objects remain visibly related through a common base symbol plus mathematically meaningful indices, superscripts, hats, tildes, or symmetry labels;
- compact semantic abbreviations may replace repeated prose when their role is stable;
- after a genuine symmetry or coordinate reduction, the active coordinate and repeatedly used derived quantities may be renamed to simpler local symbols;
- notation is normally introduced near the first mathematical use rather than through a large front-loaded glossary.

The corpus typography is **mixed**. It contains semantic calligraphic sets and, in some papers, calligraphic or fraktur functionals/operators. Therefore do not attribute the user's stricter plain-typography preference to the Gui corpus. The user's house style—avoid `\mathscr`, avoid `\mathfrak` unless unavoidable in imported standard notation, and keep `\mathcal` sparse and semantic—is a separate higher-priority runtime override.

Exact letters, exact symbol sequences, and coauthor-specific choices from any individual paper are never templates. If a corpus-preferred symbol is already assigned to another recurring object, choose another clear conventional symbol or a semantic modifier. The duplicate-symbol audit always has priority.

### C0.19 — Supplied proofs are trusted by default during writing

For an ordinary writing request, treat every proof supplied by the user as mathematically correct and complete for its stated purpose. The default is `proof_correctness_mode: trusted_source`.

In this mode:
- do not independently re-prove the argument;
- do not search for gaps, counterexamples, or hidden failure modes;
- do not emit `MATHEMATICAL-CHECK` merely because a step is difficult, compressed, or unfamiliar;
- do not run adversarial-referee correctness checks unless explicitly requested;
- reconstruct the supplied proof faithfully, preserving its assumptions, branches, equalities, endpoints, and constant dependencies;
- treat source-specified external mathematical inputs as valid for proof reconstruction, while keeping bibliographic and priority verification separate.

`ProofCoreGate` in trusted mode checks **faithful coverage and semantic preservation relative to the supplied proof**, not independent mathematical validity.

Trusted mode never authorizes invention. If the source literally lacks a needed formula, page, or referenced mathematical object, mark `SOURCE-MISSING`; do not manufacture the missing content.

Switch to `proof_correctness_mode: verify_proof` only when the user explicitly asks for correctness checking, gap finding, referee simulation, stress testing, mathematical repair, or independent verification. Apply `protocols/01a_trusted_proof_mode.md`.

### C0.20 — Introduction composition follows the selected mode

For `LOCAL_POLISH`, preserve the selected Introduction and apply only demonstrated scoped repairs. For `RECONSTRUCT`, `introduction_reconstruction_mode: from_scratch` remains the default at the authorized scale, but composition follows the compact reader-first route rather than a mandatory ledger cascade. Source claims, terminology, citation candidates, and authorial priorities may inform the rebuild; reference wording and choreography do not.

The default workflow is:

`closed theorem truth + verified literature → IntroductionCoreBrief (plus conditional PDE extension when applicable) → two short candidate arcs when useful → select one arc → direct prose draft → reader contract → precise revision`.

For `RECONSTRUCT`, source Introduction sentences, paragraph order, theorem latency, citation choreography remain non-binding; for `LOCAL_POLISH`, the selected authorial baseline remains binding unless a demonstrated repair requires change.

The following are conditional rather than default: `IntroductionNarrativeLedger`, `MathematicalStoryLedger`, `NarrativeAmbitionLedger`, `ScientificContextLedger`, `IntroductionParagraphPlan`, calibrated narrative amplification, and editorial-impact review. Trigger only the module that solves a demonstrated reader, positioning, or context problem.

Required principles:
- the exact problem, pre-paper gap, theorem, obstruction, conceptual hinge, meaning, and scope must be recoverable from the Introduction alone;
- theorem orientation, formal statement, and interpretation remain functionally distinct when all three are needed;
- pre-theorem paragraphs pass an indispensability test;
- paragraph boundaries follow information change, not a one-role database schema;
- literature prose is claim-centered;
- the proof overview is causal and selective;
- the first/last-sentence spine is coherent;
- no detachable background or ceremonial ending survives;
- `INTRODUCTION-PROSE-INTEGRITY` is release-blocking whenever a substantial Introduction is produced.

### C0.21 — Strong positioning is precise, not amplified by default

A research Introduction should state the strongest defensible mathematical position of the paper. Verified terms such as `sharp`, `global`, `complete`, `first`, `resolves`, `settles`, and `closes` may and should be used at exact scope. Understatement and overstatement are both defects.

`NarrativeAmbitionLedger`, `protocols/04h_narrative_ambition.md`, and `protocols/04j_editorial_impact_gate.md` are conditional tools for verified conjecture resolutions, classifications, first global results, sharp theorems, or a demonstrated under-positioning problem. `protocols/04i_narrative_amplification.md` is not a default second pass; use it only to repair a specific evidence-backed omission. `EDITORIAL-IMPACT` remains a conditional blocker when program-level positioning is claimed.

### C0.22 — Scientific context is operative or omitted

Mathematical ambition and scientific-context depth remain independent axes when the corresponding optional modules are triggered; neither axis is a default drafting burden.

A specialist audience does not automatically suppress genuine scientific context, but the presence of a PDE does not create a scientific-context obligation. Apply `protocols/04k_scientific_context_research.md` and build `ScientificContextLedger` only when the model, mechanism, scaling, or parameter regime changes why the theorem is natural or how it should be interpreted.

Scientific context must return to the focal mathematics. Decorative one-line motivation and encyclopedic background are both failures. `protocols/04m_contextual_grandeur.md` is conditional: a routine definition-first opening is rejected only when a verified larger stake gives a clearer theorem-facing entry point.

### C0.15 — Package governance is release-only

The constitution, state machine, artifact registry, gate registry, schemas, templates, manifest, behavioral regressions, and release tests must remain mutually consistent when developing or releasing the skill package. `tools/contract_consistency.py` is a package-release blocker, not a step in ordinary manuscript writing. Human-readable regression specifications without executable coverage are not sufficient for research-grade package release status.

---

## 1. Default operating profile

Unless the user specifies otherwise:

```yaml
language: English
paper_type: research_article
field_profile: general_pure_math
reconstruction_strength: full
math_edit_permission: none
proof_detail_policy: preserve_all_operational_details
citation_policy: verify_or_flag
style: classical_analysis_proof_prose
composition_order: proof_body_first
frontmatter_gate: after_proof_core_pass
introduction_engine: reader_first_core_brief_with_conditional_pde_extension
pde_introduction_branch: conditional_when_theorem_coordinates_or_closure_interfaces_matter
pde_frontier_policy: multi_axis_partial_order_when_needed
pde_length_policy: explanatory_burden_not_venue_prestige
introduction_scale: optional_standard_expansive_grand_grand_plus
introduction_core_brief: required_for_substantial_introduction
introduction_narrative_ledger: optional_for_complex_multi_theorem_or_literature_heavy_introduction
introduction_reconstruction_mode: from_scratch
introduction_paragraph_plan: optional_when_complexity_justifies_it
introduction_existing_prose_policy: claim_and_citation_extraction_only
introduction_audience_default: specialist_research
introduction_prose_profile: reader_first_authorial_research_prose
introduction_prose_integrity_gate: required_for_substantial_introduction
problem_tension_map: required_when_natural_route_has_real_obstruction
result_hierarchy: reader_significance_not_proof_chronology
literature_landscape: role_based_verified
adjacent_problem_bridge: require_shared_structure_and_decisive_difference
proof_overview: mechanism_chain_first
proof_explanation: reader_independent_causal_outline_when_nonroutine
reformulation_priority: obstruction_dictionary_gain_and_remaining_cost
compression_guard: preserve_novel_mechanism_explanations
grand_narrative_hype: evidence_calibrated
narrative_ambition_ledger: optional_for_verified_strong_positioning
narrative_amplification: off_unless_specific_underpositioning_is_diagnosed
editorial_impact_gate: conditional_for_program_level_positioning
verified_strong_claim_policy: surface_at_strongest_defensible_scope
style_reference_mode: abstract_traits_only
style_extraction_order: before_proof_core
style_fidelity: high_abstract_trait_fidelity
paragraph_fingerprint: enabled_when_style_corpus_exists
paragraph_boundary_policy: mathematics_driven
paragraph_numeric_fit: forbidden
section_narrative_fingerprint: enabled_when_style_corpus_exists
section_boundary_policy: obligation_family_driven
section_numeric_fit: forbidden
section_role_sequence_reuse: forbidden
subsection_pattern_reuse: forbidden
whole_paper_narrative_fingerprint: enabled_when_style_corpus_exists
whole_paper_global_spine_policy: target_dependency_graph_driven
whole_paper_numeric_fit: forbidden
source_global_sequence_reuse: forbidden
source_frontmatter_ratio_reuse: forbidden
source_appendix_pattern_reuse: forbidden
appendix_modularity_test: required
conclusion_section: mathematically_optional
style_sentence_template_reuse: forbidden
latex_policy: journal_neutral_ams
source_reuse: mathematical_content_only
source_structure_reuse: forbidden
source_prose_reuse: forbidden_except_unavoidable_standard_phrases
style_source_prose_reuse: forbidden
naturalization_mode: authorial_mathematical_prose
generative_residue_policy: diagnose_review_rewrite
authorial_density_allocation: mathematics_driven
random_humanization: forbidden
cold_author_pass: required_final
execution_mode: direct_composition
writing_order_plan: concise_then_write
notation_architecture: before_proof_core
notation_ledger: required_for_nontrivial_proof_production
theorem_statement_architecture: after_proof_core_gate
theorem_statement_ledger: required_for_reader_facing_theorem_packaging
theorem_grouping_policy: reader_and_math_driven
research_director: off_unless_explicitly_requested
execution_plan: optional_for_complex_or_audit_tasks
behavioral_regression: package_release_only
gate_repair_routing: explicit_audit_or_recovery_only
contract_consistency_compiler: package_release_only
proof_correctness_mode: trusted_source
correctness_audit: off_unless_explicitly_requested
```

---

## 2. Core workflow

For full manuscript reconstruction, begin with Pass 0 and Pass 0a, then move directly into source extraction and proof drafting. Do not build or display an `ExecutionPlan` unless the user explicitly asks for orchestration, audit, recovery, or the task genuinely requires multi-artifact state management. The numbered passes describe the canonical full-manuscript pipeline; routine tasks should use the shortest faithful reconstruction path. In ordinary writing mode, assume the supplied proof is correct and do not perform an independent correctness audit. For `LOCAL_POLISH`, use Protocol 00 directly; reconstruction is not a prerequisite. For selected-region reconstruction, use that protocol's scoped route.

### Pass 0 — Task contract

Infer and record:
- task kind (writing, review, or skill development), and writing mode when applicable;
- accepted baseline, editable scope and protected regions;
- target theorem(s);
- intended audience;
- target language;
- desired proof-detail level;
- target venue if supplied;
- whether external literature may be consulted;
- proof correctness mode, defaulting to `trusted_source`;
- whether mathematical corrections are authorized, default `false`.

Do not ask questions that can be resolved from the supplied material. For any under-specified stylistic choice, adopt Protocol 05p automatically; never ask for a preferred language style or present style alternatives. Explicit output-language requirements still control.

Output internally: `TaskContract`.

### Pass 0a — Writing-order synthesis

Apply `protocols/02b_direct_writing_order.md`. Before drafting, determine the cleanest exposition order from the mathematics itself. Build only the minimal internal dependency sketch needed to answer:

- what must be defined first;
- which lemmas are genuinely prerequisites;
- which arguments belong together;
- where the main proof should begin;
- where equality, rigidity, endpoint, or classification arguments should close.

For substantial tasks, give the user a **concise writing-order plan**—usually a short ordered sequence of sections or proof movements—and then begin writing immediately. Do not stop after planning.

Use `protocols/15_adaptive_research_director.md` only when the user explicitly asks for research orchestration, resource scheduling, recovery of a complex partial project, or package-level audit.

The plan must:
- identify the workflow class and requested deliverables;
- list required, conditional, and skipped states;
- state why every skip is safe;
- declare reusable validated artifacts;
- list applicable release gates and blocker owners;
- preserve proof-first and semantic-order invariants.

For narrow tasks, do not execute the entire full-manuscript pipeline merely because it exists. For full reconstruction, the usual proof-first critical path remains active.

### Pass 1 — Source reconnaissance

Read all supplied sources and classify every component as one of:
- theorem/claim;
- definition/normalization;
- proof mechanism;
- calculation/certificate;
- external input;
- motivation/context;
- engineering artifact;
- duplicated material;
- source-missing item;
- suspected gap only in explicit `verify_proof` mode;
- obsolete branch.

Do **not** begin rewriting prose.

### Pass 2 — Mathematical invariant ledger

Build the ledger specified in `schemas/math_ledger.yaml`.

At minimum record:
- main theorem with exact quantifiers;
- hypotheses and parameter ranges;
- notation and normalizations;
- dependency graph;
- proof mechanisms;
- constants and their dependencies;
- equality/rigidity cases;
- endpoint and compactness issues;
- external inputs;
- computational inputs;
- unresolved source-availability issues; mathematical validity issues only in explicit `verify_proof` mode.

Assign stable semantic IDs such as `CLAIM-MAIN`, `LEM-COMPACTNESS`, `MECH-STEINER`, independent of source numbering. These IDs are working proof obligations, not final theorem numbering. Record the semantic objects that will require stable notation, but do not yet draft publication theorem prose.

### Pass 3 — Source quarantine checkpoint

Create a `SourceFirewallReport` containing:
- what mathematical content is retained;
- what source architecture is discarded;
- which source phrases/labels must not propagate;
- any unavoidable fixed terminology.

From this point, do not use the source as a writing template.

### Pass 3a — Optional author-corpus intake (no style prompt)

**Do not ask for an author, preferred style, genre voice or list of alternatives.** If the user has voluntarily supplied a specific author, corpus or exemplar for style analysis, use Protocol 05o within the authorized scope. Otherwise omit this stage and proceed under Protocol 05p's fixed house voice. Skip style-corpus acquisition for mechanical edits, bibliography-only tasks, translations, verification without writing and requests prohibiting browsing.

When activated, apply `protocols/05o_author_corpus_supplement.md`:
- resolve the exact scholarly identity;
- build a candidate publication inventory;
- retrieve by default four representative open-access papers, with three to six allowed according to availability;
- prefer author-prepared preprints for prose analysis;
- record exact versions, stable locators, local file paths when available, and SHA-256 hashes;
- create `AuthorCorpusDossier`;
- pass only supported abstract traits into the ordinary style ledgers.

The downloaded corpus is style evidence only. It is not automatically a literature source for the target manuscript, and no citation from it enters the paper without Protocol 07 verification.

### Pass 4 — Style-corpus distillation prepass

If a style reference was supplied by the user or acquired through the author-corpus route, apply `protocols/05a_style_distillation.md` **before the proof core is written**. When the corpus is substantial enough for role stratification, additionally apply `protocols/05m_high_intensity_corpus_distillation.md`.

Build:
- `LanguageStyleLedger`;
- `MathematicalWritingStyleLedger`;
- `ParagraphFingerprintLedger` via `protocols/05g_paragraph_fingerprint_distillation.md`;
- `SectionNarrativeFingerprintLedger` via `protocols/05i_section_narrative_fingerprint_distillation.md`;
- `WholePaperNarrativeFingerprintLedger` via `protocols/05k_whole_paper_narrative_fingerprint_distillation.md`;
- combined `StyleLedger`;
- `ConditionalStyleLedger` and high-intensity aggregate evidence report when the corpus supports stratification;
- aggregate style signature using `tools/proof_style_signature.py`, paragraph fingerprint using `tools/paragraph_fingerprint.py`, section-level evidence using `tools/section_narrative_fingerprint.py`, and whole-paper evidence using `tools/whole_paper_narrative_fingerprint.py` when useful.

Use stratified windows across different mathematical functions rather than a single passage. For large corpora, require role-conditioned strata and cross-fold stability before promoting a trait to a default. Record confidence for extracted traits. Quarantine the style corpus after extraction. Corpus statistics are evidence only; context-conditioned rules override global averages.

This is an internal analysis pass, so it does not violate proof-body-first composition: no publication prose is written here.

### Pass 5 — Proof-graph synthesis

Design the **proof body**, not the paper front matter.

From the locked mathematical ledger, build a proof graph whose nodes are mathematical obligations and whose edges record genuine logical dependence. For a nontrivial result, compare at least two proof-body organizations when more than one is viable. Select the one that minimizes:
- circular dependence;
- forward proof references;
- repeated hypotheses;
- artificial lemma fragmentation;
- notation churn;
- bookkeeping interruptions.

Output internally: `ProofGraph` and `ProofBodyBlueprint`.

### Pass 5a — Notation architecture

Apply `protocols/02d_notation_architecture.md`, **`protocols/02h_semantic_notation_selection.md`**, `protocols/02f_duplicate_symbol_audit.md`, `protocols/02e_symbol_reservation_and_plain_typography.md`, and `protocols/02g_changfeng_gui_notation_prior.md`. From `MathLedger` and `ProofGraph`, actively choose field-native, structure-revealing symbols and build `NotationLedger` before the proof body is drafted. An existing clear user-approved vocabulary is preserved when edits are scoped.

Within Pass 5a, use this lightweight order: **semantic objects and proof relations → field conventions and user-fixed constraints → plausible symbol candidates → representative-formula/readability comparison → selected symbols and limited reasons → global audits**. Review exact-theorem notation translations again after Pass 6a; do not attempt to certify theorem applicability from a string map.

Lock:
- canonical symbols for recurring objects;
- normalization conventions;
- local/global and finite/limiting pairs;
- index families by mathematical role;
- operator, measure, transform, norm, and variation conventions;
- manuscript-wide duplicate-symbol checks for all recurring canonical symbols;
- plain-symbol typography with decorative alphabets suppressed;
- the empirical v2 Changfeng Gui corpus prior for still-undecided, collision-free symbol choices, using the inventoried multi-paper evidence rather than a fixed symbol list;
- generic versus structural constant families and relevant dependencies.

Resolve symbol collisions and translation debt now. Choose symbols for the actual theorem and proof rather than from an alphabet dictionary. Record decisions in the **existing** `NotationLedger.notation_selection`, run `tools/notation_choice_audit.py --strict` for a locked full-reconstruction notation ledger, followed by existing notation audits. The checker validates declared structure, not actual mathematical fit. Do not preserve source notation merely from inertia; do not rename it without a reader-facing reason. This pass may redesign symbols but may not alter mathematical content.

### Pass 6 — Proof-core drafting

This is the **first publication-style prose written by the skill**. Apply `protocols/02a_proof_first_composition.md`, `protocols/03_proof_reconstruction.md`, and **always** apply the single voice under `protocols/05p_unified_manuscript_voice.md`; when a style corpus exists, additionally use `protocols/05b_style_realization.md` only for compatible abstract traits. If `ConditionalStyleLedger` exists, also apply `protocols/05n_conditional_style_realization.md` so routine, delicate, technical, bridge, theorem-leadin, and opening contexts receive different realization.

Draft the mathematical body from the leaves of the dependency graph through the final assembly. Use semantic placeholders such as `CLAIM-MAIN`, `CLAIM-COMPACTNESS`, or `CLAIM-RIGIDITY` until final theorem packaging is decided.

Requirements:
- preserve every necessary hypothesis;
- expose the decisive mechanism before surrounding bookkeeping when this improves readability;
- use the canonical notation fixed in `NotationLedger`, introducing each symbol in prose at first mathematical need;
- justify a non-obvious choice at the point it is made;
- state the exact obstruction when changing tools or regularity classes;
- separate genuinely different regimes/cases;
- track equality and rigidity through every sharp inequality;
- retain exact constant dependencies where relevant;
- apply the abstract style ledgers without source phrase reuse;
- choose paragraph boundaries from changes in target mathematical state, using the paragraph fingerprint only as conditional editorial policy;
- organize working proof modules by obligation families rather than inherited source sections; the final reader-facing section architecture remains gated until after `ProofCoreGate`;
- in `trusted_source` mode, do not search for or flag mathematical gaps; only surface literal `SOURCE-MISSING` material; in explicit `verify_proof` mode, flag gaps rather than hiding them.

Do not write the introduction or abstract as a motivational aid to yourself. The proof must stand on its own first.

### Pass 6a — Exact-theorem citation compression (default for editable proof bodies)

Apply [Protocol 07a](protocols/07a_exact_theorem_citation_compression.md) **after a usable proof core exists and before `ProofCoreGate`**. Make a focused, proof-graph-wide review of significant repeated obligations, not a hunt for references to every routine formula. From already cited works and targeted outside searches, identify the precise source result, including its original theorem/lemma/proposition/corollary number **in the inspected version**. Verify external assumptions, target conclusion, sharpness, uniformity, endpoints and equality before deleting any proof text. Use an exact result citation plus a short application; retain nontrivial adaptations and everything not covered. Never replace a proof on the strength of an abstract, a whole-paper citation, a guessed theorem number or an unrelated result.

For material candidates keep a concise `ProofCitationReplacementDossier` or equivalent table; a read-only structural checker is available at `tools/proof_citation_dossier_audit.py`. If none can safely be imported, retain the original proof without creating citation padding. In `LOCAL_POLISH` this is scoped to proof passages actually authorized for editing; Intro-only work does not trigger it. The later Protocol 04u search reuses verified import evidence and updates fair credit; it need not duplicate it.

### Pass 7 — ProofCoreGate

Run the proof-core gate before any front matter is drafted.

In the default `trusted_source` mode, `PASS` requires:
- every principal source proof path has been represented through its stated closure;
- no source-supplied hypothesis, branch, equality/rigidity condition, endpoint, or constant dependency has been lost;
- parameter ranges, regularity, constants, endpoint cases, and equality cases agree with the ledger;
- proof dependencies are locatable and the exposition order is coherent;
- no mathematical content absent from the source has been invented;
- no source-specific proof packaging survives merely by inertia;
- the proof prose respects the distilled style ledgers without source imitation.

This is a **fidelity/coverage gate**, not an independent proof-validity audit. A compressed or unfamiliar *original* source step is accepted as correct rather than reopened for proof discovery. Literal missing source content is `SOURCE-MISSING`. **For passages newly replaced by external results under Pass 6a,** the exact imported statement, source version and locator, hypothesis transfer and full target conclusion must have been checked; otherwise restore the original proof. This targeted external-dependency condition is not a global audit of the supplied proof.

Only in explicit `verify_proof` mode does the gate additionally require independent mathematical closure, verified external dependencies, and resolution of `MATHEMATICAL-CHECK` items.

If the gate fails in trusted mode, repair reconstruction fidelity first. Do not turn the writing task into correctness research unless the user requested verification.

### Pass 8 — Fresh manuscript architecture

Only after `ProofCoreGate: PASS`, design the final paper architecture around the completed proof body. Apply `protocols/02_reconstruction_blueprint.md`.

For nontrivial papers, construct at least two candidate architectures and select the one minimizing:
- forward references;
- duplicated hypotheses;
- theorem fragmentation;
- proof interruption;
- notation churn;
- appendix dependency;
- artificial whole-paper symmetry;
- duplicated main-result exposure;
- engineering residue.

The final article may of course place its introduction and theorem statements before the proofs. **Draft order and reading order are different.** The proof-first rule governs construction, not final typesetting order.

### Pass 8a — Whole-paper narrative realization

Apply `protocols/05l_whole_paper_narrative_fingerprint_realization.md` to the candidate architectures before fixing local section boundaries.

Record:
- the target-induced global proof spine;
- the main-result statement exposure mode;
- the proof activation mode and eventual proof-closure point;
- the qualitative technical-core shape;
- the front-matter compression policy;
- every proposed appendix with owner, role, body import, centrality, and modularity reason;
- the mathematically justified final endpoint of the paper.

Reject architectures that hide a readable main result, equalize technical mass for visual balance, duplicate theorem exposure, exile mechanism-bearing novelty to appendices, imitate source-wide proportions, or append a ceremonial conclusion after mathematical closure.

Output internally: `WholePaperNarrativeReport`.

### Pass 8b — Section-narrative realization

Apply `protocols/05j_section_narrative_fingerprint_realization.md` inside the selected whole-paper spine.

For every proposed section, record:
- its obligation family or reader-facing mathematical purpose;
- the section-scale state change that justifies its boundary;
- its opening mode;
- the theorem-latency mode (`IMMEDIATE`, `MOTIVATED`, `DEVELOPED`, or `DEFERRED`);
- whether its lemma cluster has downstream life;
- whether subsections are actually needed;
- its conceptual/technical pressure role;
- its closure mode and downstream consumer.

Reject sections created only by source inheritance, discovery chronology, length, lemma count, or visual balance. Do not force conceptual/technical alternation. Do not tune section count, length, subsection rate, or theorem distance to the style corpus.

Output internally: `SectionNarrativeReport`.

### Pass 9 — Theorem-statement and preliminaries reconstruction

Apply `protocols/02c_theorem_statement_architecture.md`. Build `TheoremStatementLedger` from the closed `MathLedger`, passed proof core, selected paper architecture, and `NotationLedger`.

Decide:
- which closed claims belong in the main theorem;
- which structural or quantitative strengthenings deserve separate theorem units;
- whether equality/rigidity/classification belongs in the main statement or a distinct result;
- the exact visible hypotheses, parameter ranges, normalization, endpoint exclusions, and exceptional cases;
- theorem order by reader significance rather than proof chronology;
- whether descriptive theorem subtitles are genuinely useful.

Do not inherit source theorem numbering or packaging. Do not hide substantive assumptions behind distant standing conventions. Do not let proof-only constants or notation obscure the main qualitative conclusion.

Finalize theorem/lemma packaging only after `THEOREM-STATEMENT-INTEGRITY` can pass. Update `SemanticChecksum` against the formal statements.

### Pass 10 — Proof-exposition refinement and style realization

Refine the already complete proof body; do not replace it with a fresh paraphrase. Apply Protocol 05p consistently, plus the relevant domain conventions and `profiles/classical_analysis_proof_prose.md`; add `protocols/05b_style_realization.md` only when a style corpus was supplied and its traits do not conflict with the unified voice. When available, `profiles/classical_analysis_conditional_style_model.md` and `protocols/05n_conditional_style_realization.md` take precedence over global style averages.

Optimize:
- mechanism visibility;
- obstruction visibility at tool changes;
- local justification;
- theorem/lemma dependency logic;
- equation/prose interaction;
- natural case and approximation transitions;
- proof granularity;
- sentence and paragraph cadence driven by mathematical load;
- paragraph boundaries whose mathematical reason can be stated;
- section boundaries whose obligation-family reason can be stated;
- theorem placement as early as prerequisites permit;
- subsection suppression when internal phases do not justify hierarchy;
- main-result exposure without duplicate restatement;
- whole-paper technical mass that follows proof pressure rather than visual balance;
- appendix modularity and body-import clarity;
- front-matter compression without proof replay;
- removal of workflow scaffolding.

A proof may be reordered only when the dependency graph permits it. Style fidelity is judged against the abstract ledger, never by matching source vocabulary. Recheck any **Pass 6a proof-by-citation replacements** after lemma/theorem packaging changes: the exact locator must remain a source theorem number (not the paper's new lemma number), and deleted equations or labels must not leave broken downstream dependencies.

### Pass 11 — Introduction reconstruction

#### Reader-First Introduction Engine

Apply [Protocol 04](protocols/04_introduction_abstract.md). In `RECONSTRUCT`, draft anew within the authorized scope; in `LOCAL_POLISH`, preserve effective authorial prose and repair only identified deficiencies.

**Pass 11a — Research-first literature and fair credit.** After theorem framing and before Introduction prose, perform [Protocol 04u](protocols/04u_literature_discovery_and_credit.md) for reconstructed Introductions: independently search related research beyond the inherited reference list, verify original claims/versions and the closest prior frontier, credit origins, direct results, competing/parallel lines and method ancestry, and record a compact `IntroductionLiteratureDossier`. Reuse exact-source evidence imported in Pass 6a: credit external theorem authors explicitly for that borrowed ingredient, while assigning the new result/method only to the genuinely remaining contribution. Do not write historical or novelty claims beyond the research actually inspected. For `LOCAL_POLISH`, honor the bounded scope and recheck only affected claims.

**Pass 11a.1 — Introduction core.** Build `IntroductionCoreBrief` from the stable theorem and verified literature: exact question, benchmark, pre-paper frontier, main theorem, nonroutine obstruction, conceptual hinge, unlocked control, meaning, limits, and essential citations. Keep each item compact. For a PDE-governed theorem, activate Protocol 04t and record only the operative equation/regime coordinates, multi-axis result delta, result architecture, assumption roles, obstruction stack, mechanism-to-control bridge, and typed scope boundaries.

**Pass 11b — Programmatic arc selection.** Apply [Protocol 04v](protocols/04v_evidence_grounded_grand_narrative.md) to every reconstructed Introduction: test whether verified mathematical ancestry supports a canonical principle → larger program → structural obstruction → exact result story. Prefer the most expansive *supported* arc for a substantial theorem, keeping fair credit integrated into the plot. If the larger connection is only ceremonial, choose `DIRECT`. For a weak, flat, or high-stakes Introduction, sketch two genuinely different six-line arcs and select the one with the clearest problem pressure, earliest intelligible theorem, and strongest paper-specific mathematical relation. Do not draft two complete Introductions and merge them.

**Pass 11c — Optional modules.** Trigger only what the core story needs:
- `MathematicalStoryLedger` and Protocols 04n/04o for a genuine parent program or scale transition;
- `ScientificContextLedger` and Protocols 04k/04l when the model or regime is operative;
- Protocols 04p/04q when the central reformulation or proof route cannot be understood compactly;
- `NarrativeAmbitionLedger`, `GRAND_PLUS`, and Protocols 04h/04j for verified program-level positioning or demonstrated underclaiming;
- `IntroductionNarrativeLedger` and `IntroductionParagraphPlan` only for unusually complex multi-theorem, literature-heavy, or long model-driven Introductions.

Do not instantiate all optional artifacts. The older Grand Introduction engine remains available as a compatibility module, not the default.

**Pass 11d — Direct prose realization.** Apply `protocols/04e_introduction_prose_realization.md` **in the single Protocol 05p voice**, without offering story-tone variants to the user. Compose through a mathematical question chain rather than converting ledger fields into sentences. A paragraph may combine history, literature, obstruction, and interpretation when they support one coherent information change. Use the swap test to remove transferable generic prose.

**Pass 11e — Theorem and proof resolution.** State the theorem as soon as it is accurately readable. Page 2 is acceptable when the preceding benchmark, restriction, frontier, and notation are indispensable. Explain the conceptual hinge and stage interfaces; compress routine estimates, denominators, cutoffs, case labels, and section bookkeeping.

**Pass 11f — Reader-contract cold read.** Apply `protocols/04f_introduction_cold_read.md`. Using only the Introduction, recover the exact problem, benchmark, prior frontier, remaining gap, theorem, obstruction, central idea, meaning, and limits. Run swap, detachability, theorem-latency, proof-resolution, and voice tests. Repair the earliest missing inference.

**Pass 11g — Integrity.** Run `protocols/04g_introduction_prose_integrity.md`. Run `GRAND-NARRATIVE-INTEGRITY`, `MATHEMATICAL-STORY-INTEGRITY`, or `EDITORIAL-IMPACT` only when the corresponding optional positioning module was deliberately triggered.

Do not tune Introduction length, theorem position, paragraph count, literature density, sentence length, or narrative sequence to a reference paper. **Investigate the larger mathematical story by default, but include it only when verification establishes a useful causal connection.** Do not improve weak prose by adding unattached history, and do not cap relevant credit merely for a sparse citation count.

### Pass 12 — Abstract reconstruction

Write the abstract from the stable result and mechanism using [Protocol 04s](protocols/04s_abstract_calibration.md). Select the necessary reader inferences rather than allocating a fixed number of sentences to background, theorem and method. A direct result may come first; a genuine obstruction or an exact equality case may need more space than generic context. No claim may exceed the supplied proof. In local polishing, preserve an effective abstract unless an identified deficiency justifies a change.

### Pass 13 — Editorial pass

Only now edit globally at paragraph and sentence level, and only within authorized editable scope. Apply `protocols/05_editorial_style.md`, the **whole-manuscript Protocol 05p voice audit**, and re-run `protocols/05b_style_realization.md` as a subordinate drift check when a style corpus was supplied. If high-intensity distillation was used, re-run `protocols/05n_conditional_style_realization.md` to detect flattening of role-conditioned pressure.

Optimize:
- mathematical density;
- local coherence;
- referent clarity;
- verb strength;
- transition economy;
- sentence-length variation driven by logic;
- removal of repeated meta-language.

Do not literary-ize technical mathematics. Run `checklists/unified_language_style.md` as a final cross-section cold read; select a single best formulation when tone/style guidance conflicts, without requesting user style choices.

### Pass 14 — Generative-residue diagnosis

Apply `protocols/05c_generative_residue_diagnosis.md` and the compatibility checklist in `protocols/06_anti_formulaic_style.md`.

Diagnose, rather than blindly rewrite:
- recurrent proof openings and closures;
- empty signposting;
- formula paraphrase;
- template proof geometry;
- flat information density;
- generic importance inflation;
- administrative first-person narration;
- repeated local transition tics.

Use `tools/phrase_recurrence_audit.py`, `tools/prose_rhythm_audit.py`, `tools/equation_prose_redundancy.py`, and `tools/transition_density.py` when useful. Their statistics are review signals, never generation targets.

### Pass 15 — Authorial-decision pass

Apply `protocols/05d_authorial_decision_pass.md`. Classify proof paragraphs as `ROUTINE`, `STRUCTURAL`, `DELICATE`, `SURPRISING`, `BRIDGE`, or `CLOSURE`, and allocate prose density accordingly.

The explicitness policy is asymmetric:
- `MUST_EXPLICIT`: nontrivial legality, uniformity, topology, parameter balancing, compactness, endpoints, equality/rigidity, external-theorem conditions;
- `MAY_BE_IMPLICIT`: one-step algebra, direct substitution, identical symmetric arguments when conditions do not change;
- `SHOULD_BE_IMPLICIT`: display paraphrase, elementary arithmetic, redundant reminders, empty reassurance.

Record material decisions in `AuthorialDecisionReport`.

### Pass 16 — Paragraph-fingerprint realization

Apply `protocols/05h_paragraph_fingerprint_realization.md`. Re-evaluate paragraph boundaries after the authorial-decision pass. A retained break must correspond to a mathematical state change; adjacent routine paragraphs doing the same job should be merged unless a display or genuine cognitive boundary intervenes.

Use `tools/paragraph_fingerprint_audit.py` as a diagnostic when useful. Never tune paragraph lengths, variances, or role proportions toward the source corpus.

### Pass 17 — Mathematical-transition pass

Apply `protocols/05e_mathematical_transition_pass.md`. Replace editorial continuity with mathematical continuity. Classify transitions by relation—cause, reduction, normalization, regime change, approximation, limit passage, contradiction, rigidity, assembly, or return from an auxiliary result.

Never fix recurrence by rotating synonyms.

### Pass 18 — Cold-author compression

Apply `protocols/05f_cold_author_compression.md`. This is a deletion-oriented pass with a frozen `MathLedger` and semantic checksum. Allowed operations are `DELETE`, `MERGE`, `COMPRESS`, and dependency-safe `MOVE`.

Delete redundant background and empty narration before logic. Preserve explanations of new objects, reformulation gains, operational formula meanings, and proof-stage dependencies alongside delicate justifications, generality bridges, uniformity, and equality propagation. Recheck outline comprehension after substantive compression.

### Pass 19 — LaTeX and final notation audit

Apply `protocols/09_latex_and_notation.md`. Audit the earlier `NotationLedger` against the final theorem statements and proof body, then check theorem environments, labels/references, equation numbering, macros, delimiter sizing, display punctuation, packages, appendices, and bibliography calls.

A local typography issue may be repaired here. Recheck Protocol 02h's selected symbols, representative identities, first-use definitions, optional external theorem symbol crosswalks and protected-scope decisions. A duplicate recurring symbol, decorative-alphabet violation, normalization conflict, local/global ambiguity, overloaded index family, font-only semantic distinction, or theorem/proof notation mismatch must roll back to `NOTATION_ARCHITECTURE`. Do not cosmetically rewrite mathematics in ways that alter semantics.

### Pass 20 — Source/style-independence audit

Apply `protocols/10_source_independence_audit.md` to both mathematical sources and style corpora.

The final paper must pass:

**Structural independence:** it is not a cosmetic permutation of any source manuscript.

**Prose independence:** it does not reproduce substantial source/style prose except unavoidable fixed mathematical language.

**Style abstraction:** a supplied style corpus influenced sentence-level and proof-level *decisions only through the abstract ledgers*; no source sentence or paragraph template was reused.

**Style-ledger fidelity:** the manuscript retains supported cadence, local-justification, obstacle-transition, theorem/lemma, and closure behaviors after research compression.

**Paragraph-fingerprint fidelity:** paragraph boundaries and role-sensitive density follow target mathematical state changes; no exact source paragraph sequence or numerical fingerprint is reproduced.

**Section-narrative fidelity:** section boundaries follow target obligation families; theorem latency follows prerequisite burden; subsections correspond to stable internal phases; no source section order, role sequence, subsection pattern, or numerical section fingerprint is reproduced.

**Whole-paper narrative fidelity:** the global spine follows the target proof graph; the main result is exposed as early as readability permits; technical mass follows actual proof pressure; front matter is a compressed projection of the closed body; appendices pass the modularity test; no source-wide sequence, mass profile, front-matter ratio, or appendix pattern is reproduced.

High phrase overlap triggers manual review; formulas, theorem names, standard terminology, and bibliographic titles are excluded from the judgment.

### Pass 21 — Adversarial referee simulation (explicit audit only)

Skip this pass during ordinary `trusted_source` writing. Run it only when the user explicitly requests correctness/referee/submission auditing or independent verification. In that audit mode, read the reconstructed manuscript as a skeptical specialist who has never seen the source project. Ask:
- Is the main theorem unambiguous, readable, and packaged at the right level of strength?
- Are qualitative, quantitative, and rigidity/classification results split or merged for a mathematical reason?
- Can every assumption be located, and has any proof-only assumption leaked into the theorem statement?
- Does notation remain stable from theorem statement through proof, with local/global and normalization distinctions visible?
- Can the proof be followed without engineering history?
- Are nontrivial “standard” steps actually justified or cited?
- Are equality cases complete?
- Are constants uniform where claimed?
- Are appendix dependencies transparent and genuinely modular?
- Is central novelty or equality/rigidity unnecessarily exiled to an appendix?
- Is the main theorem exposed early enough for a reader to know the destination?
- Is technical mass distributed by proof pressure rather than visual symmetry?
- Is any result claimed before it is established?
- Does the introduction accurately describe the completed proof?

Produce `RefereeAudit` with severity `BLOCKER`, `MAJOR`, `MINOR`, `STYLE`.

### Pass 22 — Submission gate

The manuscript is ready only if all blocker classes pass:
- `MATH-SEMANTICS`;
- `PROOF-CORE-ORDER`;
- `SOURCE-INDEPENDENCE`;
- `STYLE-SOURCE-INDEPENDENCE`;
- `STYLE-LEDGER-FIDELITY`;
- `CONDITIONAL-STYLE-FIDELITY` when high-intensity conditional style distillation is used;
- `GENERATIVE-RESIDUE`;
- `AUTHORIAL-DECISION`;
- `PARAGRAPH-FINGERPRINT-FIDELITY`;
- `SECTION-NARRATIVE-FIDELITY`;
- `WHOLE-PAPER-NARRATIVE-FIDELITY`;
- `GRAND-NARRATIVE-INTEGRITY`;
- `MATHEMATICAL-STORY-INTEGRITY` for `EXPANSIVE`, `GRAND`, or `GRAND_PLUS` Introductions;
- `INTRODUCTION-PROSE-INTEGRITY`;
- `EDITORIAL-IMPACT`;
- `THEOREM-STATEMENT-INTEGRITY`;
- `MATHEMATICAL-TRANSITIONS`;
- `COLD-AUTHOR`;
- `CITATION-INTEGRITY`;
- `NOTATION-CONSISTENCY`;
- `PROOF-CLOSURE`;
- `LATEX-INTEGRITY`.

If a blocker remains, route it through `protocols/16_gate_repair_routing.md` and `registry/gates.yaml`. Roll back to the owning layer, invalidate dependent artifacts, repair there, and re-audit the registered dependent gates. If the blocker cannot be repaired under the current mathematical permissions, say so. Do not label the paper submission-ready.

---

## 3. Editing permission matrix

| Operation | Default | Notes |
|---|---:|---|
| Rebuild section architecture | REQUIRED | Core behavior |
| Rename/repackage lemmas | REQUIRED when useful | Semantic IDs replace source numbering |
| Reorder independent proof components | Allowed | Dependency graph must permit |
| Compress repetitive algebra | Allowed | Only if no operative detail is lost |
| Rewrite theorem prose | Allowed | Exact semantics must remain |
| Change theorem mathematics | Forbidden | Needs explicit authorization |
| Independently search for proof gaps | OFF by default | Enable only in explicit `verify_proof` mode |
| Fill source-missing mathematics | Forbidden | Do not invent absent formulas or arguments |
| Invent citations | Forbidden | Always |
| Preserve source structure | Forbidden | This skill has no such mode |
| Copy source prose | Forbidden | Except unavoidable fixed language |

---

## 4. Mathematical semantic checksum

For every principal theorem create a before/after checksum containing:

```yaml
quantifiers:
hypotheses:
parameter_ranges:
normalization:
conclusion:
equality_cases:
constant_dependencies:
regularity:
domain_and_dimension:
external_inputs:
```

The reconstructed theorem passes only if the checksum is semantically identical, unless mathematical changes were explicitly authorized and documented.

---

## 5. Proof-detail policy

Three output detail levels are supported, but all use fresh reconstruction.

### `full`
Preserve every mathematically operative derivation, including technical estimates, endpoint arguments, and equality propagation.

### `journal`
Preserve rigorous closure while compressing routine algebra and moving genuine technical bulk to appendices.

### `compressed`
Use only when the user permits significant shortening. Never omit a nonstandard argument essential to correctness.

Default: `full` when the supplied source appears to contain a complete proof or the user asks to keep details.

---

## 6. Domain profiles

Load the closest profile from `profiles/`.

Profiles affect exposition priorities, not mathematical truth.

Available domain profiles:
- `general_pure_math.md`
- `analysis_pde.md` — including the conditional PDE Introduction route in `protocols/04t_pde_introduction_branch.md` and `profiles/pde_introduction_archetypes.md`
- `geometric_analysis.md`
- `spectral_variational.md`
- `probability_combinatorics.md`

Default proof-prose profiles:
- `classical_analysis_proof_prose.md` — base abstract proof style;
- `classical_analysis_conditional_style_model.md` — high-intensity role-conditioned microstyle when the large Markdown corpus is supplied.

When the supplied reference corpus is the classical-analysis style corpus used for this skill, the global architecture may additionally consult:
- `classical_analysis_paragraph_fingerprint.md`;
- `classical_analysis_section_fingerprint.md`;
- `classical_analysis_whole_paper_fingerprint.md`.

Grand Introduction profiles:
- `grand_mathematical_story_archetypes.md` — parent-program discovery, scale-transition archetypes, and program-level theorem interpretation.

- `scientific_context_introduction.md` — scientific/physical model research and prose integration when context is operative.
- `grand_mathematical_introduction.md` — narrative scale and positioning;
- `literature_first_grand_introduction.md` — research-first fair credit and source-grounded programmatic narrative;
- `grand_introduction_authorial_prose.md` — paragraph/sentence realization for research Introductions.

Reference-specific narrative distillation evidence may be stored in `grand_introduction_reference_distillation_report.md` and `grand_introduction_reference_distillation_report_v2.md`; these are abstract evidence reports, never prose templates. High-intensity Markdown evidence may additionally be stored in `classical_analysis_high_intensity_distillation_report.md` and `classical_analysis_conditional_style_model.signature.json`. For Introductions, the large Markdown corpus supplies microstyle only; research-scale narrative and editorial positioning remain controlled by the research-article Introduction reference and verified literature.

All are abstract research-writing profiles. None is an author imitation preset or a numerical layout template.

---

## 7. Required research artifacts

For substantial reconstruction, maintain applicable internal artifacts according to `registry/artifacts.yaml`. Local polishing needs the baseline, scoped change rationale and relevant fidelity checks, not the full artifact inventory. The registry is authoritative; this list is the reader-facing summary.

Ordinary direct-composition mode does **not** require Research Director artifacts. `ResearchDirectorBrief`, `ResearchDirectorAdvice`, and `ExecutionPlan` are optional governance artifacts used only for explicit orchestration, recovery, audit, or package-development tasks.

1. `TaskContract`
2. `WritingOrder`
3. `MathLedger`
4. `DependencyGraph`
5. `ProofGraph`
6. `ProofBodyBlueprint`
7. `NotationLedger` (including active field-native `notation_selection`) before nontrivial proof-core drafting
8. `SourceFirewallReport`
9. `AuthorCorpusDossier` when the user activates the author-corpus supplement
10. `LanguageStyleLedger` when a style corpus is supplied or acquired
11. `MathematicalWritingStyleLedger` when a style corpus is supplied or acquired
12. `ConditionalStyleLedger` when a substantial style corpus supports high-intensity stratification
13. `HighIntensityStyleEvidenceReport` when high-intensity distillation is run
14. `ParagraphFingerprintLedger` when a style corpus is supplied or acquired
15. `SectionNarrativeFingerprintLedger` when a style corpus is supplied or acquired
16. `WholePaperNarrativeFingerprintLedger` when a style corpus is supplied or acquired
17. combined `StyleLedger` when a style corpus is supplied or acquired
18. `ParagraphFingerprintReport` when applicable
19. `SectionNarrativeReport` for full-manuscript architecture
20. `WholePaperNarrativeReport` for full-manuscript architecture
21. `ProofCoreGateReport`
21a. `ProofCitationReplacementDossier` for substantive proof-by-citation candidates within authorized proof-editing scope (omit if there are no material candidates)
22. `TheoremStatementLedger` for reader-facing theorem packaging
23. `ReconstructionBlueprint` when reader-facing architecture is requested
24. `IntroductionLiteratureDossier` for Introduction reconstruction with scholarly research; record unavailable/offline search honestly, without claiming comprehensive discovery
24a. `IntroductionCoreBrief` for substantial Introduction composition; its optional `pde_extension` is activated only when PDE theorem coordinates materially affect readability
25. `IntroductionNarrativeLedger` only for unusually complex compatibility workflows
26. `MathematicalStoryLedger` when a genuine parent program or scale transition is triggered
27. `NarrativeAmbitionLedger` for verified program-level editorial positioning
28. `ScientificContextLedger` when scientific/physical context is operative
29. `IntroductionParagraphPlan` only when multiple theorem/literature/model threads justify it
30. `IntroductionProseAudit` / `ReaderContractAudit` after Introduction cold read
31. `EditorialImpactAudit` only after conditional editorial-positioning review
32. `SemanticChecksum`
33. `CitationLedger` when citations or external inputs are present
34. `RefereeAudit` when a referee/submission audit is requested
35. `SourceIndependenceReport` for source-based reconstruction audit
36. `GenerativeResidueReport` when naturalization is run
37. `AuthorialDecisionReport` when naturalization is run
38. `NaturalizationGateReport` when naturalization is run
39. `RepairRouteReport` after a gate failure
40. `ContractConsistencyReport` for skill release builds
41. `BehavioralValidationReport` for skill release builds
42. `SubmissionGateReport` when submission readiness is assessed

Conditional artifacts are not fabricated when the corresponding workflow state is skipped. In direct-composition mode, no explicit `ExecutionPlan` is required; omitted audit/governance artifacts are simply not created. If an explicit orchestration or audit mode is used, its plan must state unavailable artifacts clearly.

These artifacts may be hidden during normal drafting but must be available when the user asks for an audit trail.

---

## 8. Handling incomplete or incorrect source proofs — trusted default

For ordinary writing, the supplied proof is authoritative mathematical input. Treat it as correct and complete for reconstruction, even if an argument is compressed or would be difficult to verify independently. Do not diagnose gaps, counterexamples, or proof failures during composition.

In `trusted_source` mode:
1. extract the proof as supplied;
2. preserve its theorem semantics and operative details;
3. reconstruct it in a fresh exposition order;
4. treat source-stated mathematical dependencies as valid;
5. mark only literal missing source material as `SOURCE-MISSING`;
6. do not run mathematical repair.

If the user explicitly asks for correctness checking, switch to `verify_proof` mode. Then apply `protocols/01_math_integrity.md` and `protocols/01a_trusted_proof_mode.md`, mark genuine uncertainty `MATHEMATICAL-CHECK`, and keep mathematical repair separate from editorial reconstruction.

Never conceal source absence with invented mathematics.

---

## 9. Handling multiple source manuscripts

In local polishing, identify the accepted draft as the baseline and use other files as evidence; do not merge away the user's chosen text. In reconstruction, when several drafts or proof files are supplied:
- do not choose one as the base document;
- merge them at the ledger level;
- detect conflicts in statements, conventions, or proof routes;
- select the strongest justified route by mathematical criteria;
- synthesize one new architecture independent of all source architectures.

If two sources prove the same component differently, compare mechanisms and choose or combine them explicitly; do not splice prose.

---

## 10. Citation protocol

Maintain a `CitationLedger` with:
- claim supported;
- source;
- exact theorem/result if verified;
- status: `verified`, `user-supplied`, `needs-check`;
- whether the citation is background, dependency, comparison, or priority.

Never infer exact theorem numbers from memory when verification is available. Use [Protocol 07](protocols/07_citation_integrity.md) for the executable inventory and source-verification workflow, and [Protocol 07a](protocols/07a_exact_theorem_citation_compression.md) for the formal proof-body compression step. Record metadata, locator and claim-support results separately; undefined keys, unused entries and unverifiable sources have different meanings. Every removed proof obligation must have an exact, inspected source result and an explicit hypothesis-to-conclusion application; otherwise the original proof remains.

---

## 11. Output contract

A normal full-manuscript task should return:
- reconstructed manuscript source;
- compiled PDF when requested and tools permit;
- concise reconstruction notes;
- explicit unresolved mathematical/citation blockers, if any.

Do not clutter the paper with audit metadata.

When the user asks only for the manuscript, keep audit reports internal unless a blocker materially affects correctness.

---

## 12. Failure conditions

The skill fails if any of the following occurs:
- the final article follows the source section-by-section without mathematical necessity;
- source lemma numbering survives merely by inertia;
- large source prose passages are paraphrased sentence-by-sentence;
- theorem semantics drift without authorization;
- theorem packaging hides a substantive hypothesis, changes a parameter range, or overstates equality/rigidity/classification;
- final theorem units merely preserve source grouping/numbering without mathematical reason;
- notation architecture is deferred until final polish for a nontrivial proof, causing avoidable symbol churn or collisions;
- theorem and proof use inconsistent normalizations or ambiguous local/global notation;
- a gap is rhetorically smoothed over;
- an unverified citation is stated as fact;
- internal workflow names remain in the submission manuscript;
- the abstract or introduction claims more than the body proves;
- a supplied Introduction is polished line-by-line instead of reconstructed from closed mathematics and verified literature;
- an Introduction paragraph mixes several unrelated narrative roles because ledger fields were converted directly into prose;
- literature paragraphs are organized mainly by author chronology rather than mathematical claims;
- adjacent-problem excursions do not return mathematically to the focal problem;
- specialist research front matter retains textbook-level background with no theorem-facing function;
- theorem orientation, formal statement, and interpretation collapse into repetitive paraphrase;
- repeated administrative paragraph openings survive where mathematical subjects could carry the prose;
- a detachable literature/background paragraph survives the Introduction cold-read test;
- a verified central contribution is euphemized into vague `progress` language despite a stronger defensible description;
- a GRAND or GRAND_PLUS Introduction fails to expose the exact pre-paper frontier, theorem strength, or mathematical consequence;
- an EXPANSIVE/GRAND/GRAND_PLUS Introduction remains at the scale of the local conjecture even though a verified parent mathematical program and nontrivial scale transition are available;
- the Introduction uses generic field-level grandeur instead of a specific parent program, canonical principle, or structural transition;
- asymptotic/limiting convergence is presented as if it explained exact finite-parameter rigidity without naming the missing gap;
- scientific context becomes the entire story and the theorem's mathematical ancestry disappears;
- scientifically operative context is suppressed merely because the audience is specialist;
- a model-based paper uses decorative one-line physics or unstructured encyclopedic background instead of a verified model-to-mathematics bridge;
- a GRAND/GRAND_PLUS paper begins from routine definitions when a larger verified historical/scientific/structural stake should organize the opening;
- narrative amplification exceeds a recorded factuality ceiling;
- prestige adjectives are added where no concrete mathematical relation supports them;
- final-form front matter is drafted before the proof core closes;
- a style reference is used as a sentence/paragraph template rather than distilled into abstract traits;
- a large style corpus is reduced to unsupported traits inferred from one passage;
- a substantial style corpus is collapsed to one global average instead of role-conditioned strata;
- a tentative or holdout-unstable style feature is promoted to a hard realization rule;
- source medians, variances, or role frequencies are optimized as prose-generation targets;
- Introduction macro narrative is inferred from textbook Markdown rather than the research-article narrative reference and verified literature;
- proof prose is drafted before the requested style corpus has been abstractly distilled and quarantined;
- the manuscript avoids copying but drifts into generic prose that no longer matches supported style-ledger decisions;
- random synonymization, deliberate errors, fake uncertainty, or other cosmetic humanization is used;
- repeated proof geometry or empty signposting survives without mathematical justification;
- routine and delicate proof passages are flattened to the same explanatory density by editorial habit;
- paragraph boundaries are inserted or removed to imitate source lengths rather than changes in mathematical state;
- an exact source paragraph-role sequence is reused as a proof template;
- post-display prose systematically restates formulas rather than giving consequences or legality;
- an explicit orchestration/audit task violates an admissible `ExecutionPlan`;
- an explicit orchestration/audit plan silently skips required states or evidence;
- a failed blocker is repaired at a downstream prose layer rather than its registered owner;
- a gate is declared PASS without re-auditing dependencies invalidated by its repair;
- a legacy regression specification exists without executable behavioral coverage;
- package release proceeds despite contract-consistency failure;
- “submission-ready” is declared with unresolved blockers.

---

## 13. Decision rule for difficult cases

When editorial elegance conflicts with mathematical traceability, prefer mathematical traceability.

When source fidelity conflicts with fresh reconstruction, preserve mathematical content but discard source packaging.

When brevity conflicts with proof closure, prefer proof closure.

When front-matter elegance conflicts with what the proof actually establishes, let the proof determine the front matter.

When theorem compactness conflicts with visible hypotheses or exact rigidity, preserve theorem correctness and split the result if needed.

When source notation conflicts with a coherent target notation architecture, keep the mathematics and replace the source symbols.

When stylistic resemblance conflicts with prose independence, preserve only abstract stylistic traits.

When language-style traits conflict with mathematical-writing traits, preserve the proof logic and local auditability first; sentence cadence is subordinate to mathematical exposition.

When natural-looking variation conflicts with mathematical function, reject the variation. Irregularity is valid only when explained by mathematical load.

When recurrence can be removed either by synonym substitution or by making the mathematical relation explicit, choose the mathematical relation.

When paragraph regularity conflicts with the target proof graph, follow the proof graph. Source paragraph statistics are descriptive evidence only.

When compression conflicts with a delicate justification or an indispensable explanation of a new mechanism, preserve that explanation and delete redundant background elsewhere.

When a plausible sentence conflicts with verified scholarship, prefer verification or flagging.

When full-pipeline completeness conflicts with task relevance, execute the minimal admissible critical path and record every skip.

When a gate fails, repair at the earliest owning layer rather than the most convenient visible location.

When a downstream artifact conflicts with an updated upstream ledger, invalidate and reconstruct the downstream artifact; do not preserve it because the prose is polished.

---

## 14. Completion definition

A reconstruction is complete only when a specialist can read the final article without knowing the source draft and reasonably perceive it as a coherent paper designed around the mathematics itself rather than around the history of how the proof was assembled. Operationally, completion requires that the requested writing task has been carried through to the requested deliverable, the mathematical claims remain faithful to the trusted proof source, and no final prose is stale relative to authoritative upstream mathematics. Ordinary completion does not imply an independent correctness audit unless one was explicitly requested. An admissible `ExecutionPlan` is required only in explicit orchestration/audit modes.
