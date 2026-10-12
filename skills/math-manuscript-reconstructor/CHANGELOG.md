# v1.42.0 — Unified Manuscript Language Style, No Style Selection

- Introduced Protocol 05p, one journal-neutral, mathematically precise and evidence-grounded research-paper voice across Abstract, Introduction, theorems, proofs and remarks; density changes with mathematical obligations, not with selectable personas or tones.
- Removed the default v1.38 author-style selection prompt from current entry points, state sequence, README and author-corpus procedure. Author/style corpora are now considered only when proactively specified by the user; mathematical literature discovery and accurate scholarly credit remain compulsory where applicable.
- Added an explicit autonomous priority hierarchy: mathematics/protected scope > explicit requirements and submission rules > field clarity > canonical voice > optional corpus evidence > cosmetics. Any stylistic conflict is resolved to **one** manuscript version rather than presented as options.
- Kept editing-mode authorization distinct from style selection, preserving reconstruction/local-polish boundaries and accepted authorial text. The exact-citation (v1.40) and notation-selection (v1.41) mechanisms remain unchanged.
- Added a single voice profile, a cross-section audit checklist, new behavioral cases, and a v1.42 release contract. Historical "ask once" tests have been updated to assert supersession without dropping the legal-retrieval or attribution safeguards.
- This release modifies the skill package only; it does not audit an arbitrary manuscript's literary quality or perform a fresh citation verification.


# v1.41.0 — Active Semantic Notation Selection

- Added Protocol 02h for active, field-native selection of main and recurring symbols before proof-core drafting; choose by user constraints, mathematical semantics, subfield conventions, structural families, source continuity and representative-formula readability rather than arbitrary typography scores.
- Incorporated `notation_selection` decisions and optional exact-theorem symbol crosswalk in the existing NotationLedger schema/template; no competing mandatory dossier or new workflow state.
- Linked Pass 5a, state machine, Protocol 07a citation compression, and final LaTeX audit, preserving original user-selected modes and protected prose.
- Added a notation-selection checklist, read-only consistency tool and tests. The tool does not certify mathematical elegance or external theorem applicability; live manuscript output was not edited in this release.

# v1.40.0 — Exact-Theorem Citation Compression as Proof Stage

- Promoted the previously optional Protocol 07 §6 proof-citation rule to an explicit, systematic **Pass 6a** after proof-core drafting and before `ProofCoreGate`; preserved proof-first and all original writing-mode/permission boundaries.
- Added Protocol 07a with unit-level candidate discovery, full-text/version-specific theorem-number verification, two-sided hypothesis/conclusion mapping, direct/adapted/partial replacements, circularity checks, and no-padding/retain-original fallbacks.
- Added a compact optional `ProofCitationReplacementDossier` schema, a proof-import checklist, a read-only dossier-field checker and local checker tests. The checker cannot certify source content or mathematical implication.
- Connected downstream label/bibliography/Intro-credit checks to the existing citation and submission gates. Reused established metadata/locator/claim-support verification; no competing bibliography workflow created.
- Added version 1.40 regression and behavioral fixtures covering precise locators, mismatched geometric classes, parameter uniformity, rigidity, protected scope, unresolved sources and partial overlaps.
- This is a skill upgrade, not an actual proof-by-citation substitution in an identified mathematics manuscript; no specific external mathematical theorem was independently verified here.

# v1.39.0 — Literature-First Credit and Evidence-Grounded Grand Introduction

- **Changed the ordinary Introduction reconstruction order:** stable theorem truth → live outward discovery of relevant mathematical papers → verified source/claim evidence → fair credit and exact frontier map → compact `IntroductionCoreBrief` → a source-grounded programmatic story test → prose and cold read. This is an Introduction-only research step, not a repeal of proof-body-first full reconstruction.
- Added [Protocol 04u](protocols/04u_literature_discovery_and_credit.md): search beyond existing `.bib` entries by multiple independent routes, include original/benchmark/direct/partial/parallel/method sources, inspect the primary theorem or method for pivotal comparisons, distinguish metadata/claim/priority support, and disclose inaccessible/offline research. Citation quantity is role-driven, not capped.
- Added [Protocol 04v](protocols/04v_evidence_grounded_grand_narrative.md): test a genuine parent mathematical program for every reconstructed Introduction, favor a grand causal opening when earned, keep the theorem early, integrate positive credit, and return to exact field-level consequences. Reject inflated history or priority when the source-backed structural bridge is absent.
- Added one compact `IntroductionLiteratureDossier` (schema/template, registry entry), default credit/grand profile and checklist, and procedural source notes including SIAM, Oxford, MathSciNet, Crossref, OpenAlex and arXiv guidance. The dossier is a research record, not a second stack of planning ledgers.
- Integrated discovery/credit into SKILL, Protocol 04, Protocol 07, state-machine and prose-integrity checks, the Introduction core schema, reader checklist, README and release manifest. Preserved full reconstruction versus local polishing boundaries and the optional author-style corpus firewall.
- Added ten executable good/bad semantic regression fixtures (163–172) and a v1.39 contract test; updated v1.38 version-floor compatibility without weakening its substantive author-corpus assertions. Earlier optional narrative modules remain conditional.
- This is a **skill package upgrade**. No mathematical article was rewritten; no new theorem has been independently verified. The live web checks in this development turn establish procedural sources, not the actual bibliography for an as-yet-unprovided manuscript.

## 1.38.0 — Author-Corpus Writing Supplement

- Preserved the v1.36 reader-first Introduction rebuild and v1.37 conditional PDE theorem-structure branch.
- Added a one-time post-proof request for a manuscript author or user-named writing exemplar, with an explicit `skip` path.
- Added Protocol 05o for scholarly identity resolution, legal open-access acquisition, representative 3–6 paper selection, version locking, SHA-256 recording, and corpus quarantine.
- Defined a balanced default four-paper corpus using topic proximity, author-centrality evidence, recency, genre match, and sole/cross-collaboration control instead of citation count or venue prestige alone.
- Added cautious coauthor attribution: coauthored prose is author-associated corpus evidence unless cross-collaboration or sole-authored evidence supports a stronger inference.
- Separated style evidence from literature evidence; author papers never enter the target bibliography or novelty narrative without Protocol 07 verification.
- Added `AuthorCorpusDossier`, schema/template, checklist, task-contract fields, style-ledger source roles, and v1.38 regression/contract coverage.
- Kept `LOCAL_POLISH` baseline prose above the author-corpus supplement in the priority order and prohibited wholesale restyling.

# v1.37.0 — Conditional PDE Introduction Architecture

Preserve the compact reader-first route from v1.36 and add a PDE-specific extension inside `IntroductionCoreBrief`, rather than a second mandatory ledger. Distill Introduction decisions from representative Annals, Inventiones, Publications Mathématiques de l’IHÉS, and CPAM papers across Navier–Stokes nonuniqueness, obstacle-problem stratification, Allen–Cahn/minimal-surface limits, inviscid damping, critical NLS thresholds, fully nonlinear partial regularity, and critical SQG. Add multi-axis result deltas and partially ordered frontiers; separate narrative arc from theorem architecture; classify assumptions by role and proof location; allow a short causal obstruction stack; connect decisive formulas to PDE closure; distinguish theorem, method, counterexample, and open boundaries; and add conditional checks for continuation, linear-to-nonlinear closure, singular limits, nonuniqueness classes, and stratification. Add Protocol 04t, PDE archetype and reader-contract profiles, a corpus distillation report, eleven behavioral regressions, and a v1.37 contract test. A clean short PDE Introduction remains valid; length follows explanatory burden, not journal prestige. No manuscript was rewritten in this release.

# v1.36.0 — Reader-First Introduction Simplification

Replace the accumulated default Introduction stack with a compact reader-first route: `IntroductionCoreBrief → one selected arc → direct prose → seven-question reader contract`. Make mathematical-story, scientific-context, ambition, paragraph-plan, amplification, and editorial-impact modules conditional rather than cumulative defaults. Permit integrated paragraphs when several functions support one information change; govern theorem latency by indispensability rather than page number; group literature by mathematical claim; and compress proof-local bookkeeping in the overview. Add swap, detachability, latency, proof-resolution, and voice tests; a new core schema, templates, checklist, narrative-archetype profile, and five behavioral regressions. Preserve controlled program-level positioning when the mathematics earns it. No manuscript was rewritten in this release.

# v1.35.0

Add a proof-replacement route to Protocol 07, the main entry point and the citation evidence gate. Require a verified exact result and source version, a checked hypothesis-to-conclusion mapping, and readable application prose. Distinguish direct, adapted, partial and unavailable replacements. Preserve unmatched arguments, parameter uniformity, equality cases, labels and the central explanatory mechanism. The workflow applies directly within authorized proof-editing scope, without expanding read-only or protected-text tasks. No manuscript edits or new external theorem verification were performed for this instruction update.

# v1.34.0

Add a scoped reference-verification workflow to Protocol 07 and the main entry point. Separate source metadata, version-specific locators and claim support; distinguish dependencies, background, comparisons and priority claims. Add a read-only TeX/BibTeX citation inventory with explicit file coverage, nested citation support, uncited/nocite distinctions and no source-verification claims. Nine executable tests cover the new tool and are included in the release suite. Manuscript content and installed skills are not changed.

# v1.33.1

After an actual unchanged manuscript application, route whole-candidate retention to the existing Protocol 04q stopping policy. Record the checks and rejected alternatives; reuse unchanged outputs and distinguish editorial review from new generation or new compilation. The ending guidance remains consolidated rather than accumulating more case-specific instructions.

# v1.33.0

Consolidate the abstract-ending guidance accumulated over the previous two replays into a shorter general instruction. Make initial revision conditional on a demonstrated decision problem; repeating an application does not require another prose change. Preserve causal fidelity and exact theorem scope.

# v1.32.1

Following the frozen v1.32.0 trial, refine the same ending instruction: distinguish causal agents while allowing a proved characterization to summarize its technical reconstruction at abstract resolution. The paper revision retains the reference's economy and removes an unnecessary new technical name. Existing writing modes and protected scopes remain unchanged.

# v1.32.0

Refine the existing abstract-ending instruction: distinguish the hypothesis forcing an auxiliary conclusion from the rigidity or reconstruction identifying the original object; check causal subjects before compressing those operations. No new mandatory stage, phrase or sentence count is introduced.

# v1.31.1

After applying v1.31.0, compare the frozen candidate with the user abstract. Retain only two abstract clarifications, restore the reference's more economical representation/equality narration, and record the distinction between an abstract inference and an implementation detail. Add one bounded case profile; no fixed wording or sentence count is prescribed.

# v1.31.0

Replace fixed abstract sentence slots with a causal, scope-aware abstract pass. Add a bounded candidate–reference comparison route. Clarify that peripheral citations need proportionate explanation and that source existence alone does not justify placement. Preserve both writing modes and all prior editing boundaries.

# v1.30.1 — Ask for the Writing Mode First

Require an initial full-reconstruction versus local-polishing question before new writing, unless the choice is already explicit. Wait for an unanswered choice; retain prior choices during continuation. No repeated approval for scoped edits. Instruction-only patch; planner code unchanged.

# v1.30.0 — Explicit Reconstruction and Local Polishing

Separate intervention mode from editable scope. Add a baseline-preserving local path, a selected-region reconstruction path, and precedence over incompatible legacy proof-first/source-firewall defaults. Carry mode and boundaries through the optional planner; reject mode conflicts and advice that expands bounded work. Preserve legacy named workflows and their prerequisites. Add executable routing tests. No manuscript revision is part of this release.

# v1.29.0 — A Documented No-Change Replay

Apply released v1.28 and retain the v128 manuscript after evaluating and rejecting further expansions and cosmetic edits. Refine replay outcome handling to reuse unchanged artifacts and require new evidence for new general writing rules. Consolidate the same-sample case history into a compact profile table. No manuscript change, new style prescription, independent-reader result or proof certification.

# v1.28.0 — One Sentence-Level Refinement from a Second Replay

Apply released v1.27 to the preceding trial and reorganize one Ward-comparison sentence, retaining its mathematical content. The comparison identifies accumulated parenthetical burden, not missing proof material. Add a conditional whole-sentence reread to Protocol 04p and record the limited gain and preservation constraints in the case profile. No new gate, formula, vocabulary rule, or claim of independent validation.

# v1.27.0 — Evidence from a Preserved-Introduction Replay

Apply the released v1.26 skill to the accepted manuscript, freeze the actual three-fragment candidate, and compare its local gains and density cost with the preferred original. Make prose preservation operative in local editing, qualify full-reconstruction inheritance rules, check semantic comparison objects as well as formulas, and replace opaque technique labels with the needed operation. Update the positive-example profile with the user’s restoration feedback. No universal phrase, paragraph quota, new validator, or independent-reader claim.

# v1.26.0 — Learning from a Preferred Conceptual Introduction

Add a positive-example profile distinguishing the mathematical effect of the Fourier bridge from its phrasing and local editing constraints. Refine Protocols 04p, 04e, and 04q to compose the conceptual explanation before expanding technical dependencies when appropriate, group routine work, and preserve the different roles of repeated tools. No manuscript edits, new universal gate, required vocabulary, or independent behavioral validation.

# v1.25.0 — Source-Backed Revision after Referee Analysis

Extend Protocol 04r with the transition from diagnosis to authorized edits: inspect source provenance, foreground existing results with exact hypotheses, and report unresolved mathematical work separately from completed exposition. Preserve the flexible wording policy and avoid adding universal theorem or process quotas.

# v1.24.0 — Referee Perspective and Contribution Clarity

Add a scope-bound referee reading route distinguishing contribution, comprehension, and proof reproducibility. Keep a manuscript-specific case study with unresolved interface questions. Clarify full-reconstruction versus local-review scope in conflicting entrypoint rules. No new universal gate or automated prose score is introduced.

# v1.23.1 — Expressive intent without prescribed wording

Treat example phrases as expressive guidance, choose the assessment from the mathematical relation, and check repeated announcements across abstract and Introduction. Preserve supported emphasis without keyword compliance or synonym rotation.

# v1.23.0 — Explanatory Decisions and Mathematical Connections

- Reworked Protocol 04p around the reason for an editorial move: the missing inference, a source-backed mathematical witness, and a conditional choice of explanation.
- Distinguished stage coverage from explanation of the operation at the conceptual bottleneck; preserved concise black boxes for routine modules.
- Corrected tone rules to realize supported surprise, unexpected connections, and elegance when requested, without converting judgment into historical priority.
- Added structural literature search and four connection statuses, with a researched polygonal Sobolev/quadrature and auxiliary-function case study.
- Strengthened the existing cold read with text-level evidence, choice/judgment/neighbor tests, and safeguards against importing the evaluator's knowledge of the proof.
- Added conditional reasoning cases and clarified the inferred rationale behind Naber/coauthor writing moves. No new gate, required agent, or automatic prose-comprehension score.
- This release updates the skill only; the previously delivered manuscript is unchanged.

# v1.22.0 — Reformulation and Comprehensible Proof Outlines

- Distilled selected Introduction/outline windows from ten downloaded Naber/coauthored papers; added a versioned, hashed corpus inventory and a conditional explanatory profile.
- Added Protocol 04p for the original obstruction, object dictionary, bridge status, new capability, and remaining cost of a reformulation.
- Added Protocol 04q for a reader's Introduction-only comprehension check; integrated it into the existing Introduction prose gate.
- Repaired conflicting compression rules directly. Preserve meaningful formula interpretation and causal stage explanations; allow conditional assembly, model cases, and asymmetrical outline depth.
- Added optional proof-explanation records and a dependency/evidence checker which explicitly cannot certify prose comprehension or mathematical correctness.
- Added ten decision regressions and graph/evidence mutation tests. Preserved existing mathematical and notation behavior.
- Made scope explicit for skill-development, Introduction-only, and user-requested local edits. Corrected the entrypoint frontmatter to include a description and place package fields in metadata.

# v1.21.0 — Grand Mathematical Story Engine

- Added `MathematicalStoryLedger`, `protocols/04n_mathematical_story_discovery.md`, and `protocols/04o_mathematical_story_integration.md`.
- Ambitious Introductions now climb from focal theorem to focal problem, parent mathematical program, and canonical principle when supported.
- Added structural story archetypes including continuum→finite complexity, limit→exact finite, local→global, qualitative→quantitative, symmetry→rigidity, compactness→structure, critical/endpoint, and classification-program transitions.
- Added a mathematical `story_graph` with a selected `critical_story_path`, so rich background is researched internally but prose follows one theorem-relevant spine.
- Added role-based mathematical ancestry research and outward search beyond the supplied draft's bibliography for triangulated/deep story discovery.
- Added program-level theorem interpretation and proof-story requirements: the theorem must return to the parent program and the proof overview must explain the mechanism that crosses the central transition.
- Separated larger mathematical story from scientific context. Physics/model background may lead or enrich the Introduction but never substitutes for mathematical ancestry.
- Added `MATHEMATICAL-STORY-INTEGRITY` as a release blocker for `EXPANSIVE`, `GRAND`, and `GRAND_PLUS`.
- Added `tools/mathematical_story_audit.py`, schema/template/profile/checklist support, and behavioral regressions 119–128.
- Added a large-`N` polygonal Pólya–Szegő regression requiring the isoperimetric continuum→finite-complexity→exact-rigidity story rather than definition-first exposition.

# v1.20.0 — Contextual Grandeur & Scientific Background Research

- Split Introduction scale into two independent axes: mathematical ambition and scientific-context depth.
- Added `ScientificContextLedger` with depth modes `NONE`, `ORIGIN_BRIEF`, `SUBSTANTIAL`, `PHYSICS_LED`, and `INTERDISCIPLINARY_LED`.
- Removed the old tendency to suppress physical/model context merely because the intended reader is a specialist.
- Added deep scientific-context research roles: `MODEL_ORIGIN`, `MECHANISM`, `REGIME_OR_SCALING`, `MATH_BRIDGE`, with optional modern/experimental context when theorem-facing.
- Added research-breadth modes `COMPACT / TRIANGULATED / DEEP`; physics-led Introductions normally require deep, source-diverse context research rather than a single secondary-source summary.
- Added explicit model-to-mathematics mapping, parameter/scaling interpretation, and theorem-to-science wording ceilings.
- Added `protocols/04k_scientific_context_research.md`, `04l_scientific_context_integration.md`, and `04m_contextual_grandeur.md`.
- Added a physics-wallpaper rejection test: context must change problem legibility, regime naturality, theorem interpretation, historical position, or proof mechanism.
- Strengthened `GRAND/GRAND_PLUS` openings so a verified classical stake, scientific origin, or structural tension precedes routine definitions when that produces the truthful larger entry point.
- Added the continuous-optimizer → discrete-class → asymptotic-localization → exact-finite-rigidity pattern as a decision rule for finite-complexity extremal problems.
- Added scientific-context auditing and behavioral regressions 109–118, including a dry large-`N` spectral Introduction regression distilled from a real reconstruction failure.
- Preserved the no-forced-physics rule: scientific context is triggered by verified lineage, not by the mere presence of a PDE.

# v1.19.0 — Empirical Changfeng Gui Notation Prior

- Re-ran the notation distillation against an explicit multi-paper corpus rather than relying on a short qualitative summary.
- Added `profiles/changfeng_gui_notation_corpus.yaml` with arXiv IDs, evidence levels, and observed notation patterns.
- Promoted only cross-paper habits: direct primary symbols, semantic geometry initials, related-family indices/modifiers, field-standard spectral/PDE notation, local simplification after reduction, and first-need introduction.
- Added strong evidence from the triangle, symmetric quadrangle, Beckner-S4, and 2026 mean-field/Hawking full text, with supporting evidence from Sphere Covering, Liouville, Navier–Stokes, and related papers.
- Corrected the earlier overstatement that the corpus avoids decorative alphabets: the Beckner paper uses `\mathfrak L` and `\mathcal J_\alpha`, while spectral papers use semantic calligraphic sets such as `\mathcal Z(u)` and `\mathcal C_{nv}(u)`.
- Kept the user's plain-typography preference as a separate higher-priority house-style override instead of misattributing it to the author corpus.
- Strengthened generic-to-specific domain notation (`\Omega` → `T/Q/K` when useful), semantic side labels, deformation-family notation, spectral-family distinctions, and coordinate-reduction rules.
- Added v1.19 contract coverage and executable behavioral regressions 101–108.

# v1.18.0 — Changfeng Gui Corpus Notation Prior

- Added the first soft Changfeng Gui corpus notation prior for still-undecided, collision-free symbol choices.
- Kept duplicate-symbol integrity, user requirements, and field conventions at higher priority.
- Added notation-prior profile/report, advisory audit tool, and behavioral cases 93–100.
- This layer is superseded and empirically corrected by v1.19.0.

# v1.17.0 — Duplicate-Symbol Audit

- Simplified symbol discipline to exactly the user requirement: check whether one recurring visible symbol is assigned to multiple recurring mathematical objects.
- Removed any special semantic status for `\Delta` or other symbols.
- Made the duplicate check manuscript-wide for recurring canonical notation.
- Excluded local dummy variables from the duplicate-symbol table.
- Split duplicate-symbol checking from plain-typography policy.
- Added a dedicated `duplicate_symbol_audit.py` tool and regression coverage.

# v1.16.0 — Collision-Free Notation Semantics

- Corrected the v1.15 `\Delta` policy: `\Delta` is no longer universally reserved for the Laplacian.
- Replaced permanent symbol reservation with context-sensitive semantic collision detection.
- A manuscript-global symbol assignment now blocks unrelated local shadowing.
- If `\Delta` denotes a Laplacian in a manuscript, it cannot also denote a deficit/gap there; if no Laplacian meaning is active, another standard unambiguous use is allowed.
- Extended the same collision rule to all recurring symbols, not only `\Delta`.
- Retained the plain-typography policy: decorative `\mathscr`/`\mathfrak` remain disallowed by default, and font-only semantic distinctions remain forbidden.

# v1.15.0 — Symbol Discipline & Plain Mathematical Typography

- Reserved `\Delta` exclusively for the Laplace/Laplace–Beltrami operator.
- Forbid uppercase `\Delta` for deficits, increments, gaps, discriminants, or bookkeeping quantities.
- Added hard plain-typography defaults: no `\mathscr` or `\mathfrak`; `\mathcal` exceptional only; `\mathbb` standard-only; boldface semantic-only.
- Added no-font-only-distinction rule.
- Extended `NotationLedger`, notation audit, final LaTeX audit, profiles, behavioral regressions, and release contract.

# Changelog

## 1.14.0 — High-Intensity Conditional Style Distillation

- upgraded large-corpus style extraction from global summaries to role-conditioned strata;
- added `ConditionalStyleLedger` and high-intensity evidence reporting;
- added eight-fold holdout stability checks for default style traits;
- added conditional realization for routine, delicate, technical, bridge, closure, theorem-leadin, section-opening, conceptual, and Introduction contexts;
- explicitly separated Markdown microstyle from research-Introduction macro narrative;
- forbade global-average override, numerical style fitting, and unstable-trait promotion;
- added high-intensity distillation and conditional-style diagnostics plus behavioral regression coverage.

## 1.13.0

- Added `NarrativeAmbitionLedger` and calibrated Introduction scales `STANDARD / EXPANSIVE / GRAND / GRAND_PLUS`.
- Added `protocols/04h_narrative_ambition.md`, `04i_narrative_amplification.md`, and `04j_editorial_impact_gate.md`.
- Changed strong-result policy from merely anti-hype to evidence-sensitive positioning: verified `sharp`, `global`, `complete`, `first`, `resolves`, `settles`, and `closes` claims may and should be used at their exact supported scope.
- Added a factuality ceiling so narrative amplification can broaden context, sharpen contrast, clarify obstruction, strengthen consequence, and expose method afterlife without creating new facts.
- Added `EDITORIAL-IMPACT` release blocker to catch both unsupported inflation and avoidable under-positioning.
- Added specialist-editor first-two-pages read and `EditorialImpactAudit`.
- Added `calibrated_grand_narrative.md`, editorial-positioning checklist, narrative-ambition schema/template, and `introduction_editorial_impact.py`.
- Added executable behavioral regressions 66–75 for strong-claim surfacing, factuality ceilings, earned GRAND_PLUS scale, frontier positioning, theorem interpretation, method afterlife, licensed amplification, editorial visibility, and evidence-sensitive strong terminology.
- Preserved v1.12 from-scratch Introduction reconstruction, v1.11 trusted-proof writing, theorem/notation architecture, and proof-first direct composition.


## 1.12.0

- Rebuilt the Introduction subsystem as a dedicated from-scratch research-prose engine rather than a narrative-ledger-plus-polish pass.
- Added `IntroductionParagraphPlan` with one dominant paragraph role, mathematical entry/exit anchors, literature clusters, theorem function, qualitative pressure, and detachability checks.
- Added `protocols/04d_introduction_paragraph_architecture.md`, `04e_introduction_prose_realization.md`, `04f_introduction_cold_read.md`, and `04g_introduction_prose_integrity.md`.
- Added research-specialist background compression: standard PDE/spectral/function-space exposition is suppressed unless theorem-facing.
- Added claim-centered literature realization and explicit return paths for adjacent-problem excursions.
- Added theorem-cadence rules separating orientation, formal statement, and interpretation.
- Added first/last-sentence continuity and paragraph-removal cold-read tests.
- Added `INTRODUCTION-PROSE-INTEGRITY` release blocker and deterministic repair routing.
- Added `grand_introduction_authorial_prose.md` and a second abstract distillation report for the designated research Introduction reference.
- Added `introduction_prose_audit.py` and executable behavioral regressions 56–65.
- Preserved trusted-proof direct writing, theorem/notation architecture, proof-first composition, and Grand Mathematical Introduction positioning.

## 1.11.0

- Added default `proof_correctness_mode: trusted_source` for ordinary manuscript writing.
- Added `protocols/01a_trusted_proof_mode.md`.
- `ProofCoreGate` now checks source-relative proof coverage and semantic fidelity in trusted mode rather than independently re-proving the supplied argument.
- Disabled gap hunting, counterexample search, adversarial correctness checking, and mathematical repair unless the user explicitly requests `verify_proof`.
- Added `SOURCE-MISSING` for literal absent source content; trusted mode never invents missing mathematics.
- Made adversarial-referee correctness simulation explicit-audit-only.
- Added executable behavioral regression 55 and v1.11 contract tests.
- Preserved v1.10 theorem/notation architecture, v1.9 Grand Introduction, and v1.8 direct composition.

## 1.10.0

- Added `NotationLedger` and a pre-proof `NOTATION_ARCHITECTURE` state.
- Added `TheoremStatementLedger` and post-closure theorem-statement reconstruction.
- Added `protocols/02c_theorem_statement_architecture.md` and `02d_notation_architecture.md`.
- Added theorem/notation schemas, templates, checklist, and ledger audit tools.
- Added `THEOREM-STATEMENT-INTEGRITY` release blocker.
- Strengthened `NOTATION-CONSISTENCY` so structural notation failures roll back to notation architecture.
- Added executable behavioral regressions 47–54 for theorem grouping, assumptions, normalization, quantitative packaging, equality/rigidity, notation timing, symbol stability, and local/global distinction.
- Preserved v1.8 direct composition and v1.9 Grand Mathematical Introduction behavior.

## 1.9.0

- Added the Grand Mathematical Introduction Engine after proof closure and theorem framing.
- Added `IntroductionNarrativeLedger` with `STANDARD / EXPANSIVE / GRAND` scale selection.
- Added `ProblemTensionMap`, `ResultHierarchy`, role-based `LiteratureLandscape`, adjacent-problem bridges, and mechanism-first proof narrative.
- Added `GRAND-NARRATIVE-INTEGRITY` release blocker and deterministic repair routing.
- Added protocols 04a–04c, grand-introduction profile/checklist/schema/template, and a diagnostic Introduction audit tool.
- Added executable behavioral regressions 38–46 for earned scale, mathematical obstruction, theorem order, literature roles, adjacent bridges, functional result repetition, mechanism-first roadmap, and anti-hype verification.
- Preserved v1.8 direct composition: proof body is still written first; no Introduction prose appears before proof closure.


## 1.8.0

- Changed the default interaction from planner-first to direct composition.
- A supplied proof now leads directly to: mathematics extraction → writing-order synthesis → proof-body drafting.
- Research Director / ExecutionPlan are optional and reserved for explicit orchestration, recovery, audit, or package-development tasks.
- Behavioral regression and contract-consistency tools remain package-release safeguards, not manuscript-writing steps.
- Added `WRITING_ORDER` as the ordinary pre-drafting state.
- Preserved proof-first composition, source/style firewalls, semantic safeguards, authorial prose, paragraph/section/whole-paper fingerprints, and submission audits.
