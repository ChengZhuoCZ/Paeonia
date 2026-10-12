# Protocol 04q — Introduction-only comprehension check

## Scope

Read the Introduction and its proof outline while the body is closed. Assume the stated audience's standard background, but no knowledge of this paper's proof. Inspect the body afterward only to check fidelity. This is an editorial read, not proof verification.

Do not certify comprehension from keywords, sentence counts, source labels, or a filled ledger. A route may have all of them and still fail to explain a single step.

## Recover the argument

Answer in your own words, using only the visible prose:

1. What does the main theorem say, in what regime, and what remains beyond its scope?
2. Why does the obvious or existing information fail to settle it? Name the specific loss.
3. What is the central change of viewpoint? What do its objects mean in the original problem?
4. Which part of the connection is exact, and which still needs an estimate or reconstruction?
5. What capability does the new formulation provide? Why is that capability relevant to the target?
6. For every indispensable stage, what enters, what exits, and what becomes possible afterward? At the conceptual bottleneck, what visible mathematical reason explains how the claimed improvement is obtained?
7. Where is the hard part, and what distinguishes its solution from the first inadequate bound?
8. How do the components yield the conclusion, including equality or rigidity if claimed?

For each difficult inference, identify the actual sentence or formula that licenses the answer. A paragraph locator alone is insufficient if the paragraph only names the technique. If the answer needs a proof-body definition, reference number, or the evaluator's memory to supply the missing idea, flag the exact first point of failure. Omit questions genuinely irrelevant to a short routine argument; do not manufacture a reformulation or bootstrap to fill the checklist.

## Perturbation checks

Before checking individual dependencies, recover the central mathematical relation in ordinary language and point to the calculation or construction that makes it intelligible. Then say what obstacle survives it. If the answer is only a list of tools, the draft may have passed coverage checks while failing to communicate its conceptual center. A contribution need not be a reformulation; use the corresponding decisive estimate or construction when that is what the paper offers.

Use the applicable checks, with an actual answer rather than a yes/no assertion:

- **Technique-name removal:** replace names such as “quadrature,” “neck,” or “constraint chart” mentally by “this tool.” Does the neighboring prose still say what the tool accomplishes?
- **Bridge deletion:** remove the explanation of the representation change. If the route reads identically, the deleted passage may have been labeling rather than explaining. Conversely, if a necessary inference breaks, preserve or improve the explanation.
- **Weaker-estimate substitution:** replace the decisive estimate by the natural weaker one described in the text. Can the reader locate exactly where the proof no longer closes?
- **Tiny-defect test:** when relevant, hold the external parameter fixed and consider successively smaller positive defects. Does the stated error control still support the claimed exact conclusion in its stated class?
- **Bootstrap entry test:** list what is known before geometric or analytic regularity is obtained. Does the first improvement already require the regularity it is meant to prove?
- **Return test:** can the reader get back from the auxiliary equality case to the original theorem without inventing realizability, normalization, or a missing reconstruction result?
- **Choice test:** why this new object, rather than merely renaming the old one? Recover the compatible requirements it meets, using the visible text. Do not demand a catalog of rejected methods.
- **Judgment test:** when the prose calls something surprising, unexpected, or elegant, what specific relation or economy supports the judgment? If the adjective is removed, the mathematical explanation should survive; if the explanation is removed, the adjective should visibly become unsupported. Neither absence of adjectives nor inclusion of a requested example phrase is a quality criterion. Does the wording fit the particular mathematical assessment, and do repeated announcements across the abstract and Introduction add substance?
- **Neighbor test:** when broader relevance is claimed, can a reader name the corresponding object or operation in the other field, the exact status of the connection, and the additional work needed here? Merely recognizing a famous author's name fails this test.
- **Resolution test:** which proof details can be grouped without losing a necessary inference, and which distinction must remain visible? For a repeated tool, can the reader distinguish a first use that obtains admissible inputs from a later use that exploits them? Do not reward a longer list of stages merely because each stage has a correct purpose.

These checks diagnose prose; they do not authorize new mathematical arguments or generic theorem strengthening.

## Repair at the missing link

Expand the first missing explanation, remove a premature technical name, supply a minimal definition, or bring an intermediate result's use before its technical discussion. Then read again. Do not compensate by adding general praise, historical background, or a list of section titles.

Select a repair for its effect, not its size. If a longer rewrite still requires the same unstated inference, reject that rewrite. If a standard module's purpose and applicability were already clear, leave it compact. A supplied model must retain the obstruction; a model that assumes away the hard case cannot count as a successful explanation.

A short formula with an explained implication may repair more than a paragraph of summary. A worked model is appropriate only when its assumptions and limitations are explicit. Permit the outline to become longer if that is needed to communicate an indispensable mechanism.

## Report and integration

Record the reader answers, first missing link, repairs, and remaining limitations in the existing `IntroductionProseAudit`. A failed applicable comprehension check blocks `INTRODUCTION-PROSE-INTEGRITY`; the existing gate owns the repair. No additional gate or mandatory subagent is required.

A same-agent read is vulnerable to knowing the proof already. Record it as a manual assessment supported by text-level evidence, not as a fresh-reader result. If a reader test was not independently performed, say so. Do not infer failure merely from its absence; complete the authorized editorial task and describe the actual validation scope. If user feedback contradicts the self-assessment, treat that as evidence to revise the explanatory decision, not as something a completed checklist overrides.

`tools/proof_explanation_audit.py` checks the dependency and evidence structure of the internal record. Its `STRUCTURE_OK` result is not a prose-comprehension pass; the cold read above remains necessary. Explicitly distinguish manual review, deterministic checks, and any independently performed evaluation. Never claim a fresh-agent test when none was run.

A successful introduction-only read does not establish that a referee can verify the body. For a requested submission or referee assessment, continue with [Protocol 04r](04r_referee_perspective.md), focusing on the decisive argument rather than repeating this comprehension checklist.

## Requested apply–compare–adjust replay

When the user requests a skill replay against a preferred Introduction or Abstract (for the latter, also read [Protocol 04s](04s_abstract_calibration.md)), apply the currently released skill within the active editing boundaries and preserve the actual candidate before changing the skill. Compare that candidate with both the user's reference and the accepted manuscript baseline. Distinguish repairs inherited from the baseline, new changes in the candidate, and later repairs made after comparison. An unchanged candidate is valid if no further edit is justified; do not manufacture differences to prove that polishing occurred.

Assess a concrete reader inference gained and the cost paid for it. A target can be elegant yet omit a needed proof interface; a corrected candidate can be more accurate yet become dense or lose the original narrative. Preserve both observations. Do not rank drafts by recency, length, adjective counts, or how many conditions they mention. If a local edit clarifies one operation, do not claim it improves the whole Introduction.

Count only generated or edited passages as generative evidence. Preserving a strong Fourier bridge or an effective outlook demonstrates fidelity, not the ability to write one from raw mathematics. Describe same-agent, context-aware review as such; it is neither a blind test nor independent reader validation. Package checks establish integrity, not future prose quality.

Change the narrowest existing instruction that explains an observed decision failure. If no such failure remains in the current scope, record why plausible further edits were rejected and retain the current manuscript; do not duplicate unchanged public TeX/PDF files or invent a writing rule merely because another iteration was requested. A repeated read of the same reference is not a new independent validation sample. Consolidate repeated case observations instead of accumulating prescriptions. New reader feedback or new mathematical evidence may reopen a specific passage; a scope-bound stopping point is not a claim of universal quality. Do not turn the reference into a paragraph template or the user's preference into a rule for every manuscript. Keep the actual outcome and its limitations in one traceable review record.
