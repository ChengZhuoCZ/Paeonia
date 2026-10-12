#!/usr/bin/env python3
from pathlib import Path
import sys,yaml
ROOT=Path(__file__).resolve().parents[1]
proto=(ROOT/'protocols/02f_duplicate_symbol_audit.md').read_text(encoding='utf-8')
schema=yaml.safe_load((ROOT/'schemas/notation_ledger.yaml').read_text(encoding='utf-8'))
audit=(ROOT/'tools/duplicate_symbol_audit.py').read_text(encoding='utf-8')
checks={
 'version_floor':tuple(map(int,(ROOT/'VERSION').read_text().strip().split('.'))) >= (1,17,0),
 'protocol_exists':'same recurring mathematical symbol' in proto,
 'no_reserved_symbol_semantics':'No symbol is reserved in advance' in proto,
 'manuscript_wide':'manuscript-wide' in proto,
 'dummy_exclusion':'local dummy variables' in proto.lower(),
 'schema_uniqueness':schema.get('policy',{}).get('recurring_symbol_uniqueness') is True,
 'schema_domain':schema.get('duplicate_symbol_policy',{}).get('audit_domain')=='canonical_objects',
 'tool_exact_duplicate':'duplicate_symbol' in audit,
 'case92':any((ROOT/'tests/behavioral_cases').glob('92_*.yaml')),
}
fail=[k for k,v in checks.items() if not v]
if fail:
 print('V1_17_CONTRACT_FAIL'); [print(x) for x in fail]; sys.exit(1)
print('V1_17_CONTRACT_PASS'); print(f'contract_checks={len(checks)}')
