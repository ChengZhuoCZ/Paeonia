#!/usr/bin/env python3
"""Tests status/locator/applicability-record guardrails (not math validity)."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'tools'))
from proof_citation_dossier_audit import audit


def example():
    return {'artifact': 'ProofCitationReplacementDossier',
            'editable_proof_scope': 'Proof of Lemma A',
            'entries': [{
                'id': 'CLAIM-A',
                'manuscript': {'location': 'sec3.tex:Lemma A', 'full_claim': 'For all t, a uniform inequality holds'},
                'source': {'bibkey': 'SomeVerifiedRef', 'url': 'https://arxiv.org/abs/1111.1111',
                           'version': 'specific edition/number verified in source',
                           'result_kind': 'Theorem', 'result_number': '2.4',
                           'metadata_checked': True, 'locator_checked': True, 'primary_statement_checked': True},
                'application': {'hypotheses_map': [{'source_hypothesis': 'H', 'local_fact': 'Lemma B', 'local_locator': 'sec2.tex:Lemma B'}],
                                'conclusion_map': 'Source C -> all-t claim in original notation',
                                'scope_uniformity_equality_checked': True,
                                'independent_dependency_checked': True,
                                'adaptations': [], 'retained_steps': []},
                'decision': {'status': 'APPLIED_DIRECT', 'replacement_location': 'sec3.tex:L90',
                             'exact_citation_written': True, 'downstream_checked': True,
                             'protected_scope_checked': True}
            }]}


class Checks(unittest.TestCase):
    def check_error(self, mutator, substring):
        d = example()
        mutator(d['entries'][0])
        errors, _, _ = audit(d)
        self.assertTrue(any(substring in e for e in errors), errors)

    def test_complete_direct(self):
        self.assertEqual(audit(example())[0], [])

    def test_exact_result_required(self):
        self.check_error(lambda e: e['source'].update(result_number=None), 'result_number')

    def test_read_primary_required(self):
        self.check_error(lambda e: e['source'].update(primary_statement_checked=False), 'primary_statement_checked')

    def test_version_required(self):
        self.check_error(lambda e: e['source'].update(version='TBD'), 'source.version')

    def test_hypothesis_map_required(self):
        self.check_error(lambda e: e['application'].update(hypotheses_map=[]), 'no hypothesis map')

    def test_conclusion_map_required(self):
        self.check_error(lambda e: e['application'].update(conclusion_map=''), 'conclusion_map')

    def test_uniformity_required(self):
        self.check_error(lambda e: e['application'].update(scope_uniformity_equality_checked=False), 'scope_uniformity_equality_checked')

    def test_independence_required(self):
        self.check_error(lambda e: e['application'].update(independent_dependency_checked=False), 'independent_dependency_checked')

    def test_partials_preserve_unmatched(self):
        self.check_error(lambda e: e['decision'].update(status='APPLIED_PARTIAL'), 'partial replacement')

    def test_adaptation_record_required(self):
        self.check_error(lambda e: e['decision'].update(status='APPLIED_ADAPTED'), 'adapted application')

    def test_unnumbered_needs_exact_page(self):
        self.check_error(lambda e: e['source'].update(result_kind='Unnumbered', result_number=None, result_locator='Section 3'), 'exact page locator')

    def test_unnumbered_needs_named_statement(self):
        self.check_error(lambda e: e['source'].update(result_kind='Unnumbered', result_number=None, result_locator='page 19'), 'result_name')

    def test_correct_unnumbered(self):
        d = example()
        d['entries'][0]['source'].update(result_kind='Unnumbered', result_number=None, result_name='Named coercivity statement', result_locator='Named coercivity statement, page 19')
        self.assertEqual(audit(d)[0], [])

    def test_proposed_can_have_open_source_gaps(self):
        d = example()
        d['entries'][0]['decision']['status'] = 'RETAINED_UNVERIFIED'
        d['entries'][0]['source']['primary_statement_checked'] = False
        self.assertEqual(audit(d)[0], [])

    def test_protected_scope_check_required(self):
        self.check_error(lambda e: e['decision'].update(protected_scope_checked=False), 'protected_scope_checked')

    def test_duplicate_candidate_id(self):
        d = example()
        d['entries'].append(deepcopy(d['entries'][0]))
        errors, _, _ = audit(d)
        self.assertTrue(any('repeated' in x for x in errors))


if __name__ == '__main__':
    unittest.main()
