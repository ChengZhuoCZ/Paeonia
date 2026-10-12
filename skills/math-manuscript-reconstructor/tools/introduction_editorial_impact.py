#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from pathlib import Path
import yaml

VAGUE_UNDERCLAIM = [
    r'we obtain a result related to', r'we make progress on', r'we provide some progress',
    r'we give a partial answer'  # only a flag when ledger says central must-surface claim is stronger
]
PRESTIGE = [r'\bmajor breakthrough\b', r'\bgroundbreaking\b', r'\bfar-reaching\b', r'\bdeep and fundamental\b']

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('introduction', type=Path)
    ap.add_argument('--ledger', type=Path)
    args=ap.parse_args()
    text=args.introduction.read_text(encoding='utf-8',errors='ignore')
    low=text.lower()
    flags=[]
    vague=sum(len(re.findall(p,low,re.I)) for p in VAGUE_UNDERCLAIM)
    prestige=sum(len(re.findall(p,low,re.I)) for p in PRESTIGE)
    if prestige: flags.append('prestige_language_requires_concrete_mathematical_replacement')
    missing=[]
    selected_scale=None
    if args.ledger and args.ledger.exists():
        data=yaml.safe_load(args.ledger.read_text(encoding='utf-8')) or {}
        selected_scale=((data.get('scale') or {}).get('value'))
        for item in data.get('strongest_defensible_positions',[]) or []:
            if item.get('verified') and item.get('must_surface'):
                wording=(item.get('preferred_wording') or '').strip()
                if wording and wording.lower() not in low:
                    missing.append(wording)
        if missing: flags.append('verified_must_surface_claim_missing_or_too_indirect')
        if selected_scale in ('GRAND','GRAND_PLUS') and vague:
            flags.append('grand_scale_intro_contains_vague_underclaim_language')
    out={
        'status':'REVIEW' if flags else 'PASS',
        'selected_scale':selected_scale,
        'vague_underclaim_markers':vague,
        'prestige_markers':prestige,
        'missing_must_surface_preferred_wording':missing,
        'flags':flags,
        'diagnostic_only':True,
        'factuality_ceiling_required':True,
        'strong_claims_are_allowed_when_verified':True,
    }
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
