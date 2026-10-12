# Protocol 02e — Plain Mathematical Typography

## Purpose

Keep notation visually quiet and conventional. This protocol controls typography only. Symbol duplication is handled separately by `protocols/02f_duplicate_symbol_audit.md`.

## 1. Plain alphabet is the default

Prefer, in order:
1. ordinary italic Roman letters;
2. ordinary Greek letters;
3. transparent subscripts and superscripts;
4. standard operator notation.

Do not create extra notation levels merely by changing fonts.

## 2. Decorative alphabets

Default policy:
- `\mathscr{...}` — forbidden;
- `\mathfrak{...}` — forbidden;
- exotic script alphabets such as `\mathpzc`, `\mathds`, `\mathbbm` — forbidden unless explicitly required;
- `\mathcal{...}` — restrained semantic use only;
- `\mathbb{...}` — standard canonical objects only;
- boldface — semantic only, never decorative.

Use `\mathcal` sparingly for a genuine named set, class, or function space, or when it is genuinely standard in the subject. Do not use calligraphic/script/fraktur letters simply because an ordinary letter has already been used; solve that problem with a different plain symbol or a semantic subscript. This restrained-semantic policy is consistent with the Changfeng Gui corpus prior in `protocols/02g_changfeng_gui_notation_prior.md`.

## 3. No font-only semantic distinctions

Do not distinguish unrelated objects only by typography.

Avoid patterns such as
- `E`, `\mathcal E`, `\mathscr E` for three unrelated energies;
- `P`, `\mathbf P`, `\mathbb P` for unrelated operators;
- `g`, `\mathfrak g` merely because `g` was already taken.

Prefer `E`, `E_N`, `E_*`, or another genuinely different symbol.

## 4. Source notation

Source typography is not binding. If supplied material uses unnecessary decorative alphabets, normalize them before manuscript prose is drafted, without changing the mathematics.

## 5. Audit

Before release verify:
- no forbidden decorative alphabet remains without explicit user override;
- each `\mathcal` use has a genuine semantic role or an explicit justification;
- each `\mathbb` use is conventional;
- boldface has a real mathematical role;
- unrelated objects are not distinguished only by font.
