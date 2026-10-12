# Protocol 09 — LaTeX and Final Notation Audit

## Relationship to notation architecture

The symbol system is designed earlier by `protocols/02d_notation_architecture.md` and `protocols/02e_symbol_reservation_and_plain_typography.md` and recorded in `NotationLedger` before proof-core drafting. This pass is a **final consistency and LaTeX audit**, not the first moment notation is considered. Active selection happened under Protocol 02h in Pass 5a; review the recorded choices and any precise-citation notation crosswalk (Protocol 07a) after downstream renumbering.

If this pass discovers a structural collision, normalization conflict, overloaded index family, or theorem/proof symbol mismatch, roll back to `NOTATION_ARCHITECTURE` and invalidate affected downstream prose. Do not patch a structural notation problem locally.

## Independent no-box release blocker

Apply Protocol 09a (`09a_no_box_typesetting.md`) to **every delivered TeX manuscript**. A clean compile is not enough: `\boxed`, `\fbox`, framed/colored/shaded theorem boxes, `tcolorbox`, `mdframed`, `framed` and all visually highlighted callouts are prohibited. Use `tools/no_box_audit.py` on the main source and its local included files, then inspect the rendered PDF when available. Report a protected-source conflict instead of editing outside scope. Record `NO-BOX-TYPESETTING` separately from conditional `LATEX-INTEGRITY`.

## Normalize

- theorem environment hierarchy;
- labels by semantics, not source numbering;
- notation macros used repeatedly;
- equation punctuation;
- cross-references;
- appendix references;
- bibliography style requested by venue;
- theorem/proof notation alignment;
- local/global symbol conventions;
- normalization conventions;
- constant-dependence notation;
- duplicate-symbol integrity for all recurring canonical notation;
- plain-mathematical-typography policy, removing decorative script/fraktur and unjustified calligraphic alphabets.

## Remove

- unused packages;
- stale labels;
- duplicate macros;
- dead aliases that survived a notation bridge;
- internal semantic IDs;
- internal TODO/project tags in final submission;
- manually typed theorem numbers;
- visual spacing hacks that obscure source maintainability;
- decorative `\mathscr` / `\mathfrak` notation introduced only for visual variety;
- unjustified `\mathcal` or nonstandard `\mathbb` symbols when a plain symbol is clearer.

## Mathematical caution

Do not rewrite formula structure solely for visual preference when associativity, operator scope, normalization, constant dependence, or symmetry quotient could become ambiguous.
