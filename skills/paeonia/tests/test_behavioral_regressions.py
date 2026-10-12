#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from behavioral_case_runner import run_dir
results, uncovered, legacy_count = run_dir(ROOT)
bad=[r for r in results if not r['pass']]
if uncovered or bad or len(results)!=legacy_count:
    print('BEHAVIORAL_REGRESSION_FAIL')
    print('legacy',legacy_count,'fixtures',len(results),'uncovered',uncovered)
    for r in bad: print('bad',r)
    sys.exit(1)
print('BEHAVIORAL_REGRESSION_PASS')
print(f'legacy_specs={legacy_count}')
print(f'executable_fixtures={len(results)}')
print(f'good_candidate_passes={sum(r["good_pass"] for r in results)}')
print(f'bad_candidate_rejections={sum(r["bad_rejected"] for r in results)}')
