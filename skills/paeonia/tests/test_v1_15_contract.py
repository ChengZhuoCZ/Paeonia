#!/usr/bin/env python3
from pathlib import Path
import sys, yaml
ROOT=Path(__file__).resolve().parents[1]
proto=(ROOT/'protocols/02e_symbol_reservation_and_plain_typography.md').read_text(encoding='utf-8')
schema=yaml.safe_load((ROOT/'schemas/notation_ledger.yaml').read_text(encoding='utf-8'))
checks={
 'version_floor':tuple(map(int,(ROOT/'VERSION').read_text().strip().split('.'))) >= (1,15,0),
 'decorative_forbidden': all(x in proto for x in ['`\\mathscr{...}` — forbidden','`\\mathfrak{...}` — forbidden']),
 'mathcal_restrained':('`\\mathcal{...}` — exceptional only' in proto or '`\\mathcal{...}` — restrained semantic use only' in proto),
 'font_only_rule':'No font-only semantic distinctions' in proto,
 'schema_typography': schema.get('typography_policy',{}).get('mathscr')=='forbidden' and schema.get('typography_policy',{}).get('mathcal') in {'exceptional_only','restrained_semantic_only'},
 'profile_exists':(ROOT/'profiles/plain_symbol_discipline.md').exists(),
}
fail=[k for k,v in checks.items() if not v]
if fail:
 print('V1_15_CONTRACT_FAIL'); [print(x) for x in fail]; sys.exit(1)
print('V1_15_CONTRACT_PASS'); print(f'contract_checks={len(checks)}')
