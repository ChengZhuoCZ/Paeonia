# Diagnostic: large-N polygonal spectral manuscript

This is a case-specific editorial regression reference, not a reusable Introduction template. Source: `large_N_polya_szego_reconstructed_v121.tex`, supplied by the user. Its mathematics is treated as trusted source content. No independent correctness or novelty certification is made. Labels below refer to that supplied version; do not impose its symbols or powers on other problems.

## What already works, and what the skill missed

The existing Introduction already identifies the continuum-to-finite gap, defines the atomic measure, motivates the inverse-cubic exponent, and says that the final error must be relative. The failure is not a total absence of mechanisms. It is insufficient hierarchy and connective explanation: new technical objects arrive faster than their jobs become clear, and the central reformulation has the narrative weight of an ordinary encoding.

The proof supplies more than a convenient coordinate choice. Within its hypotheses, the turning measure records the discrete constraint that disk convergence cannot resolve, an atomic inequality singles out the regular configuration, and spectral comparison transfers that rigidity back to the domain. These are different links. The spectral functional is not asserted to equal the atomic energy, and arbitrary atomic measures must not be asserted to be globally realizable as polygons.

## Evidence anchors and explanatory jobs

| Source anchor | What the outline should explain |
|---|---|
| `prop:existence`, `prop:full-activation`, `prop:global-minimizer-radial-entry` | Why it is enough to identify a minimizer, why it has N effective sides, and why it enters a disk chart without mesh lower bounds. |
| `def:polar-coordinates`, `eq:curvature-coordinates-006`, `eq:curvature-coordinates-007` | Vertex directions locate the turning; normalized exterior angles give positive masses. Centering is a geometric normalization, not the claimed spectral reduction. |
| `thm:atomic-rigidity`, `thm:microscopic-rigidity` | The auxiliary defect is nonnegative, its zero set is the regular root configuration, and sufficiently small scaled defect also gives mesh control. These are distinct uses. |
| `sec:disk-perturbation`, `thm:bessel-coercivity`, `sec:polar-geometry` | Two integrations motivate the curvature-to-displacement factor; the order-one Hessian motivates inverse-cubic weights. The exact Bessel comparison and nonlinear turning equation still need control. |
| `prop:critical-localization`, `thm:critical-cubic-quadrature`, `cor:first-localization`, `cor:refined-localization` | Coarse information first controls the defect; a first cubic comparison improves it enough to obtain near-regular weights and gaps. Do not assume that mesh at the start. |
| `prop:principal-cubic-relative`, `thm:material-endpoint-comparison` | Explain why subtracting the regular endpoint and matching geometric comparisons reveals cancellation hidden by separate absolute estimates. |
| `thm:constraint-chart`, `thm:relative-remainder` | Explain what possible tiny-defect competitors would remain after a cutoff estimate, and why exact constraints close that range without assuming criticality. |
| `thm:spectral-gap`, `lem:polar-equality-reconstruction` | State the localized class of the final comparison. Minimality forces zero atomic defect; turning reconstruction and area recover the geometric equality case. |

## Internal causal spine

Global variational reduction supplies a near-disk minimizer, but not a regular mesh. The atomic representation retains discrete turning data and gives a defect whose zero set is known. Matching its principal Fourier energy to the disk's spectral response explains why it is the right defect. The initial nonlinear estimates localize that defect; the first cubic comparison improves localization enough for microscopic rigidity to supply a nearly regular mesh. That improved geometry enables relative cancellation. Compatible endpoint comparison and exact constraints extend the relative estimate to every positive defect in the localized class. The resulting sign forces zero defect at a minimizer and the original polygon is then recovered.

This internal spine is not final manuscript prose. A future outline should make the central atomic reduction prominent, explain its exact and approximate links separately, and group its stages by reader need rather than retain the supplied subsection or paragraph order.

## Acceptance questions specific to this case

- Why does closeness to the disk leave a finite-N optimization problem unresolved?
- What information is preserved by locations and masses of the atomic measure?
- Why this Fourier weight, rather than an arbitrary discrepancy norm?
- What prevents the atomic minimization theorem alone from proving the spectral theorem?
- Which independent estimate precedes the acquisition of a nearly regular mesh?
- Why are the two uses of cubic information different in purpose and available assumptions?
- Why does a bound depending only on N fail for arbitrarily tiny positive defects?
- Why does zero atomic defect determine the polygon only after geometric reconstruction and normalization?

The source has answers to these questions. The outline should expose them without requiring the reader to open the proof.


For researched Sobolev/quadrature and auxiliary-function connections, see [the connection dossier](large_n_connections.md). It distinguishes exact interpretation from methodological precedent and the remaining spectral obligations.
