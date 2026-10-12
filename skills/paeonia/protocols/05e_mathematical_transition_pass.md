# Protocol 05e — Mathematical Transition Pass

## Purpose

Replace editorial continuity with mathematical continuity.

A transition should answer **why the next sentence is mathematically licensed or necessary**.

## 1. Transition semantics

Classify transitions by relation, not by preferred synonym.

Supported classes include:
- `PREMISE_ACTIVATION` — a hypothesis becomes usable;
- `CAUSE` — one fact produces another;
- `REDUCTION` — the current goal is replaced by an equivalent/sufficient one;
- `NORMALIZATION` — scaling or symmetry removes inessential freedom;
- `CONTRAST` — a previous method fails or a regime changes;
- `CASE_CHANGE` — sign/scale/frequency/geometric regime changes;
- `APPROXIMATION` — passage from a tractable class to the target class;
- `LIMIT_PASSAGE` — a uniform bound or convergence permits a limit;
- `BOOTSTRAP` — an estimate improves regularity/size and is fed back;
- `CONTRADICTION` — the derived statement conflicts with an assumption;
- `RIGIDITY` — equality forces structural constraints;
- `ASSEMBLY` — independently controlled pieces close the target estimate;
- `RETURN_TO_MAIN_ARGUMENT` — an auxiliary lemma has supplied the missing input.

## 2. Mathematicalize, do not synonymize

Bad transformation:
`Therefore` → `Consequently` → `Hence` solely to avoid repetition.

Preferred transformation:
- state the vanishing boundary term;
- name the uniformity that permits the limit;
- state which error is absorbed;
- state which hypothesis excludes the alternative;
- state why equality propagates.

The actual relation determines the sentence.

## 3. Preferred compact forms

Use concise forms when the relation is local and obvious from the named reason:
- `By Lemma 3.2, ...`
- `Since the bound is uniform in ε, letting ε→0 gives ...`
- `After rescaling, it is enough to consider ...`
- `The first term vanishes by symmetry, while ...`
- `Equality in the previous estimate forces ...`

These are patterns of logical function, not fixed templates; vary only when the mathematics varies.

## 4. Return from auxiliary results

After proving an auxiliary lemma, return to the main proof by naming the exact missing input it supplies. Avoid generic prose such as `We can now continue the proof.`

## 5. Assembly sentences

When several estimates are combined, state the final mathematical effect rather than announcing combination.

Prefer:
`The tail is o(N^{-3}) and the low-frequency term is coercive, so the deficit is positive for all sufficiently large N.`

Avoid:
`Combining the above estimates, we obtain the desired result.`

## 6. Pass condition

`MATHEMATICAL-TRANSITIONS: PASS` requires that high-frequency editorial transitions have either been deleted or replaced by relations carrying mathematical information. Repetition of standard short connectors is acceptable when it is the clearest form.
