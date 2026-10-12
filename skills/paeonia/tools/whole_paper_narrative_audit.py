#!/usr/bin/env python3
import argparse, json, re, statistics
from pathlib import Path

WORD=re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
FORMAL=re.compile(r'\b(?:Theorem|Lemma|Proposition|Corollary)\s+\d+(?:\.\d+)*\b',re.I)


def wc(s): return len(WORD.findall(s))


def parse_latex(text):
    pat=re.compile(r'\\section\*?\{([^}]*)\}')
    ms=list(pat.finditer(text)); out=[]; app=False
    app_pos=(re.search(r'\\appendix\b',text).start() if re.search(r'\\appendix\b',text) else None)
    for i,m in enumerate(ms):
        end=ms[i+1].start() if i+1<len(ms) else len(text)
        seg=text[m.end():end]; title=m.group(1).strip().lower()
        role='APPENDIX' if (app_pos is not None and m.start()>app_pos) or 'appendix' in title else ('INTRO' if 'introduction' in title else 'BODY')
        out.append((role,seg,title))
    return out


def parse_md(text):
    lines=text.splitlines(); marks=[]
    for i,l in enumerate(lines):
        m=re.match(r'^#{1,2}\s+(.+)$',l.strip())
        if m:
            t=m.group(1).strip()
            if re.search(r'contents|foreword|preface|bibliography|references|index',t,re.I): continue
            marks.append((i,t))
    out=[]
    for k,(i,t) in enumerate(marks):
        j=marks[k+1][0] if k+1<len(marks) else len(lines)
        role='APPENDIX' if 'appendix' in t.lower() else ('INTRO' if 'introduction' in t.lower() else 'BODY')
        out.append((role,'\n'.join(lines[i+1:j]),t.lower()))
    return out


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('path'); args=ap.parse_args()
    text=Path(args.path).read_text(encoding='utf-8',errors='ignore')
    units=parse_latex(text) if '\\section' in text else parse_md(text)
    body=[u for u in units if u[0]=='BODY']; intro=[u for u in units if u[0]=='INTRO']; app=[u for u in units if u[0]=='APPENDIX']
    flags=[]
    bw=[wc(u[1]) for u in body if wc(u[1])>0]
    if len(bw)>=5:
        mean=statistics.mean(bw); cv=statistics.pstdev(bw)/mean if mean else 0
        # Review signal only: unusually uniform substantial sections can indicate template mass balancing.
        if cv < 0.12:
            flags.append('REVIEW_SUSPICIOUSLY_UNIFORM_SECTION_MASS')
    if intro:
        intro_text='\n'.join(u[1] for u in intro)
        if len(FORMAL.findall(intro_text))==0:
            flags.append('REVIEW_MAIN_RESULT_NOT_FORMALLY_EXPOSED_IN_INTRODUCTION')
        admin=len(re.findall(r'\b(?:Section|section)\s+\d+\b',intro_text))
        if admin>=5:
            flags.append('REVIEW_INTRODUCTION_MAY_BE_SECTION_BY_SECTION_ADMINISTRATION')
    # Appendices with formal results but no textual body mention are worth reviewing.
    if app:
        body_text='\n'.join(u[1] for u in body)
        if len(FORMAL.findall('\n'.join(u[1] for u in app)))>0 and not re.search(r'\bappendix\b',body_text,re.I):
            flags.append('REVIEW_SUBSTANTIAL_APPENDIX_WITH_NO_BODY_IMPORT_SIGNAL')
    if any('conclusion' in u[2] for u in units):
        flags.append('REVIEW_CONCLUSION_SECTION_FOR_MATHEMATICAL_PAYLOAD_NOT_CEREMONY')
    out={
      'status':'REVIEW' if flags else 'OK',
      'flags':flags,
      'body_unit_count':len(body),
      'introduction_count':len(intro),
      'appendix_count':len(app),
      'numeric_targets_forbidden':True,
      'automatic_length_repair_forbidden':True,
      'source_profile_matching_forbidden':True
    }
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
