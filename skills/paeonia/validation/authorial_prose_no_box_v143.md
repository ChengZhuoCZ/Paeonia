# Paeonia v1.43.0 — Authorial Prose and No-Box Validation

Date: 2026-10-13 (Asia/Tokyo). Scope: **skill package only**; no user manuscript was revised or compiled as part of this release.

## Executed checks

- Entire `python tests/run_release_suite.py` completed with `RELEASE_SUITE_PASS` after the final scanner patch (see `release_suite_v143.log`).
- `python tests/test_v1_43_contract.py` passed 25 targeted checks, including clean/comment/verbatim sources, nested-input detection, boxed macros, box environments, dedicated packages, empheq boxing, constructor macros, missing local files, integration with the older manuscript static gate and advisory prose diagnostic behavior.
- Contract compiler returned `PASS`: 29 canonical states, 48 registered artifacts, 23 release blockers and 222 legacy/executable behavioral cases, with zero structural errors or warnings.
- Behavioral regression runner returned `BEHAVIORAL_PASS`: 222 good decisions accepted and 222 contrasting bad decisions rejected.
- `tests/test_tools.py` passed, and Python source compilation and linked-document path checks succeeded.

## Exactly what these tests establish

The tests verify the package routes, the no-box static checker, the inclusion rules, the declared release contract, and selected good-versus-bad editorial decisions. `NO-BOX-TYPESETTING` is a **new separate hard gate**, applicable even if TeX compilation was not requested. The prose reviewer emits `REVIEW` locations without pretending to infer author identity or an "AI percentage".

## Limits and release claims

- No manuscript-specific PDF was supplied for this release; **no visual PDF inspection or real-manuscript readability certification** was performed. The static checker may miss novel user macros, class-file drawing styles or box-like graphics, and may conservatively fail on a missing local `\\input`.
- No model-independent human-authorship classifier exists in this package. Natural prose and accurate scientific prose must be judged editorially and mathematically; the tool does not claim to drive an AI detector below a numerical threshold.
- The package has not independently established the correctness of any mathematical theorem, the applicability of an external paper's proof, or the originality of any as-yet-unsupplied manuscript.
- `LOCAL_POLISH` and explicitly protected regions retain their boundaries. An inherited protected box blocks final manuscript release rather than authorizing silent edits.
