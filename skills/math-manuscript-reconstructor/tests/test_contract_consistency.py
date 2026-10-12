#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from contract_consistency import compile_contract
r=compile_contract(ROOT)
if r['status']!='PASS':
    print('CONTRACT_CONSISTENCY_TEST_FAIL')
    [print(x) for x in r['errors']]
    sys.exit(1)
print('CONTRACT_CONSISTENCY_TEST_PASS')
print(f"artifacts={r['artifacts']}")
print(f"gates={r['gates']}")
print(f"behavioral_fixtures={r['behavioral_fixtures']}")
