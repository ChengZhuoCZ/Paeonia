# Regression 14 — No formula paraphrase

## Input failure

A display proves `A <= B`. The following sentence only says in words that `A is at most B`.

## Required behavior

Classify the follow-up as `DELETE` unless it adds a consequence, legality condition, interpretation, parameter dependence, equality/rigidity information, or a transition to the next proof obligation.

## Forbidden repair

Do not preserve the sentence by changing `shows` to `demonstrates`, `implies`, or another synonym when no new mathematical content is added.
