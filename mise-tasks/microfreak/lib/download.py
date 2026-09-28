#!/usr/bin/env python3
"""Download a complete MicroFreak preset without modifying device state.

Protocol source: Elektroid's microfreak_preset_download at
https://github.com/dagargo/elektroid/blob/6f3d50e2588f0236afb3510e1c55bbb292446aa2/src/connectors/microfreak.c#L322-L444
The raw file is the 35-byte header followed by 146 unmodified 32-byte data
packets. It is not an .mfp or .mbp file; those use a separate serialization.
"""

import argparse
import datetime as dt
import hashlib
import json
import sys
import time
from pathlib import Path

from sync import PREFIX, decode_header

HEADER_LEN = 35
PARTS = 146
PART_LEN = 32
SOURCE = ('https://github.com/dagargo/elektroid/blob/'
          '6f3d50e2588f0236afb3510e1c55bbb292446aa2/'
          'src/connectors/microfreak.c#L322-L444')


def receive(midi_in, midi_out, sequence, op, payload, expected_op, expected_len):
    """Request one packet and reject truncated or misidentified responses."""
    while midi_in.get_message():
        pass
    midi_out.send_message(PREFIX + [sequence, len(payload), op] + payload + [0xF7])
    deadline = time.monotonic() + 3
    while time.monotonic() < deadline:
        received = midi_in.get_message()
        if received:
            message = received[0]
            if message[:6] != PREFIX or len(message) < 7 or message[6] != sequence:
                continue
            if (len(message) != 10 + expected_len or message[7] != expected_len
                    or message[8] != expected_op or message[-1] != 0xF7):
                raise ValueError(f'Unexpected response for sequence {sequence}')
            return message
        time.sleep(.002)
    raise RuntimeError(f'Timed out waiting for response to sequence {sequence}')


def read_patch(midi_in, midi_out, slot):
    """Return the preset header and every data byte from a populated slot."""
    if not 1 <= slot <= 512:
        raise ValueError('Slot must be from 1 to 512')
    preset_id = slot - 1
    address = [preset_id // 128, preset_id % 128]
    sequence = 0
    header_message = receive(midi_in, midi_out, sequence, 0x19,
                             address + [0], 0x52, HEADER_LEN)
    metadata = decode_header(header_message, slot, sequence)
    header = bytes(header_message[9:-1])
    if metadata['initialized']:
        raise ValueError(f'Slot {slot} is initialized and has no patch data')
    time.sleep(.005)
    sequence = (sequence + 1) % 128
    receive(midi_in, midi_out, sequence, 0x19, address + [1], 0x15, 0)
    time.sleep(.005)
    chunks = []
    for index in range(PARTS):
        sequence = (sequence + 1) % 128
        expected_op = 0x17 if index == PARTS - 1 else 0x16
        message = receive(midi_in, midi_out, sequence, 0x18, [0],
                          expected_op, PART_LEN)
        chunks.append(bytes(message[9:-1]))
        time.sleep(.005)
    data = b''.join(chunks)
    if len(data) != PARTS * PART_LEN:
        raise ValueError('Incomplete preset data')
    return metadata, header, data


def open_ports(port):
    try:
        import rtmidi
    except ImportError as exc:
        raise RuntimeError('Install python-rtmidi==1.5.8, or run the mise task.') from exc
    midi_in, midi_out = rtmidi.MidiIn(), rtmidi.MidiOut()

    def select(ports):
        matches = [(index, name) for index, name in enumerate(ports)
                   if (name == port if port else 'microfreak' in name.lower())]
        if len(matches) != 1:
            raise RuntimeError(f'Choose a unique MicroFreak MIDI port with --port; available: {ports}')
        return matches[0]

    input_id, input_name = select(midi_in.get_ports())
    output_id, _ = select(midi_out.get_ports())
    midi_in.ignore_types(sysex=False)
    midi_in.open_port(input_id)
    midi_out.open_port(output_id)
    return midi_in, midi_out, input_name


def save_patch(output_dir, metadata, header, data, device):
    slot = metadata['number']
    if len(header) != HEADER_LEN or len(data) != PARTS * PART_LEN:
        raise ValueError('Refusing to save an incomplete patch')
    raw = header + data
    raw_name = f'slot-{slot:03d}.bin'
    manifest_name = f'slot-{slot:03d}.json'
    manifest = {
        'schema': 1,
        'slot': slot,
        'name': metadata['name'],
        'category': metadata['category'],
        'device': device,
        'captured_at': dt.datetime.now(dt.timezone.utc).isoformat(),
        'raw_file': raw_name,
        'raw_bytes': len(raw),
        'raw_sha256': hashlib.sha256(raw).hexdigest(),
        'header_bytes': len(header),
        'header_sha256': hashlib.sha256(header).hexdigest(),
        'data_bytes': len(data),
        'data_sha256': hashlib.sha256(data).hexdigest(),
        'protocol_source': SOURCE,
    }
    raw_path = output_dir / raw_name
    manifest_path = output_dir / manifest_name
    if raw_path.exists() or manifest_path.exists():
        raise FileExistsError(f'Preset export already exists for slot {slot}: {output_dir}')
    output_dir.mkdir(parents=True, exist_ok=True)
    with raw_path.open('xb') as output:
        output.write(raw)
    with manifest_path.open('x') as output:
        output.write(json.dumps(manifest, indent=2) + '\n')
    return raw_path, manifest_path, manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--slot', type=int, required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--port', help='Exact MIDI input/output port name')
    args = parser.parse_args()
    midi_in = midi_out = None
    try:
        midi_in, midi_out, device = open_ports(args.port)
        metadata, header, data = read_patch(midi_in, midi_out, args.slot)
        raw_path, manifest_path, manifest = save_patch(args.output_dir, metadata,
                                                       header, data, device)
        print(f"{raw_path}: {manifest['raw_bytes']} bytes, SHA-256 {manifest['raw_sha256']}")
        print(f'{manifest_path}')
        return 0
    except (OSError, ValueError, RuntimeError) as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 1
    finally:
        if midi_in is not None:
            midi_in.close_port()
        if midi_out is not None:
            midi_out.close_port()


if __name__ == '__main__':
    sys.exit(main())
