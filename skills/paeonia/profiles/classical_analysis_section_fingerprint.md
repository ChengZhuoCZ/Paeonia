# Classical Analysis Section Narrative Fingerprint — Distilled Research Projection

This profile records section-scale **abstract narrative decisions** extracted from the supplied analysis corpus. It is not a section-count template, a theorem-placement template, or an authorship classifier.

## Descriptive evidence

The heuristic section extractor located 141 usable non-exercise/problem sections across the corpus. Of these, 80 had no detected subsection and 61 had at least one. The median section contained about 1469 prose words, with an interquartile range of roughly 765–2868. The median detected formal-result count was 5. These numbers are evidence only.

Subsection use was strongly non-uniform across broad section-size bins: it was uncommon in shorter sections and much more common in long sections. This supports a conditional rule—**internal hierarchy appears when stable internal phases accumulate**—not a word-count threshold.

The first formal-result placement also varied substantially. The extractor observed all four qualitative theorem-latency modes: immediate, motivated, developed, and deferred, together with sections whose purpose was expository/machinery-building and contained no detected formal result. The source therefore does not support a single preferred distance from section heading to theorem.

## Distilled section policy

1. **A section is an obligation family.** It collects a coherent mathematical phase rather than a convenient amount of text.
2. **Theorem latency follows prerequisite burden.** If the theorem is already intelligible, state it immediately; if definitions or machinery are needed, earn the delay mathematically.
3. **Lemma clusters need downstream life.** Several local lemmas do not automatically deserve a section. Isolation is justified by reuse, stable local notation, a distinct method, or a genuine proof milestone.
4. **Subsections are optional.** A continuous theorem-centered section may remain flat even when substantial. Internal hierarchy is introduced only when the reader must navigate distinct stable phases.
5. **One-subsection hierarchy is suspicious, not forbidden.** It should trigger review of whether the heading is doing real mathematical work.
6. **Conceptual and technical pressure form waves, not an alternation rule.** Conceptual setup may lead into a technical engine and then an application or synthesis, but consecutive technical or conceptual sections are allowed when demanded by the proof.
7. **Section openings establish state.** They state a goal, problem, object, obstruction, application target, or exact pivot rather than merely announce a topic change.
8. **Section closure is functional.** Stop when the obligation family is closed; add a forward link only when it identifies a concrete next mathematical use or obstruction.
9. **Research projection compresses textbook navigation.** Historical asides, exercises, elementary recaps, and pedagogical chapter logistics are not transferred into research-paper architecture.

## Theorem-latency modes

- `IMMEDIATE`: theorem is the section's organizing object and all prerequisites are already available.
- `MOTIVATED`: a short reduction, problem statement, or interpretation is useful first.
- `DEVELOPED`: definitions or compact local machinery must precede the formal claim.
- `DEFERRED`: the section's purpose is to build an engine/construction whose payoff appears later.

No observed latency count or word distance may be used as a generation target.

## Subsection decision

Prefer no subsection when the section is one continuous proof phase. Add subsections only for stable internal roles such as setup, local theory, a substantial estimate block, compactness/limit passage, rigidity/equality, application, or final assembly.

The fact that the corpus contains many sections without subsections is evidence that **flat section structure is normal** when the mathematics is continuous.

## Section pressure wave

The supported abstract pattern is not `conceptual → technical → conceptual → technical` by rule. The supported pattern is:

`orientation when needed → sustained proof work → reorientation only after a genuine state change → payoff/return`.

## Non-target rule

No statistic in this file may be optimized directly. Section boundaries, section lengths, theorem positions, and subsection counts must be generated from the target `ProofGraph`, downstream dependency structure, and reader re-entry needs.
