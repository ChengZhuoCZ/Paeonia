# Protocol 05a — Language and Mathematical-Writing Style Distillation

For Introduction/outline work, [Protocol 04p](../protocols/04p_reformulation_and_proof_explanation.md) qualifies research compression: retain necessary explanations of novel objects, reformulation gains, and proof dependencies.

## Purpose

A user may supply a mathematical document whose language and writing style should guide a new research manuscript, or Protocol 05o may acquire a small public corpus after the user names an author. The skill must extract **supported abstract traits** and apply them without copying source prose or recreating an author persona. An acquired author corpus remains author-associated evidence, especially when papers are coauthored.

This protocol explicitly separates:

- **LanguageStyleLedger** — sentence-level realization;
- **MathematicalWritingStyleLedger** — proof and exposition architecture;
- **ParagraphFingerprintLedger** — paragraph boundaries, role-sensitive density, internal paragraph motion, display adjacency, and proof rhythm.
- **SectionNarrativeFingerprintLedger** — section-worthiness, theorem latency, lemma-cluster grouping, subsection policy, conceptual/technical pressure, section openings, and closure.
- **WholePaperNarrativeFingerprintLedger** — main-result exposure, global proof spine, technical-core concentration, front-matter compression, appendix modularity, and whole-paper asymmetry.

The five are combined into `StyleLedger` only after independent extraction. For a substantial corpus, Protocol 05m additionally builds `ConditionalStyleLedger`; this higher-intensity model overrides unsupported global-average assumptions with role-conditioned, holdout-checked evidence. Paragraph-level extraction follows `protocols/05g_paragraph_fingerprint_distillation.md`; section-level extraction follows `protocols/05i_section_narrative_fingerprint_distillation.md`; whole-paper extraction follows `protocols/05k_whole_paper_narrative_fingerprint_distillation.md`.

---

## 1. Style firewall

The style corpus may be read during `STYLE-EXTRACT`. It is never a sentence bank.

After the ledgers are built, quarantine the corpus. Re-open it only to:
- verify whether a proposed trait is actually supported;
- resolve an ambiguity in the style evidence;
- run a source/style overlap audit.

Do not browse source passages while composing final prose sentence by sentence.

---

## 2. Evidence requirement

Every nontrivial style trait must be supported by the corpus.

For each extracted trait record one of:

- `strong`: repeatedly observed across distinct proof/section windows;
- `moderate`: observed in multiple windows but context-dependent;
- `tentative`: observed sparsely and not suitable as a default rule.

The evidence map may store:
- source line/page locators;
- counts;
- rates;
- abstract labels.

It must **not** store source sentences or distinctive phrases.

If the corpus does not support a style claim, omit it rather than filling the gap from general writing advice.

---

## 3. Stratified sampling

Do not infer a style profile from one attractive passage.

When the corpus is large enough, sample across distinct functions:

1. short proofs;
2. long proofs;
3. contradiction arguments;
4. approximation/closure arguments;
5. case or parameter splits;
6. theorem-to-lemma transitions;
7. post-lemma interpretation;
8. technical estimates;
9. section openings;
10. theorem-centered versus machinery-building sections;
11. sections with and without subsections;
12. book/paper-scale orientation passages;
13. contrasting heavy/light major units;
14. appendix-bearing architectures;
15. proof endings.

Prefer examples from multiple chapters or sections. The objective is to distinguish stable style from topic-specific prose. For large corpora, use Protocol 05m rather than stopping at this sampling layer.

---

## 4. LanguageStyleLedger

Record abstract properties only.

```yaml
language_style:
  register:
  sentence_cadence:
  clause_architecture:
  sentence_length_tendency:
  first_person_plural_policy:
  mathematical_verb_profile:
  transition_classes:
  transition_repetition_control:
  certainty_language:
  parenthetical_policy:
  punctuation_and_display_grammar:
  formula_integration:
  lexical_density:
  reader_address_policy:
  avoid_patterns:
```

### 4.1 Sentence cadence

Estimate the distribution of short, medium, and long prose sentences. Use aggregate statistics as evidence, never as a rigid target.

### 4.2 Clause architecture

Determine whether subordinate clauses mostly carry mathematical reasons/conditions or rhetorical commentary.

### 4.3 First-person policy

Measure whether first-person plural is used for mathematical actions, meta-narration, or both. Preserve the function, not the raw frequency.

### 4.4 Mathematical verbs

Identify whether proofs move primarily through active operations (`choose`, `define`, `apply`, `estimate`, etc.) or passive description. Store semantic verb classes, not source phrase lists.

### 4.5 Transition semantics

Classify transitions by function:
- premise;
- consequence;
- construction;
- reduction;
- contrast;
- recollection;
- closure.

Do not imitate transition counts mechanically.

### 4.6 Certainty calibration

Determine how often evaluative words such as `clear`, `simple`, or `immediate` replace an actual justification. The target manuscript should preserve restraint, not verbal tics.

### 4.7 Display grammar

Determine whether displays are introduced by purpose and followed by consequence, and whether formulas participate grammatically in sentences.

---

## 5. MathematicalWritingStyleLedger

```yaml
mathematical_writing_style:
  proof_opening:
  strategy_signal:
  local_goal_visibility:
  obstruction_visibility:
  theorem_entry:
  lemma_insertion_logic:
  proof_granularity:
  step_heading_frequency:
  equation_prose_relation:
  justification_locality:
  parameter_choice_explanation:
  case_split_pattern:
  approximation_transition:
  generality_ladder:
  conceptual_interpretation:
  technical_detail_density:
  proof_closure:
  post_proof_movement:
  definition_entry:
  section_movement:
  research_projection:
  avoid_patterns:
```

### 5.1 Proof openings

Determine whether proofs begin with direct mathematical action, a strategy sentence, contradiction, normalization, or a preliminary reduction.

### 5.2 Obstruction visibility

Look specifically for transitions where a method stops working and another method is introduced. Record the *reason for the transition* as a style trait.

### 5.3 Theorem/lemma ecology

Determine whether auxiliary results are introduced because the main argument needs them, whether their role is stated first, and how quickly the text returns to the main proof.

### 5.4 Equation/prose interaction

Determine whether prose:
- gives a local purpose before a display;
- names the mathematical consequence after it;
- avoids line-by-line translation of symbols.

### 5.5 Justification locality

Measure whether hypotheses and permissions are invoked at the point of use.

### 5.6 Generality ladder

Extract recurring bridges such as:
- clean case → general case;
- smooth → rough by approximation;
- finite/model → closure;
- local → global;
- one parameter regime → another;
- formal calculation → rigorous justification.

### 5.7 Technical estimate structure

Record how the text partitions a difficult estimate and how it explains the source of each bound.

### 5.8 Closure and post-proof movement

Determine whether the proof stops at closure and whether the next paragraph gives a corollary, interpretation, or next obstruction rather than a generic recap.

---

## 6. Research-article projection

When the reference corpus is a textbook, lecture text, or expository monograph but the target is a research article, perform a controlled projection.

### Retain

- mechanism-first clarity;
- local legality checks;
- obstacle-driven changes of method;
- dependency-driven lemma insertion;
- explicit special-to-general bridges;
- purpose/display/consequence rhythm;
- natural estimate splitting;
- concise interpretation that reduces later cognitive load.

### Remove or compress

- exercises and hints;
- direct reader coaching;
- elementary definitions for specialist audiences;
- long historical digressions;
- repeated motivational analogies;
- chapter-style previews and recaps;
- pedagogical repetitions of already transparent formulas.

### Projection invariant

**Compress pedagogy before logic.** A research projection may be shorter than the corpus, but it must not delete the sentence that makes a non-obvious inference auditable.

---

## 7. Extraction before proof drafting

Style extraction is an **internal pre-drafting operation**, not manuscript prose. Therefore it is compatible with proof-body-first composition.

When a style corpus is supplied or acquired:

1. for an author corpus, first complete `AuthorCorpusDossier` under Protocol 05o;
2. build the style artifacts appropriate to the authorized scope before `PROOF_CORE`; a full-manuscript reconstruction may require `LanguageStyleLedger`, `MathematicalWritingStyleLedger`, `ParagraphFingerprintLedger`, `SectionNarrativeFingerprintLedger`, and `WholePaperNarrativeFingerprintLedger`, while an Introduction-only or local-polish task extracts only the relevant supplement;
3. quarantine the style corpus;
4. draft the proof core using the abstract ledgers;
5. do not write Introduction or Abstract before `ProofCoreGate`.

This ordering ensures that the first publication prose—the proof body—is already written in the distilled style.

---

## 8. Independence rule

Style success is not measured by verbal resemblance. It is measured by whether a specialist experiences comparable **clarity, pacing, local justification, and mathematical emphasis** while the actual sentences and paragraph structures are independently generated.

Run `tools/source_overlap_audit.py` against the style corpus and final prose. Shared long ordinary-prose n-grams trigger review. Standard mathematical expressions, theorem names, and unavoidable fixed terminology are excluded from judgment.
