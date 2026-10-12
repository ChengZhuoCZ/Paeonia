#!/usr/bin/env python3
"""v1.41 stage integration / schema / mode / citation / evidence checks."""
from pathlib import Path
import json
import sys
import yaml
R=Path(__file__).resolve().parents[1]
read=lambda path:(R/path).read_text(encoding='utf-8')
s=read('SKILL.md')
p=read('protocols/02h_semantic_notation_selection.md')
p02d=read('protocols/02d_notation_architecture.md')
p07a=read('protocols/07a_exact_theorem_citation_compression.md')
st=read('protocols/12_execution_state_machine.md')
m=json.loads(read('MANIFEST.json'))
schema=yaml.safe_load(read('schemas/notation_ledger.yaml'))
template=yaml.safe_load(read('templates/notation_ledger.yaml'))
checks={
 'version':tuple(map(int,read('VERSION').strip().split('.'))) >= (1,41,0) and tuple(map(int,m['version'].split('.'))) >= (1,41,0) and 'version: 1.' in s,
 'active_pass_5a': '### Pass 5a — Notation architecture' in s and 'semantic notation selection' in s.lower(),
 'protocol_read_first': 'protocols/02h_semantic_notation_selection.md' in s and 'Protocol 02h' in p02d,
 'not_another_artifact': 'existing `NotationLedger`' in p and 'notation_selection' in schema,
 'no_new_state': 'NOTATION_ARCHITECTURE' in st and 'no new state or dossier' in st,
 'hard_constraints':all(x in p for x in ['user-mandated notation','Strong readership/domain convention','normalizations/signs','One-to-one canonical']),
 'real_formula_decisions':all(x in p for x in ['representative proof identity','human-readable reasons','not by an unvalidated numeric score']),
 'field_conditioned':all(x in p for x in ['Dirichlet/Neumann','polygon and distinguished regular model','Hilbert/Banach/interpolation']),
 'index_constant':all(x in p for x in ['indices','generic changing `C`','sharp named constants']),
 'source_crosswalk':all(x in p for x in ['external_symbol_crosswalk','source version','hypotheses']),
 'citation_integrated':'Protocol 02h' in p07a and 'logical' in p07a,
 'mode_scope':all(x in p for x in ['LOCAL_POLISH','protected','read-only']),
 'existing_policies_preserved':all(x in s for x in ['02f_duplicate_symbol_audit.md','02e_symbol_reservation_and_plain_typography.md','02g_changfeng_gui_notation_prior.md']),
 'schema_consistency':schema['notation_selection']==template['notation_selection'],
 'schema_covers_decisions':all(x in schema['notation_selection'] for x in ['stage','field_context','decisions','external_symbol_crosswalk','protected_symbols','review']),
 'checker_registered':'tools/notation_choice_audit.py' in m['tools'] and 'tests/test_notation_choice_audit.py' in m['tests'],
 'checker_noncertifying':'certifies_editorial_quality' in read('tools/notation_choice_audit.py') and 'cannot judge mathematical elegance' in s,
 'local_polish_preservation':'LOCAL_POLISH' in p and 'baseline' in p,
 'new_cases':all(any((R/'tests/behavioral_cases').glob(f'{i}_*.yaml')) and any((R/'tests/regression_cases').glob(f'{i}_*.md')) for i in range(187,201)),
 'intro_citation_preserved':'04u_literature_discovery_and_credit.md' in s and 'Pass 6a — Exact-theorem citation compression' in s,
 'strict_audit_route':'--strict' in p and '--strict' in s and '--strict' in read('tools/notation_choice_audit.py'),
 'gate_integrated':'Protocol 02h' in read('protocols/11_submission_gate.md') and 'choose_field_native_semantic_symbols' in read('registry/gates.yaml'),
 'docs':'v1.41.0' in read('README.md') and 'v1.41.0' in read('CHANGELOG.md')
}
bad=[x for x,y in checks.items() if not y]
if bad:
 print('V1_41_CONTRACT_FAIL:',','.join(bad));sys.exit(1)
print('V1_41_CONTRACT_PASS')
print('checks='+str(len(checks)))
