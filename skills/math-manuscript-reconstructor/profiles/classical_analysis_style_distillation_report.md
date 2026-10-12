# Classical Analysis Style Distillation Report

## Scope

This report records aggregate, non-quotational evidence used to build `classical_analysis_proof_prose.md`. The source corpus is user-supplied mathematical analysis prose. No source sentences are stored here.

Because the corpus is a Markdown/OCR representation, numeric counts are descriptive rather than exact linguistic measurements. They are used to distinguish robust tendencies from accidental local patterns, not as generation quotas.

## Aggregate proof-window signature

- proof windows detected: 610
- sampled words in proof windows: 195,028
- mean sentence length: 20.6 words
- median sentence length: 18 words
- mean paragraph length: 38.16 words
- median paragraph length: 28 words
- numbered-step mentions per proof: 0.033
- explicit closure markers per proof: 0.174
- first-person-plural mentions per 1,000 sampled words: 18.8
- direct-reader-address markers per 1,000 sampled words: 0.17
- evaluative ease markers per 1,000 sampled words: 2.47

Aggregate transition-function counts in sampled proof windows:

- construction: 1,365
- consequence: 908
- premise: 906
- recollection/observation: 452
- contrast/change of regime: 196
- reduction: 162
- explicit closure: 106

These counts support a style driven more by local mathematical operations and implications than by heavy step-label scaffolding.

## Strongly supported language traits

1. **Medium cadence with logical variation.** Prose is neither clipped nor uniformly long. Sentence length changes with mathematical load.
2. **Functional subordinate clauses.** Clauses commonly carry hypotheses, legality, parameter restrictions, or consequences.
3. **First-person plural for mathematical action.** It is frequent enough to be natural but not dominant enough to justify beginning every sentence with the authorial subject.
4. **Functional connectors.** Premise, construction, and consequence markers are much more central than rhetorical signposting.
5. **Low direct reader address in proof windows.** The research projection should remove the remaining pedagogical address almost entirely.
6. **Restrained ease-labeling.** Words indicating that a step is easy occur, but the profile should prefer giving the short reason when auditability matters.
7. **Formula-integrated prose.** Displays are typically embedded in a chain of purpose and inference rather than used as isolated visual objects.

## Strongly supported mathematical-writing traits

1. **Direct proof motion.** Short proofs often begin with the needed reduction, construction, or calculation rather than a generic preview.
2. **Obstacle-driven changes of method.** When a stronger argument no longer applies, the exposition often identifies the obstruction and replaces the tool locally.
3. **Dependency-driven auxiliary results.** Lemmas are frequently isolated because the surrounding proof needs a specific identity, approximation fact, or reusable mechanism.
4. **Local justification.** Legality of approximation, interchange, limiting passage, boundedness, or parameter selection is usually addressed close to use.
5. **Sparse numbered-step scaffolding.** Explicit steps are exceptional relative to continuous proof prose, so they should be reserved for genuine logical layers.
6. **Special-to-general movement with a bridge.** Clean cases are often completed first, followed by the precise device that extends the argument.
7. **Short conceptual interpretation after central mechanisms.** Interpretive prose is useful when it prepares the next argument; it is not a default post-lemma ornament.
8. **Closure at the endpoint.** Proofs generally stop once the target is mathematically secured, with at most a compact closing clause.

## Research projection

The corpus contains pedagogical material, but the target profile is for research papers. Therefore:

Retain:
- proof mechanism visibility;
- local legality checks;
- obstacle-driven transitions;
- explicit generality bridges;
- equation/inference rhythm;
- dependency-driven lemmas.

Compress first:
- exercises and hints;
- elementary definitions;
- direct reader coaching;
- historical digressions not needed by the theorem;
- chapter previews/recaps;
- illustrative repetitions.

The governing rule is: **compress pedagogy before logic**.

## Non-imitation guarantee

This report stores no source sentences or paragraph templates. The associated profile is intended to reproduce abstract proof clarity and pacing only. Final prose must still pass ordinary-prose overlap auditing against the style corpus.

## v1.3 projection: authorial naturalness

The corpus supports a further abstract projection useful for research manuscripts: expository density is not uniformly distributed. Routine manipulations often receive little prose, while changes of method, approximation regimes, limiting arguments, and other nontrivial bridges receive local explanation. Explicit step headings are comparatively sparse, so clarity is more often carried by mathematical relations than by administrative scaffolding.

For v1.3 this is encoded as **mathematics-driven asymmetry**, not as a target sentence-length distribution. The naturalization layer therefore compresses routine narration, preserves delicate legality, and rewrites empty transitions around their mathematical function. It explicitly forbids random synonym rotation or deliberate irregularity. These are research-projection rules; they are not stored source phrases and are not author-persona imitation.

## v1.6 projection: whole-paper narrative mass

A major-unit heuristic over the long-form corpus detects strong global nonuniformity rather than a balanced chapter grid. Across 26 usable body units, major-unit mass varies by roughly a factor of six between the smallest and largest units; formal-result density also varies materially. The heaviest quartile carries a disproportionate share of both prose mass and formal results. Three substantial appendices contain serious supporting mathematics.

The research-article projection is qualitative:

- let difficult proof engines create genuine mass peaks;
- expose the main research result early even when its proof activates later;
- compress front matter from the closed proof rather than reproducing source proportions;
- treat appendices as modular mathematical components, not minor-status material or proof-debt storage;
- allow the paper to end immediately after its final mathematical contribution.

No chapter count, mass coefficient, theorem-density rate, Introduction/body ratio, appendix count, or source-wide order is a generation target.

## v1.14 high-intensity conditional distillation

The earlier proof-window averages are retained as background evidence but no longer serve as the strongest style model. A full-corpus stratified pass over 7,185 usable prose paragraphs separates routine proof motion, delicate passages, technical estimates, method bridges, theorem lead-ins, conceptual interpretation, section openings, Introduction-like orientation, and general exposition. Eight-fold holdout checks support stable role-conditioned differences, especially the local thickening of delicate/technical/bridge prose relative to routine proof motion.

See `classical_analysis_high_intensity_distillation_report.md` and `classical_analysis_conditional_style_model.signature.json`. The governing rule is covariance rather than numeric matching.
