"""Synthetic presets only: no user or factory patch data."""
import contextlib
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

import parameters
import sequence as Q
from test_parameters import pack

TASK = Path(__file__).resolve().parents[1] / 'inspect'
WRITE_TASK = Path(__file__).resolve().parents[1] / 'write-sequence'


def field(name, descriptor, value):
    return bytes([0x40 | len(name)]) + name.encode() + b'c' + bytes([descriptor]) + value.to_bytes(2, 'little')


def synthetic(length_raw=6553, gate_raw=16384, smooth=(0, 0, 0, 0)):
    """A preset with a Seq section, pattern A holding three steps and B erased."""
    block = (b'#VCF' + field('Cutoff', 238, 16384) + b'@'
             + b'#Seq' + field('Length', 60, length_raw) + field('GateLen', 80, gate_raw)
             + b''.join(field(f'Smooth{n}', 1, v) for n, v in enumerate(smooth, start=1))
             + b'@ ')
    data = bytearray(block.ljust(4088, b'\xff'))
    for name, offset in Q.PATTERN_OFFSETS.items():
        for step in range(Q.STEPS):
            data[offset + step * 16:offset + step * 16 + 16] = Q.blank_step()
        trailer = offset + 1024
        data[trailer:trailer + 18] = bytes([0xFF] * 8 + [50, 16, 0 if name == 'A' else 1,
                                            1 if name == 'A' else 0, 0, 0, 0, 0, 0xFF, 0])
    a = Q.PATTERN_OFFSETS['A']
    data[a:a + 16] = bytes([48, 0xFF, 0xFF, 0xFF, 67, 0, 0, 0, 0x80, 0, 0, 0, 2, 1, 0, 0])
    data[a + 16:a + 32] = bytes([48, 0xFF, 0xFF, 0xFF, 67, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0])
    data[a + 32:a + 48] = bytes([0xFF] * 4 + [0] * 12)
    data[a + 48:a + 64] = bytes([60, 64, 67, 0xFF, 30, 60, 90, 0, 0, 0, 0, 0, 1, 0, 0, 0])
    data[a + 1024:a + 1026] = (0x0101).to_bytes(2, 'little')
    data[a + 1040] = Q.PATTERN_IN_USE
    return pack(bytes(data))


class ConversionTests(unittest.TestCase):
    def test_length_and_gate_match_values_the_instrument_stores(self):
        for raw, steps in ((0, 4), (4369, 12), (6553, 16), (10922, 24), (15291, 32),
                           (20752, 42), (32767, 64)):
            self.assertEqual(Q.length_from_raw(raw), steps)
            self.assertEqual(Q.length_to_raw(steps), raw)
        for raw, percent in ((16384, 50), (12697, 41), (0, 10), (32767, 90)):
            self.assertEqual(Q.gate_from_raw(raw), percent)
            self.assertEqual(Q.gate_to_raw(percent), raw)

    def test_note_names_put_middle_c_at_c4(self):
        self.assertEqual(Q.note_number('C4'), 60)
        self.assertEqual(Q.note_number('f#3'), 54)
        self.assertEqual(Q.note_number('Eb2'), 39)
        self.assertEqual(Q.note_number(127), 127)
        self.assertEqual(Q.note_name(61), 'C#4')
        for bad in ('H2', 'C', 'G#9', -1):
            with self.assertRaises(ValueError):
                Q.note_number(bad)

    def test_pack_reverses_unpack(self):
        payload = synthetic()
        self.assertEqual(Q.pack_payload(parameters.unpack_payload(payload)), payload)


class DecodeTests(unittest.TestCase):
    def test_reads_shared_settings_and_pattern_a(self):
        result = Q.decode_sequence(synthetic(smooth=(32767, 0, 0, 0)))
        self.assertEqual(result['length'], 16)
        self.assertEqual(result['gate_percent'], 50)
        self.assertEqual(result['smoothing'], [True, False, False, False])
        a = result['patterns']['A']
        self.assertTrue(a['in_use'])
        self.assertEqual(len(a['steps']), 16)
        self.assertEqual(a['mod_tracks'][0], {'track': 1, 'destination_id': '0x0101',
                                              'destination': 'VCF.Cutoff'})
        self.assertEqual(a['mod_tracks'][1:], [None] * 3)
        self.assertEqual(a['steps'][0], {'step': 1, 'status': 'tie', 'notes': [48],
                                         'note_names': ['C3'], 'velocities': [67],
                                         'mod': [128, None, None, None]})
        self.assertEqual(a['steps'][1]['status'], 'note')
        self.assertEqual(a['steps'][2], {'step': 3, 'status': 'rest'})
        self.assertEqual(a['steps'][3]['notes'], [60, 64, 67])
        self.assertEqual(a['steps'][3]['velocities'], [30, 60, 90])
        self.assertFalse(result['patterns']['B']['in_use'])

    def test_notes_after_an_empty_voice_are_not_played(self):
        data = bytearray(parameters.unpack_payload(synthetic()))
        a = Q.PATTERN_OFFSETS['A']
        data[a + 1] = 0xFF
        data[a + 2] = 72
        step = Q.decode_sequence(Q.pack_payload(bytes(data)))['patterns']['A']['steps'][0]
        self.assertEqual(step['notes'], [48])
        self.assertIn('raw_hex', step)

    def test_steps_past_the_length_are_counted_not_listed(self):
        result = Q.decode_sequence(synthetic(length_raw=0))
        a = result['patterns']['A']
        self.assertEqual(result['length'], 4)
        self.assertEqual(len(a['steps']), 4)
        self.assertEqual(a['unplayed_steps_with_notes'], 0)


class EncodeTests(unittest.TestCase):
    def changed(self, before, after):
        x, y = parameters.unpack_payload(before), parameters.unpack_payload(after)
        return [i for i in range(len(x)) if x[i] != y[i]]

    def test_description_round_trips(self):
        steps = [{'notes': ['C4'], 'velocity': 100},
                 {},
                 {'notes': ['G4'], 'velocity': 90, 'tie': True},
                 {'notes': ['G4'], 'velocity': 90},
                 {'notes': ['C4', 'E4', 'G4', 'B4'], 'velocity': [30, 60, 90, 120]},
                 {'notes': [72], 'mod': [None, 255, None, None]}]
        payload = Q.encode_sequence(synthetic(), {
            'length': 8, 'gate_percent': 41, 'smoothing': [False, True, None, None],
            'patterns': {'B': {'steps': steps, 'mod_tracks': [None, 0x0602, None, None]}}})
        result = Q.decode_sequence(payload)
        self.assertEqual((result['length'], result['gate_percent']), (8, 41))
        self.assertEqual(result['smoothing'], [False, True, False, False])
        b = result['patterns']['B']
        self.assertTrue(b['in_use'])
        self.assertEqual((b['length_copy'], b['gate_percent']), (8, 41))
        self.assertEqual(b['mod_tracks'][1]['destination'], 'EG2.DecRel')
        self.assertEqual([s['status'] for s in b['steps']],
                         ['note', 'rest', 'tie', 'note', 'note', 'note', 'rest', 'rest'])
        self.assertEqual(b['steps'][4]['notes'], [60, 64, 67, 71])
        self.assertEqual(b['steps'][4]['velocities'], [30, 60, 90, 120])
        self.assertEqual(b['steps'][5]['mod'], [None, 255, None, None])
        self.assertEqual(result['patterns']['A']['steps'][0]['notes'], [48])

    def test_only_sequence_values_change(self):
        base = synthetic()
        after = Q.encode_sequence(base, {'length': 32, 'patterns': {'A': {'steps': [{'notes': [50]}]}}})
        changed = self.changed(base, after)
        report = parameters.parse_parameters(base)
        length_at = next(f['unpacked_value_offset'] for f in report['fields'] if f['name'] == 'Seq.Length')
        self.assertTrue(all(i in (length_at + 1, length_at + 2) or i >= Q.PATTERN_OFFSETS['A']
                            for i in changed))
        self.assertEqual(parameters.parse_parameters(after)['parameter_end_offset'],
                         report['parameter_end_offset'])

    def test_rest_and_blank_records_match_the_instrument(self):
        self.assertEqual(Q.encode_step({}), bytes([0xFF] * 4 + [0] * 12))
        self.assertEqual(Q.blank_step(), bytes([0xFF] * 4 + [100] * 4 + [0] * 8))
        self.assertEqual(Q.encode_step({'notes': [60, 64], 'velocity': 80, 'tie': True}),
                         bytes([60, 64, 0xFF, 0xFF, 80, 80, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0]))

    def test_pattern_without_steps_is_marked_erased(self):
        payload = Q.encode_sequence(synthetic(), {'patterns': {'A': {'steps': []}}})
        a = Q.decode_sequence(payload)['patterns']['A']
        self.assertFalse(a['in_use'])
        self.assertEqual({s['status'] for s in a['steps']}, {'rest'})

    def test_rejects_values_the_instrument_cannot_play(self):
        base = synthetic()
        bad = [{'length': 3}, {'length': 65}, {'gate_percent': 95},
               {'patterns': {'A': {'steps': [{}] * 65}}},
               {'patterns': {'A': {'steps': [{'notes': [1, 2, 3, 4, 5]}]}}},
               {'patterns': {'A': {'steps': [{'notes': [60], 'velocity': 0}]}}},
               {'patterns': {'A': {'steps': [{'notes': [60], 'velocity': 128}]}}},
               {'patterns': {'A': {'steps': [{'notes': [60, 62], 'velocity': [90]}]}}},
               {'patterns': {'A': {'steps': [{'tie': True}]}}},
               {'patterns': {'A': {'steps': [{'notes': [60], 'mod': [256, None, None, None]}]}}},
               {'patterns': {'A': {'steps': [], 'mod_tracks': [None]}}}]
        for description in bad:
            with self.subTest(description=description), self.assertRaises(ValueError):
                Q.encode_sequence(base, description)


class CommandTests(unittest.TestCase):
    def test_encoder_command_keeps_header_and_refuses_to_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            base, spec, out = (Path(directory) / n for n in ('base.bin', 'seq.json', 'out.bin'))
            header = bytes(range(35))
            base.write_bytes(header + synthetic())
            spec.write_text(json.dumps({'length': 4, 'patterns': {'A': {'steps': [{'notes': ['D4']}]}}}))
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(Q.main([str(base), str(spec), str(out)]), 0)
            raw = out.read_bytes()
            self.assertEqual(raw[:35], header)
            decoded = Q.decode_sequence(raw[35:])
            self.assertEqual(decoded['patterns']['A']['steps'][0]['notes'], [62])
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(Q.main([str(base), str(spec), str(out)]), 2)
            self.assertEqual(out.read_bytes(), raw)

    def test_write_task_accepts_usage_arguments(self):
        with tempfile.TemporaryDirectory() as directory:
            base, spec, out = (Path(directory) / n for n in ('base.bin', 'seq.json', 'out.bin'))
            base.write_bytes(bytes(35) + synthetic())
            spec.write_text(json.dumps({'length': 12}))
            env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', usage_base=str(base),
                       usage_sequence=str(spec), usage_output=str(out))
            result = subprocess.run(['bash', str(WRITE_TASK)], env=env, text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(Q.decode_sequence(out.read_bytes()[35:])['length'], 12)

    def test_inspect_flag_adds_the_sequence(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / 'synthetic.bin'
            file.write_bytes(bytes(35) + synthetic())
            env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
            for key in ('usage_file', 'usage_slot', 'usage_interpret_fw5', 'usage_sequence'):
                env.pop(key, None)
            plain = subprocess.run(['bash', str(TASK), str(file)], env=env, text=True,
                                   capture_output=True)
            flagged = subprocess.run(['bash', str(TASK), str(file), '--sequence'], env=env,
                                     text=True, capture_output=True)
            usage = subprocess.run(['bash', str(TASK)], env=dict(env, usage_file=str(file),
                                   usage_sequence='true'), text=True, capture_output=True)
            self.assertEqual((plain.returncode, flagged.returncode, usage.returncode), (0, 0, 0))
            plain, flagged, usage = (json.loads(r.stdout) for r in (plain, flagged, usage))
            self.assertNotIn('sequence', plain)
            sequence = flagged.pop('sequence')
            self.assertEqual(flagged, plain)
            self.assertEqual(sequence['patterns']['A']['steps'][0]['notes'], [48])
            self.assertEqual(usage['sequence'], sequence)


if __name__ == '__main__':
    unittest.main()
