#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path
import yaml

def get_path(obj, path):
    cur=obj
    for part in path.split('.'):
        if isinstance(cur, dict) and part in cur: cur=cur[part]
        else: return None, False
    return cur, True

def check_assertion(candidate, a):
    op=a['op']; path=a.get('path',''); value=a.get('value')
    actual, present=get_path(candidate,path)
    if op=='present': return present
    if op=='absent': return not present
    if op=='truthy': return present and bool(actual)
    if op=='falsy': return present and not bool(actual)
    if not present: return False
    if op=='equals': return actual==value
    if op=='not_equals': return actual!=value
    if op=='contains': return value in actual
    if op=='not_contains': return value not in actual
    if op=='in': return actual in value
    if op=='not_in': return actual not in value
    if op=='subset_of': return set(actual).issubset(set(value))
    if op=='before':
        # value: [left,right], candidate path resolves to sequence
        left,right=value
        try: return actual.index(left)<actual.index(right)
        except Exception: return False
    raise ValueError(f'unsupported op {op}')

def evaluate(case, candidate):
    failures=[]
    for i,a in enumerate(case.get('assertions',[]),1):
        if not check_assertion(candidate,a): failures.append(i)
    return not failures, failures

def run_case(path: Path):
    case=yaml.safe_load(path.read_text(encoding='utf-8'))
    g_ok,g_fail=evaluate(case,case.get('good_candidate',{}))
    b_ok,b_fail=evaluate(case,case.get('bad_candidate',{}))
    ok = g_ok and not b_ok
    return {
        'id':case.get('id'),'title':case.get('title'),'gate':case.get('gate'),
        'good_pass':g_ok,'good_failures':g_fail,'bad_rejected':not b_ok,'bad_failures':b_fail,'pass':ok
    }

def run_dir(root: Path):
    files=sorted((root/'tests/behavioral_cases').glob('*.yaml'))
    results=[run_case(p) for p in files]
    legacy=sorted((root/'tests/regression_cases').glob('*.md'))
    legacy_ids={re.match(r'(\d+)_',p.name).group(1) for p in legacy if re.match(r'(\d+)_',p.name)}
    fixture_ids={str(r['id']).zfill(2) for r in results}
    uncovered=sorted(legacy_ids-fixture_ids)
    return results,uncovered,len(legacy)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument('--json', action='store_true')
    args=ap.parse_args()
    results,uncovered,legacy_count=run_dir(args.root)
    bad=[r for r in results if not r['pass']]
    summary={'legacy_specs':legacy_count,'executable_fixtures':len(results),'uncovered':uncovered,'passed':len(results)-len(bad),'failed':len(bad),'results':results}
    if args.json: print(json.dumps(summary,indent=2,ensure_ascii=False))
    else:
        print('BEHAVIORAL_PASS' if not bad and not uncovered else 'BEHAVIORAL_FAIL')
        print(f"legacy_specs={legacy_count}")
        print(f"executable_fixtures={len(results)}")
        print(f"good_candidate_passes={sum(r['good_pass'] for r in results)}")
        print(f"bad_candidate_rejections={sum(r['bad_rejected'] for r in results)}")
        if uncovered: print('uncovered='+','.join(uncovered))
        for r in bad: print('failed_case='+str(r['id']))
    if bad or uncovered: sys.exit(1)
if __name__=='__main__': main()
