#!/usr/bin/env python3
"""High-intensity conditional style distillation for mathematical prose.

The tool emits only aggregate, role-conditioned evidence. It never emits source
sentences, n-grams, phrase inventories, or paragraph templates.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import statistics as st
from collections import Counter, defaultdict
from pathlib import Path

WORD_RE = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
SENT_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
PROOF_RE = re.compile(
    r"(?:\*{1,2}\s*Proof(?:\s+of\s+[^*\n.]{0,90})?\s*\*{1,2}\s*[\.:]?|(?<![A-Za-z])Proof(?:\s+of\s+[^\n.]{0,90})?\s*[\.:])",
    re.I,
)
FORMAL_RE = re.compile(r"(?:\*{0,2})(Theorem|Lemma|Proposition|Corollary|Definition|Remark)\s+\d", re.I)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$", re.M)

TRANSITIONS = {
    "premise": [r"\bsince\b", r"\bbecause\b", r"\bwhenever\b"],
    "consequence": [r"\btherefore\b", r"\bthus\b", r"\bhence\b", r"\bconsequently\b", r"\bas a consequence\b"],
    "construction": [r"\bchoose\b", r"\bdefine\b", r"\bset\b", r"\blet\b", r"\bwrite\b", r"\bfix\b"],
    "reduction": [r"\bit suffices\b", r"\bit is enough\b", r"\bwe may assume\b", r"\breduce(?:s|d)? to\b"],
    "contrast": [r"\bhowever\b", r"\binstead\b", r"\bon the other hand\b", r"\bin contrast\b"],
    "recollection": [r"\brecall\b", r"\bnote that\b", r"\bobserve that\b"],
    "closure": [r"\bthis proves\b", r"\bwhich proves\b", r"\bproof is complete\b", r"\bcompletes? the proof\b", r"\bas desired\b"],
}

OPENER_PATTERNS = [
    ("premise_led", r"^(since|because|whenever|if|when)\b"),
    ("consequence_led", r"^(therefore|thus|hence|consequently|as a consequence)\b"),
    ("contrast_led", r"^(however|instead|on the other hand|in contrast)\b"),
    ("goal_or_reduction_led", r"^(to prove|to show|it suffices|it is enough|we may assume)\b"),
    ("action_led", r"^(choose|define|set|let|write|fix|apply|integrate|differentiate|consider)\b"),
    ("recollection_led", r"^(recall|note|observe)\b"),
    ("first_person_led", r"^(we|our)\b"),
    ("administrative_led", r"^(we now|we next|in this section|the next step|we shall now|we turn now)\b"),
]

BRIDGE_PAT = re.compile(
    r"\b(no longer|cannot|instead|general case|merely|approx(?:imate|imation)|density|extend|pass to the limit|analytic continuation|lift this restriction|remove this restriction|rough|smooth case|continuous case|real-valued|complex-valued)\b",
    re.I,
)
DELICATE_PAT = re.compile(
    r"\b(uniform(?:ly)?|compact(?:ness)?|dominated|interchange|limit|boundary term|endpoint|regularity|continuity|convergen(?:ce|t)|equality|uniqueness|invertible|holomorphic|analytic continuation)\b",
    re.I,
)
ESTIMATE_PAT = re.compile(
    r"\b(estimate|bounded by|majorized|dominated by|at most|at least|upper bound|lower bound|split|tail|near|far|large|small parameter|uniformly)\b",
    re.I,
)
INTERP_PAT = re.compile(
    r"\b(interpret(?:ation|ed)?|geometric|conceptual|means that|says that|view(?:ed)? as|idea behind|in other words|suggests that|remarkable|striking)\b",
    re.I,
)
CLOSURE_PAT = re.compile(r"\b(proof is complete|completes? the proof|this proves|as desired|conclude(?:s|d)? the proof)\b", re.I)
EASE_PAT = re.compile(r"\b(clearly|obviously|immediate(?:ly)?|straightforward|simple)\b", re.I)
READER_PAT = re.compile(r"\b(the reader|we leave .* reader|you)\b", re.I)
FIRST_PERSON_PAT = re.compile(r"\b(we|our)\b", re.I)
CLAUSE_PAT = re.compile(r"\b(if|when|whenever|since|because|although|while|whereas|which|that|so that|provided that|unless)\b", re.I)
ADMIN_PAT = re.compile(r"\b(in this section|we now|we next|we proceed|the next step|it is worth noting|we shall now)\b", re.I)


def clean(s: str) -> str:
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\\[A-Za-z]+\b(?:\{[^{}]{0,120}\})?", " ", s)
    s = re.sub(r"[*_#`|]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def words(s: str) -> list[str]:
    return WORD_RE.findall(clean(s))


def sentences(s: str) -> list[str]:
    c = clean(s)
    out=[]
    for x in SENT_SPLIT_RE.split(c):
        n=len(WORD_RE.findall(x))
        if 4 <= n <= 150:
            out.append(x.strip())
    return out


def q(vals, p):
    if not vals:
        return 0
    vals=sorted(vals)
    pos=(len(vals)-1)*p
    lo=int(math.floor(pos)); hi=int(math.ceil(pos))
    if lo==hi: return vals[lo]
    return vals[lo]*(hi-pos)+vals[hi]*(pos-lo)


def formula_density(raw: str) -> float:
    # OCR/Markdown formula proxy: non-word math punctuation + common TeX-like tokens.
    mathish = len(re.findall(r"[=<>∫Σ∑πξθΩΓλµ±∞^_/]|\\[A-Za-z]+", raw))
    return mathish / max(1, len(raw))


def opener_class(s: str) -> str:
    x=clean(s).lower()
    for label, pat in OPENER_PATTERNS:
        if re.search(pat,x): return label
    return "object_or_other_led"


def in_spans(pos, spans):
    # spans sorted; linear scan is okay for corpus size.
    for a,b in spans:
        if a <= pos < b: return True
        if a > pos: break
    return False


def build_proof_spans(text: str):
    starts=list(PROOF_RE.finditer(text))
    next_boundary=re.compile(r"\n\s*(?:#{1,6}\s+|\*{0,2}(?:Theorem|Lemma|Proposition|Corollary|Definition|Remark|Exercise|Problem)\b)", re.I)
    spans=[]
    for m in starts:
        tail=text[m.end():m.end()+9000]
        b=next_boundary.search(tail)
        end=m.end()+(b.start() if b and b.start()>180 else min(len(tail),6500))
        spans.append((m.end(), min(len(text),end)))
    return spans


def heading_context(text: str):
    hs=[]
    for m in HEADING_RE.finditer(text):
        hs.append((m.start(),len(m.group(1)),clean(m.group(2))))
    return hs


def current_heading(pos, hs):
    h=""
    for p,l,t in hs:
        if p>pos: break
        if l<=3: h=t
    return h


def section_open_positions(text: str, hs):
    # first two substantial paragraphs after level 1-3 headings.
    out=[]
    for p,l,t in hs:
        if l>3: continue
        tail=text[p: p+3500]
        # skip heading line
        nl=tail.find("\n")
        if nl<0: continue
        base=p+nl+1
        cur=base
        count=0
        for part in re.finditer(r"(?:^|\n\s*\n)(.*?)(?=\n\s*\n|$)", text[base:base+3200], re.S):
            raw=part.group(1)
            if len(words(raw))>=18:
                out.append((base+part.start(1), base+part.end(1)))
                count+=1
                if count>=2: break
    return out


def primary_stratum(raw, pos, text, proof_spans, section_spans, hs):
    c=clean(raw); x=c.lower(); fd=formula_density(raw)
    h=current_heading(pos,hs).lower()
    if in_spans(pos, proof_spans):
        if CLOSURE_PAT.search(x): return "PROOF_CLOSURE"
        if BRIDGE_PAT.search(x): return "PROOF_BRIDGE"
        if ESTIMATE_PAT.search(x) and (fd>0.012 or len(words(raw))>=55): return "PROOF_TECHNICAL_ESTIMATE"
        if DELICATE_PAT.search(x) and len(words(raw))>=48: return "PROOF_DELICATE"
        return "PROOF_ROUTINE"
    # lead-in: formal statement begins shortly after paragraph
    nxt=text[pos+len(raw):pos+len(raw)+900]
    if FORMAL_RE.search(nxt): return "THEOREM_LEADIN"
    if in_spans(pos,section_spans):
        if "introduction" in h or "preface" in h or "foreword" in h:
            return "INTRO_ORIENTATION"
        return "SECTION_OPENING"
    if "introduction" in h or "preface" in h or "foreword" in h:
        return "INTRO_ORIENTATION"
    if INTERP_PAT.search(x): return "CONCEPTUAL_INTERPRETATION"
    return "GENERAL_EXPOSITION"


def paragraph_records(text: str):
    proof_spans=build_proof_spans(text)
    hs=heading_context(text)
    section_spans=section_open_positions(text,hs)
    recs=[]
    # preserve positions by scanning blank-line blocks
    block_re=re.compile(r"(?:^|\n\s*\n)(.*?)(?=\n\s*\n|$)", re.S)
    for m in block_re.finditer(text):
        raw=m.group(1)
        if re.match(r"\s*#{1,6}\s+",raw): continue
        if "Ibookroot" in raw: continue
        w=words(raw)
        if not (12 <= len(w) <= 500): continue
        ss=sentences(raw)
        if not ss: continue
        pos=m.start(1)
        stratum=primary_stratum(raw,pos,text,proof_spans,section_spans,hs)
        recs.append({
            "pos":pos,
            "stratum":stratum,
            "words":len(w),
            "sentences":len(ss),
            "sentence_lengths":[len(WORD_RE.findall(s)) for s in ss],
            "openers":[opener_class(s) for s in ss],
            "first_person":len(FIRST_PERSON_PAT.findall(clean(raw))),
            "reader":len(READER_PAT.findall(clean(raw))),
            "ease":len(EASE_PAT.findall(clean(raw))),
            "admin":len(ADMIN_PAT.findall(clean(raw))),
            "clauses":len(CLAUSE_PAT.findall(clean(raw))),
            "transitions":{k:sum(len(re.findall(p,clean(raw),re.I)) for p in pats) for k,pats in TRANSITIONS.items()},
            "semicolon":raw.count(';'),
            "colon":raw.count(':'),
            "paren":raw.count('(')+raw.count(')'),
            "formula_density":formula_density(raw),
        })
    return recs


def summarize(recs):
    wc=[r['words'] for r in recs]
    sl=[x for r in recs for x in r['sentence_lengths']]
    sc=[r['sentences'] for r in recs]
    total_words=sum(wc) or 1
    total_sents=sum(sc) or 1
    openers=Counter(x for r in recs for x in r['openers'])
    trans=Counter()
    for r in recs: trans.update(r['transitions'])
    return {
        "paragraphs":len(recs),
        "words":sum(wc),
        "paragraph_words_median":round(q(wc,.5),2),
        "paragraph_words_iqr":[round(q(wc,.25),2),round(q(wc,.75),2)],
        "sentences_per_paragraph_median":round(q(sc,.5),2),
        "sentence_words_median":round(q(sl,.5),2),
        "sentence_words_iqr":[round(q(sl,.25),2),round(q(sl,.75),2)],
        "first_person_per_1000_words":round(1000*sum(r['first_person'] for r in recs)/total_words,2),
        "reader_address_per_1000_words":round(1000*sum(r['reader'] for r in recs)/total_words,2),
        "ease_markers_per_1000_words":round(1000*sum(r['ease'] for r in recs)/total_words,2),
        "administrative_markers_per_1000_words":round(1000*sum(r['admin'] for r in recs)/total_words,2),
        "clause_markers_per_sentence":round(sum(r['clauses'] for r in recs)/total_sents,3),
        "semicolon_per_100_sentences":round(100*sum(r['semicolon'] for r in recs)/total_sents,2),
        "colon_per_100_sentences":round(100*sum(r['colon'] for r in recs)/total_sents,2),
        "parenthesis_marks_per_100_sentences":round(100*sum(r['paren'] for r in recs)/total_sents,2),
        "formula_density_median":round(q([r['formula_density'] for r in recs],.5),4),
        "sentence_opener_distribution":{k:round(v/max(1,sum(openers.values())),3) for k,v in sorted(openers.items())},
        "transition_density_per_1000_words":{k:round(1000*v/total_words,2) for k,v in sorted(trans.items())},
    }


def fold_stability(recs, text_len, nfolds=8):
    metric_names=["paragraph_words_median","sentence_words_median","first_person_per_1000_words","administrative_markers_per_1000_words","clause_markers_per_sentence"]
    by=defaultdict(list)
    for i in range(nfolds):
        a=text_len*i/nfolds; b=text_len*(i+1)/nfolds
        rs=[r for r in recs if a<=r['pos']<b]
        groups=defaultdict(list)
        for r in rs: groups[r['stratum']].append(r)
        for s,g in groups.items():
            if len(g)<10: continue
            sm=summarize(g)
            for mn in metric_names: by[(s,mn)].append(sm[mn])
    out={}
    for (s,mn),vals in by.items():
        if len(vals)<4: continue
        med=q(vals,.5); mad=q([abs(x-med) for x in vals],.5)
        scale=max(abs(med),1e-6)
        rel=mad/scale
        conf="strong" if len(vals)>=6 and rel<=.25 else "moderate" if len(vals)>=4 and rel<=.5 else "tentative"
        out.setdefault(s,{})[mn]={
            "folds":len(vals),"median":round(med,3),"range":[round(min(vals),3),round(max(vals),3)],"relative_mad":round(rel,3),"confidence":conf
        }
    return out


def contrast(a,b,summary):
    A=summary.get(a,{}); B=summary.get(b,{})
    if not A or not B: return None
    keys=["paragraph_words_median","sentence_words_median","first_person_per_1000_words","administrative_markers_per_1000_words","clause_markers_per_sentence"]
    return {k:round(B[k]-A[k],3) for k in keys}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('source')
    ap.add_argument('--folds',type=int,default=8)
    args=ap.parse_args()
    text=Path(args.source).read_text(encoding='utf-8',errors='ignore')
    recs=paragraph_records(text)
    groups=defaultdict(list)
    for r in recs: groups[r['stratum']].append(r)
    summaries={s:summarize(g) for s,g in sorted(groups.items())}
    result={
        "corpus_chars":len(text),
        "usable_paragraphs":len(recs),
        "strata":summaries,
        "cross_fold_stability":fold_stability(recs,len(text),args.folds),
        "conditional_contrasts":{
            "routine_to_delicate":contrast("PROOF_ROUTINE","PROOF_DELICATE",summaries),
            "routine_to_bridge":contrast("PROOF_ROUTINE","PROOF_BRIDGE",summaries),
            "routine_to_technical_estimate":contrast("PROOF_ROUTINE","PROOF_TECHNICAL_ESTIMATE",summaries),
            "general_to_section_opening":contrast("GENERAL_EXPOSITION","SECTION_OPENING",summaries),
            "general_to_intro_orientation":contrast("GENERAL_EXPOSITION","INTRO_ORIENTATION",summaries),
        },
        "interpretation_policy":{
            "numbers_are_evidence_not_generation_targets":True,
            "retain_only_cross_context_stable_traits_as_defaults":True,
            "context_conditioned_traits_override_global_average":True,
            "source_phrases_emitted":False,
            "source_sentences_stored":False,
            "source_paragraphs_stored":False,
        }
    }
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__': main()
