#!/usr/bin/env python3
"""Coverage for declarative notation-choice consistency, not mathematical taste."""
from pathlib import Path
import copy
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from notation_choice_audit import audit

BASE={
 'canonical_objects': [
  {'object_id':'domain','symbol':r'\Omega','meaning':'planar domain'},
  {'object_id':'eig','symbol':r'\lambda_1(\Omega)','meaning':'first Dirichlet eigenvalue'},
  {'object_id':'model','symbol':'R_N','meaning':'reference regular polygon'},
 ],
 'notation_selection': {
  'stage':'LOCKED',
  'field_context':{'primary_field':'spectral_geometry','adjacent_fields':[]},
  'protected_symbols':[{'object_id':'domain','symbol':r'\Omega'}],
  'decisions':[{'object_id':'eig','chosen_symbol':r'\lambda_1(\Omega)',
                'priority_basis':'field_standard',
                'rationale':'The Dirichlet ground-state notation is standard for this theorem.',
                'alternatives_considered':[{'symbol':r'\mu_1','reason_rejected':'May suggest Neumann spectrum here.'}]},
               {'object_id':'domain','chosen_symbol':r'\Omega',
                'priority_basis':'user_fixed','rationale':'Explicitly preserved in the supplied statement.'}],
  'external_symbol_crosswalk':[{'source_version':'arXiv:v2 inspected',
     'exact_result_locator':'Theorem 2.1 in the inspected version',
     'symbol_map':[{'source_symbol':'D','manuscript_symbol':r'\Omega','object_id':'domain'}],
     'logical_coverage_checked':True}],
  'review':{'mathematical_semantics':True,'theorem_readability':True,
             'field_conventions':True,'scope_protection':True,'source_translation':True}
 }
}

def inspect(name,mutate,expected):
    data=copy.deepcopy(BASE)
    mutate(data)
    errors,warnings,n=audit(data)
    assert (not errors)==expected,(name,errors,warnings,n)
    print(name+': PASS')

inspect('valid_complete',lambda d:None,True)
inspect('missing_selection',lambda d:d.pop('notation_selection'),True) # advisory; older ledgers remain usable
inspect('draft_not_locked',lambda d:d['notation_selection'].update(stage='DRAFT'),True)
inspect('invalid_stage',lambda d:d['notation_selection'].update(stage='COMPLETE'),False)
inspect('wrong_selected_symbol',lambda d:d['notation_selection']['decisions'][0].update(chosen_symbol='z'),False)
inspect('nonexistent_object',lambda d:d['notation_selection']['decisions'][0].update(object_id='ghost'),False)
inspect('repeat_decision',lambda d:d['notation_selection']['decisions'].append(copy.deepcopy(d['notation_selection']['decisions'][0])),False)
inspect('missing_basis',lambda d:d['notation_selection']['decisions'][0].pop('priority_basis'),False)
inspect('missing_rationale',lambda d:d['notation_selection']['decisions'][0].update(rationale='TODO'),False)
inspect('missing_alternative_reason',lambda d:d['notation_selection']['decisions'][0]['alternatives_considered'][0].update(reason_rejected=''),False)
inspect('chosen_duplicate_alternative',lambda d:d['notation_selection']['decisions'][0]['alternatives_considered'][0].update(symbol=r'\lambda_1(\Omega)'),False)
inspect('protected_mismatch',lambda d:d['notation_selection']['protected_symbols'][0].update(symbol='U'),False)
inspect('crosswalk_unknown_target',lambda d:d['notation_selection']['external_symbol_crosswalk'][0]['symbol_map'][0].update(object_id='model'),False)
inspect('crosswalk_missing_locator',lambda d:d['notation_selection']['external_symbol_crosswalk'][0].update(exact_result_locator='TBD'),False)
inspect('crosswalk_missing_version',lambda d:d['notation_selection']['external_symbol_crosswalk'][0].update(source_version=''),False)
inspect('crosswalk_false_applicability',lambda d:d['notation_selection']['external_symbol_crosswalk'][0].update(logical_coverage_checked=False),False)
inspect('crosswalk_empty',lambda d:d['notation_selection']['external_symbol_crosswalk'][0].update(symbol_map=[]),False)
inspect('review_unchecked',lambda d:d['notation_selection']['review'].update(theorem_readability='pending'),False)
inspect('locked_without_decisions',lambda d:d['notation_selection'].update(decisions=[]),False)
inspect('locked_without_field',lambda d:d['notation_selection']['field_context'].update(primary_field=''),False)
print('NOTATION_CHOICE_AUDIT_TEST_PASS: 20 cases')

# Strict route used before completing Pass 5a in new proof reconstruction.
valid=copy.deepcopy(BASE)
assert audit(valid,strict=True)[0]==[]
missing=copy.deepcopy(BASE); missing.pop('notation_selection')
assert 'required_notation_selection_not_recorded' in audit(missing,strict=True)[0]
draft=copy.deepcopy(BASE); draft['notation_selection']['stage']='DRAFT'
assert 'strict_requires_locked_selection' in audit(draft,strict=True)[0]
print('NOTATION_CHOICE_STRICT_TEST_PASS: 3 cases')

no_objects=copy.deepcopy(BASE); no_objects["canonical_objects"]=[]
assert "strict_without_canonical_objects" in audit(no_objects,strict=True)[0]
print("NOTATION_CHOICE_STRICT_EMPTY_REJECTED")
