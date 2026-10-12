#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
import yaml

CHECKS = [
    'no_strengthening','no_dropped_hypotheses','exact_parameter_ranges',
    'normalization_consistent','equality_rigidity_preserved',
    'no_duplicate_theorem_units','grouping_is_reader_motivated',
    'theorem_order_is_reader_motivated'
]

def audit(path: Path):
    d=yaml.safe_load(path.read_text(encoding='utf-8')) or {}
    issues=[]
    src=d.get('source_of_truth',{})
    if not src.get('math_ledger_locked'): issues.append('math_ledger_not_locked')
    if not src.get('proof_core_gate_passed'): issues.append('proof_core_gate_not_passed')
    units=d.get('theorem_units') or []
    if not units: issues.append('no_theorem_units')
    ids=[u.get('semantic_id') for u in units]
    if len(ids)!=len(set(ids)): issues.append('duplicate_semantic_ids')
    orders=[u.get('reader_order') for u in units if u.get('reader_order') is not None]
    if len(orders)!=len(set(orders)): issues.append('duplicate_reader_order')
    for u in units:
        if not u.get('role'): issues.append(f"missing_role:{u.get('semantic_id')}")
        if not u.get('qualitative_conclusion') and not u.get('quantitative_conclusion'):
            issues.append(f"missing_conclusion:{u.get('semantic_id')}")
        if u.get('assumptions_inherited') and not u.get('grouping_reason'):
            issues.append(f"inherited_assumptions_without_context:{u.get('semantic_id')}")
    checks=d.get('integrity_checks',{})
    for c in CHECKS:
        if checks.get(c) is not True:
            issues.append(f'integrity_not_passed:{c}')
    return {'status':'PASS' if not issues else 'REVIEW','issues':issues,'theorem_units':len(units)}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('ledger',type=Path); args=ap.parse_args()
    print(json.dumps(audit(args.ledger),indent=2,ensure_ascii=False))
if __name__=='__main__': main()
