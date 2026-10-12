# Protocol 05q — Authorial Prose Integrity and AI-like Residue Control

## Authority and aim

This protocol strengthens Protocols 05c, 05d, 05f and 05p. It applies to every **authorized** writing or polishing scope, including the Abstract, Introduction, statements, proofs and remarks. It does not authorize rewriting protected text or independent mathematical verification. Its goal is natural, serious, publication-grade mathematical writing whose syntactic decisions are justified by mathematical content. It is **not** an AI-detector evasion procedure, and it does not claim to measure authorship.

**Default:** choose and release one coherent English research-mathematics voice, unless the user explicitly asks for another language. Do not offer competing styles or author mimics. The house voice stays restrained in the Introduction as well as the proof body.

## 1. The paragraph is an argument, not a language template

Before changing a sentence, establish the paragraph's mathematical work. It must do something identifiable: introduce a precise object, locate the frontier, distinguish a hypothesis, enact a reduction, close a bound, compare regimes, explain the necessity of an auxiliary device, justify a nontrivial step, or articulate a verified consequence. If a paragraph's content can be transferred unchanged to an unrelated theorem, it requires mathematical specification or deletion (the *substitution test*).

In proofs, prefer a substantive local mathematical subject and an operative verb. A transition earns its place by identifying the actual obstruction, dependency or consequence. A roadmap is allowed when the argument has several non-obvious independent parts; a routine lemma needs no ceremonial opening. A proof may end immediately after the final justified inference. Do not manufacture symmetrical introductions, triplets of observations, fixed five-step proofs, or summative paragraphs to give the article visual regularity.

In the Introduction, make the intellectual scale arise from a *verified* parent program and an exact comparison with the pre-existing theorem frontier. Replace prestige rhetoric with mathematical relationships: which hypothesis was removed, what obstruction is new, which conclusion is strictly stronger, and what remains open. Give predecessors sufficient precise credit. The narrative must not become flat merely in order to be short, or florid merely to be long.

## 2. AI-like residue classes that require contextual review

Mark occurrences by document location, mathematical role, and disposition (`DELETE`, `COMPRESS`, `SPECIFY`, `RESTRUCTURE`, `KEEP`). A trigger is not a per se forbidden expression. Do not mechanically substitute synonyms.

- **A1. Generic field-level or novelty sentences:** e.g., assertions that a problem is fundamental, fascinating, rich, far-reaching or bridges areas without an exact demonstrated connection. Supply that connection or omit the claim.
- **A2. Administrative scaffolding:** repeated “we now turn to”, “the remainder is organized as follows”, “we are ready to”, “it is worth noting that”, or “in this section, we will”. Retain a genuine long-paper roadmap only when it helps with non-obvious navigation.
- **A3. Machine-balanced paragraph geometry:** repeated background → difficulty → contribution → takeaway pattern, every proof divided into identical numbered steps, equally sized consecutive paragraphs, or forced three-item recaps. Break the scheme according to the real dependency structure, not random variation.
- **A4. Explanation surplus:** restating a display, paraphrasing a theorem immediately after stating it, or repeating an earlier result as a mini-summary without adding a new logical function.
- **A5. Empty evaluative adverbs and assurances:** “clearly”, “obviously”, “remarkably”, “interestingly”, “crucially” as substitutes for a condition, estimate or argument. Standard mathematical adverbs are permissible when earned by the local inference.
- **A6. Diffuse agency:** stacks of nominalizations, repeated passive constructions or repeated “this observation/these considerations” without a stable referent. Prefer the object, hypothesis or estimate that actually acts.
- **A7. Unmotivated technical bulk:** displaying every routine manipulation with prose of equal intensity, or hiding the delicate uniformity, regularity, endpoint, compactness or equality passage under generic narration. Assign density by mathematical load.
- **A8. Whole-paper echo:** an Abstract, Introduction, outline, theorem comment and conclusion that all repeat the same contribution in nearly the same words, with no different reader function.
- **A9. Stylistic incoherence:** an excited, self-congratulatory opening followed by a proof memo, sudden tutorial voice, unnecessary rhetorical questions, or unnatural alternation of registers. Preserve one sober house voice.
- **A10. Artificial humanization:** injected mistakes, colloquial slang, contrived irregular punctuation, random sentence-length changes, fabricated personal history, copied authorial tics or detector-optimized obfuscation. These are prohibited repairs, not ways to pass an audit.

A genuine standard phrase appearing once, a necessary proof reminder, or an exact quotation with attribution is not residue merely because it resembles familiar academic language.

## 3. Three editorial passes, with mathematical safeguards

**Pass A — local precision.** Check the subject and verb of each paragraph and identify its *new mathematical information*. Delete empty sentences; replace generic clauses with their real objects; preserve assumptions, quantifiers, normalizations, constant dependencies, source credit and equality conditions. Do not create proof gaps by over-compressing.

**Pass B — cross-section rhythm and repetition.** Read the Abstract, first two Introduction pages, major theorem introductions and starts/ends of representative proofs in succession. Mark duplicated result announcements, repeated opening clauses, uniform paragraph architecture, redundant post-display prose and sections whose story resets. The remedy is reordering/omission/functional differentiation where permitted, not lexical randomization. Then read the whole draft without ledger headings.

**Pass C — cold mathematical reader.** At each surviving transitional sentence ask: “What precise mathematical inference would disappear if this sentence vanished?” If none, remove it. At each claim of importance ask for a theorem-level reason. At each compressed derivation ask whether a competent reader can reconstruct the omitted step without a hidden condition. Compare the Abstract, Introduction and formal result for exact agreement on novelty and scope.

For `LOCAL_POLISH`, check only the authorized prose, leaving good passages intact. If a recurring defect lies in protected content, **report** it and do not edit outside scope. For `RECONSTRUCT`, paragraphs must be newly composed from the mathematical ledger; never mask source copying with cosmetic rewriting.

## 4. Diagnostics and audit outcome

`tools/prose_residue_review.py` may flag recurrent phrases and a small set of high-confidence formulaic patterns in accessible `.tex` or plain-text source. The tool is a **review queue**, not an AI classifier; a clean run does not establish authentic authorship or high literary quality. Existing phrase recurrence, transitions, rhythm and equation/prose tools remain optional supporting diagnostics. No ratio or percentage of “AI-generated text” should be invented.

The editorial audit records for each material issue: **location → issue class → why it fails for this mathematical passage → allowed action → rechecked consequence**. Record only nontrivial findings; do not emit the ledger into the submitted paper. Gate `GENERATIVE-RESIDUE` passes when a complete relevant cold read finds no material unaddressed A1–A10 patterns and all mathematical integrity obligations remain satisfied. Diagnostic counts may motivate a check but are never numerical writing targets.

If a user supplies an external detector result, treat it as a tool-specific, unstable observation with model/version/document provenance, not as a calibrated probability or a contractual score. Improve demonstrably weak prose, but do not game a detector and never guarantee “0% AI”, “below 5% AI” or similar.

## 5. Release constraints

Before final delivery, apply `checklists/authorial_prose_integrity.md` together with the unified-voice checklist and Protocol 09a's independent no-box check. Neither a grammar checker nor a recurrence script may override mathematical truth, a verified quotation, protected editorial scope, or precise and sufficient attribution.
