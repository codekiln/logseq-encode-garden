import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import preset_page as p  # noqa: E402


def field(name, value, kind=None, label=None, **extra):
    if kind is None:
        kind = 'normalized_0_1' if isinstance(value, float) else 'metadata_scaled_integer'
    return {'name': name, 'label': label or name, 'kind': kind, 'value': value, **extra}


def interp(model='SuperWave', **overrides):
    labels = {'SuperWave': ('Wave', 'Detune', 'Volume'), 'Chords': ('Type', 'Inv/Transp', 'VCO.Param3')}[model]
    values = {
        'VCO.Param1': 1, 'VCO.Param2': 0.433, 'VCO.Param3': 0.496, 'Kbd.Octave': 1, 'Kbd.Glide': 0.0,
        'VCF.Type': 0, 'VCF.Cutoff': 0.732, 'VCF.Reso': 0.764, 'EG2.Attack': 0.0, 'EG2.DecRel': 0.126,
        'EG2.Sustain': 0.0, 'EG2.Mode': 0, 'EG1.Mode': 0, 'EG1.RiseLvl': 0.0, 'EG1.Amount': 1.0,
        'LFO.Shape': 4, 'LFO.Sync': 0, 'LFO.Rate': 0.047, 'Gen.Parafon': 0,
        'Co1.EG2': 1.0, 'Co5.LFO': 1.0, 'Mat.Assign1': 7, 'Mat.Assign2': 0, 'Mat.Assign3': 0,
    }
    values.update(overrides)
    fields = [field('VCO.Type', 2, kind='engine_index', model=model)]
    for name, value in values.items():
        kind = 'normalized_minus_1_1' if name.startswith('Co') else None
        label = labels[int(name[-1]) - 1] if name.startswith('VCO.Param') else None
        fields.append(field(name, value, kind=kind, label=label))
    return {'oscillator': {'index': 2, 'model': model}, 'fields': fields}


ADDRESS = {7: 'LFO.Rate'}


class DescribeTest(unittest.TestCase):
    def test_links_strip_back_to_plain_wording(self):
        linked = p.render(p.describe(interp(), ADDRESS))
        plain = p.render(p.describe(interp(), ADDRESS, linked=False))
        self.assertEqual([p.strip_links(line) for line in linked], plain)
        self.assertIn('\t\t- Model: SuperWave. [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]', plain)
        self.assertIn('\t\t- LFO → Assign 1 → LFO Rate: +1.000.', plain)

    def test_controls_link_to_panel_pages(self):
        text = '\n'.join(p.render(p.describe(interp(), ADDRESS)))
        self.assertIn('[Detune]([[Microfreak/UI/Oscillator/Knob/Type/SuperWave/Detune]]): 0.433.', text)
        self.assertIn('[Low-pass]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Button/Type/LPF]])', text)
        self.assertIn('[Sample-and-Hold]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Button/Shape/Random Stepped]])', text)
        self.assertIn('[Assign 1]([[Microfreak/UI/Front/Row/Top/01 Matrix/Button/Assn/1]]) → '
                      '[LFO Rate]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate]])', text)

    def test_parameter_page_names(self):
        self.assertEqual(p.param_page('Chords', 2, 'Inv/Transp'),
                         'Microfreak/UI/Oscillator/Knob/Type/Chords/Inv Transp')
        self.assertEqual(p.param_page('Chords', 3, 'Shape control'),
                         'Microfreak/UI/Oscillator/Knob/Type/Chords/Waveform')
        self.assertEqual(p.param_page('V.Analog', 1, 'Detune'),
                         'Microfreak/UI/Oscillator/Knob/Type/VAnalog/Detune')
        self.assertEqual(p.param_page(None, 2, 'VCO.Param2'), 'Microfreak/UI/Oscillator/Knob/Timbre')


class CustomizedTest(unittest.TestCase):
    def test_lists_only_changed_controls(self):
        lines = p.customized(interp(**{'VCF.Cutoff': 0.5, 'EG2.Mode': 1, 'VCF.Reso': 0.7642}),
                             interp(), ADDRESS)
        self.assertEqual(lines, [
            '[Cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): 0.500 (factory 0.732).',
            '[Amp Mod]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Button/Amp Mod]]): on (factory off).',
        ])

    def test_matrix_and_assign_changes(self):
        lines = p.customized(interp(**{'Co1.EG2': 0.5, 'Mat.Assign1': 0}), interp(), ADDRESS, linked=False)
        self.assertIn('Matrix ENV → Pitch: +0.500 (factory +1.000).', lines)
        self.assertIn('Assign 1 destination: unresolved (factory LFO Rate).', lines)

    def test_nearest_picks_fewest_differences(self):
        mine = interp(**{'VCF.Cutoff': 0.5})
        factory = {'far': ('Factory1.0', 1, 'a.mbp', 'Far', interp(**{'VCF.Cutoff': 0.1, 'VCF.Reso': 0.1})),
                   'near': ('Factory2.0', 2, 'b.mbp', 'Near', interp())}
        count, sha, entry = p.nearest(mine, factory, ADDRESS)
        self.assertEqual((count, sha), (1, 'near'))


class PageTest(unittest.TestCase):
    BODY = ['- # Notes', '\t- ## Saved export and provenance',
            '\t\t- Saved export: read from the device. Two consecutive reads returned the same file.',
            '\t- ## Oscillator', '\t\t- old', '\t- ## Filter', '\t\t- old'] + p.EVIDENCE

    def test_replace_keeps_provenance_and_evidence(self):
        body = p.replace_sections(self.BODY, [('Oscillator', ['new'])])
        self.assertEqual(body[:3], self.BODY[:3])
        self.assertEqual(body[3:5], ['\t- ## Oscillator', '\t\t- new'])
        self.assertEqual(body[5:], p.EVIDENCE)
        self.assertTrue(p.is_generated(self.BODY))

    def test_refuses_handwritten_section_between_generated_ones(self):
        body = self.BODY[:5] + ['\t- ## My Notes', '\t\t- mine'] + self.BODY[5:]
        with self.assertRaises(ValueError):
            p.replace_sections(body, [('Oscillator', ['new'])])

    def test_split_and_frontmatter(self):
        front, body = p.split_page('a:: 1\nb:: 2\n- # Notes\n')
        self.assertEqual((front, body), (['a:: 1', 'b:: 2'], ['- # Notes']))
        self.assertEqual(p.frontmatter_set(front, 'b', '3'), ['a:: 1', 'b:: 3'])
        self.assertEqual(p.frontmatter_set(front, 'c', '4'), ['a:: 1', 'b:: 3', 'c:: 4'])

    def test_asset_names(self):
        page, filename, url = p.asset_names('Microfreak/Preset/350 Smooth IPA', '2026-10-25')
        self.assertEqual(page, 'Microfreak/Preset/350 Smooth IPA/Asset/Device-Read-2026-10-25/bin')
        self.assertEqual(filename, 'Microfreak___Preset___350 Smooth IPA___Asset___Device-Read-2026-10-25.bin')
        self.assertTrue(url.endswith('350%20Smooth%20IPA___Asset___Device-Read-2026-10-25.bin'))


if __name__ == '__main__':
    unittest.main()
