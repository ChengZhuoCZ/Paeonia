#!/usr/bin/env python3
from pathlib import Path
import sys, yaml, json
ROOT=Path(__file__).resolve().parents[1]
version=tuple(map(int,(ROOT/'VERSION').read_text().strip().split('.')))
proto=(ROOT/'protocols/02g_changfeng_gui_notation_prior.md').read_text(encoding='utf-8')
profile=(ROOT/'profiles/changfeng_gui_notation_prior.md').read_text(encoding='utf-8')
report=(ROOT/'profiles/changfeng_gui_notation_distillation_report.md').read_text(encoding='utf-8')
schema=yaml.safe_load((ROOT/'schemas/notation_ledger.yaml').read_text(encoding='utf-8'))
manifest=json.loads((ROOT/'MANIFEST.json').read_text(encoding='utf-8'))
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
checks={
 'version_floor':version >= (1,18,0),
 'soft_prior_protocol':'soft selection prior' in proto.lower() and 'Duplicate-Symbol Audit' in proto,
 'priority_order':'Explicit user notation requirements' in proto and 'Strong field/problem conventions' in proto,
 'plain_semantic_profile':(('ordinary lower-case letter' in profile or 'Direct semantic naming' in profile or 'direct semantic naming' in profile.lower()) and ('shared base symbol' in profile or 'shared base' in profile.lower())),
 'mathcal_restrained':('genuine set notation' in profile.lower() or 'named set' in profile.lower()) and schema.get('typography_policy',{}).get('mathcal')=='restrained_semantic_only',
 'mathbb_spaces':'\\mathbb S' in schema.get('typography_policy',{}).get('mathbb_allowlist',[]) and '\\mathbb D' in schema.get('typography_policy',{}).get('mathbb_allowlist',[]),
 'ledger_prior':schema.get('policy',{}).get('notation_style_prior')=='changfeng_gui_corpus_soft_prior' and schema.get('policy',{}).get('notation_style_prior_is_soft') is True,
 'corpus_breadth':all(x.lower() in report.lower() for x in ['Sphere Covering','triangles','quadrangle','Beckner']),
 'anti_imitation':'anti-imitation' in profile.lower() and ('exact symbol inventory' in profile.lower() or 'exact sequence' in proto.lower()),
 'skill_integration':'Changfeng Gui corpus notation prior' in skill and 'protocols/02g_changfeng_gui_notation_prior.md' in skill,
 'manifest_prior':manifest.get('notation_style_prior')=='changfeng_gui_corpus_soft_prior',
 'cases_93_100':all(any((ROOT/'tests/behavioral_cases').glob(f'{i}_*.yaml')) for i in range(93,101)),
 'audit_tool':(ROOT/'tools/gui_notation_prior_audit.py').exists(),
}
fail=[k for k,v in checks.items() if not v]
if fail:
 print('V1_18_CONTRACT_FAIL'); [print(x) for x in fail]; sys.exit(1)
print('V1_18_CONTRACT_PASS'); print(f'contract_checks={len(checks)}')
