# Protocol 02b — Direct Writing Order

## Purpose

When a proof is supplied, decide how to **tell the mathematics** before writing sentences. This is a short composition step, not a research-management workflow.

## Default rule

Order the manuscript by the target proof dependency graph, not by the order of the source material.

Prefer an order that:

1. introduces only notation needed soon;
2. states the local goal before the machinery that serves it;
3. places genuinely reusable lemmas before their first use;
4. keeps one proof engine together instead of scattering it across sections;
5. postpones technical preliminaries that are not yet needed;
6. minimizes forward references and repeated hypotheses;
7. brings equality, rigidity, endpoint, or classification arguments immediately after the estimates that force them;
8. fixes the recurring notation before long proof prose begins;
9. assembles the main theorem once its proof engines are ready.

## User-facing plan

For a substantial task, give a concise plan such as:

1. normalization and notation;
2. first coercive/compactness mechanism;
3. second technical engine;
4. assembly of the main theorem;
5. equality or rigidity;
6. consequences.

Use only as many items as the mathematics needs. Do not pad the plan to a fixed number of sections.

## Immediate drafting rule

After presenting the writing order, **continue directly into the first proof section**. Do not ask for confirmation and do not stop after planning unless the user requested only an outline.

## Front-matter rule

The writing order may reserve later slots for theorem framing, Introduction, and Abstract, but final-form front matter remains deferred until the proof core has passed its closure check.
