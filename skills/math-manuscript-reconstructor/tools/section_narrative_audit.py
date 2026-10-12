#!/usr/bin/env python3
import argparse, json, re
from pathlib import Path

WORD=re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
SEC=re.compile(r'\\section\*?\{([^}]*)\}|^#{2,5}\s+[^#].*$',re.M)
SUB=re.compile(r'\\subsection\*?\{([^}]*)\}|^#{3,6}\s+[^#].*$',re.M)
META=re.compile(r'^(?:In this section|We now turn|We next turn|We proceed|We now consider|We next consider)\b',re.I)
FORMAL=re.compile(r'\b(?:Theorem|Lemma|Proposition|Corollary)\b')


def wc(s): return len(WORD.findall(s))

def split_sections(text):
    ms=list(SEC.finditer(text))
    out=[]
    for i,m in enumerate(ms):
        end=ms[i+1].start() if i+1<len(ms) else len(text)
        body=text[m.end():end]
        out.append(body)
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('path'); args=ap.parse_args()
    text=Path(args.path).read_text(encoding='utf-8',errors='ignore')
    sections=split_sections(text)
    flags=[]
    if not sections:
        print(json.dumps({'status':'REVIEW','flags':['no_sections_detected'],'diagnostic_only':True},indent=2)); return
    micro=0; one_sub=0; meta=0; dense_sub=0
    for body in sections:
        w=wc(body)
        subs=len(SUB.findall(body))
        if w<220: micro+=1
        if subs==1: one_sub+=1
        if w and subs*1000/w>3.5: dense_sub+=1
        # first prose-ish nonempty line
        for line in body.splitlines():
            s=re.sub(r'^[#*\s]+','',line).strip()
            if s and not s.startswith('\\'):
                if META.match(s): meta+=1
                break
    if len(sections)>=5 and micro/len(sections)>0.45: flags.append('many_microsections_review_section_worthiness')
    if one_sub>=3: flags.append('repeated_one_subsection_hierarchy_review')
    if dense_sub>=2: flags.append('subsection_fragmentation_review')
    if meta/len(sections)>0.5: flags.append('administrative_section_openings_review')
    # repeated near-uniform section geometry is a signal, not an error
    lens=[wc(s) for s in sections]
    if len(lens)>=6:
        mean=sum(lens)/len(lens)
        if mean>0:
            var=sum((x-mean)**2 for x in lens)/len(lens)
            cv=(var**0.5)/mean
            if cv<0.22: flags.append('section_length_geometry_unusually_uniform_review')
    out={
      'status':'REVIEW' if flags else 'OK',
      'flags':flags,
      'section_count':len(sections),
      'diagnostic_only':True,
      'numeric_targets_forbidden':True,
      'do_not_optimize_to_source_statistics':True
    }
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
