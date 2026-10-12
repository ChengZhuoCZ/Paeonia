#!/usr/bin/env python3
"""Diagnostic audit for whether prose reacts to mathematical role.

This tool emits review signals only. It does not score authorship and does not
optimize toward source statistics.
"""
from __future__ import annotations
import argparse, json, re, statistics as st
from pathlib import Path

WORD=re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
DELICATE=re.compile(r"\b(limit|uniform|compact|approx|endpoint|boundary|equality|rigidity|uniqueness|regularity|interchange|dominated)\b",re.I)
BRIDGE=re.compile(r"\b(however|instead|no longer|cannot|general case|pass to|extend|replace|obstruction)\b",re.I)
ADMIN=re.compile(r"\b(in this section|we now|we next|we proceed|the next step|it is worth noting)\b",re.I)

def wc(x): return len(WORD.findall(x))

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('manuscript'); args=ap.parse_args()
    text=Path(args.manuscript).read_text(encoding='utf-8',errors='ignore')
    paras=[re.sub(r'\s+',' ',p).strip() for p in re.split(r'\n\s*\n',text) if 12<=wc(p)<=500]
    routine=[]; delicate=[]; bridge=[]
    for p in paras:
        if BRIDGE.search(p): bridge.append(wc(p))
        elif DELICATE.search(p): delicate.append(wc(p))
        else: routine.append(wc(p))
    med=lambda x: st.median(x) if x else None
    signals=[]
    if len(routine)>=8 and len(delicate)>=4 and med(delicate) is not None and med(routine) is not None and med(delicate)<=med(routine):
        signals.append('delicate_prose_not_thicker_than_routine_review')
    admin=len(ADMIN.findall(text)); words=max(1,wc(text))
    if 1000*admin/words>3:
        signals.append('administrative_transition_density_review')
    res={
      'paragraphs':len(paras),'routine_median_words':med(routine),'delicate_median_words':med(delicate),'bridge_median_words':med(bridge),
      'administrative_markers_per_1000_words':round(1000*admin/words,2),'review_signals':signals,
      'numeric_targeting_forbidden':True,'authorship_classifier':False
    }
    print(json.dumps(res,indent=2))
if __name__=='__main__': main()
