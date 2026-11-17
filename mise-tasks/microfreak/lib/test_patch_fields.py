"""Conversions measured on the instrument, checked against the measured points."""
import unittest

import patch_fields as P


class ConversionTests(unittest.TestCase):
    def test_bend_range_is_the_stored_choice_in_semitones(self):
        for n in (0, 1, 2, 5, 7, 12, 24):
            self.assertEqual(P.display('VCO.BendRng', round(n * 32767 / 24), 24)['value'], n)
        self.assertEqual(P.setting('VCO.BendRng', 7), ('choice', 7))

    def test_glide_time_is_ten_seconds_times_the_cube(self):
        measured = {0.3: 0.272, 0.4: 0.641, 0.5: 1.252, 0.6: 2.162, 0.7: 3.438}
        for stored, seconds in measured.items():
            self.assertAlmostEqual(P.glide_seconds(stored), seconds, delta=0.02)
        self.assertAlmostEqual(P.glide_stored(1.25), 0.5, places=6)

    def test_glide_reads_the_mode_and_the_arp_rate(self):
        context = {'Kbd.GlMode': 32767, 'Arp.Rate': 0}
        self.assertEqual(P.display('Kbd.Glide', round(0.6 * 32767), 0, context)['unit'], 'seconds per octave')
        context['Kbd.GlMode'] = 16384
        sync = P.display('Kbd.Glide', round(0.55 * 32767), 0, context)
        self.assertEqual(sync['value'], '1/16')
        self.assertAlmostEqual(sync['seconds_at_arp_rate'], 0.5)
        self.assertEqual(P.display('Kbd.Glide', 32767, 0, context)['value'], '1/2')
        self.assertEqual(P.glide_setting('Sync', '1/8T'), ('decimal', 0.65))
        self.assertEqual(P.display('Kbd.Glide', 0, 0, context)['text'], 'off')

    def test_unison_spread_is_two_slopes_meeting_at_one_semitone(self):
        measured = {0.1: 0.19, 0.25: 0.5, 0.5: 1.01, 0.55: 2.09, 0.6: 3.23, 0.75: 6.5, 0.9: 9.8, 1.0: 12.0}
        for stored, semitones in measured.items():
            self.assertAlmostEqual(P.unison_semitones(stored), semitones, delta=0.05)
        for semitones in (0.05, 0.5, 1.0, 3.0, 12.0):
            self.assertAlmostEqual(P.unison_semitones(P.unison_stored(semitones)), semitones)
        self.assertEqual(P.unison_voices(4, 1.0), [-2.0, -1.0, 1.0, 2.0])
        self.assertEqual(P.display('Gen.UniCnt', 16384, 2)['value'], 3)

    def test_chord_offsets_and_paraphonic_modes(self):
        self.assertEqual(P.chord_raw(4), 0x4200)
        self.assertEqual(P.chord_offset(0x4000 - (5 << 7)), -5)
        self.assertIsNone(P.chord_offset(0x7F80))
        self.assertEqual(P.setting('Gen.ChOffs3', None), ('raw', 0x7F80))
        self.assertEqual(P.display('Gen.Chord', 32767, 3)['value'], 'Unison')
        self.assertEqual(P.setting('Gen.Chord', 'chord'), ('choice', 2))

    def test_preset_volume_and_arp_rate(self):
        self.assertEqual(P.display('Gen.PrstVol', 0, 24)['level_db'], -5.5)
        self.assertEqual(P.setting('Gen.PrstVol', -12), ('choice', 0))
        for stored, bpm in {0: 30.0, 8192: 84.6, 13500: 120.0, 16384: 139.2, 24575: 193.8, 32767: 240.0}.items():
            self.assertAlmostEqual(P.arp_bpm(stored), bpm, delta=0.2)
        self.assertEqual(P.arp_raw(120), 13500)

    def test_modulation_switches_read_and_write_by_name(self):
        self.assertEqual(P.display('LFO.Retrig', 32767, 2)['value'], 'Legato')
        self.assertEqual(P.display('Kbd.Veloc', 32767, 1)['value'], 'Velocity')
        self.assertEqual(P.display('EG2.Snap', 1, 1)['value'], 'Off')
        self.assertEqual(P.setting('Mat.KyMdSrc', 'Random'), ('choice', 1))
        self.assertEqual(P.setting('EG2.Legato', True), ('choice', 1))
        self.assertEqual(P.setting('LFO.Retrig', 'legato'), ('choice', 2))
        with self.assertRaises(ValueError):
            P.setting('Kbd.Veloc', 'pressure')

    def test_scale_and_root_follow_the_guide_order(self):
        self.assertEqual(P.display('Kbd.Scale', 8192, 8)['value'], 'Major')
        self.assertEqual(P.display('Kbd.Scale', 32767, 8)['value'], 'Pentatonic')
        self.assertEqual(P.display('Kbd.Root', round(2 * 32767 / 11), 11)['value'], 'D')
        self.assertEqual(P.setting('Kbd.Scale', 'harmonic minor'), ('choice', 4))
        self.assertEqual(P.setting('Kbd.Root', 'Bb'), ('choice', 10))

    def test_matrix_amounts_name_their_row_and_column(self):
        shown = P.display('Co1.Xpr', round(0.25 * 32767), 0)
        self.assertEqual((shown['source'], shown['destination']), ('Pressure', 'Pitch'))
        self.assertEqual(shown['semitones_at_full_source'], 12.0)
        self.assertEqual(P.display('Co4.EG2', (-16384) & 0xFFFF, 0)['value'], -0.5)
        self.assertEqual(P.display('Co6.Key', 0, 0)['destination'], 'Assign 2')
        self.assertEqual(P.setting('Co2.LFO', -0.3), ('decimal', -0.3))

    def test_assign_destinations_use_the_section_numbering(self):
        ids = P.destination_ids()
        heard = {'VCO.Param1': 0x0001, 'VCO.Param2': 0x0003, 'VCO.Param3': 0x0005, 'VCF.Cutoff': 0x0101,
                 'VCF.Reso': 0x0102, 'Kbd.Glide': 0x0300, 'LFO.Rate': 0x0502, 'EG2.DecRel': 0x0602,
                 'EG2.Sustain': 0x0603, 'Gen.UniSprd': 0x0705, 'Co1.LFO': 0x0A02}
        for field, value in heard.items():
            self.assertEqual(ids[field], value)
        self.assertEqual(ids['Co4.EG2'], 0x0D01)
        self.assertEqual(P.display('Mat.Assign1', 0x0603, 0)['value'], 'EG2.Sustain')
        self.assertTrue(P.display('Mat.Assign1', 0x0603, 0)['heard'])
        self.assertEqual(P.setting('Mat.Assign2', 'LFO.Rate'), ('raw', 0x0502))
        with self.assertRaises(ValueError):
            P.setting('Mat.Assign1', 'VCO.Type')

    def test_times_and_cutoff_between_measured_points(self):
        self.assertAlmostEqual(P.display('EG2.Attack', round(0.5 * 32767), 0)['value'], 0.561, places=2)
        decay = P.display('EG2.DecRel', round(0.3 * 32767), 0)
        self.assertAlmostEqual(decay['value'], 0.49, places=2)
        self.assertAlmostEqual(decay['release_seconds_to_minus_20_db'], 0.341, places=2)
        self.assertEqual(P.display('VCF.Cutoff', round(0.6 * 32767), 0)['value'], 1240)
        self.assertIsNone(P.display('VCF.Cutoff', round(0.95 * 32767), 0))
        self.assertAlmostEqual(P.value_for(1240, P.CUTOFF_POINTS, 'Cutoffs', 'Hz'), 0.6)
        self.assertEqual(P.display('Arp.Range', 32767, 3)['value'], 4)
        self.assertEqual(P.display('LFO.Div', round(6 * 32767 / 12), 12)['value'], '1/4')

    def test_cycling_envelope_resonance_and_fast_lfo(self):
        self.assertAlmostEqual(P.cycling_stage_seconds(0.5), 1.25)
        self.assertAlmostEqual(P.cycling_hold_seconds(0.4), 1.6)
        self.assertAlmostEqual(P.cycling_hold_stored(3.6), 0.6)
        self.assertEqual(P.display('EG1.Hold', 16384, 0, {'EG1.Mode': 0})['unit'], 'sustain level in Env mode')
        self.assertEqual(P.display('EG1.Hold', 16384, 0, {'EG1.Mode': 32767})['unit'], 'seconds in Run and Loop')
        self.assertAlmostEqual(P.resonance_peak_db(0.8), 9.4)
        self.assertAlmostEqual(P.lfo_hz(1.0), 100.1)
        self.assertAlmostEqual(P.lfo_stored(46.8), 0.9)

    def test_add_display_leaves_unknown_fields_alone(self):
        fields = [{'name': 'VCO.BendRng', 'descriptor': 24, 'value_le_unsigned': 16384},
                  {'name': 'VCO.Param1', 'descriptor': 238, 'value_le_unsigned': 100}]
        items = P.add_display([{'name': 'VCO.BendRng'}, {'name': 'VCO.Param1'}], fields)
        self.assertEqual(items[0]['display']['value'], 12)
        self.assertNotIn('display', items[1])


if __name__ == '__main__':
    unittest.main()
