# Protocol 05n — Conditional Style Realization

## Purpose

Turn `ConditionalStyleLedger` into manuscript prose whose **explanatory density** changes with mathematical function. This is the realization counterpart of Protocol 05m. It never creates multiple selectable voices: Protocol 05p fixes one consistent, journal-neutral, research-mathematics register throughout the paper.

## 1. Create a transient `StyleContextCard`

Before drafting or revising a nontrivial paragraph, identify internally:

- manuscript surface: proof / theorem lead-in / section opening / Introduction / interpretation;
- mathematical role: routine / delicate / estimate / bridge / closure;
- pressure: low / medium / high;
- transition function: construction / premise / reduction / contrast / consequence / return / closure;
- explicitness burden: routine / legality-sensitive / equality-sensitive / endpoint-sensitive;
- applicable conditional style stratum;
- evidence confidence.

Do not display this card to the user unless asked.

## 2. Context overrides global style

If the global style profile prefers medium cadence but the current paragraph is `PROOF_ROUTINE`, use the routine stratum. If the current paragraph is a limiting or approximation bridge, use the bridge/delicate stratum.

Never flatten all paragraphs toward the global corpus average. Never let any stratum overturn Protocol 05p or trigger an alternative tone for a section.

## 3. Role-conditioned realization

### `PROOF_ROUTINE`

- move directly;
- minimize narration;
- let formulas and concrete mathematical verbs carry the step;
- do not explain standard algebra twice.

### `PROOF_DELICATE`

- thicken locally;
- make hypotheses and legality visible at point of use;
- permit longer conditional sentences when they carry real mathematical conditions;
- state why a limit, approximation, compactness step, endpoint, or equality passage is legitimate.

### `PROOF_TECHNICAL_ESTIMATE`

- name the quantity being controlled;
- make the source of each bound visible;
- split only by genuine regimes;
- use prose to expose causal assembly, not to narrate every line.

### `PROOF_BRIDGE`

- state what the previous mechanism no longer gives;
- name the replacement mechanism;
- connect the two in one mathematical transition, not an administrative announcement.

### `PROOF_CLOSURE`

- close promptly;
- do not recap a proof whose last inference is already decisive.

### `THEOREM_LEADIN`

- orient only as much as necessary for the theorem to be readable;
- avoid ceremonial announcement language;
- expose the mathematical threshold that makes the statement natural.

### `CONCEPTUAL_INTERPRETATION`

- explain one useful mathematical meaning;
- stop once it has prepared the next move;
- do not turn every lemma into a mini-essay.

### `SECTION_OPENING`

- enter through the object, problem, method, or obstruction;
- use a broader pressure budget than a routine proof paragraph;
- avoid administrative section narration when the mathematics can lead.

### `INTRO_ORIENTATION`

- use the conditional microstyle only after research-genre projection;
- allow broader, more clause-rich sentences when they genuinely connect mathematical scales;
- suppress redundant textbook background and empty reader coaching; preserve the novel-mechanism explanation required by Protocol 04p;
- let the research-Introduction narrative engine determine what is worth saying.

## 4. Introduction role mapping

When `IntroductionParagraphPlan` is available, map paragraph roles to microstyle priors:

- `FIELD_ORIENTATION`, `CLASSICAL_LANDMARK` → projected `INTRO_ORIENTATION` / `SECTION_OPENING`;
- `CURRENT_FRONTIER`, `NARROWING_TO_TARGET` → `SECTION_OPENING` / `THEOREM_LEADIN`;
- `OBSTRUCTION`, `ADJACENT_PROBLEM_BRIDGE`, `RETURN_TO_MAIN_THREAD` → `PROOF_BRIDGE`;
- `THEOREM_ORIENTATION`, `FORMAL_THEOREM`, `RESULT_LADDER_BRIDGE` → `THEOREM_LEADIN`;
- `THEOREM_INTERPRETATION`, `METHOD_POSITIONING` → `CONCEPTUAL_INTERPRETATION`;
- `PROOF_MECHANISM` → `PROOF_BRIDGE` plus `PROOF_TECHNICAL_ESTIMATE` causal discipline.

This mapping affects sentence/paragraph realization only. It does not dictate the Introduction's macro narrative.

## 5. Do not imitate metrics

Corpus numbers are diagnostic evidence. Never ask whether a paragraph is close to the source median. Ask whether the paragraph reacts to mathematical pressure in the same *kind* of way.

## 6. Drift check

On final read, flag manuscripts where:

- routine and delicate paragraphs have become equally explanatory;
- every paragraph uses the same sentence cadence;
- administrative openers replace mathematical entry anchors;
- first-person narration becomes the default grammatical subject;
- technical estimates and conceptual interpretation share the same prose geometry;
- Introduction paragraphs ignore their role-specific microstyle.

Repair the local role realization, not the vocabulary.
