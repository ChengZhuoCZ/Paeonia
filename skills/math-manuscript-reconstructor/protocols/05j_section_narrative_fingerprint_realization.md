# Protocol 05j — Section-Level Narrative Fingerprint Realization

## Purpose

Realize a fresh section architecture from the target `ProofGraph` and `MathLedger`. An abstract `SectionNarrativeFingerprintLedger`, when a style corpus supplied one, may refine conditional presentation choices but is not required for the section architecture capability itself.

This protocol remains active without a style corpus and never imitates source section counts, lengths, subsection patterns, or theorem positions.

## 1. Start from obligation families

Before naming sections, partition the target proof graph into coherent obligation families.

For each candidate family record:

- principal mathematical question;
- active objects/space/normalization;
- proof technology;
- downstream consumers;
- whether notation is local or persistent;
- whether completion creates a genuine proof milestone.

Only after this map exists may section boundaries be proposed.

## 2. Section-worthiness test

A candidate unit becomes a section only if it passes at least one strong criterion:

- `REUSABLE_ENGINE`;
- `NEW_OBJECT_OR_SPACE`;
- `METHOD_FAMILY_SHIFT`;
- `APPLICATION_PHASE`;
- `REGIME_OR_GEOMETRY_SHIFT`;
- `OBLIGATION_FAMILY` with a genuine completion point;
- `SYNTHESIS_OR_RETURN` that materially changes the reader's state.

A sequence of lemmas is not section-worthy merely because it is long.

## 3. Theorem placement

Choose theorem latency from target prerequisite burden.

### `IMMEDIATE`
Use when the theorem is intelligible from previously established notation and the section exists principally to prove it.

### `MOTIVATED`
Use when the reader needs a short problem statement, reduction, or interpretation before seeing the formal claim.

### `DEVELOPED`
Use when exact definitions, normalization, or a compact mechanism must be introduced first for the theorem statement to be meaningful.

### `DEFERRED`
Use when the section's mathematical purpose is to build machinery or a construction whose payoff only becomes available after substantial development.

Never move a theorem earlier merely to satisfy a style profile. Never delay it to match a source statistic.

## 4. Section opening rule

The opening must establish the section's mathematical state quickly.

Preferred opening functions:

- state the goal;
- formulate the problem;
- define the object needed now;
- name the obstruction forcing a method change;
- announce the application target;
- recall one exact input and pivot.

Avoid administrative openings such as “In this section we continue our study...” unless the sentence also identifies a concrete mathematical transition.

## 5. Lemma grouping

Keep local lemmas near the theorem that consumes them unless isolation buys one of:

- multiple downstream uses;
- stable local notation;
- independent conceptual meaning;
- distinct proof technology;
- a substantial technical interruption that is clearer as a self-contained engine.

If none applies, preserve proof continuity rather than manufacturing a lemma section.

## 6. Subsection realization

Create a subsection only when its heading names a genuine internal phase that a reader may need to locate independently.

Good subsection roles:

- `SETUP`;
- `LOCAL_THEORY`;
- `KEY_ESTIMATE` when the estimate spans a substantial argument;
- `COMPACTNESS_OR_LIMIT_PASSAGE`;
- `EQUALITY_OR_RIGIDITY`;
- `APPLICATION`;
- `COUNTEREXAMPLE_CONSTRUCTION`;
- `RETURN_OR_ASSEMBLY`.

Suppress a subsection when:

- it would contain only one short result;
- the entire section is one continuous theorem proof;
- the heading merely repeats the next theorem title;
- it is a disguised numbered proof step;
- it was inherited from source/discovery history;
- it exists only because the section feels long.

One-subsection sections are a review signal: either the subsection may be unnecessary or the sibling phase is missing. They are not automatically forbidden.

## 7. Conceptual/technical pressure wave

Use the target mathematics to create a readable pressure wave.

Conceptual passages should orient, define, interpret, or expose an obstruction. Technical passages should do the proof work. Application/synthesis passages should cash out the machinery.

Do not force alternation. Instead ask after each technical block:

- has the reader's mathematical state changed enough to require reorientation?
- is the next block still the same engine, or a new obligation family?
- would a short conceptual bridge reduce cognitive load without repeating results?

## 8. Section closure

Stop when the section's obligation family is complete.

Allowed closure behavior:

- no additional prose if the final proof is self-closing;
- one concise consequence that will be used next;
- one precise statement of the next obstruction;
- one return-to-main-line sentence after auxiliary machinery.

Avoid generic summaries of what was just proved.

## 9. Architecture audit questions

For every section ask:

1. Why is this a section rather than part of the previous one?
2. What mathematical state changes at the boundary?
3. What downstream claim consumes this section?
4. Could its lemmas live inside one theorem proof without loss?
5. Is the principal theorem stated as early as its prerequisites permit?
6. Does each subsection name a real internal phase?
7. Does the section end when its obligation family ends?

If these questions cannot be answered, revise the architecture.

## 10. Forbidden realization strategies

Never:

- match source section counts;
- match source median section length;
- match source subsection rate;
- reproduce source section-role order;
- alternate conceptual/technical sections mechanically;
- create a section per lemma cluster by default;
- create subsections merely to break long text;
- place the theorem at a fixed word distance from the heading.

The source fingerprint is evidence about authorial decisions, not a layout specification.
