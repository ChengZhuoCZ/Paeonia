#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from pathlib import Path

GENERIC_HISTORY=[
    r'long and rich history', r'has attracted considerable attention', r'important topic in mathematics',
    r'fundamental problem in mathematics', r'wide range of applications'
]
HYPE=[r'groundbreaking', r'major breakthrough', r'far-reaching', r'revolutionary']
ITINERARY=[r'Section\s+\d+\s+(?:is|does|proves|establishes|develops|contains)', r'In Section\s+\d+']
OBSTRUCTION=[r'however', r'obstruction', r'fails?', r'does not extend', r'cannot be applied', r'nonlocal', r'degener', r'lack of', r'prevents?']
THEOREM=[r'\\begin\{theorem\}', r'Theorem\s+\d', r'we prove', r'we establish', r'we show']

def count(patterns,text):
    return sum(len(re.findall(p,text,re.I)) for p in patterns)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('file', type=Path)
    ap.add_argument('--json', action='store_true')
    args=ap.parse_args()
    text=args.file.read_text(encoding='utf-8',errors='ignore')
    words=len(re.findall(r"\b[\w'-]+\b",text))
    generic=count(GENERIC_HISTORY,text)
    hype=count(HYPE,text)
    itinerary=count(ITINERARY,text)
    obstruction=count(OBSTRUCTION,text)
    theorem=count(THEOREM,text)
    flags=[]
    if generic: flags.append('generic_history_or_importance_opening')
    if hype: flags.append('evaluative_hype_language')
    if itinerary>=3: flags.append('section_itinerary_dominates_mechanism')
    if words>500 and theorem==0: flags.append('main_result_not_exposed_in_long_introduction')
    if words>700 and obstruction==0: flags.append('no_visible_problem_tension_or_obstruction')
    out={
        'status':'REVIEW' if flags else 'PASS',
        'words':words,
        'generic_history_markers':generic,
        'hype_markers':hype,
        'section_itinerary_markers':itinerary,
        'obstruction_markers':obstruction,
        'main_result_markers':theorem,
        'flags':flags,
        'detector_is_diagnostic_only':True,
        'numeric_targets_forbidden':True,
    }
    print(json.dumps(out,indent=2,ensure_ascii=False))

if __name__=='__main__': main()
