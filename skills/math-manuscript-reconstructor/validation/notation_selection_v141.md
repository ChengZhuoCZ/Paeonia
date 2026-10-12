# v1.41.0 — Semantic notation-selection release review

Date: 2026-10-13. Scope: **skill workflow**, not a rewrite of an identified mathematical article.

## New behavior and integration

- Protocol 02h actively selects notation from mathematical object roles, field expectations, theorem-facing readability, true structural relations, original-source continuity and real formulas. No universal symbol ownership, automatic novelty claims, aesthetic numeric scores or author-specific inventory cloning.
- It reuses the existing `NotationLedger` (`notation_selection` added to schema/template); there is **no new mandatory research dossier or state**. Pass 5a and the `NOTATION-CONSISTENCY` release gate use the new selection rules; local polishing remains edit-scope bounded.
- Pass 6a external-theorem imports may create a version-specific symbol crosswalk, which is **not** a substitute for checking the cited theorem's hypotheses, conclusion, endpoints, uniformity or normalizations.
- The read-only structural checker `tools/notation_choice_audit.py` checks declared object/symbol consistency, protected-symbol constraints, decision reasons and citation-mapping metadata. Its `--strict` route requires a locked notation selection in new nontrivial full reconstruction; legacy or draft ledgers can be examined without it.

## Checks executed in this release

- `test_v1_41_contract.py`: 23 required stage, scope, schema, gate, citation, provenance and backwards compatibility conditions **passed**.
- `test_notation_choice_audit.py`: 20 focused declaration tests and four strict-path checks (valid lock, missing selection, draft-only lock, no canonical objects) **passed**.
- Illustrative spectral-polygon notation choice: `notation_choice_audit.py --strict` **PASS**; this illustrates schema consistency, not spectral theory proof validity.
- 200 legacy regression specifications matched by 200 executable behavioral fixtures; all 200 expected-good candidates accepted, all 200 expected-bad candidates rejected. **Fourteen new fixtures** (187–200) cover field convention, user-fixed symbols, duplicate semantics, symbol families, indices, normalization, theorem readability, constant identity, imported results, protected editing scope and anti-decorative/anti-quantitative constraints.
- Contract registry checks: **48 artifacts, 22 release gates, 200 fixtures; PASS**. Existing v1.40 theorem-citation dossier checker tests (16), v1.39 research-credit contract, v1.38 author corpus contract, notation version contracts, tool/planner/routing/citation/proof/writing mode tests were executed independently and passed.
- Attempted the monolithic `tests/run_release_suite.py` command; it hit the environment's timeout during earlier compatibility programs. This is **not** counted as a monolithic suite success. The constituent tests were instead run separately in bounded batches. See build logs; do not conflate one-command completion with constituent coverage.

## Validation limits

- Fixture success tests deliberate decision rules, not the readability of arbitrary generated manuscripts. No blinded specialist reader evaluation was performed.
- A structural audit does not parse or understand all TeX, judge mathematical meaning/beauty, check whether author typography truly is best, or verify cited external theorem texts. Passing the illustration does not certify the mathematical assertion in its example.
- No original proof was shortened, no specific external theorem was newly verified, and no scientific priority claim was checked as part of this skill release. These remain paper-by-paper tasks.
