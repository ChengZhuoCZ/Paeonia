#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
import yaml

def load_registry(root: Path):
    p=root/'registry/gates.yaml'
    return yaml.safe_load(p.read_text(encoding='utf-8'))['release_blockers']

def route(root: Path, gate: str):
    gates=load_registry(root)
    if gate not in gates:
        raise KeyError(f'unregistered gate: {gate}')
    g=dict(gates[gate])
    g['gate']=gate
    return g

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('gate')
    ap.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument('--json', action='store_true')
    args=ap.parse_args()
    try: r=route(args.root,args.gate)
    except Exception as e:
        print(f'ROUTE_INVALID: {e}', file=sys.stderr); sys.exit(2)
    print(json.dumps(r,indent=2,ensure_ascii=False) if args.json else yaml.safe_dump(r,sort_keys=False,allow_unicode=True))
if __name__=='__main__': main()
