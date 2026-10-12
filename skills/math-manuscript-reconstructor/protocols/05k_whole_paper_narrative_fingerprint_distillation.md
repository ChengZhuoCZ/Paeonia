# Protocol 05k — Whole-Paper Narrative Fingerprint Distillation

## Purpose

Extract the global narrative decisions that govern an entire mathematical work while preventing chapter counts, section masses, front-matter ratios, appendix sizes, or source-wide order from becoming templates.

The output is a `WholePaperNarrativeFingerprintLedger`.

## Constitutional rule

A paper is not a row of equally weighted sections. Its global shape must reflect the dependency topology of the mathematics.

Whole-paper distillation asks:

- what is the paper's principal proof spine?
- when can the main result be stated readably?
- when does its proof actually become executable?
- where are the technical pressure peaks?
- which material belongs to the body and which material is genuinely modular?
- how much front matter is needed to orient the reader without replaying the proof?
- when has the paper mathematically ended?

It does **not** ask how to reproduce the source work's number of chapters, relative lengths, appendix count, or exact global sequence.

## 1. Corpus-type detection and research projection

First classify the style corpus broadly:

- research article;
- lecture notes;
- monograph/textbook;
- survey;
- thesis/dissertation;
- mixed corpus.

If the corpus is not a research article, extract only cross-format traits that survive projection to a research paper. In particular, a long expository work may support conclusions about:

- nonuniform mathematical mass;
- early orientation versus delayed technical execution;
- modular supporting theory;
- pressure peaks and returns to applications;
- asymmetry of major units;

but it does **not** directly support a target paper's section count, Introduction/body ratio, number of appendices, or location of the main theorem.

Set:

`long_expository_corpus_requires_research_projection: true`

when applicable.

## 2. Separate statement exposure from proof activation

Record three distinct global events.

### Main-result statement exposure

For a research article, the main theorem should normally become visible as soon as it can be stated accurately and readably.

Allowed modes:

- `EARLY_READABLE_STATEMENT` — the notation already exists or is light enough to introduce immediately;
- `MINIMAL_SETUP_THEN_STATEMENT` — a short block of definitions/normalizations is genuinely necessary before the statement;
- `RESULT_MAP_FOR_MULTI_THEOREM_PAPER` — several main results form one constellation and should be presented together before technical development.

Do not delay the principal result merely to recreate the chronology of discovery or the architecture of the source corpus.

### Proof activation

The proof may begin later than the statement if the target dependency graph requires an engine, compactness theorem, reduction, classification lemma, or regime analysis first.

Record one of:

- `DIRECT_AFTER_SETUP`;
- `ENGINE_DELAYED`;
- `MULTI_ENGINE_DELAYED`;
- `REGIME_DELAYED`;
- `AUXILIARY_THEORY_DELAYED`.

### Proof closure

Record where the final unresolved dependency of the principal result is discharged. A paper may continue after this only for mathematically justified consequences, applications, extensions, or classification corollaries.

Do not add a ceremonial conclusion merely because the proof closed before the final page.

## 3. Global proof-spine topology

Infer the topology of the target proof graph, not the source order.

Useful abstract labels include:

- `SINGLE_SPINE` — one dominant chain of reductions and lemmas;
- `ENGINE_THEN_ASSEMBLY` — one reusable mechanism supports several later claims before final assembly;
- `TWO_ENGINE_FUSION` — two genuinely different engines meet in the main proof;
- `REGIME_SPLIT_REJOIN` — several parameter/geometric regimes are handled separately and then recombined;
- `LOCAL_TO_GLOBAL` — local structure/stability/compactness is upgraded to a global result;
- `CONSTRUCTION_TO_RIGIDITY` — existence/construction is followed by uniqueness or equality analysis;
- `THEORY_APPLICATION_RETURN` — machinery is built and then applied back to the target problem;
- `CLASSIFICATION_FUNNEL` — many possible cases are progressively excluded until a complete classification remains;
- `COUNTEREXAMPLE_ESCALATION` — increasingly structured constructions culminate in the negative result;
- `MULTI_RESULT_CONSTELLATION` — several coequal theorems share one technical body.

These labels describe dependency topology only. They do not prescribe a fixed section sequence.

## 4. Technical-core distribution

A source corpus may reveal that mathematical pressure is strongly nonuniform. Distill this as a qualitative principle, not a mass target.

Classify the target paper's technical core only after the `ProofCoreGate`:

- `COMPACT_PEAK` — one section carries most delicate estimates;
- `BROAD_CORE` — one long central phase contains several tightly coupled arguments;
- `TWO_PEAK` — two different technical engines dominate separate regions;
- `CASCADE` — several increasingly strong lemmas form a rising technical sequence;
- `REGIME_CLUSTER` — the core is distributed across several regimes that later rejoin;
- `DISTRIBUTED_BY_NECESSITY` — no clean concentration exists because distinct parts are independently essential.

Never smooth section lengths or theorem density to make the paper look balanced.

A light conceptual or synthesis section beside a heavy technical section is normal when the mathematics requires it.

## 5. Front-matter compression

The Introduction is a lossy semantic projection of the closed proof body, not a miniature duplicate of it.

After `ProofCoreGate`, compress upward from the proof ledger and retain only what a reader needs before entering the body:

1. the problem and verified mathematical context;
2. the exact main result(s);
3. the principal obstruction or reason the problem is nontrivial;
4. the new mechanism at the level of ideas;
5. the shape of the proof spine;
6. central rigidity/equality information when it is one of the paper's contributions;
7. verified comparison with prior work.

Do not carry into the Introduction:

- line-by-line estimates;
- local parameter bookkeeping;
- internal lemma dependency lists;
- the same full theorem statement more than once;
- a section-by-section itinerary when the proof mechanism itself supplies a better map;
- claims not present in the closed body.

Corpus ratios such as `Introduction words / body words` are evidence about compression only and must never become target ratios.

## 6. One theorem statement, one global identity

The principal theorem should have one canonical semantic identity across the manuscript.

Preferred pattern:

- state it once in the Introduction or opening theorem block;
- later refer to it by number/name when beginning the proof;
- do not restate a near-identical version merely to fill the transition into the technical body.

A second formal statement is justified only if the body needs a genuinely different normalized/equivalent theorem whose equivalence is explicit.

## 7. Appendix necessity test

Appendices may contain substantial mathematics. They are not restricted to minor details. But every appendix must pass a modularity test.

Strong reasons include:

- the method is mathematically orthogonal to the main proof spine;
- the material is reused by several body sections;
- self-contained foundational material would otherwise interrupt the main argument;
- a lengthy verification is necessary for rigor but does not carry the central mechanism;
- an optional extension/generalization is logically separable;
- a computational/symbolic certificate needs independent verification space.

The following fail the appendix test:

- hiding a proof gap;
- exiling the central novel insight;
- exiling the main equality/rigidity argument merely because it is long;
- dumping unused material inherited from a source manuscript;
- moving reader-critical logic out of the body solely to reduce page count;
- preserving an old appendix because the source had one.

### Local versus global appendix

Use a local appendix/module when the material is owned by one section and has no downstream life elsewhere.

Use a global appendix when it is reused, independently referenceable, or genuinely foundational to several parts of the paper.

If the main theorem depends on an appendix, the body must state exactly what is imported and why that import is sufficient. The reader should understand the main mechanism without having to reconstruct it from an appendix.

## 8. Global asymmetry policy

Do not normalize the paper into equal section masses, equal theorem counts, or alternating conceptual/technical blocks.

Healthy asymmetry may include:

- a short setup followed by a long proof engine;
- a dense technical middle followed by a short assembly;
- one large regime section and two small exclusion sections;
- a brief rigidity endgame after a long existence argument;
- an application section shorter than the machinery it consumes;
- no conclusion section at all.

A section should be heavy because it carries difficult mathematics, not because neighboring sections are heavy.

## 9. Whole-paper closure

A pure mathematics paper is allowed to end immediately after the final mathematically meaningful event.

Valid endpoints include:

- main theorem proved;
- equality/rigidity proved;
- classification completed;
- final corollary/application established;
- optional extension completed.

A separate `Conclusion` or `Discussion` section is not mandatory. Add one only if it contributes mathematics, limitations, open problems, or a conceptual synthesis that is not already clear.

## 10. Evidence fields

The ledger may store aggregate evidence such as:

- major-unit word-distribution summaries;
- variation in formal-result density;
- broad concentration of technical mass;
- Introduction/body compression evidence;
- appendix count and broad mathematical load;
- evidence locators showing contrasting global functions.

All numerical evidence is diagnostic only.

The ledger must state:

`numeric_targets_forbidden: true`

`source_global_sequence_reuse: forbidden`

`source_mass_profile_reuse: forbidden`

`source_frontmatter_ratio_reuse: forbidden`

`source_appendix_pattern_reuse: forbidden`

## 11. Output contract

Return a `WholePaperNarrativeFingerprintLedger` conforming to `schemas/whole_paper_narrative_fingerprint.yaml`.

Mark every inferred rule as `SUPPORTED`, `TENTATIVE`, or `UNSUPPORTED`.
