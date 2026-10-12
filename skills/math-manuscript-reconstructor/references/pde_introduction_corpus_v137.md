# PDE Introduction Corpus — v1.37 Distillation Record

This report stores abstract editorial decisions only. It is not a phrase bank, paragraph template, or author-imitation profile.

## Corpus

1. Tristan Buckmaster and Vlad Vicol, *Nonuniqueness of weak solutions to the Navier–Stokes equation*, Annals of Mathematics 189 (2019), arXiv:1709.10033. Introduction pp. 1–3 inspected.
2. Alessio Figalli and Joaquim Serra, *On the fine structure of the free boundary for the classical obstacle problem*, Inventiones Mathematicae 215 (2019), arXiv:1709.04002. Introduction pp. 1–3 inspected.
3. Otis Chodosh and Christos Mantoulidis, *Minimal surfaces and the Allen–Cahn equation on 3-manifolds: index, multiplicity, and curvature estimates*, Annals of Mathematics 191 (2020), arXiv:1803.02716. Opening contribution map inspected.
4. Jacob Bedrossian and Nader Masmoudi, *Inviscid damping and the asymptotic stability of planar shear flows in the 2D Euler equations*, Publications Mathématiques de l'IHÉS 122 (2015). Introduction and proof overview pp. 1–10 inspected.
5. Carlos E. Kenig and Frank Merle, *Global well-posedness, scattering and blow-up for the energy-critical focusing nonlinear Schrödinger equation in the radial case*, Inventiones Mathematicae 166 (2006), 645–675, arXiv:math/0610266. Opening theorem and method map inspected.
6. Scott Armstrong, Luis Silvestre, and Charles Smart, *Partial regularity of solutions of fully nonlinear, uniformly elliptic equations*, Communications on Pure and Applied Mathematics 65 (2012), arXiv:1103.3677. Introduction pp. 1–2 inspected.
7. Alexander Kiselev, Fedor Nazarov, and Alexander Volberg, *Global well-posedness for the critical 2D dissipative quasi-geostrophic equation*, Inventiones Mathematicae 167 (2007), arXiv:math/0604185. Introduction pp. 1–2 inspected.

## Cross-paper findings

### No common target length

The corpus contains both compact one-to-two-page Introductions and long mechanism-driven Introductions. Length follows the number of theorem coordinates, new objects, incomparable frontier results, and nonlinear interfaces—not venue prestige.

### The PDE theorem is a coordinate, not a headline

The strongest Introductions identify the solution class, regime, topology, and structural assumptions at the points where the theorem differs from known results. They do not rely on generic verbs such as “extend” or “improve.”

### Frontiers are often partially ordered

A paper may improve regularity while retaining symmetry, remove symmetry in a weaker topology, reach an endpoint for a narrower solution class, or sharpen a singular-set conclusion. Treating one predecessor as globally strongest can distort the actual mathematical position.

### Result architecture matters independently of narrative arc

Observed architectures include a solution-class separation, a threshold dichotomy, a regular/singular stratification, a two-level estimate-to-application hierarchy, and a singular-limit bridge. These cannot all be represented faithfully by a single undifferentiated “main theorem” paragraph.

### Assumptions need role and location

Several papers make interpretive use of where an assumption enters: a symmetry hypothesis may be needed only in rigidity; coefficient regularity may exclude a major operator class; a constructed weak solution may fall short of an admissible energy class. The Introduction should distinguish theorem scope from method scope.

### One obstruction is sometimes insufficient

Mechanism-heavy stability papers often require a causal stack: the linear mechanism produces transient growth; nonlinear interactions threaten closure; a custom norm or coordinate change controls resonances; a final elliptic or top-order estimate closes the argument. The stack should remain short and causal rather than becoming a list of technical difficulties.

### A formula earns space by changing understanding

The most useful displayed relations reveal a critical time, sign, threshold, modulus, scaling, or compactness mechanism. They are interpreted semantically and tied to the closing estimate. Technique labels without this bridge are less informative than one well-chosen formula.

### Boundaries should be typed

The corpus repeatedly distinguishes an open case, a method limitation, a known counterexample, and a stronger solution class not covered. A generic “we expect the assumption can be removed” sentence loses this information.

## Resulting package policy

The v1.37 PDE branch is a conditional extension of `IntroductionCoreBrief`, not a new mandatory artifact. It adds theorem coordinates, a multi-axis result delta, result architecture, assumption roles, a capped obstruction stack, mechanism-to-control semantics, proof interfaces, and typed scope boundaries. Only the fields that affect theorem interpretation should enter the final prose.
