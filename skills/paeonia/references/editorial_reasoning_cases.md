# Editorial reasoning cases: why a change helps

These are diagnostic examples for Protocol 04p. They are not sentences to copy or a required outline architecture. Target-mathematics examples use the supplied large-N manuscript as trusted evidence. Other examples are hypothetical editorial situations with their assumptions stated.

## A. A complete list can still fail to explain

**Weak passage:** “We encode the polygon by a turning measure, apply atomic rigidity, and control the remainder by cyclic cancellation.”

It names the objects, stages, and outputs. Yet the reader cannot infer why turning is the useful representation, what rigid quantity it supplies, or why cancellation has the right size. Adding three headings or calling the argument powerful changes none of these missing inferences.

**Repair decision:** expose one bridge at a time. Turning is integrated twice to obtain the linear radial potential. Pairing that potential with an order-one spectral Hessian produces inverse-cubic weights. The corresponding atomic energy retains the side constraint and detects the regular configuration. Exact spectral coefficients and nonlinear reconstruction remain separate obligations.

**Why this helps:** the reader can now predict the exponent and distinguish what the discrete comparison solves from what remains. This explanation concerns compatibility among objects, not the amount of algebra in the proof.

**When not to use it:** if the representation and its functional role are standard for the intended audience and no choice is at issue, a short statement and citation may suffice.

## B. Naming cancellation does not reveal its mechanism

**Weak passage:** “The complete cyclic expression cancels to an error of order o(E).”

**Repair decision:** explain that the apparently linear phase errors are combined before absolute values are taken. A unit-phase identity turns their real part into squared differences; residual weight errors occur paired with phase errors. Both factors are controlled by rigidity, preserving a full factor of the quadratic defect. This is supported by `eq:relative-cubic-008` through `eq:relative-cubic-011` in the target source.

**Why this helps:** the reader can locate exactly where a term-by-term absolute estimate would lose a small factor. The repaired outline need not reproduce the phase-column calculation or its cutoffs to explain that operation.

**Failure control:** an extra page of estimates without identifying the paired factors would still fail. Conversely, a black-box citation can be adequate for an imported routine estimate; it is the new bottleneck here that calls for opening this part of the argument.

## C. Earned surprise is an editorial judgment

**Weak passage:** “We establish a remarkable and surprising connection with harmonic analysis.”

It leaves the mathematical referent unspecified. Removing the adjectives would not repair it; merely replacing them with “central” would not repair it either.

**One possible realization, not a wording template:** “A surprising connection emerges between the shape of the domain and the accuracy of a weighted sampling rule on the circle. The exterior angles supply the weights and the vertex directions supply the nodes. Two integrations of these turning data, followed by the disk's spectral Hessian, select the Fourier weights of a periodic Sobolev quadrature error. The same discrete defect that identifies the regular rule then governs the spectral comparison, once the nonlinear terms have been controlled.”

This is an original editorial exercise, not a quotation or an inserted manuscript paragraph. The [connection dossier](large_n_connections.md) supplies the normalization and the limits of the interpretation.

**Why this helps:** the evaluative opening tells a broader reader where to direct attention; the following dictionary gives the judgment content. The surprising feature is the target spectral bridge, not the already standard Fourier-duality identity. Citing the latter as a precedent sharpens the contribution instead of diminishing it.

**Failure control:** a rule rejecting the passage because it contains “surprising” is too restrictive. A rule accepting the first weak passage because it names two fields is too permissive. No frequency quota for either word is useful. A passage that conveys the same supported assessment in different language, including without these adjectives, may work equally well; repeating or swapping sample phrases does not establish editorial success.

## D. Bigger audience does not mean a bigger theorem

Suppose a method expresses an existing functional through a familiar kernel energy but the supplied proof works only in one geometric class. Explain the shared operation to readers who know the kernel and identify the geometric realization that makes this application work. Do not announce validity on arbitrary manifolds. A verified structural connection can broaden the paper's intellectual audience without broadening its formal conclusion.

The research question should be “where is this kernel, duality, certificate, or construction used?” rather than “which famous theory could make the result sound important?” If a preceding theorem already covers unequal charges, do not label unequal weights as the new ingredient. If a source only treats equal weights, do not infer a variable-weight theorem from it.

## E. More overview can be the wrong repair

Suppose a three-paragraph proof applies a standard compactness theorem with all hypotheses visible and then a one-line inequality. Conditional assembly, a named reformulation, a toy model, and six stage headings would add memory burden. Retain the direct route. Use the same causal standard—what must the reader infer—but no elaborate scaffold is required.

For a longer proof, a model that assumes the desired uniform mesh cannot explain how mesh regularity is obtained. It may illustrate a later estimate only if that restriction is declared and the independent entry argument remains visible. A model earns space by preserving the obstruction being explained.

## F. A self-check can import the missing explanation

An author writes that a chart “removes the cutoff,” then answers a cold-read question from memory with a detailed tangent-ray argument. The answer is correct relative to the body, but the outline did not enable it. The assessment must identify this mismatch and repair the text with the known comparison point, quadratic coefficient control, and coverage of tiny configurations. A paragraph number and a PASS label would conceal the defect.

These cases probe decisions and explanatory effects, not preferred wording. They support manual review; they are not automated behavioral measurements or independent reader experiments.
