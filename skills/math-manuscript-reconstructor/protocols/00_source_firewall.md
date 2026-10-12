# Protocol 00 — Source Firewall

## Purpose

Prevent a supplied manuscript from becoming the hidden template of the final article.

## Extraction whitelist

Extract only:
- claims and exact assumptions;
- definitions and normalization;
- formulas and proof-critical calculations;
- dependency relations;
- proof mechanisms;
- equality/rigidity logic;
- constants and uniformity ranges;
- external inputs and provenance;
- counterexamples, excluded regimes, and endpoint behavior.

## Quarantine blacklist

Do not transfer by inertia:
- section tree;
- theorem numbering;
- names like “Stage”, “Module”, “Block”, “FCW”, “Step 5B”, or project-specific labels;
- source prose;
- repeated transition sentences;
- ordering that reflects discovery history rather than exposition logic.

## Firewall procedure

1. Parse source into semantic units.
2. Assign new semantic IDs.
3. Build the ledger and dependency graph.
4. Write a source-discard summary.
5. Design a new architecture without looking at source headings.
6. Draft from the ledger.
7. Re-open source only for verification.

## Violation test

If one can align the final section tree with the source section tree nearly one-to-one, assume firewall failure unless the structure is mathematically forced. Document the justification for any unavoidable alignment.
