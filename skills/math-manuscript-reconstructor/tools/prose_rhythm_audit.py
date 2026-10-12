#!/usr/bin/env python3
import argparse, json, math, re, statistics
from pathlib import Path

MATH_BLOCKS = re.compile(r"\\\[(?:.|\n)*?\\\]|\\\((?:.|\n)*?\\\)|\$\$(?:.|\n)*?\$\$|\$(?:\\.|[^$])*?\$", re.S)
COMMAND = re.compile(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?(?:\{[^{}]*\})?")
WORD = re.compile(r"[A-Za-z][A-Za-z'-]*")

def clean(text):
    text=MATH_BLOCKS.sub(' ',text)
    text=COMMAND.sub(' ',text)
    text=re.sub(r'%.*',' ',text)
    return text

def stats(vals):
    if not vals: return {'count':0,'mean':0,'median':0,'stdev':0,'cv':0}
    mean=statistics.mean(vals)
    sd=statistics.pstdev(vals) if len(vals)>1 else 0
    return {
        'count':len(vals),
        'mean':round(mean,3),
        'median':round(statistics.median(vals),3),
        'stdev':round(sd,3),
        'cv':round(sd/mean,3) if mean else 0,
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('file')
    ap.add_argument('--fail-on-review', action='store_true')
    args=ap.parse_args()
    text=clean(Path(args.file).read_text(encoding='utf-8',errors='ignore'))
    paragraphs=[p.strip() for p in re.split(r'\n\s*\n',text) if len(WORD.findall(p))>=5]
    sentence_lengths=[]
    para_words=[]
    para_sentences=[]
    we_starts=0
    sentence_count=0
    for p in paragraphs:
        pw=len(WORD.findall(p)); para_words.append(pw)
        ss=[s.strip() for s in re.split(r'(?<=[.!?])\s+',p) if WORD.search(s)]
        para_sentences.append(len(ss))
        for s in ss:
            toks=WORD.findall(s)
            if not toks: continue
            sentence_count += 1
            sentence_lengths.append(len(toks))
            if toks[0].lower()=='we': we_starts += 1
    sst=stats(sentence_lengths); pst=stats(para_words); pss=stats(para_sentences)
    reasons=[]
    if sst['count']>=20 and sst['cv']<0.20:
        reasons.append('low_sentence_length_variation')
    if pst['count']>=8 and pst['cv']<0.22:
        reasons.append('low_paragraph_length_variation')
    if sentence_count>=12 and we_starts/sentence_count>0.35:
        reasons.append('high_first_person_sentence_start_concentration')
    out={
        'tool':'prose_rhythm_audit',
        'sentence_words':sst,
        'paragraph_words':pst,
        'sentences_per_paragraph':pss,
        'first_person_sentence_start_rate':round(we_starts/sentence_count,4) if sentence_count else 0,
        'review_reasons':reasons,
        'status':'REVIEW' if reasons else 'PASS',
        'note':'descriptive diagnostics only; do not randomize prose to hit a target',
    }
    print(json.dumps(out,indent=2,ensure_ascii=False))
    if args.fail_on_review and reasons:
        raise SystemExit(2)

if __name__=='__main__': main()
