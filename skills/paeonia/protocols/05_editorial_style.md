# Protocol 05 — Mathematical Editorial Style

## Paragraph role

Every paragraph should have a dominant mathematical role. For final naturalization, refine the ordinary roles into the v1.3 classes defined in `05d_authorial_decision_pass.md`: `ROUTINE`, `STRUCTURAL`, `DELICATE`, `SURPRISING`, `BRIDGE`, `CLOSURE`.

If a paragraph has no mathematical role, delete or merge it.

## Sentence principles

Prefer:
- concrete mathematical subjects;
- active logical verbs: implies, yields, forces, controls, excludes, identifies;
- direct mathematical actions: choose, split, rescale, integrate, localize, absorb, pass to the limit;
- short transitions tied to mathematical purpose;
- displayed formulas when structure matters.

Avoid:
- ornamental adjectives;
- excessive meta-narration;
- repeated `we see/note/observe`;
- unexplained pronouns;
- sentence-level synonym replacement that makes standard mathematics less natural;
- equal explanatory density across routine and delicate passages.

## One house voice (Protocol 05p)

Use one consistent research-mathematics register: professional, economical when appropriate, mathematically precise, specialist-facing, and journal-neutral. Protocol 05p is authoritative for cross-section language and autonomous conflict resolution. Introduction breadth reflects an evidence-based mathematical program, **not** a separate ornate or promotional tone; proof density reflects obligation pressure, **not** a separate writing style. Do not ask for tone/style options or generate alternative style variants by default.

## Default proof-prose profile

For proof bodies, load `profiles/classical_analysis_proof_prose.md` by default. Its traits govern clarity, proof rhythm, and authorial naturalization, while source/style phrase reuse remains forbidden.

## Whole-paper authorial language control

After the unified Protocol 05p voice is fixed, apply Protocol 05q (`05q_authorial_prose_integrity.md`) to each authorized section and their interfaces. This is a mathematical precision and repetition audit, not a detector score or random “humanization.”

## Equation/prose rule

Prefer `purpose → formula → consequence`. A display should not be followed by a prose transcription of the same symbols.

## Step-label rule

Numbered steps are justified only by genuine changes of mathematical layer or regime. Continuous proofs should remain continuous.

## Naturalization rule

Do not vary language randomly. If a passage feels formulaic, diagnose whether the problem is empty signposting, recurrence, proof geometry, formula paraphrase, or flat information density. Repair the mathematical function rather than the vocabulary surface.
