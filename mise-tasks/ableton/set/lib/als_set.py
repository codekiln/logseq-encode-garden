#!/usr/bin/env python3
"""Plan or write the pages Logseq/Entity/Ableton/Set defines from a Live Set (.als) file."""
from __future__ import annotations
import argparse
import gzip
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

TRACK_TYPES = {'AudioTrack': 'audio', 'MidiTrack': 'midi', 'GroupTrack': 'group', 'ReturnTrack': 'return'}
ENTITY = {'set': 'Logseq/Entity/Ableton/Set', 'group': 'Logseq/Entity/Ableton/Track/Group',
          'track': 'Logseq/Entity/Ableton/Track/Track'}
MONITOR = {0: 'in', 1: 'auto', 2: 'off'}
# The Set file shows these settings in this order; the task writes them as properties of the H1 block.
# Any other line on a page is the author's and stays as written.
PROPERTY_ORDER = ['type', 'audio-from', 'audio-to', 'midi-from', 'midi-to', 'midi-channel', 'monitor', 'arm', 'devices']
UNSAFE_FILE_CHARS = '%?:*"<>|#\\'


class SetError(ValueError):
    pass


def read_set(path):
    try:
        data = gzip.decompress(Path(path).read_bytes())
    except (OSError, EOFError) as error:
        raise SetError(f'{path}: not a gzip-compressed Live Set ({error})') from error
    try:
        root = ET.fromstring(data)
    except ET.ParseError as error:
        raise SetError(f'{path}: Live Set XML does not parse ({error})') from error
    if root.tag != 'Ableton' or root.find('LiveSet/Tracks') is None:
        raise SetError(f'{path}: not an Ableton Live Set')
    return root


def value(element, path):
    found = element.find(path)
    return None if found is None else found.get('Value')


def number(text):
    return f'{float(text):g}'


def time_signature(code):
    """Live stores a signature as (numerator - 1) + 99 * log2(denominator)."""
    code = int(float(code))
    return f'{code % 99 + 1}/{2 ** (code // 99)}'


def routing(track, tag):
    return value(track, f'DeviceChain/{tag}/Target')


def midi_channel(track):
    target = routing(track, 'MidiInputRouting')
    if target is None:
        return None
    if target.endswith('/-1'):
        return 'all'
    match = re.search(r'\d+', value(track, 'DeviceChain/MidiInputRouting/LowerDisplayString') or '')
    return match[0] if match else None


def devices(track):
    chain = track.find('DeviceChain/DeviceChain/Devices')
    return [] if chain is None else [value(device, 'UserName') or device.tag for device in chain]


def track_properties(track, kind):
    """The settings Live's file shows for one track, in the order the entity page lists them."""
    props = {'type': kind}
    if kind == 'audio':
        props['audio-from'] = routing(track, 'AudioInputRouting')
        props['audio-to'] = routing(track, 'AudioOutputRouting')
    elif kind == 'midi':
        props['midi-from'] = routing(track, 'MidiInputRouting')
        props['midi-to'] = routing(track, 'MidiOutputRouting')
        props['midi-channel'] = midi_channel(track)
        # A MIDI track with no MIDI destination sounds through its own devices.
        if props['midi-to'] == 'MidiOut/None':
            props['audio-to'] = routing(track, 'AudioOutputRouting')
    else:
        props['audio-to'] = routing(track, 'AudioOutputRouting')
    if kind in ('audio', 'midi'):
        monitor = value(track, 'DeviceChain/MainSequencer/MonitoringEnum')
        props['monitor'] = MONITOR.get(int(monitor)) if monitor is not None else None
        armed = value(track, 'DeviceChain/MainSequencer/Recorder/IsArmed')
        props['arm'] = armed if armed in ('true', 'false') else None
    chain = devices(track)
    props['devices'] = ', '.join(chain) if chain else None
    return {key: props[key] for key in PROPERTY_ORDER if props.get(key) is not None}


def page_part(name):
    part = name.replace('/', '-').strip()
    if not part or part in ('.', '..') or '[[' in part or ']]' in part or any(ord(c) < 32 for c in part):
        raise SetError(f'Track name cannot be a page name: {name!r}')
    return part


def plan_set(root, performance, source_name):
    """Return the Set's page title, its properties, and a list of track entries in Live's order."""
    live = root.find('LiveSet')
    creator = root.get('Creator', '')
    version = re.search(r'\d+(\.\d+)*', creator)
    props = {}
    if version:
        props['live-version'] = version[0]
    tempo = value(live, 'MasterTrack/DeviceChain/Mixer/Tempo/Manual')
    if tempo is not None:
        props['tempo'] = number(tempo)
    signature = value(live, 'MasterTrack/DeviceChain/Mixer/TimeSignature/Manual')
    if signature is not None:
        props['time-signature'] = time_signature(signature)
    props['source'] = source_name
    entries, by_id = [], {}
    for element in live.find('Tracks'):
        kind = TRACK_TYPES.get(element.tag)
        if kind is None:
            continue
        name = value(element, 'Name/EffectiveName')
        if not name:
            raise SetError(f'{element.tag} {element.get("Id")} has no name')
        entry = {'id': element.get('Id'), 'name': name, 'kind': kind, 'props': track_properties(element, kind),
                 'parent': value(element, 'TrackGroupId'), 'children': []}
        entries.append(entry)
        by_id[entry['id']] = entry
    prefix = f'{performance}/Set/Track'
    top = []
    for entry in entries:
        parent = by_id.get(entry['parent']) if entry['parent'] not in (None, '-1') else None
        if entry['parent'] not in (None, '-1') and parent is None:
            raise SetError(f'Track {entry["name"]!r} is in group {entry["parent"]}, which is not in the Set')
        entry['parent_entry'] = parent
        (parent['children'] if parent else top).append(entry)
    seen = {}
    for entry in entries:
        chain, up = [], entry
        while up:
            chain.append(page_part(up['name']))
            up = up['parent_entry']
        entry['page'] = '/'.join([prefix, *reversed(chain)])
        if entry['page'].lower() in seen:
            raise SetError(f'Two tracks would share the page {entry["page"]}: rename one in Live.')
        seen[entry['page'].lower()] = entry
    return props, top, entries


def file_name(page):
    return ''.join(f'%{ord(c):02X}' if c in UNSAFE_FILE_CHARS else c for c in page).replace('/', '___') + '.md'


def embeds(children):
    return [f'\t- {{{{embed [[{child["page"]}]]}}}}' for child in children]


def new_page(entity, title, props, children):
    lines = [f'logseq-entity:: [[{entity}]]', '', f'- # {title}']
    lines += [f'  {key}:: {val}' for key, val in props.items()]
    lines += embeds(children)
    return '\n'.join(lines) + '\n'


PROPERTY = re.compile(r'^  ([a-z][a-z0-9-]*):: ?(.*)$')
EMBED = re.compile(r'^\t- \{\{embed \[\[(.+)\]\]\}\}$')


def update_page(text, props, children, owned_prefix):
    """Set the owned properties and embeds of an existing page, leaving other lines as written."""
    lines = text.rstrip('\n').split('\n')
    heading = next((i for i, line in enumerate(lines) if line.startswith('- # ')), None)
    if heading is None:
        raise SetError('existing page has no H1 block to update')
    end = heading + 1
    while end < len(lines) and PROPERTY.match(lines[end]):
        end += 1
    for key, val in props.items():
        wanted = f'  {key}:: {val}'
        existing = next((i for i in range(heading + 1, end) if PROPERTY.match(lines[i]).group(1) == key), None)
        if existing is None:
            lines.insert(end, wanted)
            end += 1
        else:
            lines[existing] = wanted
    owned = [i for i, line in enumerate(lines) if (m := EMBED.match(line)) and m[1].startswith(owned_prefix)]
    wanted = embeds(children)
    if [lines[i] for i in owned] != wanted:
        at = owned[0] if owned else len(lines)
        for i in reversed(owned):
            del lines[i]
        lines[at:at] = wanted
    return '\n'.join(lines) + '\n'


def plan_pages(root, performance, source_name, garden):
    """Map each page file to (action, text); action is create, update or unchanged."""
    props, top, entries = plan_set(root, performance, source_name)
    title = Path(source_name).stem
    pages = {}
    set_page = f'{performance}/Set'
    pages[set_page] = ('set', title, props, top, f'{performance}/Set/Track/')
    for entry in entries:
        pages[entry['page']] = ('group' if entry['kind'] == 'group' else 'track', entry['name'], entry['props'],
                                entry['children'], entry['page'] + '/')
    result = {}
    for page, (kind, title, page_props, children, owned_prefix) in pages.items():
        path = Path(garden) / 'pages' / file_name(page)
        if path.exists():
            current = path.read_text(encoding='utf-8')
            text = update_page(current, page_props, children, owned_prefix)
            result[path] = ('unchanged' if text == current else 'update', text, page)
        else:
            result[path] = ('create', new_page(ENTITY[kind], title, page_props, children), page)
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--als', type=Path, required=True, help='the Live Set file')
    parser.add_argument('--performance', required=True, help="the performance's page name, such as GitP/A/Session/26/11/01-Sun")
    parser.add_argument('--garden', type=Path, default=Path(__file__).resolve().parents[4], help='the garden to write to')
    parser.add_argument('--apply', action='store_true', help='write the pages; the default prints the plan')
    args = parser.parse_args(argv)
    try:
        if not args.performance or args.performance.strip('/') != args.performance or '//' in args.performance:
            raise SetError(f'Not a page name: {args.performance!r}')
        plan = plan_pages(read_set(args.als), args.performance, args.als.name, args.garden)
    except SetError as error:
        print(f'error: {error}', file=sys.stderr)
        return 1
    for path, (action, text, page) in plan.items():
        print(f'{action:9} {page}')
        if args.apply and action != 'unchanged':
            path.write_text(text, encoding='utf-8')
    if not args.apply:
        print('Preview only; add --apply to write these pages.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
