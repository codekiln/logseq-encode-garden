#!/usr/bin/env python3
"""Inspect saved MicroFreak parameter bytes without contacting an instrument.

The archive envelope follows Elektroid microfreak_sample.c at 6f3d50e2588f.
The parameter framing is inferred from exports and checked against a live
saved-patch read. Display conversions have not been verified.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
import zipfile


PAYLOAD_SIZE = 4672
HEADER_SIZE = 35
MAX_RECORD_SIZE = 100_000
# The guide names these controls; it does not define their serialized scales.
CONTROL_LABELS = {'VCO.Type': 'Oscillator Type', 'VCF.Cutoff': 'Filter Cutoff',
                  'VCF.Reso': 'Filter Resonance'}
# The guide lists Wave, Timbre, Shape in this order, but does not name Param1–3.
CANDIDATE_LABELS = {'VCO.Param1': 'Oscillator Wave', 'VCO.Param2': 'Oscillator Timbre',
                    'VCO.Param3': 'Oscillator Shape'}


class UnsupportedLayout(ValueError):
    """The bytes cannot be interpreted by the supported parameter layout."""


def unpack_payload(payload):
    """Expand each mask + seven 7-bit bytes into seven full bytes."""
    if len(payload) != PAYLOAD_SIZE or any(v > 127 for v in payload):
        raise UnsupportedLayout('Expected 4672 bytes of 7-bit preset payload')
    result = bytearray()
    for start in range(0, len(payload), 8):
        mask = payload[start]
        result.extend(v | (((mask >> bit) & 1) << 7)
                      for bit, v in enumerate(payload[start + 1:start + 8]))
    return bytes(result)


def parse_parameters(payload):
    """Return exact named three-byte values; leave the remaining bytes opaque."""
    data = unpack_payload(payload)
    offset = 0
    section = key = None
    fields = []
    seen = set()
    while offset < len(data):
        start = offset
        tag = data[offset]
        offset += 1
        if tag == 0x20:
            if section is not None or key is not None or not fields:
                raise UnsupportedLayout(f'Unexpected root terminator at byte {start}')
            return {'parameter_end_offset': offset,
                    'unpacked_size': len(data),
                    'uninterpreted_tail_size': len(data) - offset,
                    'fields': fields}
        if tag == 0x40:
            if section is None or key is not None:
                raise UnsupportedLayout(f'Unexpected section terminator at byte {start}')
            section = None
            continue
        kind, length = tag >> 5, tag & 31
        if length == 0 or offset + length > len(data):
            raise UnsupportedLayout(f'Invalid record length at byte {start}')
        value = data[offset:offset + length]
        offset += length
        if kind in (1, 2):
            try:
                name = value.decode('ascii')
            except UnicodeDecodeError as exc:
                raise UnsupportedLayout(f'Non-ASCII record name at byte {start}') from exc
            if not re.fullmatch(r'[A-Za-z][A-Za-z0-9]*', name):
                raise UnsupportedLayout(f'Unsupported record name at byte {start}')
            if kind == 1:
                if section is not None:
                    raise UnsupportedLayout(f'Unclosed section at byte {start}')
                section = name
            else:
                if section is None or key is not None:
                    raise UnsupportedLayout(f'Unexpected field name at byte {start}')
                key = name
        elif kind == 3:
            if section is None or key is None or length != 3:
                raise UnsupportedLayout(f'Unsupported parameter value at byte {start}')
            name = f'{section}.{key}'
            if name in seen:
                raise UnsupportedLayout(f'Duplicate field {name} at byte {start}')
            seen.add(name)
            field = {'name': name, 'unpacked_value_offset': offset - length,
                           'raw_hex': value.hex(), 'descriptor': value[0],
                           'value_le_unsigned': int.from_bytes(value[1:], 'little'),
                           'value_le_signed': int.from_bytes(value[1:], 'little', signed=True)}
            if name in CONTROL_LABELS:
                field['control_label'] = CONTROL_LABELS[name]
            if name in CANDIDATE_LABELS:
                field['candidate_control_label'] = CANDIDATE_LABELS[name]
                field['control_mapping'] = 'unverified'
            fields.append(field)
            key = None
        else:
            raise UnsupportedLayout(f'Unsupported record tag 0x{tag:02x} at byte {start}')
    raise UnsupportedLayout('Missing parameter-block root terminator')


class ArchiveReader:
    """Read length-prefixed text and decimal bytes from an MCC .mbp envelope."""
    def __init__(self, data):
        self.data, self.offset = data, 0

    def integer(self):
        match = re.match(rb'\s*(-?\d+)(?=\s|$)', self.data[self.offset:])
        if not match or len(match[1]) > 10:
            raise ValueError(f'Invalid archive integer at byte {self.offset}')
        self.offset += match.end()
        return int(match[1])

    def string(self):
        length = self.integer()
        if not 0 <= length <= MAX_RECORD_SIZE or self.data[self.offset:self.offset + 1] != b' ':
            raise ValueError('Invalid archive string length')
        self.offset += 1
        value = self.data[self.offset:self.offset + length]
        if len(value) != length:
            raise ValueError('Truncated archive string')
        self.offset += length
        return value.decode('ascii')

    def expect(self, expected):
        if self.integer() != expected:
            raise ValueError('Unsupported archive envelope')


def parse_mbp(data):
    if len(data) > MAX_RECORD_SIZE:
        raise ValueError('Preset archive record exceeds size limit')
    reader = ArchiveReader(data)
    if reader.string() != 'serialization::archive':
        raise ValueError('Unsupported archive signature')
    for value in (10, 0, 4):
        reader.expect(value)
    version, name = reader.string(), reader.string()
    category = reader.integer()
    reader.expect(0)
    reader.expect(0)
    attributes = reader.string()
    initialized = reader.integer()
    reader.expect(0)
    opaque_header_value = reader.integer()
    length = reader.integer()
    if initialized not in (0, 1) or length != (0 if initialized else PAYLOAD_SIZE):
        raise ValueError('Unsupported initialized flag or payload length')
    values = [reader.integer() for _ in range(length)]
    if any(not -128 <= v <= 255 for v in values):
        raise ValueError('Archive payload integer is outside byte range')
    if data[reader.offset:].strip():
        raise ValueError('Unexpected data after archive payload')
    return bytes(v & 255 for v in values), {
        'format_version': version, 'name': name, 'category_code': category,
        'initialized': bool(initialized), 'opaque_attributes': attributes,
        'opaque_header_value': opaque_header_value}


def load_preset(path, slot=None):
    """Load one record in memory; never extract a zip to disk."""
    suffix = path.suffix.lower()
    metadata = {}
    if suffix == '.mfprojz':
        if slot is None or not 1 <= slot <= 512:
            raise ValueError('A project archive requires --slot from 1 to 512')
        with zipfile.ZipFile(path) as archive:
            candidates = []
            for entry in archive.infolist():
                if entry.is_dir() or not entry.filename.lower().endswith('.mbp'):
                    continue
                basename = entry.filename.rsplit('/', 1)[-1]
                match = re.match(r'(\d+)-.*-[A-Za-z](\d+)\.mbp$', basename, re.IGNORECASE)
                if match and int(match[1]) == slot and int(match[2]) == slot:
                    candidates.append(entry)
            if len(candidates) != 1:
                raise ValueError('Slot must identify exactly one .mbp record in the project')
            entry = candidates[0]
            if entry.file_size > MAX_RECORD_SIZE:
                raise ValueError('Preset archive record exceeds size limit')
            content = archive.read(entry)
            metadata['archive_member'] = entry.filename
            metadata['project_slot'] = slot
        payload, envelope = parse_mbp(content)
        metadata.update(envelope)
    else:
        if slot is not None:
            raise ValueError('--slot applies only to .mfprojz project archives')
        if path.stat().st_size > MAX_RECORD_SIZE:
            raise ValueError('Preset file exceeds size limit')
        content = path.read_bytes()
        if suffix == '.mbp':
            payload, metadata = parse_mbp(content)
        elif suffix == '.bin':
            if len(content) == HEADER_SIZE + PAYLOAD_SIZE:
                metadata['header_hex'] = content[:HEADER_SIZE].hex()
                payload = content[HEADER_SIZE:]
            elif len(content) == PAYLOAD_SIZE:
                payload = content
            else:
                raise ValueError('Binary preset must be 4672 payload bytes or 35 header + 4672 payload bytes')
        else:
            raise ValueError('Supported inputs: .mbp, .mfprojz, or .bin')
    metadata['record_sha256'] = hashlib.sha256(content).hexdigest()
    metadata['payload_sha256'] = hashlib.sha256(payload).hexdigest()
    return payload, metadata


def inspect(path, slot=None):
    payload, metadata = load_preset(path, slot)
    result = {'schema': 1, 'source': str(path), 'metadata': metadata,
              'value_context': 'saved_base_setting',
              'display_conversions': 'unverified',
              'descriptor_semantics': 'unverified'}
    if metadata.get('initialized'):
        return dict(result, status='initialized', fields=[])
    try:
        return dict(result, status='raw_parameters', **parse_parameters(payload))
    except UnsupportedLayout as exc:
        return dict(result, status='unsupported_layout', error=str(exc))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', type=Path, help='Saved .mbp, .mfprojz, or .bin file')
    parser.add_argument('--slot', type=int, help='Computer-project slot for .mfprojz')
    args = parser.parse_args(argv)
    try:
        result = inspect(args.file, args.slot)
    except (OSError, ValueError, zipfile.BadZipFile, RuntimeError) as exc:
        print(json.dumps({'status': 'invalid_input', 'error': str(exc)}))
        return 2
    print(json.dumps(result, indent=2))
    return 2 if result['status'] == 'unsupported_layout' else 0


if __name__ == '__main__':
    sys.exit(main())
