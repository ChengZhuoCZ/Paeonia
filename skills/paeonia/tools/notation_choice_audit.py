#!/usr/bin/env python3
"""Structural audit of notation-selection declarations inside NotationLedger.

This checker does NOT rank mathematical beauty, recover symbols from arbitrary
LaTeX or verify cited external theorem statements/assumptions.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import yaml

STAGES={'DRAFT','LOCKED'}
BASES={'user_fixed','field_standard','structural_relation','source_continuity',
       'formula_clarity','style_tiebreak'}
REVIEWS=('mathematical_semantics','theorem_readability','field_conventions',
         'scope_protection','source_translation')


def populated(x):
    return isinstance(x,str) and x.strip().lower() not in ('','todo','tbd','unknown','null','none','to check')


def audit(doc, strict=False):
    issues, warnings = [], []
    if not isinstance(doc,dict):
        return ['ledger_not_mapping'], warnings, 0
    data=doc.get('notation_selection') or {}
    if not isinstance(data,dict):
        return ['notation_selection_not_mapping'],warnings,0
    if not data:
        if strict:
            return ['required_notation_selection_not_recorded'], [], 0
        return [], ['notation_selection_not_recorded'],0
    stage=data.get('stage')
    if stage not in STAGES:issues.append('stage_invalid')
    if strict and stage!='LOCKED':issues.append('strict_requires_locked_selection')
    ctx=data.get('field_context') or {}
    if not isinstance(ctx,dict):
        issues.append('field_context_not_mapping');ctx={}
    if stage=='LOCKED' and not populated(ctx.get('primary_field')):
        issues.append('locked_without_primary_field')

    rows=doc.get('canonical_objects') or []
    if not isinstance(rows,list):
        issues.append('canonical_objects_not_list');rows=[]
    objs={}
    for o in rows:
        if not isinstance(o,dict):
            issues.append('canonical_object_not_mapping');continue
        oid=o.get('object_id')
        if not populated(oid):
            issues.append('canonical_object_id_missing');continue
        if oid in objs and o.get('symbol')!=objs[oid].get('symbol'):
            issues.append('canonical_id_contradictory:'+oid)
        objs[oid]=o

    decisions=data.get('decisions') or []
    if not isinstance(decisions,list):
        issues.append('decisions_not_list');decisions=[]
    if strict and not objs:
        issues.append('strict_without_canonical_objects')
    if stage=='LOCKED' and objs and not decisions:
        issues.append('locked_without_decisions')
    seen=set()
    for i,d in enumerate(decisions):
        prefix=f'decision[{i}]'
        if not isinstance(d,dict):
            issues.append(prefix+':not_mapping');continue
        oid=d.get('object_id')
        if not populated(oid):
            issues.append(prefix+':object_id_missing');continue
        if oid in seen:issues.append(prefix+':duplicate_object_decision')
        seen.add(oid)
        if oid not in objs:
            issues.append(prefix+':object_not_canonical:'+oid)
        if not populated(d.get('chosen_symbol')):
            issues.append(prefix+':chosen_symbol_missing')
        elif oid in objs and d['chosen_symbol']!=objs[oid].get('symbol'):
            issues.append(prefix+':symbol_mismatch:'+oid)
        if not populated(d.get('rationale')):
            issues.append(prefix+':rationale_missing')
        if d.get('priority_basis') not in BASES:
            issues.append(prefix+':invalid_priority_basis')
        alternatives=d.get('alternatives_considered') or []
        if not isinstance(alternatives,list):
            issues.append(prefix+':alternatives_not_list');continue
        alts=set()
        for j, alt in enumerate(alternatives):
            if not isinstance(alt,dict) or not populated(alt.get('symbol')):
                issues.append(prefix+f':alternative[{j}]_invalid');continue
            sym=alt['symbol']
            if sym==d.get('chosen_symbol'):
                issues.append(prefix+':chosen_is_alternative')
            if sym in alts:
                issues.append(prefix+':duplicate_alternative:'+sym)
            alts.add(sym)
            if not populated(alt.get('reason_rejected')):
                issues.append(prefix+f':alternative[{j}]_missing_reason')

    for i,p in enumerate(data.get('protected_symbols') or []):
        loc=f'protected[{i}]'
        if not isinstance(p,dict):
            issues.append(loc+':not_mapping');continue
        oid=p.get('object_id')
        if oid not in objs:
            issues.append(loc+':unknown_object');continue
        if not populated(p.get('symbol')) or p.get('symbol')!=objs[oid].get('symbol'):
            issues.append(loc+':violated:'+str(oid))

    for i,c in enumerate(data.get('external_symbol_crosswalk') or []):
        loc=f'crosswalk[{i}]'
        if not isinstance(c,dict):
            issues.append(loc+':not_mapping');continue
        if stage=='LOCKED':
            for attr in ('source_version','exact_result_locator'):
                if not populated(c.get(attr)):
                    issues.append(loc+':'+attr+'_missing')
        pairs=c.get('symbol_map') or []
        if not isinstance(pairs,list) or not pairs:
            issues.append(loc+':empty_symbol_map');continue
        for j,m in enumerate(pairs):
            loc2=loc+f'.symbol_map[{j}]'
            if not isinstance(m,dict) or not populated(m.get('source_symbol')) or not populated(m.get('manuscript_symbol')):
                issues.append(loc2+':mapping_incomplete');continue
            oid=m.get('object_id')
            if oid not in objs or m['manuscript_symbol']!=objs[oid].get('symbol'):
                issues.append(loc2+':canonical_symbol_mismatch')
        if stage=='LOCKED' and c.get('logical_coverage_checked') is not True:
            issues.append(loc+':logical_coverage_not_marked_checked')
    review=data.get('review') or {}
    if stage=='LOCKED':
        if not isinstance(review,dict):issues.append('review_not_mapping')
        else:
            for req in REVIEWS:
                if review.get(req) is not True:
                    issues.append('locked_review_unchecked:'+req)
    return list(dict.fromkeys(issues)),warnings,len(decisions)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('ledger',type=Path)
    parser.add_argument('--strict', action='store_true', help='Require a completed LOCKED notation selection for a new proof production')
    args=parser.parse_args()
    doc=yaml.safe_load(args.ledger.read_text(encoding='utf-8')) or {}
    issues,warnings,num=audit(doc, strict=args.strict)
    print(json.dumps({'status':'PASS' if not issues else 'REVIEW',
                      'issues':issues,'warnings':warnings,'selection_decisions':num,
                      'scope':'declared_ledger_structure_only',
                      'certifies_editorial_quality':False,
                      'certifies_external_theorem':False},indent=2,ensure_ascii=False))
    return 0 if not issues else 1


if __name__=='__main__':
    raise SystemExit(main())
