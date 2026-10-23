"""Read-only audit of episode-linked MicroFreak preset research.

This checks recorded evidence and topic coverage, not the truth of parameter decoding.
Reports belong outside the knowledge graph. Historical audits are advisory.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import unicodedata

AREAS = {
    'provenance': r'(?:saved )?export(?: and provenance)?|provenance|saved sound|digital twin',
    'oscillator': r'oscillator(?: and controls)?|digital oscillator',
    'filter': r'filter',
    'envelopes': r'envelopes?|cycling envelope',
    'lfo': r'lfo|low.frequency oscillator',
    'matrix': r'modulation matrix|matrix|modulation routes',
    'performance': r'performance(?: and session context)?|session context|session edits|playing the preset',
}
WIKILINK = re.compile(r'\[\[([^\]\n]+)\]\]')
BULLET = re.compile(r'^(\s*)-\s+(.*)$')
FENCE = re.compile(r'^(`{3,}|~{3,})(.*)$')
PLACEHOLDER = re.compile(r'^(?:todo\b|tbd\b|pending\b|unknown[.! ]*$|unverified[.! ]*$|not (?:yet )?(?:researched|documented|verified)[.! ]*$|see (?:the )?(?:manual|reference)[.! ]*$)', re.I)
LIMIT = re.compile(r'\b(?:unknown|unverified|uncertain|not verified|unsupported|not captured|cannot establish)\b', re.I)


def key(value: str) -> str:
    return unicodedata.normalize('NFC', value.strip()).casefold()


def visible_lines(text: str):
    """Ignore fenced examples; opening fences may be wrapped in a Logseq bullet."""
    fence = None
    for line in text.splitlines():
        stripped = line.lstrip()
        candidate = re.sub(r'^-\s+', '', stripped)
        if fence:
            closing = FENCE.match(stripped)
            if closing and closing[1][0] == fence[0] and len(closing[1]) >= fence[1] and not closing[2].strip():
                fence = None
            continue
        opening = FENCE.match(candidate)
        if opening:
            fence = (opening[1][0], len(opening[1]))
            continue
        yield line


def without_inline_code(text: str) -> str:
    return re.sub(r'(`+)(.*?)\1', '', text)


def properties(text: str) -> dict[str, str]:
    props = {}
    for line in visible_lines(text):
        if BULLET.match(line):
            break
        if '::' in line:
            name, value = line.split('::', 1)
            props[key(name)] = value.strip()
    return props


def sections(text: str) -> dict[str, list[str]]:
    result = {area: [] for area in AREAS}
    active = []
    for line in visible_lines(text):
        match = BULLET.match(line)
        if not match:
            continue
        indent = len(match[1].expandtabs(2))
        value = match[2]
        while active and active[-1][0] >= indent:
            active.pop()
        label = re.sub(r'^#+\s*', '', without_inline_code(value)).strip().rstrip(':')
        # Headings and short topic labels identify sections; prose remains evidence.
        area = next((name for name, pattern in AREAS.items()
                     if re.fullmatch(r'(?:' + pattern + r')(?:\s*[—–:-].*)?', label, re.I)), None)
        if area:
            active.append((indent, area))
            tail = re.match(r'^(?:#+\s*)?(?:' + AREAS[area] + r')\s*[—–:-]\s*(.+)$', value, re.I)
            if tail:
                result[area].append(tail[1])
        elif active and not re.match(r'^[\w-]+::', value):
            result[active[-1][1]].append(value)
    return result


def substantive(lines: list[str]) -> list[str]:
    result = []
    for line in lines:
        plain = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', line)
        plain = WIKILINK.sub('', plain)
        plain = re.sub(r'https?://\S+', '', plain).strip(' -*#`:.')
        if plain and not PLACEHOLDER.match(plain):
            result.append(plain)
    return result


def assess(text: str) -> dict:
    groups = sections(text)
    coverage = {}
    for area, lines in groups.items():
        meaningful = substantive(lines)
        coverage[area] = ('documented-with-limits' if any(LIMIT.search(line) for line in meaningful)
                          else 'documented') if meaningful else ('unresearched' if lines else 'missing')
    props = properties(text)
    lines = list(visible_lines(text))
    body_start = next((index for index, line in enumerate(lines) if BULLET.match(line)), len(lines))
    prose = '\n'.join(lines[body_start:])
    evidence = {
        'export_reference_recorded': bool(props.get('preset-synth-file')) or bool(re.search(r'\.(?:mfprojz|mfpz|mbp|bin)\b', '\n'.join(groups['provenance']), re.I)),
        'digest_recorded': bool(re.fullmatch(r'[a-fA-F0-9]{64}', props.get('preset-synth-file-sha256', ''))),
        'sources_cited': bool(re.search(r'\[[^\]\n]+\]\(https?://[^)\s]+\)', prose)) or any('/UG/' in link for link in WIKILINK.findall(prose)),
    }
    complete = all(state.startswith('documented') for state in coverage.values()) and all(evidence.values())
    status = 'detailed' if complete else ('partial' if any(state.startswith('documented') for state in coverage.values()) else 'stub')
    return {'status': status, 'coverage': coverage, 'evidence': evidence,
            'assessment': 'Recorded coverage and evidence; parameter interpretations still require review.'}


def inventory(garden: Path):
    pages, names = {}, {}
    if not (garden / 'pages').is_dir():
        raise ValueError('Source garden pages directory is missing: ' + str(garden))
    for path in sorted((garden / 'pages').glob('*.md')):
        text = path.read_text()
        props = properties(text)
        title = props.get('title', path.stem.replace('___', '/'))
        pages[title] = (path, text)
        aliases = WIKILINK.findall(props.get('alias', '')) or props.get('alias', '').split(',')
        for name in [title, *aliases]:
            if name.strip():
                names.setdefault(key(name), set()).add(title)
    return pages, names


def audit(garden: Path, episode: str | None = None) -> list[dict]:
    pages, names = inventory(garden)
    if episode:
        matches = names.get(key(episode), set())
        if len(matches) != 1:
            raise ValueError('Episode must resolve to exactly one stored source page: ' + episode)
        selected = sorted(matches)
    else:
        selected = sorted(title for title in pages if re.fullmatch(r'GitP/A/Session/\d{2}/\d{2}/[^/]+', title, re.I))
    reports = []
    for title in selected:
        refs = WIKILINK.findall(without_inline_code('\n'.join(visible_lines(pages[title][1]))))
        found = {}
        for ref in refs:
            matches = names.get(key(ref), set())
            presets = [name for name in matches if key(name).startswith('microfreak/preset/')]
            if key(ref) == 'microfreak/preset/initialized':
                found[ref] = {'preset': ref, 'status': 'initialized', 'note': 'An initialized sound is not an identified saved preset. Describe it plainly; do not invent export settings.'}
            elif len(presets) == 1 and len(matches) == 1:
                name = presets[0]
                found[name] = {'preset': name, **assess(pages[name][1])}
            elif presets or key(ref).startswith('microfreak/preset/'):
                found[ref] = {'preset': ref, 'status': 'ambiguous' if len(matches) > 1 else 'missing'}
        reports.append({'episode': title, 'presets': list(found.values())})
    return reports


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    scope = parser.add_mutually_exclusive_group(required=True)
    scope.add_argument('--episode', help='Exact source episode title or unique alias')
    scope.add_argument('--all', action='store_true', help='Report historical source sessions without blocking publication')
    parser.add_argument('--garden', type=Path, default=Path(__file__).resolve().parents[4])
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--check', action='store_true', help='Fail on gaps for the selected episode only')
    args = parser.parse_args(argv)
    if args.check and not args.episode:
        parser.error('--check requires --episode; historical --all audits are advisory')
    try:
        reports = audit(args.garden, args.episode)
    except (ValueError, OSError) as error:
        parser.error(str(error))
    if args.json:
        print(json.dumps(reports, ensure_ascii=False, indent=2))
    else:
        for report in reports:
            print(report['episode'])
            for item in report['presets']:
                gaps = [name for name, state in item.get('coverage', {}).items() if not state.startswith('documented')]
                gaps += [name for name, present in item.get('evidence', {}).items() if not present]
                print('  ' + item['preset'] + ': ' + item['status'] + ('; needs ' + ', '.join(gaps) if gaps else ''))
                if item.get('note'):
                    print('    ' + item['note'])
            if not report['presets']:
                print('  No saved MicroFreak preset references found.')
        print('Checks recorded evidence and coverage, not decoding accuracy. Keep raw reports outside the graph.')
    gaps = any(item['status'] not in {'detailed', 'initialized'} for report in reports for item in report['presets'])
    return int(args.check and gaps)

if __name__ == '__main__':
    raise SystemExit(main())
