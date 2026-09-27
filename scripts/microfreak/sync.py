#!/usr/bin/env python3
"""Read saved MicroFreak preset headers and reconcile Logseq metadata.

Wire layout reference: dagargo/elektroid src/connectors/microfreak.c.
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
CATEGORIES = ['Bass', 'Brass', 'Keys', 'Lead', 'Organ', 'Pad', 'Percussion',
              'Sequence', 'SFX', 'Strings', 'Template', 'Vocoder']
ENTITY = '[[Logseq/Entity/Preset/Synth/Microfreak]]'
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


def update(text, values):
    lines = text.splitlines()
    boundary = 0
    while boundary < len(lines) and re.fullmatch(r'[a-z][a-z0-9-]*:: .*', lines[boundary]):
        boundary += 1
    for key, value in values.items():
        indices = [i for i in range(boundary) if lines[i].startswith(key + ':: ')]
        if indices:
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
    changes = []
    current = {}
    for path in pages.glob('Microfreak___Preset___*.md'):
        text = path.read_text()
        props = properties(text)
        if props.get('logseq-entity') == ENTITY:
            key = (props.get('preset-number'), props.get('preset-name'))
            if key in current:
                raise ValueError(f'Duplicate preset identity: {key}')
            current[key] = (path, text)
    active = set()
    for p in sorted(inventory['presets'], key=lambda p: p['number']):
        if p['initialized']:
            continue
        key = (str(p['number']), p['name'])
        active.add(key)
        title = f"Microfreak/Preset/{p['number']} {p['name']}"
        path, old = current.get(key, (pages / (title.replace('/', '___') + '.md'), None))
        if old is None and path.exists():
            raise ValueError(f'Unmanaged page already exists: {path}; reconcile its metadata before applying')
        values = {'logseq-entity': ENTITY, 'preset-number': str(p['number']),
                  'preset-name': p['name'], 'preset-category': p['category'],
                  'preset-initialized': str(p['initialized']).lower(), 'preset-on-device': 'true'}
        if old is None:
            values['preset-origin'] = 'unknown'
        new = update(old if old is not None else f"- # {p['name']}\n\t- Saved [[Microfreak]] preset in slot {p['number']}.\n", values)
        if new != old:
            changes.append((path, old, new))
    for key, (path, old) in current.items():
        if key not in active:
            new = update(old, {'preset-on-device': 'false'})
            if new != old:
                changes.append((path, old, new))
    return changes


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
            while position < end and lines[position].startswith('\t\t'):
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
    new_journal = journal_text(old_journal, changes)
    for path, _, new in changes:
        path.write_text(new)
    journal.parent.mkdir(exist_ok=True)
    journal.write_text(new_journal)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--garden', type=Path, default=Path(__file__).resolve().parents[2])
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
        for path, old, _ in changes:
            print(('CREATE ' if old is None else 'UPDATE ') + path.name)
        if args.apply:
            apply(args.garden.resolve(), changes)
        print(f'{len(changes)} page changes' + (' applied' if args.apply else ' proposed; use --apply to write'))
        return 0
    except (OSError, ValueError, RuntimeError) as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
