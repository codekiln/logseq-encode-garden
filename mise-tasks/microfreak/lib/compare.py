#!/usr/bin/env python3
"""Compare observed saved MicroFreak parameter records and complete payloads."""
import argparse
from itertools import zip_longest
import json
from pathlib import Path
import sys
import zipfile

import parameters


VALUE_KEYS = ('raw_hex', 'descriptor', 'value_le_unsigned', 'value_le_signed')


def field_value(field):
    """Keep exact bytes alongside both integer readings of the two value bytes."""
    return {key: field[key] for key in VALUE_KEYS}


def source_summary(report):
    metadata = report['metadata']
    result = {
        'source': report['source'],
        'status': report['status'],
        'record_sha256': metadata['record_sha256'],
        'payload_sha256': metadata['payload_sha256'],
    }
    if 'error' in report:
        result['error'] = report['error']
    return result


def compare(path_a, path_b, slot_a=None, slot_b=None):
    """Return observations; a named field's change does not establish its cause."""
    left = parameters.inspect(path_a, slot_a)
    right = parameters.inspect(path_b, slot_b)
    payload_a, _ = parameters.load_preset(path_a, slot_a)
    payload_b, _ = parameters.load_preset(path_b, slot_b)
    fields_a = {field['name']: field for field in left.get('fields', [])}
    fields_b = {field['name']: field for field in right.get('fields', [])}
    both_parsed = left['status'] in ('raw_parameters', 'initialized') and right['status'] in ('raw_parameters', 'initialized')
    changed = []
    added = []
    removed = []
    if both_parsed:
        for name in sorted(fields_a.keys() & fields_b.keys()):
            before, after = field_value(fields_a[name]), field_value(fields_b[name])
            if before != after:
                changed.append({'name': name, 'before': before, 'after': after})
        added = [{'name': name, 'after': field_value(fields_b[name])}
                 for name in sorted(fields_b.keys() - fields_a.keys())]
        removed = [{'name': name, 'before': field_value(fields_a[name])}
                   for name in sorted(fields_a.keys() - fields_b.keys())]
    tail_changed = None
    if left['status'] == right['status'] == 'raw_parameters':
        tail_a = parameters.unpack_payload(payload_a)[left['parameter_end_offset']:]
        tail_b = parameters.unpack_payload(payload_b)[right['parameter_end_offset']:]
        tail_changed = tail_a != tail_b
    return {
        'schema': 1,
        'status': 'compared' if both_parsed else 'unsupported_layout',
        'a': source_summary(left),
        'b': source_summary(right),
        'changed_fields': changed,
        'added_fields': added,
        'removed_fields': removed,
        'changed_payload_byte_count': sum(a != b for a, b in zip_longest(payload_a, payload_b)),
        'uninterpreted_tail_changed': tail_changed,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file_a', type=Path)
    parser.add_argument('file_b', type=Path)
    parser.add_argument('--slot-a', type=int)
    parser.add_argument('--slot-b', type=int)
    args = parser.parse_args(argv)
    try:
        result = compare(args.file_a, args.file_b, args.slot_a, args.slot_b)
    except (OSError, ValueError, zipfile.BadZipFile, RuntimeError) as exc:
        print(json.dumps({'status': 'invalid_input', 'error': str(exc)}, sort_keys=True))
        return 2
    print(json.dumps(result, separators=(',', ':'), sort_keys=True))
    return 0 if result['status'] == 'compared' else 2


if __name__ == '__main__':
    sys.exit(main())
