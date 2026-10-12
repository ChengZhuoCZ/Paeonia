# Naber corpus: Introduction and proof explanation

## Evidence and limits

This is a qualitative distillation of selected Introduction and proof-outline windows from ten downloaded papers: nine research papers and one lecture-note supplement. Six research papers informed the candidate rules; two were read afterward as held-out checks; one sole-authored research paper checks how the approach behaves across fields. The research set is coauthored except for *Characterizations of Bounded Ricci Curvature*. Observations belong to these papers, not demonstrably to one person's contribution to their writing.

See [the inventory](../references/naber_corpus.json) for exact versions, URLs, download hashes, page windows, and roles. PDF page locators refer to those downloaded versions. Full proofs were not audited. This is not a statistical author fingerprint, a comprehensive survey, or evidence of priority for the target manuscript. The harmonic-map and varifold papers share a method family, so agreement between them is not independent replication. The sole-authored lecture notes are pedagogical support, not a research-article length model.

## Source observations

| Source / locator | Explanatory decision observed | Conditional lesson |
|---|---|---|
| Cheeger–Naber, *Lower Bounds on Ricci Curvature and Quantitative Behavior of Singular Sets*, §2, PDF pp. 7–9 | A Cantor model previews the estimate; the text then identifies the missing multiple-scale issue and explains how grouping bad-scale patterns addresses it. | A toy model earns its place by exposing both the mechanism and the complication it omits. |
| Cheeger–Naber, *Regularity of Einstein Manifolds and the Codimension 4 Conjecture*, §1.1, pp. 5–8 | The hoped-for splitting property is too strong; allowing transformations of the image recovers the property actually needed. The outline first shows what slicing would accomplish in the blow-up argument. | A reformulation becomes intelligible when the reader sees what was unnecessarily demanded and what weaker, attainable structure suffices. |
| Naber–Valtorta, *Rectifiable-Reifenberg and the Regularity of Stationary and Minimizing Harmonic Maps*, §§1.1, 1.4, pp. 5–6, 10–13 | The text contrasts infinitesimal symmetry with finite-scale symmetry, explains the gain from summing energy drops, and links subspace approximation to the Reifenberg criterion. | Explain why the new quantity is stronger in the relevant sense, and show how one estimate supplies another theorem's hypothesis. |
| Jiang–Naber, *L2 Curvature Bounds on Manifolds with Bounded Ricci Curvature*, §1.3, pp. 6–12 | A neck example precedes structure estimates; local estimates plus a content bound visibly assemble the global estimate. The apparent regularity loop is stated rather than hidden. | State what a module buys before expanding its hard proof. Make bootstrapping dependencies explicit. |
| Naber–Valtorta, *Energy Identity for Stationary Yang Mills*, §1.3, pp. 5–8 | Bubble and annular pieces have different explanatory weight. A short summation closes one target conditionally; the discussion returns to the annular estimates and the gauge obstruction. | Allocate attention asymmetrically and show the purpose of decomposition and gauge choices. |
| Edelen–Naber–Valtorta, *Quantitative Reifenberg Theorem for Measures*, §2.5, pp. 14–16 | Examples limit what beta-numbers imply. Naive iteration accumulates errors; good/bad trees have complementary strengths that offset those losses. | Explain a failed iteration concretely and identify the mechanism controlling cumulative loss. |
| Naber, *Characterizations of Bounded Ricci Curvature on Smooth and Nonsmooth Spaces*, §§1–2.1, pp. 5–7 | Moving to path space is tied to characterizing two-sided curvature bounds and then defining curvature for nonsmooth spaces. Technical vocabulary is staged across introductory sections. | A new representation deserves explanation at the level of the new questions it makes accessible. Not every paper uses a failed-estimate narrative or a single compact outline. |
| Naber–Valtorta, *Volume Estimates on the Critical Sets of Solutions to Elliptic PDEs*, §2.4, pp. 9–10; §3 opening, p. 11 — held-out | Covering outputs are stated first and iterated to reach the desired bound; the construction is explained afterward through approximation and projection. | Supports conditional assembly and minimal definitions. Tangent uniqueness is useful here: a limitation from another paper must not become a universal claim. |
| Naber–Valtorta, *The Singular Structure and Regularity of Stationary Varifolds*, §1.3, pp. 8–11 — held-out, same-family check | The outline separates older qualitative and quantitative information, explains the remaining many-scale difficulty, and motivates a pair of compatible estimates. | Supports explicit mechanism interfaces; shared-family prose is not a license to copy its sequence or count it as an independent stylistic sample. |
| Naber, *Lecture Notes on Rectifiable Reifenberg for Measures*, Lecture 3 / §9, pp. 29–30 — supplement | Geometric intent accompanies neck conditions and explains what the parameters accomplish. | Technical definitions need purpose; the research projection should retain this function without importing exercises or the full lecture scaffold. |

## Promoted conditional decisions

Apply these through [Protocol 04p](../protocols/04p_reformulation_and_proof_explanation.md), not as a paragraph template:

- **Obstruction before replacement** when a new viewpoint answers a specific insufficiency. Do not invent failed prior methods.
- **Dictionary plus gain** when introducing a representation: original meaning, new control, and remaining cost.
- **Conditional assembly** when readers need to understand an engine's usefulness before its construction.
- **Operational interpretation after formulas** when the sign, scaling, or admissibility has a nonobvious role.
- **Asymmetric explanatory depth** when only some stages contain the conceptual difficulty.
- **Visible provisional assumptions** when a model case or deferred ingredient simplifies the outline.
- **Explicit bootstrap entry** when estimates improve the geometry or regularity they later exploit.

Confidence is qualitative and role-dependent. Failed-route exposition and engine assembly have repeated support across several research families. Toy examples, detailed displayed derivations, and prolonged outline subsections are optional techniques with narrower support. No default word count, equation count, heading sequence, or authorial verbal tic is inferred.

## Why these moves may help, and when they do not

The source passages establish that a writing move occurred. The reader effects below are editorial hypotheses inferred from those passages, not experimentally established effects or claims about an author's intention. Transfer the reason for the move, not its visible format.

| Move and source window | Proposed explanatory function | Selection boundary |
|---|---|---|
| Allow image transformations, codimension-four §1.1 | Separates the structure one first wishes for from the structure the argument actually needs, making the reformulation's gain assessable | Use when a source-backed requirement can be weakened; do not fabricate an unsuccessful method for drama |
| Assemble local and content estimates, L2 curvature §1.3 | Gives the reader a target against which to understand an otherwise unmotivated technical module | Use when the module's payoff is remote; a short direct proof may be clearer in forward order |
| Summable energy drop, harmonic maps §1.4 | Explains why a changed quantity survives iteration when a per-scale bound does not | Use when accumulation is the actual bottleneck; do not transplant a multiscale narrative to every perturbative argument |
| Unequal attention to bubble and annular pieces, Yang–Mills §1.3 | Makes the unresolved obstruction visible instead of weighting every decomposition piece equally | Depth follows difficulty of understanding, not the number or length of lemmas |
| Path-space characterization, bounded Ricci §§1–2.1 | Places a representation at the level of the new questions it permits | Use when a broader formulation is supported; do not infer a new theorem solely from an attractive analogy |

For this skill, Naber/coauthor organization and the user's wish for expressive, mathematically supported positioning are distinct inputs. The corpus is not evidence for a mandatory vocabulary. Retain supported expressive judgment because it helps state the mathematical assessment the user requested, not because a searched phrase occurred a certain number of times.

## Negative transfer controls

Do not transfer theorems, historical claims, geometric terms, or examples into another manuscript merely because they occur here. Do not ascribe sole authorship of coauthored writing decisions. Do not claim that every Naber Introduction follows one arc: the path-space paper provides a clear counterweight. Do not force a new abstract reformulation onto a routine result.

The useful target is an Introduction from which a reader can reconstruct the argument's purpose and dependencies while the proof remains closed. The goal is not to make a difficult discovery sound effortless, and it is not to reproduce any identifiable author's prose.
