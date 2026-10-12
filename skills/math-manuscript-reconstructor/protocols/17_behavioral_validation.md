# Protocol 17 — Executable Behavioral Regression

## Purpose

A research-grade skill must test behavior, not merely the presence of protocol files or keywords.

Version 1.7 retains the human-readable regression specifications in `tests/regression_cases/` and adds executable fixtures in `tests/behavioral_cases/`.

## Fixture contract

Each behavioral case contains:

- a stable case ID;
- the legacy regression specification it implements;
- the owning release gate;
- one or more declarative assertions;
- a `good_candidate` that must satisfy the assertions;
- a `bad_candidate` that must violate at least one assertion.

The runner must demonstrate both directions:

- good candidate → `PASS`;
- bad candidate → `FAIL`.

A case that passes both candidates, fails both candidates, or is not executable is itself a test failure.

## What behavioral validation does and does not prove

The harness verifies deterministic contracts such as:

- ordering constraints;
- presence/absence of prohibited behaviors;
- classification decisions;
- architecture ownership;
- gate routing;
- appendix modularity decisions;
- style/source independence decisions;
- task-planning decisions.

It does **not** prove arbitrary mathematical arguments correct. Mathematical correctness remains a semantic reasoning responsibility of the proof and referee gates.

## Coverage rule

Every file in `tests/regression_cases/` must have corresponding **executable behavioral coverage** through a fixture with the same numeric ID. New regression specifications may not be added without executable coverage unless explicitly marked `SEMANTIC_ONLY` with a documented reason.

## Candidate fields are semantic outputs, not prose templates

Behavioral fixtures encode decisions such as:

```yaml
section_boundary_reason: METHOD_CHANGE
appendix_centrality: peripheral
followup_classification: DELETE
frontmatter_before_proof_gate: false
```

They do not prescribe exact manuscript sentences.

## Release requirement

`tests/test_behavioral_regressions.py` must pass from a freshly unpacked release artifact.

The validation report must state:

- number of legacy regression specs;
- number of executable behavioral fixtures;
- uncovered cases, if any;
- good-candidate passes;
- bad-candidate rejections.
