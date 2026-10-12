# Case study: what expressive polishing did not settle

Diagnostic source: `large_N_polya_szego_reconstructed_v1231.tex`, SHA256 `db10be7965f8645c663be12a213c7404cca2d8004faa29f18855953aff4ad895`. Locators below belong to this version. This is a same-agent referee-style reading, not a complete correctness audit. The supplied manuscript is not a runtime dependency for other uses of the skill.

## Contribution is not the same as interpretation

Introduction §1.2 gives an exact Fourier-dual quadrature interpretation and names auxiliary-function precedents. This is useful exposition. It does not yet clearly separate standard framework, the paper's quantitative atomic rigidity, exact Bessel comparison, and nonlinear spectral comparison uniform in the defect.

The principle: after finding an adjacent literature, identify what still has to be established in the target. Do not let a familiar duality identity become the whole novelty pitch. Conversely, do not diminish a difficult new application merely because the duality is standard.

Sources already inspected for this case: Cohn–Kumar, §4, including unequal charges on printed p. 121, https://arxiv.org/pdf/math/0607446v2; Krieg–Vybíral, §1.2, https://doi.org/10.1007/s00041-023-10021-7; Nagel, §§1.2–1.3 and Theorem 6, https://arxiv.org/html/2502.17082v2. These establish relevant precedents, not a completed priority search for every target theorem.

## Breadth has an existing candidate inside the paper

Theorem 4.3 packages sharp inverse-power inequalities, weight control, low-frequency control, and microscopic rigidity. This is a candidate for a more visible mathematical interface for approximation/discrete-energy readers. Foregrounding its existing content may serve broader readers better than adding more contextual citations. Its centering condition and scaled-defect regime must remain visible; no uncentered quantitative extension is inferred here.

## A readable cancellation slogan can hide an underspecified calculation

Lemma 7.2(iii), source lines 2958–3018, introduces completion weights, a normalized returned sum, alias contributions, and a shifted-return decomposition. The proof at lines 3030–3048 gives the useful idea of recombination, but the inspected text does not provide an explicit construction of the completion weights or a fully displayed definition of the returned sum and shifted pieces. The finite ranges, normalization, and boundary contributions are central to the claimed estimate.

The appropriate objection is reproducibility of a central argument. It is not a conclusion that the estimate is false. The outline's unit-phase identity should remain, while the body must determine the finite construction and explain the passage to the bound. An ordinary prose-polishing pass cannot invent the omitted derivation.

## A hypothesis issue must be traced, not dramatized

Lemma 7.2(i), source line 2898, assumes a degree-zero phase; its proof explicitly uses this for vanishing first moments. Proposition 7.3, lines 3092–3099, constructs a periodic phase by noting that the sum of its increments divided by 2π is an integer. The inspected sentence does not establish that the integer is zero. The later near-regular construction, line 3572, explicitly chooses degree zero.

The bounded question is which parts of Lemma 7.2 the critical-scale argument actually needs. It may be enough to separate identities valid for any periodic unimodular phase from those requiring zero winding. If first-moment cancellation is needed there, zero winding or the corresponding correction must be supplied. No counterexample to the main theorem has been established by this observation.

## Uniformity needs an operative citation interface

In the proof of Theorem 9.2, source lines 4264–4271, a transported-kernel Sobolev estimate is attributed to a Calderón commutator bound and classical references. A referee can reasonably ask for the particular estimate, its domain, and how two material derivatives and the stated uniform constants fit its hypotheses. This is a targeted request for a central analytic interface, not a rule that every standard estimate requires a full reproving.

## Do not convert this case into a universal template

There is no requirement for all manuscripts to have a sampling interpretation, a standalone auxiliary theorem, a phase model, or an application section. Nor is there a fixed introduction length or preferred adjective. The reusable lesson is to distinguish reader orientation, contribution assessment, and reproducibility of the decisive argument, then repair the level that actually failed.
