# Abstract calibration, v1.31.0 application and v1.31.1 feedback

- Mode: LOCAL_POLISH, continuing the accepted minimal-edit scope.
- Baseline SHA-256: `6f46a7d33b43a18f16d896290341da317f27bfdc9a48eeb90f519e69ed75dcbf`.
- User-reference SHA-256: `1d4bb78b4a88b101fca4bd5ed575f3a8c7bc18af24353f396ff7eab4ded70cea`.
- Initial v1.31.0 skill archive SHA-256, frozen before application: `c4acb405f828ea3f62346036e614a01f35c3e52c68cc79c043ae874129f98ebc`.
- Actual candidate SHA-256, frozen before comparison: `df59c301ecda9952f1ed5256d97aa1da2dbebac97c5d094d41eb1b25c77407a2`.
- Selected manuscript SHA-256: `70de4605beadcb61d2355ce14c0a9927ff89811da9fe5557b20a31c1fcd9349b`.

The 141-word trial splits an already effective encoding sentence and repeats the full equality configuration. The selected 124-word abstract restores those parts of the 112-word user reference, retains a directional clarification for the quadratic lower bound, and names the implication from minimality to zero defect. Four reference sentences remain verbatim. Counts are whitespace-separated descriptions, not quality metrics.

The paper application also repairs two Introduction interfaces: subtracting the common cubic leading term in the first bootstrap, and separating coefficient control from Taylor-error control below the cutoff. Their source evidence is `cor:first-localization`, `eq:localization-044`, `lem:vanishing-defect`, and `eq:exact-constraints-020`–`021`. This uses existing Protocol 04p as well as the new abstract protocol. No new theorem, proof argument, rate or citation is added.

Deterministic manuscript checks: reversing the three recorded replacements recovers the full baseline; the protected Introduction before the original fourth-page marker, the complete proof body, all display formulas and citation commands are unchanged. PDF: 64 pages, 33 cited references, no compilation warnings or undefined references. Abstract and Introduction pages 1–5 rendered and visually inspected.

Package checks: Skill Creator quick validation PASS; all 29 existing release-suite programs PASS (see [log](release_suite_v1311.log)). These tests check existing contracts and tools, not the new natural-language guidance's generative quality. Changed documentation links, versions, ZIP paths and file hashes are checked during packaging.

This is a same-agent, context-aware editorial application with one paper and a reference known in advance. It is not blind generation, independent reader validation, an independent application of v1.31.1, or proof certification. The [case profile](../profiles/causal_abstract_calibration.md) stores decision evidence, not reusable source prose.
