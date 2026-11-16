#!/usr/bin/env python3
"""Play one MicroFreak slot's sequence from the Mac and report the notes it plays.

The task reads the slot (read-only), selects it with bank select and program
change, clocks the sequencer over USB MIDI, records the MicroFreak's own MIDI
output and the Zoom H5 at the same time, then prints one JSON report that
places MIDI-out notes and audio-detected pitches on the same step grid.

Global settings it needs (Clock Source, Arp/Seq MIDI Out, MIDI Output
Destination) are changed only when they are off, read back after each change,
and restored afterwards. The slot is reselected at the end, which discards
analysis CCs, and the sequencer is left stopped.
"""
import argparse
import datetime as dt
import hashlib
import json
import math
import os
import sys
import time
from pathlib import Path

import download
import parameters
import semantics
import sequence
import sequence_midi

GLOBAL_PREFIX = [0xF0, 0x00, 0x20, 0x6B, 0x07]
REQUEST_PREFIX = GLOBAL_PREFIX + [0x01]
# Global setting codes and values from Freakout's MIDI Control Center command
# table (src/minifreak_patch/microfreak_midi.py, microfreak_global_specs.py).
CLOCK_SOURCE, NOTES_OUT, OUTPUT_DEST, CHANNEL_IN = 0x2E, 0x2B, 0x25, 0x20
GLOBAL_NAMES = {CLOCK_SOURCE: 'clock.source', NOTES_OUT: 'midi.arp_seq_notes_out',
                OUTPUT_DEST: 'midi.output_destination', CHANNEL_IN: 'midi.channel_in'}
CLOCK_SOURCES = ('Internal', 'USB', 'MIDI', 'Clock', 'Auto')
OUTPUT_DESTINATIONS = {0: 'None', 1: 'USB', 4: 'MIDI', 5: 'Both'}
# The stored Arp.Div index sets the clocks per step (sequence.DIVISIONS). At play
# time CC 92 = index * 127 / 10 overrides it: 0, 64, 89 and 100 gave 96, 12, 6
# and 4 clocks per step on hardware.
DIVISIONS, DIVISION_CLOCKS = sequence.DIVISIONS, sequence.DIVISION_CLOCKS
RATE_SYNC_CC = 92
# Basic Waves square wave, no sub-oscillator, Spice or Glide, open filter
# without resonance, instant attack, full sustain and the shortest release.
PLAIN_CCS = ((9, 10), (10, 0), (12, 64), (13, 0), (2, 0), (5, 0),
             (23, 127), (83, 0), (105, 0), (29, 127), (106, 0))
PLAIN_LABELS = {9: 'Oscillator Type', 10: 'Oscillator Wave', 12: 'Oscillator Timbre',
                13: 'Oscillator Shape', 2: 'Spice', 5: 'Glide', 23: 'Filter Cutoff',
                83: 'Filter Resonance', 105: 'Envelope Attack', 29: 'Envelope Sustain',
                106: 'Envelope Decay', 92: 'ARP/SEQ rate (sync)'}
REPO_ROOT = Path(__file__).resolve().parents[3]


class AuditionError(RuntimeError):
    pass


def read_global(midi_in, midi_out, code, timeout=2.0):
    """Read one global setting with operation 0x43; the reply family is 07 7F."""
    while midi_in.get_message():
        pass
    midi_out.send_message(REQUEST_PREFIX + [0, 1, 0x43, code, 0xF7])
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        received = midi_in.get_message()
        if received:
            message = received[0]
            if (message[:5] == GLOBAL_PREFIX and len(message) == 12
                    and message[7:10] == [0x02, 0x42, code]):
                return message[10]
            continue
        time.sleep(0.002)
    raise AuditionError(f'No reply reading global {GLOBAL_NAMES.get(code, hex(code))}')


def write_global(midi_in, midi_out, code, value):
    """Set one global with operation 0x42, then read it back."""
    midi_out.send_message(REQUEST_PREFIX + [0, 2, 0x42, code, value, 0xF7])
    time.sleep(0.05)
    readback = read_global(midi_in, midi_out, code)
    if readback != value:
        raise AuditionError(f'{GLOBAL_NAMES[code]} read back {readback} after writing {value}')


def plan_globals(current, want_midi_out):
    """Return the temporary global changes playback needs, as (code, value) pairs."""
    changes = []
    if current[CLOCK_SOURCE] not in (1, 4):
        changes.append((CLOCK_SOURCE, 1))
    if want_midi_out:
        if current[NOTES_OUT] != 1:
            changes.append((NOTES_OUT, 1))
        if current[OUTPUT_DEST] not in (1, 5):
            changes.append((OUTPUT_DEST, 5))
    return changes


def input_channel(value):
    if value == 126:
        raise AuditionError('MIDI Input Chan is None; the MicroFreak ignores all MIDI notes and CCs')
    return 0 if value == 127 else value


def select_slot(midi_out, slot, channel):
    bank, program = divmod(slot - 1, 128)
    midi_out.send_message([0xB0 | channel, 0, bank])
    midi_out.send_message([0xC0 | channel, program])
    return bank, program


def preset_summary(header_meta, data):
    fields = parameters.parse_parameters(data)['fields']
    values = {f['name']: f['value'] for f in semantics.interpret_fields(fields)['fields']}
    division = values.get('Arp.Div')
    return {
        'name': header_meta['name'], 'category': header_meta['category'],
        'data_sha256': hashlib.sha256(data).hexdigest(),
        'seq_length': values.get('Seq.Length'),
        'gate_length': values.get('Seq.GateLen'),
        'arp_enable': values.get('Arp.Enable'),
        'seq_on': values.get('Arp.SeqOn'),
        'arp_div': division,
        'division': DIVISIONS[division] if isinstance(division, int) and 0 <= division < len(DIVISIONS) else None,
        'paraphonic': values.get('Gen.Parafon'),
    }


def choose_timing(preset, args):
    """Clocks per step and the evidence for it."""
    if args.division:
        index = DIVISIONS.index(args.division)
        return DIVISION_CLOCKS[index], f'--division {args.division} sent as CC 92', index
    if args.clocks_per_step:
        return args.clocks_per_step, '--clocks-per-step', None
    index = preset['arp_div']
    if isinstance(index, int) and 0 <= index < len(DIVISION_CLOCKS):
        return DIVISION_CLOCKS[index], f'Arp.Div {index} ({DIVISIONS[index]}) stored in the slot', None
    return 6, 'default 1/16', None


class Recorder:
    """Collect one input channel of an audio device in the background."""

    def __init__(self, device, channel, samplerate):
        import numpy
        import sounddevice
        self.np, self.sd = numpy, sounddevice
        self.device, self.channel, self.samplerate = device, channel, samplerate
        self.blocks, self.first_adc, self.status_flags = [], None, set()

    def _callback(self, indata, frames, time_info, status):
        if status:
            self.status_flags.add(str(status))
        if self.first_adc is None:
            self.first_adc = time_info.inputBufferAdcTime
        self.blocks.append(indata[:, self.channel].copy())

    def __enter__(self):
        self.stream = self.sd.InputStream(device=self.device, channels=self.channel + 1,
                                          samplerate=self.samplerate, dtype='float32',
                                          callback=self._callback)
        self.stream.start()
        # Pair the stream clock with perf_counter so host events map to samples.
        before = time.perf_counter()
        stream_time = self.stream.time
        self.offset = stream_time - (before + time.perf_counter()) / 2
        return self

    def __exit__(self, *exc):
        self.stream.stop()
        self.stream.close()

    def seconds_for(self, host_time):
        """Position in the recording, in seconds, of a perf_counter time."""
        return host_time + self.offset - self.first_adc

    def audio(self):
        return self.np.concatenate(self.blocks) if self.blocks else self.np.zeros(0, 'float32')


def play(midi_in, midi_out, clocks, bpm, settle):
    """Send Start and `clocks` Clocks at `bpm`, then Stop; return events and clock times."""
    interval = 60.0 / bpm / 24
    events, clock_times = [], []
    while midi_in.get_message():
        pass
    sent = 0

    def drain(t0):
        while True:
            received = midi_in.get_message()
            if not received:
                return
            events.append({'t': round(time.perf_counter() - t0, 5), 'host_clocks': sent,
                           'data': received[0]})

    start = time.perf_counter()
    midi_out.send_message([0xFA])
    try:
        for index in range(clocks):
            due = start + index * interval
            while time.perf_counter() < due:
                drain(start)
                time.sleep(0.0004)
            midi_out.send_message([0xF8])
            clock_times.append(time.perf_counter())
            sent += 1
            drain(start)
    finally:
        midi_out.send_message([0xFC])
    stop = time.perf_counter()
    while time.perf_counter() < stop + settle:
        drain(start)
        time.sleep(0.001)
    return start, events, clock_times


def write_wav(path, samples, samplerate):
    import wave
    import numpy as np
    ints = np.clip(np.round(np.asarray(samples, np.float64) * 8388607), -8388608, 8388607).astype('<i4')
    with wave.open(str(path), 'wb') as output:
        output.setnchannels(1)
        output.setsampwidth(3)
        output.setframerate(samplerate)
        output.writeframes(ints.view(np.uint8).reshape(-1, 4)[:, :3].tobytes())


def analyse_audio(recorder, rows, step_starts_host, step_seconds):
    import numpy as np
    import audio_steps
    audio = recorder.audio().astype(np.float64)
    sr = recorder.samplerate
    peak = float(np.abs(audio).max()) if audio.size else 0.0
    if not audio.size or peak == 0 or recorder.first_adc is None:
        return {'peak': peak, 'seconds': len(audio) / sr, 'error': 'no audio captured'}, [None] * len(rows)
    normalized = audio / peak
    starts = [recorder.seconds_for(t) for t in step_starts_host]
    noise = normalized[:max(1, int((starts[0] - 0.05) * sr))]
    noise_rms = float(np.sqrt(np.mean(noise ** 2))) if noise.size else 1e-6
    times, flux = audio_steps.onset_envelope(normalized, sr)
    triggers = [s for s, row in zip(starts, rows) if row['midi']['notes']] or starts
    search = min(0.06, 0.45 * step_seconds)
    lag = audio_steps.estimate_lag(times, flux, triggers, search)
    threshold = audio_steps.onset_threshold(flux)
    results = audio_steps.analyse_steps(normalized, sr, [s + lag for s in starts], step_seconds,
                                        noise_rms, threshold, times, flux)
    info = {'peak': round(peak, 4), 'seconds': round(len(audio) / sr, 3),
            'noise_floor_db_re_peak': round(20 * math.log10(max(noise_rms, 1e-9)), 1),
            'latency_ms': round(lag * 1000, 1), 'onset_threshold': round(threshold, 2)}
    if recorder.status_flags:
        info['stream_status'] = sorted(recorder.status_flags)
    return info, results


def guard_wav_dir(path):
    resolved = path.expanduser().resolve()
    if resolved == REPO_ROOT or REPO_ROOT in resolved.parents:
        raise AuditionError(f'--wav-dir must be outside the repository: {resolved}')
    resolved.mkdir(parents=True, exist_ok=True)
    return resolved


def parse_cc(text):
    try:
        number, value = (int(part) for part in text.split('='))
    except ValueError as exc:
        raise argparse.ArgumentTypeError('use NUMBER=VALUE, for example 23=127') from exc
    if not (0 <= number <= 119 and 0 <= value <= 127):
        raise argparse.ArgumentTypeError('CC number 0-119 and value 0-127')
    return number, value


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--slot', type=int, required=True, help='Preset slot from 1 to 512')
    parser.add_argument('--bpm', type=float, default=120.0)
    parser.add_argument('--loops', type=int, default=2)
    parser.add_argument('--steps', type=int, help='Steps per loop; default Seq.Length')
    parser.add_argument('--division', choices=DIVISIONS, help='Force the step division with CC 92')
    parser.add_argument('--clocks-per-step', type=int)
    parser.add_argument('--plain', action='store_true', help='Send CCs for a simple, analysable timbre')
    parser.add_argument('--cc', type=parse_cc, action='append', default=[], metavar='N=V')
    parser.add_argument('--no-midi-out', action='store_true',
                        help='Leave Arp/Seq MIDI Out as it is; audio only')
    parser.add_argument('--no-audio', action='store_true', help='Skip the H5 recording')
    parser.add_argument('--no-select', action='store_true',
                        help='Play the sound and pattern already loaded, such as pattern B '
                             'chosen on the panel; sends no program change or CC')
    parser.add_argument('--device', default='H5')
    parser.add_argument('--input-channel', type=int, default=2, help='Zero-based audio input channel')
    parser.add_argument('--samplerate', type=int, default=48000)
    parser.add_argument('--wav-dir', type=Path,
                        default=Path(os.environ.get('TMPDIR', '/tmp')) / 'microfreak-audition')
    parser.add_argument('--output', type=Path, help='Also write the JSON report here')
    parser.add_argument('--port', help='Exact MIDI port name')
    return parser


def run(args):
    if not 1 <= args.slot <= 512:
        raise AuditionError('Slot must be from 1 to 512')
    if args.loops < 1 or (args.steps is not None and not 1 <= args.steps <= 64):
        raise AuditionError('--loops must be positive and --steps 1-64')
    if not 20 <= args.bpm <= 300:
        raise AuditionError('--bpm must be from 20 to 300')
    if args.no_select and (args.plain or args.cc or args.division):
        raise AuditionError('--no-select keeps the loaded sound; leave out --plain, --cc and --division')
    wav_dir = None if args.no_audio else guard_wav_dir(args.wav_dir)
    want_midi_out = not args.no_midi_out
    midi_in, midi_out, port = download.open_ports(args.port)
    midi_in.ignore_types(sysex=False, timing=False, active_sense=True)
    report = {'schema': 1, 'slot': args.slot,
              'captured_at': dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')}
    applied, restored = [], []
    recorder = channel = None
    try:
        header_meta, _, data = download.read_patch(midi_in, midi_out, args.slot)
        preset = preset_summary(header_meta, data)
        report.update(name=preset['name'], category=preset['category'], preset=preset)
        current = {code: read_global(midi_in, midi_out, code) for code in GLOBAL_NAMES}
        channel = input_channel(current[CHANNEL_IN])
        steps = args.steps or preset['seq_length'] or 16
        clocks_per_step, timing_source, forced_index = choose_timing(preset, args)
        for code, value in plan_globals(current, want_midi_out):
            write_global(midi_in, midi_out, code, value)
            applied.append((code, current[code], value))
        if args.no_select:
            bank = program = None
        else:
            bank, program = select_slot(midi_out, args.slot, channel)
            time.sleep(0.6)
        sent_ccs = list(PLAIN_CCS) if args.plain else []
        sent_ccs += args.cc
        if forced_index is not None:
            sent_ccs.append((RATE_SYNC_CC, round(forced_index * 127 / 10)))
        for number, value in sent_ccs:
            midi_out.send_message([0xB0 | channel, number, value])
            time.sleep(0.01)
        time.sleep(0.2)
        clocks = steps * clocks_per_step * args.loops
        if not args.no_audio:
            recorder = Recorder(args.device, args.input_channel, args.samplerate)
            with recorder:
                time.sleep(0.4)
                _, events, clock_times = play(midi_in, midi_out, clocks, args.bpm, 0.8)
        else:
            _, events, clock_times = play(midi_in, midi_out, clocks, args.bpm, 0.8)
        report['tempo'] = {'bpm': args.bpm, 'clocks_per_step': clocks_per_step,
                           'clocks_per_step_source': timing_source,
                           'step_ms': round(60000 / args.bpm / 24 * clocks_per_step, 2),
                           'steps_per_loop': steps, 'loops': args.loops, 'clocks_sent': len(clock_times)}
        report['instrument'] = {
            'midi_port': port, 'selection': {'bank_select_cc0': bank, 'program_change': program,
                                             'midi_channel': channel + 1},
            'globals_before': {GLOBAL_NAMES[c]: v for c, v in current.items()},
            'ccs_sent': [{'cc': n, 'value': v, 'label': PLAIN_LABELS.get(n)} for n, v in sent_ccs],
        }
        built = sequence_midi.build_steps(events, clocks_per_step, steps, args.loops)
        rows = built['rows']
        note_messages = sum(1 for e in events if e['data'][0] & 0xF0 in (0x80, 0x90))
        report['midi_out'] = {
            'arp_seq_midi_out_on': want_midi_out or current[NOTES_OUT] == 1,
            'transmits_sequence': built['note_count'] > 0,
            'notes': built['note_count'], 'note_messages': note_messages,
            'notes_after_last_step': built['notes_after_last_step'],
            'off_grid_notes': built['off_grid_notes'],
            'cc_numbers': built['cc_numbers'], 'clock_reference': built['clock_reference'],
            'clock_echoes': sum(1 for e in events if e['data'] == [0xF8]),
            'loop_differences': sequence_midi.loop_differences(rows),
        }
        if recorder is not None:
            step_starts = [clock_times[i * clocks_per_step] for i in range(len(rows))]
            info, results = analyse_audio(recorder, rows, step_starts,
                                          60 / args.bpm / 24 * clocks_per_step)
            stamp = dt.datetime.now().strftime('%Y%m%d-%H%M%S')
            wav = wav_dir / f'slot-{args.slot:03d}-{stamp}.wav'
            write_wav(wav, recorder.audio(), args.samplerate)
            report['recording'] = {'wav': str(wav), 'device': args.device,
                                   'input_channel_index': args.input_channel,
                                   'samplerate': args.samplerate, **info}
            for row, audio in zip(rows, results):
                row['audio'] = audio
                if built['note_count']:
                    row['agreement'] = sequence_midi.classify(row['midi'], audio)
                    recall = sequence_midi.chord_recall(row['midi'], audio)
                    if recall and len(row['midi']['notes']) > 1:
                        row['chord_recall'] = recall
        warnings = []
        if preset['seq_on'] != 1:
            warnings.append('The slot does not store Seq mode (Arp.SeqOn is not 1)')
        if built['off_grid_notes']:
            warnings.append(f"{built['off_grid_notes']} note-ons fall between steps; "
                            'the step division may differ from clocks_per_step')
        overridden = sorted({n for n, _ in sent_ccs} & set(built['cc_numbers']))
        if overridden:
            warnings.append('The pattern\'s modulation tracks send CC '
                            + ', '.join(map(str, overridden))
                            + ' during playback, replacing the values sent before Start')
        if want_midi_out and not built['note_count']:
            warnings.append('No notes on MIDI out: pattern A may be empty')
        report['warnings'] = warnings
        report['steps'] = rows
        report['summary'] = sequence_midi.summarize(rows)
    finally:
        midi_out.send_message([0xFC])
        try:
            if channel is not None:
                midi_out.send_message([0xB0 | channel, 123, 0])
                if not args.no_select:
                    select_slot(midi_out, args.slot, channel)
                    time.sleep(0.3)
            failed = []
            for code, before, temporary in reversed(applied):
                try:
                    write_global(midi_in, midi_out, code, before)
                except AuditionError:
                    failed.append(f'{GLOBAL_NAMES[code]} (was {before})')
                    continue
                restored.append({'setting': GLOBAL_NAMES[code], 'value': before,
                                 'temporary_value': temporary, 'restored': True})
            if failed:
                raise AuditionError('Could not restore ' + ', '.join(failed)
                                    + '; set them in Utility or MIDI Control Center')
        finally:
            midi_in.close_port()
            midi_out.close_port()
    report.setdefault('instrument', {})
    report['instrument']['globals_changed'] = restored
    report['instrument']['left_stopped'] = True
    report['instrument']['slot_reselected'] = not args.no_select
    return report


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        report = run(args)
    except (AuditionError, OSError, ValueError, RuntimeError) as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 1
    text = json.dumps(report, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + '\n')
    print(text)
    return 0


if __name__ == '__main__':
    sys.exit(main())
