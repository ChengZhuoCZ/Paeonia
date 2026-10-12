# Protocol 05b — Distilled-Style Realization and Drift Control

For Introduction/outline work, [Protocol 04p](../protocols/04p_reformulation_and_proof_explanation.md) qualifies research compression: retain necessary explanations of novel objects, reformulation gains, and proof dependencies.

## Purpose

Convert an abstract `StyleLedger` into independently written research mathematics without source imitation.

When `ConditionalStyleLedger` exists, Protocol 05n governs role-sensitive **density**, but Protocol 05p fixes the manuscript-wide editorial voice and overrides conflicting stylistic traits; a corpus global average never overrides it.

This protocol is applied twice:

1. during `PROOF_CORE`, so the first publication prose already has the distilled style;
2. during final editorial refinement, to remove drift toward generic academic or formulaic prose.

## 1. Priority order

When style rules conflict, use this order:

1. mathematical correctness, verified citations, semantic fidelity and protected content;
2. explicit user language/format requirements, accepted `LOCAL_POLISH` baseline and mandatory target-journal rules;
3. field-native terminology, readability and coherent mathematical reasoning;
4. the **single Protocol 05p house voice** for every section;
5. compatible stable traits from an *already supplied* corpus, as optional soft evidence;
6. cosmetic editorial preferences.

Do not offer a stylistic selection menu; settle competing recommendations according to the hierarchy.

Never sacrifice a necessary hypothesis, qualification, or justification to match cadence.

## 2. Realization map

Translate ledger traits into decisions, not phrases.

Examples:

- `obstruction_visibility: high` → before changing method, state the precise failure of the current method;
- `lemma_insertion_logic: dependency_driven` → isolate an auxiliary result only when it removes a real obstruction or is genuinely reusable;
- `equation_prose_relation: purpose-display-consequence` → frame the display by role and inference;
- `first_person_plural_policy: mathematical_actions_only` → use first person for actual operations, not administrative narration;
- `proof_closure: closure_at_math_endpoint` → stop when the claim is established.

Do not translate a ledger trait into a fixed sentence template.

## 3. Sentence-level drift checks

Flag a paragraph for rewrite if several of the following occur:

- three or more consecutive sentences begin with first-person plural;
- neighboring paragraphs repeat the same transition phrase;
- a display is followed only by a verbal restatement of the formula;
- generic phrases (`we now proceed`, `it is worth noting`, `the following crucial`) outnumber mathematical reasons;
- `clear/obvious/standard` masks a step that is not locally justified;
- sentence lengths become artificially uniform;
- long sentences contain multiple independent proof moves that should be separated.

## 4. Paragraph-level drift checks

Each proof paragraph should have a dominant role:
- reduction;
- construction;
- estimate;
- legality/justification;
- case transition;
- approximation/limit;
- equality/rigidity;
- closure;
- concise interpretation.

If a paragraph mixes three or more roles, split it unless the mathematics is clearer as a single compact chain.

## 5. Research projection control

When the style corpus is pedagogical, remove pedagogy without flattening the proof.

Delete first:
- reader invitations;
- elementary reminders;
- repeated previews;
- historical asides;
- illustrative examples not used in the proof.

Preserve last:
- why a parameter is chosen;
- why a limit/interchange is legal;
- why the argument must split into regimes;
- what changes in the general case;
- where equality is forced.


## 5a. Section-level drift checks

When a `SectionNarrativeFingerprintLedger` exists, flag architecture for review if:

- sections are created primarily by length, lemma count, or inherited source order;
- theorem placement appears standardized rather than prerequisite-sensitive;
- subsection headings merely rename proof steps;
- repeated one-subsection sections create decorative hierarchy;
- conceptual/technical alternation appears mechanically regular;
- section openings are administrative rather than mathematical;
- long section summaries repeat results without creating a new downstream state.

Judge fidelity against target obligation families, never source section statistics.

## 5b. Whole-paper drift checks

When a `WholePaperNarrativeFingerprintLedger` exists, flag architecture for review if:

- the main result is hidden until the technical proof section despite being readable earlier;
- the Introduction repeats local estimates or mirrors the body section by section;
- technical mass is suspiciously equalized across substantial sections;
- appendices are used as proof-debt storage or contain an unarticulated central mechanism;
- central equality/rigidity logic is exiled from the reader-facing proof spine merely for length;
- the paper inherits a source-wide chapter/section sequence or mass profile;
- a generic Conclusion repeats the Abstract/Introduction after the mathematics has already ended.

Judge fidelity against the target proof graph and appendix modularity, never source-wide ratios or counts.

## 6. Style drift audit

At the final editorial pass, compare the manuscript against the abstract ledger, not against source text.

Report:
- `STYLE-LEDGER-FIDELITY: PASS/REVIEW`;
- `GENERIC-PROSE-DRIFT: PASS/REVIEW`;
- `SOURCE-IMITATION-RISK: PASS/REVIEW`.

A successful manuscript can differ strongly in vocabulary from the corpus while preserving its supported mathematical-writing behavior.

## 7. v1.3 authorial-naturalization handoff

After ordinary style realization, do not continue polishing by free paraphrase. Hand the stable manuscript to:

1. `05c_generative_residue_diagnosis.md`;
2. `05d_authorial_decision_pass.md`;
3. `05e_mathematical_transition_pass.md`;
4. `05f_cold_author_compression.md`.

The handoff preserves the `StyleLedger`. Naturalization is allowed to change density and sentence shape only when the mathematical role justifies it. It must not reopen the style corpus or introduce random lexical variation.
