#!/usr/bin/env python3
"""Diagnostic paragraph-level audit. Produces review signals, not authorship scores."""
from __future__ import annotations
import re, json, sys, statistics
from pathlib import Path

def clean(s):
    s=re.sub(r"\\\[.*?\\\]|\$\$.*?\$\$|\$.*?\$"," ",s,flags=re.S)
    s=re.sub(r"\\begin\{[^}]+\}.*?\\end\{[^}]+\}"," ",s,flags=re.S)
    s=re.sub(r"\\[A-Za-z]+(?:\[[^]]*\])?(?:\{[^{}]*\})?"," ",s)
    s=re.sub(r"[*_#`|<>]"," ",s)
    return re.sub(r"\s+"," ",s).strip()

def wc(s): return len(re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", clean(s)))
def sc(s):
    c=clean(s)
    return len([x for x in re.split(r"(?<=[.!?])\s+",c) if len(re.findall(r'[A-Za-z]+',x))>=3]) if c else 0

def role(s):
    x=clean(s).lower(); n=wc(s)
    if re.search(r"\b(?:proof is complete|completes? the proof|this proves|as desired|we are done)\b",x): return 'CLOSURE'
    if re.search(r"\b(?:however|instead|no longer|cannot|general case|pass to|approximation|we return)\b",x): return 'BRIDGE'
    d=len(re.findall(r"\b(?:uniform|uniformly|interchange|compactness|continuity|convergence|limit|endpoint|boundary|regularity|equality|rigidity|justify|justified)\b",x))
    if d>=2 or (d>=1 and n>=55): return 'DELICATE'
    if re.search(r"\b(?:it suffices|reduce|decomposition|we claim|the idea|key point)\b",x): return 'STRUCTURAL'
    if re.search(r"\b(?:remarkable|striking|interpretation|interesting)\b",x): return 'SURPRISING'
    return 'ROUTINE'

def main():
    if len(sys.argv)<2: raise SystemExit('usage: paragraph_fingerprint_audit.py MANUSCRIPT')
    text=Path(sys.argv[1]).read_text(encoding='utf-8',errors='ignore')
    paras=[p for p in re.split(r"\n\s*\n",text) if 8<=wc(p)<=500]
    lens=[wc(p) for p in paras]
    sent=[sc(p) for p in paras]
    roles=[role(p) for p in paras]
    flags=[]
    if len(lens)>=20:
        mean=statistics.mean(lens); sd=statistics.pstdev(lens)
        if mean and sd/mean<0.28: flags.append('paragraph_length_homogeneity')
        if len(set(sent))<=2: flags.append('sentence_count_homogeneity')
    meta=sum(bool(re.match(r"^(?:we now|we next|we proceed|the next step|we turn)",clean(p).lower())) for p in paras)
    if paras and meta/len(paras)>0.12: flags.append('meta_led_opening_concentration')
    over=sum(r=='ROUTINE' and n>85 for r,n in zip(roles,lens))
    under=sum(r=='DELICATE' and n<22 for r,n in zip(roles,lens))
    if over>=3: flags.append('routine_overexplanation')
    if under>=2: flags.append('delicate_underexplanation')
    # exact three-sentence paragraph geometry over many paragraphs
    if len(sent)>=12 and sum(x==3 for x in sent)/len(sent)>0.70: flags.append('repeated_three_sentence_geometry')
    out={
      'status':'REVIEW' if flags else 'PASS',
      'paragraphs':len(paras),
      'flags':flags,
      'role_counts':{r:roles.count(r) for r in sorted(set(roles))},
      'statistics_are_generation_targets':False,
      'authorship_classifier':False,
    }
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
