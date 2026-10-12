# Protocol 04n — Mathematical Story Discovery


> **Conditional research module.** Use only when the theorem's meaning depends on a specific parent program or nontrivial transition. Do not force a larger story for every expansive paper; Protocol 04's compact core is the default.

## Purpose

Build the **larger mathematical story** that makes the focal theorem feel necessary rather than merely new.

This protocol is not a literature-summary pass and not a request for inflated rhetoric. It asks a harder structural question:

> What larger mathematical program, principle, or transition contains the focal theorem as a meaningful missing piece?

For a paper that triggers this module, a good Introduction should be able to answer this before it starts listing technical advances.

The output is an internal `MathematicalStoryLedger`. It contains no publication prose.

## 1. Climb above the local problem

Starting from the main theorem, climb outward through up to four levels:

1. `FOCAL_THEOREM` — the exact result proved in this paper;
2. `FOCAL_PROBLEM` — the conjecture, optimization problem, classification problem, or parameter regime directly addressed;
3. `PARENT_PROGRAM` — the larger theory in which that problem is a natural model case;
4. `CANONICAL_PRINCIPLE` — the classical principle, symmetry, compactness mechanism, variational law, geometric paradigm, or analytic dichotomy that makes the parent program recognizable.

Not every paper needs all four levels. Stop when the next level becomes generic prestige language rather than a mathematically operative relation.

A phrase such as `shape optimization is an important field` is not a parent program. A parent program must identify a mathematical objective, mechanism, or unresolved structural question.

## 2. Identify the primary story archetype

Choose one primary archetype and at most two secondary archetypes from:

- `CONTINUUM_TO_FINITE_COMPLEXITY` — a canonical continuum theorem is restricted to polygons, graphs, finite-rank objects, lattices, finite dimensions, or another finite-complexity class;
- `LIMIT_TO_EXACT_FINITE` — limiting/asymptotic information is known, but exact finite-parameter structure or rigidity remains open;
- `LOCAL_TO_GLOBAL` — local coercivity, perturbative uniqueness, or branch information exists, while global control is missing;
- `QUALITATIVE_TO_QUANTITATIVE` — existence/uniqueness/inequality is known, but sharp deficit, stability, rate, or modulus is missing;
- `SYMMETRY_TO_RIGIDITY` — symmetry identifies a candidate, but uniqueness/equality classification requires a rigidity mechanism;
- `COMPACTNESS_TO_STRUCTURE` — compactness gives convergence or existence, but does not preserve enough combinatorial/geometric structure to finish the theorem;
- `VARIATIONAL_TO_GEOMETRIC` — an analytic variational principle must be converted into a geometric classification or shape statement;
- `CRITICAL_OR_ENDPOINT` — a theory changes at a threshold, endpoint, critical dimension, or critical exponent;
- `CLASSIFICATION_PROGRAM` — local branches, special classes, or partial regimes are known, but a full classification is not;
- `UNIFICATION_OF_REGIMES` — separate asymptotic, local, dimensional, or parameter regimes need a common mechanism;
- `UNIVERSALITY_ACROSS_FUNCTIONALS` — parallel extremal or rigidity phenomena appear across several functionals and the paper resolves one structurally central member;
- `DISCRETE_CONTINUUM_DUALITY` — a discrete object approximates or encodes a continuum one, but the exact relation is mathematically nontrivial;
- `MODEL_CASE_FOR_BROADER_PROGRAM` — the theorem is a sharp model where a broader method can be tested or completed;
- `OTHER` — only with an explicit mathematical description.

Archetypes are organizing abstractions, not templates. Never force one because it sounds grand.

## 3. Find the scale transition

Many strong mathematical stories are driven by a change of scale or category. Record any genuine transition such as:

- continuum → discrete/finite complexity;
- limiting object → finite parameter;
- weak convergence → exact structure;
- local neighborhood → full moduli space;
- qualitative inequality → sharp stability;
- special symmetry class → unrestricted class;
- subcritical → critical/endpoint;
- low dimension → all dimensions;
- approximate optimizer → exact optimizer;
- existence → uniqueness/rigidity;
- one functional → a family of related functionals.

For every transition record **why the target side is not a routine corollary of the source side**.

This explanation is often the real intellectual center of the Introduction.

## 4. Identify the governing structural tension

Write the paper's main tension as a relation between two mathematically meaningful facts, not as `the problem is difficult`.

Examples of admissible forms:

- the continuum optimizer is selected by symmetrization, but the admissible discrete class is not preserved by symmetrization;
- compactness forces near-symmetry, but exact combinatorial type is not stable under weak limits;
- the limiting model is rigid, but the error term is larger than the finite-parameter energy gap one must resolve;
- local second variation is positive, but the moduli space has degenerate boundary configurations;
- a monotonicity formula controls one regime while losing sign in another;
- classification is known in a symmetric class, but symmetry breaking cannot be excluded globally.

The tension must map to an actual proof obstacle or theorem-level distinction.

## 5. Build the mathematical story graph

Before deciding paragraph order, build a small graph of the theorem's mathematical neighborhood. Typical node types are:

- canonical principle or unrestricted theorem;
- focal restricted problem;
- limiting/asymptotic model;
- local or perturbative theory;
- quantitative/stability theory;
- parallel functional or neighboring classification problem;
- degeneration/boundary regime;
- present theorem.

Useful edge types include:

- `SPECIALIZES`;
- `RESTRICTS_TO`;
- `LIMIT_OF`;
- `DISCRETE_ANALOGUE_OF`;
- `GLOBALIZES`;
- `QUANTIFIES`;
- `RIGIDIFIES`;
- `EXTENDS_PARAMETER_RANGE`;
- `PARALLEL_TO`;
- `SUPPLIES_MECHANISM_FOR`;
- `OBSTRUCTED_BY`.

Then select one `critical_story_path`: the shortest mathematically honest path that explains why the present theorem matters. The graph may be rich; the Introduction should not be.

For `GRAND`/`GRAND_PLUS`, the critical path should normally contain at least one nontrivial edge above the local conjecture.

## 6. Build the mathematical ancestry, not merely the chronology

Research literature outward from the focal paper. For substantial stories, distinguish the following roles:

- `PROGRAM_ORIGIN` — where the parent mathematical question or principle was formulated;
- `CANONICAL_THEOREM` — the benchmark theorem in the unrestricted/limiting/continuous setting;
- `DISCRETE_OR_RESTRICTED_FORMULATION` — where the present constrained version enters;
- `PARALLEL_PROBLEM` — a closely related functional or geometric problem whose status clarifies the landscape;
- `ASYMPTOTIC_OR_LOCAL_FRONTIER` — what is known near the candidate or in a limit;
- `GLOBAL_FRONTIER` — strongest exact result before the paper;
- `RIGIDITY_OR_STABILITY_PRECURSOR` — a theorem supplying the mechanism but not the final scope;
- `OBSTRUCTION_EVIDENCE` — a result explaining why an obvious route is insufficient.

The purpose is to recover the **mathematical ancestry of the theorem**, not to maximize citation count.

## 7. Research breadth

Choose one:

- `COMPACT` — the parent program is standard and a small number of authoritative sources suffices;
- `TRIANGULATED` — verify the story using at least distinct source roles, typically origin/benchmark/frontier;
- `DEEP` — required when the Introduction depends on a multi-decade program, several parallel theories, or a non-obvious bridge between limiting and exact problems.

For `GRAND_PLUS`, default to `DEEP` unless the program is unusually self-contained.

No fixed number of references is required. Diversity of mathematical role matters more than count.

### Outward research procedure

For `TRIANGULATED` or `DEEP`, search outward rather than only following the source manuscript's bibliography:

1. verify the exact focal problem and strongest current frontier;
2. locate an authoritative source for the parent program or canonical principle;
3. identify the limiting/unrestricted theorem if one organizes the story;
4. search for parallel functionals or analogous constrained problems only when they test the same structural mechanism;
5. locate stability, rigidity, compactness, or classification precursors that explain the missing transition;
6. stop when additional literature adds chronology but no new node or edge to the story graph.

For `GRAND_PLUS`, avoid building the entire story from papers already cited in the supplied draft when independent verification is available.

## 8. Parallel-problem test

A neighboring theorem may enlarge the story only if it answers one of:

- Does the same canonical object optimize several different functionals?
- Is the focal problem the last unresolved member of a natural family?
- Does one parallel problem reveal the obstruction or suggest the mechanism?
- Does the theorem complete a continuum/discrete or local/global analogy?

For each parallel problem record:

`shared structure → known status → decisive difference → relevance to present theorem`.

Delete decorative parallels.

## 9. Program-level theorem interpretation

After the exact theorem is closed, ask what it does to the parent program. Possible roles include:

- `CONFIRMS_CANONICAL_SYMMETRY_IN_RESTRICTED_CLASS`;
- `UPGRADES_ASYMPTOTIC_SELECTION_TO_EXACT_RIGIDITY`;
- `CLOSES_LOCAL_GLOBAL_GAP`;
- `COMPLETES_PARAMETER_OR_DIMENSION_RANGE`;
- `PROVIDES_SHARP_STABILITY`;
- `IDENTIFIES_NEW_REDUCTION_OR_INVARIANT`;
- `LINKS_TWO_PREVIOUSLY_SEPARATE_REGIMES`;
- `ESTABLISHES_A_MODEL_CASE_FOR_A_BROADER_PROGRAM`;
- `OTHER`.

This interpretation must be stronger than a paraphrase of the theorem and weaker than any unsupported program-level claim.

## 10. Opening selection

For a mathematically ambitious paper, choose the first-page entry from the story ledger, not from the need to define notation.

Preferred story openings include:

- `CANONICAL_PRINCIPLE`;
- `PARENT_PROGRAM`;
- `STRUCTURAL_TENSION`;
- `LIMITING_THEOREM_AND_FINITE_GAP`;
- `PARALLEL_EXTREMAL_FAMILY`;
- `CLASSIFICATION_PROGRAM`;
- `SCIENTIFIC_ORIGIN` when ScientificContextLedger independently supports it.

A standard formula may appear early, but it should enter **after the reader understands why this particular formula is the next mathematical object to look at**.

## 11. One-sentence story compression test

Before prose drafting, compress the story to one internal sentence of the form:

> Within [parent program], [canonical principle/known theory] predicts or selects [candidate/structure], but [scale transition or structural tension] prevents the known theory from yielding [exact target]; the present theorem supplies [new mechanism/result], thereby [program-level consequence].

The sentence is diagnostic only. Do not copy its syntax into the paper.

If no non-generic sentence can be written, the story has not been discovered yet.

## 12. Anti-inflation conditions

A larger mathematical story is invalid if it relies on any of:

- field-level importance slogans;
- unrelated famous theorems;
- an unproved claim that the present problem is a `model` or `test case`;
- a parallel problem with no operative shared structure;
- an asymptotic theorem presented as if it nearly proves the finite theorem when the missing step is substantial;
- a scientific application used to substitute for mathematical significance;
- an excessively long history that never returns to the exact frontier.

Grandeur must come from **mathematical architecture**, not from the prestige of surrounding subjects.

## 13. Output

Produce `MathematicalStoryLedger` and pass it to Protocol 04o before paragraph planning.
