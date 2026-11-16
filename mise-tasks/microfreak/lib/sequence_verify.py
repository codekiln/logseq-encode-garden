#!/usr/bin/env python3
"""Check on the instrument that a slot plays and stores a described sequence.

With --base, the description is first written to --slot as
microfreak:write-sequence does. microfreak:audition then selects the slot,
plays it with MIDI Start and Clock, and records MIDI out and the Zoom H5.
Finally the slot is downloaded again and decoded. The report lists, for every
played step, the notes the description expects, the notes MIDI out carried and
the pitch the audio analysis heard, and whether the download still holds the
description.

A program change always loads pattern A, so playback is compared with
pattern A. To compare with pattern B, select the slot and press B on the
panel, then run with --pattern B --keep-selection, which plays the loaded
pattern without a program change.
"""
import argparse
import datetime as dt
import hashlib
import json
import sys
from pathlib import Path

import sequence as Q

# Modulation-track destinations whose CC was observed on MIDI out, with
# smoothing off: the CC carries half the stored value.
DESTINATION_CCS = {0x0101: 23, 0x0602: 106}


def expected_rows(pattern, loops, smoothing=(False,) * 4):
    """What MIDI out should carry on each played step of a canonical pattern.

    `pattern` is Q.canonical_pattern output plus in_use. A step tied into a
    step with the same note holds that note with no new Note On, also from the
    last step into step 1 on the next loop. Each modulation value on a track
    with a known CC and smoothing off sends that CC with half the value.
    """
    steps = pattern['steps']
    tracks = pattern.get('mod_tracks') or [None] * Q.TRACKS
    rows = []
    for loop in range(loops):
        for index, step in enumerate(steps):
            notes = step.get('notes', []) if pattern.get('in_use', True) else []
            previous = steps[index - 1] if (loop or index) else {}
            tied = set(previous.get('notes', [])) if previous.get('tie') else set()
            starts = [(note, velocity) for note, velocity in zip(notes, step.get('velocities', []))
                      if note not in tied]
            ccs = {}
            if pattern.get('in_use', True):
                for track, value in enumerate(step.get('mod') or []):
                    cc = DESTINATION_CCS.get(tracks[track])
                    if value is not None and cc is not None and not smoothing[track]:
                        ccs[str(cc)] = value // 2
            rows.append({'loop': loop + 1, 'step': index + 1, 'notes': sorted(starts),
                         'held': sorted(n for n in notes if n in tied), 'ccs': ccs})
    return rows


def names(notes):
    return [Q.note_name(n) for n in notes]


def compare_row(expected, row):
    """Merge one expected row with the audition row for the same step."""
    import sequence_midi
    midi = row['midi']
    got = sorted((n['note'], n['velocity']) for n in midi['notes'])
    held = {n['note'] for n in midi['held']}
    problems = []
    if got != expected['notes']:
        problems.append('notes')
    if not set(expected['held']) <= held:
        problems.append('held')
    if any(midi['ccs'].get(cc) != value for cc, value in expected['ccs'].items()):
        problems.append('ccs')
    result = {
        'loop': row['loop'], 'step': row['step'],
        'expected': {'notes': names(n for n, _ in expected['notes']),
                     'velocities': [v for _, v in expected['notes']],
                     'held': names(expected['held']), 'ccs': expected['ccs']},
        'midi_out': {'notes': names(n for n, _ in got), 'velocities': [v for _, v in got],
                     'held': names(sorted(held)), 'ccs': midi['ccs']},
        'midi_out_matches': not problems,
    }
    if problems:
        result['midi_out_differs_in'] = problems
    audio = row.get('audio')
    if audio is not None:
        result['audio'] = {
            'pitch': Q.note_name(audio['midi']) if audio.get('midi') is not None else None,
            'chord': names(c['midi'] for c in audio.get('chord') or []),
            'sounding': audio.get('sounding'), 'onset': audio.get('onset'),
        }
        wanted = {'notes': [{'note': n} for n, _ in expected['notes']],
                  'held': [{'note': n} for n in expected['held']]}
        result['audio_check'] = sequence_midi.classify(wanted, audio)
    return result


def summarize(rows, decode_differences, read_back_unchanged):
    mismatches = [f"loop {r['loop']} step {r['step']}: expected {r['expected']['notes'] or 'rest'} "
                  f"{r['expected']['velocities']}, MIDI out {r['midi_out']['notes'] or 'rest'} "
                  f"{r['midi_out']['velocities']}"
                  + (f" held {r['midi_out']['held']}" if 'held' in r.get('midi_out_differs_in', []) else '')
                  + (f" ccs {r['midi_out']['ccs']}" if 'ccs' in r.get('midi_out_differs_in', []) else '')
                  for r in rows if not r['midi_out_matches']]
    checks = {}
    for row in rows:
        if 'audio_check' in row:
            checks[row['audio_check']] = checks.get(row['audio_check'], 0) + 1
    return {'played_steps': len(rows),
            'midi_out_matching_steps': len(rows) - len(mismatches),
            'midi_out_mismatches': mismatches,
            'audio_checks': checks,
            'download_matches_description': not decode_differences,
            'download_differences': decode_differences,
            'download_equals_upload': read_back_unchanged}


def playing_pattern(sequence, decoded, name='A'):
    """The canonical pattern that plays: from the description, or from the slot when the
    description leaves it out."""
    stored = Q.stored_form(sequence)
    length = decoded['length']
    described = (stored.get('patterns') or {}).get(name)
    source = described if described is not None else Q.describe(decoded)['patterns'][name]
    pattern = Q.canonical_pattern(source, length)
    pattern['in_use'] = any(s.get('notes') or s.get('mod') for s in pattern['steps'])
    if described is None:
        pattern['in_use'] = decoded['patterns'][name]['in_use']
    return pattern, ('description' if described is not None else 'slot (left out of the description)')


def audition_args(args, out_dir):
    import audition
    argv = ['--slot', str(args.slot), '--loops', str(args.loops), '--bpm', str(args.bpm),
            '--wav-dir', str(out_dir)]
    if args.keep_selection:
        argv.append('--no-select')
    elif not args.preset_sound:
        argv.append('--plain')
    if args.no_audio:
        argv.append('--no-audio')
    if args.port:
        argv += ['--port', args.port]
    return audition.build_parser().parse_args(argv)


def download_slot(slot, port):
    import download
    midi_in, midi_out, _ = download.open_ports(port)
    try:
        _, _, data = download.read_patch(midi_in, midi_out, slot)
    finally:
        midi_in.close_port()
        midi_out.close_port()
    return data


def run(args):
    import audition
    import sequence_write
    if args.keep_selection and args.base is not None:
        raise ValueError('--keep-selection plays what is loaded; write with --base in a separate run')
    sequence = Q.load_description(args.sequence)
    out_dir = audition.guard_wav_dir(args.out_dir)
    report = {'schema': 1, 'slot': args.slot, 'description': str(args.sequence),
              'checked_at': dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')}
    uploaded_sha = None
    if args.base is not None:
        written = sequence_write.write(sequence, args.base, args.slot, backup_dir=args.backup_dir,
                                       name=args.name, category=args.category, port=args.port)
        report['write'] = {k: written[k] for k in ('base', 'name', 'category', 'settings_changed',
                                                   'upload', 'differences') if k in written}
        if 'stored_as' in written:
            report['write']['stored_as'] = written['stored_as']
        uploaded_sha = written['data_sha256']
    played = audition.run(audition_args(args, out_dir))
    report['sound'] = ('preset' if args.preset_sound or args.keep_selection
                       else 'microfreak:audition --plain')
    data = download_slot(args.slot, args.port)
    decoded = Q.decode_sequence(data)
    pattern, source = playing_pattern(sequence, decoded, args.pattern)
    expected = expected_rows(pattern, args.loops, decoded['smoothing'])
    rows = [compare_row(e, r) for e, r in zip(expected, played['steps'])]
    if len(expected) != len(played['steps']):
        report['warning'] = (f"audition played {len(played['steps'])} steps; "
                             f"the description expects {len(expected)}")
    read_back = hashlib.sha256(data).hexdigest()
    report.update({
        'name': played.get('name'),
        'played_pattern': args.pattern, 'expected_from': source,
        'selection': 'kept as loaded' if args.keep_selection else 'program change',
        'tempo': played.get('tempo'),
        'recording': played.get('recording'),
        'audition_warnings': played.get('warnings'),
        'globals_restored': played.get('instrument', {}).get('globals_changed'),
        'download': {'data_sha256': read_back, 'sequence': Q.describe(decoded)},
        'summary': summarize(rows, Q.differences(sequence, decoded),
                             None if uploaded_sha is None else read_back == uploaded_sha),
        'steps': rows,
    })
    stamp = dt.datetime.now().strftime('%Y%m%d-%H%M%S')
    path = out_dir / f'slot-{args.slot:03d}-{stamp}-verify.json'
    path.write_text(json.dumps(report, indent=1) + '\n')
    report['report_file'] = str(path)
    return report


def build_parser():
    import sequence_write
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('sequence', type=Path, help='JSON or YAML sequence description')
    parser.add_argument('--slot', type=int, required=True, help='Slot to write and play')
    parser.add_argument('--base', help='Write the description first, starting from this slot or .bin file')
    parser.add_argument('--backup-dir', type=Path, help='Save the slot here first when it holds a preset')
    parser.add_argument('--name')
    parser.add_argument('--category', choices=sequence_write.CATEGORIES)
    parser.add_argument('--loops', type=int, default=2)
    parser.add_argument('--bpm', type=float, default=120.0)
    parser.add_argument('--pattern', choices=('A', 'B'), default='A',
                        help='Pattern to compare playback with; B needs --keep-selection')
    parser.add_argument('--keep-selection', action='store_true',
                        help='Play the slot as loaded on the panel, without a program change')
    parser.add_argument('--preset-sound', action='store_true',
                        help='Play with the preset\'s own sound; by default audition\'s plain timbre')
    parser.add_argument('--no-audio', action='store_true', help='Skip the H5 recording')
    parser.add_argument('--out-dir', type=Path, required=True,
                        help='Folder outside the repository for the WAV and the JSON report')
    parser.add_argument('--port', help='Exact MIDI port name')
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.pattern == 'B' and not args.keep_selection:
        parser.error('a program change loads pattern A; press B on the panel and add --keep-selection')
    import audition
    import parameters
    try:
        report = run(args)
    except (audition.AuditionError, OSError, ValueError, KeyError, RuntimeError,
            parameters.UnsupportedLayout) as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 1
    import sequence_write
    print(sequence_write.dumps({k: report[k] for k in ('slot', 'name', 'report_file', 'summary')}
                               | {'steps': [compact(r) for r in report['steps']]}))
    summary = report['summary']
    return 0 if not summary['midi_out_mismatches'] and summary['download_matches_description'] else 1


def compact(row):
    """One line per step for the printed summary."""
    expected = ' '.join(f'{n}/{v}' for n, v in zip(row['expected']['notes'], row['expected']['velocities']))
    expected += (' held ' + ' '.join(row['expected']['held'])) if row['expected']['held'] else ''
    got = ' '.join(f'{n}/{v}' for n, v in zip(row['midi_out']['notes'], row['midi_out']['velocities']))
    line = (f"{row['loop']}.{row['step']:02d} expected [{expected or 'rest'}] "
            f"midi [{got or 'rest'}] {'ok' if row['midi_out_matches'] else 'DIFFERS'}")
    if 'audio' in row:
        line += f" audio [{row['audio']['pitch'] or '-'}; {' '.join(row['audio']['chord'])}] {row['audio_check']}"
    return line


if __name__ == '__main__':
    sys.exit(main())
