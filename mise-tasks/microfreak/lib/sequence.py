#!/usr/bin/env python3
"""Decode and encode the sequencer patterns stored in a MicroFreak preset.

The layout and the experiments behind each field are on the garden page
Microfreak/Sequence/Storage:
https://github.com/codekiln/logseq-encode-garden/blob/main/pages/Microfreak___Sequence___Storage.md
It follows Freakout's sequence parser, src/minifreak_patch/microfreak_sequence.py
(https://github.com/kmorrill/freakout), checked here against the notes the
instrument sends while it plays uploaded presets.

Offsets count from the start of the 4088 expanded data (see
parameters.unpack_payload). Pattern A starts at 1980 and pattern B at 3022.
Each is 64 step records of 16 followed by an 18-long pattern trailer:

  step record   0-3   note per voice, 0x80 and above = no voice; the
                      instrument plays voices up to the first empty one
                4-7   velocity per voice, 1-127
                8-11  modulation-track value per track, 0-255
                12    0 rest, 1 note, 2 note held into the next step
                13    bit n set = track n+1 holds a value on this step
                14-15 zero
  trailer       0-7   four little-endian modulation-track destinations,
                      0xFFFF = track unused
                8     copy of the gate length (Seq.GateLen decides)
                9     copy of the sequence length (Seq.Length decides)
                16    0xA5 = pattern in use; 0xFF = erased, plays nothing
                10-15, 17 kept as found

Length, gate length and smoothing are the named Seq.Length, Seq.GateLen and
Seq.Smooth1-4 parameters; both patterns share them.
"""
import json
from pathlib import Path

import parameters

PATTERN_OFFSETS = {'A': 1980, 'B': 3022}
STEPS = 64
STEP_SIZE = 16
TRAILER_SIZE = 18
VOICES = 4
TRACKS = 4
EMPTY_NOTE = 0xFF
BLANK_VELOCITY = 100
STATUS_NAMES = {0: 'rest', 1: 'note', 2: 'tie'}
STATUS_CODES = {name: code for code, name in STATUS_NAMES.items()}
# The instrument writes 0xA5 at trailer offset 16 of a pattern that holds
# steps and 0xFF in an erased pattern.
PATTERN_IN_USE = 0xA5
PATTERN_ERASED = 0xFF
LENGTH_RANGE = (4, 64)
GATE_RANGE = (10, 90)
SWITCH_ON = 32767
NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


def note_name(number):
    """Name a MIDI note with middle C (60) as C4."""
    return f'{NOTE_NAMES[number % 12]}{number // 12 - 1}'


def note_number(name):
    """Return the MIDI note for a name such as C4, F#3 or Eb2 (C4 = 60)."""
    if isinstance(name, int):
        number = name
    else:
        text = name.strip()
        letter, rest = text[:1].upper(), text[1:]
        if letter not in 'CDEFGAB' or not rest:
            raise ValueError(f'Unknown note name {name!r}')
        offset = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}[letter]
        while rest[:1] in ('#', 'b'):
            offset += 1 if rest[0] == '#' else -1
            rest = rest[1:]
        try:
            octave = int(rest)
        except ValueError as exc:
            raise ValueError(f'Unknown note name {name!r}') from exc
        number = (octave + 1) * 12 + offset
    if not 0 <= number <= 127:
        raise ValueError(f'Note {name!r} is outside MIDI notes 0-127')
    return number


def pack_payload(data):
    """Inverse of parameters.unpack_payload: 4088 values to 4672 7-bit values."""
    if len(data) != 4088:
        raise ValueError('Expected 4088 expanded values')
    result = bytearray()
    for start in range(0, len(data), 7):
        block = data[start:start + 7]
        result.append(sum((v >> 7) << bit for bit, v in enumerate(block)))
        result.extend(v & 0x7F for v in block)
    return bytes(result)


def length_from_raw(value):
    low, high = LENGTH_RANGE
    return low + round(value * (high - low) / 32767)


def length_to_raw(steps):
    low, high = LENGTH_RANGE
    return round((steps - low) * 32767 / (high - low))


def gate_from_raw(value):
    low, high = GATE_RANGE
    return low + round(value * (high - low) / 32767)


def gate_to_raw(percent):
    low, high = GATE_RANGE
    return round((percent - low) * 32767 / (high - low))


def destination_names():
    """Map modulation-track destination ids to named parameters.

    The ids are the live-parameter addresses in Freakout's hardware map.
    """
    import freakout_live_map
    names = {}
    for field, addresses in freakout_live_map.MICROFREAK_STRUCTURED_LIVE_WORDS.items():
        for address in addresses:
            names.setdefault(address, field)
    return names


def seq_fields(fields):
    return {f['name']: f for f in fields if f['name'].startswith('Seq.')}


def decode_step(record, number):
    voices = 0
    while voices < VOICES and record[voices] < 0x80:
        voices += 1
    notes = list(record[:voices])
    status = STATUS_NAMES.get(record[12], f'unknown-{record[12]}')
    step = {'step': number, 'status': status}
    if notes and status != 'rest':
        step['notes'] = notes
        step['note_names'] = [note_name(n) for n in notes]
        step['velocities'] = list(record[4:4 + voices])
    elif notes:
        step['stored_notes'] = notes
    mods = [record[8 + track] if record[13] >> track & 1 else None for track in range(TRACKS)]
    if any(v is not None for v in mods):
        step['mod'] = mods
    stranded = any(record[v] < 0x80 for v in range(voices, VOICES))
    if stranded or record[12] not in STATUS_NAMES or record[13] >> TRACKS or record[14] or record[15]:
        step['raw_hex'] = bytes(record).hex()
    return step


def decode_pattern(data, name, length, names=None):
    names = destination_names() if names is None else names
    offset = PATTERN_OFFSETS[name]
    trailer = data[offset + STEPS * STEP_SIZE:offset + STEPS * STEP_SIZE + TRAILER_SIZE]
    tracks = []
    for track in range(TRACKS):
        dest = int.from_bytes(trailer[2 * track:2 * track + 2], 'little')
        if dest == 0xFFFF:
            tracks.append(None)
        else:
            tracks.append({'track': track + 1, 'destination_id': f'0x{dest:04x}',
                           'destination': names.get(dest)})
    steps = [decode_step(data[offset + i * STEP_SIZE:offset + (i + 1) * STEP_SIZE], i + 1)
             for i in range(STEPS)]
    played = steps[:length]
    return {
        'pattern': name,
        'unpacked_offset': offset,
        'in_use': trailer[16] == PATTERN_IN_USE,
        'gate_percent': trailer[8],
        'length_copy': trailer[9],
        'mod_tracks': tracks,
        'steps': played,
        'unplayed_steps_with_notes': sum(
            1 for s in steps[length:] if s['status'] != 'rest' or 'stored_notes' in s),
        'trailer_hex': bytes(trailer).hex(),
    }


def decode_sequence(payload):
    """Return both patterns of a 4672-value preset payload as plain data."""
    report = parameters.parse_parameters(payload)
    data = parameters.unpack_payload(payload)
    if report['parameter_end_offset'] > PATTERN_OFFSETS['A']:
        raise parameters.UnsupportedLayout('Named parameters overlap the sequence area')
    seq = seq_fields(report['fields'])
    if 'Seq.Length' not in seq:
        raise parameters.UnsupportedLayout('Preset has no Seq.Length field')
    length = length_from_raw(seq['Seq.Length']['value_le_unsigned'])
    result = {'length': length, 'note_name_convention': 'C4 = MIDI 60'}
    if 'Seq.GateLen' in seq:
        result['gate_percent'] = gate_from_raw(seq['Seq.GateLen']['value_le_unsigned'])
    result['smoothing'] = [bool(seq[f'Seq.Smooth{n}']['value_le_unsigned'])
                           if f'Seq.Smooth{n}' in seq else None for n in range(1, 5)]
    names = destination_names()
    result['patterns'] = {name: decode_pattern(data, name, length, names)
                          for name in PATTERN_OFFSETS}
    return result


def blank_step():
    return bytes([EMPTY_NOTE] * VOICES + [BLANK_VELOCITY] * VOICES + [0] * 8)


def encode_step(step):
    """Return the 16-value record for one step description.

    A step is a dict with optional keys: notes (list of up to four note
    numbers or names), velocity (one value or one per note, default 100),
    tie (true holds the notes into the next step; the next step usually
    repeats them), mod (four values 0-255 or None). A step with no notes is
    a rest.
    """
    if step is None:
        step = {}
    notes = [note_number(n) for n in step.get('notes', [])]
    if len(notes) > VOICES:
        raise ValueError('A step holds at most four notes')
    velocity = step.get('velocity', step.get('velocities', BLANK_VELOCITY))
    velocities = list(velocity) if isinstance(velocity, (list, tuple)) else [velocity] * len(notes)
    if len(velocities) != len(notes) or any(not 1 <= v <= 127 for v in velocities):
        raise ValueError('Give one velocity from 1 to 127, or one per note')
    record = bytearray(blank_step())
    for voice, (note, vel) in enumerate(zip(notes, velocities)):
        record[voice], record[4 + voice] = note, vel
    if notes:
        record[12] = STATUS_CODES['tie'] if step.get('tie') else STATUS_CODES['note']
        for voice in range(len(notes), VOICES):
            record[4 + voice] = 0
    elif step.get('tie'):
        raise ValueError('A rest cannot be tied')
    else:
        record[4:8] = bytes(VOICES)
    mods = step.get('mod') or [None] * TRACKS
    if len(mods) != TRACKS:
        raise ValueError('Give four modulation values (or None) per step')
    for track, value in enumerate(mods):
        if value is not None:
            if not 0 <= value <= 255:
                raise ValueError('Modulation values run from 0 to 255')
            record[8 + track] = value
            record[13] |= 1 << track
    return bytes(record)


def set_field(data, fields, name, value):
    field = fields.get(name)
    if field is None:
        raise ValueError(f'Base preset has no {name} field to set')
    offset = field['unpacked_value_offset'] + 1
    data[offset:offset + 2] = value.to_bytes(2, 'little')


def encode_sequence(payload, sequence):
    """Write a sequence description into a copy of a preset payload.

    sequence keys: length (4-64, shared by both patterns), gate_percent
    (10-90, optional), smoothing (four booleans, optional), and patterns:
    {'A': pattern, 'B': pattern}. A pattern is a dict with steps (a list of at
    most 64 step dicts, see encode_step) and optional mod_tracks (four
    destination ids or None). Patterns left out keep their stored data.
    Every other value in the payload is kept.
    """
    report = parameters.parse_parameters(payload)
    fields = seq_fields(report['fields'])
    data = bytearray(parameters.unpack_payload(payload))
    length = sequence.get('length')
    if length is None:
        length = length_from_raw(fields['Seq.Length']['value_le_unsigned'])
    if not LENGTH_RANGE[0] <= length <= LENGTH_RANGE[1]:
        raise ValueError('Sequence length runs from 4 to 64 steps')
    set_field(data, fields, 'Seq.Length', length_to_raw(length))
    gate = sequence.get('gate_percent')
    if gate is not None:
        if not GATE_RANGE[0] <= gate <= GATE_RANGE[1]:
            raise ValueError('Gate length runs from 10 to 90 percent')
        set_field(data, fields, 'Seq.GateLen', gate_to_raw(gate))
    for n, on in enumerate(sequence.get('smoothing') or [], start=1):
        if on is not None:
            set_field(data, fields, f'Seq.Smooth{n}', 32767 if on else 0)
    for name, offset in PATTERN_OFFSETS.items():
        trailer = offset + STEPS * STEP_SIZE
        data[trailer + 9] = length
        if gate is not None:
            data[trailer + 8] = gate
        pattern = (sequence.get('patterns') or {}).get(name)
        if pattern is None:
            continue
        steps = pattern.get('steps', [])
        if len(steps) > STEPS:
            raise ValueError('A pattern holds at most 64 steps')
        for index in range(STEPS):
            record = encode_step(steps[index]) if index < len(steps) else blank_step()
            data[offset + index * STEP_SIZE:offset + (index + 1) * STEP_SIZE] = record
        tracks = pattern.get('mod_tracks') or [None] * TRACKS
        if len(tracks) != TRACKS:
            raise ValueError('Give four modulation-track destinations (or None)')
        for track, dest in enumerate(tracks):
            value = 0xFFFF if dest is None else int(dest, 0) if isinstance(dest, str) else dest
            data[trailer + 2 * track:trailer + 2 * track + 2] = value.to_bytes(2, 'little')
        in_use = any(s and (s.get('notes') or any(v is not None for v in s.get('mod') or []))
                     for s in steps)
        data[trailer + 16] = PATTERN_IN_USE if in_use else PATTERN_ERASED
    return pack_payload(bytes(data))


def stored_form(sequence):
    """Return the description the way the instrument can store it.

    The shortest sequence the instrument holds is 4 steps. A description of
    1-3 steps is repeated to fill 4 or 6 steps (1 to 4, 2 to 4, 3 to 6), which
    plays the same loop. Other descriptions come back unchanged.
    """
    length = sequence.get('length')
    if length is None or length >= LENGTH_RANGE[0]:
        return sequence
    if length < 1:
        raise ValueError('Sequence length runs from 1 to 64 steps')
    repeats = -(-LENGTH_RANGE[0] // length)
    patterns = {}
    for name, pattern in (sequence.get('patterns') or {}).items():
        steps = list(pattern.get('steps', []))
        if len(steps) > length:
            raise ValueError(f'Pattern {name} has {len(steps)} steps for a length of {length}')
        if not any(s and (s.get('notes') or s.get('mod')) for s in steps):
            patterns[name] = dict(pattern, steps=[])
            continue
        steps += [{}] * (length - len(steps))
        patterns[name] = dict(pattern, steps=steps * repeats)
    return dict(sequence, length=length * repeats, patterns=patterns)


def make_playable(payload, sequence):
    """Write a description and turn on the settings that let it play.

    Returns the new payload and the named settings it changed, as
    {name: [before, after]}. Arp.SeqOn on puts the preset in sequencer mode;
    Gen.Parafon on lets a step sound more than its lowest note, so it is turned
    on when a step holds a chord.
    """
    new = bytearray(parameters.unpack_payload(encode_sequence(payload, stored_form(sequence))))
    fields = {f['name']: f for f in parameters.parse_parameters(payload)['fields']}
    wanted = {'Arp.SeqOn': SWITCH_ON}
    chords = any(len(step.get('notes') or []) > 1
                 for pattern in (sequence.get('patterns') or {}).values()
                 for step in pattern.get('steps', []) if step)
    if chords:
        wanted['Gen.Parafon'] = SWITCH_ON
    changed = {}
    for name, value in wanted.items():
        before = fields[name]['value_le_unsigned'] if name in fields else None
        if before != value:
            set_field(new, fields, name, value)
            changed[name] = [before, value]
    return pack_payload(bytes(new)), changed


def describe_step(step):
    """Turn one decoded step into the description format."""
    result = {}
    if 'notes' in step:
        result['notes'] = step['note_names']
        velocities = step['velocities']
        result['velocity'] = velocities[0] if len(set(velocities)) == 1 else velocities
        if step['status'] == 'tie':
            result['tie'] = True
    if 'mod' in step:
        result['mod'] = step['mod']
    return result


def describe(decoded):
    """Turn decode_sequence output back into a sequence description.

    Each pattern lists its played steps, with trailing rests left out, its
    modulation-track destinations, and in_use, false for an erased pattern.
    """
    result = {'length': decoded['length']}
    for key in ('gate_percent', 'smoothing'):
        if key in decoded:
            result[key] = decoded[key]
    result['patterns'] = {}
    for name, pattern in decoded['patterns'].items():
        steps = [describe_step(s) for s in pattern['steps']]
        while steps and not steps[-1]:
            steps.pop()
        result['patterns'][name] = {
            'in_use': pattern['in_use'],
            'steps': steps,
            'mod_tracks': [t['destination_id'] if t else None for t in pattern['mod_tracks']],
        }
    return result


def _canonical_step(step):
    step = step or {}
    notes = [note_number(n) for n in step.get('notes', [])]
    result = {}
    if notes:
        velocity = step.get('velocity', step.get('velocities', BLANK_VELOCITY))
        velocities = list(velocity) if isinstance(velocity, (list, tuple)) else [velocity] * len(notes)
        result = {'notes': notes, 'velocities': velocities}
        if step.get('tie'):
            result['tie'] = True
    mods = step.get('mod')
    if mods and any(v is not None for v in mods):
        result['mod'] = list(mods)
    return result


def _destination(value):
    if value is None:
        return None
    return int(value, 0) if isinstance(value, str) else int(value)


def canonical_pattern(pattern, length):
    """Steps 1 to length with note numbers and per-note velocities, for comparing."""
    steps = [_canonical_step(s) for s in pattern.get('steps', [])[:length]]
    steps += [{}] * (length - len(steps))
    tracks = pattern.get('mod_tracks') or [None] * TRACKS
    return {'steps': steps, 'mod_tracks': [_destination(t) for t in tracks]}


def differences(sequence, decoded):
    """List where a decoded preset differs from a description.

    Only what the description sets is compared: the length, the gate length
    and smoothing when given, and the patterns it lists. Short descriptions
    are compared in their stored form (see stored_form).
    """
    sequence = stored_form(sequence)
    found = []
    length = sequence.get('length', decoded['length'])
    if length != decoded['length']:
        found.append(f"length: described {length}, stored {decoded['length']}")
    if sequence.get('gate_percent') is not None and sequence['gate_percent'] != decoded.get('gate_percent'):
        found.append(f"gate_percent: described {sequence['gate_percent']}, "
                     f"stored {decoded.get('gate_percent')}")
    for n, on in enumerate(sequence.get('smoothing') or [], start=1):
        if on is not None and bool(on) != decoded['smoothing'][n - 1]:
            found.append(f'smoothing {n}: described {bool(on)}, stored {decoded["smoothing"][n - 1]}')
    stored = describe(decoded)['patterns']
    for name, pattern in (sequence.get('patterns') or {}).items():
        want = canonical_pattern(pattern, decoded['length'])
        got = canonical_pattern(stored[name], decoded['length'])
        in_use = any(s.get('notes') or s.get('mod') for s in want['steps'])
        if in_use != stored[name]['in_use']:
            found.append(f'{name}: described {"in use" if in_use else "erased"}, '
                         f'stored {"in use" if stored[name]["in_use"] else "erased"}')
        for number, (w, g) in enumerate(zip(want['steps'], got['steps']), start=1):
            if w != g:
                found.append(f'{name} step {number}: described {w or "rest"}, stored {g or "rest"}')
        if want['mod_tracks'] != got['mod_tracks']:
            found.append(f"{name} mod_tracks: described {want['mod_tracks']}, stored {got['mod_tracks']}")
    return found


def load_description(path):
    """Read a sequence description from a JSON or YAML file."""
    text = Path(path).read_text()
    if Path(path).suffix.lower() in ('.yaml', '.yml'):
        try:
            import yaml
        except ImportError as exc:
            raise ValueError('Reading YAML needs PyYAML; run the mise task, which installs it') from exc
        sequence = yaml.safe_load(text)
    else:
        sequence = json.loads(text)
    if not isinstance(sequence, dict):
        raise ValueError(f'{path} does not hold a sequence description')
    return sequence
