"""A synthetic firmware-5 style preset only: no user or factory patch data."""
import unittest

import parameters
import patch
import patch_fields as P
import sequence as Q
from test_sequence import field, synthetic

SECTIONS = {
    'VCO': [('Type', 22, 2979), ('Param1', 238, 0), ('Param2', 238, 0), ('Param3', 238, 0), ('BendRng', 24, 16384)],
    'VCF': [('Type', 2, 0), ('Cutoff', 0, 32767), ('Reso', 0, 0)],
    'EG1': [('Mode', 2, 0), ('RiseLvl', 0, 0), ('RiseSlp', 0, 16383), ('FallLvl', 0, 0), ('Hold', 0, 0),
            ('FallSlp', 0, 16383), ('Amount', 0, 0)],
    'Kbd': [('Glide', 0, 0), ('Octave', 6, 16384), ('Veloc', 1, 0), ('GlMode', 2, 0), ('PresAmp', 10, 0),
            ('Scale', 8, 0), ('Root', 11, 0)],
    'Arp': [('Div', 10, 22937), ('Rate', 0, 13500), ('SeqOn', 1, 0)],
    'LFO': [('Shape', 5, 0), ('Rate', 0, 16384), ('Sync', 1, 0), ('Retrig', 2, 0)],
    'EG2': [('Mode', 1, 32767), ('Attack', 0, 0), ('DecRel', 0, 9000), ('Sustain', 0, 32767), ('Legato', 1, 0),
            ('Snap', 1, 1)],
    'Gen': [('Parafon', 1, 0), ('PrstVol', 24, 16384), ('UniSprd', 233, 1985), ('UniCnt', 2, 32767),
            ('Chord', 3, 0), ('ChOffs1', 247, 0x4000), ('ChOffs2', 247, 0x4000), ('ChOffs3', 247, 0x4000)],
    'Mat': [('Assign1', 0, 0), ('Assign2', 0, 0), ('Assign3', 0, 0), ('KyMdSrc', 1, 0)],
    **{f'Co{n}': [(row, 0, 0) for row in ('EG1', 'EG2', 'LFO', 'Xpr', 'Key')] for n in range(1, 8)},
    'Seq': [('Length', 60, 6553), ('GateLen', 80, 16384)] + [(f'Smooth{n}', 1, 0) for n in range(1, 5)],
}


def full_preset():
    block = b''.join(b'#' + name.encode() + b''.join(field(k, d, v) for k, d, v in fields) + b'@'
                     for name, fields in SECTIONS.items()) + b' '
    data = bytearray(parameters.unpack_payload(synthetic()))
    data[:1980] = block.ljust(1980, b'\xff')
    return Q.pack_payload(bytes(data))


def values(payload):
    return {f['name']: f['value_le_unsigned'] for f in parameters.parse_parameters(payload)['fields']}


class PatchTests(unittest.TestCase):
    def setUp(self):
        self.base = full_preset()

    def test_sections_write_their_fields(self):
        new, changed = patch.prepare({
            'oscillator': {'type': 'Two Op. FM', 'timbre': 0.5},
            'filter': {'type': 'BPF', 'cutoff': 0.25},
            'envelope': {'attack': 0.1, 'amp_mod': 'off', 'legato': True},
            'lfo': {'shape': 'Square', 'retrig': 'Legato'},
            'keyboard': {'bend_range': 2, 'scale': 'Minor', 'root': 'A', 'velo_amp_mod': 5},
            'arp': {'bpm': 120},
        }, self.base)
        v = values(new)
        self.assertEqual(v['VCO.Type'], round(8 * 32767 / 22))
        self.assertEqual(v['VCO.Param2'], 16384)
        self.assertEqual(v['VCF.Type'], 16384)
        self.assertEqual(v['EG2.Mode'], 0)
        self.assertEqual(v['LFO.Retrig'], 32767)
        self.assertEqual(v['Kbd.Root'], round(9 * 32767 / 11))
        self.assertEqual(v['Kbd.PresAmp'], 16384)
        self.assertEqual(changed['VCO.BendRng'], ['±12 semitones', '±2 semitones'])
        self.assertEqual(changed['Kbd.Scale'][1], 'Minor')
        self.assertNotIn('Arp.Rate', changed)

    def test_glide_and_voice(self):
        new, changed = patch.prepare({'glide': {'mode': 'Sync', 'division': '1/16'},
                                      'voice': {'mode': 'Unison', 'unison_voices': 3, 'unison_spread': 0.5,
                                                'volume': -2}}, self.base)
        v = values(new)
        self.assertEqual(v['Kbd.GlMode'], 16384)
        self.assertEqual(v['Kbd.Glide'], round(0.55 * 32767))
        self.assertEqual(v['Gen.Parafon'], 32767)
        self.assertEqual(changed['Gen.UniSprd'][1], '0.500')
        self.assertEqual(changed['Gen.PrstVol'][1], '-2 (-1.0 dB)')
        new, _ = patch.prepare({'voice': {'mode': 'Chord', 'chord': [3, 7]}}, self.base)
        v = values(new)
        self.assertEqual((v['Gen.ChOffs1'], v['Gen.ChOffs2'], v['Gen.ChOffs3']), (0x4180, 0x4380, 0x7F80))

    def test_matrix_is_whole_and_fills_assign_columns(self):
        base, _ = patch.prepare({'fields': {'Co4.EG2': 0.5}}, self.base)
        new, _ = patch.prepare({'matrix': [
            {'source': 'LFO', 'destination': 'Pitch', 'semitones': 0.5},
            {'source': 'Pressure', 'destination': 'Cutoff', 'amount': 0.3},
            {'source': 'Envelope', 'destination': 'LFO rate', 'amount': -0.2},
            {'source': 'Key/Arp', 'destination': 'Gen.UniSprd', 'amount': 0.1},
            {'source': 'CycEnv', 'destination': 'LFO.Rate', 'amount': 0.4}]}, base)
        v = values(new)
        self.assertEqual(v['Co1.LFO'], round(0.5 / 48 * 32767))
        self.assertEqual(v['Co4.Xpr'], round(0.3 * 32767))
        self.assertEqual(v['Co4.EG2'], 0)
        self.assertEqual(v['Mat.Assign1'], 0x0502)
        self.assertEqual(v['Co5.EG2'], (-round(0.2 * 32767)) & 0xFFFF)
        self.assertEqual(v['Co5.EG1'], round(0.4 * 32767))
        self.assertEqual(v['Mat.Assign2'], 0x0705)
        with self.assertRaises(ValueError):
            patch.prepare({'matrix': [{'source': 'LFO', 'destination': d, 'amount': 0.1}
                                      for d in ('Glide', 'Resonance', 'Sustain', 'Attack')]}, self.base)

    def test_an_lfo_rate_turns_sync_off(self):
        base, _ = patch.prepare({'lfo': {'sync': 'on'}}, self.base)
        new, changed = patch.prepare({'lfo': {'hz': 4.785}}, base)
        v = values(new)
        self.assertEqual(v['LFO.Sync'], 0)
        self.assertAlmostEqual(v['LFO.Rate'] / 32767, 0.6, places=3)
        self.assertEqual(changed['LFO.Rate'][1], 'about 4.78 Hz')
        new, _ = patch.prepare({'lfo': {'rate': 0.3, 'sync': 'on'}}, base)
        self.assertEqual(values(new)['LFO.Sync'], 32767)

    def test_sequence_and_unknown_keys(self):
        new, changed = patch.prepare({'sequence': {'length': 4, 'patterns': {'A': {'steps': [{'notes': ['C4']}]}}}},
                                     self.base)
        self.assertEqual(Q.decode_sequence(new)['patterns']['A']['steps'][0]['notes'], [60])
        self.assertIn('Arp.SeqOn', changed)
        with self.assertRaises(ValueError):
            patch.prepare({'reverb': 1}, self.base)
        with self.assertRaises(ValueError):
            patch.prepare({'filter': {'type': 'Notch'}}, self.base)


if __name__ == '__main__':
    unittest.main()
