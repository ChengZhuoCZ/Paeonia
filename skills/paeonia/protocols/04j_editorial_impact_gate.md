# Protocol 04j — Editorial Impact Gate


> **Conditional gate.** Use for program-level or demonstrably under-positioned papers. Ordinary Introductions pass through the reader contract in Protocol 04; they do not need to answer every parent-program question listed here.

## Purpose

Audit whether a mathematically correct, stylistically natural Introduction has fully communicated the paper's genuine significance. This gate complements anti-hype checks: it blocks unsupported inflation **and** avoidable under-positioning.

The question is not `Does the Introduction sound important?` The question is `Does the Introduction make the strongest verified mathematical case for why this paper deserves attention?`

## Editorial first-two-pages test

A specialist editor reading only the first part of the Introduction should be able to answer, at the level supported by the paper:

1. What is the parent mathematical program or canonical principle above the local conjecture?
2. What scale/category transition makes the focal problem a natural missing piece of that program?
3. What was the strongest verified position before this paper?
4. What exactly remained unresolved?
5. Why did the most natural prior mechanism fail or stop, if this matters?
6. What exactly does the present theorem add?
7. How strong is the result: local/global, partial/complete, qualitative/quantitative, sharp/nonsharp, restricted/unrestricted?
8. What changes in the mathematical picture because of the theorem?
9. Is there a proof mechanism that actually crosses the recorded mathematical transition rather than merely executing local estimates?
10. After the theorem, can the reader say what changed in the parent program?

Not every paper must answer all nine at grand scale. A `STANDARD` paper passes when it accurately communicates its smaller scope. A `GRAND` or `GRAND_PLUS` paper fails if central verified significance remains buried or euphemized.

## Pass conditions

Pass only if all applicable conditions hold:

- `NarrativeAmbitionLedger` selects a scale supported by evidence;
- `MathematicalStoryLedger` passes when required, with a mathematically specific parent program, supported archetype/transition, and verified ancestry;
- every verified `must_surface` contribution appears clearly;
- when central, the reformulation is explained at the level of the new information or control it unlocks, with structural importance distinguished from historical priority;
- the paper's main novelty is described at its strongest defensible scope;
- the historical/frontier arc stops at the exact gap addressed by the paper;
- the obstruction is concrete when it is part of the contribution story;
- theorem interpretation states what mathematical picture changes rather than repeating the statement;
- broader consequences are neither absent when clearly supported nor invented when unsupported;
- method significance is calibrated to actual transferability;
- strong wording is neither artificially suppressed nor used beyond its verified scope;
- the first two pages contain enough signal that an editor need not reconstruct the contribution from the proof section.

## Failure modes

Flag `FAIL_EDITORIAL_IMPACT` when any applicable condition occurs:

- a verified conjecture resolution is described only as `progress` or `a result related to`;
- a verified first global/complete/sharp result is hidden behind generic cautious language;
- the Introduction spends substantial space on history but never identifies the exact frontier before the paper;
- the theorem is stated accurately but its consequence for the existing picture is never explained;
- the new mechanism is potentially transferable and this is mathematically evident, yet the Introduction presents it as routine bookkeeping;
- the Introduction uses broad evaluative language without a corresponding mathematical relation;
- the paper is labeled `GRAND` or `GRAND_PLUS` but its narrative scale is not supported by theorem/literature evidence;
- the paper is genuinely program-level but the Introduction remains at the scale of the technical lemma that closes the proof;
- amplification introduces a stronger factual claim than the ledger permits;
- the Introduction remains at local-problem scale when the paper's verified significance lies in a larger program;
- physical/scientific motivation is rich but substitutes for, rather than complements, the mathematical story.

## Repair routing

Repair at `INTRODUCTION_NARRATIVE` if the scale, frontier, result hierarchy, or ambition ledger is wrong. Repair at `FRONTMATTER` if the underlying positioning is correct but the prose understates, overstates, or fails to interpret the contribution.

Do not repair by adding unsupported adjectives. Repair by changing mathematical positioning, contrast, consequence, or mechanism prose.

## Scientific-context and grandeur check

If the paper has a verified scientific lineage, ask whether the Introduction surfaces it at the depth selected by `ScientificContextLedger`. Reject both decorative one-line motivation and unjustified encyclopedic background.

Apply `protocols/04n_mathematical_story_discovery.md` and `protocols/04o_mathematical_story_integration.md` only when an operative parent program or scale/category transition is part of the verified significance. Apply `protocols/04m_contextual_grandeur.md` only when a larger verified stake, historical axis, or scientific model gives a clearer theorem-facing opening; a scale label alone does not force either module.
