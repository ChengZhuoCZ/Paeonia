# v1.38.0 Author-Corpus Writing Supplement Validation

## Scope

This release adds a conditional author-associated corpus after a proof-bearing source is available and the writing mode/scope are resolved. It preserves the reader-first Introduction reconstruction, the conditional PDE branch, full reconstruction, bounded reconstruction, and local polishing.

## Contract checks

- One-time author request with an explicit `skip` path.
- Identity resolution before author-specific attribution or download.
- Legal open-access acquisition only; no access-control circumvention.
- Exact version, locator, local path and SHA-256 recording.
- Default four-paper corpus, with an admissible range of three to six.
- Selection by topic proximity, author-centrality evidence, recency, genre match and authorship control rather than prestige alone.
- Complete Introduction sampling plus functionally varied proof windows when mathematical-writing habits are in scope.
- Coauthored prose treated as author-associated evidence; no inference about who drafted a passage.
- Stable traits require recurrence across papers and preferably collaborator configurations.
- Style sources remain separate from novelty, priority and bibliography evidence.
- Existing `LOCAL_POLISH` prose takes precedence over corpus tendencies.
- Corpus quarantine and overlap protection before final realization.

## Executed validation

The 33 constituent release programs passed in bounded groups. This includes all legacy contract tests, tool checks, writing-mode and gate-repair tests, citation inventory, proof-explanation checks, and the v1.36, v1.37 and v1.38 contracts. The behavioral runner accepted all 162 positive fixtures and rejected all 162 negative fixtures. Contract consistency reported 29 states, 46 artifacts, 22 gates and 162 behavior fixtures with no errors or warnings.

The single wrapper `tests/run_release_suite.py` was not used as the sole evidence because the container imposed a cumulative process timeout during the long wrapper run. Its constituent programs were run separately in bounded groups instead. This is an execution-environment limitation, not a claim that an unobserved monolithic run passed.

Release packaging additionally checks YAML and JSON parsing, Python compilation, relative Markdown links, archive structure, and payload SHA-256 verification after re-extraction.

## Evidence limits

No author name or live paper corpus was supplied in this skill-development task. The release therefore validates the policy and executable routing but does not demonstrate real-world author disambiguation, PDF acquisition, prose extraction, or downstream Introduction quality on a particular scholar. Coauthorship makes individual stylistic attribution intrinsically uncertain; the protocol deliberately records corpus-associated patterns rather than asserting sentence authorship.

The supplement is not a style-cloning system. It stores abstract editorial decisions, not source sentences, phrase banks, distinctive tics or paragraph templates. Mathematical correctness, theorem scope, citation truth and the user's protected prose remain higher-priority constraints.
