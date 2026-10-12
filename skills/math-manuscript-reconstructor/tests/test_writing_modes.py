#!/usr/bin/env python3
"""Test actual planner routing and non-expansion, not prose quality or NL intent."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from execution_planner import plan


class WritingModes(unittest.TestCase):
    def local(self, **overrides):
        task = dict(writing_mode='LOCAL_POLISH', editable_scope=['Introduction'],
                    protected_scope=['proof_body'], has_editing_baseline=True)
        task.update(overrides)
        return plan(task)

    def test_local_without_proof_gate_or_checksum(self):
        p = self.local(existing_proof_core_gate='NONE', semantic_checksum_available=False,
                       has_math_sources=False)
        self.assertEqual(p['required_states'], ['TASK_CONTRACT','EXECUTION_PLAN','EDIT','AUDIT','RELEASE'])
        self.assertEqual(p['applicable_gates'], ['MATH-SEMANTICS','NOTATION-CONSISTENCY'])
        self.assertEqual(p['writing_mode'], 'LOCAL_POLISH')
        self.assertEqual(p['protected_scope'], ['proof_body'])

    def test_whole_paper_polish_stays_local(self):
        p = self.local(editable_scope='whole_manuscript', protected_scope=[])
        self.assertEqual(p['workflow'], 'LOCAL_POLISH')
        self.assertNotIn('MANUSCRIPT_ARCHITECTURE', p['required_states'])

    def test_style_and_naturalization_do_not_escalate_polish(self):
        p = self.local(has_style_corpus=True, authorial_naturalization=True)
        self.assertNotIn('STYLE_QUARANTINE', p['required_states'])
        self.assertNotIn('SOURCE-INDEPENDENCE', p['applicable_gates'])
        self.assertEqual(p['conditional_states'], [])

    def test_polish_requires_baseline_and_scope(self):
        for bad in ({'has_editing_baseline': False}, {'editable_scope': []}):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                self.local(**bad)

    def test_conflicting_mode_cannot_silently_reconstruct(self):
        with self.assertRaises(ValueError):
            self.local(workflow='FULL_MANUSCRIPT_RECONSTRUCTION')

    def test_scoped_reconstruction_without_new_proof_gate(self):
        p = plan(dict(writing_mode='RECONSTRUCT', editable_scope=['Introduction'],
                      protected_scope=['proof_body'], has_math_sources=True,
                      existing_proof_core_gate='NONE'))
        self.assertEqual(p['workflow'], 'SCOPED_RECONSTRUCTION')
        self.assertIn('EXTRACT', p['required_states'])
        self.assertIn('SOURCE-INDEPENDENCE', p['applicable_gates'])
        self.assertNotIn('PROOF_CORE', p['required_states'])
        self.assertNotIn('PROOF-CLOSURE', p['applicable_gates'])

    def test_scoped_reconstruction_requires_explicit_sources(self):
        with self.assertRaises(ValueError):
            plan(dict(writing_mode='RECONSTRUCT', editable_scope=['Introduction']))

    def test_scoped_style_extraction_does_not_require_global_fingerprints(self):
        p = plan(dict(writing_mode='RECONSTRUCT', editable_scope=['Introduction'],
                      has_math_sources=True, has_style_corpus=True))
        states = p['required_states']
        self.assertLess(states.index('STYLE_EXTRACT'), states.index('STYLE_QUARANTINE'))
        self.assertLess(states.index('STYLE_QUARANTINE'), states.index('EDIT'))
        self.assertNotIn('WHOLE_PAPER_FINGERPRINT_LOCK', states)

    def test_full_reconstruction_preserves_proof_first(self):
        p = plan(dict(writing_mode='RECONSTRUCT', editable_scope=['whole_manuscript'], has_math_sources=True))
        states = p['required_states']
        self.assertEqual(p['workflow'], 'FULL_MANUSCRIPT_RECONSTRUCTION')
        self.assertLess(states.index('PROOF_CORE_GATE'), states.index('FRONTMATTER'))

    def test_advice_cannot_expand_local_or_scoped_work(self):
        tasks = [dict(writing_mode='LOCAL_POLISH', has_editing_baseline=True),
                 dict(writing_mode='RECONSTRUCT', has_math_sources=True)]
        for task in tasks:
            with self.subTest(mode=task['writing_mode']):
                p = plan(dict(task, editable_scope=['Introduction'], has_style_corpus=True,
                              existing_proof_core_gate='PASS', director_advice={
                                  'recommended_required_states': ['PROOF_CORE','MANUSCRIPT_ARCHITECTURE','FRONTMATTER'],
                                  'recommended_skips': ['EDIT']}))
                self.assertEqual(len(p['director_advice_review']['rejected']), 4)
                self.assertNotIn('PROOF_CORE', p['required_states'])
                self.assertIn('EDIT', p['required_states'])

    def test_legacy_polish_advice_cannot_add_proof(self):
        p = plan(dict(workflow='LATEX_NOTATION_ONLY', semantic_checksum_available=True,
                      director_advice={'recommended_required_states':['PROOF_CORE']}))
        self.assertNotIn('PROOF_CORE', p['required_states'])

    def test_read_only_workflows_have_no_writing_mode(self):
        for workflow in ['STYLE_DISTILLATION_ONLY', 'SUBMISSION_AUDIT_ONLY']:
            with self.subTest(workflow=workflow):
                p = plan(dict(workflow=workflow, has_style_corpus=True))
                self.assertIsNone(p['writing_mode'])
                self.assertNotIn('EDIT', p['required_states'])

    def test_boundaries_not_silently_discarded(self):
        bad = [dict(workflow='FULL_MANUSCRIPT_RECONSTRUCTION', editable_scope=['Introduction']),
               dict(workflow='FULL_MANUSCRIPT_RECONSTRUCTION', protected_scope=['opening']),
               dict(workflow='SCOPED_RECONSTRUCTION', editable_scope=['whole_manuscript']),
               dict(writing_mode='LOCAL_POLISH', has_editing_baseline=True,
                    editable_scope=['Introduction'], protected_scope=['Introduction'])]
        for task in bad:
            with self.subTest(task=task), self.assertRaises(ValueError):
                plan(task)

    def test_requested_output_checks_remain_active(self):
        p = self.local(latex_output=True, citations_or_external_inputs=True)
        self.assertIn('LATEX-INTEGRITY', p['applicable_gates'])
        self.assertIn('CITATION-INTEGRITY', p['applicable_gates'])


if __name__ == '__main__':
    unittest.main()
