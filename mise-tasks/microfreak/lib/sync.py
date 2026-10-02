#!/usr/bin/env python3
"""Read saved MicroFreak preset headers and reconcile Logseq metadata.

Wire layout and category mapping:
https://github.com/dagargo/elektroid/blob/6f3d50e2588f0236afb3510e1c55bbb292446aa2/src/connectors/microfreak.c
Only the preset-header request (0x19, mode 0) is sent to the instrument.
"""
import argparse
import datetime as dt
import json
import re
import sys
import time
from pathlib import Path

PREFIX = [0xF0, 0, 0x20, 0x6B, 7, 1]
# IDs match elektroid's microfreak_get_category_name at the source URL above.
CATEGORIES = ['Bass', 'Brass', 'Keys', 'Lead', 'Organ', 'Pad', 'Percussion',
              'Sequence', 'SFX', 'Strings', 'Template', 'Vocoder']
ENTITY = '[[Logseq/Entity/Preset/Synth/Microfreak]]'
MICROFREAK_PROPERTY = 'preset-synth-microfreak-'
SHARED_PROPERTY = 'preset-synth-'
CATEGORY_PAGE = 'Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category'
ORIGIN_PAGE = 'Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin'
LEGACY_PROPERTIES = {
    'preset-number': MICROFREAK_PROPERTY + 'number',
    'preset-name': MICROFREAK_PROPERTY + 'name',
    'preset-category': MICROFREAK_PROPERTY + 'category',
    'preset-initialized': MICROFREAK_PROPERTY + 'initialized',
    'preset-on-device': MICROFREAK_PROPERTY + 'on-device',
    'preset-origin': SHARED_PROPERTY + 'origin',
    'preset-file': SHARED_PROPERTY + 'file',
    'preset-file-sha256': SHARED_PROPERTY + 'file-sha256',
    'preset-oscillator-type': MICROFREAK_PROPERTY + 'oscillator-type',
}
ALPHABET = re.compile(r'[ A-Za-z0-9._-]{1,14}\Z')


def decode_header(message, slot, sequence):
    if (len(message) != 45 or message[:6] != PREFIX or message[6] != sequence
            or message[7:9] != [35, 0x52] or message[-1] != 0xF7):
        raise ValueError('Unexpected preset-header response')
    header = message[9:-1]
    if header[0] * 128 + header[1] != slot - 1:
        raise ValueError('Response belongs to a different preset slot')
    name = bytes(header[12:26]).split(b'\0', 1)[0].decode('ascii')
    if not ALPHABET.fullmatch(name) or not name.strip():
        raise ValueError(f'Unsupported preset name in slot {slot}: {name!r}')
    if header[10] >= len(CATEGORIES):
        raise ValueError(f'Unknown preset category in slot {slot}')
    return dict(number=slot, name=name.strip(), category=CATEGORIES[header[10]],
                initialized=bool(header[3] & 8))


def read_device(port=None):
    try:
        import rtmidi
    except ImportError as exc:
        raise RuntimeError('Install python-rtmidi==1.5.8, or run the mise task.') from exc
    midi_in, midi_out = rtmidi.MidiIn(), rtmidi.MidiOut()
    def select(ports):
        choices = [(i, p) for i, p in enumerate(ports)
                   if (p == port if port else 'microfreak' in p.lower())]
        if len(choices) != 1:
            raise RuntimeError(f'Choose a unique MicroFreak MIDI port with --port; available: {ports}')
        return choices[0]
    input_id, input_name = select(midi_in.get_ports())
    output_id, _ = select(midi_out.get_ports())
    midi_in.ignore_types(sysex=False)
    midi_in.open_port(input_id)
    midi_out.open_port(output_id)
    presets = []
    try:
        for slot in range(1, 513):
            # Clear old traffic before issuing a new, sequenced read request.
            while midi_in.get_message():
                pass
            seq = (slot - 1) % 128
            midi_out.send_message(PREFIX + [seq, 3, 0x19, (slot - 1) // 128,
                                            (slot - 1) % 128, 0, 0xF7])
            deadline = time.monotonic() + 3
            while True:
                received = midi_in.get_message()
                if received:
                    message = received[0]
                    if message[:6] == PREFIX and len(message) > 8 and message[6] == seq:
                        presets.append(decode_header(message, slot, seq))
                        break
                if time.monotonic() > deadline:
                    raise RuntimeError(f'Timed out reading slot {slot}; close MIDI Control Center and retry.')
                time.sleep(.002)
            time.sleep(.005)
    finally:
        midi_in.close_port()
        midi_out.close_port()
    return dict(schema=1, device=input_name, captured_at=dt.datetime.now(dt.timezone.utc).isoformat(),
                presets=presets)


def validate(data):
    if data.get('schema') != 1 or not isinstance(data.get('presets'), list):
        raise ValueError('Unsupported inventory format')
    slots = []
    for p in data['presets']:
        if (type(p.get('number')) is not int or not isinstance(p.get('name'), str)
                or not ALPHABET.fullmatch(p['name']) or p['name'] != p['name'].strip()
                or not p['name'] or p.get('category') not in CATEGORIES
                or type(p.get('initialized')) is not bool):
            raise ValueError('Invalid inventory preset')
        slots.append(p['number'])
    if sorted(slots) != list(range(1, 513)):
        raise ValueError('Inventory must contain every slot exactly once; graph has not been modified')
    return data


def properties(text):
    props = {}
    for line in text.splitlines():
        match = re.fullmatch(r'([a-z][a-z0-9-]*):: (.*)', line)
        if not match:
            break
        if match[1] in props:
            raise ValueError(f'Duplicate property: {match[1]}')
        props[match[1]] = match[2]
    return props


def migrate_properties(text):
    """Rename owned metadata without touching tags or the handwritten body."""
    props = properties(text)
    for old, new in LEGACY_PROPERTIES.items():
        if old not in props:
            continue
        if new in props and props[new] != props[old]:
            raise ValueError(f'Conflicting preset properties: {old}, {new}')
        if new in props:
            text = update(text, {old: None})
        else:
            text = re.sub(rf'^{re.escape(old)}:: ', new + ':: ', text, count=1, flags=re.M)
    return text


def category_link(category):
    return f'[[{CATEGORY_PAGE}/{category}]]'


def origin_link(origin):
    if origin.startswith('[[') and origin.endswith(']]'):
        return origin
    if origin.casefold() not in {'unknown', 'factory', 'custom'}:
        raise ValueError(f'Unsupported preset origin: {origin}')
    return f'[[{ORIGIN_PAGE}/{origin.title()}]]'


def strip_stock_body(text, name, number):
    """Remove only script-generated repetition, retaining all user-authored blocks."""
    stock = f'- # {name}\n\t- Saved [[Microfreak]] preset in slot {number:03d}.\n'
    legacy = f'- # {name}\n\t- Saved [[Microfreak]] preset in slot {number}.\n'
    if stock in text:
        return text.replace(stock, '- # Notes\n', 1)
    if legacy in text:
        return text.replace(legacy, '- # Notes\n', 1)
    return text


def update(text, values):
    lines = text.splitlines()
    boundary = 0
    while boundary < len(lines) and re.fullmatch(r'[a-z][a-z0-9-]*:: .*', lines[boundary]):
        boundary += 1
    for key, value in values.items():
        indices = [i for i in range(boundary) if lines[i].startswith(key + ':: ')]
        if value is None:
            if indices:
                lines.pop(indices[0])
                boundary -= 1
        elif indices:
            lines[indices[0]] = f'{key}:: {value}'
        else:
            lines.insert(boundary, f'{key}:: {value}')
            boundary += 1
    return '\n'.join(lines) + '\n'


def plan(garden, inventory):
    validate(inventory)
    pages = garden / 'pages'
    if not pages.is_dir():
        raise ValueError('Garden must contain a pages directory')
    original = {path: path.read_text() for folder in ('pages', 'journals')
                for path in (garden / folder).glob('*.md')}
    desired = dict(original)
    current, renames = {}, {}
    for path in pages.glob('Microfreak___Preset___*.md'):
        text = original[path]
        props = properties(text)
        if props.get('logseq-entity') != ENTITY:
            continue
        number = props.get(MICROFREAK_PROPERTY + 'number', props.get('preset-number', ''))
        if not number.isdigit() or not 1 <= int(number) <= 512:
            raise ValueError(f'Invalid preset number: {path}')
        name = props.get(MICROFREAK_PROPERTY + 'name', props.get('preset-name'))
        key = (int(number), name)
        if key in current:
            raise ValueError(f'Duplicate preset identity: {key}')
        # Pad the original title's slot, preserving its historical identity.
        match = re.fullmatch(r'Microfreak___Preset___([0-9]+) (.+)', path.stem)
        if not match or not 1 <= int(match[1]) <= 512:
            raise ValueError(f'Unsupported preset page title: {path}')
        target = path.with_name(f'Microfreak___Preset___{int(match[1]):03d} {match[2]}.md')
        if target != path:
            if target in original or target in desired and target not in original:
                raise ValueError(f'Preset rename destination already exists: {target}')
            renames[path.stem.replace('___', '/')] = target.stem.replace('___', '/')
            del desired[path]
        text = migrate_properties(text)
        text = strip_stock_body(text, name, int(number))
        migrated = properties(text)
        values = {MICROFREAK_PROPERTY + 'number': f'{int(number):03d}'}
        if SHARED_PROPERTY + 'origin' in migrated:
            values[SHARED_PROPERTY + 'origin'] = origin_link(migrated[SHARED_PROPERTY + 'origin'])
        if MICROFREAK_PROPERTY + 'category' in migrated:
            category = migrated[MICROFREAK_PROPERTY + 'category']
            if category in CATEGORIES:
                values[MICROFREAK_PROPERTY + 'category'] = category_link(category)
        desired[target] = update(text, values)
        current[key] = target
    active = {}
    for p in sorted(inventory['presets'], key=lambda p: p['number']):
        if p['initialized']:
            continue
        key = (p['number'], p['name'])
        title = f"Microfreak/Preset/{p['number']:03d} {p['name']}"
        path = current.get(key, pages / (title.replace('/', '___') + '.md'))
        if key not in current and path in desired:
            raise ValueError(f'Unmanaged page already exists: {path}; reconcile its metadata before applying')
        # An unmanaged legacy page must not be silently duplicated either.
        legacy = pages / f"Microfreak___Preset___{p['number']} {p['name']}.md"
        if key not in current and legacy in original:
            raise ValueError(f'Unmanaged page already exists: {legacy}; reconcile its metadata before applying')
        old = desired.get(path)
        values = {'logseq-entity': ENTITY,
                  MICROFREAK_PROPERTY + 'number': f"{p['number']:03d}",
                  MICROFREAK_PROPERTY + 'name': p['name'],
                  MICROFREAK_PROPERTY + 'category': category_link(p['category']),
                  MICROFREAK_PROPERTY + 'initialized': 'false',
                  MICROFREAK_PROPERTY + 'on-device': 'true'}
        if old is None:
            values[SHARED_PROPERTY + 'origin'] = origin_link('unknown')
        desired[path] = update(old if old is not None else '- # Notes\n', values)
        active[key] = path
    sequence = list(active.values())
    for i, path in enumerate(sequence):
        desired[path] = update(desired[path], {
            'prev': f"[[{sequence[i - 1].stem.replace('___', '/')}]]" if i else None,
            'next': f"[[{sequence[i + 1].stem.replace('___', '/')}]]" if i + 1 < len(sequence) else None})
    for key, path in current.items():
        if key not in active:
            desired[path] = update(desired[path], {MICROFREAK_PROPERTY + 'on-device': 'false',
                                                   'prev': None, 'next': None})
    if renames:
        link = re.compile(r'\[\[([^\[\]]+)\]\]')
        for path, text in desired.items():
            lines = []
            for line in text.splitlines(keepends=True):
                replaced = link.sub(lambda m: '[[' + renames.get(m[1], m[1]) + ']]', line)
                if line.startswith('tags::') and replaced != line:
                    raise ValueError(f'Protected tags reference a renamed preset: {path}')
                lines.append(replaced)
            desired[path] = ''.join(lines)
    return [(path, original.get(path), desired.get(path))
            for path in sorted(original.keys() | desired.keys())
            if original.get(path) != desired.get(path)]


def journal_text(old, changes):
    # The namespace hub keeps repeated bulk inventories out of the curated journal.
    if not changes:
        return old
    lines = old.splitlines()
    entries = {'Filed': [], 'Updated': []}
    section = None
    for i, line in enumerate(lines):
        if line and not line.startswith(('\t', ' ')):
            section = next((name for name in entries
                            if line == f'- # [[{name}]]'), None)
        elif section and line.strip() == '- [[Microfreak/Preset]]':
            entries[section].append(i)
    # A page filed today stays Filed even after subsequent metadata updates.
    existing = entries['Filed'] or entries['Updated']
    if existing:
        keep = existing[0]
        duplicates = set(entries['Filed'] + entries['Updated']) - {keep}
        if not duplicates:
            return old
        return '\n'.join(line for i, line in enumerate(lines) if i not in duplicates) + '\n'
    heading = '- # [[Updated]]'
    if heading not in lines:
        lines.append(heading)
    start = lines.index(heading) + 1
    end = start
    while end < len(lines) and (lines[end].startswith(('\t', ' ')) or not lines[end]):
        end += 1
    labels = [(i, line[3:]) for i, line in enumerate(lines[start:end], start)
              if line.startswith('\t- ') and not line[3:].startswith('[[')]
    if labels:
        matching = next((i for i, label in labels if label.casefold() == 'presets'), None)
        if matching is not None:
            position = matching + 1
            while position < end and (lines[position].startswith('\t\t')
                                      or lines[position].startswith('\t  ')):
                position += 1
            lines.insert(position, '\t\t- [[Microfreak/Preset]]')
        else:
            position = next((i for i, label in labels if label.casefold() > 'presets'), end)
            lines[position:position] = ['\t- presets', '\t\t- [[Microfreak/Preset]]']
    else:
        lines.insert(end, '\t- [[Microfreak/Preset]]')
    return '\n'.join(lines) + '\n'


def apply(garden, changes):
    # Preflight all pages before writing any page. Git supplies the review/recovery boundary.
    for path, old, _ in changes:
        if (path.read_text() if path.exists() else None) != old:
            raise ValueError(f'Page changed during sync: {path}')
    if not changes:
        return
    journal = garden / 'journals' / (dt.date.today().strftime('%Y_%m_%d') + '.md')
    old_journal = journal.read_text() if journal.exists() else ''
    planned_journal = next((new for path, _, new in changes if path == journal), old_journal)
    new_journal = journal_text(planned_journal, changes)
    for path, _, new in changes:
        if new is None:
            path.unlink()
        else:
            path.write_text(new)
    journal.parent.mkdir(exist_ok=True)
    journal.write_text(new_journal)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--garden', type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument('--port', help='Exact CoreMIDI input/output port name')
    parser.add_argument('--inventory', type=Path, help='Read a previously captured complete JSON inventory')
    parser.add_argument('--save-inventory', type=Path, help='Save the complete device inventory as JSON')
    parser.add_argument('--apply', action='store_true', help='Apply graph metadata and journal changes (default: preview)')
    args = parser.parse_args()
    try:
        inventory = validate(json.loads(args.inventory.read_text()) if args.inventory else read_device(args.port))
        if args.save_inventory:
            args.save_inventory.write_text(json.dumps(inventory, indent=2) + '\n')
        changes = plan(args.garden.resolve(), inventory)
        for path, old, new in changes:
            print(('DELETE ' if new is None else 'CREATE ' if old is None else 'UPDATE ') + path.name)
        if args.apply:
            apply(args.garden.resolve(), changes)
        print(f'{len(changes)} page changes' + (' applied' if args.apply else ' proposed; use --apply to write'))
        return 0
    except (OSError, ValueError, RuntimeError) as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
