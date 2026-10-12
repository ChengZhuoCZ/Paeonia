#!/usr/bin/env python3
"""Behavioral release contract for the default unified voice, no style selection."""
from pathlib import Path
import json, sys, yaml
R=Path(__file__).resolve().parents[1]
read=lambda p:(R/p).read_text(encoding='utf8')
version=tuple(map(int,read('VERSION').strip().split('.')))
m=json.loads(read('MANIFEST.json'))
skill=read('SKILL.md')
p=read('protocols/05p_unified_manuscript_voice.md')
a=read('protocols/05o_author_corpus_supplement.md')
modes=read('protocols/00_writing_modes.md')
state=read('protocols/12_execution_state_machine.md')
checks={
 'version':version>=(1,42,0) and m['version']==read('VERSION').strip() and 'version: '+m['version'] in skill,
 'canonical_protocol':all(x in skill for x in ['Protocol 05p','05p_unified_manuscript_voice.md','unified_language_style.md']),
 'single_profile':m['canonical_editorial_voice']=='profiles/unified_research_mathematics_voice.md' and (R/m['canonical_editorial_voice']).is_file(),
 'language':all(x in p for x in ['research mathematics','English','explicitly different']),
 'no_style_selection':all(x in p for x in ['Do not ask users to select','do not present a menu','one best coherent draft']),
 'no_author_prompt_in_live_entry':all(x in skill for x in ['Do not proactively ask for an author','Do not ask for an author']) and 'ask once for the author' not in skill.lower(),
 'author_opt_in_only':all(x in a for x in ['does **not** ask','has already supplied','Do not ask for an author']),
 'state_route_no_prompt':'Do not ask for an author/style preference' in state,
 'role_density_not_tone':all(x in p for x in ['Role-conditioned density is not multiple selectable writing styles','one editorial voice']),
 'conflict_hierarchy':all(x in p for x in ['Truth and integrity','User constraints and mandatory submission requirements','Mathematical communication','This unified voice','Optional reference evidence','Cosmetics']),
 'intro_and_proof':all(x in p for x in ['Abstract','Introduction','Proof','Definitions and theorem statements']),
 'cross_section':all(x in p for x in ['At integration','Final cold read','checklists/unified_language_style.md']),
 'editorial_style_integration':'Protocol 05p' in read('protocols/05_editorial_style.md') and 'Protocol 05p' in read('protocols/05b_style_realization.md') and 'Protocol 05p' in read('protocols/05n_conditional_style_realization.md'),
 'mode_independence':'separate writing-mode question' in skill and 'LOCAL_POLISH' in p and 'does not change the selected writing mode' in modes,
 'requirements_and_protected_scope':all(x in p for x in ['mandatory submission requirements','protected content','LOCAL_POLISH']),
 'stage_integration':all(x in skill for x in ['Pass 3a — Optional author-corpus intake','Pass 13 — Editorial pass','Protocol 05p voice audit']),
 'schema_compat':yaml.safe_load(read('schemas/style_ledger.yaml'))==yaml.safe_load(read('templates/style_ledger.yaml')) and 'unified_voice_contract' in read('schemas/style_ledger.yaml'),
 'submission':'Protocol 05p unified voice' in read('protocols/11_submission_gate.md'),
 'new_cases':all(any((R/'tests/behavioral_cases').glob(f'{i}_*.yaml')) and any((R/'tests/regression_cases').glob(f'{i}_*.md')) for i in range(201,215)),
 'manifest_declared':'tests/test_v1_42_contract.py' in m['tests'] and all(x in m['hard_invariants'] for x in ['no_unprompted_style_tone_or_author_reference_selection','one_unified_journal_neutral_editorial_voice_in_all_authorized_manuscript_sections']),
 'v139_literature_retained':'04u_literature_discovery_and_credit.md' in skill and '04v_evidence_grounded_grand_narrative.md' in skill,
 'v140_citations_retained':'Pass 6a — Exact-theorem citation compression' in skill,
 'v141_notation_retained':'02h_semantic_notation_selection.md' in skill,
}
failed=[key for key,passed in checks.items() if not passed]
if failed:
 print('V1_42_CONTRACT_FAIL',', '.join(failed));sys.exit(1)
print('V1_42_CONTRACT_PASS')
print('checks='+str(len(checks)))
