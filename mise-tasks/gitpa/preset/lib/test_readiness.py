import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from readiness import assess, audit, main

DETAILED = '''preset-synth-file-sha256:: {digest}
- # Notes
\t- ## Saved export and provenance
\t\t- Saved export: archived September 28 bank `saved.mfprojz`, computer bank slot 16, matches the later factory payload. No session-time capture is available.
\t\t- [Decoder evidence](https://example.com/decoder)
\t- ## Oscillator and controls
\t\t- SawX blends saw waves; Timbre controls detuning. [[Microfreak/UG/Oscillator]]
\t- ## Filter
\t\t- Low-pass with saved cutoff 0.4 normalized; no calibrated Hz conversion is verified.
\t- ## Envelopes
\t\t- Main attack is short; cycling envelope controls rate modulation.
\t- ## LFO
\t\t- Triangle shape, unsynced normalized rate 0.5; display units are unverified.
\t- ## Modulation matrix
\t\t- Pressure opens the filter; matrix amount is normalized signed −1…+1.
\t- ## Performance and session context
\t\t- This archive establishes a saved baseline, not the unsaved session edits heard in the recording.
'''.format(digest='a'*64)

class ReadinessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root/'pages').mkdir()
    def tearDown(self):
        self.temp.cleanup()
    def page(self, title, body):
        (self.root/'pages'/(title.replace('/', '___')+'.md')).write_text(body)
    def invoke(self, *args):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            status = main(['--garden', str(self.root), *args])
        return status, out.getvalue()
    def test_archived_evidence_does_not_require_new_public_binary_or_guessed_units(self):
        result = assess(DETAILED)
        self.assertEqual(result['status'], 'detailed')
        self.assertTrue(all(result['evidence'].values()))
        self.assertEqual(result['coverage']['lfo'], 'documented-with-limits')
        self.assertNotIn('preset-synth-file::', DETAILED)
    def test_stub_and_link_only_topic_bodies_are_reported_without_length_guessing(self):
        self.assertEqual(assess('- # Notes\n')['status'], 'stub')
        result = assess('- # Notes\n\t- ## Oscillator\n\t\t- [[Microfreak/UG/Oscillator]]\n\t- ## Filter\n\t\t- TODO research filter\n')
        self.assertEqual(result['status'], 'stub')
        self.assertEqual(result['coverage']['oscillator'], 'unresearched')
    def test_episode_aliases_repeated_links_and_literals_do_not_create_false_work(self):
        self.page('GitP/A/Session/26/10/22-Thu', '- [[VoIdOm]] [[Microfreak/Preset/016 Voidom]]\n- `[[Microfreak/Preset/Missing]]`\n- ~~~text\n  [[Microfreak/Preset/Fenced]]\n  - ~~~\n  [[Microfreak/Preset/Still fenced]]\n  ~~~\n')
        self.page('Microfreak/Preset/016 Voidom', 'alias:: [[Voidom]]\n'+DETAILED)
        result = audit(self.root, 'GitP/A/Session/26/10/22-Thu')[0]['presets']
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['status'], 'detailed')
    def test_missing_ambiguous_and_initialized_are_distinct(self):
        self.page('GitP/A/Session/26/10/22-Thu', '- [[Microfreak/Preset/Missing]] [[Same preset]] [[Microfreak/Preset/Initialized]]\n')
        self.page('Microfreak/Preset/001 One', 'alias:: [[Same preset]]\n- # Notes\n')
        self.page('Microfreak/Preset/002 Two', 'alias:: [[Same preset]]\n- # Notes\n')
        states = {row['status'] for row in audit(self.root)[0]['presets']}
        self.assertEqual(states, {'missing', 'ambiguous', 'initialized'})
    def test_historical_report_is_advisory_but_selected_episode_check_fails_on_gaps(self):
        episode = 'GitP/A/Session/26/10/22-Thu'
        self.page(episode, '- [[Microfreak/Preset/016 Voidom]]\n')
        self.page('Microfreak/Preset/016 Voidom', '- # Notes\n')
        self.assertEqual(self.invoke('--all')[0], 0)
        status, output = self.invoke('--episode', episode, '--check', '--json')
        self.assertEqual(status, 1)
        self.assertEqual(json.loads(output)[0]['presets'][0]['status'], 'stub')
        self.page('Microfreak/Preset/016 Voidom', DETAILED)
        self.assertEqual(self.invoke('--episode', episode, '--check')[0], 0)
    def test_cli_rejects_check_all_and_unknown_episode(self):
        for args in [('--all', '--check'), ('--episode', 'Unknown')]:
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as caught:
                self.invoke(*args)
            self.assertEqual(caught.exception.code, 2)
    def test_separate_labelled_citations_count_but_loose_urls_do_not(self):
        body = DETAILED.replace('\t\t- [Decoder evidence](https://example.com/decoder)\n', '').replace(' [[Microfreak/UG/Oscillator]]', '')
        self.assertFalse(assess(body + '- Bare URL https://example.com/manual\n')['evidence']['sources_cited'])
        self.assertTrue(assess(body + '\t- ## Evidence and interpretation\n\t\t- Read the [saved-parameter inspector](https://example.com/decoder).\n')['evidence']['sources_cited'])
    def test_fenced_frontmatter_examples_are_not_recorded_export_evidence(self):
        example = '~~~text\npreset-synth-file:: https://example.com/fake.mbp\npreset-synth-file-sha256:: '+'a'*64+'\n~~~\n- # Notes\n'
        result = assess(example)
        self.assertFalse(result['evidence']['digest_recorded'])
        self.assertFalse(result['evidence']['export_reference_recorded'])
    def test_invalid_garden_is_an_error_not_an_empty_clean_audit(self):
        with self.assertRaises(ValueError):
            audit(self.root/'absent')
    def test_evidence_status_does_not_turn_a_digest_or_name_into_complete_research(self):
        result = assess('preset-synth-file-sha256:: '+'a'*64+'\npreset-synth-file:: https://example.com/preset.mfpz\n- # Notes\n')
        self.assertEqual(result['status'], 'stub')
        self.assertFalse(result['evidence']['sources_cited'])
        self.assertTrue(result['evidence']['digest_recorded'])

if __name__ == '__main__':
    unittest.main()
