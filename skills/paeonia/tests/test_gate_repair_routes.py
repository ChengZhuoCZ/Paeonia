#!/usr/bin/env python3
from pathlib import Path
import sys, yaml
ROOT=Path(__file__).resolve().parents[1]
gates=yaml.safe_load((ROOT/'registry/gates.yaml').read_text(encoding='utf-8'))['release_blockers']
fail=[]
required={'audit_key','owner_state','rollback_to','allowed_repairs','forbidden_repairs','invalidates','re_audit'}
for name,g in gates.items():
    miss=required-set(g)
    if miss: fail.append(f'{name}:missing:{sorted(miss)}')
    if not g.get('allowed_repairs'): fail.append(f'{name}:no_allowed_repairs')
    if not g.get('re_audit'): fail.append(f'{name}:no_reaudit')
# high-value route assertions
if gates['MATH-SEMANTICS']['rollback_to']!='EXTRACT': fail.append('math_semantics_wrong_rollback')
if gates['PROOF-CLOSURE']['rollback_to']!='PROOF_GRAPH': fail.append('proof_closure_wrong_rollback')
if 'return_central_argument_from_appendix' not in gates['WHOLE-PAPER-NARRATIVE-FIDELITY']['allowed_repairs']: fail.append('appendix_debt_repair_missing')
if 'random_synonyms' not in gates['GENERATIVE-RESIDUE']['forbidden_repairs']: fail.append('random_synonym_forbidden_missing')
if fail:
    print('GATE_REPAIR_ROUTE_FAIL'); [print(x) for x in fail]; sys.exit(1)
print('GATE_REPAIR_ROUTE_PASS')
print(f'gates={len(gates)}')
