"""Synthetic presets and synthetic audio only: no user or factory patch data."""
import unittest

import parameters
import probe
from test_sequence import field, synthetic

try:
    import numpy as np
except ImportError:  # `mise run microfreak:test` provides numpy
    np = None


def with_section(name, *fields):
    """A synthetic payload whose parameter block also holds one more section."""
    import sequence as Q
    data = bytearray(parameters.unpack_payload(synthetic()))
    end = parameters.parse_parameters(synthetic())['parameter_end_offset'] - 1
    block = b'#' + name.encode() + b''.join(fields) + b'@'
    data[end:end] = block
    del data[-len(block):]
    return Q.pack_payload(bytes(data))


class SetTests(unittest.TestCase):
    def test_parse_set_reads_choices_decimals_and_raw_values(self):
        self.assertEqual(probe.parse_set('VCO.BendRng=2'), ('VCO.BendRng', ('choice', 2)))
        self.assertEqual(probe.parse_set('VCF.Cutoff=0.5'), ('VCF.Cutoff', ('decimal', 0.5)))
        self.assertEqual(probe.parse_set('Co1.LFO=-0.25'), ('Co1.LFO', ('decimal', -0.25)))
        self.assertEqual(probe.parse_set('Mat.Assign1=raw:0x0d01'), ('Mat.Assign1', ('raw', 0x0D01)))
        with self.assertRaises(ValueError):
            probe.parse_set('VCO.BendRng')

    def test_raw_for_scales_choices_by_the_descriptor(self):
        bend = {'name': 'VCO.BendRng', 'descriptor': 24}
        self.assertEqual(probe.raw_for(bend, ('choice', 0)), 0)
        self.assertEqual(probe.raw_for(bend, ('choice', 12)), 16384)
        self.assertEqual(probe.raw_for(bend, ('choice', 24)), 32767)
        with self.assertRaises(ValueError):
            probe.raw_for(bend, ('choice', 25))

    def test_raw_for_reads_decimals_as_normalized_values(self):
        cutoff = {'name': 'VCF.Cutoff', 'descriptor': 0}
        self.assertEqual(probe.raw_for(cutoff, ('decimal', 1.0)), 32767)
        with self.assertRaises(ValueError):
            probe.raw_for(cutoff, ('choice', 1))
        amount = {'name': 'Co1.LFO', 'descriptor': 0}
        self.assertEqual(probe.raw_for(amount, ('decimal', -1.0)), (-32767) & 0xFFFF)

    def test_apply_settings_changes_only_the_named_field(self):
        base = with_section('VCO', field('BendRng', 24, 16384))
        before = {f['name']: f for f in parameters.parse_parameters(base)['fields']}
        new, changed = probe.apply_settings(base, [('VCO.BendRng', ('choice', 2))])
        after = {f['name']: f for f in parameters.parse_parameters(new)['fields']}
        self.assertEqual(changed, {'VCO.BendRng': [16384, 2731]})
        self.assertEqual(after['VCO.BendRng']['descriptor'], 24)
        for name in before:
            if name != 'VCO.BendRng':
                self.assertEqual(after[name]['raw_hex'], before[name]['raw_hex'])
        self.assertEqual(parameters.unpack_payload(new)[1980:], parameters.unpack_payload(base)[1980:])

    def test_apply_settings_refuses_a_field_the_base_lacks(self):
        with self.assertRaises(ValueError):
            probe.apply_settings(synthetic(), [('Kbd.Scale', ('choice', 1))])


class ScriptTests(unittest.TestCase):
    def test_compile_script_orders_notes_bends_ccs_and_pressure(self):
        script = {'events': [{'t': 0.5, 'off': 'C4'}, {'t': 0.0, 'on': 'C4', 'velocity': 90},
                             {'t': 0.1, 'bend': 1.0}, {'t': 0.2, 'bend': -1.0},
                             {'t': 0.3, 'cc': [1, 64]}, {'t': 0.4, 'pressure': 100}]}
        compiled = probe.compile_script(script, channel=2)
        self.assertEqual([m for _, m, _ in compiled],
                         [[0x92, 60, 90], [0xE2, 0x7F, 0x7F], [0xE2, 0, 0],
                          [0xB2, 1, 64], [0xD2, 100], [0x82, 60, 0]])

    def test_yaml_on_and_off_keys_read_as_notes(self):
        import yaml
        script = yaml.safe_load('events:\n  - {t: 0, on: C4}\n  - {t: 1, off: C4}\n')
        compiled = probe.compile_script(script, channel=0)
        self.assertEqual([m for _, m, _ in compiled], [[0x90, 60, 100], [0x80, 60, 0]])

    def test_a_ramp_sends_evenly_spaced_values(self):
        compiled = probe.compile_script({'events': [{'t': 1.0, 'cc': [1, 0], 'to': 127,
                                                     'over': 1.0, 'steps': 4}]}, channel=0)
        self.assertEqual([round(t, 2) for t, _, _ in compiled], [1.0, 1.25, 1.5, 1.75, 2.0])
        self.assertEqual([m[2] for _, m, _ in compiled], [0, 32, 64, 95, 127])
        pressure = probe.compile_script({'events': [{'t': 0, 'pressure': 0, 'to': 127, 'over': 1.0,
                                                     'steps': 3}]}, channel=0)
        self.assertEqual([label for _, _, label in pressure], ['pressure 0', 'pressure 42', 'pressure 85', 'pressure 127'])


@unittest.skipIf(np is None, 'numpy is not installed; run mise run microfreak:test')
class AnalysisTests(unittest.TestCase):
    SR = 48000

    def tone(self, hz, seconds, level):
        t = np.arange(int(seconds * self.SR)) / self.SR
        return level * sum(np.sin(2 * np.pi * hz * h * t) / h for h in range(1, 6))

    def test_frames_and_notes_report_level_and_pitch(self):
        silence = np.zeros(int(0.2 * self.SR))
        audio = np.concatenate([silence, self.tone(261.63, 0.8, 0.1), silence])
        rows = probe.frames(audio, self.SR)
        compiled = probe.compile_script({'events': [{'t': 0.2, 'on': 'C4'}, {'t': 1.0, 'off': 'C4'}]}, 0)
        notes = probe.summarize_notes(rows, [0.2, 1.0], compiled)
        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0]['pitch'], 'C4')
        self.assertLess(abs(notes[0]['cents_from_note']), 5)
        self.assertLess(notes[0]['onset_latency_ms'], 40)
        self.assertAlmostEqual(notes[0]['peak_db'], -20.5, delta=2)

    def test_a_quiet_tail_stays_out_of_the_note_summary(self):
        t = np.arange(int(1.0 * self.SR)) / self.SR
        decaying = self.tone(261.63, 1.0, 0.1) * np.exp(-t / 0.08)
        noise = np.random.default_rng(3).normal(0, 1e-4, len(decaying))
        audio = np.concatenate([np.zeros(int(0.2 * self.SR)), decaying + noise])
        rows = probe.frames(audio, self.SR)
        compiled = probe.compile_script({'events': [{'t': 0.2, 'on': 'C4'}, {'t': 1.2, 'off': 'C4'}]}, 0)
        note = probe.summarize_notes(rows, [0.2, 1.2], compiled)[0]
        # Five harmonics at 1/h around C4 put the centroid near 570 Hz.
        self.assertAlmostEqual(note['centroid_hz_median'], 570, delta=40)
        self.assertLess(note['midi_max'] - note['midi_min'], 0.2)


if __name__ == '__main__':
    unittest.main()
