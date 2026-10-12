#!/usr/bin/env python3
"""Observable inventory behavior; not tests of scholarly truth or prose quality."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from citation_inventory import inventory


class CitationInventoryTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, name, text):
        p = self.root / name
        p.write_text(text, encoding='utf-8')
        return p

    def test_nested_citations_and_notes_have_distinct_locations(self):
        p = self.write('paper.tex', r'''\citep[][cf.\ \citealp{B} for another topic]{A}
\begin{thebibliography}{9}
\bibitem{A} A title.
\bibitem{B} B title.
\end{thebibliography}''')
        r = inventory([p], [])
        self.assertTrue(r['mechanical_ok'])
        self.assertEqual(r['summary']['cited_defined_keys'], 2)
        self.assertEqual([c['keys'] for c in r['citation_calls']], [['A'], ['B']])
        self.assertIn(r'\citealp{B}', r['citation_calls'][0]['notes'][1])
        self.assertEqual(r['references'][0]['definitions'][0]['line'], 3)
        self.assertFalse(r['source_verification_performed'])
        self.assertEqual(r['references'][0]['review']['metadata'], 'not_checked')

    def test_comments_verbatim_and_escaped_percent(self):
        p = self.write('paper.tex', r'''% \cite{fake}
\begin{verbatim}
% literal \cite{fake2}
\end{verbatim}
\verb|\cite{fake3}| and 20\% \citet{A} % \cite{fake4}
\begin{thebibliography}{9}\bibitem{A} Title.\end{thebibliography}''')
        r = inventory([p], [])
        self.assertEqual(r['undefined_keys'], [])
        self.assertEqual(len(r['citation_calls']), 1)
        self.assertEqual(r['citation_calls'][0]['line'], 5)

    def test_nocite_does_not_count_as_discussion(self):
        p = self.write('paper.tex', r'''\cite{A}\nocite{*}
\begin{thebibliography}{9}\bibitem{A} A.\bibitem{B} B.\end{thebibliography}''')
        r = inventory([p], [])
        self.assertTrue(r['mechanical_ok'])
        self.assertEqual(r['uncited_keys'], ['B'])
        self.assertEqual(r['included_without_citation'], ['B'])
        self.assertEqual(r['summary']['cited_defined_keys'], 1)

    def test_undefined_and_duplicate_keys_are_separate(self):
        p = self.write('paper.tex', r'''\cite{missing}\nocite{absent}
\begin{thebibliography}{9}\bibitem{A} First.\bibitem{A} Second.\end{thebibliography}''')
        r = inventory([p], [])
        self.assertFalse(r['mechanical_ok'])
        self.assertEqual(r['undefined_keys'], ['missing'])
        self.assertEqual(r['undefined_nocite_keys'], ['absent'])
        self.assertEqual(r['duplicate_keys'], ['A'])

    def test_bibtex_braces_quotes_and_declared_file(self):
        tex = self.write('paper.tex', r'\parencite[Theorem~2]{A}\bibliography{refs}')
        bib = self.write('refs.bib', '''% discarded
@article{A,
 title = {An {API}, a theorem},
 author = "Doe, Jane and Roe, John",
 url = {https://example.test/a%20b},
 year = {2001}
}
@book(B, title="A book, with commas", year=2002)
''')
        before = tex.read_bytes(), bib.read_bytes()
        r = inventory([tex], [bib])
        self.assertTrue(r['mechanical_ok'])
        self.assertEqual(r['uncited_keys'], ['B'])
        self.assertEqual(r['references'][0]['definitions'][0]['fields']['title'], '{An {API}, a theorem}')
        self.assertIn('%20', r['references'][0]['definitions'][0]['fields']['url'])
        self.assertEqual(before, (tex.read_bytes(), bib.read_bytes()))

    def test_unscanned_input_is_reported_then_resolved(self):
        main = self.write('main.tex', r'\input{intro}\begin{thebibliography}{9}\bibitem{A} A.\end{thebibliography}')
        intro = self.write('intro.tex', r'\cite{A}')
        r = inventory([main], [])
        self.assertFalse(r['mechanical_ok'])
        self.assertEqual(r['coverage_issues'][0]['kind'], 'declared_file_not_scanned')
        r = inventory([main, intro], [])
        self.assertTrue(r['mechanical_ok'])
        self.assertEqual(r['uncited_keys'], [])

    def test_multicite_and_brace_shielded_closing_bracket(self):
        p = self.write('p.tex', r'''\textcites[see {a]b}][p.~1]{A}[p.~2]{B}
\begin{thebibliography}{9}\bibitem{A} A.\bibitem{B} B.\end{thebibliography}''')
        r = inventory([p], [])
        self.assertTrue(r['mechanical_ok'])
        self.assertEqual([c['keys'] for c in r['citation_calls']], [['A'], ['B']])
        self.assertEqual(r['citation_calls'][0]['notes'][0], 'see {a]b}')

    def test_macro_and_bibtex_inheritance_are_not_silently_verified(self):
        tex = self.write('p.tex', r'\cite{\mykey}\citeCustom{B}')
        bib = self.write('r.bib', '@book{B,title={T},crossref={Parent}}')
        r = inventory([tex], [bib])
        kinds = {x['kind'] for x in r['coverage_issues']}
        self.assertFalse(r['mechanical_ok'])
        self.assertTrue({'dynamic_or_empty_key', 'unsupported_command', 'unevaluated_bibtex_relation'} <= kinds)
        self.assertFalse(r['source_verification_performed'])

    def test_strict_cli_output_and_source_overwrite_guard(self):
        tex = self.write('p.tex', r'\cite{missing}')
        dest = self.root / 'inventory.json'
        tool = ROOT / 'tools/citation_inventory.py'
        cmd = [sys.executable, str(tool), '--tex', str(tex), '--strict', '--output', str(dest)]
        r = subprocess.run(cmd, capture_output=True, text=True)
        self.assertEqual(r.returncode, 1)
        self.assertEqual(json.loads(dest.read_text())['undefined_keys'], ['missing'])
        before = tex.read_bytes()
        r = subprocess.run(cmd[:-1] + [str(tex)], capture_output=True, text=True)
        self.assertEqual(r.returncode, 2)
        self.assertEqual(tex.read_bytes(), before)


if __name__ == '__main__':
    unittest.main()
