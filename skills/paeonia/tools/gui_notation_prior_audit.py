#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
import yaml

GEOMETRY_TYPES={'triangle','quadrangle','quadrilateral','kite','polygon','domain','surface','manifold'}
FAMILY_TYPES={'eigenvalue','vertex','coefficient','threshold','mode','operator_family','functional_family','deformation_family'}


def load(path):
    return yaml.safe_load(Path(path).read_text(encoding='utf-8')) or {}


def audit(path):
    d=load(path); issues=[]; suggestions=[]; evidence=[]
    pol=d.get('policy') or {}
    prior=(d.get('notation_style_prior') or {})
    if pol.get('notation_style_prior')!='changfeng_gui_corpus_soft_prior':
        issues.append('gui_notation_prior_not_enabled')
    if pol.get('notation_style_prior_is_soft') is not True:
        issues.append('gui_notation_prior_not_soft')
    if pol.get('notation_style_prior_never_overrides_collision_or_user_convention') is not True:
        issues.append('gui_prior_precedence_not_protected')
    if prior.get('version') not in {'empirical_v2','v2'}:
        suggestions.append('review_gui_prior_version')
    if not prior.get('corpus_manifest'):
        suggestions.append('missing_gui_corpus_manifest')

    objs=d.get('canonical_objects') or []
    for o in objs:
        sym=str(o.get('symbol','')); typ=str(o.get('object_type','')); oid=str(o.get('object_id',''))
        relation=str(o.get('family_relation',''))
        if typ in GEOMETRY_TYPES and o.get('notation_choice_was_open') and ('\\mathscr' in sym or '\\mathfrak' in sym):
            suggestions.append(f'plain_semantic_geometry_preferred:{oid}:{sym}')
        if typ in FAMILY_TYPES and o.get('has_related_family') and not (o.get('index_or_modifier_encodes_relation') or relation):
            suggestions.append(f'review_family_relation_visibility:{oid}:{sym}')
        if o.get('reduced_coordinate_from') and len(sym)>3:
            suggestions.append(f'consider_simpler_reduced_coordinate:{oid}:{sym}')
        if o.get('repeated_derived_expression') and not o.get('short_derived_symbol'):
            suggestions.append(f'consider_named_derived_quantity:{oid}:{sym}')
        if o.get('generic_domain_symbol') and o.get('concrete_geometry_symbol'):
            evidence.append(f'generic_to_specific_geometry:{oid}')

    return {
      'status':'PASS' if not issues else 'REVIEW',
      'issues':issues,
      'suggestions':suggestions,
      'evidence':evidence,
      'profile':'changfeng_gui_corpus_soft_prior',
      'profile_version':'empirical_v2',
      'corpus_typography_is_mixed':True,
      'user_plain_typography_override_is_separate':True,
      'blocking_policy':'duplicate_symbol_user_requirement_and_field_convention_take_precedence',
      'exact_reference_symbol_sequence_copying':False,
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('ledger',type=Path); args=ap.parse_args()
    print(json.dumps(audit(args.ledger),indent=2,ensure_ascii=False))
if __name__=='__main__': main()
