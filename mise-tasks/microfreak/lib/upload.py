#!/usr/bin/env python3
"""Write one complete MicroFreak preset to a slot over USB.

Protocol source: Elektroid's microfreak_preset_upload at
https://github.com/dagargo/elektroid/blob/6f3d50e2588f0236afb3510e1c55bbb292446aa2/src/connectors/microfreak.c#L449-L552
The input is the raw file that microfreak:download saves: the 35-byte header
followed by 146 32-byte data packets. A slot that holds a preset is saved to
--backup-dir in the same format before it is overwritten. After the transfer
the slot is read back and compared with what was sent.
"""

import argparse
import hashlib
import sys
import time
from pathlib import Path

from download import (HEADER_LEN, PART_LEN, PARTS, open_ports, read_header,
                      read_patch, receive, save_patch, slot_address)
from sync import ALPHABET, CATEGORIES

ACK = 0x18
INIT = 3
SLOT_IN_BANK = 8
HALF = 9
CATEGORY = 10
FLAGS = 11
NAME = slice(12, 26)
NAME_LEN = 14
RAW_LEN = HEADER_LEN + PARTS * PART_LEN


def preset_name(header):
    name = bytes(header[NAME]).split(b'\0', 1)[0].decode('ascii', 'replace')
    check_name(name)
    return name


def check_name(name):
    if not ALPHABET.fullmatch(name) or name != name.strip():
        raise ValueError(f'Preset names are 1-14 letters, digits, spaces, '
                         f'periods, underscores or hyphens, without leading or '
                         f'trailing spaces: {name!r}')
    return name


def load_patch(path):
    """Return the header and data of a file saved by microfreak:download."""
    raw = Path(path).read_bytes()
    if len(raw) != RAW_LEN:
        raise ValueError(f'{path} is {len(raw)} bytes long; a microfreak:download '
                         f'file is {RAW_LEN}')
    if any(value > 0x7F for value in raw):
        raise ValueError(f'{path} has values above 0x7F, which SysEx cannot carry')
    header, data = raw[:HEADER_LEN], raw[HEADER_LEN:]
    if header[INIT] & 8:
        raise ValueError(f'{path} marks its preset as initialized')
    if header[CATEGORY] >= len(CATEGORIES):
        raise ValueError(f'{path} has an unknown category number {header[CATEGORY]}')
    preset_name(header)
    return header, data


def build_header(source, slot, name=None, category=None):
    """Return the header Elektroid sends for a slot.

    Elektroid's .mfp format keeps the name, the category and the value at
    offset 11 of the header; its upload sends those with the target address
    and leaves every other field zero. The initialized flag is clear.
    Elektroid also sends zero at offset 9, but the MicroFreak stores
    (slot - 1) // 256 there whatever it receives, so this header sends the
    value the slot will hold.
    """
    bank, program = slot_address(slot)
    header = [0] * HEADER_LEN
    header[0], header[1], header[SLOT_IN_BANK] = bank, program, program
    header[HALF] = (slot - 1) // 256
    header[CATEGORY] = CATEGORIES.index(category) if category else source[CATEGORY]
    header[FLAGS] = source[FLAGS]
    name = check_name(name) if name is not None else preset_name(source)
    header[NAME] = list(name.encode('ascii').ljust(NAME_LEN, b'\0'))
    return header


def write_patch(midi_in, midi_out, slot, header, data):
    """Send the header, the store request and every data packet.

    The MicroFreak acknowledges each message with an empty operation 0x18
    response; any other response stops the transfer.
    """
    sequence = 0

    def send(op, payload):
        nonlocal sequence
        receive(midi_in, midi_out, sequence, op, list(payload), ACK, 0)
        sequence = (sequence + 1) % 128
        time.sleep(.005)

    send(0x52, header)
    send(0x52, slot_address(slot) + [1])
    send(0x15, [])
    for index in range(PARTS):
        op = 0x17 if index == PARTS - 1 else 0x16
        send(op, data[index * PART_LEN:(index + 1) * PART_LEN])
    time.sleep(.03)


def upload(midi_in, midi_out, slot, header, data, backup_dir=None, device=''):
    """Back up the slot if it holds a preset, write, then read the slot back."""
    result = {'slot': slot}
    before, _ = read_header(midi_in, midi_out, slot)
    result['before'] = before
    if not before['initialized']:
        if backup_dir is None:
            raise ValueError(f"Slot {slot} holds {before['name']} ({before['category']}); "
                             'pass --backup-dir to save it before writing')
        metadata, old_header, old_data = read_patch(midi_in, midi_out, slot)
        result['backup'], _, _ = save_patch(Path(backup_dir), metadata,
                                            old_header, old_data, device)
    time.sleep(.005)
    write_patch(midi_in, midi_out, slot, header, data)
    after, after_header, after_data = read_patch(midi_in, midi_out, slot)
    result.update(after=after, sent_header=bytes(header), read_header=after_header,
                  sha256=hashlib.sha256(after_data).hexdigest())
    if after_data != bytes(data):
        part = next(i for i in range(PARTS)
                    if after_data[i * PART_LEN:(i + 1) * PART_LEN]
                    != bytes(data[i * PART_LEN:(i + 1) * PART_LEN]))
        raise ValueError(f'Slot {slot} read back differs from the file from packet {part + 1} of {PARTS}')
    if (after['name'], after['category']) != (preset_name(header), CATEGORIES[header[CATEGORY]]):
        raise ValueError(f"Slot {slot} read back as {after['name']} ({after['category']})")
    return result


def report(result):
    slot, before, after = result['slot'], result['before'], result['after']
    if 'backup' in result:
        print(f"Saved {before['name']} ({before['category']}) from slot {slot} to {result['backup']}")
    else:
        print(f'Slot {slot} was initialized; nothing to back up')
    print(f"Wrote {after['name']} ({after['category']}) to slot {slot}; "
          f"read back matches, data SHA-256 {result['sha256']}")
    changed = [f'{i}: sent {s:02x}, read {r:02x}'
               for i, (s, r) in enumerate(zip(result['sent_header'], result['read_header']))
               if s != r]
    if changed:
        print('Header fields that read back differently from what was sent: '
              + '; '.join(changed))


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('file', type=Path, help='.bin file saved by microfreak:download')
    parser.add_argument('--slot', type=int, required=True, help='Preset slot from 1 to 512')
    parser.add_argument('--backup-dir', type=Path,
                        help='Save the slot here first; required when the slot holds a preset')
    parser.add_argument('--name', help='Preset name to store instead of the one in the file')
    parser.add_argument('--category', choices=CATEGORIES,
                        help='Category to store instead of the one in the file')
    parser.add_argument('--port', help='Exact MIDI input/output port name')
    args = parser.parse_args()
    midi_in = midi_out = None
    try:
        source, data = load_patch(args.file)
        header = build_header(source, args.slot, args.name, args.category)
        midi_in, midi_out, device = open_ports(args.port)
        report(upload(midi_in, midi_out, args.slot, header, data, args.backup_dir, device))
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
