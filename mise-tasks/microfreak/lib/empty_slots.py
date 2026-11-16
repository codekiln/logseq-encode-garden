#!/usr/bin/env python3
"""List the MicroFreak slots that hold no preset, reading only preset headers.

A slot is empty when its header marks it initialized: microfreak:download
refuses it, and microfreak:upload and microfreak:write-sequence write to it
without a backup. Only the preset-header request (0x19, mode 0) is sent, as
microfreak:sync does, so nothing on the instrument changes.
"""
import argparse
import json
import sys
import time

import download


def ranges(slots):
    """['321-349', '383', '403-512'] for a sorted list of slot numbers."""
    found = []
    for slot in slots:
        if found and found[-1][1] == slot - 1:
            found[-1][1] = slot
        else:
            found.append([slot, slot])
    return [f'{a}-{b}' if a != b else str(a) for a, b in found]


def empty_slots(midi_in, midi_out, first, last, read_header=download.read_header):
    """Return the initialized slots from first to last."""
    empty = []
    for slot in range(first, last + 1):
        metadata, _ = read_header(midi_in, midi_out, slot, (slot - 1) % 128)
        if metadata['initialized']:
            empty.append(slot)
        time.sleep(.005)
    return empty


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--first', type=int, default=1, help='First slot to read; default 1')
    parser.add_argument('--last', type=int, default=512, help='Last slot to read; default 512')
    parser.add_argument('--port', help='Exact MIDI port name')
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    if not 1 <= args.first <= args.last <= 512:
        print('error: slots run from 1 to 512, with --first no greater than --last', file=sys.stderr)
        return 1
    midi_in = midi_out = None
    try:
        midi_in, midi_out, _ = download.open_ports(args.port)
        empty = empty_slots(midi_in, midi_out, args.first, args.last)
    except (OSError, ValueError, RuntimeError) as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 1
    finally:
        if midi_in is not None:
            midi_in.close_port()
        if midi_out is not None:
            midi_out.close_port()
    print(json.dumps({'slots_read': f'{args.first}-{args.last}', 'empty_count': len(empty),
                      'empty': ranges(empty)}))
    return 0


if __name__ == '__main__':
    sys.exit(main())
