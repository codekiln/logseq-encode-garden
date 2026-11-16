import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('sequence_midi', Path(__file__).with_name('sequence_midi.py'))
sm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sm)


def device_stream(pattern, clocks_per_step, loops, echo=True, ccs=None, stop=True):
    """Imitate the MicroFreak's USB MIDI output while it follows host clock.

    `pattern` holds one entry per step: a list of (note, velocity, gate_ticks),
    or [] for a rest. Start plays the first step at once; every later step
    plays right after the instrument echoes the clock that begins it.
    """
    ccs = ccs or {}
    total = len(pattern) * clocks_per_step * loops
    events, pending, sent = [], [], 0

    def emit(data):
        events.append({'t': sent * 0.02, 'host_clocks': sent, 'data': data})

    def play_step(tick):
        index = tick // clocks_per_step
        for control, value in ccs.get(index % len(pattern), []):
            emit([0xB0, control, value])
        for note, velocity, gate in pattern[index % len(pattern)]:
            emit([0x90, note, velocity])
            pending.append((tick + gate, note))

    def release(tick):
        for item in sorted(p for p in pending if p[0] == tick):
            emit([0x80, item[1], 64])
            pending.remove(item)

    emit([sm.START])
    play_step(0)
    for tick in range(total):
        sent += 1
        if echo:
            emit([sm.CLOCK])
        release(tick)
        if tick and tick % clocks_per_step == 0:
            play_step(tick)
    if stop:
        emit([sm.STOP])
    return events


SIMPLE = [[(36, 9, 2)], [(24, 24, 2)], [], [(37, 100, 3)]]


class StepTests(unittest.TestCase):
    def test_notes_rests_and_gates_land_on_their_steps(self):
        built = sm.build_steps(device_stream(SIMPLE, 6, 2), 6, 4, 2)
        rows = built['rows']
        self.assertEqual(built['clock_reference'], 'device_clock_echo')
        self.assertEqual([(r['loop'], r['step']) for r in rows][:5], [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1)])
        self.assertEqual(rows[0]['midi']['notes'],
                         [{'note': 36, 'name': 'C2', 'velocity': 9, 'gate_ticks': 2, 'gate_steps': 0.333}])
        self.assertEqual(rows[1]['midi']['notes'][0]['note'], 24)
        self.assertEqual(rows[2]['midi'], {'notes': [], 'held': [], 'ccs': {}})
        self.assertEqual(rows[3]['midi']['notes'][0]['gate_ticks'], 3)
        self.assertEqual(built['note_count'], 6)
        self.assertEqual(built['off_grid_notes'], 0)
        self.assertEqual(sm.loop_differences(rows), [])

    def test_host_clock_count_replaces_missing_echoes(self):
        echoed = sm.build_steps(device_stream(SIMPLE, 6, 1), 6, 4, 1)
        plain = sm.build_steps(device_stream(SIMPLE, 6, 1, echo=False), 6, 4, 1)
        self.assertEqual(plain['clock_reference'], 'host_clocks_sent')
        self.assertEqual(plain['rows'], echoed['rows'])

    def test_chord_tied_across_steps_is_held_on_the_next_step(self):
        chord = [(39, 70, 9), (51, 34, 9), (58, 126, 9)]
        pattern = [chord, [], [(63, 116, 3)], []]
        rows = sm.build_steps(device_stream(pattern, 6, 1), 6, 4, 1)['rows']
        self.assertEqual([n['note'] for n in rows[0]['midi']['notes']], [39, 51, 58])
        self.assertEqual(rows[0]['midi']['notes'][0]['gate_steps'], 1.5)
        self.assertEqual([h['note'] for h in rows[1]['midi']['held']], [39, 51, 58])
        self.assertEqual(rows[1]['midi']['held'][0]['from_step'], 1)
        self.assertEqual(rows[3]['midi']['held'], [])

    def test_modulation_track_ccs_are_kept_per_step(self):
        events = device_stream(SIMPLE, 6, 1, ccs={0: [(23, 76)], 2: [(12, 73), (13, 102)]})
        built = sm.build_steps(events, 6, 4, 1)
        self.assertEqual(built['rows'][0]['midi']['ccs'], {'23': 76})
        self.assertEqual(built['rows'][2]['midi']['ccs'], {'12': 73, '13': 102})
        self.assertEqual(built['cc_numbers'], [12, 13, 23])

    def test_note_still_open_at_stop_is_marked_cut(self):
        pattern = [[(60, 90, 2)], [(62, 90, 40)]]
        rows = sm.build_steps(device_stream(pattern, 6, 1), 6, 2, 1)['rows']
        note = rows[1]['midi']['notes'][0]
        self.assertTrue(note['cut_by_stop'])
        self.assertEqual(note['gate_ticks'], 5)

    def test_loop_difference_and_off_grid_note_are_reported(self):
        events = device_stream(SIMPLE, 6, 2)
        second_loop_first_note = [e for e in events if e['data'][:2] == [0x90, 36]][1]
        second_loop_first_note['data'] = [0x90, 36, 100]
        built = sm.build_steps(events, 6, 4, 2)
        self.assertEqual(sm.loop_differences(built['rows']), [1])
        # The same stream read as 1/8 steps puts odd 1/16 steps between steps.
        self.assertGreater(sm.build_steps(events, 12, 2, 2)['off_grid_notes'], 0)

    def test_note_on_with_zero_velocity_ends_a_note(self):
        events = [{'host_clocks': 0, 'data': [0xFA]}, {'host_clocks': 0, 'data': [0x90, 48, 80]}]
        events += [{'host_clocks': i, 'data': [0xF8]} for i in range(1, 4)]
        events += [{'host_clocks': 3, 'data': [0x90, 48, 0]}]
        rows = sm.build_steps(events, 6, 1, 1)['rows']
        self.assertEqual(rows[0]['midi']['notes'][0]['gate_ticks'], 2)


class CompareTests(unittest.TestCase):
    def midi(self, *notes, held=()):
        return {'notes': [{'note': n} for n in notes], 'held': [{'note': n} for n in held], 'ccs': {}}

    def audio(self, midi=None, onset=True, sounding=True, chord=()):
        return {'onset': onset, 'sounding': sounding, 'midi': midi,
                'chord': [{'midi': c} for c in chord]}

    def test_single_note_labels(self):
        self.assertEqual(sm.classify(self.midi(48), self.audio(48)), 'match')
        self.assertEqual(sm.classify(self.midi(48), self.audio(60)), 'octave')
        self.assertEqual(sm.classify(self.midi(48), self.audio(51, chord=[48, 55])), 'match_in_chord')
        self.assertEqual(sm.classify(self.midi(48), self.audio(51)), 'mismatch')
        self.assertEqual(sm.classify(self.midi(48), self.audio(None, sounding=False)), 'silent')

    def test_rest_held_and_chord_labels(self):
        self.assertEqual(sm.classify(self.midi(), self.audio(onset=False)), 'rest')
        self.assertEqual(sm.classify(self.midi(), self.audio(onset=True)), 'unexpected_onset')
        self.assertEqual(sm.classify(self.midi(held=[48]), self.audio(48, onset=False)), 'held')
        self.assertEqual(sm.classify(self.midi(60, 64, 67), self.audio(60, chord=[60, 64, 67, 72])), 'match')
        self.assertEqual(sm.classify(self.midi(60, 64, 67), self.audio(60, chord=[60, 76])), 'partial')
        self.assertEqual(sm.classify(self.midi(60, 64), self.audio(61, chord=[61, 66])), 'mismatch')
        self.assertIsNone(sm.classify(self.midi(60), None))
        self.assertEqual(sm.chord_recall(self.midi(60, 64, 67), self.audio(chord=[60, 76])),
                         {'notes': 0.333, 'pitch_classes': 0.667})

    def test_summary_counts_agreement(self):
        rows = [{'midi': self.midi(48), 'agreement': 'match'},
                {'midi': self.midi(50), 'agreement': 'octave'},
                {'midi': self.midi(), 'agreement': 'rest'}]
        summary = sm.summarize(rows)
        self.assertEqual(summary['note_steps'], 2)
        self.assertEqual(summary['rest_steps'], 1)
        self.assertEqual(summary['note_match_ratio'], 0.5)

    def test_note_names_use_scientific_pitch(self):
        self.assertEqual(sm.note_name(60), 'C4')
        self.assertEqual(sm.note_name(24), 'C1')
        self.assertEqual(sm.note_name(61), 'C#4')


if __name__ == '__main__':
    unittest.main()
