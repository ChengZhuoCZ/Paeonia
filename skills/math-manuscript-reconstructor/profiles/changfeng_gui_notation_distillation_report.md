# Changfeng Gui Notation Distillation Report — Empirical v2

## Purpose

This report records the evidence used for the runtime notation prior. It is deliberately more conservative than a style-imitation profile: the papers are coauthored, many exact letters are dictated by subject convention, and typography varies across papers. The goal is to isolate **cross-paper notation habits that remain useful after those caveats**.

The machine-readable inventory is `profiles/changfeng_gui_notation_corpus.yaml`.

## Corpus inspected

Representative arXiv papers include:

- 1605.06481 — *The Sphere Covering Inequality and Its Applications* (2016).
- 1709.02474 — *Non-axially symmetric solutions of a mean field equation on S^2* (2017).
- 1812.09994 — *The sphere covering inequality and its dual* (2018).
- 1905.10842 — *Remarks on a mean field equation on S^2* (2019).
- 2109.13390 — *Improved Beckner's inequality for axially symmetric functions on S^4* (2021).
- 2109.13924 — *Improved Beckner's inequality for axially symmetric functions on S^n* (2021).
- 2208.03612 — *Some geometric inequalities related to Liouville equation* (2022).
- 2306.05184 — *Rigidity of Steady Solutions to the Navier-Stokes Equations in High Dimensions and its applications* (2023).
- 2311.12659 — *Uniqueness of critical points of the second Neumann eigenfunctions on triangles* (2023; later Inventiones Mathematicae).
- 2510.18681 — *A Generalization of the Sphere Covering Inequality* (2025).
- 2604.19003 — *Critical points of the second Neumann eigenfunctions on the quadrangles with symmetry* (2026).
- 2605.15448 — *Symmetry and Rigidity Results for the Mean Field Equation and Hawking Mass on S^2* (2026).

For the triangle, quadrangle, Beckner-S4, and 2026 mean-field/Hawking papers, substantial full text or experimental arXiv HTML was inspected; other entries were used as supporting first-page/abstract evidence.

## Direct observations from substantial full text

### Triangle Neumann paper

The paper starts with a generic domain `\Omega\subset\mathbb R^n`, then specializes to an open triangle `T`. The second eigenfunction is `u`; Neumann eigenvalues are `\mu_j`; mixed eigenvalues are written with `\lambda`, for example `\lambda_1^{\Gamma_D}`. Long/medium/short sides are abbreviated by `L,M,S`. The nodal set is `\mathcal Z(u)`. A rotational vector field about a point `p` is written `R_p`. Domain deformation uses a family such as `T^t`, with corresponding eigenfunctions such as `u^0`.

This is strong evidence for:

- generic-to-concrete geometry renaming;
- semantic side labels;
- family notation via indices/superscripts;
- ordinary point/vector-field notation;
- calligraphic notation when a genuine named set is being introduced.

### Symmetric quadrangle paper

The generic PDE domain is again `\Omega`, while an open quadrangle is `Q`; a kite is `K`; vertices are `P_i`; the center is `C`. The non-vertex critical set is `\mathcal C_{nv}(u)`. Geometry is parametrized by an angle `\alpha`, a height `h`, and thresholds `\widehat h`, `\widetilde h`, `h_0`, `h_1`. Symmetric/antisymmetric spectral quantities are distinguished with superscripts such as `\mu^s` and `\mu^a`. In preliminaries a generic elliptic operator is simply `L`, with coefficients `a_{ij},b_i,c`, and standard basis vectors are `e_i`.

This is strong evidence for:

- meaningful initials for concrete geometric subclasses;
- related objects encoded by a common base plus mathematically meaningful modifiers;
- short standard letters for generic operators and coefficients;
- avoiding new fonts when indices or superscripts already express the relation.

### Beckner S4 paper

The equation uses `u`, parameter `\alpha`, the Paneitz operator `P_4`, functionals `J_\alpha` and `I_\alpha`, and normalized sphere measure `dw`. After axial reduction, `\xi_1` is renamed `x`; the repeated derivative quantity is compressed to `G(x)=(1-x^2)u'`. Gegenbauer polynomials are `F_k`, with eigenvalues `\lambda_k`; expansion coefficients use `a_k`, together with scalars such as `\beta` and `\gamma`.

This strongly supports:

- plain indexed operator/functional families;
- local simplification after dimension reduction;
- compact derived symbols for repeatedly used analytic quantities;
- coefficient families encoded by subscripts.

It also provides an important correction to an earlier overstatement: the paper uses `\mathfrak L`, and also calligraphic functional notation such as `\mathcal J_\alpha`. Hence one cannot honestly infer from the Gui corpus that decorative alphabets are categorically absent.

### Mean-field/Hawking S2 paper

The main unknown and parameter remain ordinary (`u`, `\alpha`), with standard sphere notation. The paper introduces geometric objects—great circles, hemispheres, reflections, tangent vector fields—near first mathematical use instead of front-loading a large notation glossary. The notation follows the geometry locally rather than manufacturing a global typographic hierarchy.

This supports a first-need introduction policy and semantic geometry notation.

## Cross-paper conclusions

### High-confidence transferable habits

1. **Direct naming of primary objects.** Main functions, parameters, domains, and operators use ordinary field-standard symbols.
2. **Semantic initials for concrete geometry.** When a shape has a stable name, a meaningful capital initial is natural (`T`, `Q`, `K`) while `\Omega` remains useful for a generic domain.
3. **Related-family notation.** Indices, superscripts, hats, and tildes are used to express mathematical relation, not decoration.
4. **Standard spectral/PDE notation.** Operators, eigenvalues, Sobolev spaces, ambient Euclidean/spherical spaces, and measures are written in recognizable field notation.
5. **Local simplification after reduction.** Once symmetry or coordinates reduce the problem, active variables are simplified (`\xi_1` to `x`) and repeated expressions may receive a short derived symbol (`G`).
6. **Notation introduced near need.** A large glossary is not the default when local definitions suffice.

### Moderate-confidence preferences

- `u` as main scalar solution/eigenfunction;
- `P_i` for vertices;
- `\mu_j` for Neumann spectral data and `\lambda` for Dirichlet/mixed data in the spectral-geometry papers;
- `T/Q/K` for triangle/quadrangle/kite.

These should remain soft because coauthors and field conventions matter.

## What must NOT be claimed from the corpus

- That Changfeng Gui never uses `\mathcal` or `\mathfrak` notation.
- That every paper should use `u,T,Q,P_i,\mu_j` regardless of context.
- That exact symbol choices in coauthored papers can be personally attributed to one author.
- That a single paper's complete notation map should be copied into a new manuscript.

## User house-style overlay

The user's explicit preferences are stronger than the corpus on typography:

- avoid `\mathscr`;
- avoid `\mathfrak` unless forced by imported standard notation;
- use `\mathcal` sparingly and semantically;
- never create a second semantic meaning for an already used recurring symbol.

This overlay is intentionally separate from the empirical author corpus prior.

## Runtime ordering

1. duplicate-symbol integrity;
2. explicit user requirements;
3. problem/field convention;
4. collision-free source notation;
5. Gui corpus prior for genuinely open choices;
6. user plain-typography overlay when multiple equivalent representations remain.

The result should feel like a concise analysis/PDE notation system, not a reproduction of any source paper.
