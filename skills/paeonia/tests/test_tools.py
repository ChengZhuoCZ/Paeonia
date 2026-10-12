#!/usr/bin/env python3
from pathlib import Path
import subprocess, tempfile, sys, yaml

ROOT = Path(__file__).resolve().parents[1]

with tempfile.TemporaryDirectory() as td:
    td = Path(td)
    source = td / "source.tex"
    final = td / "final.tex"
    source.write_text("The boundary contribution is controlled by the following uniform estimate which is valid for every admissible perturbation in the class.", encoding="utf-8")
    final.write_text("A uniform estimate controls the boundary term throughout the admissible perturbation class.", encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/source_overlap_audit.py'), str(source), str(final)], capture_output=True, text=True)
    if p.returncode != 0:
        print(p.stdout, p.stderr)
        raise SystemExit(1)

    clean = td / "clean.tex"
    clean.write_text(r"\\section{Main result} The estimate follows from coercivity. \\label{sec:main}", encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/manuscript_static_gate.py'), str(clean)], capture_output=True, text=True)
    if p.returncode != 0 or "STATIC_GATE_PASS" not in p.stdout:
        print(p.stdout, p.stderr)
        raise SystemExit(1)

    bad = td / "bad.tex"
    bad.write_text("Stage 5B. We now proceed to prove this. We now proceed to prove that. TODO", encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/manuscript_static_gate.py'), str(bad)], capture_output=True, text=True)
    if p.returncode == 0:
        raise SystemExit("static gate failed to reject bad manuscript")


    recurrent = td / "recurrent.tex"
    recurrent.write_text(("We now proceed to prove the estimate. " * 8) + "The boundary term vanishes by symmetry.", encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/phrase_recurrence_audit.py'), str(recurrent), '--ngram', '4', '--threshold', '4'], capture_output=True, text=True)
    if p.returncode != 0 or '"status": "REVIEW"' not in p.stdout:
        print(p.stdout, p.stderr)
        raise SystemExit('phrase recurrence diagnostic failed')

    p = subprocess.run([sys.executable, str(ROOT/'tools/transition_density.py'), str(recurrent), '--review-rate', '1'], capture_output=True, text=True)
    if p.returncode != 0 or '"status": "REVIEW"' not in p.stdout:
        print(p.stdout, p.stderr)
        raise SystemExit('transition diagnostic failed')

    formula = td / "formula.tex"
    formula.write_text(r"\[ A \le B. \] This inequality shows that A is less than or equal to B.", encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/equation_prose_redundancy.py'), str(formula)], capture_output=True, text=True)
    if p.returncode != 0 or '"status": "REVIEW"' not in p.stdout:
        print(p.stdout, p.stderr)
        raise SystemExit('formula redundancy diagnostic failed')

    rhythm = td / "rhythm.tex"
    rhythm.write_text("\n\n".join(["We apply the estimate. We obtain the bound. We close the claim." for _ in range(12)]), encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/prose_rhythm_audit.py'), str(rhythm)], capture_output=True, text=True)
    if p.returncode != 0 or '"status": "REVIEW"' not in p.stdout:
        print(p.stdout, p.stderr)
        raise SystemExit('rhythm diagnostic failed')


    para_src = td / "para_source.md"
    para_src.write_text(("*Proof*. We apply the estimate and obtain the bound.\n\n" "However, uniformity is needed before taking the limit, so we verify convergence uniformly on the parameter set.\n\n" "The claim follows.\n\n") * 20, encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/paragraph_fingerprint.py'), str(para_src)], capture_output=True, text=True)
    if p.returncode != 0 or '"numeric_targets_forbidden": true' not in p.stdout.lower() or '"stores_source_paragraphs": false' not in p.stdout.lower():
        print(p.stdout, p.stderr); raise SystemExit('paragraph fingerprint extraction failed')

    para_bad = td / "para_bad.tex"
    para_bad.write_text("\n\n".join(["We now proceed with the next step. The estimate follows. The claim follows." for _ in range(20)]), encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/paragraph_fingerprint_audit.py'), str(para_bad)], capture_output=True, text=True)
    if p.returncode != 0 or '"status": "REVIEW"' not in p.stdout:
        print(p.stdout, p.stderr); raise SystemExit('paragraph fingerprint audit failed')


    section_src = td / "section_source.md"
    section_src.write_text("# 1 Chapter\n\n##### 1 Main theory\n\nThe aim is the theorem.\n\nTheorem 1.1 Statement.\n\nProof text.\n\n##### 2 Application\n\nWe apply the theory.\n\nLemma 2.1 Statement.\n" * 8, encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/section_narrative_fingerprint.py'), str(section_src)], capture_output=True, text=True)
    if p.returncode != 0 or '"numeric_targets_forbidden": true' not in p.stdout.lower() or '"stores_source_sections": false' not in p.stdout.lower():
        print(p.stdout, p.stderr); raise SystemExit('section narrative fingerprint extraction failed')

    section_bad = td / "section_bad.tex"
    section_bad.write_text("\\section{A}\nTiny.\n\\subsection{Only}\nTiny.\n" * 8, encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/section_narrative_audit.py'), str(section_bad)], capture_output=True, text=True)
    if p.returncode != 0 or '"status": "REVIEW"' not in p.stdout:
        print(p.stdout, p.stderr); raise SystemExit('section narrative audit failed')


    whole_src = td / "whole_source.md"
    whole_src.write_text("## Introduction\n\nOrientation.\n\n# 1 Foundation\n\nTheorem 1.1 Statement.\n" + ("Technical proof. " * 300) + "\n# 2 Application\n\n" + ("Application. " * 60) + "\n## Appendix A: Tool\n\nLemma 1.1 Tool.\n" + ("Verification. " * 120), encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/whole_paper_narrative_fingerprint.py'), str(whole_src)], capture_output=True, text=True)
    if p.returncode != 0 or '"numeric_targets_forbidden": true' not in p.stdout.lower() or '"stores_source_unit_prose": false' not in p.stdout.lower():
        print(p.stdout, p.stderr); raise SystemExit('whole paper fingerprint extraction failed')

    whole_bad = td / "whole_bad.tex"
    whole_bad.write_text(r"\section{Introduction} Background only. " + "\n" + (r"\section{A} Routine sentence. Routine sentence. Routine sentence. " * 6) + r"\appendix\section{Technical Appendix} Theorem 9.1 Hidden central claim.", encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/whole_paper_narrative_audit.py'), str(whole_bad)], capture_output=True, text=True)
    if p.returncode != 0 or '"status": "REVIEW"' not in p.stdout:
        print(p.stdout, p.stderr); raise SystemExit('whole paper narrative audit failed')

    intro_bad = td / "intro_bad.tex"
    intro_bad.write_text(("This fundamental problem has a long and rich history and is a major breakthrough. " * 12) + ("Section 2 develops the method. Section 3 proves estimates. Section 4 contains applications. " * 4), encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/introduction_narrative_audit.py'), str(intro_bad)], capture_output=True, text=True)
    if p.returncode != 0 or '"status": "REVIEW"' not in p.stdout:
        print(p.stdout, p.stderr); raise SystemExit('introduction narrative audit failed')

    intro_prose_bad = td / "intro_prose_bad.tex"
    intro_prose_bad.write_text("\n\n".join(["In this paper, we now discuss the problem. More recently, several authors studied it. It is worth noting that this result is important." for _ in range(8)]), encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/introduction_prose_audit.py'), str(intro_prose_bad)], capture_output=True, text=True)
    if p.returncode != 0 or '"status": "REVIEW"' not in p.stdout:
        print(p.stdout, p.stderr); raise SystemExit('introduction prose audit failed')

    style_src = td / "style.md"
    style_src.write_text("*Proof*. Since x is positive, we choose y. Therefore the estimate follows. " * 20, encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/proof_style_signature.py'), str(style_src)], capture_output=True, text=True)
    if p.returncode != 0 or '"emits_source_phrases": false' not in p.stdout.lower() or '"stores_source_sentences": false' not in p.stdout.lower():
        print(p.stdout, p.stderr)
        raise SystemExit(1)

    # v1.7 adaptive planner / routing / consistency tools
    task = td / "task.yaml"
    task.write_text("workflow: PROOF_BODY_ONLY\nhas_math_sources: true\nhas_style_corpus: false\n", encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/execution_planner.py'), str(task), '--json'], capture_output=True, text=True)
    if p.returncode != 0 or '"PROOF_CORE_GATE"' not in p.stdout or '"FRONTMATTER"' in p.stdout.split('"required_states"',1)[1].split('"conditional_states"',1)[0]:
        print(p.stdout, p.stderr); raise SystemExit('execution planner tool failed')

    p = subprocess.run([sys.executable, str(ROOT/'tools/gate_repair_router.py'), 'PROOF-CLOSURE', '--json'], capture_output=True, text=True)
    if p.returncode != 0 or '"rollback_to": "PROOF_GRAPH"' not in p.stdout:
        print(p.stdout, p.stderr); raise SystemExit('gate repair router tool failed')

    p = subprocess.run([sys.executable, str(ROOT/'tools/behavioral_case_runner.py')], capture_output=True, text=True)
    if p.returncode != 0 or 'BEHAVIORAL_PASS' not in p.stdout:
        print(p.stdout, p.stderr); raise SystemExit('behavioral case runner failed')

    p = subprocess.run([sys.executable, str(ROOT/'tools/contract_consistency.py')], capture_output=True, text=True)
    if p.returncode != 0 or 'CONTRACT_CONSISTENCY_PASS' not in p.stdout:
        print(p.stdout, p.stderr); raise SystemExit('contract consistency tool failed')

    theorem_ledger = td / "theorem_ledger.yaml"
    theorem_ledger.write_text("""version: 1
source_of_truth:
  math_ledger_locked: true
  proof_core_gate_passed: true
theorem_units:
  - semantic_id: CLAIM-MAIN
    role: MAIN
    reader_order: 1
    assumptions_explicit: [H1]
    assumptions_inherited: []
    qualitative_conclusion: Main conclusion
integrity_checks:
  no_strengthening: true
  no_dropped_hypotheses: true
  exact_parameter_ranges: true
  normalization_consistent: true
  equality_rigidity_preserved: true
  no_duplicate_theorem_units: true
  grouping_is_reader_motivated: true
  theorem_order_is_reader_motivated: true
""", encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/theorem_statement_audit.py'), str(theorem_ledger)], capture_output=True, text=True)
    if p.returncode != 0 or '"status": "PASS"' not in p.stdout:
        print(p.stdout, p.stderr); raise SystemExit('theorem statement audit failed')

    notation_ledger = td / "notation_ledger.yaml"
    notation_ledger.write_text("""version: 6
policy:
  planned_before_proof_core: true
  recurring_symbol_uniqueness: true
  local_dummy_variables_excluded_from_duplicate_audit: true
  plain_symbol_typography: true
  font_only_semantic_distinctions: forbidden
  notation_style_prior: changfeng_gui_corpus_soft_prior
  notation_style_prior_is_soft: true
  notation_style_prior_never_overrides_collision_or_user_convention: true
  notation_style_prior_version: empirical_v2
duplicate_symbol_policy:
  audit_domain: canonical_objects
  uniqueness_rule: one_visible_symbol_one_recurring_object_across_manuscript
  exact_visible_symbol_match: true
  same_symbol_same_object_allowed: true
  local_dummy_variables_excluded: true
typography_policy:
  plain_alphabet_default: true
  mathscr: forbidden
  mathfrak: forbidden
  mathcal: restrained_semantic_only
  mathbb: standard_only
  boldface: semantic_only
  mathcal_exceptions: []
  mathcal_semantic_roles: [named_set, function_space, admissible_class, nodal_set, critical_set, standard_named_family]
  mathbb_allowlist: ['\\mathbb R', '\\mathbb C', '\\mathbb Z', '\\mathbb N', '\\mathbb Q', '\\mathbb P', '\\mathbb E', '\\mathbb S', '\\mathbb D']
notation_style_prior:
  profile: profiles/changfeng_gui_notation_prior.md
  evidence_report: profiles/changfeng_gui_notation_distillation_report.md
  corpus_manifest: profiles/changfeng_gui_notation_corpus.yaml
  version: empirical_v2
  priority: after_collision_user_domain_and_source_conventions
  geometry_strategy: generic_Omega_then_semantic_concrete_initial_when_helpful
  family_strategy: base_symbol_plus_semantic_index_or_modifier
  spectral_strategy: field_standard_then_stable_family_distinction
  reduction_strategy: simplify_active_coordinate_and_repeated_derived_quantities
  typography_note: corpus_is_mixed_user_plain_typography_override_is_stricter
canonical_objects:
  - object_id: OBJ-E
    symbol: E
    object_type: functional
  - object_id: OBJ-D
    symbol: '\\Delta'
    object_type: discriminant
  - object_id: OBJ-S
    symbol: '\\mathbb S^N'
    object_type: ambient_space
  - object_id: OBJ-Z
    symbol: '\\mathcal Z(u)'
    object_type: named_set
    semantic_role: nodal_set
duplicate_symbol_review:
  duplicate_symbols: []
  object_definition_inconsistencies: []
  font_only_distinctions: []
  decorative_alphabet_violations: []
  other_notation_issues: []
final_checks:
  theorem_proof_alignment: true
  normalization_alignment: true
  local_global_distinction: true
  constant_dependencies_visible: true
  duplicate_symbol_integrity: true
  plain_typography_integrity: true
  internal_semantic_ids_removed: true
""", encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/notation_architecture_audit.py'), str(notation_ledger)], capture_output=True, text=True)
    if p.returncode != 0 or '"status": "PASS"' not in p.stdout or '"special_symbol_reservations": false' not in p.stdout:
        print(p.stdout, p.stderr); raise SystemExit('notation architecture audit failed')

    p = subprocess.run([sys.executable, str(ROOT/'tools/gui_notation_prior_audit.py'), str(notation_ledger)], capture_output=True, text=True)
    if p.returncode != 0 or '"status": "PASS"' not in p.stdout or 'changfeng_gui_corpus_soft_prior' not in p.stdout:
        print(p.stdout, p.stderr); raise SystemExit('Gui notation prior audit failed')

    # The dedicated duplicate-symbol audit must pass a unique symbol table.
    p = subprocess.run([sys.executable, str(ROOT/'tools/duplicate_symbol_audit.py'), str(notation_ledger)], capture_output=True, text=True)
    if p.returncode != 0 or '"status": "PASS"' not in p.stdout:
        print(p.stdout, p.stderr); raise SystemExit('duplicate symbol audit pass case failed')

    # Any recurring symbol assigned to two distinct recurring objects is rejected.
    duplicate_bad = td / "notation_duplicate_bad.yaml"
    bad = yaml.safe_load(notation_ledger.read_text(encoding="utf-8"))
    bad['canonical_objects'].append({'object_id':'OBJ-DEF','symbol':'\\Delta','object_type':'deficit'})
    duplicate_bad.write_text(yaml.safe_dump(bad, sort_keys=False), encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/duplicate_symbol_audit.py'), str(duplicate_bad)], capture_output=True, text=True)
    if p.returncode != 0 or '"status": "REVIEW"' not in p.stdout or 'duplicate_symbol' not in p.stdout:
        print(p.stdout, p.stderr); raise SystemExit('duplicate symbol detection failed')

    intro_editorial = td / "intro_editorial.tex"
    intro_editorial.write_text("We make progress on the conjecture. This is a major breakthrough.", encoding="utf-8")
    ambition_ledger = td / "ambition.yaml"
    ambition_ledger.write_text("""scale:
  value: GRAND
strongest_defensible_positions:
  - verified: true
    must_surface: true
    preferred_wording: resolves the conjecture
""", encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/introduction_editorial_impact.py'), str(intro_editorial), '--ledger', str(ambition_ledger)], capture_output=True, text=True)
    if p.returncode != 0 or '"status": "REVIEW"' not in p.stdout or 'verified_must_surface_claim_missing_or_too_indirect' not in p.stdout:
        print(p.stdout, p.stderr); raise SystemExit('introduction editorial impact diagnostic failed')


    # v1.20 scientific-context audit
    context_good = td / "scientific_context_good.yaml"
    context_good.write_text("""trigger:
  detected: true
  context_depth: SUBSTANTIAL
  research_breadth: TRIANGULATED
model_to_math_map:
  - scientific_object: fundamental frequency
    mathematical_object: lambda_1
    meaning: spectral observable
source_dossier:
  - {role: MODEL_ORIGIN, verified: true, claim_supported: origin, source_type: ORIGINAL_OR_CANONICAL_SCIENCE}
  - {role: MECHANISM, verified: true, claim_supported: mechanism, source_type: REVIEW_OR_MONOGRAPH}
  - {role: REGIME_OR_SCALING, verified: true, claim_supported: regime, source_type: REVIEW_OR_MONOGRAPH}
  - {role: MATH_BRIDGE, verified: true, claim_supported: bridge, source_type: MATHEMATICAL_PHYSICS_BRIDGE}
introduction_use:
  return_anchor_to_mathematics: focal theorem
theorem_interpretation:
  scientific_interpretation: calibrated model statement
  wording_ceiling: idealized model only
integrity:
  context_depth_supported: true
  nontrivial_scientific_claims_verified: true
  model_to_math_bridge_complete: true
  decorative_context_removed: true
  theorem_interpretation_calibrated: true
""", encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/scientific_context_audit.py'), str(context_good)], capture_output=True, text=True)
    if p.returncode != 0 or '"status": "PASS"' not in p.stdout or '"audience_does_not_control_context_depth": true' not in p.stdout.lower():
        print(p.stdout, p.stderr); raise SystemExit('scientific context audit failed')

    # v1.21 mathematical-story audit
    story_good = td / "mathematical_story_good.yaml"
    story_good.write_text("""trigger:
  required: true
  research_depth: TRIANGULATED
hierarchy:
  focal_theorem: exact finite theorem
  focal_problem: constrained extremal problem
  parent_program: continuum-to-finite isoperimetric optimization
  canonical_principle: continuum symmetrization
story_archetypes:
  primary: CONTINUUM_TO_FINITE_COMPLEXITY
  secondary: [LIMIT_TO_EXACT_FINITE]
scale_transitions:
  - {from: continuum optimizer, to: exact finite optimizer, why_not_routine: symmetrization leaves the restricted class, evidence_anchor: verified}
structural_tensions:
  - {tension: continuum symmetry versus finite admissibility, mathematical_objects: [disk, polygon], theorem_level_relevance: central, proof_obstruction_anchor: proof graph}
story_graph:
  nodes: [continuum theorem, polygonal problem, present theorem]
  edges:
    - {from: continuum theorem, to: polygonal problem, relation: RESTRICTS_TO}
    - {from: polygonal problem, to: present theorem, relation: RIGIDIFIES}
  critical_story_path: [continuum theorem, polygonal problem, present theorem]
mathematical_ancestry:
  - {role: CANONICAL_THEOREM, work: benchmark, verified_claim: continuum optimizer, evidence_anchor: verified, why_story_needs_it: benchmark}
parallel_problems: []
program_interpretation:
  theorem_role: UPGRADES_ASYMPTOTIC_SELECTION_TO_EXACT_RIGIDITY
  program_level_consequence: exact finite rigidity in the stated regime
  factuality_ceiling: stated regime only
opening:
  preferred_entry: CANONICAL_PRINCIPLE
  first_page_goal: expose the continuum-to-finite gap
  theorem_entry_anchor: exact finite gap
proof_story:
  transition_to_explain: limit to exact finite
  mechanism_that_crosses_transition: quantitative gap and rigidity
scientific_context_relation:
  mode: MATH_ONLY_MAINLINE
story_compression:
  diagnostic_sentence: The continuum principle predicts the finite candidate but does not preserve the admissible class; the theorem restores exact finite rigidity.
  publication_template_forbidden: true
integrity:
  parent_program_is_mathematically_specific: true
  primary_archetype_supported: true
  scale_transition_or_tension_supported: true
  ancestry_claims_verified: true
  story_graph_has_nontrivial_critical_path: true
  parallel_problems_are_structurally_relevant: true
  theorem_returns_to_parent_program: true
  no_generic_grandeur: true
  no_story_inflation_beyond_evidence: true
""", encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/mathematical_story_audit.py'), str(story_good)], capture_output=True, text=True)
    if p.returncode != 0 or '"status": "PASS"' not in p.stdout:
        print(p.stdout, p.stderr); raise SystemExit('mathematical story audit failed')

    # v1.14 high-intensity conditional style tools
    hi_src = td / "hi_style.md"
    hi_src.write_text(("# Section\n\nThe object is introduced for the argument.\n\n*Proof*. We apply the estimate and obtain the bound.\n\nHowever, uniformity is needed before taking the limit, so the convergence is verified on the full parameter set.\n\nThe remaining term is bounded by the preceding estimate and the tail is then absorbed.\n\n" * 24), encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/high_intensity_corpus_distiller.py'), str(hi_src)], capture_output=True, text=True)
    if p.returncode != 0 or '"source_phrases_emitted": false' not in p.stdout.lower() or '"context_conditioned_traits_override_global_average": true' not in p.stdout.lower():
        print(p.stdout, p.stderr); raise SystemExit('high-intensity corpus distiller failed')

    cond_bad = td / "conditional_bad.tex"
    cond_bad.write_text("\n\n".join(["The estimate follows from the identity." for _ in range(12)] + ["To pass to the limit, uniform convergence and compactness must be justified." for _ in range(6)]), encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT/'tools/conditional_style_audit.py'), str(cond_bad)], capture_output=True, text=True)
    if p.returncode != 0 or '"numeric_targeting_forbidden": true' not in p.stdout.lower():
        print(p.stdout, p.stderr); raise SystemExit('conditional style audit failed')

print("TOOL_TEST_PASS")
