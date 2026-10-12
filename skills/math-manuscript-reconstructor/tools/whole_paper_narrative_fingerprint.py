#!/usr/bin/env python3
import argparse, json, re, statistics
from pathlib import Path

WORD = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
FORMAL = re.compile(r'\b(?:Theorem|Lemma|Proposition|Corollary)\s+\d+(?:\.\d+)*\b', re.I)
MD_CHAPTER = re.compile(r'^#\s+\d+\s+.+$')
MD_INTRO = re.compile(r'^#{1,3}\s+Introduction\s*$', re.I)
MD_APPENDIX = re.compile(r'^#{1,3}\s+Appendix\b.*$', re.I)
LATEX_SECTION = re.compile(r'\\section\*?\{([^}]*)\}')
LATEX_APPENDIX = re.compile(r'\\appendix\b')


def wc(s):
    return len(WORD.findall(s))


def qstats(xs):
    if not xs:
        return {}
    d={'median':statistics.median(xs),'min':min(xs),'max':max(xs)}
    if len(xs)>=4:
        q=statistics.quantiles(xs,n=4)
        d.update({'q1':q[0],'q3':q[2]})
    return d


def cv(xs):
    if len(xs)<2 or statistics.mean(xs)==0:
        return None
    return statistics.pstdev(xs)/statistics.mean(xs)


def classify(title, appendix_mode=False):
    t=title.lower()
    if 'introduction' == t.strip() or t.strip().startswith('introduction'):
        return 'INTRODUCTION'
    if appendix_mode or 'appendix' in t:
        return 'APPENDIX'
    if any(k in t for k in ['references','bibliography','index','notes and references','symbol glossary']):
        return 'BACKMATTER'
    return 'BODY'


def markdown_units(lines):
    # Long expository corpus mode: numbered chapter headings are major units,
    # with book-level Introduction/Appendix retained as special units.
    has_chapters=any(MD_CHAPTER.match(l.strip()) for l in lines)
    marks=[]
    for i,l in enumerate(lines):
        s=l.strip()
        if has_chapters:
            if MD_CHAPTER.match(s) or MD_INTRO.match(s) or MD_APPENDIX.match(s):
                marks.append((i,re.sub(r'^#+\s*','',s)))
        else:
            m=re.match(r'^#{1,2}\s+(.+)$',s)
            if m:
                title=m.group(1).strip()
                if not re.search(r'contents|foreword|preface',title,re.I):
                    marks.append((i,title))
    return marks


def latex_units(text):
    app_pos=None
    mapp=LATEX_APPENDIX.search(text)
    if mapp: app_pos=mapp.start()
    marks=[]
    for m in LATEX_SECTION.finditer(text):
        title=m.group(1).strip()
        marks.append((m.start(),title, bool(app_pos is not None and m.start()>app_pos)))
    return marks


def records_markdown(text):
    lines=text.splitlines(); marks=markdown_units(lines)
    rec=[]
    for k,(i,title) in enumerate(marks):
        j=marks[k+1][0] if k+1<len(marks) else len(lines)
        seg='\n'.join(lines[i+1:j])
        role=classify(title)
        rec.append({'role':role,'words':wc(seg),'formal_count':len(FORMAL.findall(seg))})
    return rec


def records_latex(text):
    marks=latex_units(text); rec=[]
    for k,(pos,title,app) in enumerate(marks):
        end=marks[k+1][0] if k+1<len(marks) else len(text)
        # find end of heading command conservatively
        m=LATEX_SECTION.search(text,pos)
        seg=text[m.end():end] if m else text[pos:end]
        rec.append({'role':classify(title,app),'words':wc(seg),'formal_count':len(FORMAL.findall(seg))})
    return rec


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('path')
    args=ap.parse_args()
    p=Path(args.path)
    text=p.read_text(encoding='utf-8',errors='ignore')
    rec=records_latex(text) if '\\section' in text else records_markdown(text)
    body=[r for r in rec if r['role']=='BODY']
    intro=[r for r in rec if r['role']=='INTRODUCTION']
    app=[r for r in rec if r['role']=='APPENDIX']
    if not body:
        print(json.dumps({'status':'REVIEW','reason':'no_major_body_units_detected','numeric_targets_forbidden':True},indent=2)); return
    body_words=[r['words'] for r in body]
    formal=[r['formal_count'] for r in body]
    densities=[1000*r['formal_count']/r['words'] if r['words'] else 0 for r in body]
    total_body=sum(body_words)
    total_formal=sum(formal)
    sorted_w=sorted(body_words,reverse=True)
    sorted_f=sorted(formal,reverse=True)
    k=max(1,(len(body)+3)//4)
    out={
      'status':'OK',
      'major_body_unit_count':len(body),
      'body_unit_word_distribution':qstats(body_words),
      'body_unit_mass_cv':round(cv(body_words),4) if cv(body_words) is not None else None,
      'formal_result_count_distribution':qstats(formal),
      'formal_result_density_per_1000_words_distribution':qstats([round(x,4) for x in densities]),
      'largest_body_unit_share':round(max(body_words)/total_body,4) if total_body else None,
      'top_quartile_body_units_word_share':round(sum(sorted_w[:k])/total_body,4) if total_body else None,
      'top_quartile_body_units_formal_result_share':round(sum(sorted_f[:k])/total_formal,4) if total_formal else None,
      'introduction_count':len(intro),
      'introduction_words':sum(r['words'] for r in intro),
      'introduction_to_body_word_ratio':round(sum(r['words'] for r in intro)/total_body,6) if total_body else None,
      'appendix_count':len(app),
      'appendix_words':sum(r['words'] for r in app),
      'appendix_formal_results':sum(r['formal_count'] for r in app),
      'appendix_to_body_word_ratio':round(sum(r['words'] for r in app)/total_body,6) if total_body else None,
      'numeric_targets_forbidden':True,
      'stores_source_unit_prose':False,
      'emits_source_titles':False,
      'source_global_sequence_reuse':'forbidden',
      'source_mass_profile_reuse':'forbidden',
      'source_frontmatter_ratio_reuse':'forbidden',
      'source_appendix_pattern_reuse':'forbidden',
      'research_projection_required_for_long_expository_corpora':True
    }
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
