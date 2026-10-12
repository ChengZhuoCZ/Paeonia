# Theorem and Notation Architecture Checklist

## Theorem statements

- Is the main theorem the cleanest statement of the result the reader came for?
- Are all substantive assumptions visible and exact?
- Have proof-only assumptions been removed from the theorem statement?
- Are parameter ranges and endpoint exclusions unchanged from the closed proof?
- Is a quantitative strengthening separated when it would obscure the qualitative theorem?
- Are equality, rigidity, uniqueness, and classification stated at exactly the strength proved?
- Are theorem units split or merged for mathematical/readability reasons rather than source inheritance?
- Is reader order better than proof chronology for the front of the paper?
- Are theorem subtitles used only when they improve navigation?

## Notation architecture

For active symbol choices, also run [Mathematical Notation Selection](notation_selection.md) (Protocol 02h) before checking collisions.

- Does every recurring object have one canonical symbol per reader scope?
- Are global/local and normalized/unnormalized objects visibly distinct?
- Are index families assigned by mathematical role?
- Are transform, measure, operator, norm, and variation conventions fixed before use?
- Are generic and structural constants distinguished?
- Are relevant constant dependencies visible?
- Are source-notation collisions repaired before proof drafting?
- Has proof-only notation been kept out of the main theorem where possible?
- Do theorem statements and proofs use the same canonical symbols?
- Have internal semantic IDs been removed from final prose?


## Duplicate symbols and typography

- Does every recurring canonical symbol denote exactly one recurring object across the manuscript?
- Has `NotationLedger.canonical_objects` been checked for exact duplicate visible symbols?
- Are local dummy variables excluded from this audit rather than over-policed?
- If a duplicate recurring symbol is found, has one object been renamed consistently throughout the paper?
- Are `\mathscr` and `\mathfrak` absent unless the user explicitly overrode the default?
- Is each `\mathcal` use genuinely necessary and recorded as an exception?
- Is `\mathbb` restricted to standard canonical objects?
- Are unrelated objects distinguished by semantic subscripts/names rather than font alone?
- Is boldface semantic rather than decorative?


## Changfeng Gui corpus notation prior

- After collision checks and field/user conventions, were undecided symbols chosen with the plain semantic corpus prior?
- Are primary unknowns, domains, geometric objects, operators, and parameters represented by ordinary conventional letters where possible?
- Are related families distinguished by subscripts or meaningful modifiers rather than font switching?
- Is `\mathcal` reserved for genuine named sets/classes/spaces rather than decorative renaming?
- Are standard spaces such as `\mathbb R^n`, `\mathbb S^N`, and `\mathbb D` written conventionally?
- Did the prior remain subordinate to collision avoidance, explicit user notation, and strong field conventions?
- Was any exact reference-paper symbol sequence copied? If so, redesign it from the abstract prior instead.
