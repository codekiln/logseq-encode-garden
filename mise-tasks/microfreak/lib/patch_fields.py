#!/usr/bin/env python3
"""Convert stored MicroFreak preset fields to the panel's values and back.

Each conversion here was measured on a MicroFreak (firmware 5) by writing
values into a test slot with microfreak:probe, playing it over USB MIDI and
recording it with the Zoom H5. The garden page Microfreak/Patch/Storage lists
the conversions and Microfreak/Patch/Research the runs behind them. A field
missing here has no measured conversion yet.

`display(name, raw, descriptor, context)` reads a stored value. `setting(name,
value)` returns what microfreak:probe's apply_settings stores for a panel value:
('choice', n), ('decimal', x) or ('raw', n).
"""
import math

EVIDENCE = 'https://github.com/codekiln/logseq-encode-garden/blob/main/pages/Microfreak___Patch___Storage.md'
FULL = 32767

GLIDE_MODES = ('Time', 'Sync', 'Rate')
# Sync glide length by floor(10 x stored Glide). Below 3 the glide was too
# short to measure at 30 BPM.
SYNC_GLIDE = {3: '1/32', 4: '1/16T', 5: '1/16', 6: '1/8T', 7: '1/8', 8: '1/4T', 9: '1/4', 10: '1/2'}
SYNC_GLIDE_BEATS = {'1/32': 1 / 8, '1/16T': 1 / 6, '1/16': 1 / 4, '1/8T': 1 / 3, '1/8': 1 / 2,
                    '1/4T': 2 / 3, '1/4': 1, '1/2': 2}
PARAPHONIC_MODES = {0: 'Paraphonic', 2: 'Chord', 3: 'Unison'}
# Choice fields whose every stored choice was played and told apart.
CHOICES = {
    'EG2.Legato': ('Off', 'On'),
    'EG2.Snap': ('Off', 'On'),
    'LFO.Retrig': ('Off', 'On', 'Legato'),
    'Kbd.Veloc': ('Aftertouch', 'Velocity'),
    'Mat.KyMdSrc': ('Linear', 'Random'),
    'Kbd.Scale': ('Global', 'Off', 'Major', 'Minor', 'Harmonic Minor', 'Dorian', 'Mixolydian',
                  'Blues', 'Pentatonic'),
    'Kbd.Root': ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'),
    'VCF.Type': ('LPF', 'BPF', 'HPF'),
    'LFO.Shape': ('Sine', 'Triangle', 'Saw', 'Square', 'Random Stepped', 'Random Gliding'),
    'EG1.Mode': ('Env', 'Run', 'Loop'),
    'EG2.Mode': ('Off', 'On'),
    'Kbd.Octave': ('-3', '-2', '-1', '0', '+1', '+2', '+3'),
    'LFO.Sync': ('Off', 'On'),
    'Arp.Dir': ('Up', 'Order', 'Random', 'Pattern'),
    'Arp.Enable': ('Off', 'On'),
    'LFO.Div': ('8 bars', '4 bars', '2 bars', '1 bar', '1/2', '1/2T', '1/4', '1/4T', '1/8', '1/8T',
                '1/16', '1/16T', '1/32'),
}
# Envelope times on slot 359's Basic Waves sound, seconds:
# attack to 90 % of full level, decay with sustain 0 to 20 dB down,
# release after the note ends with sustain 1 to 20 dB down.
ATTACK_POINTS = ((0.1, 0.031), (0.2, 0.061), (0.3, 0.141), (0.4, 0.291), (0.5, 0.561),
                 (0.6, 1.031), (0.7, 1.801))
DECAY_POINTS = ((0.1, 0.11), (0.2, 0.27), (0.3, 0.49), (0.4, 0.78), (0.5, 1.17), (0.6, 1.71),
                (0.7, 2.5))
RELEASE_POINTS = ((0.1, 0.071), (0.2, 0.181), (0.3, 0.341), (0.4, 0.581), (0.5, 0.921))
# Low-pass cutoff, Hz at -3 dB, from a sawtooth's harmonics with resonance 0.
CUTOFF_POINTS = ((0.3, 140), (0.4, 300), (0.5, 580), (0.6, 1240), (0.7, 2720), (0.8, 6460))
# Free-running LFO rate (LFO.Sync off): stored value and the vibrato rate heard.
LFO_RATE_POINTS = ((0.1, 0.143), (0.2, 0.239), (0.3, 0.521), (0.4, 1.074), (0.5, 2.246),
                   (0.6, 4.785), (0.7, 10.254), (0.75, 14.974), (0.8, 21.908), (0.85, 32.0),
                   (0.9, 46.8), (0.95, 68.5), (1.0, 100.1))
# Low-pass resonance: peak above the passband, dB, at cutoff 0.5.
RESONANCE_POINTS = ((0.0, 0.0), (0.2, 0.3), (0.4, 1.7), (0.5, 2.9), (0.6, 4.3), (0.7, 6.5), (0.8, 9.4),
                    (0.9, 15.3), (1.0, 26.5))


def cycling_stage_seconds(stored):
    """Rise or Fall of the Cycling Envelope with a linear shape: 10 s x stored cubed."""
    return 10 * stored ** 3


def cycling_stage_stored(seconds):
    if not 0 <= seconds <= 10:
        raise ValueError('A Cycling Envelope stage runs from 0 to 10 seconds')
    return (seconds / 10) ** (1 / 3)


def cycling_hold_seconds(stored):
    """Hold of the Cycling Envelope in Run and Loop: 10 s x stored squared."""
    return 10 * stored ** 2


def cycling_hold_stored(seconds):
    if not 0 <= seconds <= 10:
        raise ValueError('The Cycling Envelope hold runs from 0 to 10 seconds')
    return math.sqrt(seconds / 10)


def resonance_peak_db(stored):
    for (x0, y0), (x1, y1) in zip(RESONANCE_POINTS, RESONANCE_POINTS[1:]):
        if x0 <= stored <= x1:
            return y0 + (stored - x0) / (x1 - x0) * (y1 - y0)
    return None


def _log_interp(x, points):
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        if x0 <= x <= x1:
            return math.exp(math.log(y0) + (x - x0) / (x1 - x0) * (math.log(y1) - math.log(y0)))
    return None


def value_for(target, points, label, unit):
    """The stored value whose measured result is `target`, between measured points."""
    ys = [y for _, y in points]
    if not min(ys) <= target <= max(ys):
        raise ValueError(f'{label} from {min(ys)} to {max(ys)} {unit} were measured; '
                         f'give a 0-1 value outside them')
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        if y0 <= target <= y1:
            return x0 + (math.log(target) - math.log(y0)) / (math.log(y1) - math.log(y0)) * (x1 - x0)


def measured(stored, points):
    return _log_interp(stored, points)


def lfo_hz(stored):
    """The free LFO rate in Hz between the measured points, else None."""
    return _log_interp(stored, LFO_RATE_POINTS)


def lfo_stored(hz):
    low, high = LFO_RATE_POINTS[0][1], LFO_RATE_POINTS[-1][1]
    if not low <= hz <= high:
        raise ValueError(f'LFO rates from {low} to {high} Hz were measured; give rate (0-1) outside them')
    for (x0, y0), (x1, y1) in zip(LFO_RATE_POINTS, LFO_RATE_POINTS[1:]):
        if y0 <= hz <= y1:
            return x0 + (math.log(hz) - math.log(y0)) / (math.log(y1) - math.log(y0)) * (x1 - x0)
LABELS = {'EG2.Legato': 'Envelope Legato', 'EG2.Snap': 'Envelope Snap', 'LFO.Retrig': 'LFO Retrig',
          'Kbd.Veloc': 'Press Mode', 'Mat.KyMdSrc': 'Key/Arp Mode', 'Kbd.Scale': 'Scale',
          'Kbd.Root': 'Root Note', 'VCF.Type': 'Filter Type', 'LFO.Shape': 'LFO Shape',
          'EG1.Mode': 'Cycling Envelope Mode', 'EG2.Mode': 'Amp Mod', 'Kbd.Octave': 'Keyboard Octave',
          'LFO.Sync': 'LFO Sync', 'Arp.Dir': 'Arp direction', 'Arp.Enable': 'Arpeggiator',
          'LFO.Div': 'LFO sync division'}
FLATS = {'db': 'c#', 'eb': 'd#', 'gb': 'f#', 'ab': 'g#', 'bb': 'a#'}
# Level of C4 against choice 12, measured in 0.5 dB steps. Choices 9 and 10 played alike.
PRESET_VOLUME_DB = (-5.5, -5.0, -4.5, -4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -1.0, -0.5, 0.0,
                    0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0)
CHORD_UNUSED = 0x7F80
CHORD_CENTRE = 0x4000
ARP_BPM_RANGE = (30.0, 240.0)


# The matrix: Co1-Co7 are its columns, EG1/EG2/LFO/Xpr/Key its rows (source).
MATRIX_COLUMNS = {1: 'Pitch', 2: 'Wave', 3: 'Timbre', 4: 'Cutoff', 5: 'Assign 1', 6: 'Assign 2', 7: 'Assign 3'}
MATRIX_ROWS = {'EG1': 'CycEnv', 'EG2': 'Envelope', 'LFO': 'LFO', 'Xpr': 'Pressure', 'Key': 'Key/Arp'}
PITCH_SEMITONES_PER_AMOUNT = 48
# A destination id, as Mat.Assign1-3 and the sequencer's modulation tracks store
# it, is four hex digits: a section, then a field within it.
DESTINATION_SECTIONS = {'VCO': 0x00, 'VCF': 0x01, 'EG1': 0x02, 'Kbd': 0x03, 'Arp': 0x04, 'LFO': 0x05,
                        'EG2': 0x06, 'Gen': 0x07, 'Mat': 0x09, 'Seq': 0x12, 'Voc': 0x13,
                        **{f'Co{n}': 0x09 + n for n in range(1, 8)}}
# Destination ids heard doing what their field does on the instrument.
HEARD_DESTINATIONS = {0x0001, 0x0003, 0x0005, 0x0101, 0x0102, 0x0300, 0x0502, 0x0602, 0x0603, 0x0705, 0x0A02}


def destination_ids():
    """{field: destination id} from Freakout's live map, one id per field."""
    import freakout_live_map
    ids = {}
    for field, addresses in freakout_live_map.MICROFREAK_STRUCTURED_LIVE_WORDS.items():
        section = DESTINATION_SECTIONS.get(field.partition('.')[0])
        match = [a for a in addresses if a >> 8 == section]
        if len(match) == 1:
            ids[field] = match[0]
    return ids


def destination_field(value):
    return {v: k for k, v in destination_ids().items()}.get(value)


def choice(raw, descriptor):
    return round(raw * descriptor / FULL)


def glide_seconds(stored):
    """Time mode: seconds for any glide. Rate mode: seconds per octave."""
    return 10 * stored ** 3


def glide_stored(seconds):
    if not 0 <= seconds <= 10:
        raise ValueError('Glide time runs from 0 to 10 seconds')
    return (seconds / 10) ** (1 / 3)


def unison_semitones(stored):
    """The detune S, in semitones, that a stored Unison spread gives."""
    return 2 * stored if stored <= 0.5 else 1 + 22 * (stored - 0.5)


def unison_stored(semitones):
    if not 0 < semitones <= 12:
        raise ValueError('Unison spread runs from 0.001 to 12 semitones')
    return semitones / 2 if semitones <= 1 else 0.5 + (semitones - 1) / 22


def unison_voices(count, semitones):
    """Each voice's offset from the played note, in semitones."""
    if count == 2:
        return [-semitones, semitones]
    if count == 3:
        return [-semitones, 0.0, semitones]
    return [-2 * semitones, -semitones, semitones, 2 * semitones]


def arp_bpm(raw):
    return min(ARP_BPM_RANGE[1], ARP_BPM_RANGE[0] + raw / 150)


def arp_raw(bpm):
    low, high = ARP_BPM_RANGE
    if not low <= bpm <= high:
        raise ValueError('Arp/Seq rate runs from 30 to 240 BPM')
    return round((bpm - low) * 150)


def chord_offset(raw):
    """Semitones above the played note, or None for an unused voice."""
    if raw == CHORD_UNUSED:
        return None
    return (raw - CHORD_CENTRE) >> 7


def chord_raw(semitones):
    if semitones is None:
        return CHORD_UNUSED
    if not -48 <= semitones <= 48:
        raise ValueError('A chord offset runs from -48 to 48 semitones')
    return CHORD_CENTRE + (semitones << 7)


def _glide(raw, context):
    stored = raw / FULL
    mode_raw = context.get('Kbd.GlMode')
    mode = GLIDE_MODES[choice(mode_raw, 2)] if mode_raw is not None else None
    if stored == 0:
        return {'value': 0, 'unit': 'off', 'text': 'off'}
    if mode == 'Sync':
        division = SYNC_GLIDE.get(math.floor(10 * stored + 1e-9))
        bpm = arp_bpm(context['Arp.Rate']) if 'Arp.Rate' in context else None
        out = {'value': division, 'unit': 'note division', 'text': division or 'shorter than 1/32'}
        if division and bpm:
            out['seconds_at_arp_rate'] = round(60 / bpm * SYNC_GLIDE_BEATS[division], 3)
        return out
    seconds = round(glide_seconds(stored), 3)
    if mode == 'Rate':
        return {'value': seconds, 'unit': 'seconds per octave', 'text': f'{seconds} s per octave'}
    return {'value': seconds, 'unit': 'seconds', 'text': f'{seconds} s'}


def display(name, raw, descriptor, context=None):
    """The panel value of one stored field, or None when no conversion is known."""
    context = context or {}
    if name in CHOICES:
        n = choice(raw, descriptor)
        names = CHOICES[name]
        return {'value': names[n] if n < len(names) else None, 'unit': LABELS[name],
                'text': names[n] if n < len(names) else f'unknown choice {n}'}
    if name == 'VCO.BendRng':
        n = choice(raw, descriptor)
        return {'value': n, 'unit': 'semitones', 'text': f'±{n} semitones'}
    if name == 'Kbd.GlMode':
        return {'value': GLIDE_MODES[choice(raw, descriptor)], 'unit': 'mode',
                'text': GLIDE_MODES[choice(raw, descriptor)]}
    if name == 'Kbd.Glide':
        return _glide(raw, context)
    if name == 'Gen.PrstVol':
        n = choice(raw, descriptor)
        return {'value': n - 12, 'unit': 'steps from 0', 'level_db': PRESET_VOLUME_DB[n],
                'text': f'{n - 12:+d} ({PRESET_VOLUME_DB[n]:+.1f} dB)'}
    if name == 'Gen.Parafon':
        on = choice(raw, descriptor) == 1
        return {'value': on, 'unit': 'switch', 'text': 'on' if on else 'off'}
    if name == 'Gen.Chord':
        mode = PARAPHONIC_MODES.get(choice(raw, descriptor))
        return {'value': mode, 'unit': 'paraphonic mode', 'text': mode or 'unknown'}
    if name == 'Gen.UniCnt':
        n = choice(raw, descriptor) + 2
        return {'value': n, 'unit': 'voices', 'text': f'{n} voices'}
    if name == 'Gen.UniSprd':
        s = round(unison_semitones(raw / FULL), 3)
        return {'value': s, 'unit': 'semitones', 'text': f'{s:.3f}'}
    if name.startswith('Gen.ChOffs'):
        n = chord_offset(raw)
        return {'value': n, 'unit': 'semitones', 'text': 'unused' if n is None else f'{n:+d}'}
    group, _, row = name.partition('.')
    if group.startswith('Co') and group[2:].isdigit() and row in MATRIX_ROWS:
        amount = round((raw - 0x10000 if raw >= 0x8000 else raw) / FULL, 4)
        out = {'value': amount, 'unit': 'amount', 'source': MATRIX_ROWS[row],
               'destination': MATRIX_COLUMNS[int(group[2:])], 'text': f'{amount:+.3f}'}
        if group == 'Co1':
            out['semitones_at_full_source'] = round(amount * PITCH_SEMITONES_PER_AMOUNT, 2)
        return out
    if name.startswith('Mat.Assign'):
        field = destination_field(raw)
        return {'value': field, 'unit': 'destination', 'destination_id': f'0x{raw:04x}',
                'heard': raw in HEARD_DESTINATIONS, 'text': field or f'0x{raw:04x}'}
    if name == 'Arp.Range':
        n = choice(raw, descriptor) + 1
        return {'value': n, 'unit': 'octaves', 'text': f'{n} octave' + ('s' if n > 1 else '')}
    if name == 'Arp.Swing':
        n = choice(raw, descriptor) + 50
        return {'value': n, 'unit': 'percent', 'text': f'{n}%'}
    if name == 'Arp.Div':
        import sequence
        return {'value': sequence.division_from_raw(raw), 'unit': 'note division',
                'text': sequence.division_from_raw(raw)}
    if name in ('EG1.RiseLvl', 'EG1.FallLvl'):
        seconds = cycling_stage_seconds(raw / FULL)
        return {'value': round(seconds, 3), 'unit': 'seconds with a linear shape',
                'text': f'{raw / FULL:.3f} (about {seconds:.2g} s)'}
    if name == 'EG1.Hold':
        mode = context.get('EG1.Mode')
        if mode is not None and choice(mode, 2) == 0:
            return {'value': round(raw / FULL, 3), 'unit': 'sustain level in Env mode',
                    'text': f'{raw / FULL:.3f} (sustain level)'}
        seconds = cycling_hold_seconds(raw / FULL)
        return {'value': round(seconds, 3), 'unit': 'seconds in Run and Loop',
                'text': f'{raw / FULL:.3f} (about {seconds:.2g} s)'}
    if name == 'VCF.Reso':
        peak = resonance_peak_db(raw / FULL)
        return {'value': round(peak, 1), 'unit': 'dB peak at the cutoff',
                'text': f'{raw / FULL:.3f} (peak about +{peak:.1f} dB)'}
    for field, points, what in (('EG2.Attack', ATTACK_POINTS, 'to full'),
                                ('EG2.DecRel', DECAY_POINTS, 'decay to -20 dB'),
                                ('VCF.Cutoff', CUTOFF_POINTS, None)):
        if name == field:
            x = raw / FULL
            y = measured(x, points)
            if y is None:
                return None
            if field == 'VCF.Cutoff':
                return {'value': round(y), 'unit': 'Hz at -3 dB (low-pass)', 'text': f'{x:.3f} (about {y:.3g} Hz)'}
            out = {'value': round(y, 3), 'unit': f'seconds {what}', 'text': f'{x:.3f} (about {y:.2g} s {what})'}
            if field == 'EG2.DecRel':
                release = measured(x, RELEASE_POINTS)
                if release is not None:
                    out['release_seconds_to_minus_20_db'] = round(release, 3)
            return out
    if name == 'LFO.Rate':
        sync = context.get('LFO.Sync')
        if sync is not None and choice(sync, 1) == 1:
            return {'value': round(raw / FULL, 3), 'unit': 'ignored while LFO Sync is on',
                    'text': f'{raw / FULL:.3f} (LFO Sync on)'}
        hz = lfo_hz(raw / FULL)
        return {'value': None if hz is None else round(hz, 3), 'unit': 'Hz',
                'text': f'{raw / FULL:.3f}' if hz is None else f'about {hz:.3g} Hz'}
    if name == 'Arp.Rate':
        bpm = round(arp_bpm(raw), 2)
        return {'value': bpm, 'unit': 'BPM', 'text': f'{bpm:g} BPM'}
    return None


def add_display(interpretations, fields):
    """Add a 'display' entry to each interpretation whose field has a conversion."""
    context = {f['name']: f['value_le_unsigned'] for f in fields}
    raw = {f['name']: f for f in fields}
    for item in interpretations:
        source = raw.get(item['name'])
        if source is None:
            continue
        shown = display(item['name'], source['value_le_unsigned'], source['descriptor'], context)
        if shown is not None:
            item['display'] = dict(shown, evidence=EVIDENCE)
    return interpretations


def setting(name, value):
    """What microfreak:probe stores for a panel value of one field."""
    if name in CHOICES:
        names = [n.lower() for n in CHOICES[name]]
        text = {True: 'on', False: 'off'}.get(value, str(value)).lower() if isinstance(value, bool) else str(value).lower()
        if name == 'Kbd.Root':
            text = FLATS.get(text, text)
        if name == 'Kbd.Octave' and text.lstrip('+-').isdigit():
            text = f'{int(text):+d}' if int(text) else '0'
        if text not in names:
            raise ValueError(f'{LABELS[name]} takes one of {", ".join(CHOICES[name])}')
        return ('choice', names.index(text))
    if name == 'VCO.BendRng':
        if not isinstance(value, int) or not 0 <= value <= 24:
            raise ValueError('Bend range runs from 0 to 24 semitones')
        return ('choice', value)
    if name == 'Kbd.GlMode':
        return ('choice', GLIDE_MODES.index(str(value).capitalize()))
    if name == 'Gen.PrstVol':
        if not isinstance(value, int) or not -12 <= value <= 12:
            raise ValueError('Preset volume runs from -12 to 12')
        return ('choice', value + 12)
    if name == 'Gen.Parafon':
        return ('choice', 1 if value else 0)
    if name == 'Gen.Chord':
        modes = {v.lower(): k for k, v in PARAPHONIC_MODES.items()}
        return ('choice', modes[str(value).lower()])
    if name == 'Gen.UniCnt':
        if value not in (2, 3, 4):
            raise ValueError('Unison uses 2, 3 or 4 voices')
        return ('choice', value - 2)
    if name == 'Gen.UniSprd':
        return ('decimal', unison_stored(float(value)))
    if name.startswith('Gen.ChOffs'):
        return ('raw', chord_raw(value))
    if name == 'Arp.Rate':
        return ('raw', arp_raw(float(value)))
    if name == 'Arp.Range':
        if value not in (1, 2, 3, 4):
            raise ValueError('The arpeggio range is 1 to 4 octaves')
        return ('choice', value - 1)
    if name == 'Arp.Swing':
        if not 50 <= value <= 75:
            raise ValueError('Swing runs from 50 to 75 percent')
        return ('choice', round(value) - 50)
    if name == 'Arp.Div':
        import sequence
        return ('raw', sequence.division_to_raw(value))
    if name.startswith('Mat.Assign'):
        ids = destination_ids()
        if value not in ids:
            raise ValueError(f'No destination id known for {value!r}')
        return ('raw', ids[value])
    group, _, row = name.partition('.')
    if group.startswith('Co') and row in MATRIX_ROWS:
        if not -1 <= float(value) <= 1:
            raise ValueError('A matrix amount runs from -1 to 1')
        return ('decimal', float(value))
    raise ValueError(f'No measured conversion for {name}')


def glide_setting(mode, value):
    """The stored Glide for a time in seconds (Time, Rate) or a division (Sync)."""
    if str(mode).capitalize() == 'Sync':
        index = {v: k for k, v in SYNC_GLIDE.items()}.get(str(value).upper())
        if index is None:
            raise ValueError(f'Sync glide takes one of {", ".join(SYNC_GLIDE.values())}')
        return ('decimal', min(1.0, (index + 0.5) / 10))
    return ('decimal', glide_stored(float(value)))
