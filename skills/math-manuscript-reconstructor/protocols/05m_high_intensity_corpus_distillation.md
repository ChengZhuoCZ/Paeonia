# Protocol 05m — High-Intensity Conditional Corpus Distillation

For Introduction/outline work, [Protocol 04p](../protocols/04p_reformulation_and_proof_explanation.md) qualifies research compression: retain necessary explanations of novel objects, reformulation gains, and proof dependencies.

## Purpose

Use this protocol when the user supplies a substantial mathematical style corpus, or Protocol 05o acquires enough representative papers to support genuine role stratification, and strong style transfer is requested. The objective is not a longer style summary. The objective is a **conditional style model** whose decisions change with the mathematical role of the sentence, paragraph, proof movement, section, and Introduction paragraph.

This protocol supplements 05a. It never replaces the source/style firewall.

## 1. Trigger

Use high-intensity distillation when the style corpus is large enough to support stratification across multiple mathematical functions. A long book, monograph, broad collection of papers, or large Markdown extraction normally qualifies. The default four-paper author corpus does **not** automatically qualify: it falls back to 05a unless its sampled windows cover enough independent roles, years, and coauthor configurations for stable conditional evidence.

## 2. Distill by mathematical role, not global average

Partition the corpus into abstract strata such as:

- `PROOF_ROUTINE`;
- `PROOF_DELICATE`;
- `PROOF_TECHNICAL_ESTIMATE`;
- `PROOF_BRIDGE`;
- `PROOF_CLOSURE`;
- `THEOREM_LEADIN`;
- `CONCEPTUAL_INTERPRETATION`;
- `SECTION_OPENING`;
- `INTRO_ORIENTATION`;
- `GENERAL_EXPOSITION`.

The labels are analytical categories, not source headings. Do not store the source paragraphs assigned to them.

A single global sentence-length mean or paragraph-length mean is never sufficient evidence for realization.

## 3. Extract conditional features

For each stratum, measure only abstract features:

- paragraph pressure;
- sentence cadence;
- clause load;
- first-person use;
- administrative opener density;
- sentence-opener classes;
- transition-function classes;
- parenthetical and punctuation behavior;
- formula adjacency / formula density proxies;
- closure density;
- reader-address and ease-label frequency.

Do not emit lexical inventories or distinctive phrases.

## 4. Cross-fold stability

Split a large corpus into multiple contiguous or chapter-level folds. Re-estimate each major feature on held-out regions.

Classify a feature:

- `strong` when it recurs across enough independent folds with low relative dispersion;
- `moderate` when it is recurrent but context-sensitive;
- `tentative` when it is sparse or unstable.

Only strong features may become default realization rules. Moderate features become preferences. Tentative features remain diagnostics and may not control prose.

The purpose is to distinguish an authorial habit from a local chapter accident.

## 5. Learn covariance, not targets

The central object is not a target distribution. It is **how prose changes when mathematics changes**.

Examples of admissible evidence:

- delicate proof paragraphs are consistently thicker than routine proof paragraphs;
- technical estimates carry more conditional clauses than routine algebra;
- theorem lead-ins are shorter than section openings;
- section openings rely less on administrative authorial narration than ordinary proof movement;
- conceptual interpretation receives more space than a routine consequence but less than a full technical bridge.

These relations may guide realization.

Forbidden:

- matching a source median word count;
- forcing the source variance;
- reproducing the source role sequence;
- adjusting prose until a numerical style score matches the corpus.

## 6. Build `ConditionalStyleLedger`

The ledger records:

1. source role assignment (`microstyle_corpus`, optional `narrative_reference`, optional domain reference);
2. stratum-conditioned realization decisions;
3. stable cross-context covariance;
4. Introduction microstyle mapping;
5. research-article projection;
6. confidence and holdout stability.

It stores no source sentence, source paragraph, n-gram bank, or author persona.

## 7. Research-genre projection

A textbook or monograph can be a strong microstyle corpus without being a valid research-article architecture source.

When projecting to a specialist paper:

- retain cadence, mathematical subject choice, local explanation, obstruction handling, theorem-entry discipline, estimate movement, and closure rhythm;
- compress pedagogy, elementary definitions, reader coaching, exercises, recaps, and historical exposition that does not position the theorem;
- do not infer research-priority rhetoric or journal-scale narrative from textbook material.

This separation is mandatory.

## 8. Reference-role separation for Introductions

When a separate research-article Introduction reference exists, assign roles explicitly:

- **large Markdown / book corpus** → microstyle, sentence/paragraph realization, mathematical movement;
- **research-article Introduction reference** → macro narrative geometry, theorem positioning, literature choreography, editorial scale.

The final Introduction combines the two at the level of abstract decisions only.

## 9. Quarantine

After `ConditionalStyleLedger` and its aggregate evidence report are built, quarantine the source corpus. Final prose is composed from the ledgers, never by repeatedly consulting attractive source passages.

## 10. Release criterion

High-intensity distillation passes only if:

- multiple strata are supported;
- major default traits survive holdout checks;
- context-conditioned rules are more informative than global averages;
- the research projection is explicit;
- no source phrases or source sequence templates are stored.
