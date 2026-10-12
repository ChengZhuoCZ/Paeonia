# Protocol 02g — Empirical Changfeng Gui Corpus Notation Prior

## Purpose

Use notation habits distilled from a multi-paper Changfeng Gui coauthored corpus as a **soft selection prior** when several collision-free symbols would be mathematically equivalent.

The evidence source is `profiles/changfeng_gui_notation_corpus.yaml`; the interpretation report is `profiles/changfeng_gui_notation_distillation_report.md`.

This protocol never imitates a complete symbol inventory from one paper.

## Hard priority

Apply notation decisions in this order:

1. `Duplicate-Symbol Audit`: one recurring visible symbol may not denote two recurring objects.
2. Explicit user notation requirements.
3. Strong field/problem conventions.
4. Clear collision-free notation already present in the supplied proof when preserving it reduces translation debt.
5. The Gui corpus prior for notation still genuinely undecided.

No corpus preference may defeat a higher-priority constraint.

## Corpus-conditioned preferences

### A. Direct symbol before typographic hierarchy

Prefer an ordinary Roman/Greek symbol that directly names the object over a new decorative alphabet. This is especially strong for unknowns, geometric objects, parameters, operators, and spectral data.

### B. Generic-to-specific geometry

It is often clearer to retain `\Omega` for a generic PDE domain, then use a meaningful initial after specialization:

- triangle `T`;
- quadrangle `Q`;
- kite `K`;
- vertices `P_i`;
- center `C`.

These exact letters are examples of a strategy, not reserved assignments.

### C. Families by relation

If objects form one mathematical family, preserve a common base symbol and encode the relation through:

- indices: `P_i`, `\mu_j`, `a_k`;
- deformation parameters: `T^t`;
- symmetry labels: e.g. `s/a` when stable;
- genuine threshold modifiers: `h_0,h_1,\widehat h,\widetilde h`.

Never add a modifier merely to make symbols look different.

### D. Semantic abbreviations

Stable geometric/combinatorial roles may receive short semantic labels, as in longest/medium/shortest side labels. Use this only when it reduces repeated prose and remains unambiguous.

### E. Spectral notation follows the local problem

Use field-standard spectral notation first. In Neumann/mixed boundary work, `\mu` and `\lambda` may usefully separate spectral families, but the skill must not impose this mapping in unrelated subjects.

### F. Simplify after a genuine reduction

When geometry reduces a problem to one active coordinate, simplify the local variable and compress repeated analytic expressions into short derived symbols if this materially shortens the proof. Keep the relationship explicit at first definition.

### G. Introduce notation near first mathematical use

Do not front-load a glossary unless notation density genuinely requires it. Define local geometric and analytic objects immediately before the theorem, lemma, or argument that needs them.

## Typography: corpus evidence vs user house style

The corpus is mixed: it contains semantic calligraphic sets and also examples of `\mathfrak` and calligraphic functional notation. Therefore this protocol does **not** claim that decorative alphabets are absent from Gui papers.

The user has a separate house style:

- avoid `\mathscr`;
- avoid `\mathfrak` unless unavoidable in imported standard notation;
- keep `\mathcal` sparse and semantic.

This user preference has higher priority than the corpus typography evidence.

## Anti-imitation rule

Do not reproduce:

- a paper's complete symbol table;
- the exact order in which one source paper introduces symbols;
- an exact sequence such as `T,u,\mu_j,L,M,S,R_p` merely because it appears in a reference.

Transfer only the stable strategy: **direct names, semantic initials, related-family modifiers, standard field notation, and local simplification.**

## Audit order

1. `tools/duplicate_symbol_audit.py` — blocking;
2. `tools/notation_architecture_audit.py` — structural;
3. `tools/gui_notation_prior_audit.py` — advisory author-corpus fit.

A corpus-prior warning is never allowed to override a collision-free, user-requested, field-standard choice.
