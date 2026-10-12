# Protocol 04u — Literature-First Discovery, Fair Credit, and Frontier Verification

## Authority and purpose

For an authorized **reconstruction of an Introduction**, this is the default research pass **after the mathematical theorem and proof scope are known, and before composing Introduction prose**. It is not optional merely because the manuscript contains references. A bibliography is a list of candidates, not evidence that the relevant scholarship has been found. This protocol precedes the `IntroductionCoreBrief` and supplies its verified benchmark, frontier, method ancestry, and priority boundaries. The compact record is `IntroductionLiteratureDossier`; it is **one research artifact, not a mandatory stack of narrative ledgers**.

For `LOCAL_POLISH`, preserve protected prose: apply only to references, novelty language, or historical claims inside the authorized editable region, and reuse valid previous research when the exact source and claim have not changed. A read-only literature review may produce a dossier without changing the article. A user instruction to work offline controls: use available sources, identify the discovery gap, and **never represent an offline inventory as a current comprehensive search**. Author-style papers from Protocol 05o are not silently imported as scholarship; only source-verified relevant works become citation candidates under Protocol 07.

**Order invariant:** `closed theorem truth → theorem fingerprint → external literature discovery → source and claim verification → fair-credit map → exact prior-frontier comparison → IntroductionCoreBrief → narrative design → prose`. In full reconstruction, proof-body-first composition still controls manuscript prose; the research pass may collect evidence earlier, but no final-form Introduction is drafted before `ProofCoreGate`.

## 1. Build a searchable theorem fingerprint

Record the exact result and search terms before running queries:

- mathematical object, operator/functional, domain, dimension, boundary conditions, normalization;
- admissible geometric/functional/parameter class and whether the result is local/global, asymptotic/exact, qualitative/quantitative, sharp/nonsharp;
- conclusion including uniqueness, equality, stability, thresholds, and excluded endpoints;
- conjecture or named classical principle (only if traceable);
- proof mechanism and the nonroutine obstruction, **without asserting priority**;
- alternate spellings, languages, terminology, and Mathematics Subject Classification (MSC) neighborhoods when useful.

Translate theorem claims into several query families. A title-only exact search is insufficient. Avoid allowing the source manuscript's novelty rhetoric to define the search frontier.

## 2. Mandatory outward search: distinct routes, distinct roles

When live scholarly search is available, conduct **at least two materially independent discovery routes** and expand until the theorem-relevant roles are covered. Recommended routes:

1. **Problem-forward:** exact question, conjecture, canonical inequality/model, synonymous formulations and restricted variants; older and most recent papers.
2. **Method-side:** central transformation, estimate, variational principle, rigidity/stability device, limiting mechanism; identify true technical ancestry.
3. **Citation-graph:** backward references of the strongest sources and forward citations, related/independently developed approaches; identify papers the manuscript did not cite.
4. **Boundary search:** nearby classes (e.g. convex/nonconvex, Dirichlet/Neumann, finite/asymptotic, symmetric/general, fixed dimension/all dimensions) that could be confused with the theorem.
5. **Recency check:** newly published and preprint work at the actual research date, including revised versions, corrections and related simultaneous results.

Use appropriate discovery systems: MathSciNet and zbMATH Open when accessible; arXiv and publisher/author pages for preprints and original work; OpenAlex or comparable citation graphs for discovery; Crossref/DOI metadata and publisher pages for bibliographic checks. These systems have different coverage and may have access limits. No search-engine rank, citation count, or paper title is proof of relevance or priority. Try spelling/notation variants; use reviews as maps to the underlying primary sources. When a route is inaccessible, note it and use independent alternatives rather than claiming the route was completed.

Search breadth follows the work: a routine small result can close with a concise search, while a conjecture resolution, comprehensive classification, global optimality claim, or priority-sensitive theorem calls for a deeper history, closest competitive papers, parallel routes and updated preprints. **There is no preset cap on references or required paper count.** The target is sufficiently complete and fair *scholarship*, not a large numerical bibliography.

## 3. Separate discovery, identity, theorem support, and priority

For each relevant candidate, record: canonical authors/title/year; journal, DOI, arXiv identifier and **version** where applicable; accessible primary URL; discovery route; role; claim for which it is proposed; inspected evidence location; and status:

- `FOUND_UNREAD` — bibliographic candidate only;
- `METADATA_VERIFIED` — bibliographic identity confirmed, theorem support not yet checked;
- `ABSTRACT_CONTEXT_ONLY` — broadly related topic checked, no exact theorem comparison;
- `SOURCE_CHECKED` — primary-source theorem/method and its hypotheses inspected;
- `CLAIM_SUPPORTED` — precise adjacent Introduction claim justified by the inspected source;
- `MISMATCH`, `SUPERSEDED`, `RETRACTED_OR_CORRECTED`, or `UNRESOLVED` — explain the reason and effect.

Do not mix journal metadata with theorem numbers from another preprint version. For central comparison and priority claims, an abstract, metadata record, search snippet, citation graph, or another paper's bibliography is **not enough**: inspect the relevant primary source where legally accessible. If not accessible, qualify the claim or withhold it. Protocol 07 governs the separate metadata / locator / claim-support checks; this protocol governs **discovering what should be credited in the first place**.

## 4. Fair-credit map — scholarship as an intellectual dependency graph

Assign roles to sources by actual contribution, not author prestige or citation count. Several roles may apply to one paper, and different papers may support the same role:

- `ORIGIN`: original problem, model, or formulation;
- `CLASSICAL_BENCHMARK`: the organizing theorem or inequality;
- `CONJECTURE_FORMULATION`: who stated which conjecture, in what form;
- `DIRECT_PREDECESSOR`: mathematically closest previously established theorem;
- `PARTIAL_FRONTIER`: sharpest results along different and sometimes incomparable axes;
- `METHOD_ANCESTOR`: specific imported or adapted proof idea;
- `RIGIDITY_STABILITY_OR_LOCAL`: a precursor addressing another crucial obstruction;
- `PARALLEL_OR_INDEPENDENT`: closely related or contemporaneous work, neither automatically predecessor nor derivative;
- `COUNTEREXAMPLE_OR_LIMITATION`: boundaries of an apparently plausible stronger claim;
- `SURVEY_OR_SYNTHESIS`: an orientation source, without displacing the primary source for priority;
- `RELEVANT_ADJACENT`: neighboring theory that substantively changes the theorem's interpretation.

Provide **positive credit**: state what each pivotal work *did prove or introduce* before stating the residual gap. Cite the original contribution and the most relevant precise modern results when both matter; don't attribute an old result only to a survey or a later generalization. Do not systematically exclude competitors, non-English originals, recent preprints, or work outside the manuscript's citation network. Do not use one generic list citation as a substitute for differentiating the contributions of materially distinct works. Do not cite a source merely to inflate counts or imply endorsement.

For each original claim in the manuscript, make visible the three-way boundary:

`prior author(s) established X; the present work establishes Y under Z; X alone does not imply Y because of obstruction W`.

If the manuscript genuinely uses a prior method, say what is borrowed or adapted and what new step is required. Distinguish `inspired by`, `adapts`, `builds on`, `uses`, `extends`, `parallel to`, and `independent of` only when the documented relation supports the verb. Avoid categorical `first`, `only`, `never studied`, `long-standing open`, `settles`, or priority dates without targeted primary-source checks and adequate coverage. A failed search cannot prove an absence.

## 5. Exact frontier comparison, not a fame-based timeline

For pivotal prior theorems, compare along the axes that the manuscript changes. Relevant fields may include:

| Axis | Prior source | Present work | Gap/non-implication |
| --- | --- | --- | --- |
| object and admissible class | exact object | exact object | why restricted/extended |
| dimension, boundary conditions, regime | exact scope | exact scope | comparability |
| conclusion | existence, inequality, classification, etc. | exact delta | which assertion is new |
| constant/rate/equality case | if relevant | if relevant | sharpness/rigidity |
| mechanism | precursor operation | present operation | what remains novel |

When two prior results improve different axes, record **incomparable frontier nodes**; never name a single strongest result by ignoring a competing dimension. If priority is disputed or unavailable, use qualified descriptions and disclose the unresolved evidence outside the manuscript. Use mathematical statements, not adjectives, to locate the contribution.

## 6. Integrate enough citations, but only where they work

A citation-worthy prose unit does one of four jobs: establishes origin; assigns exact prior credit; supports a theorem/method comparison; or anchors a mathematically useful adjacent connection. When literature is substantial, group by **question and achieved results**, not in author-year recital. Give direct predecessors a substantive sentence or comparison when the reader needs it; foundational and parallel work can be grouped concisely when their roles are genuinely shared.

Use `verified mathematical claim → named contribution and citations → remaining mathematical tension`. Credit must remain visible in the main Introduction, not hidden solely in the bibliography, a footnote or a supplementary ledger. It is permissible for the evidence dossier to contain many more sources than the Introduction: do not turn an Introduction into an encyclopedic review. Unused good sources may enter a genuine Related Work section, or remain in the dossier; avoid unnecessary citations.

## 7. Research stop and anti-false-completeness gate

Before drafting, answer:

1. Did the search include paths **outside** the supplied manuscript's references?
2. Are the historical source, benchmark, closest direct results, strongest relevant frontier, and method ancestry identified or explicitly recorded as not found/not accessible?
3. Were relevant recent and parallel developments checked, including competing claims and changed versions?
4. Can the reader distinguish imported ingredients from the present theorem's precise new step?
5. Is every strong historical/novelty claim supported by sources at the proper verification level?
6. Does each planned cluster of citations carry a distinct mathematical responsibility?

If a pivotal source is unverified, **do not silently pass the priority check**. Either continue searching, narrow the sentence, or report the blocker. If browsing is unavailable or the user disallows it, label the dossier `OFFLINE_INCOMPLETE`, do not claim novelty exhaustiveness or a complete frontier survey, and produce only wording justified by accessible records. A completed search is not proof that no uncatalogued work exists; avoid guarantees of exhaustive coverage.

## 8. Output and interaction with other modules

Record one compact `IntroductionLiteratureDossier`: date, scope/mode, query routes and access limits, selected-source evidence matrix, fair-credit map, theorem frontier, unresolved claims, and suggested citation locations. The source universe may be large, but the record should be concise and audit-friendly. It can be internal in an ordinary writing request; show a bibliography/link list when asked for related work, when priority is uncertain, or when the user expressly requests credit documentation.

Feed **verified** findings to the `IntroductionCoreBrief` and [Protocol 04v](04v_evidence_grounded_grand_narrative.md). For a complex parent program, deepen with [Protocol 04n](04n_mathematical_story_discovery.md); for scientific mechanisms, use 04k. Scholarly search never authorizes modifying the theorem or a protected Introduction. All actual citation insertion or bibliography edits obey Protocol 07 and the selected writing mode.
