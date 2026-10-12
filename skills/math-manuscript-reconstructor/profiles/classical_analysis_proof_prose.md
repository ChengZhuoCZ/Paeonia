# Proof-Prose Profile — Classical Analysis, Research Projection v3

For Introduction/outline work, [Protocol 04p](../protocols/04p_reformulation_and_proof_explanation.md) qualifies research compression: retain necessary explanations of novel objects, reformulation gains, and proof dependencies.

## Status

This is an **abstract, source-independent style profile** distilled from a user-supplied mathematical analysis corpus. It captures recurring linguistic and expository decisions, not source sentences, paragraph templates, or an author persona.

The profile has two layers:

1. **language style** — sentence cadence, clause structure, connectors, mathematical verbs, certainty, punctuation, and equation integration;
2. **mathematical writing style** — proof sequencing, theorem/lemma ecology, local explanation, obstacle handling, case transitions, and proof closure.

The research projection deliberately removes textbook-only pedagogy while retaining the corpus's proof clarity.

---

## I. Language style

### 1. Core voice

Use calm, exact, forward-moving prose. Mathematical objects and operations should carry the sentence. Prefer concrete analytical verbs over editorial verbs.

Strong default verbs include:
`choose`, `define`, `write`, `split`, `apply`, `differentiate`, `integrate`, `estimate`, `bound`, `compare`, `pass`, `deduce`, `conclude`, `exclude`, `identify`, `reduce`, `extend`, `approximate`, `normalize`, `rescale`.

Avoid turning the author into the grammatical subject when the mathematics can be the subject instead.

### 2. Sentence cadence

Use mostly medium-length sentences, with deliberate variation.

- Short sentences are appropriate for a decisive reduction, contradiction, or closure.
- Medium sentences should carry one principal mathematical move plus its reason or consequence.
- Longer sentences are reserved for a controlled chain of hypotheses, case qualifications, or a compact comparison of two mechanisms.

Do not create uniformly short "LLM prose" or uniformly long formal prose. Sentence length must follow logical load.

### 3. Clause architecture

Prefer one main mathematical assertion per sentence. Secondary clauses should answer one of four questions:

- why the operation is legal;
- which hypothesis is being used;
- what parameter regime is active;
- what the displayed relation implies.

Avoid decorative subordinate clauses and generic evaluative clauses.

### 4. First-person plural

First-person plural is allowed and often useful for genuine mathematical actions (`we choose`, `we split`, `we apply`), but it is not a default sentence starter.

Do not stack paragraphs whose sentences all begin with `we`. Alternate naturally among:
- the mathematical object as subject;
- a hypothesis-led sentence (`Since ...`);
- a consequence-led sentence;
- a direct construction.

### 5. Transition vocabulary

Transitions should encode mathematical function, not merely continuity of prose.

Preferred classes:
- premise / hypothesis activation;
- consequence;
- construction;
- reduction;
- contrast / change of regime;
- recollection of a previously established tool;
- closure.

Use familiar connectors naturally, but vary them according to function. Do not reproduce corpus frequencies mechanically.

### 6. Certainty and evaluative language

Words such as `clear`, `obvious`, `simple`, `straightforward`, or `immediate` are permitted only when the reason is genuinely short and visible. Prefer to state the reason.

Avoid novelty adjectives, praise, and rhetorical inflation inside proofs.

### 7. Parentheses and side remarks

Use parenthetical remarks for compact qualifications that would otherwise interrupt the proof. A parenthesis should not contain a second proof track.

If a remark changes the logic or adds a hypothesis, move it into the main sentence or a separate paragraph.

### 8. Formula punctuation and grammar

Displayed formulas are grammatical components of surrounding prose. Introduce them with a sentence that makes their role clear and punctuate them according to the sentence.

Do not use a display as a visual pause without a mathematical reason.

---

## II. Mathematical writing style

### 9. Proof openings

For a short proof, begin directly with the reduction, construction, normalization, or estimate.

For a non-obvious proof, use at most one compact strategy sentence identifying the decisive mechanism or obstruction. Do not give a generic roadmap.

If contradiction is the natural mechanism, state it immediately and identify what will contradict the hypothesis.

### 10. Local goal visibility

At each nontrivial transition, the reader should know the current mathematical goal. The goal may be stated explicitly, or it may be obvious from the preceding formula; do not restate it when it is already clear.

Use local goal sentences especially before:
- a delicate estimate;
- a compactness passage;
- an approximation argument;
- a change of regularity class;
- an endpoint limit;
- an equality/rigidity analysis.

### 11. Obstacle-driven exposition

A characteristic move of this profile is:

`current method → exact obstruction → replacement mechanism`.

When the argument changes tools, say what the previous tool no longer provides. Examples include:
- uniform approximation no longer available for rough data;
- a formal identity requiring a justification before limits can pass;
- a local estimate insufficient for a global conclusion;
- a real-variable argument needing analytic continuation;
- an interior estimate needing a separate endpoint treatment.

Do not write vague transitions such as "we now consider the general case" when the real reason for the transition can be stated.

### 12. Equation/prose rhythm

The preferred local unit is:

`mathematical purpose → displayed relation → mathematical consequence`.

Before a display, say what is being computed, compared, or estimated. After the display, say what it gives: decay, convergence, coercivity, cancellation, contradiction, compactness, sharpness, equality, or closure.

Do not translate the symbols line-by-line into prose.

### 13. Theorem and lemma ecology

Statements should enter the exposition because the proof needs them, not because a document template expects them.

A lemma deserves isolation when it:
- removes a genuine obstruction;
- packages a reusable mechanism;
- separates a technically different argument;
- supplies a conceptual fact used more than once;
- protects the main proof from a long but logically subordinate calculation.

Whenever possible, motivate a lemma by the exact role it will play, prove it, and return promptly to the main line.

Do not preserve source theorem grouping by inertia.

### 14. Proof granularity and steps

Continuous prose is the default.

Use numbered steps only for real logical layers, for example:
- model class → finite span → density/closure;
- existence → uniqueness → rigidity;
- low frequency → high frequency → assembly;
- smooth case → approximation → rough case;
- local estimate → global principle → application.

Do not impose three-step scaffolding on a proof that is naturally continuous.

### 15. Justification locality

Place technical permissions where they are used:
- why a parameter can be chosen;
- why a denominator is nonzero;
- why a family is bounded;
- why a limit and integral may be interchanged;
- why integration by parts has no boundary term;
- why approximation is uniform or strong enough;
- why compactness applies;
- why equality propagates.

Do not collect these justifications in a distant paragraph unless they form a reusable lemma.

### 16. Generality ladder

When the clean case reveals the mechanism, prove it first and then bridge explicitly to the general case.

Typical ladders:
- normalized → general by scaling;
- real → complex by decomposition;
- smooth → rough by approximation or closure;
- finite/model → limiting class;
- local → global;
- strict interior parameter → endpoint;
- one sign/regime → complementary sign/regime.

The bridge is part of the proof and must be written, not hidden behind `similarly` when a new issue occurs.

### 17. Technical estimates

State the target quantity before beginning a long estimate. Split the estimate according to the mathematics: near/far, low/high frequency, compact/tail, good/bad set, interior/boundary, small/large parameter.

For each piece, give the source of the bound at the point of use. Choose auxiliary parameters only after the competing errors or constraints are visible.

When several estimates are assembled, one concise assembly sentence should identify the final implication.

### 18. Approximation and limiting arguments

Approximation arguments should show all three layers when nontrivial:

1. what class is dense in what topology;
2. which estimate is stable under that topology;
3. how the limit recovers the desired conclusion.

Do not use `by density` as a black box when the topology or uniformity is mathematically relevant.

### 19. Conceptual interpretation

After a central lemma, one concise sentence may explain its geometric or analytic interpretation **only if** that interpretation makes the next proof easier to follow.

The interpretation should reduce cognitive load, not decorate the manuscript.

### 20. Definitions and setup

Introduce definitions at first mathematical need. If a definition is not standard, precede it by the problem it solves or the phenomenon it captures.

For standard specialist notions, do not reproduce textbook explanations unless the manuscript uses a nonstandard convention.

### 21. Proof endings

End at the actual closure step.

A short closing clause is acceptable when it clarifies which claim has just been completed. Do not append a prose recap of a proof whose final formula already closes the argument.

If a proof has a clean case followed by a generalization, close the clean case locally and then make the generalization transition explicit.

### 22. Post-proof movement

After a result, move in one of four directions only when mathematically useful:
- extract an immediate corollary;
- record a conceptual interpretation;
- identify the exact next obstruction;
- invoke the result in the main proof.

Avoid generic praise or repeated summaries.

---

## III. Research-article projection

The source corpus is expository. A research paper should preserve its proof discipline while compressing pedagogy.

### Retain

- mechanism-first clarity;
- obstacle-driven changes of method;
- local explanations of non-obvious choices;
- dependency-driven lemma insertion;
- purpose → display → consequence rhythm;
- explicit special-to-general bridges;
- mathematically natural regime splits;
- concise conceptual interpretation after genuinely central results;
- enough connective prose for a specialist to audit the argument without reconstructing intent.

### Reduce or remove

- reader coaching;
- exercises and hints;
- historical narrative not needed for the theorem;
- elementary prerequisite definitions;
- repeated chapter previews and recaps;
- long motivational analogies;
- pedagogical repetition of a formula in words;
- repeated reassurance that a calculation is easy.

### Research compression rule

Compress **pedagogy before logic**. Never obtain a shorter paper by deleting the sentence that explains why a limit, approximation, case transition, or equality argument is valid.

---

## IV. Anti-copy and anti-caricature rule

The target is similarity of **clarity architecture and mathematical pacing**, not verbal resemblance.

Forbidden:
- source sentence reuse;
- distinctive phrase reuse;
- source paragraph skeleton reuse;
- source theorem-order reuse merely to preserve style;
- deliberate imitation of an identifiable author persona;
- mechanical insertion of `we now`, `indeed`, `in fact`, or other corpus-frequent markers.

A successful output should feel compatible with the corpus at the level of mathematical exposition while remaining independently written.

---

## V. Authorial Mathematical Prose Overlay

### 23. Naturalness comes from mathematical asymmetry

Do not manufacture irregularity. A research manuscript should be uneven where the mathematics is uneven.

Use six paragraph roles:
- `ROUTINE`: compress;
- `STRUCTURAL`: name the move and its purpose;
- `DELICATE`: justify locally and explicitly;
- `SURPRISING`: add one concise interpretation if it helps the next step;
- `BRIDGE`: state the obstruction and the replacement mechanism;
- `CLOSURE`: stop.

The same syntactic density should not be imposed on these roles.

### 24. Controlled implicitness

The profile distinguishes what must be said from what should be left to standard mathematical literacy.

Must be explicit when nontrivial:
- limit/interchange permissions;
- applicability of external results;
- parameter balancing;
- topology in approximation or compactness;
- uniformity of constants;
- endpoint passages;
- equality and rigidity propagation.

Usually implicit:
- one-line algebra;
- direct substitution;
- immediate differentiation;
- a genuinely identical symmetric case.

Should be implicit:
- symbol-by-symbol translation of a display;
- elementary arithmetic unrelated to a sharp constant;
- redundant reminders of active notation;
- reassurance that a visible one-line operation is easy.

### 25. Transition semantics over transition vocabulary

A transition is chosen by its mathematical relation: cause, reduction, normalization, contrast, regime change, approximation, limit passage, contradiction, rigidity, assembly, or return from an auxiliary result.

Do not rotate `therefore`, `thus`, `hence`, and `consequently` for variety. If recurrence is visible, first ask whether the sentence can name the actual mathematical relation or be deleted.

### 26. Recurrence without cosmetic rewriting

Repeated proof openings, closures, or local phrases are review signals. The available actions are:
`KEEP`, `DELETE`, `COMPRESS`, `MATHEMATICALIZE`, `RESTRUCTURE`.

`SYNONYMIZE` is not an action.

Standard short phrases may repeat when they remain the clearest mathematical language.

### 27. Formula follow-up discipline

A display may be followed by prose only when that prose contributes a consequence, legality condition, interpretation, parameter dependence, equality/rigidity implication, or transition to the next obligation.

If the sentence merely restates the display, remove it.

### 28. Cold-author finish

After style realization and proof closure, perform one deletion-oriented pass. Ask whether every sentence either states mathematics, gives a mathematical reason, or supplies a necessary orientation cue.

The pass may delete, merge, compress, or move prose. It does not add new mathematics.

### 29. Forbidden cosmetic humanization

Never make the manuscript appear more human by:
- random synonym replacement;
- random sentence shortening;
- random paragraph splitting;
- deliberate typos or grammar errors;
- fake uncertainty;
- fake personal voice;
- artificial colloquialism;
- random connector variation;
- optimization against an AI-detector score.

The target is not noisier prose. The target is prose whose choices can be explained by the proof.


## Paragraph-Level Author Fingerprint Overlay (v1.4)

Apply `profiles/classical_analysis_paragraph_fingerprint.md` and `protocols/05h_paragraph_fingerprint_realization.md`. Paragraph boundaries follow changes in mathematical state, not desired visual variety. Routine passages may stay thin; delicate legality and bridge passages thicken locally. Aggregate paragraph statistics from the style corpus are evidence only and must never be generation targets.

## v1.14 high-intensity overlay

For substantial style corpora, this base profile is no longer sufficient by itself. Use `classical_analysis_conditional_style_model.md` and Protocol 05n so the global profile does not flatten routine, delicate, technical, bridge, theorem-leadin, section-opening, and Introduction contexts into one average cadence. Conditional evidence overrides global averages; source numbers remain diagnostic only.
