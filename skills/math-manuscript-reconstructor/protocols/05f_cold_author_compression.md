# Protocol 05f — Cold-Author Compression

## Purpose

Perform a final deletion-oriented pass after the mathematics and style are stable.

The imagined task is not to improve eloquence. It is to ask, with distance, whether each sentence earns its place in a research paper.

## 1. Allowed operations

The pass may:
- `DELETE`;
- `MERGE`;
- `COMPRESS`;
- `MOVE` a sentence or paragraph when dependency permits;
- replace an empty transition with a shorter mathematical transition.

The pass should not introduce new claims, new lemmas, new citations, new proof mechanisms, or new motivational material.

## 2. Three questions

For each prose sentence ask:

1. Does a specialist need this sentence to follow or audit the argument?
2. Does it state mathematics, a mathematical reason, or a necessary orientation cue?
3. Would the proof become less clear, less rigorous, or harder to navigate if it disappeared?

If all answers are no, delete it.

## 3. Deletion order

Delete or compress first:
- repeated previews;
- repeated recaps;
- empty reader coaching that supplies no mathematical orientation;
- empty signposting;
- formula paraphrases that add no interpretation or inference;
- novelty adjectives;
- duplicated hypothesis reminders;
- prose announcing a calculation that the next line already makes obvious;
- mechanical closure sentences.

The protected explanatory core of Protocol 04p survives this pass: novel-object dictionaries, the gain and cost of a reformulation, formula interpretations that connect proof stages, and the final assembly. A source's teaching apparatus is not a template, but clarity is not a defect. If a compression breaks Protocol 04q, restore the missing explanation.

Preserve last:
- parameter-choice explanations;
- nontrivial legality;
- topology in limiting arguments;
- uniformity of constants;
- equality/rigidity propagation;
- genuine obstruction statements;
- bridges from model/smooth/normalized cases to the target case.

## 4. Mathematical-semantic freeze

During this pass, the `MathLedger` and `SemanticChecksum` are read-only. If compression appears to require changing mathematics, stop and return to the appropriate earlier proof pass.

## 5. Style freeze

Do not use random sentence shortening or synonym variation to create irregularity. Preserve the supported `StyleLedger`; only remove excess prose.

## 6. Pass condition

`COLD-AUTHOR: PASS` requires that every remaining transition or explanatory sentence has a local mathematical function, while audit-critical detail is unchanged.
