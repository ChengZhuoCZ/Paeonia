# Protocol 08 — Adversarial Referee (Explicit Verification Only)

This protocol is **off by default** in `trusted_source` writing. Run it only when the user explicitly asks for correctness checking, referee simulation, stress testing, mathematical repair, or independent verification.

When activated, read only the reconstructed manuscript. Pretend the project history is unavailable.

## Correctness questions

- Is every symbol defined before nonlocal use?
- Are hypotheses stable across theorem restatements?
- Do claimed uniform constants have stated dependence?
- Does each external theorem match the exact regime used?
- Are endpoint cases covered?
- Does every case split close?
- Are equality cases propagated rather than asserted?
- Is a “standard argument” actually standard in this setting?

## Exposition questions

- Can the main mechanism be identified within one reading?
- Are there too many tiny lemmas?
- Is a technical appendix hiding a conceptual gap?
- Does the introduction accurately predict the proof?
- Does engineering history leak into the narrative?

## Severity

`BLOCKER`: invalidates theorem or submission claim.
`MAJOR`: substantial gap/ambiguity.
`MINOR`: local fix.
`STYLE`: exposition only.
