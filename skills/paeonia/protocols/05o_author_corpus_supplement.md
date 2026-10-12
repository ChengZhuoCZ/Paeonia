# Protocol 05o — Author-Corpus Acquisition and Writing Supplement

## Purpose

The skill does **not** ask the user to choose an author or language style. This supplement activates only when the user has already supplied a named author, an exemplar corpus, or a direct instruction to study a specific style reference. This protocol preserves the existing reconstruction and local-polish routes. It adds a **small, evidence-controlled author-associated corpus** that supplements, but never replaces, the mathematics-first Introduction engine, the user's baseline prose, or the ordinary style firewall.

The objective is not to “write like” an identifiable person. It is to learn supported, high-level decisions about Introduction architecture and mathematical exposition: how a problem is entered, how literature is grouped, when the theorem appears, how a proof mechanism is explained, and how formulas and prose interact.

## 1. Trigger — user-provided evidence only, no style selection

Activate only when **all** of the following apply:

1. the user has *already volunteered* a style-author name or exemplar/corpus, or explicitly requested study of a specified reference;
2. the proof-bearing manuscript and authorized scope are known;
3. the work is substantial enough for such evidence to help, and access/rights permit it.

**Do not ask for an author, the preferred style, an exemplar, or an opt-out; do not pause drafting for a style preference.** Without qualifying evidence, use Protocol 05p directly. An explicit opt-out is honored. Skip automatic acquisition for a mechanical notation fix, bibliography-only repair, translation, proof verification without a writing deliverable, or forbidden browsing. For a user-named reference that cannot be disambiguated, request the missing identity detail only if the user specifically requires that reference; otherwise omit the supplement and proceed.

## 2. Identity resolution before download

A name is not an identity. Resolve the intended scholar using as many of the following as needed:

- current or historical affiliation;
- research field and subject overlap with the supplied proof;
- ORCID or institutional profile;
- personal homepage or public CV;
- arXiv author identifier;
- stable coauthor network;
- DOI/Crossref/OpenAlex/zbMATH-style publication metadata.

For a common or ambiguous name, do not guess. Ask only for the missing disambiguator that cannot be recovered from the proof, manuscript metadata, or public record. Record an identity-confidence level: `CONFIRMED`, `HIGH`, `MEDIUM`, or `UNRESOLVED`. `UNRESOLVED` blocks author-specific attribution but not ordinary writing.

If the user supplies multiple named references without designating a primary one, select the best-supported subset for the task and resolve conflicting traits under Protocol 05p; do not ask the user to choose among styles. Do not silently merge authors into a fictitious individual style.

## 3. Legal and version-controlled acquisition

Use only legally accessible copies:

1. author or institutional pages;
2. arXiv or another recognized preprint repository;
3. open journal versions;
4. institutional repositories.

Never circumvent a paywall or access control. When a publisher version is closed but an author manuscript is open, use the author manuscript.

For style analysis, prefer the latest author-prepared preprint or accepted manuscript over a heavily copyedited publisher PDF. Record:

- title and complete author list;
- year and venue/status;
- DOI and/or repository identifier;
- exact version/date;
- source URL or stable locator;
- local path when downloaded;
- SHA-256 hash;
- whether the copy is author-prepared or publisher-edited.

The paper inventory is reproducibility metadata, not a bibliography to paste into the target manuscript.

### 3.1 Retrieval execution

Build the candidate bibliography before downloading full text. Prefer primary scholarly records and the author's own publication list for identity and version resolution. For each selected item:

1. verify the complete author list, title, year, and stable identifier against a primary repository or publisher record;
2. locate a legal full-text author manuscript, preprint, accepted manuscript, or open publisher copy;
3. download the complete file to the task workspace rather than relying on a search-result snippet or abstract page;
4. reject corrupt, incomplete, abstract-only, or mismatched files;
5. record the exact file hash and version before analysis;
6. extract the complete Introduction and only the functionally selected body windows required by the task.

Do not ask the user to upload papers that are already available from a verified legal source. Do not treat search snippets, automated summaries, citation pages, or bibliographic abstracts as style evidence. If the only discoverable copy is inaccessible, record the candidate as unavailable and select another representative paper or fall back without the supplement.

## 4. What counts as a representative “core” corpus

Do not rank papers by citation count or journal prestige alone. Build a candidate inventory, then select a balanced default corpus of **four papers**; use three to six when availability or authorship structure requires it.

The selected set should cover, with overlap allowed:

- **topic-near:** usually two papers closest to the supplied theorem or PDE mechanism;
- **author-central:** a work identified on the author's selected-publications page, CV, survey, or later research program as central;
- **recent:** at least one recent paper that reflects current habits;
- **authorship-control:** a sole-authored paper when available, otherwise papers from different coauthor configurations;
- **genre-match:** research articles rather than only surveys, lecture notes, or books when the target is a research paper.

Prefer a spread across years and collaborators sufficient to separate a stable corpus pattern from a single project's local editing. When the author has changed fields or writing language, weight papers matching the target field, genre, language, and current period.

Record why each paper was selected and why plausible candidates were excluded. If fewer than three usable papers exist, mark the profile `LOW_EVIDENCE` and do not claim a stable author habit.

## 5. Sampling windows

Read the complete Introduction of every selected paper. To infer broader writing habits, also sample functions rather than attractive passages:

- theorem lead-in and formal statement;
- proof overview or organization paragraph;
- a routine proof opening;
- a delicate estimate, compactness, endpoint, or rigidity passage;
- a method-change bridge;
- a proof closure or return to the main argument;
- section openings when section architecture is in scope.

For an Introduction-only task, the body sample may remain light, but do not infer proof-writing habits from Introductions alone.

## 6. Attribution and confidence

A coauthored paper does not reveal who wrote a sentence. Use the following evidence classes:

- `SOLE_AUTHORED_EVIDENCE` — stronger evidence, still conditioned by period and topic;
- `CROSS_COLLABORATION_STABLE` — a trait recurs across at least three papers and at least two coauthor configurations;
- `COLLABORATION_ASSOCIATED` — recurrent only inside one coauthor cluster;
- `TOPIC_CONDITIONED` — recurrent only in one equation, method, or genre;
- `TENTATIVE` — supported by one paper or one window;
- `UNSUPPORTED` — omit from realization.

Describe the result as an **author-associated corpus profile** unless sole-authored evidence and cross-collaboration stability justify stronger wording. Never infer personality, intention, competence, or who drafted a coauthored passage.

## 7. Distillation targets

### 7.1 Introduction supplement

Extract only abstract decisions such as:

- opening scale: equation/problem/benchmark/history/model;
- speed from context to exact mathematical question;
- literature grouping: claim-centered, chronological, or problem-axis based;
- treatment of incomparable prior results;
- theorem latency and presentation mode;
- use of informal previews before formal statements;
- post-theorem interpretation;
- proof-overview resolution and causal structure;
- handling of assumptions, limitations, and open regimes;
- use or suppression of an organization paragraph;
- first-person and certainty calibration.

Feed these decisions into Protocol 04 and, for PDE papers, Protocol 04t only after theorem facts and the `IntroductionCoreBrief` are locked. The corpus affects realization, not the mathematical narrative's truth conditions.

### 7.2 Mathematical-writing supplement

Extract high-level habits already represented by Protocols 05a–05n:

- proof openings and strategy signals;
- local-goal and obstruction visibility;
- theorem/lemma insertion logic;
- equation–prose integration;
- justification locality;
- transition semantics;
- paragraph pressure by mathematical role;
- approximation, special-to-general, and closure movement;
- notation preferences only when collision-free and subordinate to the target mathematics.

Do not build a lexical inventory, phrase bank, punctuation caricature, or distinctive sentence template.

## 8. Priority and scope

Apply this priority order:

1. mathematical correctness and exact theorem semantics;
2. explicit user instructions and target-journal requirements;
3. the accepted `LOCAL_POLISH` baseline and protected scope;
4. field conventions and reader needs;
5. **Protocol 05p's unified voice**, governing the manuscript-wide register;
6. compatible stable author-corpus traits, as soft evidence only;
7. generic cosmetic preferences.

No extracted author trait may replace the house register or generate competing stylistic versions.

For `RECONSTRUCT`, the supplement may guide newly composed proof prose and front matter after extraction and quarantine.

For `LOCAL_POLISH`, the existing manuscript voice remains primary. Use author-corpus evidence only to repair a diagnosed, in-scope weakness. Do not rewrite an effective paragraph merely to increase resemblance to the corpus.

For a bounded Introduction reconstruction, use the proof as trusted evidence, acquire the corpus if activated, and rebuild only the authorized Introduction. Do not reconstruct the protected proof body.

## 9. Separation from literature research

Author papers downloaded for style are not automatically evidence for:

- novelty or priority;
- the pre-paper frontier;
- historical claims;
- theorem applicability;
- scientific interpretation.

Any such use must separately pass Protocol 07 with exact bibliographic and claim support. Conversely, a paper may be used as literature evidence without being admitted to the style corpus.

## 10. Quarantine and overlap protection

After `AuthorCorpusDossier` and the applicable style ledgers are built:

- quarantine all downloaded papers;
- compose from abstract traits only;
- do not consult passages sentence by sentence;
- run source/style overlap checks on final prose when substantial corpus influence was used;
- reject distinctive phrase reuse, near-paraphrase, paragraph-sequence copying, theorem-announcement imitation, and imported examples or historical asides.

A successful supplement should be visible as better mathematical pacing and emphasis, not verbal resemblance.

## 11. Failure and fallback

Proceed with the ordinary writing route when:

- identity remains unresolved;
- no legally accessible full text can be found;
- fewer than three representative papers are available;
- the corpus is too heterogeneous to support stable traits;
- the user's baseline already supplies a stronger authorial signal;
- the user opts out.

State the limitation briefly. Do not delay or weaken the underlying reconstruction or polishing task.

## 12. Required record

When activated, create `AuthorCorpusDossier` containing:

- user request and selected author role;
- identity evidence and confidence;
- candidate inventory and selection rationale;
- selected-paper metadata, versions, locators, paths, and hashes;
- corpus balance by topic, year, genre, and coauthor configuration;
- sampled mathematical functions;
- supported traits with evidence class and confidence;
- unstable or rejected traits;
- attribution caveats;
- application scope and priority;
- quarantine and overlap-audit status.

The dossier stores no source sentences.
