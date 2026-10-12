#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
import yaml

REQUIRED_ROLES = {
    'SUBSTANTIAL': {'MODEL_ORIGIN','MECHANISM','REGIME_OR_SCALING','MATH_BRIDGE'},
    'PHYSICS_LED': {'MODEL_ORIGIN','MECHANISM','REGIME_OR_SCALING','MATH_BRIDGE'},
    'INTERDISCIPLINARY_LED': {'MODEL_ORIGIN','MECHANISM','REGIME_OR_SCALING','MATH_BRIDGE'},
}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('ledger', type=Path)
    args=ap.parse_args()
    data=yaml.safe_load(args.ledger.read_text(encoding='utf-8')) or {}
    trig=data.get('trigger') or {}
    depth=trig.get('context_depth','NONE')
    breadth=trig.get('research_breadth','NONE')
    dossier=data.get('source_dossier') or []
    roles={x.get('role') for x in dossier if x.get('verified')}
    source_types={x.get('source_type') for x in dossier if x.get('verified') and x.get('source_type')}
    flags=[]
    missing=[]
    if depth in REQUIRED_ROLES:
        if depth == 'SUBSTANTIAL' and breadth not in {'TRIANGULATED','DEEP'}:
            flags.append('substantial_context_research_breadth_too_thin')
        if depth in {'PHYSICS_LED','INTERDISCIPLINARY_LED'} and breadth != 'DEEP':
            flags.append('physics_led_context_requires_deep_research')
        missing=sorted(REQUIRED_ROLES[depth]-roles)
        if missing: flags.append('substantial_context_missing_evidence_roles')
        if breadth in {'TRIANGULATED','DEEP'} and len(source_types) < 2:
            flags.append('scientific_context_source_diversity_too_thin')
        if not data.get('model_to_math_map'):
            flags.append('model_to_math_map_missing')
        iu=data.get('introduction_use') or {}
        if not iu.get('return_anchor_to_mathematics'):
            flags.append('scientific_context_has_no_return_anchor')
    if depth != 'NONE':
        for x in dossier:
            if x.get('claim_supported') and not x.get('verified'):
                flags.append('unverified_scientific_claim_in_dossier'); break
        integ=data.get('integrity') or {}
        for k in ['context_depth_supported','nontrivial_scientific_claims_verified','decorative_context_removed']:
            if not integ.get(k): flags.append(f'integrity_{k}_false')
    ti=data.get('theorem_interpretation') or {}
    if ti.get('scientific_interpretation') and not ti.get('wording_ceiling'):
        flags.append('theorem_scientific_interpretation_without_wording_ceiling')
    out={
        'status':'REVIEW' if flags else 'PASS',
        'context_depth':depth,
        'research_breadth':breadth,
        'verified_source_types':sorted(source_types),
        'verified_source_roles':sorted(r for r in roles if r),
        'missing_roles':missing,
        'flags':sorted(set(flags)),
        'audience_does_not_control_context_depth':True,
        'physics_wallpaper_forbidden':True,
        'diagnostic_only':True,
    }
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
