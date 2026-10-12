# Protocol 04e — Introduction Prose Realization

## Purpose

For full reconstruction, write the Introduction from the authoritative `IntroductionCoreBrief` and the selected narrative arc. `IntroductionNarrativeLedger` and `IntroductionParagraphPlan` are optional planning aids for unusually complex cases, not default prerequisites. For a user-requested local revision, use the supplied Introduction as the baseline and preserve protected text. A positive writing example informs the explanatory choices; it does not automatically authorize rewriting it.

The goal is a mathematically continuous authorial voice: broad when the theorem earns breadth, compressed where the audience already knows the background, and explicit exactly where the problem changes state.

## 1. Draft through a mathematical question chain

Do not convert core-brief keys or optional ledger fields into prose in their stored order. Compose one continuous line of mathematical pressure. The previous paragraph should leave a question that the next paragraph answers or sharpens.

For each paragraph:

1. identify the new inference the reader must make;
2. state the mathematical subject early;
3. integrate history, literature, or formulas only when they support that inference;
4. stop when the mathematical state has changed;
5. end with the object, gap, or consequence that makes the next move necessary.

Several functions may coexist in one paragraph when they support the same information change. Do not split prose merely to satisfy a role table.

Do not write headings such as `Background`, `Literature`, or `Our contribution` unless the target journal or paper scale genuinely benefits from them.


## 1A. Reference-role separation and high-intensity microstyle

When a large Markdown style corpus and a separate research-article Introduction reference are both available, do not blend them indiscriminately.

- the Markdown corpus controls conditional microstyle: sentence/paragraph pressure, mathematical entry, bridge syntax, theorem-leadin restraint, and conceptual interpretation;
- the research-article Introduction reference controls macro narrative geometry, literature positioning, theorem scale, and editorial ambition.

Use `ConditionalStyleLedger` and Protocol 05n for the first role. Use `IntroductionNarrativeLedger` / `NarrativeAmbitionLedger` for the second. A textbook corpus must never manufacture priority rhetoric or journal-scale ambition.

## 2. Research-specialist compression

Assume the intended research audience knows standard material appropriate to the field, but not the new constructions of this paper. Prefer one precise sentence for familiar background; supply the explanation needed for a novel object or bridge. An operational interpretation of a formula is not redundant symbol-reading.

For a standard object, choose the minimum needed among:

- name the object;
- give the governing equation;
- state the relevant variational/spectral interpretation;
- cite a standard reference.

Do not automatically include physical motivation, elementary functional-analytic setup, or full definitions of standard Sobolev spaces in the Introduction.

### 2A. PDE coordinate discipline

When Protocol 04t is active, introduce only the equation, regime, solution class, topology, and assumptions on which the theorem's novelty depends. State the result delta on explicit axes. If prior results are incomparable, preserve that partial order instead of naming a fictitious single strongest predecessor. Distinguish the primary narrative arc from the result architecture: one continuous story may contain a threshold dichotomy, a regular/singular stratification, a two-level estimate-to-application hierarchy, or a solution-class separation.

Use the theorem-presentation mode selected in the PDE extension. A definition stack before the theorem is legitimate only when a blow-up, stratum, threshold object, admissibility class, or cross-field dictionary is needed to read the statement. Journal prestige is never a reason to delay or enlarge the theorem.

### 2B. Author-corpus supplement

When Protocol 05o is active, apply only stable abstract Introduction habits from `AuthorCorpusDossier`: opening scale, context-to-question speed, literature grouping, theorem latency, theorem-announcement cadence, proof-overview resolution, limitation handling, and organization-paragraph policy. The `IntroductionCoreBrief`, exact theorem facts, PDE result delta, and reader contract remain authoritative.

Do not reproduce a paper's opening sequence, distinctive wording, citation set, historical aside, or theorem-announcement formula. Coauthored evidence is corpus-associated, not individually attributed. In local polishing, preserve the accepted voice unless a concrete in-scope defect requires change.

## 3. Paragraph openings

Prefer mathematically led openings:

- object-led;
- theorem-led;
- conjecture-led;
- contrast-led;
- obstruction-led;
- result-led;
- return-to-main-thread through a named mathematical referent.

Use administrative openings sparingly. Repeated patterns such as
`In this paper`, `We now`, `More recently`, `It is worth noting`, `This result`, `The next step`, or `On the other hand`
create generated rhythm when they carry no mathematical information.

Do not repair repetition by rotating synonyms. Rewrite the underlying sentence around the mathematical subject.


## 3A. Specificity and the swap test

After drafting each substantial paragraph, replace the paper-specific nouns mentally by generic placeholders. If the paragraph would still fit many unrelated papers, it is too generic. Repair it with a non-transferable relation: the exact restriction, missing implication, lost invariant, scale transition, equality structure, or control supplied by the new method.

A paragraph may use a broad mathematical noun such as `rigidity`, `compactness`, or `duality`, but the same or following sentence must identify the concrete objects and operation. Do not end paragraphs with detachable claims that the problem is important, classical, rich, or widely studied.

## 4. Literature sentences are result-centered

The default sentence subject should be the theorem, phenomenon, or mathematical limitation—not the bibliography itself.

Prefer structures of the form:

`mathematical landmark → citation support → consequence for present question`

or

`strongest prior result → exact remaining gap`

rather than a serial sequence of author-centric sentences.

Cluster citations that support the same proposition. Separate works only when their mathematical roles differ.

Historical adjectives such as `classical`, `landmark`, `breakthrough`, or `seminal` are optional and require a reason. Supported authorial judgment may direct attention to the mathematical content: for example, “a surprising connection” should name the connected objects and explain the bridge nearby. Do not remove such language merely for neutrality, particularly when the user requested expressive positioning. Treat example wording as illustrative unless explicitly required verbatim. Unsupported evaluation remains a defect.

## 5. State difficulty as mathematics

Replace generic language such as `the problem is highly nontrivial` with the actual obstruction.

A good obstruction paragraph identifies:

- the natural mechanism one would try;
- the exact property it requires;
- the feature of the present problem that breaks it;
- the structural replacement used in the paper, if revealing it here helps the reader.

The paragraph should make the new method feel necessary rather than merely novel.

For a mechanism-heavy PDE argument, use at most a short causal obstruction stack: benchmark failure, nonlinear/global closure failure, and a terminal endpoint/top-order/compactness issue. Tie each retained layer to the operation that resolves it. Do not turn the Introduction into a catalogue of estimates.

## 6. Theorem announcement prose

Before a formal theorem, use only the orientation required to make the statement readable. Avoid ceremonial phrases such as `We are now ready to state our main result` unless a real logical threshold has just been crossed.

After a theorem, do not restate its formula in prose. Choose at most the functions actually needed:

- identify the conjectural implication;
- explain a surprising regime or endpoint;
- compare strength with prior work;
- explain why the quantitative refinement is needed later;
- identify a structural consequence.

A theorem ladder must read as an escalation of mathematical information, not as a list of accomplishments.

## 7. Macro-scale voice without hype

Use large mathematical nouns and precise relations rather than prestige adjectives. Breadth should come from linking:

`canonical problem ↔ classical benchmark ↔ unresolved obstruction ↔ present theorem ↔ broader consequence`.

Do not manufacture scale through phrases such as `deep and fundamental`, `far-reaching`, `major breakthrough`, or `long-standing problem` unless independently verified and genuinely needed.

## 8. Proof-mechanism exposition

For nonroutine mechanisms apply Protocol 04p only when the compact explanation in Protocol 04 is insufficient. Write the proof overview as a continuous causal mechanism, not a checklist. Its length follows the explanatory burden. Open the conceptual bottleneck and compress routine bookkeeping; a long outline is not evidence of completeness. Explain the original meaning and payoff of a central representation, then the remaining work needed to use it. Meaningful formula interpretation, conditional assembly of intermediate results, and a declared model case are allowed.

Each move should answer why the next move becomes possible:

`representation change → structural simplification → critical reduction → quantitative control → closure`.

When a PDE formula is decisive, interpret it in the original variables, name the adverse scale/sign/resonance/concentration it reveals, identify the control obtained, and connect that control to the continuation, bootstrap, rigidity, stratification, or limit-identification step. A named technique without this semantic bridge is not a proof explanation.

Use section numbers only after the mechanism is clear, and only if navigation helps.

When the main contribution is a conceptual bridge, apply the positive-example decisions in [the conceptual-bridge profile](../profiles/conceptual_bridge_introduction.md). Let the reader see the connection before expanding the technical route that makes it effective. This may require more space for one short derivation and less for a list of proof modules. Keep the prose centered on the mathematical discovery while making the remaining obstruction explicit. Do not enforce the displayed arrow sequence above as a paragraph template, and do not append every referee concern to the conceptual explanation. In unrestricted composition, integrate necessary qualifications at their first operative use; in a bounded edit, place them within the authorized region and record any limits that remain.

## 9. Continuity pass

After the first complete draft, read only the first and last sentence of every paragraph. They should form a coherent mathematical spine.

Repair any pair for which:

- the next paragraph introduces an unprepared object;
- the previous paragraph raises no reason to continue;
- the transition is merely temporal or administrative;
- a literature excursion does not return to the target problem;
- the theorem appears after several detachable background paragraphs.

## 10. Citation-prose pass

Read the Introduction again while ignoring uncited prose. Verify that every citation is attached to a concrete mathematical claim and that every literature paragraph changes the problem position.

Compress:

- strings of names with parallel verbs;
- multiple sentences that differ only by date;
- repeated `more recently` chronology;
- survey material not used in the theorem narrative.

## 11. Authorial naturalization specific to Introductions

Run an Introduction-specific naturalization pass after mathematical continuity is stable:

- vary paragraph pressure because roles differ, not for cosmetic variety;
- replace repeated meta-subjects (`we`, `this paper`, `this result`) with mathematical subjects when natural;
- remove redundant orientation already visible from notation or theorem statements;
- allow a short paragraph when a genuine return, obstruction, or theorem bridge deserves emphasis;
- avoid a uniform paragraph template of topic sentence + citations + concluding slogan.

## 12. Output

Produce the complete Introduction. Then run Protocol 04f. Run Protocol 04c only when a grand/program-level narrative was deliberately selected.

## 13. Strong verified claim realization

Before release, compare the prose against `NarrativeAmbitionLedger`. If a central verified contribution is marked `must_surface`, state it directly at its exact scope. Do not replace `resolves`, `complete`, `sharp`, `first global`, or an equivalent precise description by vague language such as `makes progress` merely to sound cautious.

This rule does not license stronger claims. The factuality ceiling remains binding.
