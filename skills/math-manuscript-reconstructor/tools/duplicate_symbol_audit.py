#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
import yaml

FORBIDDEN_DECORATIVE=('\\mathscr','\\mathfrak','\\mathpzc','\\mathds','\\mathbbm')

def _load(path: Path):
    return yaml.safe_load(path.read_text(encoding='utf-8')) or {}

def duplicate_symbol_issues(d):
    issues=[]
    by_symbol={}
    for o in d.get('canonical_objects') or []:
        sym=o.get('symbol'); oid=o.get('object_id')
        if not sym or not oid:
            issues.append('object_missing_id_or_symbol')
            continue
        by_symbol.setdefault(str(sym),[]).append(o)
    duplicates=[]
    for sym, rows in by_symbol.items():
        ids=sorted({str(r.get('object_id')) for r in rows})
        if len(ids)>1:
            duplicates.append({'symbol':sym,'object_ids':ids})
            issues.append('duplicate_symbol:'+sym+':'+'|'.join(ids))
        # Same object id with contradictory declared meanings/types is a ledger error, not a second symbol policy.
        for oid in ids:
            same=[r for r in rows if str(r.get('object_id'))==oid]
            sigs={(str(r.get('meaning','')),str(r.get('object_type',''))) for r in same}
            if len(sigs)>1:
                issues.append('object_definition_inconsistent:'+oid)
    return issues, duplicates

def main():
    ap=argparse.ArgumentParser(description='Audit recurring canonical symbols for duplicate assignments.')
    ap.add_argument('ledger',type=Path)
    args=ap.parse_args()
    d=_load(args.ledger)
    issues, duplicates=duplicate_symbol_issues(d)
    print(json.dumps({
        'status':'PASS' if not issues else 'REVIEW',
        'duplicate_symbols':duplicates,
        'issues':issues,
        'audit_domain':'NotationLedger.canonical_objects',
        'local_dummy_variables_excluded':True,
        'special_symbol_reservations':False,
    },indent=2,ensure_ascii=False))
if __name__=='__main__': main()
