#!/usr/bin/env python3
"""Read-only lexical citation inventory. Does not execute TeX or verify sources."""
import argparse
import json
from pathlib import Path
import re


CITES = set('cite citep citet citealp citealt citeauthor citeyear citeyearpar '
            'citetalias citepalias parencite textcite autocite footcite smartcite '
            'supercite fullcite footfullcite notecite nocite'.split())
MULTI = set('cites parencites textcites autocites footcites smartcites'.split())
CONFIG = {'citestyle', 'setcitestyle', 'defcitealias'}
COMMAND = re.compile(r'\\([A-Za-z]+)\*?')


def blank(s):
    return ''.join('\n' if c == '\n' else ' ' for c in s)


def mask_tex(s):
    """Preserve offsets and line numbers while masking non-prose regions."""
    # Raw environments are masked before comments: percent is literal in them.
    pattern = r'\\begin\{(verbatim\*?|Verbatim|lstlisting|minted|comment)\}.*?\\end\{\1\}'
    s = re.sub(pattern, lambda m: blank(m.group()), s, flags=re.S)
    s = re.sub(r'\\verb\*?([^\sA-Za-z]).*?\1', lambda m: blank(m.group()), s)
    chars = list(s)
    for i, c in enumerate(s):
        if c != '%':
            continue
        j = i - 1
        while j >= 0 and s[j] == '\\':
            j -= 1
        if (i - j - 1) % 2:
            continue
        end = s.find('\n', i)
        end = len(s) if end < 0 else end
        chars[i:end] = ' ' * (end - i)
    return ''.join(chars)


def space(s, i):
    while i < len(s) and s[i].isspace():
        i += 1
    return i


def group(s, i, opener='{'):
    i = space(s, i)
    if i >= len(s) or s[i] != opener:
        raise ValueError('expected ' + opener)
    closer = {'{': '}', '[': ']', '(': ')'}[opener]
    start = i + 1
    depth, braces, quoted = 1, 0, False
    i += 1
    while i < len(s):
        c = s[i]
        if c == '\\':
            i += 2
            continue
        if opener == '{':
            if c == '{':
                depth += 1
            elif c == '}':
                depth -= 1
        else:
            if opener == '(' and c == '"' and braces == 0:
                quoted = not quoted
            if c == '{':
                braces += 1
            elif c == '}':
                braces -= 1
            elif braces == 0 and not quoted:
                if c == opener:
                    depth += 1
                elif c == closer:
                    depth -= 1
        if depth == 0:
            return s[start:i], i + 1
        i += 1
    raise ValueError('unclosed ' + opener)


def argument(s, i):
    notes = []
    i = space(s, i)
    while i < len(s) and s[i] == '[':
        value, i = group(s, i, '[')
        notes.append(value)
        i = space(s, i)
    value, i = group(s, i)
    return value, notes, i


def split_fields(s):
    """Split BibTeX fields without splitting braced/quoted commas."""
    depth, quoted, start, i = 0, False, 0, 0
    fields = []
    while i < len(s):
        c = s[i]
        if c == '\\':
            i += 2
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
        elif c == '"' and depth == 0:
            quoted = not quoted
        elif c == ',' and depth == 0 and not quoted:
            fields.append(s[start:i])
            start = i + 1
        i += 1
    fields.append(s[start:])
    return fields


def inventory(tex_paths, bib_paths):
    definitions, calls, declarations, coverage = {}, [], [], []
    supplied = {Path(p).resolve() for p in [*tex_paths, *bib_paths]}

    def issue(path, line, kind, detail):
        coverage.append(dict(file=str(path), line=line, kind=kind, detail=detail))

    def define(key, data):
        definitions.setdefault(key, []).append(data)

    for path in dict.fromkeys(Path(p).resolve() for p in tex_paths):
        raw = path.read_text(encoding='utf-8')
        s = mask_tex(raw)
        items = []
        for m in COMMAND.finditer(s):
            name = m.group(1).lower()
            line = s.count('\n', 0, m.start()) + 1
            if name not in CITES | MULTI | {'bibitem', 'input', 'include', 'bibliography', 'addbibresource'}:
                if ('cite' in name and name not in CONFIG) or name == 'entry':
                    issue(path, line, 'unsupported_command', m.group())
                continue
            try:
                value, notes, end = argument(s, m.end())
            except ValueError as exc:
                issue(path, line, 'unparsed_argument', m.group() + ': ' + str(exc))
                continue
            if name == 'bibitem':
                items.append((m.start(), end, value.strip(), notes, line))
            elif name in {'input', 'include', 'bibliography', 'addbibresource'}:
                extension = '.bib' if name in {'bibliography', 'addbibresource'} else '.tex'
                for target in value.split(','):
                    declarations.append((path, line, target.strip(), extension))
            else:
                while True:
                    keys = [k.strip() for k in value.split(',') if k.strip()]
                    if not keys or any('\\' in k or '#' in k for k in keys):
                        issue(path, line, 'dynamic_or_empty_key', value)
                    else:
                        calls.append(dict(file=str(path), line=line, command=name,
                                          keys=keys, notes=notes,
                                          context=s[max(0, m.start()-180):min(len(s), end+180)]))
                    if name not in MULTI:
                        break
                    nextpos = space(s, end)
                    if nextpos >= len(s) or s[nextpos] not in '[{':
                        break
                    try:
                        value, notes, end = argument(s, nextpos)
                    except ValueError as exc:
                        issue(path, line, 'unparsed_multicite', str(exc))
                        break
        for index, (start, end, key, notes, line) in enumerate(items):
            stop = items[index+1][0] if index+1 < len(items) else len(s)
            closing = s.find(r'\end{thebibliography}', end, stop)
            if closing >= 0:
                stop = closing
            define(key, dict(file=str(path), line=line, format='bibitem',
                             label_notes=notes, raw=s[end:stop].strip()))

    for path in dict.fromkeys(Path(p).resolve() for p in bib_paths):
        raw = path.read_text(encoding='utf-8')
        # Preserve URL percent escapes; only whole-line BibTeX comments are masked.
        s = re.sub(r'(?m)^\s*%[^\n]*', lambda m: blank(m.group()), raw)
        cursor = 0
        while True:
            m = re.search(r'@([A-Za-z]+)\s*([({])', s[cursor:])
            if not m:
                break
            start = cursor + m.start()
            opening = cursor + m.end() - 1
            line = s.count('\n', 0, start) + 1
            try:
                body, cursor = group(s, opening, m.group(2))
            except ValueError as exc:
                issue(path, line, 'unparsed_bibtex_entry', str(exc))
                break
            kind = m.group(1).lower()
            if kind == 'comment':
                continue
            if kind in {'string', 'preamble'}:
                issue(path, line, 'unevaluated_bibtex_directive', kind)
                continue
            parts = split_fields(body)
            key = parts[0].strip()
            fields = {}
            for field in parts[1:]:
                if not field.strip():
                    continue
                if '=' not in field:
                    issue(path, line, 'unparsed_bibtex_field', field.strip())
                    continue
                name, value = field.split('=', 1)
                fields[name.strip().lower()] = value.strip()
            if not key:
                issue(path, line, 'empty_bibtex_key', body[:80])
                continue
            for name in ('crossref', 'xref', 'xdata', 'related', 'ids'):
                if name in fields:
                    issue(path, line, 'unevaluated_bibtex_relation', key + ': ' + name)
            define(key, dict(file=str(path), line=line, format='bibtex',
                             entry_type=kind, fields=fields, raw=s[start:cursor]))

    for path, line, target, extension in declarations:
        if not target or '\\' in target or '#' in target:
            issue(path, line, 'dynamic_file_reference', target)
            continue
        linked = path.parent / target
        if not linked.suffix:
            linked = linked.with_suffix(extension)
        if linked.resolve() not in supplied:
            issue(path, line, 'declared_file_not_scanned', str(linked.resolve()))

    cited = {k for c in calls if c['command'] != 'nocite' for k in c['keys']}
    nocited = {k for c in calls if c['command'] == 'nocite' for k in c['keys']}
    defined = set(definitions)
    unknown = sorted(cited - defined)
    unknown_nocite = sorted(nocited - defined - {'*'})
    duplicate = sorted(k for k, ds in definitions.items() if len(ds) > 1)
    references = []
    for key, ds in definitions.items():
        references.append(dict(key=key, definitions=ds,
                               citations=[c for c in calls if c['command'] != 'nocite' and key in c['keys']],
                               included_by_nocite=key in nocited or '*' in nocited,
                               review=dict(metadata='not_checked', locator='not_checked', claim_support='not_checked')))
    return dict(status='inventory_only', source_verification_performed=False,
                summary=dict(bibliography_keys=len(defined), cited_defined_keys=len(cited & defined),
                             citation_commands=len([c for c in calls if c['command'] != 'nocite'])),
                references=references, citation_calls=calls, undefined_keys=unknown,
                undefined_nocite_keys=unknown_nocite, duplicate_keys=duplicate,
                uncited_keys=sorted(defined-cited),
                included_without_citation=sorted((defined if '*' in nocited else defined & nocited)-cited),
                coverage_issues=coverage,
                mechanical_ok=not (unknown or unknown_nocite or duplicate or coverage),
                limitations=['Lexical inventory only; custom macros and conditional TeX are not evaluated.',
                             'Declared relative paths are resolved beside the source file; TeX search paths are not evaluated.',
                             'BibTeX field expressions are retained verbatim, not expanded or externally verified.'])


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--tex', action='append', default=[])
    ap.add_argument('--bib', action='append', default=[])
    ap.add_argument('--output', type=Path)
    ap.add_argument('--strict', action='store_true')
    args = ap.parse_args()
    if not args.tex and not args.bib:
        ap.error('at least one --tex or --bib is required')
    if args.output and args.output.resolve() in {Path(p).resolve() for p in args.tex + args.bib}:
        ap.error('--output must not overwrite an input source')
    result = inventory(args.tex, args.bib)
    data = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.output:
        args.output.write_text(data, encoding='utf-8')
        print(json.dumps(dict(result['summary'], mechanical_ok=result['mechanical_ok'],
                              source_verification_performed=False)))
    else:
        print(data, end='')
    return 1 if args.strict and not result['mechanical_ok'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
