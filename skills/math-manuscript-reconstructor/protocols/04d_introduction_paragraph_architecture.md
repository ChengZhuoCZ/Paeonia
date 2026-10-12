# Protocol 04d — Introduction Paragraph Architecture


> **Optional extended planning module.** Most Introductions should be drafted directly from `IntroductionCoreBrief` after selecting one narrative arc. Use this file only when multiple theorem statements, literature clusters, or long scientific/model context make a paragraph plan genuinely useful. Protocol 04 takes precedence.

## Purpose

Convert `IntroductionNarrativeLedger` into an ordered `IntroductionParagraphPlan` before any final Introduction prose is drafted. This is the missing layer between a correct narrative blueprint and natural research prose.

The Introduction is reconstructed **from scratch**. If a supplied manuscript already contains an Introduction, that text may contribute only verified mathematical claims, citation candidates, terminology, and historical facts. Its sentences, paragraph order, rhetorical sequence, theorem latency, and citation choreography are not a drafting template.

## 1. Choose the opening mode from audience and theorem

Select one opening mode:

- `CANONICAL_PROBLEM` — begin from a standard field-level problem whose relevance to the theorem is immediate;
- `LANDMARK_RESULT` — begin from a classical theorem whose unresolved extension leads directly to the paper;
- `CONJECTURE` — begin from a precise conjecture when it is the natural organizing object;
- `STRUCTURAL_TENSION` — begin from a contrast or obstruction that defines the current problem;
- `PHENOMENON` — begin from a mathematically striking phenomenon revealed or explained by the theorem;
- `PHYSICAL_ORIGIN` — begin from the scientific phenomenon or historical model that produced the mathematics;
- `SCIENTIFIC_MODEL` — begin from a canonical equation, energy, or model and explain why the focal regime is natural;
- `DISCRETE_CONTINUUM_TENSION` — begin from a continuous scientific/mathematical principle whose finite-complexity version creates the present problem.

For a specialist research audience, suppress textbook preliminaries unless they are needed to state the problem or explain the new mechanism. Standard definitions and elementary facts should not occupy the opening merely because they appeared in the source manuscript or reference paper. **Do not equate expert audience with removal of physical/scientific context.** If Protocol 04k selects `SUBSTANTIAL`, `PHYSICS_LED`, or `INTERDISCIPLINARY_LED`, scientifically operative background may occupy several opening paragraphs.

The opening must create two things at once:
1. a mathematically concrete object or problem;
2. a directional pull toward the exact theorem.

## 2. Assign one dominant function to each paragraph

Legacy documents called this “one dominant role.” In v1.36 the phrase means one primary information change, not one isolated database role; coherent secondary functions may be integrated.

Each planned paragraph records one primary information change. It may integrate several functions—history, literature, obstruction, theorem interpretation—when they jointly support that change. Role labels are diagnostic, not prose slots.

Recommended roles:

- `PROGRAM_ORIENTATION`
- `CANONICAL_PRINCIPLE`
- `SCALE_TRANSITION`
- `LIMITING_THEORY`
- `PARALLEL_FAMILY`
- `PROGRAM_RETURN`
- `FIELD_ORIENTATION`
- `CLASSICAL_LANDMARK`
- `CURRENT_FRONTIER`
- `NARROWING_TO_TARGET`
- `CONJECTURE_SETUP`
- `ADJACENT_PROBLEM_BRIDGE`
- `RETURN_TO_MAIN_THREAD`
- `OBSTRUCTION`
- `THEOREM_ORIENTATION`
- `FORMAL_THEOREM`
- `THEOREM_INTERPRETATION`
- `RESULT_LADDER_BRIDGE`
- `METHOD_POSITIONING`
- `PROOF_MECHANISM`
- `OPEN_DIRECTION`
- `SCIENTIFIC_PHENOMENON`
- `MODEL_ORIGIN`
- `MODEL_TO_MATHEMATICS`
- `PHYSICAL_PARAMETER_REGIME`
- `MATHEMATICAL_PHYSICS_LANDMARK`
- `SCIENTIFIC_TO_MATHEMATICAL_FRONTIER`
- `PHYSICAL_INTERPRETATION_OF_THEOREM`
- `SCIENTIFIC_RE_EXPANSION`
- `ORGANIZATION`

A paragraph is overloaded only when its functions do not support one coherent mathematical move. Do not split an effective integrated paragraph merely to satisfy the role inventory.

Conversely, several short paragraphs with the same role and no mathematical state change should be merged. Paragraph boundaries are caused by a change of mathematical obligation, not by visual variety.

## 3. Build the paragraph-link graph

For every paragraph record:

- `entry_anchor` — the mathematical referent inherited from the previous paragraph;
- `dominant_claim` — what this paragraph changes in the reader's understanding;
- `exit_anchor` — the object/question/result that makes the next paragraph necessary.

Adjacent paragraphs should normally share at least one mathematical referent: an object, conjecture, theorem, obstruction, method, or comparison class.

Administrative continuity such as `We now turn to...`, `Next we discuss...`, or `It remains to mention...` cannot substitute for a missing mathematical link.

## 4. Literature clusters, not bibliography paragraphs

Before drafting prose, group verified literature into claim-centered clusters. Each cluster must answer one mathematical question, for example:

- What is the classical benchmark?
- What is the strongest known result before this paper?
- Which neighboring result motivates the method?
- Which failed route exposes the present obstruction?

Within a cluster, mathematical content comes first and names/citations support the claim. Avoid a paragraph whose only internal logic is chronological author order.

A literature cluster that can be removed without changing the reader's understanding of the theorem's position is detachable and should normally be deleted or compressed.

## 5. Theorem cadence

Separate three functions:

- `THEOREM_ORIENTATION` — a concise conceptual statement of what changes;
- `FORMAL_THEOREM` — the exact reader-facing theorem;
- `THEOREM_INTERPRETATION` — a consequence or meaning that is not obvious from the displayed statement.

Do not stack multiple formal theorems without narrative work between them. A genuine theorem ladder should contain a mathematical bridge explaining why the next result is stronger, more quantitative, more global, or structurally different.

Do not delay the main theorem merely to create drama. Once the problem, normalization, and significance are readable, the reader should be allowed to see the result.

## 6. Adjacent-problem excursion and return

An adjacent problem needs both an entry reason and a return route.

Record:

`shared structure → useful neighboring result → decisive difference → consequence for present method → return to current problem`

If the paragraph never changes how the reader understands the present obstruction or theorem, remove it.

## 7. Density policy

Assign each paragraph one of:

- `LEAN` — orientation, return, theorem bridge, closure;
- `MEDIUM` — literature positioning, conceptual comparison, theorem interpretation;
- `THICK` — a genuine obstruction, a delicate historical frontier, or a mechanism explanation that requires several linked facts.

These labels are qualitative. Never fit paragraph word counts to a reference paper.

## 8. Display policy

Use a display in the Introduction only when it carries one of:

- the central PDE/variational problem needed to orient the reader;
- a main conjecture;
- a main theorem;
- a quantitative formula whose structure matters to the paper's contribution.

Do not reproduce standard definitions, auxiliary function spaces, routine spectral sequences, or proof-local formulas merely because they occur early in the body.

## 9. Detachability test

Before prose drafting, test each planned paragraph:

> If this paragraph is removed, what mathematical connection, historical position, obstruction, theorem interpretation, or proof mechanism becomes unavailable?

If the answer is `none`, delete or merge the paragraph.

## 10. Mathematical-story paragraph branch

When `MathematicalStoryLedger` is required, apply `protocols/04o_mathematical_story_integration.md` before the scientific-context branch. The paragraph plan must preserve the primary story archetype through explicit mathematical anchors.

When the story module is triggered, preserve the selected mathematical transition somewhere before or around the theorem. It need not occupy a dedicated program paragraph, and no separate return paragraph is mandatory.

Do not satisfy this requirement by inserting a generic opening paragraph about the field.

## 11. Scientific-context paragraph branch

When `ScientificContextLedger.context_depth` is not `NONE`, apply `protocols/04l_scientific_context_integration.md` before finalizing the paragraph-link graph. Scientific paragraphs must carry a return anchor to the focal mathematical object. Multi-paragraph context is allowed when the model chain itself is necessary for the theorem to be legible.

## 12. Output

Produce `IntroductionParagraphPlan`. Do not write final Introduction prose in this protocol.
