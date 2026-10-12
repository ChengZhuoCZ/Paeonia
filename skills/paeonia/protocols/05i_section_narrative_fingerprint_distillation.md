# Protocol 05i — Section-Level Narrative Fingerprint Distillation

## Purpose

Extract from a sufficiently large style corpus the **conditional decisions** governing section architecture without turning source section lengths, order, titles, theorem positions, or subsection counts into templates.

The output is a `SectionNarrativeFingerprintLedger`. It stores abstract policies and aggregate evidence only.

## Constitutional rule

A section is a mathematical unit, not a page-length bucket.

Create or retain a section only when a reader-facing mathematical state changes at a scale larger than a paragraph. Typical triggers are:

- `OBLIGATION_FAMILY`: a coherent family of proof obligations becomes active;
- `NEW_OBJECT_OR_SPACE`: a new class of objects, function space, geometry, or normalization becomes the working setting;
- `METHOD_FAMILY_SHIFT`: the proof changes to a different engine or technology;
- `REUSABLE_ENGINE`: several downstream claims will consume the same mechanism;
- `REGIME_OR_GEOMETRY_SHIFT`: a genuinely different parameter regime or geometry begins;
- `APPLICATION_PHASE`: an established theory is now applied to a distinct target problem;
- `COUNTEREXAMPLE_OR_CONSTRUCTION_PHASE`: the paper changes from theory to an extended construction;
- `SYNTHESIS_OR_RETURN`: auxiliary machinery is complete and the argument returns to the principal theorem.

The following are **not** sufficient reasons by themselves:

- the source manuscript had a section there;
- a discovery notebook grouped the lemmas there;
- the page count feels long;
- there are three lemmas in a row;
- the author wants visual variety;
- the source corpus often used a similar number of sections.

## 1. Corpus segmentation

Sample sections across different mathematical functions, not only attractive exposition. Include, when present:

- theorem-centered sections;
- definition/setup sections;
- technical proof-engine sections;
- application sections;
- counterexample/construction sections;
- sections with and without subsections;
- short sections and long sections;
- sections whose principal theorem is stated immediately and sections where it is delayed by necessary setup.

Exclude exercises/problems and OCR page headers from quantitative evidence when possible.

## 2. Section role taxonomy

Classify each sampled section by its dominant function. A section can have a primary and secondary role.

- `CONCEPTUAL_SETUP`: establishes the objects, problem, definitions, or viewpoint needed later.
- `THEOREM_CENTERED`: the main result is the immediate organizing object.
- `TECHNICAL_ENGINE`: develops estimates, kernels, transforms, compactness, interpolation, or another reusable mechanism.
- `APPLICATION_RETURN`: applies established machinery to a mathematical target.
- `CONSTRUCTION_COUNTEREXAMPLE`: develops an explicit object or negative example.
- `SYNTHESIS`: assembles previous pieces or returns from auxiliary theory to the main theorem.
- `REFERENCE_APPENDIX`: isolates supporting material whose local role is primarily reference/verification.

Do not infer that target manuscripts need the same role sequence as the source.

## 3. Theorem-latency modes

For each section, record the **reason** the principal formal result is placed where it is.

- `IMMEDIATE`: the theorem itself is the section's point; prerequisites are already available.
- `MOTIVATED`: a short problem statement, reduction, or interpretive bridge is needed before the theorem.
- `DEVELOPED`: definitions, notation, or a compact proof engine must be established first.
- `DEFERRED`: the section is itself a machinery-building or construction phase; the payoff arrives only after substantial development.

The corpus may support all four modes. Their observed word distances are evidence only. Never generate toward source medians or quantiles.

## 4. Lemma-cluster to section decision

A cluster of lemmas earns its own section when one or more of the following hold:

1. the lemmas form a reusable engine consumed by multiple later claims;
2. they share a stable object, notation, or regime that is not active outside the cluster;
3. they solve a coherent obligation family whose completion marks a genuine proof milestone;
4. they require a different method from the surrounding proof;
5. isolating them removes a substantial technical interruption from the main theorem;
6. the reader will later need a natural re-entry point to cite or revisit the mechanism.

A cluster should usually **remain inside the surrounding section** when it is merely a linear chain of local steps for one theorem, uses no independent notation/method, and has no downstream life of its own.

Discovery history is never a section criterion.

## 5. Subsection policy

A subsection is justified only by a stable internal phase that has its own mathematical role.

Strong triggers:

- two or more distinct local obligation families inside one section;
- a method or regime change that is important but not large enough for a new section;
- a reusable construction followed by its consequences;
- a long section in which named re-entry points materially improve navigation;
- several logically independent components that share one overarching section purpose.

Suppress subsections when:

- the section is theorem-centered and flows continuously;
- headings would merely rename `Step 1`, `Step 2`, `Step 3`;
- there is only one genuine internal phase;
- a subsection would contain only one short lemma or calculation;
- headings duplicate theorem names rather than clarify structure;
- the only reason is length or visual balance.

A section with no subsections is a normal outcome, not a missing organizational layer.

## 6. Conceptual/technical section pressure

Record how the source moves between conceptual and technical pressure, but never copy the exact sequence.

Useful abstract transitions include:

- `CONCEPTUAL_SETUP → TECHNICAL_ENGINE`;
- `TECHNICAL_ENGINE → APPLICATION_RETURN`;
- `APPLICATION_RETURN → NEW_OBSTRUCTION`;
- `THEOREM_CENTERED → TECHNICAL_ENGINE → SYNTHESIS`;
- `CONSTRUCTION_COUNTEREXAMPLE → INTERPRETATION`.

Do **not** enforce alternation. Consecutive technical sections are legitimate when the proof requires them; consecutive conceptual sections are legitimate when a new language or geometry must be built. The fingerprint stores a **pressure wave**, not a decorative alternating pattern.

## 7. Section openings

Classify section openings by mathematical function:

- `GOAL_FIRST` — state the theorem/problem immediately;
- `PROBLEM_FIRST` — formulate the question before formal results;
- `OBJECT_FIRST` — define the object/space/normalization needed for the section;
- `OBSTRUCTION_FIRST` — explain why the previous method is insufficient;
- `APPLICATION_FIRST` — announce the new target to which established machinery is applied;
- `RECALL_AND_PIVOT` — recall one precise input and immediately change direction;
- `CONSTRUCTION_FIRST` — introduce the object to be built.

Avoid generic section openings that only say the paper now turns to another topic.

## 8. Section closure modes

Classify closure by what mathematical state becomes true:

- `OBLIGATION_CLOSED` — the section's proof family is complete;
- `ENGINE_READY` — a tool is now available downstream;
- `APPLICATION_RESOLVED` — the target application is complete;
- `RETURN_TO_MAIN` — auxiliary development is finished and the main line resumes;
- `NEXT_OBSTRUCTION_EXPOSED` — a new unresolved issue is named precisely;
- `NO_EXTRA_CLOSURE` — the final proof/formula already supplies a sufficient endpoint.

Do not add summary prose simply because a section is long.

## 9. Evidence fields

The ledger may store:

- section count in the sampled corpus;
- proportion with/without subsections;
- broad section-size bins;
- theorem-latency class counts;
- formal-result density distributions;
- subsection-use distributions by broad size bin;
- qualitative role-transition counts;
- optional line/page locators for evidence.

It must not store source section prose, source paragraph sequences, source section-order templates, or numerical targets for generation.

## 10. Output contract

Return a `SectionNarrativeFingerprintLedger` conforming to `schemas/section_narrative_fingerprint.yaml`.

Every inferred rule must be marked:

- `SUPPORTED` — repeated evidence across materially different sections;
- `TENTATIVE` — plausible but sparsely evidenced;
- `UNSUPPORTED` — do not use for generation.

The ledger must explicitly state:

`numeric_targets_forbidden: true`

`source_section_order_reuse: forbidden`

`source_subsection_pattern_reuse: forbidden`

`exact_theorem_latency_reuse: forbidden`
