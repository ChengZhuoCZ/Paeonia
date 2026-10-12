#!/usr/bin/env python3
"""Source-level ban on visual boxes in mathematical LaTeX manuscripts.

Best-effort static analysis, *not* a compiled-PDF visual certification.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

# Literal macros with known framed/colored/highlighted output.
BAD_COMMANDS = (
    'boxed', 'Aboxed', 'bbox', 'fbox', 'framebox', 'colorbox', 'fcolorbox',
    'shadowbox', 'doublebox', 'ovalbox', 'Ovalbox', 'tcbox', 'tcboxfit',
    'tcbhighmath', 'newtcolorbox', 'newtcbox', 'NewTColorBox',
    'DeclareTColorBox', 'tcolorbox', 'Tcolorbox',
)
BAD_ENVIRONMENTS = (
    'tcolorbox', 'mdframed', 'framed', 'shaded', 'snugshade',
    'boxed', 'boxedminipage', 'box', 'Box', 'shadebox',
)
BAD_PACKAGES = {'tcolorbox', 'mdframed', 'framed', 'fancybox'}
VERBATIM_ENVIRONMENTS = ('verbatim', 'Verbatim', 'lstlisting', 'minted', 'filecontents', 'filecontents*', 'comment')

# A conservatively estimated pattern must be reviewed, not automatically banned.
PATTERNS = [
    ('BOX_MACRO', re.compile(r'\\(?:' + '|'.join(map(re.escape, BAD_COMMANDS)) + r')(?![A-Za-z@])')),
    ('BOX_ENV', re.compile(r'\\(?:begin|end)\s*\{([^}\n]*)\}')),
    ('BOX_PACKAGE', re.compile(r'\\(?:usepackage|RequirePackage)(?:\s*\[[^\]]*\])?\s*\{([^}]*)\}')),
    ('BOX_EQUATION_OPTION', re.compile(r'\\begin\s*\{empheq\}\s*\[([^]]*)\]', re.S)),
    ('BOX_ENV_DEFINITION', re.compile(r'\\(?:newenvironment|renewenvironment|NewDocumentEnvironment)\s*\{([^}\n]*)\}')),
]
INCLUDES = re.compile(r'\\(?:input|include|subfile)\s*\{([^}\n]+)\}')
VERBATIM = re.compile(r'\\begin\s*\{('+'|'.join(map(re.escape,VERBATIM_ENVIRONMENTS))+r')\}(.*?)\\end\s*\{\1\}', re.S)


def blank_except_newlines(s: str) -> str:
    return ''.join('\n' if c == '\n' else ' ' for c in s)


def clean_tex(text: str) -> str:
    """Hide literal snippets/comments, preserving offsets/line numbers."""
    text = VERBATIM.sub(lambda m: blank_except_newlines(m.group(0)), text)
    # TeX verb is delimited by the character immediately following command.
    text = re.sub(r'\\verb\*?([^\sA-Za-z])(?:[^\n]*?)\1',
                  lambda m: blank_except_newlines(m.group(0)), text)
    text = re.sub(r'\\lstinline(?:\[[^\]]*\])?([^\sA-Za-z])(?:[^\n]*?)\1',
                  lambda m: blank_except_newlines(m.group(0)), text)
    text = re.sub(r'\\mintinline(?:\[[^\]]*\])?\{[^}]*\}([^\sA-Za-z])(?:[^\n]*?)\1',
                  lambda m: blank_except_newlines(m.group(0)), text)
    # Strip unescaped comment tails, even when a literal \\% was written.
    # Count immediately preceding slashes: even => a comment starter.
    lines=[]
    for line in text.splitlines(keepends=True):
        hit=None
        for i, c in enumerate(line):
            if c != '%':
                continue
            back=0; j=i-1
            while j >= 0 and line[j] == '\\':
                back+=1; j-=1
            if back % 2 == 0:
                hit=i; break
        if hit is None:
            lines.append(line)
        else:
            lines.append(line[:hit]+blank_except_newlines(line[hit:]))
    return ''.join(lines)


def line_col(text: str, off: int) -> tuple[int,int]:
    line = text.count('\n',0,off)+1
    last = text.rfind('\n',0,off)
    return line, off-last


def find_issues(text: str, file: Path) -> list[dict]:
    issues=[]
    for category, pattern in PATTERNS:
        for m in pattern.finditer(text):
            bad = False
            if category == 'BOX_MACRO':
                bad = True
            elif category == 'BOX_ENV':
                env = m.group(1).strip(); low = env.lower()
                bad = env in BAD_ENVIRONMENTS or low.endswith('box') or low.endswith('box*') or low.endswith('framed')
            elif category == 'BOX_PACKAGE':
                names={v.strip().lower() for v in m.group(1).split(',')}
                bad=bool(names & BAD_PACKAGES)
            elif category == 'BOX_EQUATION_OPTION':
                bad=bool(re.search(r'(?<![A-Za-z])(?:box|frame)\s*=',m.group(1)))
            elif category == 'BOX_ENV_DEFINITION':
                env=m.group(1).strip().lower(); bad=env.endswith('box') or env.endswith('framed')
            if bad:
                line,col=line_col(text,m.start())
                issues.append({'file':str(file),'line':line,'column':col,'code':category,
                               'token':m.group(0).split('\n',1)[0][:90]})
    return issues


def audit(paths: list[Path], follow_inputs: bool=True) -> dict:
    seen=set(); issues=[]; missing=[]; inspected=[]

    def inspect(file: Path, anchor: Path):
        file=file.resolve()
        if not file.is_relative_to(anchor):
            missing.append('OUT_OF_SCOPE_LOCAL_INPUT: '+str(file)); return
        if file in seen: return
        seen.add(file)
        if not file.is_file():
            missing.append(str(file));return
        inspected.append(str(file))
        clean=clean_tex(file.read_text(encoding='utf-8',errors='replace'))
        issues.extend(find_issues(clean,file))
        if follow_inputs:
            for m in INCLUDES.finditer(clean):
                stem=m.group(1).strip()
                if not stem or '\\' in stem or '#' in stem: continue
                # Only local dependencies. Don't fetch files or traverse other absolute locations.
                nested=(file.parent/stem)
                if not nested.suffix: nested=nested.with_suffix('.tex')
                inspect(nested, anchor)
    for p in paths: inspect(p, p.resolve().parent)
    issues.sort(key=lambda v:(v['file'],v['line'],v['column'],v['code']))
    return {'status':'FAIL' if issues or missing else 'STATIC_PASS',
            'files_inspected':inspected,'violations':issues,'missing_local_inputs':missing,
            'visual_review_required':True}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('tex', nargs='+', type=Path)
    p.add_argument('--no-follow-inputs',action='store_true')
    p.add_argument('--json',action='store_true')
    args=p.parse_args()
    result=audit(args.tex,not args.no_follow_inputs)
    if args.json: print(json.dumps(result,indent=2,ensure_ascii=False))
    else:
        print('NO_BOX_'+result['status'])
        for issue in result['violations']:
            print('{file}:{line}:{column}: {code}: {token}'.format(**issue))
        for miss in result['missing_local_inputs']:
            print('MISSING_LOCAL_INPUT: '+miss)
        print('Checked '+str(len(result['files_inspected']))+' file(s). Static PASS still requires PDF/macro visual review.')
    return 1 if result['status']=='FAIL' else 0


if __name__=='__main__':
    raise SystemExit(main())
