#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from pathlib import Path
import yaml

FORBIDDEN_DECORATIVE=('\\mathscr','\\mathfrak','\\mathpzc','\\mathds','\\mathbbm')
CAL_SEMANTIC={'named_set','function_space','admissible_class','nodal_set','critical_set','standard_named_family'}


def _load(path: Path):
    return yaml.safe_load(path.read_text(encoding='utf-8')) or {}


def duplicate_symbol_issues(d):
    issues=[]; by_symbol={}
    for o in d.get('canonical_objects') or []:
        sym=o.get('symbol'); oid=o.get('object_id')
        if not sym or not oid:
            issues.append('object_missing_id_or_symbol'); continue
        by_symbol.setdefault(str(sym),[]).append(o)
    duplicates=[]
    for sym, rows in by_symbol.items():
        ids=sorted({str(r.get('object_id')) for r in rows})
        if len(ids)>1:
            duplicates.append({'symbol':sym,'object_ids':ids})
            issues.append('duplicate_symbol:'+sym+':'+'|'.join(ids))
        for oid in ids:
            same=[r for r in rows if str(r.get('object_id'))==oid]
            sigs={(str(r.get('meaning','')),str(r.get('object_type',''))) for r in same}
            if len(sigs)>1: issues.append('object_definition_inconsistent:'+oid)
    return issues, duplicates


def _mathbb_base(sym:str):
    """Return canonical blackboard-bold base, ignoring braces and subscripts/superscripts."""
    m=re.search(r'\\mathbb\s*(?:\{\s*([A-Za-z])\s*\}|([A-Za-z]))', sym)
    if not m: return None
    return '\\mathbb '+(m.group(1) or m.group(2))


FINAL_CHECKS=[
    'theorem_proof_alignment','normalization_alignment','local_global_distinction',
    'constant_dependencies_visible','duplicate_symbol_integrity','plain_typography_integrity',
    'internal_semantic_ids_removed'
]


def audit(path: Path, manuscript: Path|None=None):
    d=_load(path); issues=[]
    policy=d.get('policy',{}) or {}
    if policy.get('planned_before_proof_core') is not True: issues.append('not_planned_before_proof_core')
    if policy.get('recurring_symbol_uniqueness') is not True: issues.append('recurring_symbol_uniqueness_not_enabled')
    if policy.get('local_dummy_variables_excluded_from_duplicate_audit') is not True: issues.append('dummy_variable_exclusion_not_enabled')
    if policy.get('plain_symbol_typography') is not True: issues.append('plain_symbol_typography_not_enabled')
    if policy.get('font_only_semantic_distinctions') != 'forbidden': issues.append('font_only_distinctions_not_forbidden')

    dsp=d.get('duplicate_symbol_policy',{}) or {}
    if dsp.get('audit_domain')!='canonical_objects': issues.append('duplicate_audit_domain_not_canonical_objects')
    if dsp.get('uniqueness_rule')!='one_visible_symbol_one_recurring_object_across_manuscript': issues.append('duplicate_uniqueness_rule_missing')
    if dsp.get('local_dummy_variables_excluded') is not True: issues.append('duplicate_policy_dummy_exclusion_missing')

    typo=d.get('typography_policy',{}) or {}
    if typo.get('mathscr')!='forbidden': issues.append('mathscr_not_forbidden')
    if typo.get('mathfrak')!='forbidden': issues.append('mathfrak_not_forbidden')
    if typo.get('mathcal') not in {'restrained_semantic_only','exceptional_only'}: issues.append('mathcal_policy_invalid')
    if typo.get('mathbb')!='standard_only': issues.append('mathbb_not_standard_only')
    mathcal_ex=set(typo.get('mathcal_exceptions') or [])
    mathcal_roles=set(typo.get('mathcal_semantic_roles') or CAL_SEMANTIC)
    mathbb_allow=set(typo.get('mathbb_allowlist') or [])

    approved_mathcal=[]
    for o in d.get('canonical_objects') or []:
        sym=str(o.get('symbol','')); oid=str(o.get('object_id',''))
        role=str(o.get('semantic_role',''))
        if any(cmd in sym for cmd in FORBIDDEN_DECORATIVE): issues.append(f'forbidden_decorative_alphabet:{oid}:{sym}')
        if '\\mathcal' in sym:
            justified=(sym in mathcal_ex or role in mathcal_roles or bool(o.get('mathcal_justification')) or bool(o.get('field_standard_calligraphic')))
            if not justified: issues.append(f'unjustified_mathcal:{oid}:{sym}')
            else: approved_mathcal.append(sym)
        if '\\mathbb' in sym:
            base=_mathbb_base(sym)
            if base is None or base not in mathbb_allow: issues.append(f'nonstandard_mathbb:{oid}:{sym}')

    dup_issues, duplicates=duplicate_symbol_issues(d); issues.extend(dup_issues)

    rev=d.get('duplicate_symbol_review',{}) or {}
    for k in ['duplicate_symbols','object_definition_inconsistencies','font_only_distinctions','decorative_alphabet_violations','other_notation_issues']:
        if rev.get(k): issues.append(f'duplicate_symbol_review_nonempty:{k}')

    checks=d.get('final_checks',{}) or {}
    for c in FINAL_CHECKS:
        if checks.get(c) is not True: issues.append(f'final_check_not_passed:{c}')

    if manuscript is not None:
        text=manuscript.read_text(encoding='utf-8',errors='ignore')
        for cmd in FORBIDDEN_DECORATIVE:
            if cmd in text: issues.append(f'manuscript_forbidden_decorative_command:{cmd}')
        # Raw TeX cannot determine the semantic role of every calligraphic occurrence.
        # Flag only when the manuscript uses calligraphic notation but the ledger approves none.
        if '\\mathcal' in text and not approved_mathcal: issues.append('manuscript_mathcal_without_semantic_ledger_entry')

    issues=list(dict.fromkeys(issues))
    return {
        'status':'PASS' if not issues else 'REVIEW',
        'issues':issues,
        'duplicate_symbols':duplicates,
        'canonical_objects':len(d.get('canonical_objects') or []),
        'duplicate_symbol_policy':'exact_recurring_symbol_uniqueness',
        'local_dummy_variables_excluded':True,
        'special_symbol_reservations':False,
        'plain_typography_policy':True,
        'mathcal_policy':typo.get('mathcal'),
        'mathbb_base_matching':True,
    }


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('ledger',type=Path); ap.add_argument('--manuscript',type=Path); args=ap.parse_args()
    print(json.dumps(audit(args.ledger,args.manuscript),indent=2,ensure_ascii=False))
if __name__=='__main__': main()
