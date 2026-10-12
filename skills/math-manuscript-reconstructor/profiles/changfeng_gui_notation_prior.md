# Changfeng Gui Empirical Notation Prior

## Status

`soft_prior`, version 2, distilled from a multi-paper Changfeng Gui coauthored corpus spanning nonlinear PDE, conformal geometry, spectral geometry, Beckner/GJMS inequalities, and fluid equations.

This profile is **not** a symbol template and not an attribution claim about which coauthor chose a specific letter. Runtime priority is:

1. manuscript-wide duplicate-symbol integrity;
2. explicit user notation requirements;
3. established notation of the problem and field;
4. clear, collision-free notation already present in the supplied proof;
5. this corpus prior only for notation choices that are still genuinely open.

The evidence inventory is `profiles/changfeng_gui_notation_corpus.yaml`.

## What the corpus actually supports

### 1. Primary mathematical objects are named directly

Across the inspected papers, the main unknown is typically an ordinary lower-case letter, most often `u`; a generic domain is naturally `\Omega`; concrete geometric objects often receive a meaningful capital initial such as triangle `T`, quadrangle `Q`, or kite `K`; vertices are naturally `P_i`.

The important principle is not the exact letter. It is **direct semantic naming without an extra typographic layer**.

### 2. Generic and concrete objects are allowed to have different symbols

A recurrent pattern is:

- `\Omega` for a generic domain in the PDE setup;
- `T`, `Q`, or `K` once the argument specializes to a triangle, quadrangle, or kite.

This is preferable to forcing one symbol to serve every geometric level.

### 3. Related families stay visibly related

Use a shared base symbol with meaningful indices or modifiers whenever the mathematics says the objects belong to one family. Corpus examples include:

- `\mu_j`, `\lambda_k`, `P_i`;
- `T^t` for a domain deformation;
- `h_0,h_1,\widehat h,\widetilde h` for related thresholds;
- `\mu^s,\mu^a` for symmetric/antisymmetric spectral quantities;
- `a_k` for coefficients in a basis expansion.

The modifier must encode a real relation. Do not add a hat, tilde, superscript, or font merely for visual variety.

### 4. Semantic abbreviations are useful when they reduce prose

The triangle paper uses side labels `L,M,S` for longest, medium, and shortest sides and uses those labels in mixed-boundary eigenvalue notation. This supports a general preference for short semantic labels when the relation is stable throughout a section or paper.

### 5. Spectral notation follows the problem, not a universal house alphabet

In the Neumann-eigenfunction papers, `\mu_j` is used for Neumann eigenvalues and `\lambda_1^{\Gamma_D}` or related `\lambda` notation for mixed/Dirichlet quantities. In other subjects, `\lambda_k` may denote polynomial/spectral eigenvalues. Therefore:

- use the field-standard spectral letter first;
- keep the distinction stable once chosen;
- use superscripts/subscripts to expose boundary condition, mode, or symmetry when useful.

Do **not** impose `\mu = Neumann` and `\lambda = Dirichlet` outside a context where that convention is helpful.

### 6. Coordinate reduction should simplify notation

In the axially symmetric Beckner paper, the ambient coordinate `\xi_1` is renamed `x` after reduction to one dimension, and a derived quantity is introduced as `G(x)=(1-x^2)u'`. This is a useful general habit:

- keep ambient notation while geometry is active;
- after a genuine reduction, rename the active coordinate to a simple local variable;
- introduce a compact derived symbol when it is used repeatedly and carries a stable analytic meaning.

### 7. Standard operators and spaces remain standard

Use conventional notation such as `\Delta`, `\nabla`, `P_4`, `\mathbb R^n`, `\mathbb S^N`, Sobolev spaces, and standard measure notation. A named operator family is naturally a plain capital plus an index or parameter when that is the field convention.

### 8. Named sets may use calligraphic notation, but the corpus is mixed

The corpus contains genuine set notation such as `\mathcal Z(u)` for a nodal set and `\mathcal C_{nv}(u)` for non-vertex critical points. It also contains typography such as `\mathfrak L` and `\mathcal J_\alpha` in a Beckner paper.

Therefore **the corpus does not justify the claim that Changfeng Gui papers avoid calligraphic or fraktur notation altogether**.

For this skill, the user's house style is stricter than the corpus:

- `\mathscr`: avoid;
- `\mathfrak`: avoid unless unavoidable in imported standard notation;
- `\mathcal`: use sparingly for a genuinely named set/class/space when it materially improves readability.

This is a **user-style override**, not an author-attribution claim.

## Object-class preferences when notation is undecided

These are soft suggestions only.

### Unknowns and auxiliary functions

- scalar solution/eigenfunction: `u`;
- comparison/reflected/secondary functions: `v,w`;
- reduced or derived repeated quantity: a short plain capital/lower-case symbol such as `G`, chosen from its analytic role.

### Domains and geometry

- generic domain: `\Omega`;
- triangle/quadrangle/kite: `T,Q,K` when natural and collision-free;
- vertices: `P_i`;
- center: `C` when unambiguous;
- generic points: `p,q,x,y`;
- basis directions: `e_i`.

### Spectral and PDE notation

- differential operators: standard field notation;
- operator family: plain capital plus index/parameter, e.g. `P_N`;
- eigenvalue families: `\mu_j` or `\lambda_j` according to the problem;
- mixed-boundary variants: semantic superscript/subscript rather than a new font;
- parameters: conventional Greek letters such as `\alpha,\beta,\lambda,\mu,\rho,\varepsilon` when available.

### Deformations, thresholds, and variants

- deformation family: a common base symbol with a deformation parameter, e.g. `T^t`;
- related thresholds: `h_0,h_1,\widehat h,\widetilde h` only when the modifiers correspond to distinct mathematical roles;
- symmetry variants: semantic labels such as superscripts `s/a` when the distinction is stable.

## Collision rule

The corpus prior never creates a duplicate recurring symbol. If a preferred symbol is already assigned, choose the next clear conventional symbol. `protocols/02f_duplicate_symbol_audit.md` has absolute priority.

## Anti-imitation rule

Never copy the exact symbol inventory of an individual Gui paper. The transferable signal is the notation strategy:

**direct symbols, semantic initials, related-family modifiers, standard field notation, and local simplification after reduction.**
