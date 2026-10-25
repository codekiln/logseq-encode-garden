#!/usr/bin/env python3
"""List MicroFreak slots whose saved sound differs from the garden's preset pages.

Reads every requested slot with the same read-only requests as
``microfreak:download`` and compares each payload's SHA-256 with the page's
``preset-synth-microfreak-parameter-payload-sha256``. It never writes to the
instrument. With ``--save-dir`` it keeps the reads of changed and new slots
so ``microfreak:pages`` can back them up.
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

import download

PROPERTY = re.compile(r'^([a-z0-9-]+):: (.*)$', re.M)


def page_index(garden):
    """Return {slot: {page, name, payload_sha256, on_device}} from the preset pages."""
    index = {}
    for path in sorted((Path(garden) / 'pages').glob('Microfreak___Preset___[0-9][0-9][0-9] *.md')):
        if '___Asset___' in path.name:
            continue
        front = path.read_text().split('\n- ', 1)[0]
        props = dict(PROPERTY.findall(front))
        try:
            slot = int(props.get('preset-synth-microfreak-number', ''))
        except ValueError:
            continue
        index[slot] = {'page': path.stem.replace('___', '/'),
                       'name': props.get('preset-synth-microfreak-name'),
                       'payload_sha256': props.get('preset-synth-microfreak-parameter-payload-sha256'),
                       'file_sha256': props.get('preset-synth-file-sha256'),
                       'on_device': props.get('preset-synth-microfreak-on-device') == 'true'}
    return index


def classify(slot, read, pages):
    """Return a change record, or None when the page already matches the device.

    ``read`` is None for an initialized slot, else {name, category, payload_sha256,
    raw_sha256}. A page without a payload digest still matches when its file
    digest equals the raw read (header plus data).
    """
    page = pages.get(slot)
    if read is None:
        if page and page['on_device'] and (page['payload_sha256'] or page['file_sha256']):
            return {'slot': slot, 'status': 'emptied', 'page': page['page']}
        return None
    record = {'slot': slot, 'name': read['name'], 'category': read['category'],
              'payload_sha256': read['payload_sha256']}
    if page is None:
        return dict(record, status='new')
    record['page'] = page['page']
    if not page['payload_sha256']:
        if page['file_sha256'] and page['file_sha256'] == read.get('raw_sha256'):
            return None
        return dict(record, status='no payload digest' if page['file_sha256'] else 'not backed up')
    if page['payload_sha256'] != read['payload_sha256']:
        return dict(record, status='changed', page_payload_sha256=page['payload_sha256'])
    if page['name'] != read['name']:
        return dict(record, status='renamed', page_name=page['name'])
    return None


def read_slot(midi_in, midi_out, slot):
    """Return (metadata, header, data), or None for an initialized slot."""
    try:
        return download.read_patch(midi_in, midi_out, slot)
    except ValueError as exc:
        if 'initialized' in str(exc):
            return None
        raise


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    parser.add_argument('--garden', type=Path, required=True)
    parser.add_argument('--slots', default='1-512', help='Slot range, e.g. 1-400')
    parser.add_argument('--port', help='Exact MIDI input/output port name')
    parser.add_argument('--save-dir', type=Path, help='Keep reads of changed and new slots here')
    parser.add_argument('--json', action='store_true', help='Print one JSON object')
    args = parser.parse_args(argv)
    first, _, last = args.slots.partition('-')
    slots = range(int(first), int(last or first) + 1)
    pages = page_index(args.garden)
    changes, unchanged, initialized = [], 0, 0
    midi_in = midi_out = None
    try:
        midi_in, midi_out, device = download.open_ports(args.port)
        for slot in slots:
            result = read_slot(midi_in, midi_out, slot)
            read = None
            if result is None:
                initialized += 1
            else:
                metadata, header, data = result
                read = {'name': metadata['name'], 'category': metadata['category'],
                        'payload_sha256': hashlib.sha256(data).hexdigest(),
                        'raw_sha256': hashlib.sha256(header + data).hexdigest()}
            change = classify(slot, read, pages)
            if change is None:
                unchanged += result is not None
                continue
            changes.append(change)
            if args.save_dir and result is not None:
                download.save_patch(args.save_dir, metadata, header, data, device)
    except (OSError, RuntimeError) as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 1
    finally:
        if midi_in is not None:
            midi_in.close_port()
        if midi_out is not None:
            midi_out.close_port()
    summary = {'slots_read': len(slots), 'unchanged': unchanged, 'initialized': initialized,
               'changes': changes}
    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        for change in changes:
            print(f"{change['slot']:03d} {change['status']}: {change.get('name') or change.get('page')}")
        print(f'{len(changes)} to update, {unchanged} unchanged, {initialized} initialized')
    return 0


if __name__ == '__main__':
    sys.exit(main())
