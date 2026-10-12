# v1.36.0 Reader-First Introduction Validation

## Scope

This release changes the skill package, not a manuscript. It replaces the accumulated default Introduction stack with a compact core-and-reader-contract route while retaining deeper modules behind explicit triggers.

The redesign addresses a structural failure rather than a vocabulary problem. In v1.35, several independently useful layers could all become active in one ordinary task: grand-narrative planning, mathematical-story discovery, narrative ambition, scientific context, paragraph-role planning, a factual draft, narrative amplification, and editorial-impact review. Their cumulative effect could produce repeated widening and narrowing, role-filled paragraphs, and technically complete but generic prose.

## New ordinary route

`closed theorem truth → IntroductionCoreBrief → one selected narrative arc → direct prose → seven-question reader contract → precise revision`

The core brief records the exact question, benchmark, pre-paper frontier, theorem, obstruction, conceptual hinge, unlocked control, meaning, limits, and essential literature claims. It is a composition aid, not a paragraph template.

The older Introduction artifacts are conditional:

- `MathematicalStoryLedger` for an operative parent program or scale/category transition;
- `ScientificContextLedger` for a model, mechanism, scaling, or regime that changes problem legibility;
- `NarrativeAmbitionLedger` and `EditorialImpactAudit` for verified high-stakes positioning or a demonstrated under-positioning defect;
- `IntroductionNarrativeLedger` and `IntroductionParagraphPlan` for unusually complex multi-theorem, literature-heavy, or model-driven Introductions;
- narrative amplification only for a specific evidence-backed omission.

## Contract checks

The release was checked at the package, compatibility, and behavioral levels.

- Release suite: **PASS**, 31 programs, executed in three batches because the working container imposes a short per-command cap.
- Core package test: 152 required files and 51 contract checks.
- v1.36 Introduction contract: 12 checks.
- Executable behavioral regressions: 143 specifications, 143 fixtures, 143 good candidates accepted, and 143 bad candidates rejected.
- Contract compilation: 29 states, 45 registered artifacts, 22 release blockers, 143 behavioral fixtures, zero errors, zero warnings.
- Proof-explanation tests: one valid graph plus 12 invalid graph/evidence cases and scope guards.
- Citation inventory: 23 unit tests across the two suites reported by the test runner.
- Python bytecode compilation: 62 Python files compiled successfully.
- Data parsing: 188 YAML files and 17 JSON files parsed successfully.
- Relative Markdown links: 52 checked, none missing.

Raw logs are stored in:

- `validation/release_suite_v136_batch1.log`;
- `validation/release_suite_v136_batch2.log`;
- `validation/release_suite_v136_batch3.log`;
- `validation/contract_consistency_v136.json`.

## New behavioral cases

Cases 139–143 enforce five decisions that were previously under-specified:

1. ordinary Introductions use the compact core and one selected arc rather than all optional modules;
2. benchmark, literature, and obstruction may be integrated when they create one coherent information change;
3. a theorem may naturally appear on page 2 when all preceding material is indispensable;
4. a paragraph that survives a subject-noun swap is too generic;
5. an accurate restrained draft is not automatically broadened by a second amplification pass.

## Compatibility

Legacy grand-narrative, scientific-context, mathematical-story, and editorial-positioning modules remain available. The release retains the older contract vocabulary needed by existing workflows, but Protocol 04, the state machine, artifact registry, manifest, and repair routing now agree that these modules are conditional.

## Limits

The regression suite validates declared contracts and selected semantic decisions. It cannot establish that every generated Introduction is elegant, field-appropriate, or independently comprehensible. Stronger evidence requires replaying the released skill on several representative manuscripts—a focused technical paper, a genuinely program-level theorem, and a model-driven paper—and comparing frozen candidates with readers who did not construct the prompts.
