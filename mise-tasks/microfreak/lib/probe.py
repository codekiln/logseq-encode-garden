#!/usr/bin/env python3
"""Write named settings into a MicroFreak slot, play a MIDI script, and measure it.

The base is a slot, read without changing it, or a file saved by
microfreak:download. Each --set changes one stored field. With --slot the
result goes through microfreak:upload (a slot holding a preset is saved to
--backup-dir first) and the slot is selected. The task then plays a short
script of notes, pitch bend, CCs and channel pressure over USB MIDI while it
records the Zoom H5, and prints one JSON report: what changed, what was played,
and the recording measured every 10 ms (level in dBFS, pitch, spectral
centroid) with a summary per note.
"""
import argparse
import hashlib
import json
import math
import sys
import time
from pathlib import Path

import parameters
import sequence as Q

FRAME_HOP = 0.01
PITCH_WINDOW = 4096
LEVEL_WINDOW = 1024
SILENCE_DB = -70.0
REPO_ROOT = Path(__file__).resolve().parents[3]


class ProbeError(RuntimeError):
    pass


# ---------------------------------------------------------------- settings

def parse_set(text):
    """Split NAME=VALUE. VALUE is an integer choice, a decimal, or raw:N."""
    name, sep, value = text.partition('=')
    name, value = name.strip(), value.strip()
    if not sep or not name or not value:
        raise ValueError(f'--set takes NAME=VALUE, such as VCO.BendRng=2: {text!r}')
    if value.lower().startswith('raw:'):
        raw = int(value[4:], 0)
        if not 0 <= raw <= 0xFFFF:
            raise ValueError(f'{name}: raw values run from 0 to 65535')
        return name, ('raw', raw)
    if any(c in value for c in '.eE') and not value.lower().startswith('0x'):
        return name, ('decimal', float(value))
    return name, ('choice', int(value, 0))


def raw_for(field, spec):
    """The stored 16-bit value a setting spec means for one parsed field.

    A choice field (descriptor 1-127) stores index * 32767 / descriptor, as
    every saved preset examined does. A decimal is a normalized value: 0 to 1,
    or -1 to 1 for the matrix amounts, which store a signed value.
    """
    kind, value = spec
    descriptor = field['descriptor']
    name = field['name']
    if kind == 'raw':
        return value
    if kind == 'choice':
        if not 1 <= descriptor <= 127:
            raise ValueError(f'{name} is not a choice field (descriptor {descriptor}); '
                             'give a decimal or raw:N')
        if not 0 <= value <= descriptor:
            raise ValueError(f'{name} takes a choice from 0 to {descriptor}')
        return round(value * 32767 / descriptor)
    group, _, short = name.partition('.')
    if group.startswith('Co') and short in ('EG1', 'EG2', 'LFO', 'Xpr', 'Key'):
        if not -1 <= value <= 1:
            raise ValueError(f'{name} takes a decimal from -1 to 1')
        return round(value * 32767) & 0xFFFF
    if not 0 <= value <= 1:
        raise ValueError(f'{name} takes a decimal from 0 to 1')
    return round(value * 32767)


def apply_settings(payload, settings):
    """Return the new payload and {name: [before, after]} for each changed field."""
    fields = {f['name']: f for f in parameters.parse_parameters(payload)['fields']}
    data = bytearray(parameters.unpack_payload(payload))
    changed = {}
    for name, spec in settings:
        field = fields.get(name)
        if field is None:
            raise ValueError(f'The base preset has no {name} field; '
                             f'choose a base saved on firmware 5, such as slot 359')
        value = raw_for(field, spec)
        before = field['value_le_unsigned']
        Q.set_field(data, fields, name, value)
        if before != value:
            changed[name] = [before, value]
    return Q.pack_payload(bytes(data)), changed


# ------------------------------------------------------------------ script

def note_number(value):
    return value if isinstance(value, int) else Q.note_number(str(value))


def load_script(path):
    text = Path(path).read_text()
    if Path(path).suffix.lower() in ('.yaml', '.yml'):
        import yaml
        script = yaml.safe_load(text)
    else:
        script = json.loads(text)
    if isinstance(script, list):
        script = {'events': script}
    return script


def simple_script(note, velocity, hold, tail):
    return {'events': [{'t': 0.0, 'on': note, 'velocity': velocity},
                       {'t': hold, 'off': note}], 'tail': tail}


def compile_script(script, channel):
    """Turn a script into time-ordered (seconds, [MIDI bytes], label) tuples.

    Events: {'t': s, 'on': note, 'velocity': v}, {'t': s, 'off': note},
    {'t': s, 'bend': -1..1}, {'t': s, 'cc': [number, value]},
    {'t': s, 'pressure': 0-127}, {'t': s, 'poly_pressure': [note, value]}.
    A ramp repeats bend, cc or pressure from its value to 'to' over 'over'
    seconds in 'steps' steps.
    """
    out = []

    def bend_bytes(amount):
        value = max(0, min(16383, round(8192 + amount * (8191 if amount > 0 else 8192))))
        return [0xE0 | channel, value & 0x7F, value >> 7]

    for event in script.get('events', []):
        t = float(event['t'])
        if 'on' in event:
            note = note_number(event['on'])
            velocity = int(event.get('velocity', 100))
            out.append((t, [0x90 | channel, note, velocity], f"on {Q.note_name(note)}/{velocity}"))
        elif 'off' in event:
            note = note_number(event['off'])
            out.append((t, [0x80 | channel, note, 0], f'off {Q.note_name(note)}'))
        elif 'bend' in event or 'cc' in event or 'pressure' in event:
            if 'bend' in event:
                start, make, label = float(event['bend']), bend_bytes, 'bend'
            elif 'cc' in event:
                number, start = int(event['cc'][0]), int(event['cc'][1])
                make = (lambda n: lambda v: [0xB0 | channel, n, int(round(v))])(number)
                label = f'cc {number}'
            else:
                start = int(event['pressure'])
                make, label = (lambda v: [0xD0 | channel, int(round(v))]), 'pressure'
            if 'to' in event:
                end, over = float(event['to']), float(event['over'])
                steps = int(event.get('steps', max(2, int(over / 0.01))))
                for i in range(steps + 1):
                    value = start + (end - start) * i / steps
                    out.append((t + over * i / steps, make(value), f'{label} {value:g}'))
            else:
                out.append((t, make(start), f'{label} {start:g}'))
        elif 'poly_pressure' in event:
            note, value = event['poly_pressure']
            out.append((t, [0xA0 | channel, note_number(note), int(value)], 'poly pressure'))
        else:
            raise ValueError(f'Unknown script event {event!r}')
    out.sort(key=lambda item: item[0])
    return out


def play_script(midi_out, compiled, start):
    """Send each message at its time after `start` (perf_counter); return send times."""
    sent = []
    for t, message, _ in compiled:
        due = start + t
        while True:
            now = time.perf_counter()
            if now >= due:
                break
            time.sleep(min(0.0005, due - now))
        midi_out.send_message(message)
        sent.append(time.perf_counter() - start)
    return sent


def all_notes_off(midi_out, channel):
    midi_out.send_message([0xE0 | channel, 0, 64])
    midi_out.send_message([0xD0 | channel, 0])
    midi_out.send_message([0xB0 | channel, 123, 0])


# ---------------------------------------------------------------- analysis

def frames(audio, sr, hop=FRAME_HOP, fmin=30.0, fmax=2500.0):
    """Measure the recording every `hop` seconds: level, pitch and centroid."""
    import numpy as np
    import audio_steps
    audio = np.asarray(audio, dtype=np.float64)
    step = int(round(hop * sr))
    rows = []
    window = np.hanning(LEVEL_WINDOW)
    freqs = np.fft.rfftfreq(LEVEL_WINDOW, 1 / sr)
    for start in range(0, max(0, len(audio) - LEVEL_WINDOW), step):
        chunk = audio[start:start + LEVEL_WINDOW]
        rms = float(np.sqrt(np.mean(chunk ** 2)))
        db = 20 * math.log10(max(rms, 1e-9))
        row = {'t': round((start + LEVEL_WINDOW / 2) / sr, 3), 'db': round(db, 2)}
        if db > SILENCE_DB:
            spectrum = np.abs(np.fft.rfft(chunk * window))
            total = spectrum.sum()
            if total > 0:
                row['centroid_hz'] = round(float((freqs * spectrum).sum() / total), 1)
            centre = start + LEVEL_WINDOW // 2
            lo = max(0, centre - PITCH_WINDOW // 2)
            segment = audio[lo:lo + PITCH_WINDOW]
            if len(segment) == PITCH_WINDOW:
                f0, aperiodicity = audio_steps.yin(segment, sr, fmin=fmin, fmax=fmax)
                if f0:
                    row['f0_hz'] = round(f0, 2)
                    row['midi'] = round(audio_steps.hz_to_midi(f0), 3)
                    row['aperiodicity'] = round(aperiodicity, 3)
        rows.append(row)
    return rows


def onset_after(rows, t, rise_db=12.0, window=0.25):
    """First frame within `window` after t whose level is rise_db above the level before t.

    The level before t comes from the last frame whose window ends before t.
    """
    before = [r for r in rows if r['t'] <= t - LEVEL_WINDOW / 2 / 48000]
    floor = before[-1]['db'] if before else SILENCE_DB
    for row in rows:
        if t <= row['t'] <= t + window and row['db'] >= floor + rise_db:
            return row['t']
    return None


def summarize_notes(rows, played, compiled):
    """One summary per note-on: onset, peak, pitch statistics and centroid."""
    import numpy as np
    notes = []
    ons = [(t, m) for (t, m, _), t_sent in zip(compiled, played) if (m[0] & 0xF0) == 0x90 and m[2]]
    times = [t for t, _ in ons]
    for index, (t, message) in enumerate(ons):
        note = message[1]
        off = next((ct for ct, m, _ in compiled
                    if ct > t and (m[0] & 0xF0) in (0x80, 0x90) and m[1] == note
                    and ((m[0] & 0xF0) == 0x80 or m[2] == 0)), None)
        nxt = times[index + 1] if index + 1 < len(times) else None
        end = min(x for x in (off, nxt, rows[-1]['t'] if rows else t) if x is not None)
        span = [r for r in rows if t <= r['t'] <= end]
        summary = {'note': Q.note_name(note), 'velocity': message[2], 't': round(t, 3),
                   'until': round(end, 3)}
        if not span:
            notes.append(summary)
            continue
        onset = onset_after(rows, t)
        peak = max(span, key=lambda r: r['db'])
        summary.update(onset_latency_ms=None if onset is None else round((onset - t) * 1000),
                       peak_db=peak['db'], peak_at=round(peak['t'] - t, 3),
                       end_db=span[-1]['db'])
        settled = [r for r in span if r['t'] >= t + 0.05 and 'midi' in r]
        if settled:
            pitches = np.array([r['midi'] for r in settled])
            summary.update(pitch=Q.note_name(int(round(float(np.median(pitches))))),
                           midi_median=round(float(np.median(pitches)), 3),
                           cents_from_note=round(float(np.median(pitches) - note) * 100, 1),
                           midi_min=round(float(pitches.min()), 3),
                           midi_max=round(float(pitches.max()), 3))
        centroids = [r['centroid_hz'] for r in span if 'centroid_hz' in r]
        if centroids:
            summary['centroid_hz_median'] = round(float(np.median(centroids)), 1)
        notes.append(summary)
    return notes


# --------------------------------------------------------------------- run

def guard_outside_repo(path, flag):
    resolved = Path(path).expanduser().resolve()
    if resolved == REPO_ROOT or REPO_ROOT in resolved.parents:
        raise ProbeError(f'{flag} must be outside the repository: {resolved}')
    return resolved


def build_parser():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--base', help='Slot number to read, or a .bin from microfreak:download')
    p.add_argument('--slot', type=int, help='Slot to write the result to and play')
    p.add_argument('--set', action='append', default=[], metavar='NAME=VALUE',
                   help='Stored field to change: an integer choice, a decimal, or raw:N')
    p.add_argument('--backup-dir', help='Save the slot in a new timestamped folder here first when it holds a preset')
    p.add_argument('--name', help='Preset name to store; default Probe')
    p.add_argument('--script', help='YAML or JSON script of MIDI events')
    p.add_argument('--note', default='C4', help='Note for the default script; default C4')
    p.add_argument('--velocity', type=int, default=100)
    p.add_argument('--hold', type=float, default=1.5, help='Seconds the default note is held')
    p.add_argument('--tail', type=float, help='Seconds recorded after the last event; default 1')
    p.add_argument('--no-write', action='store_true', help='Play --slot as it is')
    p.add_argument('--no-play', action='store_true', help='Write only')
    p.add_argument('--settle', type=float, default=0.4, help='Seconds between selecting and playing')
    p.add_argument('--device', default='H5')
    p.add_argument('--input-channel', type=int, default=2)
    p.add_argument('--samplerate', type=int, default=48000)
    p.add_argument('--wav-dir', help='Save the recording here, outside the repository')
    p.add_argument('--output', help='Also write the full report here')
    p.add_argument('--frames', action='store_true', help='Print every 10 ms frame, not only note summaries')
    p.add_argument('--port', help='Exact MIDI port name')
    return p


def write_slot(midi_in, midi_out, args, settings):
    import download
    import upload
    import sequence_write as W
    slot = W.base_slot(args.base) if args.base is not None else None
    if args.base is None:
        raise ProbeError('Give --base: a slot number or a microfreak:download file')
    if slot is not None:
        header, data, _ = W.read_base_slot(midi_in, midi_out, slot)
    else:
        header, data = W.load_base_file(args.base)
    new, changed = apply_settings(data, settings)
    result = {'base': str(args.base), 'settings_changed': changed,
              'data_sha256': hashlib.sha256(new).hexdigest()}
    if args.slot:
        header = upload.build_header(header, args.slot, name=args.name or 'Probe')
        backup_dir = None
        if args.backup_dir:
            # One folder per run, so the same test slot can be probed again and again.
            backup_dir = Path(args.backup_dir).expanduser() / time.strftime('%Y%m%d-%H%M%S')
        done = upload.upload(midi_in, midi_out, args.slot, header, new,
                             backup_dir=backup_dir, device='')
        result['upload'] = {'slot': args.slot, 'was': done['before'].get('name'),
                            'backup': str(done['backup']) if 'backup' in done else None,
                            'read_back_matches': True}
    return result


def run(args):
    import audition
    import download
    settings = [parse_set(text) for text in args.set]
    if args.wav_dir:
        guard_outside_repo(args.wav_dir, '--wav-dir')
    if args.output:
        guard_outside_repo(args.output, '--output')
    if args.backup_dir:
        guard_outside_repo(args.backup_dir, '--backup-dir')
    script = load_script(args.script) if args.script else simple_script(
        args.note, args.velocity, args.hold, 1.0)
    midi_in, midi_out, port = download.open_ports(args.port)
    report = {'port': port}
    try:
        channel = audition.input_channel(audition.read_global(midi_in, midi_out, audition.CHANNEL_IN))
        report['midi_channel'] = channel + 1
        if not args.no_write:
            report.update(write_slot(midi_in, midi_out, args, settings))
        elif settings:
            raise ProbeError('--set needs a write; drop --no-write')
        if args.no_play:
            return report
        if not args.slot:
            raise ProbeError('Give --slot to play')
        audition.select_slot(midi_out, args.slot, channel)
        time.sleep(args.settle)
        compiled = compile_script(script, channel)
        tail = args.tail if args.tail is not None else float(script.get('tail', 1.0))
        recorder = audition.Recorder(args.device, args.input_channel, args.samplerate)
        with recorder:
            time.sleep(0.3)
            start = time.perf_counter()
            played = play_script(midi_out, compiled, start)
            end = start + (compiled[-1][0] if compiled else 0) + tail
            while time.perf_counter() < end:
                time.sleep(0.005)
            all_notes_off(midi_out, channel)
            time.sleep(0.05)
        audio = recorder.audio()
        origin = recorder.seconds_for(start)
        sr = args.samplerate
        import numpy as np
        trimmed = np.asarray(audio[max(0, int(origin * sr)):], dtype=np.float64)
        rows = frames(trimmed, sr)
        report['played'] = [{'t': round(t, 3), 'event': label}
                            for (_, _, label), t in zip(compiled, played)]
        report['audio'] = {'device': args.device, 'input_channel_index': args.input_channel,
                           'seconds': round(len(trimmed) / sr, 3),
                           'peak_dbfs': round(20 * math.log10(max(float(np.abs(trimmed).max()), 1e-9)), 2)
                           if len(trimmed) else None}
        if recorder.status_flags:
            report['audio']['stream_status'] = sorted(recorder.status_flags)
        report['notes'] = summarize_notes(rows, played, compiled)
        report['frames'] = rows
        if args.wav_dir:
            wav_dir = Path(args.wav_dir).expanduser()
            wav_dir.mkdir(parents=True, exist_ok=True)
            stamp = time.strftime('%Y%m%d-%H%M%S')
            wav = wav_dir / f'probe-slot{args.slot:03d}-{stamp}.wav'
            audition.write_wav(wav, trimmed, sr)
            report['audio']['wav'] = str(wav)
        return report
    finally:
        midi_in.close_port()
        midi_out.close_port()


def main(argv=None):
    args = build_parser().parse_args(argv)
    try:
        report = run(args)
    except (ProbeError, ValueError, OSError, RuntimeError) as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 1
    if args.output:
        Path(args.output).expanduser().write_text(json.dumps(report, indent=1))
    shown = report if args.frames else {k: v for k, v in report.items() if k != 'frames'}
    print(json.dumps(shown, indent=1))
    return 0


if __name__ == '__main__':
    sys.exit(main())
