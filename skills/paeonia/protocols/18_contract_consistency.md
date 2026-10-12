# Protocol 18 — Contract, Artifact, and Schema Consistency

## Purpose

As the skill evolves, the constitution, state machine, artifact list, schemas, templates, gate list, manifest, and tests must not drift apart.

Version 1.7 introduces a package-level consistency compiler. The source-of-truth registries are:

- `registry/artifacts.yaml`
- `registry/gates.yaml`

## Compiler checks

`tools/contract_consistency.py` must verify at least:

### Version identity
- `VERSION`, `SKILL.md`, and `MANIFEST.json` agree.

### Artifact closure
- every required artifact in `registry/artifacts.yaml` has a known owner state;
- every schema/template path declared by the registry exists;
- every artifact marked as a release report is represented in the output/gate contracts;
- conditionally produced style artifacts are explicitly conditional rather than silently absent.

### Gate closure
- every blocker in `registry/gates.yaml` appears in the submission gate protocol;
- every registered gate has owner state, rollback state, repair policy, invalidation set, and re-audit list;
- every registered audit key exists in `schemas/audit_report.yaml`;
- every submission-gate template line corresponds to a registered blocker.

### State closure
- every artifact owner/rollback state exists in the execution state machine;
- every state named by the adaptive planner is recognized;
- proof-first ordering constraints remain valid.

### Behavioral-test closure
- every legacy regression spec has an executable fixture;
- every fixture references a registered gate.

### Manifest closure
- listed tests and tools exist;
- v1.7 tests are included in the manifest.

## Failure policy

Any consistency failure is a release blocker. Do not patch the generated package around the compiler. Fix the source contract or registry and re-run all tests.

## Why this matters

A manuscript skill with excellent local rules can still fail operationally if one layer says a gate exists while another layer cannot report or repair it. The consistency compiler converts this kind of version drift from a latent defect into an immediate test failure.
