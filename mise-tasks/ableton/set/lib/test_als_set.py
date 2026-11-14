import gzip
import io
import tempfile
import unittest
import xml.etree.ElementTree as ET
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path

from als_set import SetError, file_name, main, plan_pages, read_set, time_signature

PERFORMANCE = 'GitP/A/Session/26/11/01-Sun'


def value(parent, tag, text):
    ET.SubElement(parent, tag, Value=text)


def route(chain, tag, target, lower='', upper=None):
    """One routing: the target Live stores, and the text of the two boxes Live shows for it."""
    element = ET.SubElement(chain, tag)
    value(element, 'Target', target)
    if upper is not None:
        value(element, 'UpperDisplayString', upper)
        value(element, 'LowerDisplayString', lower)


def track(tracks, kind, ident, name, group='-1', monitor=None, armed=None, devices=(), routes=(), user_devices=()):
    element = ET.SubElement(tracks, kind, Id=ident)
    names = ET.SubElement(element, 'Name')
    value(names, 'EffectiveName', name)
    value(names, 'UserName', name)
    value(element, 'TrackGroupId', group)
    chain = ET.SubElement(element, 'DeviceChain')
    for tag, target, *shown in routes:
        route(chain, tag, target, *shown)
    sequencer = ET.SubElement(chain, 'MainSequencer')
    if monitor is not None:
        value(sequencer, 'MonitoringEnum', str(monitor))
    if armed is not None:
        value(ET.SubElement(sequencer, 'Recorder'), 'IsArmed', armed)
    listed = ET.SubElement(ET.SubElement(chain, 'DeviceChain'), 'Devices')
    for device in devices:
        ET.SubElement(listed, device)
    for device, user in user_devices:
        value(ET.SubElement(listed, device), 'UserName', user)
    return element


def fixture(signature='201', tempo='120', creator='Ableton Live 11.3.43'):
    """A small Set built from XML: a group holding an audio and a MIDI track, a loose track, a return."""
    root = ET.Element('Ableton', Creator=creator)
    live = ET.SubElement(root, 'LiveSet')
    tracks = ET.SubElement(live, 'Tracks')
    track(tracks, 'GroupTrack', '1', 'Pattern A', routes=[('AudioOutputRouting', 'AudioOut/Master', '', 'Master')])
    track(tracks, 'AudioTrack', '2', 'Pattern A Audio', group='1', monitor=1, armed='false',
          devices=['GlueCompressor', 'Compressor2'],
          routes=[('AudioInputRouting', 'AudioIn/External/S0', '1/2', 'Ext. In'),
                  ('AudioOutputRouting', 'AudioOut/GroupTrack', '', 'Group')])
    track(tracks, 'MidiTrack', '3', 'Pattern A MIDI', group='1', monitor=0, armed='true',
          routes=[('MidiInputRouting', 'MidiIn/External.All/-1', '', 'Ext: All Ins'),
                  ('MidiOutputRouting', 'MidiOut/Track.4/TrackIn', 'Track In', 'Lead / Synth'),
                  ('AudioOutputRouting', 'AudioOut/GroupTrack', '', 'Group')])
    track(tracks, 'MidiTrack', '4', 'Lead / Synth', monitor=2, armed='false', user_devices=[('Operator', 'My Lead')],
          routes=[('MidiInputRouting', 'MidiIn/Track.3/TrackOut', 'Post Mixer', 'Pattern A MIDI'),
                  ('MidiOutputRouting', 'MidiOut/None', '', 'None'),
                  # A file without the display text: the target itself is written.
                  ('AudioOutputRouting', 'AudioOut/Master')])
    track(tracks, 'ReturnTrack', '5', 'A-Reverb', devices=['Reverb'],
          routes=[('AudioOutputRouting', 'AudioOut/Track.99/TrackIn', 'Track In', 'Gone')])
    mixer = ET.SubElement(ET.SubElement(ET.SubElement(live, 'MasterTrack'), 'DeviceChain'), 'Mixer')
    value(ET.SubElement(mixer, 'Tempo'), 'Manual', tempo)
    value(ET.SubElement(mixer, 'TimeSignature'), 'Manual', signature)
    return root


def write_als(directory, root, name='26.11.01.als'):
    path = Path(directory) / name
    path.write_bytes(gzip.compress(ET.tostring(root)))
    return path


def garden(directory):
    path = Path(directory) / 'garden'
    (path / 'pages').mkdir(parents=True)
    return path


def run(*args):
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        code = main(list(args))
    return code, out.getvalue(), err.getvalue()


class PlanTests(unittest.TestCase):
    def plan(self, root=None, directory='/nonexistent'):
        return {page: (action, text) for _, (action, text, page) in
                plan_pages(root if root is not None else fixture(), PERFORMANCE, '26.11.01.als', directory).items()}

    def test_set_page_names_the_set_and_embeds_top_level_pages_in_live_order(self):
        action, text = self.plan()[f'{PERFORMANCE}/Set']
        self.assertEqual(action, 'create')
        self.assertEqual(text, (
            'logseq-entity:: [[Logseq/Entity/Ableton/Set]]\n\n- # 26.11.01\n'
            '  live-version:: 11.3.43\n  tempo:: 120\n  time-signature:: 4/4\n  source:: 26.11.01.als\n'
            f'\t- {{{{embed [[{PERFORMANCE}/Set/Track/Pattern A]]}}}}\n'
            f'\t- {{{{embed [[{PERFORMANCE}/Set/Track/Lead - Synth]]}}}}\n'
            f'\t- {{{{embed [[{PERFORMANCE}/Set/Track/A-Reverb]]}}}}\n'))

    def test_group_embeds_its_tracks_and_tracks_sit_under_the_group(self):
        pages = self.plan()
        base = f'{PERFORMANCE}/Set/Track'
        action, text = pages[f'{base}/Pattern A']
        self.assertEqual(text, (
            'logseq-entity:: [[Logseq/Entity/Ableton/Track/Group]]\n\n- # Pattern A\n  type:: group\n  audio-to:: Master\n'
            f'\t- {{{{embed [[{base}/Pattern A/Pattern A Audio]]}}}}\n'
            f'\t- {{{{embed [[{base}/Pattern A/Pattern A MIDI]]}}}}\n'))
        self.assertIn('logseq-entity:: [[Logseq/Entity/Ableton/Track/Track]]', pages[f'{base}/Pattern A/Pattern A Audio'][1])

    def test_track_settings_follow_type(self):
        pages = self.plan()
        base = f'{PERFORMANCE}/Set/Track'
        self.assertEqual(pages[f'{base}/Pattern A/Pattern A Audio'][1].split('\n\n', 1)[1], (
            # Live's two boxes, and the track's own group as a link to the group's page.
            f'- # Pattern A Audio\n  type:: audio\n  audio-from:: Ext. In 1/2\n  audio-to:: [[{base}/Pattern A]]\n'
            '  monitor:: auto\n  arm:: false\n  devices:: GlueCompressor, Compressor2\n'))
        self.assertEqual(pages[f'{base}/Pattern A/Pattern A MIDI'][1].split('\n\n', 1)[1], (
            # A routing to another track of the Set links that track's page, then Live's second box.
            '- # Pattern A MIDI\n  type:: midi\n  midi-from:: Ext: All Ins\n'
            f'  midi-to:: [[{base}/Lead - Synth]] Track In\n  midi-channel:: all\n  monitor:: in\n  arm:: true\n'))
        # A MIDI track with no MIDI destination records its own audio output; a named device keeps its name.
        self.assertEqual(pages[f'{base}/Lead - Synth'][1].split('\n\n', 1)[1], (
            f'- # Lead / Synth\n  type:: midi\n  audio-to:: AudioOut/Master\n  midi-from:: [[{base}/Pattern A/Pattern A MIDI]] Post Mixer\n'
            '  midi-to:: None\n  monitor:: off\n  arm:: false\n  devices:: My Lead\n'))
        # A target that names a track the Set does not hold keeps Live's text.
        self.assertEqual(pages[f'{base}/A-Reverb'][1].split('\n\n', 1)[1],
                         '- # A-Reverb\n  type:: return\n  audio-to:: Gone Track In\n  devices:: Reverb\n')

    def test_midi_channel_comes_from_the_input_routing(self):
        root = fixture()
        track(root.find('LiveSet/Tracks'), 'MidiTrack', '8', 'Keys', monitor=1, armed='true',
              routes=[('MidiInputRouting', 'MidiIn/External.Dev:Launchpad Pro MK3 (LPProMK3 MIDI)/4', 'Ch. 5',
                       'Launchpad Pro MK3 (LPProMK3 MIDI)'),
                      ('MidiOutputRouting', 'MidiOut/External.Dev:Arturia MicroFreak/0', 'Ch. 1', 'Arturia MicroFreak')])
        self.assertEqual(self.plan(root)[f'{PERFORMANCE}/Set/Track/Keys'][1].split('\n\n', 1)[1], (
            '- # Keys\n  type:: midi\n  midi-from:: Launchpad Pro MK3 (LPProMK3 MIDI) Ch. 5\n'
            '  midi-to:: Arturia MicroFreak Ch. 1\n  midi-channel:: 5\n  monitor:: auto\n  arm:: true\n'))

    def test_public_marks_every_page(self):
        pages = {page: text for _, (_, text, page) in
                 plan_pages(fixture(), PERFORMANCE, '26.11.01.als', '/nonexistent', public=True).items()}
        self.assertEqual(len(pages), 6)
        for page, text in pages.items():
            self.assertEqual(text.split('\n')[1], 'public:: true', page)

    def test_time_signature_and_tempo(self):
        self.assertEqual([time_signature(code) for code in ('201', '302', '2', '0')], ['4/4', '6/8', '3/1', '1/1'])
        _, text = self.plan(fixture(signature='302', tempo='93.5'))[f'{PERFORMANCE}/Set']
        self.assertIn('  tempo:: 93.5\n  time-signature:: 6/8\n', text)

    def test_duplicate_names_in_one_group_are_refused(self):
        root = fixture()
        track(root.find('LiveSet/Tracks'), 'AudioTrack', '9', 'Pattern A Audio', group='1')
        with self.assertRaisesRegex(SetError, 'share the page'):
            self.plan(root)

    def test_unsafe_file_characters_are_encoded(self):
        self.assertEqual(file_name('GitP/A/Set/Track/What?'), 'GitP___A___Set___Track___What%3F.md')


class FileTests(unittest.TestCase):
    def test_preview_writes_nothing_and_apply_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            als, root = write_als(directory, fixture()), garden(directory)
            args = ['--als', str(als), '--performance', PERFORMANCE, '--garden', str(root)]
            code, out, _ = run(*args)
            self.assertEqual(code, 0)
            self.assertIn(f'create    {PERFORMANCE}/Set\n', out)
            self.assertEqual(list((root / 'pages').iterdir()), [])
            self.assertEqual(run(*args, '--apply')[0], 0)
            written = {path.name: path.read_text() for path in (root / 'pages').iterdir()}
            self.assertEqual(len(written), 6)
            _, out, _ = run(*args, '--apply')
            self.assertNotIn('create', out)
            self.assertNotIn('update', out)
            self.assertEqual({path.name: path.read_text() for path in (root / 'pages').iterdir()}, written)

    def test_rerun_keeps_hand_written_lines_and_refreshes_owned_ones(self):
        with tempfile.TemporaryDirectory() as directory:
            root = garden(directory)
            args = lambda als: ['--als', str(als), '--performance', PERFORMANCE, '--garden', str(root)]
            run(*args(write_als(directory, fixture())), '--apply')
            audio = root / 'pages' / file_name(f'{PERFORMANCE}/Set/Track/Pattern A/Pattern A Audio')
            text = audio.read_text()
            audio.write_text(text.replace('  monitor:: auto\n', '  monitor:: auto\n  color:: red\n')
                             .replace('  arm:: false\n', '  arm:: true\n') + '\t- Holds layer A\'s audio loops.\n')
            setfile = root / 'pages' / file_name(f'{PERFORMANCE}/Set')
            setfile.write_text(setfile.read_text().replace('\t- {{embed', '\t- My note\n\t- {{embed', 1) + '\t- Another note\n')
            changed = fixture(tempo='122')
            track(changed.find('LiveSet/Tracks'), 'AudioTrack', '7', 'Commentary')
            code, out, _ = run(*args(write_als(directory, changed)), '--apply')
            self.assertEqual(code, 0)
            self.assertIn(f'update    {PERFORMANCE}/Set\n', out)
            self.assertIn(f'update    {PERFORMANCE}/Set/Track/Pattern A/Pattern A Audio\n', out)
            self.assertIn(f'create    {PERFORMANCE}/Set/Track/Commentary\n', out)
            audio_text = audio.read_text()
            self.assertIn('  color:: red\n', audio_text)
            self.assertIn('  arm:: false\n', audio_text)
            self.assertTrue(audio_text.endswith("\t- Holds layer A's audio loops.\n"))
            set_text = setfile.read_text()
            self.assertIn('  tempo:: 122\n', set_text)
            self.assertIn('\t- My note\n', set_text)
            self.assertTrue(set_text.endswith('\t- Another note\n'))
            self.assertIn('Set/Track/Commentary]]}}', set_text)
            self.assertEqual(set_text.count('{{embed'), 4)
            # --public marks pages that exist, once, and a second run changes nothing.
            self.assertNotIn('public::', set_text)
            run(*args(write_als(directory, changed)), '--public', '--apply')
            for path in (root / 'pages').iterdir():
                lines = path.read_text().split('\n')
                self.assertEqual((lines[0][:15], lines[1], lines[2]), ('logseq-entity::', 'public:: true', ''), path.name)
            _, out, _ = run(*args(write_als(directory, changed)), '--public', '--apply')
            self.assertNotIn('update', out)
            self.assertIn('  color:: red\n', audio.read_text())

    def test_bad_inputs_fail_with_a_message(self):
        with tempfile.TemporaryDirectory() as directory:
            plain = Path(directory) / 'plain.als'
            plain.write_text('not gzip')
            code, _, err = run('--als', str(plain), '--performance', PERFORMANCE, '--garden', directory)
            self.assertEqual(code, 1)
            self.assertIn('not a gzip', err)
            notset = write_als(directory, ET.Element('Other'), 'other.als')
            self.assertEqual(run('--als', str(notset), '--performance', PERFORMANCE, '--garden', directory)[0], 1)
            als = write_als(directory, fixture())
            self.assertEqual(run('--als', str(als), '--performance', '/bad/', '--garden', directory)[0], 1)


if __name__ == '__main__':
    unittest.main()
