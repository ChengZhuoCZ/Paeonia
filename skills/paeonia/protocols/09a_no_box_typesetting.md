# Protocol 09a — Absolute No-Box Manuscript Typesetting

## Binding rule

**NO BOXES IN THE ARTICLE.** For all newly produced or modified manuscript outputs, do not enclose theorems, lemmas, definitions, remarks, formulas, estimates, conclusions, proof steps or explanatory prose in visually framed, shaded, colored or otherwise decorative boxes. This is a **hard global formatting rule**, not a style preference. It applies to Abstract, Introduction, proofs, appendices and supplementary manuscript text alike, independently of the mathematical writing mode. Plain `amsthm` theorem and proof environments and ordinary unboxed display math are allowed.

Forbidden LaTeX constructions include, whether direct or hidden inside user-defined macros:

- `\boxed`, `\Aboxed`, `\bbox` and boxed equation wrappers;
- `\fbox`, `\framebox`, `\colorbox`, `\fcolorbox`, `\shadowbox`, `\doublebox`, `\ovalbox`, `\Ovalbox`;
- `tcolorbox`, `mdframed`, `framed`, `shaded`, `snugshade`, `boxed`, `boxedminipage` and custom decorated theorem/callout box environments;
- `empheq` equation boxing (`box=...`), `\tcbox`, `\tcbhighmath`, `\newtcolorbox`, `\newtcbox`, and analogous wrappers;
- framed or shaded `\tikz`/`\color` panels used to emphasize mathematical statements, even if a simple macro scanner cannot find them.

Do not replace a box with an unframed but showy substitute such as a colored panel, margin slogan, bold banner, decorative rule block or oversized boxed-looking display. Use ordinary narrative syntax, a standard `theorem`/`proof` environment, unboxed `equation`/`align`, an accurate cross-reference, or a short sober italic remark when structurally necessary.

Technical TeX internals (`\hbox`, `\mbox`, invisible alignment boxes, `\makebox` used for alignment) are not themselves visible *framed callouts* and are not banned by this **visual** rule, although avoid extraneous layout hacks. Mathematical diagrams that genuinely depict a geometric square/rectangle are not expository framing; do not use that exception for highlighted claims.

## Static check and visual inspection

Before releasing any `.tex` manuscript or `.tex` source bundle, run:

`python tools/no_box_audit.py main.tex`

The checker follows existing local `\input`, `\include` and `\subfile` files by default. It ignores TeX comments and verbatim/lstlisting/minted code examples, reports file/line/column and returns failure for recognized forbidden visual-box commands, environments, custom wrappers, and dedicated box packages. Manually examine macro definitions and the rendered PDF (if generated) for boxes created indirectly. Neither compilation nor a scanner alone proves the absence of all visual boxes.

**No-box audit is not optional because a manuscript is short or an Introduction-only edit.** It applies to the entire *delivered* TeX artifact; in `LOCAL_POLISH`, do not silently modify protected source regions. If a required final artifact contains an inherited protected box and permission does not allow changing it, classify `NO-BOX-TYPESETTING: BLOCKED`, disclose the exact location, and do not call the result submission-ready. If no LaTeX artifact is produced, apply the same no-decorative-box rule to authorized manuscript formatting without pretending a TeX scan ran.

At final audit record `NO-BOX-TYPESETTING: PASS` only after source-level inspection of all delivered editable `.tex` dependencies plus visual inspection when a PDF is available. A single known forbidden visual box is `FAIL` (or `BLOCKED` when uneditable). No exception for the main theorem or final displayed inequality.
