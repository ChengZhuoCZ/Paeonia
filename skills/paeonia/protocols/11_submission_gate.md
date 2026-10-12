# Protocol 11 — Submission Gate

A manuscript may be called submission-ready only if every **applicable** registered release blocker passes. Applicability is declared by the `ExecutionPlan`; a gate may be omitted only when its evidence domain is genuinely outside the requested deliverable.

## Registered blocker set

The authoritative registry is `registry/gates.yaml`. For a full source-based research manuscript, the blocker set is:

- `MATH-SEMANTICS`
- `PROOF-CORE-ORDER`
- `SOURCE-INDEPENDENCE`
- `STYLE-SOURCE-INDEPENDENCE` when a style corpus is used
- `STYLE-LEDGER-FIDELITY` when a style corpus is used
- `CONDITIONAL-STYLE-FIDELITY` when high-intensity conditional style distillation is used
- `GENERATIVE-RESIDUE`
- `AUTHORIAL-DECISION`
- `PARAGRAPH-FINGERPRINT-FIDELITY`
- `SECTION-NARRATIVE-FIDELITY`
- `WHOLE-PAPER-NARRATIVE-FIDELITY`
- `GRAND-NARRATIVE-INTEGRITY` when a substantial Introduction is produced
- `MATHEMATICAL-STORY-INTEGRITY` for `EXPANSIVE`, `GRAND`, or `GRAND_PLUS` Introductions
- `INTRODUCTION-PROSE-INTEGRITY` when a substantial Introduction is produced
- `EDITORIAL-IMPACT` when a substantial Introduction is produced for serious journal positioning
- `THEOREM-STATEMENT-INTEGRITY` when reader-facing theorem packaging is produced
- `MATHEMATICAL-TRANSITIONS`
- `COLD-AUTHOR`
- `CITATION-INTEGRITY` when citations or external proof inputs are present
- `NOTATION-CONSISTENCY`
- `PROOF-CLOSURE`
- `LATEX-INTEGRITY` when LaTeX/compilation is part of the requested output

In addition:

- if an adversarial/referee audit was explicitly requested, no `BLOCKER` referee items may remain;
- title, abstract, introduction, and formal theorem statements must agree with the body;
- theorem statements must expose exactly the hypotheses, ranges, normalizations, and equality/rigidity strength proved;
- a substantial Introduction must pass the grand-narrative integrity audit: earned scale, verified literature position, real obstruction, faithful result hierarchy, and mechanism-first roadmap;
- an `EXPANSIVE`, `GRAND`, or `GRAND_PLUS` Introduction must pass mathematical-story integrity: a specific parent program, a supported structural archetype/scale transition, verified mathematical ancestry, theorem-level return to the program, and no generic grandeur;
- a substantial Introduction must also pass the prose-integrity audit: from-scratch reconstruction, paragraph-role coherence, claim-centered literature, theorem cadence, mathematical continuity, and cold-read compression;
- a substantial Introduction must pass editorial-impact calibration: the strongest verified contribution is surfaced, the exact pre-paper frontier is visible, consequence and method significance are explained at their evidence-supported strength, and every amplification respects a factuality ceiling;
- no internal engineering labels may remain in submission prose;
- bibliography metadata must be verified or flagged;
- no cosmetic humanization strategy may have been used;
- **Protocol 05p unified voice:** the editorial cold read must confirm one consistent research register across all editable sections, with any conflicting style guidance resolved internally and without an unsolicited style-selection prompt. The checklist is `checklists/unified_language_style.md`. This is an editorial review, not a machine-certified proof of literary quality.

## Evidence rule

A gate may be marked `PASS` only if its required evidence artifacts exist and are current. If the `ExecutionPlan` skipped a prerequisite state, the dependent gate is `UNAVAILABLE`, not silently `PASS`.

## Notation evidence

For full proof-producing reconstruction, `NOTATION-CONSISTENCY` includes **active semantic symbol selection** under Protocol 02h, not merely absence of duplicate letters. Require the finished `NotationLedger.notation_selection`, the structural `notation_choice_audit.py --strict` declaration check, and the existing normalization/duplicate/typography audits. Assess field conventions and representative formulas editorially; a structural checker cannot establish that a notation choice is mathematically optimal or that an imported theorem applies. Exact-theorem source/manuscript symbol maps must agree with the independently verified Protocol 07a proof coverage. For `LOCAL_POLISH`, audit only the authorized changes and preserve protected notation.

## Citation evidence

For applicable citation checks, use [Protocol 07](07_citation_integrity.md). An inventory with resolved keys is not evidence that sources, locators or claim support have been verified. Record those dimensions separately and report any unresolved dependency applicability or priority attribution. An explicitly requested reference audit can be completed with documented unresolved entries; that outcome is not a blanket `CITATION-INTEGRITY: PASS` or a submission-readiness claim. A flagged unrelated background source need not stop an authorized local edit.

For citation-based proof replacements, apply Protocol 07a: each removed argument must be covered by a **primary-text-verified, version-pinned theorem/lemma/proposition/corollary and its true number or precise unnumbered-page locator**, with checked hypothesis and conclusion mapping and no circular reliance. Preserve unmatched steps, required uniformity, rates, endpoints and equality/rigidity conclusions; unresolved candidates retain their proofs. Check downstream labels, citations and Introduction/Abstract method credit before declaring the replacement complete. Structural `ProofCitationReplacementDossier` checks do not certify external theorem applicability.

## Failure routing

On any blocker failure, use `protocols/16_gate_repair_routing.md` and the deterministic route in `registry/gates.yaml`. The repair must occur at the gate owner or earlier, stale downstream artifacts must be invalidated, and every registered dependent gate must be re-audited.

## Output status

Return exactly one status:

- `SUBMISSION_READY` — all applicable blockers pass under the declared proof-correctness mode; in `trusted_source` mode this is not an independent certification of the supplied proof;
- `CONDITIONALLY_READY` — no unresolved mathematical blocker, but explicit non-mathematical conditions remain;
- `NOT_READY` — at least one blocker remains or a required gate is unavailable.
