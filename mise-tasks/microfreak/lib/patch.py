#!/usr/bin/env python3
"""Write a MicroFreak patch described in the panel's own words into a preset.

A description is YAML or JSON: oscillator, filter, envelope, cycling_envelope,
lfo, glide, keyboard, voice, arp, matrix, fields and sequence, each optional.
Every setting it names goes through lib/patch_fields.py, whose conversions were
measured on the instrument; `fields` stores a named field directly. The base
preset keeps every setting the description leaves out. A `matrix` list is the
whole matrix: amounts it does not list become 0.

Without --slot the task prints what it would store and changes nothing. With
--slot the result goes through microfreak:upload: a slot that holds a preset is
saved to --backup-dir first, and the slot is read back and compared.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

import parameters
import patch_fields as P
import probe
import sequence as Q

CATEGORIES = ('Bass', 'Brass', 'Keys', 'Lead', 'Organ', 'Pad', 'Percussion',
              'Sequence', 'SFX', 'Strings', 'Template', 'Vocoder')
MODELS = [m for m in __import__('semantics').ENGINE_MODELS]
SOURCES = {'cycenv': 'EG1', 'cycling envelope': 'EG1', 'cycling_envelope': 'EG1',
           'env': 'EG2', 'envelope': 'EG2', 'lfo': 'LFO', 'pressure': 'Xpr',
           'key/arp': 'Key', 'key': 'Key', 'keyarp': 'Key', 'key_arp': 'Key'}
COLUMNS = {'pitch': 1, 'wave': 2, 'timbre': 3, 'cutoff': 4}
# Panel names for Assign destinations; any field name with a destination id also works.
DESTINATIONS = {
    'shape': 'VCO.Param3', 'resonance': 'VCF.Reso', 'glide': 'Kbd.Glide',
    'lfo rate': 'LFO.Rate', 'attack': 'EG2.Attack', 'decay': 'EG2.DecRel', 'release': 'EG2.DecRel',
    'sustain': 'EG2.Sustain', 'rise': 'EG1.RiseLvl', 'fall': 'EG1.FallLvl', 'hold': 'EG1.Hold',
    'cycenv amount': 'EG1.Amount', 'unison spread': 'Gen.UniSprd', 'arp rate': 'Arp.Rate',
}
UNIT = ('start', 'oscillator', 'filter', 'envelope', 'cycling_envelope', 'lfo', 'glide', 'keyboard',
        'voice', 'arp', 'matrix', 'fields', 'sequence', 'name', 'category')
# `start: plain` sets these first, so a sound does not inherit its base's.
PLAIN = {
    'oscillator': {'type': 'BasicWaves', 'wave': 0.5, 'timbre': 0.0, 'shape': 0.0},
    'filter': {'type': 'LPF', 'cutoff': 1.0, 'resonance': 0.0},
    'envelope': {'attack': 0.0, 'decay': 0.3, 'sustain': 1.0, 'amp_mod': True, 'legato': False,
                 'snap': False},
    'cycling_envelope': {'mode': 'Env', 'amount': 0.0},
    'lfo': {'shape': 'Sine', 'rate': 0.5, 'retrig': 'Off'},
    'glide': 'off',
    'keyboard': {'bend_range': 2, 'octave': 0, 'scale': 'Off', 'press_mode': 'Aftertouch',
                 'key_arp_mode': 'Linear', 'velo_amp_mod': 0},
    'voice': {'paraphonic': False, 'volume': 0},
    'arp': {'on': False},
    'matrix': [],
}


def unit(value, name):
    value = float(value)
    if not 0 <= value <= 1:
        raise ValueError(f'{name} runs from 0 to 1')
    return ('decimal', value)


def on_off(value):
    if isinstance(value, bool):
        return value
    text = str(value).lower()
    if text not in ('on', 'off', 'true', 'false'):
        raise ValueError(f'Expected on or off, not {value!r}')
    return text in ('on', 'true')


def oscillator_settings(spec, descriptor):
    out = []
    if 'type' in spec:
        wanted = str(spec['type']).replace(' ', '').replace('.', '').lower()
        names = [m and m.replace(' ', '').replace('.', '').lower() for m in MODELS]
        if wanted not in names:
            raise ValueError(f'Unknown oscillator type {spec["type"]!r}; use one of '
                             + ', '.join(m for m in MODELS if m))
        index = names.index(wanted)
        if index > descriptor:
            raise ValueError(f'The base preset stores {descriptor + 1} oscillator types; '
                             f'{spec["type"]} needs a base saved on firmware 5')
        out.append(('VCO.Type', ('choice', index)))
    for key, field in (('wave', 'VCO.Param1'), ('timbre', 'VCO.Param2'), ('shape', 'VCO.Param3')):
        if key in spec:
            out.append((field, unit(spec[key], f'oscillator {key}')))
    return out


def section_settings(spec, table, label):
    out = []
    for key, value in spec.items():
        if key not in table:
            raise ValueError(f'Unknown {label} key {key!r}; use {", ".join(table)}')
        field, kind = table[key]
        if kind == 'unit':
            out.append((field, unit(value, f'{label} {key}')))
        elif kind == 'switch':
            out.append((field, ('choice', 1 if on_off(value) else 0)))
        else:
            out.append((field, P.setting(field, value)))
    return out


FILTER = {'type': ('VCF.Type', 'named'), 'cutoff': ('VCF.Cutoff', 'unit'), 'resonance': ('VCF.Reso', 'unit')}
ENVELOPE = {'attack': ('EG2.Attack', 'unit'), 'decay': ('EG2.DecRel', 'unit'), 'sustain': ('EG2.Sustain', 'unit'),
            'amp_mod': ('EG2.Mode', 'switch'), 'legato': ('EG2.Legato', 'switch'), 'snap': ('EG2.Snap', 'switch')}


def envelope_settings(spec):
    """Envelope keys; filter_amount comes back apart, to apply after any matrix."""
    spec = dict(spec)
    out = []
    if 'attack_seconds' in spec:
        out.append(('EG2.Attack', ('decimal', P.value_for(float(spec.pop('attack_seconds')),
                                                         P.ATTACK_POINTS, 'Attack times', 's'))))
    if 'decay_seconds' in spec:
        out.append(('EG2.DecRel', ('decimal', P.value_for(float(spec.pop('decay_seconds')),
                                                         P.DECAY_POINTS, 'Decay times', 's'))))
    amount = spec.pop('filter_amount', None)
    if amount is not None and not -1 <= float(amount) <= 1:
        raise ValueError('filter_amount runs from -1 to 1')
    later = [] if amount is None else [('Co4.EG2', ('decimal', float(amount)))]
    return section_settings(spec, ENVELOPE, 'envelope') + out, later
CYCLING = {'mode': ('EG1.Mode', 'named'), 'rise': ('EG1.RiseLvl', 'unit'), 'fall': ('EG1.FallLvl', 'unit'),
           'hold': ('EG1.Hold', 'unit'), 'amount': ('EG1.Amount', 'unit'),
           'rise_shape': ('EG1.RiseSlp', 'unit'), 'fall_shape': ('EG1.FallSlp', 'unit')}
LFO = {'shape': ('LFO.Shape', 'named'), 'rate': ('LFO.Rate', 'unit'), 'retrig': ('LFO.Retrig', 'named'),
       'sync': ('LFO.Sync', 'switch'), 'division': ('LFO.Div', 'named')}


def lfo_settings(spec):
    """A rate or hz turns LFO Sync off unless the description sets sync."""
    spec = dict(spec)
    out = []
    if 'hz' in spec:
        out.append(('LFO.Rate', ('decimal', P.lfo_stored(float(spec.pop('hz'))))))
    if 'division' in spec and 'sync' not in spec:
        out.append(('LFO.Sync', ('choice', 1)))
    elif ('rate' in spec or out) and 'sync' not in spec:
        out.append(('LFO.Sync', ('choice', 0)))
    return section_settings(spec, LFO, 'lfo') + out
KEYBOARD = {'bend_range': ('VCO.BendRng', 'named'), 'press_mode': ('Kbd.Veloc', 'named'),
            'key_arp_mode': ('Mat.KyMdSrc', 'named'), 'scale': ('Kbd.Scale', 'named'),
            'root': ('Kbd.Root', 'named'), 'octave': ('Kbd.Octave', 'named')}


def glide_settings(spec):
    if spec in (0, None, False, 'off', 'Off'):
        return [('Kbd.Glide', ('decimal', 0.0))]
    mode = str(spec.get('mode', 'Time')).capitalize()
    out = [('Kbd.GlMode', P.setting('Kbd.GlMode', mode))]
    if mode == 'Sync':
        value = spec.get('division')
    elif mode == 'Rate':
        value = spec.get('seconds_per_octave')
    else:
        value = spec.get('seconds')
    if value is None:
        raise ValueError('glide needs seconds (Time), division (Sync) or seconds_per_octave (Rate)')
    out.append(('Kbd.Glide', P.glide_setting(mode, value)))
    return out


def keyboard_settings(spec):
    spec = dict(spec)
    out = []
    if 'velo_amp_mod' in spec:
        amp = spec.pop('velo_amp_mod')
        if isinstance(amp, bool) or not isinstance(amp, (int, float)) or not 0 <= amp <= 10:
            raise ValueError('velo_amp_mod runs from 0 to 10')
        out.append(('Kbd.PresAmp', ('raw', round(amp * 32767 / 10))))
    return out + section_settings(spec, KEYBOARD, 'keyboard')


def voice_settings(spec):
    out = []
    for key, value in spec.items():
        if key == 'paraphonic':
            out.append(('Gen.Parafon', ('choice', 1 if on_off(value) else 0)))
        elif key == 'mode':
            out.append(('Gen.Chord', P.setting('Gen.Chord', value)))
            out.append(('Gen.Parafon', ('choice', 1)))
        elif key == 'unison_voices':
            out.append(('Gen.UniCnt', P.setting('Gen.UniCnt', int(value))))
        elif key == 'unison_spread':
            out.append(('Gen.UniSprd', P.setting('Gen.UniSprd', value)))
        elif key == 'chord':
            offsets = list(value) + [None] * (3 - len(value))
            if len(offsets) != 3:
                raise ValueError('chord takes up to three offsets in semitones')
            out += [(f'Gen.ChOffs{n}', P.setting(f'Gen.ChOffs{n}', o)) for n, o in enumerate(offsets, 1)]
        elif key == 'volume':
            out.append(('Gen.PrstVol', P.setting('Gen.PrstVol', int(value))))
        else:
            raise ValueError(f'Unknown voice key {key!r}')
    return out


def destination_field(name):
    text = str(name)
    field = DESTINATIONS.get(text.lower(), text)
    if field not in P.destination_ids():
        raise ValueError(f'Unknown matrix destination {name!r}: use Pitch, Wave, Timbre, Cutoff, '
                         f'{", ".join(DESTINATIONS)} or a field name such as LFO.Rate')
    return field


def matrix_settings(routes, current):
    """Settings for a whole matrix: listed amounts, every other amount 0, Assign columns as needed."""
    amounts = {(c, r): 0.0 for c in range(1, 8) for r in P.MATRIX_ROWS}
    assigns = {}
    for route in routes:
        source = SOURCES.get(str(route['source']).lower())
        if source is None:
            raise ValueError(f'Unknown matrix source {route["source"]!r}; use CycEnv, Envelope, LFO, Pressure or Key/Arp')
        column = COLUMNS.get(str(route['destination']).lower())
        if column is None:
            field = destination_field(route['destination'])
            column = next((c for c, f in assigns.items() if f == field), None)
            if column is None:
                column = next((c for c in (5, 6, 7) if c not in assigns), None)
                if column is None:
                    raise ValueError('The matrix has three Assign columns; this description needs more')
                assigns[column] = field
        if 'semitones' in route:
            if column != 1:
                raise ValueError('semitones applies to the Pitch destination only')
            amount = float(route['semitones']) / P.PITCH_SEMITONES_PER_AMOUNT
        else:
            amount = float(route['amount'])
        if not -1 <= amount <= 1:
            raise ValueError('A matrix amount runs from -1 to 1 (48 semitones on Pitch)')
        amounts[(column, source)] = amount
    out = [(f'Co{c}.{r}', ('decimal', a)) for (c, r), a in amounts.items()]
    for column, field in assigns.items():
        out.append((f'Mat.Assign{column - 4}', P.setting(f'Mat.Assign{column - 4}', field)))
    return out


def field_settings(spec):
    out = []
    for name, value in spec.items():
        if isinstance(value, str):
            out.append(probe.parse_set(f'{name}={value}'))
        elif isinstance(value, float):
            out.append((name, ('decimal', value)))
        elif isinstance(value, bool):
            out.append((name, ('choice', int(value))))
        else:
            out.append((name, ('choice', int(value))))
    return out


def settings_for(description, fields):
    """Turn a description into (field, spec) pairs, in order; later pairs win."""
    unknown = set(description) - set(UNIT)
    if unknown:
        raise ValueError(f'Unknown description keys: {", ".join(sorted(unknown))}')
    out = []
    later = []
    if description.get('start') not in (None, 'plain'):
        raise ValueError('start takes plain')
    if description.get('start') == 'plain':
        out += settings_for(dict(PLAIN), fields)
    if 'oscillator' in description:
        out += oscillator_settings(description['oscillator'], fields['VCO.Type']['descriptor'])
    if 'filter' in description:
        spec = dict(description['filter'])
        if 'cutoff_hz' in spec:
            out.append(('VCF.Cutoff', ('decimal', P.value_for(float(spec.pop('cutoff_hz')),
                                                             P.CUTOFF_POINTS, 'Cutoffs', 'Hz'))))
        out += section_settings(spec, FILTER, 'filter')
    if 'envelope' in description:
        settings, later = envelope_settings(description['envelope'])
        out += settings
    if 'cycling_envelope' in description:
        out += section_settings(description['cycling_envelope'], CYCLING, 'cycling_envelope')
    if 'lfo' in description:
        out += lfo_settings(description['lfo'])
    if 'glide' in description:
        out += glide_settings(description['glide'])
    if 'keyboard' in description:
        out += keyboard_settings(description['keyboard'])
    if 'voice' in description:
        out += voice_settings(description['voice'])
    if 'arp' in description:
        keys = {'bpm': 'Arp.Rate', 'direction': 'Arp.Dir', 'octaves': 'Arp.Range', 'swing': 'Arp.Swing',
                'division': 'Arp.Div'}
        for key, value in description['arp'].items():
            if key == 'on':
                out.append(('Arp.Enable', ('choice', 1 if on_off(value) else 0)))
                if on_off(value):
                    out.append(('Arp.SeqOn', ('choice', 0)))
            elif key in keys:
                out.append((keys[key], P.setting(keys[key], value)))
            else:
                raise ValueError(f'Unknown arp key {key!r}; use on, {", ".join(keys)}')
    if 'matrix' in description:
        out += matrix_settings(description['matrix'], fields)
    out += later
    if 'fields' in description:
        out += field_settings(description['fields'])
    return out


def shown(name, raw, fields, context):
    import semantics
    field = fields[name]
    value = P.display(name, raw, field['descriptor'], context)
    if value:
        return value['text']
    signed = raw - 0x10000 if raw >= 0x8000 else raw
    read = semantics._field_value({'name': name, 'descriptor': field['descriptor'],
                                   'value_le_unsigned': raw, 'value_le_signed': signed})
    if read.get('model'):
        return read['model']
    if isinstance(read['value'], float):
        return round(read['value'], 3)
    return read['value']


def prepare(description, payload):
    """Return the new payload and {field: [before, after]} in panel terms where known."""
    fields = {f['name']: f for f in parameters.parse_parameters(payload)['fields']}
    settings = settings_for(description, fields)
    new, changed = probe.apply_settings(payload, settings)
    sequence_changed = {}
    if description.get('sequence') is not None:
        new, sequence_changed = Q.make_playable(new, description['sequence'])
    before = {n: f['value_le_unsigned'] for n, f in fields.items()}
    after_fields = {f['name']: f for f in parameters.parse_parameters(new)['fields']}
    after = {n: f['value_le_unsigned'] for n, f in after_fields.items()}
    report = {}
    for name in list(changed) + [n for n in sequence_changed if n not in changed]:
        if before.get(name) != after.get(name):
            report[name] = [shown(name, before[name], fields, before), shown(name, after[name], after_fields, after)]
    return new, report


def load_description(path):
    text = Path(path).read_text()
    if Path(path).suffix.lower() in ('.yaml', '.yml'):
        import yaml
        return yaml.safe_load(text) or {}
    return json.loads(text)


def main(argv=None):
    import sequence_write as W
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('description', type=Path, help='YAML or JSON patch description')
    parser.add_argument('--base', required=True, help='Slot number to read, or a .bin from microfreak:download')
    parser.add_argument('--slot', type=int, help='Slot to write; without it, preview only')
    parser.add_argument('--backup-dir', type=Path, help='Save the slot here first when it holds a preset')
    parser.add_argument('--output', type=Path, help='Also save the result as a microfreak:download file')
    parser.add_argument('--name', help='Preset name; default the description name, then the base name')
    parser.add_argument('--category', choices=CATEGORIES)
    parser.add_argument('--port', help='Exact MIDI port name')
    args = parser.parse_args(argv)
    try:
        description = load_description(args.description)
        slot = W.base_slot(args.base)
        midi = None
        if slot is not None or args.slot:
            import download
            midi = download.open_ports(args.port)
        try:
            if slot is not None:
                header, payload, _ = W.read_base_slot(midi[0], midi[1], slot)
            else:
                header, payload = W.load_base_file(args.base)
            new, changed = prepare(description, payload)
            import upload
            name = args.name or description.get('name') or upload.preset_name(header)
            category = args.category or description.get('category')
            upload.check_name(name)
            if category is not None and category not in CATEGORIES:
                raise ValueError(f'Unknown category {category!r}')
            report = {'base': str(args.base), 'name': name, 'category': category,
                      'settings_changed': changed, 'data_sha256': hashlib.sha256(new).hexdigest()}
            target = args.slot or 1
            sent = upload.build_header(header, target, name=name, category=category)
            if args.output:
                args.output.write_bytes(bytes(sent) + new)
                report['output'] = str(args.output)
            if args.slot:
                result = upload.upload(midi[0], midi[1], args.slot, sent, new, args.backup_dir, midi[2])
                report['upload'] = {'slot': args.slot, 'was': None if result['before']['initialized']
                                    else result['before']['name'],
                                    'backup': str(result['backup']) if 'backup' in result else None,
                                    'read_back_matches': True}
        finally:
            if midi:
                midi[0].close_port()
                midi[1].close_port()
    except (ValueError, OSError, RuntimeError, KeyError) as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 1
    print(json.dumps(report, indent=1, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
