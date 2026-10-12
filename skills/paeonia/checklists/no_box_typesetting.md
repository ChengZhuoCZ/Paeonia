# No-Box Manuscript Checklist (hard rule)

- [ ] No boxed mathematics (`\boxed`, `\Aboxed`, `\bbox`, including boxed final estimates).
- [ ] No framed, shaded or colored theorems, lemmas, proofs, definitions, remarks, conclusions or examples.
- [ ] No `tcolorbox`, `mdframed`, `framed`, `boxed` or custom theorem/callout box wrappers.
- [ ] No hidden box style in `empheq`, macros, imported files or elaborate highlighted TikZ panels.
- [ ] No replacement decorative card, panel, title banner or frame in final manuscript formatting.
- [ ] Unboxed `equation`, `align`, standard theorem/proof environments and normal references retain the same mathematical meaning.
- [ ] `tools/no_box_audit.py` was run on the complete delivered TeX dependency set; its reported results were reviewed.
- [ ] A PDF, when delivered, was visually inspected for framed decorations not detectable by the scanner.
- [ ] Protected inherited boxes, if any, were not silently rewritten; conflicts are reported and release remains blocked.
