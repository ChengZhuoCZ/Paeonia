# Polygonal spectral reformulation: mathematical connections

This is an editorial research dossier for the supplied large-N polygon manuscript, checked on 2026-09-08. It identifies context for explaining the existing argument. It neither verifies the original proof nor inserts new claims into the manuscript. Use the general decision rules in Protocol 04p for other papers; do not reuse this bibliography by default.

## 1. Periodic Sobolev duality and quadrature — exact reinterpretation

**Primary source.** David Krieg and Jan Vybíral, *New Lower Bounds for the Integration of Periodic Functions*, J. Fourier Anal. Appl. 29, 41 (2023), [§1.2, equations (2)–(4)](https://doi.org/10.1007/s00041-023-10021-7). The paper formulates weighted quadrature on periodic Fourier-defined Hilbert spaces and measures its error in the dual norm. This supports the framework below, not a claim that the source treats polygon eigenvalues or proves the manuscript's sharp atomic inequality.

**Specialization made in this dossier.** On the circle with normalized measure m, use the convention

\[
 \|f\|_{H_*}^2=|\widehat f(0)|^2+
 \sum_{k\ne0}|k|^3|\widehat f(k)|^2.
\]

This is a periodic Sobolev H^(3/2) norm with the specified Fourier normalization. For a probability measure ν = Σ_j w_j δ_{ψ_j}, let Q_ν(f) = Σ_j w_j f(ψ_j). Fourier duality identifies the squared worst-case error as

\[
 e(\nu)^2:=\sup_{\|f\|_{H_*}\le1}|Q_\nu(f)-\!\int f\,dm|^2
 =\sum_{k\ne0}\frac{|\widehat\nu(k)|^2}{|k|^3}
 =2\sum_{k\ge1}\frac{|\widehat\nu(k)|^2}{k^3}.
\]

The constant Fourier mode cancels because ν has mass one. Equivalently this is the squared homogeneous H^(-3/2) norm of ν−m, with the same convention. This short calculation is a specialization of the standard framework; it is not attributed as a polygonal result of Krieg–Vybíral.

**Relation to the manuscript.** For its uniform root measure σ_N,

\[
 E_N(\nu)=\tfrac12\{e(\nu)^2-e(\sigma_N)^2\},
 \qquad e(\sigma_N)^2=2\zeta(3)/N^3.
\]

Thus the auxiliary defect compares the integration errors of weighted sampling rules in this particular norm. It is an energy excess relative to the regular rule, **not** generally the squared H^(-3/2) distance from ν to σ_N. Nor is it the eigenvalue difference. The manuscript still needs the exact Bessel comparison, nonlinear reconstruction, and relative spectral remainder.

**Reader payoff.** A harmonic analyst can recognize a negative Sobolev discrepancy; a numerical analyst can recognize the error of a finite weighted rule. The spectral argument explains why smoothness 3/2 appears: two integrations of turning produce k^(-2), and the order-one Hessian produces k·k^(-4). This gives an entry to the method beyond the conjecture.

## 2. Positive auxiliary functions in discrete energy — a method precedent

**Primary source.** Henry Cohn and Abhinav Kumar, *Universally optimal distribution of points on spheres*, JAMS 20 (2007), 99–148, [§4, Proposition 4.1 and the unequal-charge extension on printed p.121](https://arxiv.org/pdf/math/0607446v2). Their lower bound uses an auxiliary function below the potential with nonnegative harmonic coefficients. Section 4 also discusses charges of the same sign; it would be incorrect to describe unequal weights alone as absent from that framework. Table 1 includes regular N-gons, and Theorem 1.2 concerns sharp configurations and completely monotonic potentials.

**Target correspondence, inferred from the supplied proof.** In `lem:atomic-fejer-certificate`, the target potential is 1/(a+u), where u=2−2cosθ. The polynomial h lies below it; the remainder has a Fejér-square sign; positive Fourier coefficients produce squares of moments after summing over atom pairs. The diagonal exposes Σw_j²−1/N. This is a concrete correspondence with the auxiliary-function method, not merely a shared use of Fourier series.

**Boundary of the connection.** The manuscript requires a particular weighted certificate with quantitative remainder, microscopic mesh recovery, exact spectral coefficients, and nonlinear comparison. The cited general theorem does not by itself establish those claims or the polygonal eigenvalue result. Historical influence and priority for the particular certificate have not been established by this focused search.

**Reader payoff.** Discrete-geometry readers can recognize why positivity of a suitably chosen kernel detects a distinguished configuration. Exposition can then focus on the target paper's use of this structure to control a moving domain and its eigenfunction.

## 3. Torus energy, quadrature, and linear programming — a neighboring synthesis

**Primary source.** Nicolas Nagel, *On the Global Optimality of Fibonacci Lattices in the Torus*, [arXiv:2502.17082v2, §§1.2–1.3 and Theorem 6](https://arxiv.org/html/2502.17082v2). The paper relates periodic Sobolev quadrature errors to pair energies and uses a Fourier-positive auxiliary-function bound on the torus. Its concrete setup includes equal-weight rules and tensor-product kernels; it does not establish the target inverse-cubic, variable-weight spectral comparison.

**Reader payoff.** This is a verified example of the neighboring communities already meeting through these operations. It supports positioning the polygon argument at a further interface with spectral shape optimization. It does not justify claiming a new connection between energy and quadrature itself.

## Editorial selection

The nearest useful connection is the Sobolev/quadrature interpretation of the actual energy, followed by the auxiliary-function precedent for the actual certificate. Avoid a tour of E8 lattices, coding theory, or all discrepancy notions when these do not explain the target mechanism. The fact that these subjects share literature is not sufficient reason to include them.

The relation between the spectral problem and a discrete harmonic-analytic energy can carry the central assessment; choose its wording from the actual argument, not from an example phrase. Explain what makes this relation noteworthy in the target setting: the eigenvalue depends on a domain-wide eigenfunction, yet the turning data lead to a rigid sampling-energy comparison. The Fourier-duality identity itself is standard, and the novelty of the particular spectral bridge must be assessed separately from that standard identity.

“Elegant” can refer to the same defect obtaining mesh information, controlling spectral errors, and identifying equality. This economy is visible in the supplied proof. It does not mean that every subsequent estimate is short or that the approach is already known to handle other eigenvalues, nonconvex polygons, or higher dimensions.

All three references were inspected at the listed primary-source locations. The search is a targeted contextual investigation, not an exhaustive priority review. No source quotations or full source prose are embedded here.
