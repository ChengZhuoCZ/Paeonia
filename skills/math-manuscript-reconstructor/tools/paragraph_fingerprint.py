#!/usr/bin/env python3
import re, json, statistics, sys
from collections import Counter,defaultdict

src=sys.argv[1] if len(sys.argv)>1 else None
if not src: raise SystemExit('usage: paragraph_fingerprint.py SOURCE')
text=open(src,encoding='utf-8',errors='ignore').read()
proof_re=re.compile(r"(?:\*{1,2}\s*Proof(?:\s+of\s+[^*\n.]{0,80})?\s*\*{1,2}\s*[\.:]?|(?<![A-Za-z])Proof(?:\s+of\s+[^\n.]{0,80})?\s*[\.:])",re.I)
starts=list(proof_re.finditer(text))

heading_re=re.compile(r"\n\s*(?:#{1,6}\s+|\*{0,2}(?:Theorem|Lemma|Proposition|Corollary|Remark|Definition|Exercise|Problem)\b)",re.I)

def clean(s):
    s=re.sub(r"<[^>]+>"," ",s)
    s=re.sub(r"[*_#`|]"," ",s)
    s=re.sub(r"\\[A-Za-z]+\b(?:\{[^{}]{0,80}\})?"," ",s)
    s=re.sub(r"\s+"," ",s)
    return s.strip()

def wc(s): return len(re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?",clean(s)))
def sc(s):
    c=clean(s)
    return max(1,len([x for x in re.split(r"(?<=[.!?])\s+",c) if len(re.findall(r'[A-Za-z]+',x))>=3])) if c else 0

open_patterns={
'direct_action':r'^(?:we\s+)?(?:choose|define|set|let|write|fix|take|apply|integrate|differentiate|consider)\b',
'goal_or_reduction':r'^(?:to prove|to show|it suffices|it is enough|we may assume|we first reduce|by .* it suffices)\b',
'premise':r'^(?:since|because|as )\b',
'contrast_bridge':r'^(?:however|instead|in contrast|on the other hand|if .* merely|when .* merely|in general|for the general case)\b',
'recall_or_observe':r'^(?:recall|note|observe)\b',
'consequence':r'^(?:therefore|thus|hence|consequently|as a consequence)\b',
'return_or_next':r'^(?:we now|we next|we return|we can now|next)\b',
}
role_kw={
'BRIDGE':[r'\bhowever\b',r'\binstead\b',r'\bno longer\b',r'\bcannot\b',r'\bgeneral case\b',r'\bwe return\b',r'\bpass to\b',r'\bextend\b',r'\bapprox(?:imate|imation)\b'],
'DELICATE':[r'\buniform(?:ly)?\b',r'\bjustif(?:y|ied|ication)\b',r'\binterchange\b',r'\bcompact(?:ness)?\b',r'\bcontinu(?:ity|ous)\b',r'\bconvergen(?:ce|t)\b',r'\blimit\b',r'\bboundary\b',r'\bendpoint\b',r'\bdominated\b',r'\bregularity\b',r'\bequality\b',r'\bunique(?:ness)?\b'],
'STRUCTURAL':[r'\bidea\b',r'\bkey\b',r'\bit suffices\b',r'\breduce\b',r'\bdecomposition\b',r'\bwe claim\b',r'\bwe contend\b'],
'SURPRISING':[r'\bremarkable\b',r'\bstriking\b',r'\binteresting\b',r'\binterpretation\b',r'\bsurpris'],
'CLOSURE':[r'\bproof is complete\b',r'\bcompletes? the proof\b',r'\bthis proves\b',r'\bwe are done\b',r'\bas desired\b',r'\bconclude the proof\b'],
}

para_records=[]
seqs=[]
for m in starts:
    raw=text[m.end():m.end()+5500]
    hm=heading_re.search(raw)
    if hm and hm.start()>250: raw=raw[:hm.start()]
    paras=[]
    for p in re.split(r"\n\s*\n",raw):
        n=wc(p)
        if n<10 or n>420: continue
        c=clean(p)
        x=c.lower()
        op='object_or_other'
        for k,pat in open_patterns.items():
            if re.search(pat,x): op=k; break
        scores={k:sum(len(re.findall(pat,x,re.I)) for pat in pats) for k,pats in role_kw.items()}
        if scores['CLOSURE']>0: role='CLOSURE'
        elif scores['BRIDGE']>0 and (op in ('contrast_bridge','return_or_next') or scores['BRIDGE']>=2): role='BRIDGE'
        elif scores['DELICATE']>=2 or (scores['DELICATE']>=1 and n>=55): role='DELICATE'
        elif scores['SURPRISING']>0: role='SURPRISING'
        elif scores['STRUCTURAL']>0: role='STRUCTURAL'
        else: role='ROUTINE'
        paras.append(role)
        para_records.append((n,sc(p),op,role))
    if len(paras)>=1: seqs.append(paras)

lens=[r[0] for r in para_records]
sents=[r[1] for r in para_records]
roles=Counter(r[3] for r in para_records)
openings=Counter(r[2] for r in para_records)
role_lens=defaultdict(list)
role_sents=defaultdict(list)
for n,s,o,r in para_records:
    role_lens[r].append(n); role_sents[r].append(s)
trans=Counter()
for seq in seqs:
    for a,b in zip(seq,seq[1:]): trans[(a,b)]+=1

res={
'proofs':len(starts),'proof_sequences':len(seqs),'paragraphs':len(para_records),
'paragraph_words_mean':round(statistics.mean(lens),2) if lens else 0,
'paragraph_words_median':statistics.median(lens) if lens else 0,
'paragraph_words_p25':round(statistics.quantiles(lens,n=4)[0],1) if len(lens)>=4 else 0,
'paragraph_words_p75':round(statistics.quantiles(lens,n=4)[2],1) if len(lens)>=4 else 0,
'paragraph_sentences_mean':round(statistics.mean(sents),2) if sents else 0,
'opening_classes':dict(openings),
'role_counts':dict(roles),
'role_word_means':{r:round(statistics.mean(v),2) for r,v in role_lens.items()},
'role_word_medians':{r:statistics.median(v) for r,v in role_lens.items()},
'role_sentence_means':{r:round(statistics.mean(role_sents[r]),2) for r in role_sents},
'top_role_transitions':[{'from':a,'to':b,'count':c} for (a,b),c in trans.most_common(16)],
'one_paragraph_proof_fraction':round(sum(1 for x in seqs if len(x)==1)/max(1,len(seqs)),3),
'median_paragraphs_per_proof':statistics.median([len(x) for x in seqs]) if seqs else 0,
'paragraphs_per_proof_mean':round(statistics.mean([len(x) for x in seqs]),2) if seqs else 0,
'source_phrases_emitted':False,
'numeric_targets_forbidden':True,
'stores_source_paragraphs':False,
}
print(json.dumps(res,indent=2))
