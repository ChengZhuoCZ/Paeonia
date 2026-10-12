# Protocol 02f — Duplicate-Symbol Audit

## Purpose

Check one thing: **the same recurring mathematical symbol must not be assigned to two different recurring objects in the manuscript.**

No symbol is reserved in advance. `\Delta`, `E`, `P`, `Q`, `\lambda`, and every other symbol are treated in exactly the same way.

## 1. Audit domain

The audit applies to the formal recurring notation recorded in `NotationLedger.canonical_objects`.

It does **not** audit ordinary local dummy variables such as `x`, `y`, `i`, `j`, `k`, or a temporary integration variable that is introduced and discharged inside one local argument. Those variables are intentionally outside `canonical_objects`.

## 2. Exact rule

Build the table

```text
visible symbol  ->  recurring mathematical object
```

For every exact visible symbol:
- if it maps to one object, PASS;
- if repeated rows map to the same object, PASS;
- if it maps to two or more different objects/meanings, FAIL and rename one of them.

The check is manuscript-wide for recurring notation. Do not exempt two recurring objects merely because they occur in different sections.

## 3. Examples

Allowed:
- `\Delta` denotes one discriminant throughout the paper;
- `\Delta` denotes one Laplace operator throughout the paper;
- `E` denotes one energy throughout the paper;
- different proofs reuse `x` as a local dummy variable, because `x` is not a recurring canonical object.

Rejected:
- `\Delta` denotes the Laplacian in one part and a deficit in another;
- `E` denotes the energy and later an exceptional set;
- `P_N` denotes an operator and elsewhere a polygon family.

The reason for rejection is simply **duplicate symbol assignment**, not any preferred meaning of the symbol.

## 4. Repair

When a duplicate is found:
1. keep the symbol for the object whose notation is more standard or already more deeply integrated;
2. rename the other recurring object with a plain unused symbol or a semantic subscript;
3. update theorem statements, proofs, Introduction, appendices, and cross-references consistently;
4. rerun the duplicate-symbol audit.

## 5. Final release condition

`NotationLedger` must satisfy:

```text
for every recurring visible symbol S:
    number of distinct recurring meanings assigned to S <= 1
```

No other semantic policy is implied by this protocol.
