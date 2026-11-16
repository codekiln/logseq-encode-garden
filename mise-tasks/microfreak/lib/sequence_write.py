#!/usr/bin/env python3
"""Write a described sequence into a MicroFreak preset, to a file, a slot or both.

The base preset is a slot, read without changing it, or a file saved by
microfreak:download. sequence.make_playable writes the steps and turns on
sequencer mode, and paraphony when a step holds a chord. With --slot the
result goes through microfreak:upload: a slot that holds a preset is saved to
--backup-dir first, and the slot is read back and compared with what was sent.
The task prints one JSON report that includes the stored sequence, decoded
again from the result, and any difference from the description.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

import parameters
import sequence as Q

CATEGORIES = ('Bass', 'Brass', 'Keys', 'Lead', 'Organ', 'Pad', 'Percussion',
              'Sequence', 'SFX', 'Strings', 'Template', 'Vocoder')


def base_slot(text):
    """The slot number when --base names a slot, else None."""
    text = str(text)
    return int(text) if text.isdigit() else None


def load_base_file(path):
    import upload
    header, data = upload.load_patch(path)
    return bytes(header), bytes(data)


def read_base_slot(midi_in, midi_out, slot):
    import download
    metadata, header, data = download.read_patch(midi_in, midi_out, slot)
    return bytes(header), bytes(data), metadata


def prepare(sequence, header, payload, name=None, category=None):
    """Return the new payload, the header values to store and what changed."""
    import upload
    new, changed = Q.make_playable(payload, sequence)
    name = name or sequence.get('name') or upload.preset_name(header)
    category = category or sequence.get('category')
    upload.check_name(name)
    if category is not None and category not in CATEGORIES:
        raise ValueError(f'Unknown category {category!r}; use one of {", ".join(CATEGORIES)}')
    return new, changed, name, category


def file_header(header, name, category):
    """The base's header with the new name and category, for a .bin file."""
    import upload
    result = bytearray(header)
    if category is not None:
        result[upload.CATEGORY] = CATEGORIES.index(category)
    result[upload.NAME] = name.encode('ascii').ljust(upload.NAME_LEN, b'\0')
    return bytes(result)


def report_for(sequence, base, header, new, changed, name, category):
    import upload
    decoded = Q.decode_sequence(new)
    stored = Q.stored_form(sequence)
    report = {'base': base, 'name': name,
              'category': category or CATEGORIES[header[upload.CATEGORY]],
              'settings_changed': changed}
    if stored is not sequence:
        report['stored_as'] = (f"the {sequence['length']}-step loop repeated to fill {stored['length']} "
                               f"steps; the instrument's shortest length is 4")
    report['sequence'] = Q.describe(decoded)
    kept = [p for p in Q.PATTERN_OFFSETS if p not in (sequence.get('patterns') or {})]
    if kept:
        report['kept_from_base'] = kept
    report['differences'] = Q.differences(sequence, decoded)
    report['data_sha256'] = hashlib.sha256(new).hexdigest()
    return report


def write(sequence, base, slot=None, output=None, backup_dir=None, name=None,
          category=None, port=None):
    """Write the description; returns the report the task prints."""
    import upload
    source_slot = base_slot(base)
    midi_in = midi_out = None
    try:
        if source_slot is not None or slot is not None:
            import download
            midi_in, midi_out, device = download.open_ports(port)
        if source_slot is not None:
            header, payload, metadata = read_base_slot(midi_in, midi_out, source_slot)
            base_info = {'slot': source_slot, 'name': metadata['name']}
        else:
            header, payload = load_base_file(base)
            base_info = {'file': str(base), 'name': upload.preset_name(header)}
        new, changed, name, category = prepare(sequence, header, payload, name, category)
        report = report_for(sequence, base_info, header, new, changed, name, category)
        if output is not None:
            with Path(output).open('xb') as handle:
                handle.write(file_header(header, name, category) + new)
            report['output'] = str(output)
        if slot is not None:
            sent = upload.build_header(header, slot, name, category)
            result = upload.upload(midi_in, midi_out, slot, sent, new, backup_dir, device)
            report['upload'] = {
                'slot': slot, 'name': result['after']['name'],
                'category': result['after']['category'],
                'was': (None if result['before']['initialized']
                        else f"{result['before']['name']} ({result['before']['category']})"),
                'backup': str(result['backup']) if 'backup' in result else None,
                'read_back_matches': result['sha256'] == report['data_sha256'],
            }
        return report
    finally:
        if midi_in is not None:
            midi_in.close_port()
        if midi_out is not None:
            midi_out.close_port()


def dumps(value, indent=0, width=100):
    """JSON with any list or object that fits in `width` characters on one line."""
    flat = json.dumps(value)
    if not isinstance(value, (dict, list)) or len(flat) + indent <= width:
        return flat
    pad = ' ' * (indent + 2)
    if isinstance(value, dict):
        items = [f'{pad}{json.dumps(k)}: {dumps(v, indent + 2, width)}' for k, v in value.items()]
        return '{\n' + ',\n'.join(items) + '\n' + ' ' * indent + '}'
    items = [pad + dumps(v, indent + 2, width) for v in value]
    return '[\n' + ',\n'.join(items) + '\n' + ' ' * indent + ']'


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('sequence', type=Path, help='JSON or YAML sequence description')
    parser.add_argument('--base', required=True,
                        help='Preset to start from: a slot number or a microfreak:download .bin file')
    parser.add_argument('--slot', type=int, help='Upload the result to this slot and read it back')
    parser.add_argument('--output', type=Path, help='Also write the result to this new .bin file')
    parser.add_argument('--backup-dir', type=Path,
                        help='Save the target slot here first; required when it holds a preset')
    parser.add_argument('--name', help='Preset name; default the description\'s name, else the base\'s')
    parser.add_argument('--category', choices=CATEGORIES,
                        help='Preset category; default the description\'s category, else the base\'s')
    parser.add_argument('--port', help='Exact MIDI port name')
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        sequence = Q.load_description(args.sequence)
        report = write(sequence, args.base, args.slot, args.output, args.backup_dir,
                       args.name, args.category, args.port)
    except FileExistsError as exc:
        print(f'error: {exc.filename} already exists', file=sys.stderr)
        return 1
    except (OSError, ValueError, KeyError, RuntimeError, parameters.UnsupportedLayout) as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 1
    print(dumps(report))
    return 1 if report['differences'] else 0


if __name__ == '__main__':
    sys.exit(main())
