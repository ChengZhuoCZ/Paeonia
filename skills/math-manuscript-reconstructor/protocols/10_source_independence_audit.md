# Protocol 10 — Source/Style Independence and Style-Ledger Fidelity Audit

## Mathematical-source structural independence

Compare source and final:
- section tree;
- order of major claims;
- lemma granularity;
- appendix boundary;
- proof-step packaging.

A near one-to-one correspondence is a warning unless logically forced by the dependency graph.

## Mathematical-source prose independence

After removing formulas, citations, labels, theorem names, and common mathematical boilerplate, inspect long phrase overlap.

Suggested heuristic:
- exact overlap of 10+ consecutive ordinary prose tokens: review;
- repeated overlap across multiple paragraphs: likely failure;
- isolated standard phrases: ignore.

## Style-corpus independence

When a style reference was supplied, audit it separately. The final manuscript may resemble the corpus in abstract properties such as pacing, proof granularity, obstacle visibility, local justification, and equation/prose balance, but it must not reproduce distinctive sentences, paragraph skeletons, examples, or author-specific verbal patterns.

Required checks:
- `LanguageStyleLedger` and `MathematicalWritingStyleLedger` contain traits, not source sentences;
- style corpus was quarantined before proof prose drafting;
- long ordinary-prose n-gram overlap is reviewed;
- step headings and transition phrases are generated from the mathematics, not copied from the corpus;
- transition-word frequencies were not mechanically imitated;
- if the corpus is pedagogical, the final research article does not inherit exercise/lecture scaffolding.

## Style-ledger fidelity

Independence alone is insufficient. A manuscript can avoid copying while drifting back to generic academic prose.

Audit whether the final text still implements the supported abstract traits, especially:
- direct or mechanism-led proof openings;
- explicit obstruction when changing tools;
- purpose/display/consequence equation rhythm;
- local legality checks;
- dependency-driven lemma insertion;
- explicit smooth-to-rough / special-to-general bridges when needed;
- natural case splitting;
- restrained certainty language;
- proof closure without recap;
- research compression that removes pedagogy before logic.

Do **not** compare vocabulary to the corpus to measure fidelity. Compare decisions to the ledger.

## Semantic fidelity is not textual fidelity

A theorem may express the same mathematics in new prose. Mathematical formulas and canonical terminology are not expected to be artificially changed merely to reduce overlap.

## Report

Return one or more of:
- `PASS`;
- `PASS_WITH_JUSTIFIED_OVERLAP`;
- `FAIL_STRUCTURAL_COPY`;
- `FAIL_PROSE_COPY`;
- `FAIL_STYLE_SOURCE_COPY`;
- `FAIL_STYLE_LEDGER_LEAK`;
- `REVIEW_STYLE_LEDGER_DRIFT`.

## Naturalization independence

The v1.3 naturalization passes do not weaken the source/style firewall.

Audit that:
- recurrence repair did not cause the writer to return to the style corpus for replacement phrases;
- authorial-density decisions were derived from mathematical paragraph roles, not copied paragraph lengths;
- the cold-author pass did not preserve a source sentence merely because it sounded natural;
- no detector-oriented rewriting was used as a reason to alter vocabulary;
- source/style overlap remains low after all naturalization passes.


## Section-narrative independence

When a style corpus was used, verify that the reconstructed paper does not reuse its section order, section-role sequence, subsection pattern, theorem-position pattern, or numerical section fingerprint. Section-level fidelity is judged only by conditional decisions: obligation-family boundaries, prerequisite-sensitive theorem latency, subsection restraint, conceptual/technical pressure handling, and functional closure.

## Whole-paper narrative independence

When whole-work style evidence was used, verify that the final research paper does not reuse:
- source chapter/major-unit order;
- source-wide role sequence;
- source major-unit mass proportions;
- source Introduction/body ratio;
- source theorem-density profile;
- source appendix count, size, or placement pattern;
- source culmination timing as a reason to hide a readable main theorem.

Whole-paper fidelity is conditional and target-driven. Audit only whether the final paper:
- exposes the main result when readability and prerequisites permit;
- separates theorem exposure from proof activation and closure;
- places technical mass where the target proof graph is genuinely difficult;
- compresses front matter from the closed body rather than replaying it;
- uses appendices for modular supporting mathematics rather than proof debt;
- allows mathematics-driven global asymmetry;
- ends when the mathematical contribution ends.

For textbook, monograph, lecture-note, or survey corpora, require an explicit research-article projection before whole-work evidence can influence architecture.
