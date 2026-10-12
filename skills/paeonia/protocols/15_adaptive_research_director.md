# Protocol 15 — Optional Research Director and Execution Planning

## Purpose

Version 1.8 keeps this planner as an **optional governance mode**. It is not part of the default manuscript-writing interaction. Use it only when the user explicitly asks for orchestration, recovery of a complex partial project, audit scheduling, or package-level workflow control.

The director is a scheduler, not an author. It decides *which validated operations are required next*; it does not change theorem semantics, invent missing mathematics, or waive release blockers.

## Artifacts

When this optional mode is activated, create:

1. `ResearchDirectorBrief`
2. `ResearchDirectorAdvice`
3. `ExecutionPlan`

The advice is provisional. Only the deterministic admissibility filter makes the final execution plan operative. The plan records `director_advice_review.accepted` and `director_advice_review.rejected` so unsafe scheduling advice cannot disappear silently.

## ResearchDirectorBrief

Record at least:

- workflow class;
- requested deliverables;
- mathematical-source availability;
- style-corpus availability;
- whether a closed proof already exists and how that closure was verified;
- whether manuscript prose must be produced;
- whether front matter is requested;
- whether the task is audit-only;
- whether mathematical repair is authorized;
- known blockers;
- reusable locked artifacts from a prior run;
- target audience and venue constraints if supplied.

## Workflow classes

The planner recognizes at least:

- `LOCAL_POLISH`
- `SCOPED_RECONSTRUCTION`
- `FULL_MANUSCRIPT_RECONSTRUCTION`
- `PROOF_BODY_ONLY`
- `FRONTMATTER_FROM_VERIFIED_PROOF`
- `ARCHITECTURE_ONLY`
- `STYLE_DISTILLATION_ONLY`
- `AUTHORIAL_NATURALIZATION_ONLY`
- `SUBMISSION_AUDIT_ONLY`
- `LATEX_NOTATION_ONLY`

Resolve writing mode and editable/protected scope under [Protocol 00](00_writing_modes.md) before selecting a workflow. Local polishing requires an editing baseline, not a new proof gate. Selected-region reconstruction requires supplied mathematics and explicit bounded scope. Use one plan per region for mixed modes. Advice cannot add states outside either bounded route. Legacy explicitly verified-proof workflows retain their existing prerequisites.

## ResearchDirectorAdvice

The advisory layer ranks work by:

1. critical-path necessity;
2. blocker risk;
3. semantic invalidation radius;
4. information gain;
5. expected probability of closing the requested deliverable;
6. reuse of already locked artifacts;
7. cost of redoing downstream prose if an upstream assumption changes.

The advice may recommend skipping passes, but it must state why each skip is safe.

## Deterministic admissibility filter

The final `ExecutionPlan` MUST satisfy all of the following.

### Invariants that cannot be skipped for source-based reconstruction

If this optional mode is active and mathematical source material is being transformed into manuscript prose, require:

`TASK_CONTRACT → EXECUTION_PLAN → INGEST → EXTRACT → LEDGER_LOCK → SOURCE_QUARANTINE`

If proof prose is being produced from source material, additionally require:

`PROOF_GRAPH → PROOF_CORE → PROOF_CORE_GATE`

If a style corpus is supplied and manuscript prose is being produced, require style extraction and quarantine before `PROOF_CORE`.

### Front-matter admissibility

`FRONTMATTER` is admissible only when either:

- the current run has `PROOF_CORE_GATE: PASS`; or
- workflow is `FRONTMATTER_FROM_VERIFIED_PROOF` and a prior `ProofCoreGateReport` with verified closure is supplied as reusable input.

Never infer proof closure from polished prose alone.

### Audit-only admissibility

An audit-only workflow may skip drafting states, but it must not claim semantic or proof-closure gates without the artifacts required to evaluate them.

### Naturalization admissibility

`AUTHORIAL_NATURALIZATION_ONLY` may operate only on a mathematically frozen manuscript with an available semantic checksum or equivalent locked mathematical specification. If naturalization appears to require new mathematics, route back to the proof layer.

### Style optionality

Style fingerprinting is an optional prior. Universal manuscript-architecture rules remain active without a style corpus. Absence of a style corpus may skip corpus-distillation states, but it never disables mathematics-driven paragraph, section, or whole-paper architecture.

### Skip rule

Every skipped pass must record:

- `reason`;
- `prerequisites_satisfied_elsewhere` if applicable;
- `risk_if_wrong`;
- `artifacts_not_produced`;
- `gates_that_become_unavailable`.

A silent skip is invalid.

## ExecutionPlan fields

Use `schemas/execution_plan.yaml`. At minimum include:

- workflow;
- required states in order;
- conditional states;
- skipped states with reasons;
- artifact inputs;
- artifact outputs;
- blocker owners;
- release gates applicable to this task;
- reusable artifacts and their validation status;
- revalidation scope if a reused artifact changes.

## Minimality objective

Among admissible plans, prefer the plan that minimizes unnecessary work **without increasing semantic risk**. Do not maximize the number of passes executed merely because the full pipeline exists.

## Forbidden planner behavior

- skipping `LEDGER_LOCK` because the source “looks correct”;
- writing an Introduction before proof closure because the user asked for speed;
- skipping style extraction while still claiming fidelity to a supplied style corpus;
- treating a previous manuscript as a reusable `MathLedger` without verification;
- using cost as a reason to waive a blocker;
- running all passes automatically when the task clearly requests only a narrower artifact.
