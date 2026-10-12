#!/usr/bin/env python3
import argparse, json, re, statistics
from pathlib import Path
from collections import Counter, defaultdict

WORD = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
FORMAL = re.compile(r'^\s*(?:\*\*)?(Theorem|Lemma|Proposition|Corollary)\s+\d+(?:\.\d+)*\b', re.I)
MD_CHAPTER = re.compile(r'^#\s+\d+\s+.+$')
MD_SECTION = re.compile(r'^#####\s+(\d+)\s+([A-Za-z].+)$')
PLAIN_SUB = re.compile(r'^(?:#####\s+)?(\d+\.\d+)\s+([A-Za-z].+)$')
LATEX_SECTION = re.compile(r'\\section\*?\{([^}]*)\}')
LATEX_SUB = re.compile(r'\\subsection\*?\{([^}]*)\}')


def wc(s):
    return len(WORD.findall(s))


def is_noise_title(title):
    return bool(re.search(r'\b(exercises?|problems?)\b', title, re.I))


def parse_markdown(lines):
    chapters=[]
    for i,l in enumerate(lines):
        if MD_CHAPTER.match(l.strip()):
            chapters.append(i)
    sections=[]
    for i,l in enumerate(lines):
        m=MD_SECTION.match(l.strip())
        if not m: continue
        n=int(m.group(1)); title=m.group(2).strip()
        if n<=0 or is_noise_title(title) or 'Ibookroot' in title: continue
        prev_ch=max([x for x in chapters if x < i], default=-1)
        next_ch=min([x for x in chapters if x > i], default=len(lines))
        sections.append((i, title, prev_ch, next_ch))
    rec=[]
    for idx,(i,title,ch_s,ch_e) in enumerate(sections):
        end=ch_e
        for j in range(idx+1,len(sections)):
            if sections[j][2]==ch_s:
                end=sections[j][0]
                break
            if sections[j][2]!=ch_s:
                break
        seg_lines=lines[i+1:end]
        rec.append(build_record(seg_lines, title))
    return rec


def parse_latex(text):
    matches=list(LATEX_SECTION.finditer(text))
    rec=[]
    for k,m in enumerate(matches):
        title=m.group(1)
        if is_noise_title(title): continue
        end=matches[k+1].start() if k+1<len(matches) else len(text)
        seg=text[m.end():end]
        lines=seg.splitlines()
        r=build_record(lines,title)
        r['sub_count']=len(LATEX_SUB.findall(seg))
        rec.append(r)
    return rec


def build_record(seg_lines,title):
    seg='\n'.join(seg_lines)
    sub_count=0
    for l in seg_lines:
        if PLAIN_SUB.match(l.strip()): sub_count+=1
    first=None; formal_count=0
    for j,l in enumerate(seg_lines):
        s=re.sub(r'^[#\s]+','',l)
        if FORMAL.match(s):
            formal_count+=1
            if first is None:
                first=wc('\n'.join(seg_lines[:j]))
    # OCR may put multiple formal statements on one line; add conservative inline count beyond line-start hits.
    inline=len(re.findall(r'\b(?:Theorem|Lemma|Proposition|Corollary)\s+\d+(?:\.\d+)*', seg))
    formal_count=max(formal_count,inline)
    words=wc(seg)
    return {'words':words,'sub_count':sub_count,'first_formal_offset_words':first,'formal_count':formal_count}


def latency(off):
    if off is None: return 'NO_FORMAL_RESULT'
    if off <= 100: return 'IMMEDIATE'
    if off <= 300: return 'MOTIVATED'
    if off <= 700: return 'DEVELOPED'
    return 'DEFERRED'


def median_or_none(xs):
    return statistics.median(xs) if xs else None


def quartiles(xs):
    if len(xs)<4: return {}
    q=statistics.quantiles(xs,n=4)
    return {'q1':q[0],'median':statistics.median(xs),'q3':q[2]}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('path')
    args=ap.parse_args()
    p=Path(args.path)
    text=p.read_text(encoding='utf-8',errors='ignore')
    lines=text.splitlines()
    rec=parse_latex(text) if '\\section' in text else parse_markdown(lines)
    if not rec:
        out={'status':'REVIEW','reason':'no_sections_detected','numeric_targets_forbidden':True,'stores_source_sections':False,'emits_source_titles':False}
        print(json.dumps(out,indent=2)); return
    lat=Counter(latency(r['first_formal_offset_words']) for r in rec)
    word_counts=[r['words'] for r in rec]
    formal_counts=[r['formal_count'] for r in rec]
    bins=[(0,800),(800,1500),(1500,3000),(3000,6000),(6000,10**12)]
    subbins={}
    for a,b in bins:
        rr=[r for r in rec if a<=r['words']<b]
        if rr:
            subbins[f'{a}-{b if b<10**12 else "plus"}']={
                'sections':len(rr),
                'with_subsections':sum(r['sub_count']>0 for r in rr),
                'with_subsections_rate':round(sum(r['sub_count']>0 for r in rr)/len(rr),4)
            }
    out={
      'status':'OK',
      'section_count':len(rec),
      'subsection_zero_count':sum(r['sub_count']==0 for r in rec),
      'subsection_nonzero_count':sum(r['sub_count']>0 for r in rec),
      'section_word_distribution':quartiles(word_counts),
      'formal_result_count_distribution':quartiles(formal_counts),
      'theorem_latency_counts':dict(lat),
      'subsection_use_by_broad_size_bin':subbins,
      'numeric_targets_forbidden':True,
      'stores_source_sections':False,
      'emits_source_titles':False,
      'source_section_order_reuse':'forbidden',
      'source_subsection_pattern_reuse':'forbidden'
    }
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
