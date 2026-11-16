#!/usr/bin/env python3
"""Turn the MicroFreak's own MIDI output during clocked playback into steps.

With Arp/Seq MIDI Out on, the MicroFreak sends a Note On and Note Off for every
sequencer note, with the stored velocity, and a Control Change for every
modulation-track value. During playback it also sends a Clock for every Clock
it receives. This module counts those echoed clocks to place each message on
the step grid, so it needs no audio and no knowledge of the preset format.

Standard library only; `audition.py` feeds it captured messages.
"""

NOTE_NAMES = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
CLOCK, START, STOP = 0xF8, 0xFA, 0xFC


def note_name(note):
    """Scientific pitch name, where MIDI note 60 is C4."""
    return f'{NOTE_NAMES[note % 12]}{note // 12 - 1}'


def _positions(events):
    """Yield (event, clock count, reference) for every non-clock message.

    The count is the number of clocks the instrument echoed before the
    message. When it echoed none, the count falls back to the clocks the
    host had sent when the message arrived.
    """
    echoed = any(e['data'][:1] == [CLOCK] for e in events)
    count = 0
    for event in events:
        status = event['data'][0]
        if status == CLOCK:
            count += 1
            continue
        yield event, (count if echoed else event['host_clocks']), (
            'device_clock_echo' if echoed else 'host_clocks_sent')


def _step_of(count, clocks_per_step):
    # Start plays step 1 at once; the clock that ends step k's first tick is
    # the (k * clocks_per_step + 1)th, so a message at count c sits at tick c - 1.
    return max(0, round((count - 1) / clocks_per_step))


def collect_notes(events, clocks_per_step):
    """Pair Note On and Note Off messages into notes placed on the step grid."""
    open_notes, notes, ccs, reference = {}, [], [], 'host_clocks_sent'
    stop = None
    for event, count, reference in _positions(events):
        data = event['data']
        status = data[0]
        kind, channel = status & 0xF0, (status & 0x0F) + 1
        if status == STOP and stop is None:
            stop = count
        elif kind == 0x90 and len(data) == 3 and data[2] > 0:
            key = (channel, data[1])
            if key in open_notes:  # retrigger without a Note Off
                notes.append(_close(open_notes.pop(key), count, clocks_per_step, False))
            open_notes[key] = dict(channel=channel, note=data[1], velocity=data[2],
                                   on_count=count,
                                   step_index=_step_of(count, clocks_per_step))
        elif kind in (0x80, 0x90) and len(data) == 3:
            key = (channel, data[1])
            if key in open_notes:
                notes.append(_close(open_notes.pop(key), count, clocks_per_step, False))
        elif kind == 0xB0 and len(data) == 3:
            ccs.append(dict(channel=channel, control=data[1], value=data[2],
                            step_index=_step_of(count, clocks_per_step)))
    for note in open_notes.values():
        notes.append(_close(note, stop if stop is not None else note['on_count'],
                            clocks_per_step, True))
    notes.sort(key=lambda n: (n['step_index'], n['note']))
    return notes, ccs, reference


def _close(note, off_count, clocks_per_step, cut):
    on_tick = max(0, note['on_count'] - 1)
    off_tick = max(on_tick, off_count - 1)
    result = dict(note)
    result.update(off_tick=off_tick, on_tick=on_tick, gate_ticks=off_tick - on_tick,
                  gate_steps=round((off_tick - on_tick) / clocks_per_step, 3),
                  cut_by_stop=cut)
    return result


def _public(note):
    return {'note': note['note'], 'name': note_name(note['note']),
            'velocity': note['velocity'], 'gate_ticks': note['gate_ticks'],
            'gate_steps': note['gate_steps'], **({'cut_by_stop': True} if note['cut_by_stop'] else {}),
            **({'channel': note['channel']} if note['channel'] != 1 else {})}


def build_steps(events, clocks_per_step, steps_per_loop, loops):
    """Return one row per played step with its notes, held notes and CCs.

    `events` are dicts with `host_clocks` (clocks sent when the message
    arrived) and `data` (the raw MIDI message), in arrival order. Rows are in play order;
    `step` counts from 1 within the pattern and `loop` from 1.
    """
    if clocks_per_step < 1 or steps_per_loop < 1 or loops < 1:
        raise ValueError('clocks per step, steps and loops must be positive')
    notes, ccs, reference = collect_notes(events, clocks_per_step)
    total = steps_per_loop * loops
    rows = []
    for index in range(total):
        start_tick = index * clocks_per_step
        played = [n for n in notes if n['step_index'] == index]
        held = [n for n in notes if n['step_index'] < index and n['off_tick'] > start_tick]
        step_ccs = {}
        for cc in ccs:
            if cc['step_index'] == index:
                step_ccs[str(cc['control'])] = cc['value']
        rows.append({'step': index % steps_per_loop + 1, 'loop': index // steps_per_loop + 1,
                     'midi': {'notes': [_public(n) for n in played],
                              'held': [{'note': n['note'], 'name': note_name(n['note']),
                                        'from_step': n['step_index'] % steps_per_loop + 1}
                                       for n in held],
                              'ccs': step_ccs}})
    extra = [n for n in notes if n['step_index'] >= total]
    off_grid = [n for n in notes if abs(n['on_tick'] - n['step_index'] * clocks_per_step) > 1]
    cc_numbers = sorted({cc['control'] for cc in ccs})
    return {'clock_reference': reference, 'rows': rows, 'note_count': len(notes),
            'notes_after_last_step': len(extra), 'off_grid_notes': len(off_grid),
            'cc_numbers': cc_numbers}


def loop_differences(rows):
    """Steps whose notes or velocities differ between loops (first loop as reference)."""
    by_step = {}
    for row in rows:
        signature = sorted((n['note'], n['velocity']) for n in row['midi']['notes'])
        by_step.setdefault(row['step'], []).append(signature)
    return sorted(step for step, sigs in by_step.items() if any(s != sigs[0] for s in sigs[1:]))


def classify(midi, audio):
    """Compare one step's MIDI-out notes with what the audio analysis heard."""
    expected = [n['note'] for n in midi['notes']]
    if audio is None:
        return None
    if not expected:
        if midi['held']:
            return 'held'
        return 'unexpected_onset' if audio.get('onset') else 'rest'
    if not audio.get('sounding'):
        return 'silent'
    heard = audio.get('midi')
    chord = [c['midi'] for c in audio.get('chord') or []]
    if len(expected) == 1:
        target = expected[0]
        if heard == target:
            return 'match'
        if heard is not None and (heard - target) % 12 == 0:
            return 'octave'
        if target in chord:
            return 'match_in_chord'
        return 'mismatch'
    found = set(expected) & set(chord)
    if found == set(expected):
        return 'match'
    if found or {n % 12 for n in expected} & {c % 12 for c in chord}:
        return 'partial'
    return 'mismatch'


def chord_recall(midi, audio):
    """Share of expected notes and pitch classes found in the audio chord."""
    expected = [n['note'] for n in midi['notes']]
    if not expected or audio is None:
        return None
    chord = {c['midi'] for c in audio.get('chord') or []}
    return {'notes': round(len(set(expected) & chord) / len(set(expected)), 3),
            'pitch_classes': round(len({n % 12 for n in expected} & {c % 12 for c in chord})
                                   / len({n % 12 for n in expected}), 3)}


def summarize(rows):
    counts = {}
    for row in rows:
        label = row.get('agreement')
        if label is not None:
            counts[label] = counts.get(label, 0) + 1
    note_steps = sum(1 for r in rows if r['midi']['notes'])
    agreeing = sum(counts.get(k, 0) for k in ('match', 'match_in_chord'))
    rests = sum(1 for r in rows if not r['midi']['notes'] and not r['midi']['held'])
    return {'steps': len(rows), 'note_steps': note_steps, 'rest_steps': rests,
            'agreement_counts': counts,
            'note_steps_matching': agreeing,
            'note_match_ratio': round(agreeing / note_steps, 3) if note_steps and counts else None}
