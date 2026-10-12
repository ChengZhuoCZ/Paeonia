#!/usr/bin/env python3
from pathlib import Path
import json, sys, yaml

ROOT=Path(__file__).resolve().parents[1]
version=tuple(map(int,(ROOT/'VERSION').read_text().strip().split('.')))
skill=(ROOT/'SKILL.md').read_text(encoding='utf-8')
protocol=(ROOT/'protocols/04t_pde_introduction_branch.md').read_text(encoding='utf-8')
profile=(ROOT/'profiles/analysis_pde.md').read_text(encoding='utf-8')
archetypes=(ROOT/'profiles/pde_introduction_archetypes.md').read_text(encoding='utf-8')
cold=(ROOT/'protocols/04f_introduction_cold_read.md').read_text(encoding='utf-8')
core=yaml.safe_load((ROOT/'schemas/introduction_core_brief.yaml').read_text(encoding='utf-8'))
manifest=json.loads((ROOT/'MANIFEST.json').read_text(encoding='utf-8'))
checks={
    'version': version >= (1,37,0) and tuple(map(int,manifest.get('version','0.0.0').split('.'))) >= (1,37,0) and 'version: 1.' in skill,
    'conditional_not_second_ledger': 'does **not** add another mandatory ledger' in protocol and 'Do not create a second mandatory ledger' in skill,
    'core_extension': core.get('version')==2 and core.get('pde_extension',{}).get('active') is False,
    'theorem_coordinates': all(x in protocol for x in ['solution concept','boundary or initial conditions','scaling or criticality']),
    'partial_order_frontier': 'partially ordered' in protocol and 'incomparable frontier' in profile,
    'result_delta': all(x in protocol for x in ['result-delta map','solution concept','quantitative rate']),
    'result_architecture': all(x in protocol for x in ['THRESHOLD_OR_DICHOTOMY','STRATIFICATION_OR_PARTIAL_REGULARITY','SOLUTION_CLASS_SEPARATION']),
    'theorem_modes': all(x in protocol for x in ['DIRECT_PRECISE','MODEL_THEN_PRECISE','INFORMAL_THEN_PRECISE','RESULT_FAMILY']),
    'assumption_roles': all(x in protocol for x in ['STRUCTURAL','TECHNICAL','NORMALIZATION','PROOF_LOCAL']),
    'obstruction_stack': 'at most three causally ordered layers' in protocol,
    'mechanism_to_closure': all(x in protocol for x in ['original PDE variables','control it creates','closure step']),
    'typed_boundaries': all(x in protocol for x in ['theorem boundary','method boundary','known obstruction','open regime']),
    'genre_specific_checks': all(x in cold for x in ['continuation criterion','linear mechanism','singular-limit','nonuniqueness']),
    'burden_not_length': 'Explanatory burden, not target length' in protocol and manifest.get('pde_length_policy')=='explanatory_burden_not_venue_prestige',
    'dual_audience': 'object dictionary' in protocol and 'Singular limit or geometric bridge' in archetypes,
    'corpus_record': (ROOT/'references/pde_introduction_corpus_v137.md').exists(),
    'cases_144_154': all(any((ROOT/'tests/behavioral_cases').glob(f'{i}_*.yaml')) for i in range(144,155)),
}
bad=[k for k,v in checks.items() if not v]
if bad:
    print('V1_37_CONTRACT_FAIL')
    for k in bad: print(k)
    sys.exit(1)
print('V1_37_CONTRACT_PASS')
print('checks='+str(len(checks)))
