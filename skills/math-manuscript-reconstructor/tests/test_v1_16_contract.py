#!/usr/bin/env python3
from pathlib import Path
import sys, yaml, json
ROOT=Path(__file__).resolve().parents[1]
schema=yaml.safe_load((ROOT/'schemas/notation_ledger.yaml').read_text(encoding='utf-8'))
manifest=json.loads((ROOT/'MANIFEST.json').read_text(encoding='utf-8'))
audit=(ROOT/'tools/notation_architecture_audit.py').read_text(encoding='utf-8')
checks={
 'version_floor':tuple(map(int,(ROOT/'VERSION').read_text().strip().split('.'))) >= (1,16,0),
 'no_permanent_symbol_reservation':manifest.get('symbol_reservation_policy') in {'context_sensitive_collision_avoidance','duplicate_recurring_symbol_audit'},
 'duplicate_model_present': schema.get('policy',{}).get('recurring_symbol_uniqueness') is True or schema.get('policy',{}).get('context_sensitive_symbol_assignment') is True,
 'audit_detects_symbol_conflict':'duplicate_symbol' in audit or 'symbol_collision' in audit,
 'behavioral_cases':all(any((ROOT/'tests/behavioral_cases').glob(f'{i:02d}_*.yaml')) for i in range(90,92)),
}
fail=[k for k,v in checks.items() if not v]
if fail:
 print('V1_16_CONTRACT_FAIL'); [print(x) for x in fail]; sys.exit(1)
print('V1_16_CONTRACT_PASS'); print(f'contract_checks={len(checks)}')
