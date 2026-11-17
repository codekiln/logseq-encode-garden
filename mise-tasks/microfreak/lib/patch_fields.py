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
}
LABELS = {'EG2.Legato': 'Envelope Legato', 'EG2.Snap': 'Envelope Snap', 'LFO.Retrig': 'LFO Retrig',
          'Kbd.Veloc': 'Press Mode', 'Mat.KyMdSrc': 'Key/Arp Mode'}
# Level of C4 against choice 12, measured in 0.5 dB steps. Choices 9 and 10 played alike.
PRESET_VOLUME_DB = (-5.5, -5.0, -4.5, -4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -1.0, -0.5, 0.0,
                    0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0)
CHORD_UNUSED = 0x7F80
CHORD_CENTRE = 0x4000
ARP_BPM_RANGE = (30.0, 240.0)


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
    raise ValueError(f'No measured conversion for {name}')


def glide_setting(mode, value):
    """The stored Glide for a time in seconds (Time, Rate) or a division (Sync)."""
    if str(mode).capitalize() == 'Sync':
        index = {v: k for k, v in SYNC_GLIDE.items()}.get(str(value).upper())
        if index is None:
            raise ValueError(f'Sync glide takes one of {", ".join(SYNC_GLIDE.values())}')
        return ('decimal', min(1.0, (index + 0.5) / 10))
    return ('decimal', glide_stored(float(value)))
