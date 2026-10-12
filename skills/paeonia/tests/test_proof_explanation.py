#!/usr/bin/env python3
"""Dependency/evidence checks; deliberately no claims of generated-prose testing."""
import copy
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from proof_explanation_audit import audit

base = {
 'enabled': True,
 'evidence': {'a': {'source': 'manuscript', 'locator': 'prop:entry', 'role': 'coarse entry estimate'}},
 'initial_facts': [{'id': 'admissible', 'meaning': 'competitor in the target class', 'evidence': ['a']}],
 'reformulations': [{'id': 'defect', 'original_problem': 'identify the optimizer', 'obstruction': 'limit loses arrangement', 'dictionary': 'masses encode the discrete constraint', 'bridge_kind': 'controlled_comparison', 'new_capability': 'positive defect', 'remaining_cost': 'relative error and reconstruction', 'evidence': ['a']}],
 'stages': [
  {'id': 'coarse', 'requires': ['admissible'], 'obstacle': 'no regular mesh', 'action': 'use the independent coarse estimate', 'produces': [{'id': 'small_defect', 'meaning': 'scaled defect is small'}], 'payoff': 'rigidity becomes applicable', 'regime': 'no gap lower bound', 'evidence': ['a']},
  {'id': 'rigidity', 'requires': ['small_defect'], 'obstacle': 'need discrete geometry', 'action': 'apply microscopic rigidity', 'produces': [{'id': 'regular_mesh', 'meaning': 'near-regular gaps and masses'}], 'payoff': 'relative comparison becomes available', 'regime': 'small scaled defect', 'evidence': ['a']},
  {'id': 'relative', 'requires': ['regular_mesh'], 'obstacle': 'tiny competitor defect', 'action': 'compare in compatible coordinates', 'produces': [{'id': 'positive_gap', 'meaning': 'strictly positive comparison at positive defect'}], 'payoff': 'minimality forces zero defect', 'regime': 'all positive defects in localized class', 'evidence': ['a']},
 ],
 'assembly': {'requires': ['positive_gap'], 'implication': 'minimality forces zero defect', 'scope': 'localized minimizers', 'claims_equality': True, 'equality_recovery': 'source reconstruction and normalization identify optimizer', 'evidence': ['a']}
}
assert audit(base, r'\label{prop:entry}')['status'] == 'STRUCTURE_OK'
assert audit(base)['prose_comprehension'] == 'NOT_ASSESSED'
mutations = [
 lambda x: x['stages'][0]['requires'].append('regular_mesh'),
 lambda x: x['stages'][1]['requires'].append('unknown_fact'),
 lambda x: x['stages'][1]['produces'][0].update(id='small_defect'),
 lambda x: x['reformulations'][0].update(bridge_kind='same_thing'),
 lambda x: x['reformulations'][0].update(dictionary=''),
 lambda x: x['reformulations'][0].update(remaining_cost=''),
 lambda x: x['stages'][0].update(evidence=['missing_anchor']),
 lambda x: x['stages'][2].update(regime=''),
 lambda x: x['assembly'].update(requires=['unproduced_conclusion']),
 lambda x: x['assembly'].update(equality_recovery=''),
 lambda x: x.update(stages=[]),
]
for mutate in mutations:
 d = copy.deepcopy(base); mutate(d)
 assert audit(d)['status'] == 'REVIEW'
assert audit(base, r'\label{different}')['status'] == 'REVIEW'
assert audit({'enabled': False})['status'] == 'NOT_APPLICABLE'
assert audit({'proof_explanation': None})['status'] == 'REVIEW'
# Absence of a reformulation is legitimate for a routine proof.
ordinary = copy.deepcopy(base); ordinary['reformulations'] = []
assert audit(ordinary)['status'] == 'STRUCTURE_OK'
print('PROOF_EXPLANATION_TEST_PASS: valid graph, 12 invalid graph/evidence cases, scope guards')
