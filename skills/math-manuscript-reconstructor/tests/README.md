# Regression and Release Suite

Run the complete suite from the package root:

```bash
python tests/run_release_suite.py
```

The suite runs legacy contract tests, tool checks, writing-mode routing, gate-repair consistency, executable behavioral fixtures, citation inventory tests, the v1.36 reader-first Introduction contract, the v1.37 conditional PDE Introduction contract, the v1.38 author-corpus supplement contract, and the v1.39 literature-first/grand-narrative contract.

## v1.36 Introduction coverage

Cases 139–143 check that:

- ordinary Introductions use `IntroductionCoreBrief` and one selected arc rather than every optional module;
- coherent paragraph functions may be integrated;
- a theorem may appear on page 2 when all preceding material is indispensable;
- noun-swappable generic prose is rejected;
- narrative amplification is conditional rather than automatic.

These are semantic contract tests. They do not score literary quality or replace theorem-aware editorial review.


## v1.37 PDE Introduction coverage

Cases 144–154 check that:

- PDE novelty is stated as a multi-axis result delta;
- incomparable frontier results remain a partial order;
- branching theorem architectures are not flattened;
- theorem latency follows prerequisite objects rather than prestige;
- assumptions have roles and, when useful, proof-stage locations;
- obstruction stacks are short and causal;
- decisive formulas are connected to the control and closure they provide;
- theorem, method, counterexample, and open boundaries remain distinct;
- global results connect a priori control to continuation;
- Introduction length follows explanatory burden;
- dual-audience bridges use an object dictionary rather than parallel surveys.

The PDE extension remains conditional and is stored inside `IntroductionCoreBrief`; it is not a second mandatory planning artifact.

## v1.38 author-corpus supplement coverage

Cases 155–162 check that:

- under v1.42, no author/style selection question is initiated by the skill; a proactively supplied corpus is optional;
- ambiguous names are disambiguated instead of guessed;
- retrieval uses legal open-access, version-locked copies;
- a representative corpus balances topic proximity, centrality, recency, genre and authorship control;
- coauthored writing is attributed cautiously;
- style evidence remains separate from literature and citation evidence;
- a `LOCAL_POLISH` baseline has priority over corpus tendencies;
- no phrase bank, persona imitation or paragraph-sequence copying is permitted.

These tests verify routing and evidence discipline. They do not perform a live scholarly search or establish that a corpus uniquely identifies an individual's prose.

## Executable behavioral regression

Every numbered specification in `tests/regression_cases/` must have a corresponding YAML fixture in `tests/behavioral_cases/`. The runner must accept the good semantic candidate and reject the bad candidate. Missing fixture coverage is a release failure.

## Other coverage

`test_execution_planner.py` checks that narrow workflows do not trigger irrelevant full-manuscript passes. `test_gate_repair_routes.py` checks gate ownership, rollback, repairs, invalidations, and re-audits. `test_contract_consistency.py` compiles version identity, state vocabulary, artifact and gate registries, audit schemas, behavioral coverage, manifest tools/tests, and release invariants.

The suite does not prove mathematical correctness of arbitrary manuscripts.

## v1.39 literature/credit/program narrative coverage

Cases 163–172 check outward literature discovery rather than inherited-BibTeX-only review, positive credit for exact prior achievements, multi-axis result comparison, evidence-grounded larger mathematical stories, refusal to inflate unsupported stories, offline/priority discipline, local-polish preservation, recency and parallel work, no arbitrary citation quotas, and separation of author-style and mathematical-literature evidence. `test_v1_39_contract.py` checks the routing and the compact dossier. These are structural and behavioral *fixtures*; they cannot prove actual search completeness, correctness of a new paper's citations, or the quality of generated prose.
