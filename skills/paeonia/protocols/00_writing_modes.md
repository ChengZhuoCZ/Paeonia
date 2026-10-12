# Writing modes — reconstruct or locally polish

Resolve **task kind, writing mode, and editable scope separately**, from the current request and still-active prior constraints. These instructions govern the applicability of older reconstruction protocols, profiles, manifest defaults and gates. A request to review or develop the skill does not itself authorize manuscript editing.

## Choosing a mode

**Ask first:** before new manuscript-writing work, ask “这次希望全文重构，还是局部润色？” and wait for the answer before changing prose. An explicit mode choice already given for the current task, including a precise passage-only replacement instruction, suffices; do not ask again during continuation. Read-only inspection may proceed while awaiting the choice. A skill-development request itself does not trigger this manuscript question.

| Mode | Baseline and permitted change | Success criterion |
| --- | --- | --- |
| `RECONSTRUCT` — 重构写作 | Treat mathematics as evidence. Independently choose exposition, grouping and language within the authorized region; do not use source prose as a paraphrase template. | A coherent new exposition with faithful mathematics, visible contribution and an intelligible proof route. |
| `LOCAL_POLISH` — 局部润色 | Treat the selected draft as the text to preserve. Keep its voice, narrative, paragraph order and unaffected wording; change only what a concrete requested improvement requires. | The identified problem is resolved with the least disruption to effective prose and meaning. Unchanged output is valid. |

Mode specifies **depth of intervention**; scope specifies **where**. Reconstructing only an Introduction does not authorize rewriting the proof. Polishing throughout a paper does not authorize a new paper architecture. Neither mode licenses changing theorem semantics or inventing supporting literature.

### Author-corpus supplement

For a proof-bearing writing task, Protocol 05p fixes one consistent mathematical editorial voice without any style-choice prompt. Protocol 05o may examine a corpus **only when the user has already supplied an author or exemplar for style evidence**; never ask for the author by default. This does not change the selected writing mode.

- In `RECONSTRUCT`, a verified and quarantined author corpus may inform newly composed Introduction and proof prose through abstract traits only.
- In `LOCAL_POLISH`, the accepted manuscript remains the primary voice. Author-corpus evidence may support a diagnosed local repair but may not trigger wholesale restyling.
- A style download never expands editable scope, supplies theorem facts, or authorizes new citations.

- “从头重写 / 重构全文 / 重新组织论证和叙事” selects reconstruction in the named scope.
- “润色 / 微调 / 修正局部 / 保留语言只改记号” suggests local polishing, but does not replace the initial mode question when the user has not yet selected a mode; precise notation-only or passage-only instructions already define local scope. “太平淡 / 思路不清 / 学习某人的 intro” identifies a goal or reference, not automatic permission to replace the user's prose.
- A later “再润色一遍” retains the accepted baseline, mode and boundaries. “用新 skill” changes the guidance, not the editing permission. An explicit later request to reconstruct a region changes the mode there.
- For mixed work, apply modes per region: e.g. reconstruct the proof outline, locally correct notation in the opening, preserve the remaining text. Do not relabel the entire document as reconstruction. Identify the input version before using page boundaries; use source anchors because pagination may change.
- If the mode has not been explicitly selected, ask the question above rather than starting from an inferred default. Once selected, clarify scope only when it cannot be recovered from the request or prior constraints. Do not turn the initial mode question into repeated approval requests for ordinary edits within that scope.

## Local polishing path

1. Identify the accepted editing baseline and permitted changes, including any protected prose, pages, formulas or regions. Read relevant proof passages as trusted evidence; keep the baseline available throughout.
2. Locate the actual deficiency: notation conflict, inaccurate restatement, missing causal step, unclear referent, or unnecessary reader effort. Retain successful passages. Apply the relevant explanatory protocol diagnostically rather than running all reconstruction passes.
3. Make the smallest **sufficient** repair. This may add a needed explanatory sentence or locally recast an unclear one; it does not mean optimizing a word-change count. Preserve the voice, emphasis and narrative sequence. Global reordering, rewriting an effective paragraph or adding a new literature excursion requires reconstruction authorization for that region.
4. Compare against the baseline, including protected regions. Check changed hypotheses, signs, normalizations, exact/asymptotic status, parameter ranges, notation, citations and section references against the supplied source. Record any necessary local factual correction and its evidence. An unresolved mathematical issue remains a reported issue, not a silent new proof.
5. Deliver the revised requested file and a short location–change–reason list when edits are substantive or the user requested a list. Compile modified TeX and check relevant layout/reference effects when a compilable source and tools are available. Do not produce a new manuscript version merely to demonstrate activity when nothing needs changing.

**Bypassed in local polishing:** source-prose quarantine, source-overlap penalties against the user's baseline, fresh architecture, proof-body-first redrafting, full corpus distillation, new proof closure certification and the full reconstruction artifact set. Borrowed third-party style text still cannot become a sentence bank. Existing abstract style observations may guide an authorized edit; preserving the author's voice takes precedence over making it resemble a reference author.

The new-change comparison checks editorial fidelity; it is not an independent correctness audit. Read broadly as needed to understand a local claim, but do not thereby enlarge the writable scope. A notation replacement that would affect a protected region must be adapted to that boundary or reported as needing wider scope.

## Reconstruction path

For a whole-paper reconstruction, use the existing proof-first route: extract mathematics, choose writing order and notation, reconstruct the proof, check faithful coverage, then build theorem framing and front matter.

For a selected-region reconstruction, extract only the mathematics and dependencies needed there; compose that region anew and preserve everything outside it. An existing supplied proof is sufficient trusted evidence for rewriting its Introduction or outline. Do not require a new proof body or claim a fresh `ProofCoreGate: PASS`. Choose structure and explanatory detail within scope; keep formulas and restated results traceable to the body. A supplied user-selected passage that remains protected is an editing baseline, not quarantined style data.

Check a reconstructed region for mathematical fidelity, causal readability, source-prose independence where reconstruction is authorized, and its interfaces with retained text. A full-paper architecture score must not force changes to a protected region.

## Optional planner integration

Ordinary writing needs no machine plan. If the existing execution planner is used, record:

```yaml
writing_mode: LOCAL_POLISH       # or RECONSTRUCT
editable_scope: [Introduction]   # whole_manuscript is also valid
protected_scope: [proof_body]
has_editing_baseline: true       # required for LOCAL_POLISH
```

`LOCAL_POLISH` routes to `EDIT → AUDIT → RELEASE` after task/plan setup. It does not require a pre-existing proof gate or semantic-checksum artifact. `RECONSTRUCT` with a bounded explicit scope routes to `SCOPED_RECONSTRUCTION`, using trusted mathematical sources and scoped extraction before `EDIT`; `EDIT` performs the selected-region composition as well as refinement. Whole-paper reconstruction retains the existing full route. Existing named workflows remain compatible, but a contradictory explicit mode is rejected rather than silently overriding it. Review-only and style-extraction-only workflows have no writing mode.

Protected scope is a preservation instruction, not a text-locking implementation: the planner records boundaries and blocks additions to the local/scoped state sequence, while the editor must verify the actual document diff. For mixed modes use one scoped plan per region. Never use optional director advice to expand the selected mode or scope.
