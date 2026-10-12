# Protocol 04c — Grand-Narrative Integrity Audit


> **Conditional audit.** Run only when a grand/program-level narrative was deliberately selected and supported. It is not a default gate for every substantial Introduction.

## Purpose

A broad Introduction must remain mathematically earned. This audit rejects rhetorical grandeur that is unsupported by the proof or literature.

## Pass conditions

Pass `GRAND-NARRATIVE-INTEGRITY` only if all applicable conditions hold:

1. **Scale is earned.** `GRAND_PLUS`, `GRAND`, or `EXPANSIVE` follows from the theorem/literature position, not a stylistic preference.
2. **The main result is visible.** The reader reaches the exact contribution without an avoidable historical detour.
3. **The problem tension is mathematical.** Difficulty is explained through an obstruction, not prestige adjectives.
4. **The theorem ladder is real.** Each displayed result has a distinct reader-facing role.
5. **Literature has roles.** Citations locate origin, frontier, obstruction, or neighboring theory; they are not a bibliography dump.
6. **Adjacent problems have bridges.** Each excursion explains shared structure and decisive difference.
7. **Result repetition is functional.** Orientation, formal statement, and interpretation are distinct; literal restatement is removed.
8. **Mechanism beats itinerary.** The proof overview describes mathematical moves before section numbers.
9. **No hype or underclaim debt.** Priority, sharpness, completeness, and open-problem language are verified; verified central strong claims are not euphemized into materially weaker descriptions.
10. **Proof-first truth is preserved.** No claim in the Introduction exceeds the closed proof ledger.

## Automatic blockers

Flag `FAIL_GRAND_NARRATIVE` for any of:

- generic `long and rich history` opening with no mathematical function;
- unsupported claims that the result is fundamental, groundbreaking, complete, first, or long-standing;
- a verified central result is systematically weakened into vague `progress` language so that the paper's actual position becomes unclear;
- a literature paragraph that can be removed without changing the problem position;
- a conjecture presented as solved when only a subproblem or consequence is established;
- a theorem ladder invented to make the paper appear stronger;
- an adjacent problem with no stated mathematical bridge;
- proof roadmap consisting mainly of section-by-section administration;
- the main theorem delayed solely to preserve dramatic buildup;
- Introduction claims not recoverable from the MathLedger or verified scholarship.

## Repair routing

Repair at `INTRODUCTION_NARRATIVE` / `FRONTMATTER`, unless the audit reveals a false mathematical or scholarship claim. In that case roll back to `LEDGER_LOCK` or citation verification before rewriting prose.


## Larger mathematical-story dependency

For `EXPANSIVE`, `GRAND`, and `GRAND_PLUS`, `GRAND-NARRATIVE-INTEGRITY` does not substitute for `MATHEMATICAL-STORY-INTEGRITY`. The former checks whether the narrative scale is earned and coherent; the latter checks whether the Introduction has actually discovered a mathematically specific parent program and transition above the local conjecture. Both must pass.
