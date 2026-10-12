# v1.40.0 — exact-theorem proof-citation phase validation

Date: 2026-10-13.

## Change boundary

This release changes the skill's **proof-editing workflow**, not the mathematics of an identified article. Protocol 07a makes source-specific proof compression a formal Pass 6a before `ProofCoreGate`. Existing Protocol 07 owns source identity/version/claim verification; Pass 6a owns proof-unit coverage and the actual replacement decision. It works only where proof editing is authorized and never treats an unavailable, adjacent or possibly circular theorem as proof. Introduction 04u/04v fair-credit and grand-narrative capabilities are preserved.

## Checks performed

- Compatibility tests through v1.40 were run (earlier suite batches logged as PASS and remaining constituents rerun separately); new contract check passed 23 checks. The monolithic one-command release suite was attempted but timed out in the execution environment while running prior compatibility tests. Constituent results, rather than a successful single run, support the release.
- Behavioral decision fixtures: 186 legacy specs with corresponding executable good/bad fixtures; all 186 good choices accepted and all 186 incorrect choices rejected. Fourteen cases (173–186) are new and concern exact source locators, versions, class mismatches, parameter uniformity, equality, normalization, citation cycles, protected regions, access gaps, partial coverage, author credit, quota avoidance and stage routing.
- Structural `ProofCitationReplacementDossier` checker: 16 local unit tests passed, including rejection of absent theorem numbers, unspecified editions, missing hypothesis maps, missing conclusion translation, missing uniformity/independence declarations and unnumbered results without precise identification.
- Registry/contract compiler: 48 artifacts, 22 release gates, 186 behavioral fixtures; PASS.
- TeX/BibTeX citation inventory, writing-mode routes, proof explanation, and legacy tools were run as independent compatibility tests.

## Limitations

The dossier checker checks declared evidence **fields**, not the truth of their values. No original mathematical paper was supplied to this release test, no identified external theorem was independently read or applied, and no actual manuscript was shortened. The fixtures are structural/decision tests, not a blind demonstration of theorem-level citation accuracy or full logical verification. Live prior-work discovery and version-specific theorem checking happen when the skill is applied to a real manuscript with accessible primary sources.
