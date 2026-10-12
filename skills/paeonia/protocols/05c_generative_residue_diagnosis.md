# Protocol 05c — Generative Residue Diagnosis

## Purpose

Detect prose that is mathematically correct but unnaturally uniform, over-signposted, repetitious, or administratively narrated.

This is a manuscript-quality protocol, not an AI-detector evasion protocol. The target is **authored mathematical prose**: language whose density and shape are explained by the mathematics.

## 1. Residue classes

Audit the manuscript for the following classes.

### GR-1 — Recurrent proof openings and closures
Flag repeated openings or endings when the same syntactic frame occurs across unrelated proofs.

Typical symptoms:
- repeated `We now ...`, `We next ...`, `We proceed ...` openings;
- repeated `This completes ...`, `This concludes ...`, `The desired result follows ...` closures;
- every proof beginning with a roadmap even when no roadmap is needed.

The remedy is not synonym substitution. Rewrite from the local mathematical action or remove the sentence.

### GR-2 — Empty signposting
A transition is empty when it announces movement without explaining mathematical movement.

Examples of empty functions:
- announcing that a lemma comes next;
- announcing that a case will now be considered;
- announcing that equations will be combined;
- repeating a section heading in sentence form.

Replace with the actual reason, obstruction, operation, or consequence—or delete.

### GR-3 — Formula paraphrase
Flag prose immediately after a display when it merely translates the displayed symbols into words.

A post-display sentence should do at least one of:
- identify a consequence;
- explain legality;
- interpret a mechanism;
- isolate parameter dependence;
- identify an equality/rigidity implication;
- move the argument to the next obligation.

Pure restatement is deleted.

### GR-4 — Template proof geometry
Flag collections of proofs that repeatedly exhibit the same administrative shape, for example:
`strategy sentence → Step 1 → Step 2 → Step 3 → closure sentence`, regardless of mathematical content.

Proof shape should reflect dependency shape.

### GR-5 — Flat information density
Flag when routine algebra, decisive estimates, endpoint passages, and rigidity arguments receive nearly identical prose density.

The desired asymmetry is mathematical:
- routine steps are compressed;
- structural steps are named;
- delicate steps are justified locally;
- surprising steps may receive one concise interpretation.

### GR-6 — Generic importance inflation
Review repeated use of adjectives or labels such as `important`, `crucial`, `fundamental`, `key`, `significant`, or `remarkable` when the mathematical role is not specified.

Prefer naming the role: `the estimate is uniform in ε`, `this is the only place convexity is used`, `the identity closes the equality case`.

### GR-7 — Administrative author voice
Flag prose in which the author is repeatedly the subject of non-mathematical actions:
- `we now turn to`;
- `we would like to show`;
- `we are going to use`;
- `we mention for completeness`.

First-person plural is retained for genuine mathematical actions.

### GR-8 — Repeated local transition tics
Use `tools/phrase_recurrence_audit.py` and `tools/transition_density.py` as diagnostics. Repetition triggers review, not automatic rewriting.

## 2. Diagnosis labels

For every flagged passage assign one action:
- `DELETE` — no mathematical content;
- `COMPRESS` — content useful but over-narrated;
- `MATHEMATICALIZE` — replace editorial transition by the actual mathematical relation;
- `KEEP` — repetition is standard, necessary, or mathematically functional;
- `RESTRUCTURE` — paragraph/proof geometry does not match dependency geometry.

Never use `SYNONYMIZE` as an action.

## 3. Whole-manuscript diagnostics

Run or approximate:
- phrase recurrence;
- sentence and paragraph rhythm;
- empty-signposting density;
- first-person opening concentration;
- display-followup redundancy;
- proof-opening/closure concentration;
- paragraph-role uniformity.

These are review signals, not target statistics. Do not force a manuscript to match a numerical human baseline.

## 4. Pass condition

`GENERATIVE-RESIDUE: PASS` requires:
- no dominant empty signposting template;
- no repeated proof geometry imposed without mathematical reason;
- no systematic display paraphrase;
- no obvious recurrence problem left unreviewed;
- visible information-density differences between routine and delicate mathematics;
- no random or cosmetic "humanization" operations.
