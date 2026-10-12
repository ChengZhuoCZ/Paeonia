#!/usr/bin/env python3
from pathlib import Path
import sys, yaml, json
ROOT=Path(__file__).resolve().parents[1]
version=tuple(map(int,(ROOT/'VERSION').read_text().strip().split('.')))
proto=(ROOT/'protocols/02g_changfeng_gui_notation_prior.md').read_text(encoding='utf-8')
profile=(ROOT/'profiles/changfeng_gui_notation_prior.md').read_text(encoding='utf-8')
report=(ROOT/'profiles/changfeng_gui_notation_distillation_report.md').read_text(encoding='utf-8')
corpus=yaml.safe_load((ROOT/'profiles/changfeng_gui_notation_corpus.yaml').read_text(encoding='utf-8'))
schema=yaml.safe_load((ROOT/'schemas/notation_ledger.yaml').read_text(encoding='utf-8'))
manifest=json.loads((ROOT/'MANIFEST.json').read_text(encoding='utf-8'))
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
checks={
 'version_floor':version >= (1,19,0),
 'empirical_protocol':'Empirical Changfeng Gui Corpus Notation Prior' in proto and 'profiles/changfeng_gui_notation_corpus.yaml' in proto,
 'inventory_breadth':len(corpus.get('papers',[])) >= 10 and all(k in str(corpus) for k in ['2311.12659','2109.13390','2208.03612','2604.19003']),
 'coauthor_caveat':'coauthored' in str(corpus.get('attribution_caveat','')).lower(),
 'generic_specific':'generic_to_specific_geometry_notation' in str(corpus) and 'Generic-to-specific geometry' in proto,
 'family_relation':'base symbol' in proto.lower() and ('indices' in proto.lower() or 'modifier' in proto.lower()),
 'reduction_simplification':'Simplify after a genuine reduction' in proto and 'reduced_coordinate' in str(corpus),
 'mixed_typography_correction':'corpus is mixed' in proto.lower() and 'user house style' in proto.lower(),
 'profile_not_template':'symbol template' in profile.lower() and 'exact symbol inventory' in profile.lower() and 'anti-imitation' in profile.lower(),
 'priority_order':all(x in proto for x in ['Duplicate-Symbol Audit','Explicit user notation requirements','Strong field/problem conventions']),
 'ledger_empirical_v2':schema.get('policy',{}).get('notation_style_prior_version')=='empirical_v2' and schema.get('notation_style_prior',{}).get('corpus_manifest')=='profiles/changfeng_gui_notation_corpus.yaml',
 'manifest_empirical_v2':manifest.get('notation_style_prior_version')=='empirical_v2',
 'skill_empirical':'Empirical Changfeng Gui corpus notation prior' in skill and 'corpus typography is **mixed**' in skill,
 'cases_101_108':all(any((ROOT/'tests/behavioral_cases').glob(f'{i}_*.yaml')) for i in range(101,109)),
 'audit_empirical':(ROOT/'tools/gui_notation_prior_audit.py').exists() and "profile_version':'empirical_v2'" in (ROOT/'tools/gui_notation_prior_audit.py').read_text(encoding='utf-8'),
}
fail=[k for k,v in checks.items() if not v]
if fail:
 print('V1_19_CONTRACT_FAIL'); [print(x) for x in fail]; sys.exit(1)
print('V1_19_CONTRACT_PASS'); print(f'contract_checks={len(checks)}')
