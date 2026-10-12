# Proof-replacement workflow validation — v1.35.0

Date: 2026-09-09. Instruction-only update.

- Skill structure validator: PASS.
- Existing release suite: all 30 test programs PASS; see release_suite_v135.log. Executable inventory code was not changed.
- Main-entry routing points to Protocol 07, section 6. The proof-substance rule and citation evidence gate now acknowledge verified citation-based replacement.
- Same-agent instruction review covered direct application, nontrivial adaptation, partial overlap, nonuniform external estimates, inaccessible source text, protected proof regions and circular dependencies. The written route calls for applying matched results with explanations, retaining unmatched or unverifiable steps, and respecting scope. This was a review of instructions, not independent behavioral testing on a manuscript.

The exact-result requirement is deliberately stronger than a general background citation: a whole-paper or section-only pointer cannot justify deleting a proof. Unnumbered results require a precise identified statement and page. The current tool only inventories citations; no automated theorem-applicability checker is claimed.

No manuscript edits, external-source searches, real proof substitutions, PDF builds or installed-skill changes were performed. Package tests do not establish correctness of any future mathematical application.
