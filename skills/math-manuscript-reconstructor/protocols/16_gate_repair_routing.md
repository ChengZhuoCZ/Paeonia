# Protocol 16 — Gate → Repair → Re-audit Routing

## Purpose

A release gate is not merely a red light. Every blocker must have an explicit owner, rollback point, repair vocabulary, invalidation set, and re-audit path.

The authoritative routing table is `registry/gates.yaml`.

## Required behavior on gate failure

For each failed blocker:

1. identify the gate ID;
2. locate its `owner_state`;
3. roll back to `rollback_to` or earlier if the evidence requires it;
4. apply only repairs listed as semantically admissible for that gate;
5. mark downstream artifacts in `invalidates` as stale;
6. rebuild stale artifacts from their authoritative upstream source;
7. re-run every gate in `re_audit`;
8. preserve the original failure and repair history in `RepairRouteReport`.

## Repair hierarchy

Repairs must occur at the earliest layer that actually owns the defect.

Examples:

- wrong parameter range → `LEDGER_LOCK`, not sentence editing;
- missing proof bridge → `PROOF_GRAPH/PROOF_CORE`, not Introduction prose;
- source-like section order → `MANUSCRIPT_ARCHITECTURE/SECTION_NARRATIVE`, not synonym replacement;
- appendix proof debt → `WHOLE_PAPER_NARRATIVE`, returning central logic to the body;
- repeated empty signposting → `RESIDUE_DIAGNOSIS/AUTHORIAL_DECISION`;
- notation collision → notation planning/normalization, followed by local semantic re-check;
- invented citation → `CITATION-INTEGRITY`, with the unsupported claim removed or verified.

## Repair scope

Prefer **minimal semantic rollback** rather than global regeneration, but never preserve downstream prose whose upstream semantic source has changed.

A repair route may invalidate:

- theorem framing;
- proof paragraphs;
- Introduction claims;
- Abstract claims;
- appendix imports;
- notation definitions;
- cross-references;
- style realization around changed mathematical units.

## Forbidden repair patterns

- repairing a semantic gate by prose-only smoothing;
- repairing style recurrence with random synonyms;
- keeping a stale Introduction after the theorem changed;
- patching an appendix citation when the actual issue is proof debt;
- declaring a gate PASS without re-auditing dependent gates;
- repairing a source-independence violation by merely renaming headings.

## Multi-gate failures

When several gates fail, repair in upstream order. A useful priority is:

1. `MATH-SEMANTICS`
2. `PROOF-CLOSURE`
3. `PROOF-CORE-ORDER`
4. citation / external-input correctness
5. architecture and independence gates
6. notation / LaTeX integrity
7. authorial-naturalization gates

After an upstream repair, discard downstream failure diagnoses that depended on stale text and recompute them.

## Repair report

Record:

```yaml
gate:
root_cause:
owner_state:
rollback_to:
repairs_applied:
invalidated_artifacts:
reconstructed_artifacts:
re_audit:
final_status:
```

Use `tools/gate_repair_router.py` to inspect or validate deterministic routes.
