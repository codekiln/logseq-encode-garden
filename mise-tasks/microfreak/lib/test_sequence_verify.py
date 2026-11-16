"""Synthetic descriptions and audition rows only: no instrument needed."""
import contextlib
import io
import unittest

import sequence as Q
import sequence_verify as V


def pattern(steps, tracks=None):
    result = Q.canonical_pattern({'steps': steps, 'mod_tracks': tracks}, len(steps))
    result['in_use'] = any(s.get('notes') or s.get('mod') for s in result['steps'])
    return result


def audition_row(loop, step, notes=(), held=(), ccs=None, audio=None):
    row = {'loop': loop, 'step': step,
           'midi': {'notes': [{'note': n, 'velocity': v} for n, v in notes],
                    'held': [{'note': n} for n in held], 'ccs': ccs or {}}}
    if audio is not None:
        row['audio'] = audio
    return row


class ExpectedRowsTests(unittest.TestCase):
    def test_ties_hold_the_same_note_and_restart_a_different_one(self):
        rows = V.expected_rows(pattern([
            {'notes': ['G4'], 'tie': True}, {'notes': ['G4']},
            {'notes': ['C5'], 'tie': True}, {'notes': ['D5'], 'velocity': 90},
            {'notes': ['E4'], 'tie': True}, {}]), loops=1)
        self.assertEqual([(r['notes'], r['held']) for r in rows], [
            ([(67, 100)], []), ([], [67]), ([(72, 100)], []), ([(74, 90)], []),
            ([(64, 100)], []), ([], [])])

    def test_a_tie_on_the_last_step_holds_into_the_next_loop_only(self):
        rows = V.expected_rows(pattern([{'notes': ['D4']}, {'notes': ['D4'], 'tie': True}]), loops=2)
        self.assertEqual([(r['loop'], r['step'], r['notes'], r['held']) for r in rows], [
            (1, 1, [(62, 100)], []), (1, 2, [(62, 100)], []),
            (2, 1, [], [62]), (2, 2, [(62, 100)], [])])

    def test_chords_list_every_note_with_its_velocity(self):
        rows = V.expected_rows(pattern([
            {'notes': ['C4', 'E4', 'G4'], 'velocity': [30, 60, 90], 'tie': True},
            {'notes': ['C4', 'E4', 'G4']}]), loops=1)
        self.assertEqual(rows[0]['notes'], [(60, 30), (64, 60), (67, 90)])
        self.assertEqual(rows[1]['held'], [60, 64, 67])

    def test_mod_values_send_half_on_known_ccs_unless_smoothed(self):
        steps = [{'notes': ['C4'], 'mod': [128, 255, 7, None]}, {'mod': [10, None, None, None]}]
        tracks = ['0x0101', '0x0602', '0x0102', None]
        rows = V.expected_rows(pattern(steps, tracks), loops=1)
        self.assertEqual([r['ccs'] for r in rows], [{'23': 64, '106': 127}, {'23': 5}])
        smoothed = V.expected_rows(pattern(steps, tracks), 1, (True, False, False, False))
        self.assertEqual(smoothed[0]['ccs'], {'106': 127})

    def test_an_erased_pattern_plays_nothing(self):
        erased = pattern([{'notes': ['C4']}])
        erased['in_use'] = False
        self.assertEqual(V.expected_rows(erased, 1)[0]['notes'], [])


class CompareTests(unittest.TestCase):
    def test_matching_step_with_audio(self):
        expected = {'loop': 1, 'step': 1, 'notes': [(60, 100)], 'held': [], 'ccs': {'23': 64}}
        audio = {'midi': 60, 'chord': [{'midi': 60}], 'sounding': True, 'onset': True}
        row = V.compare_row(expected, audition_row(1, 1, [(60, 100)], ccs={'23': 64}, audio=audio))
        self.assertTrue(row['midi_out_matches'])
        self.assertEqual(row['audio'], {'pitch': 'C4', 'chord': ['C4'], 'sounding': True, 'onset': True})
        self.assertEqual(row['audio_check'], 'match')

    def test_each_kind_of_difference_is_named(self):
        expected = {'loop': 1, 'step': 2, 'notes': [(60, 100)], 'held': [55], 'ccs': {'23': 64}}
        row = V.compare_row(expected, audition_row(1, 2, [(60, 90)], ccs={'23': 63}))
        self.assertFalse(row['midi_out_matches'])
        self.assertEqual(row['midi_out_differs_in'], ['notes', 'held', 'ccs'])
        self.assertNotIn('audio_check', row)
        summary = V.summarize([row], ['A step 2: described …'], True)
        self.assertEqual(summary['midi_out_matching_steps'], 0)
        self.assertIn("expected ['C4'] [100], MIDI out ['C4'] [90]", summary['midi_out_mismatches'][0])
        self.assertFalse(summary['download_matches_description'])

    def test_audio_of_a_held_step_is_reported_as_held(self):
        expected = {'loop': 1, 'step': 2, 'notes': [], 'held': [67], 'ccs': {}}
        audio = {'midi': 67, 'chord': [{'midi': 67}], 'sounding': True, 'onset': False}
        row = V.compare_row(expected, audition_row(1, 2, held=[67], audio=audio))
        self.assertEqual((row['midi_out_matches'], row['audio_check']), (True, 'held'))
        self.assertIn('held G4', V.compact(row))


class PlayingPatternTests(unittest.TestCase):
    def decoded(self, a_steps, b_steps, length=4):
        description = {'length': length, 'patterns': {'A': {'steps': a_steps}, 'B': {'steps': b_steps}}}
        stored = {'length': length, 'gate_percent': 50, 'smoothing': [False] * 4, 'patterns': {}}
        for name, steps in (('A', a_steps), ('B', b_steps)):
            canonical = Q.canonical_pattern({'steps': steps}, length)['steps']
            stored['patterns'][name] = {
                'in_use': any(s.get('notes') for s in canonical), 'mod_tracks': [None] * 4,
                'steps': [{'step': i + 1, 'status': 'tie' if s.get('tie') else 'note',
                           'notes': s['notes'], 'note_names': [Q.note_name(n) for n in s['notes']],
                           'velocities': s['velocities']} if s.get('notes')
                          else {'step': i + 1, 'status': 'rest'} for i, s in enumerate(canonical)]}
        return description, stored

    def test_described_pattern_is_expected(self):
        description, decoded = self.decoded([{'notes': ['C4']}], [{'notes': ['A3']}])
        a, source = V.playing_pattern(description, decoded)
        b, _ = V.playing_pattern(description, decoded, 'B')
        self.assertEqual((a['steps'][0]['notes'], b['steps'][0]['notes'], source),
                         ([60], [57], 'description'))

    def test_pattern_left_out_comes_from_the_slot(self):
        description, decoded = self.decoded([{'notes': ['C4']}], [])
        del description['patterns']['A']
        a, source = V.playing_pattern(description, decoded)
        self.assertEqual((a['steps'][0]['notes'], a['in_use']), ([60], True))
        self.assertTrue(source.startswith('slot'))

    def test_short_description_is_expected_in_stored_form(self):
        description, decoded = self.decoded([{'notes': ['E4']}] * 4, [])
        description = {'length': 1, 'patterns': {'A': {'steps': [{'notes': ['E4']}]}}}
        a, _ = V.playing_pattern(description, decoded)
        self.assertEqual([s['notes'] for s in a['steps']], [[64]] * 4)


class ParserTests(unittest.TestCase):
    def test_pattern_b_needs_the_panel_selection(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            V.main(['seq.json', '--slot', '445', '--pattern', 'B', '--out-dir', '/tmp/x'])


if __name__ == '__main__':
    unittest.main()
