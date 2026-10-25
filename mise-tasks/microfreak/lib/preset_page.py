#!/usr/bin/env python3
"""Write decoded settings, with links to the panel controls, onto preset pages.

Reads only local files: device reads made by ``microfreak:download`` and the
MIDI Control Center factory archives. It never contacts the instrument.

Section wording follows the pages written for the October 25, 2026 factory
backup. Every control name links to its ``Microfreak/UI`` page: oscillator
controls to ``Microfreak/UI/Oscillator/Knob/...`` and the rest to the panel
position pages under ``Microfreak/UI/Front/Row/...``.

Custom presets get a "Customized controls" section listing the controls that
differ from the nearest factory payload. The garden has no trustworthy Init
baseline: the device slots named "Init" are codekiln's own sounds with filter,
envelope and LFO settings far from neutral, so the comparison uses factory
payloads only, and factory presets get no such section.

Matrix Assign destinations resolve through Freakout's hardware-correlated
live-word map, vendored as ``freakout_live_map.py`` (MIT; see FREAKOUT_LICENSE).
``--live-map`` points at another copy.
"""
import argparse
import datetime as dt
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote

import parameters
import semantics

FACTORY = Path('/Library/Arturia/MIDI Control Center/Templates/MicroFreak/Local/Factory')
B2 = 'https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/'
ORIGIN = '[[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/{}]]'
PREFIX = 'preset-synth-'

UI = 'Microfreak/UI'
OSC = UI + '/Oscillator/Knob'
FRONT = UI + '/Front/Row'
# Every front-panel page this generator links, by panel area. Renaming a row
# or an area on the panel pages means changing this table only.
PANEL = {
    'matrix': FRONT + '/01 Top/01 Matrix',
    'paraphonic': FRONT + '/01 Top/02 Paraphonic Button',
    'glide': FRONT + '/02 Main/01 Glide Knob',
    'filter': FRONT + '/02 Main/03 Analog Filter',
    'cycling': FRONT + '/02 Main/04 Cycling Envelope',
    'octave': FRONT + '/03 Bottom/01 Octave',
    'arp': FRONT + '/03 Bottom/03 Arp Seq',
    'lfo': FRONT + '/03 Bottom/04 LFO',
    'envelope': FRONT + '/03 Bottom/05 Envelope',
    'keyboard': FRONT + '/05 Keys',
}
FILTER = PANEL['filter']
CYCLING = PANEL['cycling']
ENVELOPE = PANEL['envelope']
LFO = PANEL['lfo']
MATRIX = PANEL['matrix']
ARP = PANEL['arp']
PAGES = {
    'VCO.Type': OSC + '/Type',
    'Kbd.Glide': PANEL['glide'],
    'Kbd.Octave': PANEL['octave'],
    'VCF.Type': FILTER + '/Button/Type',
    'VCF.Cutoff': FILTER + '/Knob/Cutoff',
    'VCF.Reso': FILTER + '/Knob/Resonance',
    'EG1.Mode': CYCLING + '/Button/Mode',
    'EG1.RiseLvl': CYCLING + '/Knob/Rise',
    'EG1.RiseSlp': CYCLING + '/Knob/Rise/Shift',
    'EG1.FallLvl': CYCLING + '/Knob/Fall',
    'EG1.FallSlp': CYCLING + '/Knob/Fall/Shift',
    'EG1.Hold': CYCLING + '/Knob/Hold Sustain',
    'EG1.Amount': CYCLING + '/Knob/Amount',
    'EG2.Attack': ENVELOPE + '/Knob/Attack',
    'EG2.DecRel': ENVELOPE + '/Knob/Decay Rel',
    'EG2.Sustain': ENVELOPE + '/Knob/Sustain',
    'EG2.Mode': ENVELOPE + '/Button/Amp Mod',
    'LFO.Shape': LFO + '/Button/Shape',
    'LFO.Rate': LFO + '/Knob/Rate',
    'LFO.Sync': LFO + '/Knob/Rate/Press',
    'LFO.Div': LFO + '/Knob/Rate/Press',
    'Gen.Parafon': PANEL['paraphonic'],
    'Arp.Rate': ARP + '/Knob/Rate',
    'Arp.Enable': ARP + '/Button/Arp Seq/Arp',
    'Arp.SeqOn': ARP + '/Button/Arp Seq/Seq',
}
# Guide page names under Microfreak/UG/06 Dig Osc/03 Types and the matching
# Microfreak/UI/Oscillator/Knob/Type page for each semantics.ENGINE_MODELS name.
MODELS = {
    'BasicWaves': ('01 BasicWaves', 'BasicWaves'), 'SuperWave': ('02 SuperWave', 'SuperWave'),
    'Wavetable': ('03 Wavetable', 'Wavetable'), 'Harmo': ('04 Harmo', 'Harmo'),
    'KarplusStr': ('05 KarplusStr', 'KarplusStr'), 'V.Analog': ('06 VAnalog', 'VAnalog'),
    'Waveshaper': ('07 Waveshaper', 'Waveshaper'), 'Two Op. FM': ('08 Two Op.FM', 'Two Op.FM'),
    'Formant': ('09 Formant', 'Formant'), 'Chords': ('10 Chords', 'Chords'),
    'Speech': ('11 Speech', 'Speech'), 'Modal': ('12 Modal', 'Modal'), 'Noise': ('13 Noise', 'Noise'),
    'Bass': ('14 BASS', 'BASS'), 'SawX': ('15 SAWX', 'SAWX'), 'Harm': ('16 HARM', 'HARM'),
    'WaveUser': ('17 WaveUser', 'WaveUser'), 'Sample': ('18 Sample', 'Sample'),
    'Scan Grains': ('19 Scan Grains', 'Scan Grains'), 'Cloud Grains': ('20 Cloud Grains', 'Cloud Grains'),
    'Hit Grains': ('21 Hit Grains', 'Hit Grains'), 'Vocoder': ('22 Vocoder', 'Vocoder'),
}
# The guide leaves the Chords third control unnamed; its UI page is Waveform.
PARAM_PAGE_NAMES = {'Inv/Transp': 'Inv Transp'}
UNNAMED_PARAM_PAGES = {('Chords', 3): 'Waveform'}
PANEL_KNOBS = ('Wave', 'Timbre', 'Shape')
FILTERS = [('Low-pass', '01 Low Pass Filter', 'LPF'), ('Band-pass', '02 Band Pass Filter', 'BPF'),
           ('High-pass', '03 High Pass Filter', 'HPF')]
CYC_MODES = ['Env', 'Run', 'Loop']
# Labels follow MicroFreak Reader; the panel pages use the panel's own names.
LFO_SHAPES = [('Sine', 'Sine'), ('Triangle', 'Triangle'), ('Sawtooth', 'Rising Sawtooth'),
              ('Square', 'Square'), ('Sample-and-Hold', 'Random Stepped'),
              ('Sample-and-Hold Filtered', 'Random Gliding')]
OCTAVES = ['-3', '-2', '-1', '0', '+1', '+2', '+3']
ROWS = [('EG1', 'Cycling Envelope', PANEL['cycling']),
        ('EG2', 'ENV', PANEL['envelope']),
        ('LFO', 'LFO', PANEL['lfo']),
        ('Xpr', 'PRESSURE', PANEL['keyboard']),
        ('Key', 'KEY/ARP', PANEL['keyboard'])]
COLUMNS = ['Pitch', 'Wave', 'Timbre', 'Cutoff', 'Assign 1', 'Assign 2', 'Assign 3']
COLUMN_PAGES = {'Wave': OSC + '/Wave', 'Timbre': OSC + '/Timbre', 'Cutoff': PAGES['VCF.Cutoff'],
                'Assign 1': MATRIX + '/Button/Assn/1', 'Assign 2': MATRIX + '/Button/Assn/2',
                'Assign 3': MATRIX + '/Button/Assn/3'}
DEST_LABELS = {
    'VCF.Cutoff': 'Filter Cutoff', 'VCF.Reso': 'Filter Resonance', 'VCF.Type': 'Filter Type',
    'LFO.Rate': 'LFO Rate', 'LFO.Shape': 'LFO Shape', 'EG2.Attack': 'Attack', 'EG2.DecRel': 'Decay/Release',
    'EG2.Sustain': 'Sustain', 'EG1.RiseLvl': 'Cycling Envelope Rise', 'EG1.FallLvl': 'Cycling Envelope Fall',
    'EG1.Hold': 'Cycling Envelope Hold', 'EG1.Amount': 'Cycling Envelope Amount', 'Kbd.Glide': 'Glide',
    'Arp.Rate': 'Arp/Seq Rate', 'Gen.UniSprd': 'Unison Spread', 'Gen.PrstVol': 'Preset Volume',
    'VCO.Type': 'Oscillator Type',
}
UG = {
    'filter': 'Microfreak/UG/07 Filter/01 Modifying Sound/{}',
    'env': 'Microfreak/UG/09 Envelope Gen/03 Envelope Stages',
    'cycling': 'Microfreak/UG/09 Envelope Gen/06 Cycling Envelope',
    'lfo': '[[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]',
    'matrix': 'Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations',
}
GENERATED_SECTIONS = ('Oscillator', 'Filter', 'Envelopes', 'LFO', 'Modulation matrix',
                      'Voice and keyboard', 'Customized controls')
EVIDENCE = [
    '\t- ## Evidence and interpretation',
    '\t\t- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; '
    'they are not OLED percentages, hertz or milliseconds.',
    '\t\t- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) '
    'preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.',
    '\t\t- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). '
    'Mode, LFO shape, filter type and octave labels follow the '
    '[MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).',
]
# Controls listed in "Customized controls", in panel order.
CUSTOMIZED = ['VCO.Type', 'VCO.Param1', 'VCO.Param2', 'VCO.Param3', 'Kbd.Glide', 'Kbd.Octave',
              'VCF.Type', 'VCF.Cutoff', 'VCF.Reso', 'EG1.Mode', 'EG1.RiseLvl', 'EG1.RiseSlp',
              'EG1.FallLvl', 'EG1.FallSlp', 'EG1.Hold', 'EG1.Amount', 'EG2.Attack', 'EG2.DecRel',
              'EG2.Sustain', 'EG2.Mode', 'LFO.Shape', 'LFO.Sync', 'LFO.Rate', 'LFO.Div',
              'Gen.Parafon', 'Arp.Enable', 'Arp.SeqOn', 'Arp.Rate']
NAMES = {'Kbd.Glide': 'Glide', 'Kbd.Octave': 'Octave', 'VCF.Type': 'Filter type', 'VCF.Cutoff': 'Cutoff',
         'VCF.Reso': 'Resonance', 'EG1.Mode': 'Cycling Envelope mode', 'EG1.RiseLvl': 'Rise',
         'EG1.RiseSlp': 'Rise shape', 'EG1.FallLvl': 'Fall', 'EG1.FallSlp': 'Fall shape',
         'EG1.Hold': 'Hold/Sustain', 'EG1.Amount': 'Cycling Envelope amount', 'EG2.Attack': 'Attack',
         'EG2.DecRel': 'Decay/Release', 'EG2.Sustain': 'Sustain', 'EG2.Mode': 'Amp Mod',
         'LFO.Shape': 'LFO shape', 'LFO.Sync': 'LFO sync', 'LFO.Rate': 'LFO rate',
         'LFO.Div': 'LFO sync division code', 'Gen.Parafon': 'Paraphonic', 'Arp.Enable': 'Arp',
         'Arp.SeqOn': 'Seq', 'Arp.Rate': 'Arp/Seq rate', 'VCO.Type': 'Oscillator type'}
# More differences than this means the preset was not made from that factory sound.
NEAREST_LIMIT = 12
TOLERANCE = 0.0005


def link(label, page, linked=True):
    return f'[{label}]([[{page}]])' if linked else label


def fmt(value):
    return f'{value:.3f}'


def signed(value):
    if 0 < abs(value) < 0.0005:
        return ('+' if value > 0 else '−') + '<0.001'
    return ('+' if value >= 0 else '−') + f'{abs(value):.3f}'


def param_page(model, position, label):
    """Return the UI page for oscillator control ``position`` (1–3) of ``model``."""
    if model not in MODELS:
        return OSC + '/' + PANEL_KNOBS[position - 1]
    name = UNNAMED_PARAM_PAGES.get((model, position)) or PARAM_PAGE_NAMES.get(label, label)
    return f'{OSC}/Type/{MODELS[model][1]}/{name}'


def load_live_map(path):
    """Return {address: field name} from Freakout's microfreak_live_map.py."""
    spec = importlib.util.spec_from_file_location('microfreak_live_map', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    address = {}
    for key, addresses in module.MICROFREAK_STRUCTURED_LIVE_WORDS.items():
        for item in addresses:
            address.setdefault(item, key)
    address.setdefault(0x0000, 'VCO.Type')
    return address


def interpret(path):
    report = parameters.inspect(Path(path), interpret_fw5=True)
    if report['status'] != 'raw_parameters':
        raise ValueError(f'{path}: inspect status {report["status"]}')
    return report['interpretations']


def values(interp):
    return {f['name']: f for f in interp['fields']}


def assign_labels(fields, address, linked=True):
    """Describe the destination of each Assign column, as the matrix shows it."""
    val = lambda name: fields[name]['value'] if name in fields else None
    result = {}
    for n in (1, 2, 3):
        raw = val(f'Mat.Assign{n}')
        key = address.get(raw) if raw is not None else None
        if key in ('VCO.Param1', 'VCO.Param2', 'VCO.Param3'):
            pos = int(key[-1])
            label = (fields[key]['label'] if key in fields and fields[key]['label'] != key
                     else PANEL_KNOBS[pos - 1])
            model = next((f.get('model') for f in fields.values() if f['name'] == 'VCO.Type'), None)
            label = link(label, param_page(model, pos, label), linked)
        elif key and re.fullmatch(r'Co[1-7]\.(EG1|EG2|LFO|Xpr|Key)', key):
            row = next(r for r in ROWS if r[0] == key[4:])
            column = COLUMNS[int(key[2]) - 1]
            label = f'matrix amount {link(row[1], row[2], linked)} → {column}'
        elif key in DEST_LABELS:
            label = link(DEST_LABELS[key], PAGES[key], linked) if key in PAGES else DEST_LABELS[key]
        else:
            label = f'`{key}`' if key else None
        result[f'Assign {n}'] = label
    return result


def describe(interp, address, linked=True):
    """Return [(section title, [lines])] for the decoded settings."""
    fields = values(interp)
    val = lambda name: fields[name]['value'] if name in fields else None
    L = lambda label, key: link(label, PAGES[key], linked)
    out = []
    model = interp['oscillator']['model'] if interp['oscillator'] else None
    osc = []
    if model:
        controls = []
        for position, name in enumerate(('VCO.Param1', 'VCO.Param2', 'VCO.Param3'), 1):
            f = fields.get(name)
            if not f:
                continue
            label = f['label'] if f['label'] != name else PANEL_KNOBS[position - 1] + ' control'
            shown = link(label, param_page(model, position, label), linked)
            if f['kind'] == 'normalized_0_1':
                controls.append(f'{shown}: {fmt(f["value"])}.')
            else:
                controls.append(f'{shown}: {f["value"]} (stored choice code).')
        ug, ui = MODELS[model]
        osc.append(f'{L("Model", "VCO.Type")}: {link(model, OSC + "/Type/" + ui, linked)}. '
                   f'[[Microfreak/UG/06 Dig Osc/03 Types/{ug}]]')
        osc.append(' '.join(controls))
    else:
        index = interp['oscillator']['index'] if interp['oscillator'] else None
        osc.append(f'Stored oscillator index {index} has no documented model name.')
    octave = val('Kbd.Octave')
    if octave is not None and 0 <= octave < 7:
        osc.append(f'{L("Keyboard octave", "Kbd.Octave")}: {OCTAVES[octave]}. '
                   f'{L("Glide", "Kbd.Glide")}: {fmt(val("Kbd.Glide") or 0)}.')
    out.append(('Oscillator', osc))
    t = val('VCF.Type')
    if t is not None and 0 <= t < 3 and val('VCF.Cutoff') is not None:
        name, page, button = FILTERS[t]
        out.append(('Filter', [
            f'{link(name, PAGES["VCF.Type"] + "/" + button, linked)} filter. '
            f'Saved {L("cutoff", "VCF.Cutoff")}: {fmt(val("VCF.Cutoff"))}; '
            f'{L("resonance", "VCF.Reso")}: {fmt(val("VCF.Reso") or 0)}. [[{UG["filter"].format(page)}]]']))
    env = []
    if val('EG2.Attack') is not None:
        amp = {1: f' {L("Amp Mod", "EG2.Mode")} is on, so the main envelope controls loudness.',
               0: f' {L("Amp Mod", "EG2.Mode")} is off.'}.get(val('EG2.Mode'), '')
        env.append(f'Main envelope: {L("attack", "EG2.Attack")} {fmt(val("EG2.Attack"))}, '
                   f'{L("decay/release", "EG2.DecRel")} {fmt(val("EG2.DecRel"))}, '
                   f'{L("sustain", "EG2.Sustain")} {fmt(val("EG2.Sustain"))}.{amp} [[{UG["env"]}]]')
    mode = val('EG1.Mode')
    if mode is not None and 0 <= mode < 3:
        parts = [f'{L(n.split(".")[1], n)} {fmt(val(n))}' for n in
                 ('EG1.RiseLvl', 'EG1.RiseSlp', 'EG1.FallLvl', 'EG1.FallSlp', 'EG1.Hold', 'EG1.Amount')
                 if val(n) is not None]
        env.append(f'Cycling Envelope {L("mode", "EG1.Mode")}: '
                   f'{link(CYC_MODES[mode], PAGES["EG1.Mode"] + "/" + CYC_MODES[mode], linked)}. '
                   f'Stored {", ".join(parts)}. [[{UG["cycling"]}]]')
    if env:
        out.append(('Envelopes', env))
    shape = val('LFO.Shape')
    if shape is not None and 0 <= shape < 6:
        label, panel = LFO_SHAPES[shape]
        if val('LFO.Sync') == 1:
            rate = f'clock {L("sync", "LFO.Sync")} on; stored division code: {val("LFO.Div")}'
        else:
            rate = f'clock {L("sync", "LFO.Sync")} off; stored normalized {L("rate", "LFO.Rate")}: {fmt(val("LFO.Rate"))}'
        out.append(('LFO', [f'{link(label, PAGES["LFO.Shape"] + "/" + panel, linked)}, {rate}. {UG["lfo"]}']))
    assigns = assign_labels(fields, address, linked)
    mat = []
    for col_index, column in enumerate(COLUMNS, 1):
        for row, row_label, row_page in ROWS:
            amount = val(f'Co{col_index}.{row}')
            if amount:
                dest = link(column, COLUMN_PAGES[column], linked) if column in COLUMN_PAGES else column
                if column.startswith('Assign'):
                    dest = (f'{dest} → {assigns[column]}' if assigns[column]
                            else f'{dest} (unresolved destination)')
                mat.append(f'{link(row_label, row_page, linked)} → {dest}: {signed(amount)}.')
    intro = 'Amounts' if not linked else link('Amounts', MATRIX + '/Knob')
    if mat:
        mat.insert(0, f'{intro} use the signed normalized range −1…+1. [[{UG["matrix"]}]]')
        mat.append('All other saved matrix amounts are zero.')
    else:
        mat.append(f'All saved matrix {"amounts" if not linked else link("amounts", MATRIX + "/Knob")} are zero.')
    out.append(('Modulation matrix', mat))
    if val('Gen.Parafon') is not None:
        state = 'on' if val('Gen.Parafon') == 1 else 'off'
        out.append(('Voice and keyboard', [f'{L("Paraphonic", "Gen.Parafon")} mode: {state}.']))
    return out


def shown_value(name, field, model):
    value = field['value']
    if name == 'VCO.Type':
        return model or f'index {value}'
    if name == 'Kbd.Octave':
        return OCTAVES[value] if 0 <= value < 7 else str(value)
    if name == 'VCF.Type':
        return FILTERS[value][2] if 0 <= value < 3 else str(value)
    if name == 'EG1.Mode':
        return CYC_MODES[value] if 0 <= value < 3 else str(value)
    if name == 'LFO.Shape':
        return LFO_SHAPES[value][1] if 0 <= value < 6 else str(value)
    if name in ('EG2.Mode', 'LFO.Sync', 'Gen.Parafon', 'Arp.Enable', 'Arp.SeqOn'):
        return {0: 'off', 1: 'on'}.get(value, str(value))
    if field['kind'] == 'normalized_0_1':
        return fmt(value)
    if field['kind'] == 'normalized_minus_1_1':
        return signed(value)
    return str(value)


def differs(a, b):
    if a is None or b is None:
        return a is not b
    if isinstance(a['value'], float) or isinstance(b['value'], float):
        return abs(a['value'] - b['value']) > TOLERANCE
    return a['value'] != b['value']


def customized(interp, base, address, linked=True):
    """Return one line per control whose saved value differs from ``base``."""
    mine, theirs = values(interp), values(base)
    model = interp['oscillator']['model'] if interp['oscillator'] else None
    base_model = base['oscillator']['model'] if base['oscillator'] else None
    lines = []
    for name in CUSTOMIZED:
        a, b = mine.get(name), theirs.get(name)
        if not differs(a, b) or 'raw_only' in (a and a['kind'], b and b['kind']):
            continue
        if name.startswith('VCO.Param') and model != base_model:
            continue
        if name.startswith('VCO.Param'):
            position = int(name[-1])
            label = a['label'] if a and a['label'] != name else PANEL_KNOBS[position - 1] + ' control'
            page = param_page(model, position, label)
        else:
            label, page = NAMES[name], PAGES[name]
        new = shown_value(name, a, model) if a else 'not saved'
        old = shown_value(name, b, base_model) if b else 'not saved'
        lines.append(f'{link(label, page, linked)}: {new} (factory {old}).')
    for col_index, column in enumerate(COLUMNS, 1):
        for row, row_label, _ in ROWS:
            key = f'Co{col_index}.{row}'
            a, b = mine.get(key), theirs.get(key)
            if differs(a, b):
                new = signed(a['value']) if a else 'not saved'
                old = signed(b['value']) if b else 'not saved'
                lines.append(f'{link("Matrix", MATRIX + "/Knob", linked)} {row_label} → {column}: {new} (factory {old}).')
    mine_assign = assign_labels(mine, address, linked)
    base_assign = assign_labels(theirs, address, linked)
    for n in (1, 2, 3):
        column = f'Assign {n}'
        raw_a = mine.get(f'Mat.Assign{n}')
        raw_b = theirs.get(f'Mat.Assign{n}')
        if differs(raw_a, raw_b):
            lines.append(f'{link(column, COLUMN_PAGES[column], linked)} destination: '
                         f'{mine_assign[column] or "unresolved"} (factory {base_assign[column] or "unresolved"}).')
    return lines


def factory_payloads(root=FACTORY):
    """Return {payload sha256: (archive, slot, file name, preset name, interpretation)}."""
    found = {}
    for path in sorted(root.glob('*/*/*.mbp')):
        try:
            payload, meta = parameters.load_preset(path)
        except (OSError, ValueError):
            continue
        if meta.get('initialized') or meta['payload_sha256'] in found:
            continue
        try:
            interp = semantics.interpret_fields(parameters.parse_parameters(payload)['fields'])
        except parameters.UnsupportedLayout:
            continue
        match = re.match(r'(\d+)-', path.name)
        found[meta['payload_sha256']] = (path.parent.parent.name, int(match[1]) if match else None,
                                         path.name, meta.get('name'), interp)
    return found


def nearest(interp, factory, address):
    """Return (count, sha, entry) for the factory payload with the fewest differences."""
    best = None
    for sha, entry in factory.items():
        count = len(customized(interp, entry[4], address, linked=False))
        if best is None or count < best[0]:
            best = (count, sha, entry)
    return best


def factory_page(garden, name):
    """Return the garden page title of the factory preset called ``name``, if one exists."""
    for path in sorted((garden / 'pages').glob('Microfreak___Preset___[0-9][0-9][0-9] *.md')):
        if '___Asset___' in path.name:
            continue
        text = path.read_text()
        if (f'preset-synth-microfreak-name:: {name}\n' in text
                and 'preset-synth-origin/Factory]]' in text):
            return path.stem.replace('___', '/')
    return None


def customized_section(interp, factory, address, garden, linked=True):
    count, _, (archive, slot, _, name, base) = nearest(interp, factory, address)
    source = f'{archive.replace("Factory", "Factory ")} slot {slot}' if slot else archive
    page = factory_page(garden, name) if linked else None
    shown = f'[[{page}]]' if page else f'“{name}”'
    if count > NEAREST_LIMIT:
        return [f'No factory preset is close. The nearest factory payload, {shown} ({source}), '
                f'differs in {count} controls.']
    if count == 0:
        return [f'Every control listed on this page matches the nearest factory payload, {shown} ({source}); '
                'the saved payload differs only in settings these sections do not show.']
    differ = '1 control differs' if count == 1 else f'{count} controls differ'
    lines = [f'Compared with the nearest factory payload, {shown} ({source}); {differ}.']
    return lines + customized(interp, base, address, linked)


def split_page(text):
    """Return (frontmatter lines, body lines)."""
    lines = text.rstrip('\n').split('\n')
    index = next((i for i, line in enumerate(lines) if line.startswith('- ')), len(lines))
    return lines[:index], lines[index:]


def section_spans(body):
    """Yield (title, start, end) for each level-2 section in a generated body."""
    starts = [(i, line[len('\t- ## '):]) for i, line in enumerate(body) if line.startswith('\t- ## ')]
    for n, (i, title) in enumerate(starts):
        end = starts[n + 1][0] if n + 1 < len(starts) else len(body)
        yield title, i, end


def strip_links(line):
    """Turn ``[label]([[page]])`` back into ``label``."""
    return re.sub(r'\[([^\]]+)\]\(\[\[[^\]]+\]\]\)', r'\1', line)


def is_generated(body):
    return any('Two consecutive reads returned the same file.' in line for line in body)


def render(sections):
    lines = []
    for title, items in sections:
        lines.append(f'\t- ## {title}')
        lines += [f'\t\t- {item}' for item in items]
    return lines


def replace_sections(body, sections):
    """Replace the generated decoded-setting sections; keep provenance and evidence."""
    spans = [s for s in section_spans(body) if s[0] in GENERATED_SECTIONS]
    if not spans:
        raise ValueError('no generated sections')
    first, last = spans[0][1], spans[-1][2]
    if any(t not in GENERATED_SECTIONS for t, s, e in section_spans(body) if first <= s < last):
        raise ValueError('a handwritten section sits among the generated ones')
    return body[:first] + render(sections) + body[last:]


def frontmatter_set(front, key, value):
    for i, line in enumerate(front):
        if line.startswith(key + ':: '):
            front[i] = f'{key}:: {value}'
            return front
    front.append(f'{key}:: {value}')
    return front


def asset_names(page_title, date):
    asset_page = f'{page_title}/Asset/Device-Read-{date}/bin'
    filename = asset_page.rsplit('/', 1)[0].replace('/', '___') + '.bin'
    return asset_page, filename, B2 + quote(filename, safe='')


def long_date(date):
    day = dt.date.fromisoformat(date)
    return f'{day:%B} {day.day}, {day.year}'


def asset_text(name, slot, url, raw_sha, date):
    return ('logseq-entity:: [[Logseq/Entity/Asset/B2]]\n'
            f'- # {name} slot {slot} capture\n'
            f'\t- [Download the slot {slot} capture]({url})\n'
            f'\t- Read from the connected MicroFreak\'s slot {slot} over USB on {long_date(date)} with '
            f'`mise run microfreak:download --slot {slot}`. The file is the preset header followed by the unmodified data packets '
            'the device sends, as described in [the download task](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py). '
            f'It is not a MIDI Control Center `.mbp` file. SHA-256: `{raw_sha}`.\n')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    parser.add_argument('--garden', type=Path, required=True)
    parser.add_argument('--reads', type=Path, required=True, help='First pass of microfreak:download reads')
    parser.add_argument('--reads2', type=Path, help='Second pass; required to back up a slot')
    parser.add_argument('--live-map', type=Path, default=Path(__file__).with_name('freakout_live_map.py'),
                        help="Freakout's microfreak_live_map.py (default: the vendored copy)")
    parser.add_argument('--slots', required=True, help='Slot range, e.g. 1-400')
    parser.add_argument('--date', default=dt.date.today().isoformat(), help='Read date for new backups')
    parser.add_argument('--backup', action='store_true',
                        help='Also add file, digest and provenance to pages that lack a device-read file')
    parser.add_argument('--upload-dir', type=Path, help='Copy new backup files here for upload')
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args(argv)
    first, _, last = args.slots.partition('-')
    address = load_live_map(args.live_map)
    factory = factory_payloads()
    for slot in range(int(first), int(last or first) + 1):
        plan = run_slot(args, slot, address, factory)
        if plan:
            print(json.dumps(plan, ensure_ascii=False))
    return 0


def run_slot(args, slot, address, factory):
    manifest = args.reads / f'slot-{slot:03d}.json'
    if not manifest.exists():
        return None
    meta = json.loads(manifest.read_text())
    plan = {'slot': slot, 'name': meta['name']}
    pages = [p for p in sorted((args.garden / 'pages').glob(f'Microfreak___Preset___{slot:03d} *.md'))
             if '___Asset___' not in p.name]
    if len(pages) != 1:
        return dict(plan, skip=f'{len(pages)} pages for slot')
    page = pages[0]
    text = page.read_text()
    front, body = split_page(text)
    props = dict(re.findall(r'^([a-z0-9-]+):: (.*)$', '\n'.join(front), re.M))
    if props.get('preset-synth-microfreak-name') != meta['name']:
        return dict(plan, skip='page name differs from device')
    binary = args.reads / meta['raw_file']
    payload, info = parameters.load_preset(binary)
    interp = interpret(binary)
    is_factory = info['payload_sha256'] in factory
    plan.update(page=page.name, factory=is_factory)
    recorded = props.get('preset-synth-microfreak-parameter-payload-sha256')
    has_file = 'preset-synth-file' in props
    if has_file and recorded and recorded != info['payload_sha256']:
        return dict(plan, skip='device payload differs from the page; back it up again first')
    sections = describe(interp, address)
    if not is_factory:
        sections.append(('Customized controls', customized_section(interp, factory, address, args.garden)))
    new_front, new_body, asset = list(front), list(body), None
    if is_generated(body):
        plain = render(describe(interp, address, linked=False))
        current = [l for t, s, e in section_spans(body) if t in GENERATED_SECTIONS[:-1] for l in body[s:e]]
        if plain != [strip_links(line) for line in current]:
            return dict(plan, skip='generated sections differ from the device read')
        new_body = replace_sections(body, sections)
        plan['action'] = 'link'
    elif not has_file and args.backup:
        second = args.reads2 / meta['raw_file'] if args.reads2 else None
        if not second or not second.exists() or second.read_bytes() != binary.read_bytes():
            return dict(plan, skip='second read missing or different')
        title = page.stem.replace('___', '/')
        asset_page, filename, url = asset_names(title, args.date)
        stub = {'- # Notes', f'- # {meta["name"]}', '-', ''}
        handwritten = any(line not in stub for line in body)
        origin = 'Factory' if is_factory else 'Custom'
        frontmatter_set(new_front, PREFIX + 'origin', ORIGIN.format(origin))
        model = interp['oscillator']['model'] if interp['oscillator'] else None
        if model and 'preset-synth-microfreak-oscillator-type' not in props:
            new_front.append(f'preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/{MODELS[model][0]}]]')
        frontmatter_set(new_front, 'preset-synth-microfreak-parameter-payload-sha256', info['payload_sha256'])
        frontmatter_set(new_front, PREFIX + 'file',
                        f'[{meta["name"]} — {long_date(args.date).rsplit(",", 1)[0]} slot {slot} capture]({url})')
        frontmatter_set(new_front, PREFIX + 'file-sha256', meta['raw_sha256'])
        asset = (asset_page, asset_text(meta['name'], slot, url, meta['raw_sha256'], args.date), filename, binary)
        if handwritten:
            plan['action'] = 'frontmatter'
            if not is_factory and not any(t == 'Customized controls' for t, _, _ in section_spans(body)):
                new_body = body + render([('Customized controls', customized_section(interp, factory, address, args.garden))])
                plan['action'] = 'frontmatter and customized controls'
        else:
            if is_factory:
                matches = ', '.join(sorted({e[0] for s, e in factory.items() if s == info['payload_sha256']}))
                origin_line = f'\t\t- The parameter payload matches the MIDI Control Center factory archive {matches}.'
            else:
                origin_line = '\t\t- The parameter payload matches no MIDI Control Center factory archive.'
            new_body = (['- # Notes', '\t- ## Saved export and provenance',
                         f'\t\t- Saved export: read from the device\'s slot {slot} over USB on {long_date(args.date)} with '
                         f'`mise run microfreak:download --slot {slot}`. Two consecutive reads returned the same file.',
                         origin_line,
                         f'\t\t- [Download the slot {slot} capture]({url}). It is the raw device format (header plus data packets), '
                         f'not an `.mbp` file; see [[{asset_page}]].']
                        + render(sections) + EVIDENCE)
            plan['action'] = 'backup'
        plan.update(url=url, raw_sha256=meta['raw_sha256'], payload_sha256=info['payload_sha256'], origin=origin)
    elif not is_factory and any(t == 'Customized controls' for t, _, _ in section_spans(body)):
        title, start, end = next(x for x in section_spans(body) if x[0] == 'Customized controls')
        new_body = body[:start] + render([sections[-1]]) + body[end:]
        plan['action'] = 'customized controls'
    else:
        return dict(plan, skip='handwritten page' if not is_generated(body) else 'no change')
    new_text = '\n'.join(new_front + new_body) + '\n'
    if new_text == text and not asset:
        return dict(plan, skip='no change')
    if args.apply:
        page.write_text(new_text)
        if asset:
            asset_page, content, filename, source = asset
            (args.garden / 'pages' / (asset_page.replace('/', '___') + '.md')).write_text(content)
            if args.upload_dir:
                args.upload_dir.mkdir(parents=True, exist_ok=True)
                (args.upload_dir / filename).write_bytes(source.read_bytes())
    return plan


if __name__ == '__main__':
    sys.exit(main())
