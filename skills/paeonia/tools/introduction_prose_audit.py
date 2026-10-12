#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from collections import Counter
from pathlib import Path

ADMIN_OPENERS = [
    r'^in this paper\b', r'^we now\b', r'^we next\b', r'^next\b',
    r'^more recently\b', r'^it is worth (?:noting|pointing out)\b',
    r'^it is important to note\b', r'^this result\b', r'^the next step\b',
    r'^on the other hand\b', r'^finally\b'
]
GENERIC_IMPORTANCE = [
    r'long and rich history', r'important topic in mathematics',
    r'fundamental problem in mathematics', r'wide range of applications',
    r'has attracted considerable attention', r'hot topic'
]
THEOREM_ADMIN = [
    r'we are now ready to state', r'we now state', r'we next state',
    r'the following theorem is our main result'
]
ITINERARY = [
    r'\bSection\s+\d+\s+(?:is|does|proves|establishes|develops|contains)',
    r'\bIn Section\s+\d+'
]
AUTHOR_CHRONOLOGY = [
    r'\bmore recently\b', r'\bmost recently\b', r'\bsubsequently\b',
    r'\blater\b', r'\brecent work by\b'
]

SENT_SPLIT = re.compile(r'(?<=[.!?])\s+(?=[A-Z\\])')


def strip_tex_commands(s: str) -> str:
    s = re.sub(r'%.*', '', s)
    s = re.sub(r'\\cite\w*\{[^}]*\}', ' ', s)
    s = re.sub(r'\\(?:ref|eqref)\{[^}]*\}', ' ', s)
    s = re.sub(r'\\[A-Za-z@]+\*?(?:\[[^\]]*\])?(?:\{[^{}]*\})?', ' ', s)
    s = re.sub(r'\$[^$]*\$', ' MATH ', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()


def paragraphs(text: str):
    # Remove display environments enough for prose diagnostics.
    text = re.sub(r'\\begin\{(?:equation\*?|align\*?|gather\*?|theorem|lemma|proposition|corollary)\}.*?\\end\{(?:equation\*?|align\*?|gather\*?|theorem|lemma|proposition|corollary)\}', '\n\n', text, flags=re.S)
    chunks = [c.strip() for c in re.split(r'\n\s*\n', text) if c.strip()]
    out=[]
    for c in chunks:
        if c.startswith('\\') and len(strip_tex_commands(c).split()) < 5:
            continue
        clean=strip_tex_commands(c)
        if len(clean.split()) >= 5:
            out.append(clean)
    return out


def first_words(p: str, n=3):
    words=re.findall(r"[A-Za-z][A-Za-z'-]*", p.lower())
    return ' '.join(words[:n])


def count_patterns(patterns, text):
    return sum(len(re.findall(p, text, flags=re.I|re.M)) for p in patterns)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('file', type=Path)
    ap.add_argument('--json', action='store_true')
    args=ap.parse_args()
    raw=args.file.read_text(encoding='utf-8', errors='ignore')
    ps=paragraphs(raw)
    openers=[]; sentence_counts=[]; admin_paras=[]
    for i,p in enumerate(ps,1):
        fw=first_words(p)
        if fw: openers.append(fw)
        sentence_counts.append(max(1,len(SENT_SPLIT.split(p))))
        if any(re.search(x,p,re.I) for x in ADMIN_OPENERS): admin_paras.append(i)
    opener_counts=Counter(openers)
    repeated=[{'opener':k,'count':v} for k,v in opener_counts.most_common() if v>=2]
    flags=[]
    generic=count_patterns(GENERIC_IMPORTANCE, raw)
    theorem_admin=count_patterns(THEOREM_ADMIN, raw)
    itinerary=count_patterns(ITINERARY, raw)
    chronology=count_patterns(AUTHOR_CHRONOLOGY, raw)
    if generic: flags.append('generic_importance_or_history_language')
    if len(admin_paras)>=3: flags.append('administrative_paragraph_openers_recur')
    if theorem_admin>=2: flags.append('ceremonial_theorem_announcements_recur')
    if itinerary>=3: flags.append('section_itinerary_may_dominate_mechanism')
    if chronology>=4: flags.append('chronology_markers_dense_review_literature_clusters')
    if repeated and ps:
        flags.append('paragraph_opening_shapes_repeat_review_for_template_rhythm')
    if len(sentence_counts)>=5 and len(set(sentence_counts))<=2:
        flags.append('paragraph_sentence_geometry_is_unusually_uniform')
    out={
        'status':'REVIEW' if flags else 'PASS',
        'paragraphs':len(ps),
        'administrative_opener_paragraphs':admin_paras,
        'repeated_paragraph_openers':repeated[:10],
        'generic_importance_markers':generic,
        'theorem_administration_markers':theorem_admin,
        'section_itinerary_markers':itinerary,
        'chronology_markers':chronology,
        'paragraph_sentence_counts':sentence_counts,
        'flags':flags,
        'diagnostic_only':True,
        'numeric_targets_forbidden':True,
        'no_automatic_synonym_rewrite':True,
    }
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
