from datetime import datetime
import gzip
import importlib.machinery
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

TASK = Path(__file__).resolve().parents[1] / 'sync'
loader = importlib.machinery.SourceFileLoader('ableton_locators_sync', str(TASK))
spec = importlib.util.spec_from_loader(loader.name, loader)
locators = importlib.util.module_from_spec(spec)
sys.modules[loader.name] = locators
loader.exec_module(locators)

PAGE = 'GitP/A/Session/26/11/01-Sun'
EPISODE = '''public:: true

- # Infini Pad bass and 8bitfi
\t- ## Chapters
\t\t- ### 00:00 Enter [[Microfreak/Preset/259 Infini Pad]]
\t\t\t- #### 00:00 [[Launchpad]] playing infini pad
\t\t\t- #### 03:07 Envelopes, **Fold** and #Noise
\t\t- ### {{audio-timestamp 1097}} Enter [8bitfi]([[Microfreak/Preset/260 8bitfi]])
\t\t\t- #### 26:32–26:40 · Closing fade
\t\t\t- #### Untimed heading
\t\t\t- 05:15 - a timed bullet
\t- ## Recording and Prep
\t\t- ~~~
\t\t  - #### 09:00 Inside a code fence
\t\t  ~~~
'''


def live_set(locator_xml='<Locators />', tempo_events='<FloatEvent Id="1" Time="-63072000" Value="120" />'):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<Ableton MajorVersion="5" MinorVersion="11.0_11300" Creator="Ableton Live 11.3.43">
\t<LiveSet>
\t\t<MasterTrack>
\t\t\t<AutomationEnvelopes>
\t\t\t\t<Envelopes>
\t\t\t\t\t<AutomationEnvelope Id="0">
\t\t\t\t\t\t<EnvelopeTarget>
\t\t\t\t\t\t\t<PointeeId Value="8" />
\t\t\t\t\t\t</EnvelopeTarget>
\t\t\t\t\t\t<Automation>
\t\t\t\t\t\t\t<Events>
\t\t\t\t\t\t\t\t{tempo_events}
\t\t\t\t\t\t\t</Events>
\t\t\t\t\t\t</Automation>
\t\t\t\t\t</AutomationEnvelope>
\t\t\t\t</Envelopes>
\t\t\t</AutomationEnvelopes>
\t\t\t<DeviceChain>
\t\t\t\t<Mixer>
\t\t\t\t\t<Tempo>
\t\t\t\t\t\t<Manual Value="120" />
\t\t\t\t\t\t<AutomationTarget Id="8" />
\t\t\t\t\t</Tempo>
\t\t\t\t</Mixer>
\t\t\t</DeviceChain>
\t\t</MasterTrack>
\t\t<Locators>
\t\t\t{locator_xml}
\t\t\t<NextLocatorMapping>
\t\t\t\t<PersistentKeyString Value="k" />
\t\t\t</NextLocatorMapping>
\t\t</Locators>
\t</LiveSet>
</Ableton>
'''


HAND_LOCATOR = '''<Locators>
\t\t\t\t<Locator Id="7">
\t\t\t\t\t<LomId Value="0" />
\t\t\t\t\t<Time Value="2112" />
\t\t\t\t\t<Name Value="trippy denouement" />
\t\t\t\t\t<Annotation Value="line one&#x0A;line two" />
\t\t\t\t\t<IsSongStart Value="false" />
\t\t\t\t</Locator>
\t\t\t</Locators>'''


class AbletonLocatorTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)
        (self.root / 'garden/pages').mkdir(parents=True)
        self.page = self.root / 'garden/pages/GitP___A___Session___26___11___01-Sun.md'
        self.page.write_text(EPISODE)
        self.set = self.root / '26.11.01 Project/26.11.01.als'
        self.set.parent.mkdir()
        self.write(live_set(HAND_LOCATOR))

    def tearDown(self):
        self.directory.cleanup()

    def write(self, text):
        self.set.write_bytes(gzip.compress(text.encode('utf-8')))

    def read(self):
        return gzip.decompress(self.set.read_bytes()).decode('utf-8')

    def sync(self, **options):
        options.setdefault('now', datetime(2026, 11, 4, 5, 30, 0))
        return locators.sync(PAGE, self.root / 'garden', self.set, **options)

    def placed(self):
        live = locators.ET.fromstring(self.read()).find('LiveSet')
        return [(loc.fields['Time'], loc.fields['Name'], loc.fields['Annotation'])
                for loc in locators.existing_locators(live)]

    def test_timed_headings_become_named_chapters(self):
        found = [(c.seconds, c.label, c.name) for c in locators.chapters(EPISODE)]
        self.assertEqual(found, [
            (0, '00:00', 'Enter 259 Infini Pad / Launchpad playing infini pad'),
            (187, '03:07', 'Envelopes, Fold and Noise'),
            (1097, '18:17', 'Enter 8bitfi'),
            (1592, '26:32', 'Closing fade'),
        ])

    def test_timestamps_are_strict(self):
        for value, expected in [('0', 0), ('882', 882), ('14:42', 882), ('90:00', 5400), ('1:02:03', 3723)]:
            self.assertEqual(locators.seconds(value), expected)
        for value in ['', '1.5', '14:2', '1:60', '1:2:03']:
            with self.subTest(value=value), self.assertRaises(locators.SyncError):
                locators.seconds(value)

    def test_preview_leaves_the_set_unchanged(self):
        before = self.set.read_bytes()
        outcome = self.sync()
        self.assertTrue(outcome['changed'])
        self.assertIsNone(outcome['backup'])
        self.assertEqual(self.set.read_bytes(), before)

    def test_apply_places_chapters_at_tempo_and_keeps_hand_placed_locators(self):
        original = self.read()
        outcome = self.sync(apply=True)
        self.assertEqual(self.placed(), [
            ('0', 'Enter 259 Infini Pad / Launchpad playing infini pad', PAGE),
            ('374', 'Envelopes, Fold and Noise', PAGE),
            ('2112', 'trippy denouement', 'line one\nline two'),
            ('2194', 'Enter 8bitfi', PAGE),
            ('3184', 'Closing fade', PAGE),
        ])
        backup = self.set.parent / 'Backup/26.11.01 [2026-11-04 053000].als'
        self.assertEqual(outcome['backup'], backup)
        self.assertEqual(gzip.decompress(backup.read_bytes()).decode('utf-8'), original)
        text = self.read()
        prefix, suffix = original.split(HAND_LOCATOR)
        self.assertTrue(text.startswith(prefix) and text.endswith(suffix))
        self.assertIn('<Annotation Value="line one&#x0A;line two" />', text)

    def test_second_sync_changes_nothing(self):
        self.sync(apply=True)
        written = self.set.read_bytes()
        outcome = self.sync(apply=True, now=datetime(2026, 11, 4, 6, 0, 0))
        self.assertFalse(outcome['changed'])
        self.assertIsNone(outcome['backup'])
        self.assertEqual(self.set.read_bytes(), written)
        self.assertEqual(len(list((self.set.parent / 'Backup').iterdir())), 1)

    def test_resync_follows_edited_headings(self):
        self.sync(apply=True)
        self.page.write_text(EPISODE.replace('03:07 Envelopes, **Fold** and #Noise', '03:10 Fold sweeps'))
        outcome = self.sync(apply=True, now=datetime(2026, 11, 4, 6, 0, 0))
        actions = {(loc.action, loc.fields['Name']) for loc in outcome['locators']}
        self.assertIn(('remove', 'Envelopes, Fold and Noise'), actions)
        self.assertIn(('add', 'Fold sweeps'), actions)
        self.assertIn(('380', 'Fold sweeps', PAGE), self.placed())
        self.assertNotIn('Envelopes, Fold and Noise', [name for _, name, _ in self.placed()])

    def test_locator_at_a_chapter_time_takes_the_chapter_name(self):
        self.write(live_set(HAND_LOCATOR.replace('2112', '374')))
        outcome = self.sync(apply=True)
        updated = [loc for loc in outcome['locators'] if loc.action == 'update']
        self.assertEqual([(loc.id, loc.note) for loc in updated], [(7, '03:07; was "trippy denouement"')])
        self.assertIn(('374', 'Envelopes, Fold and Noise', PAGE), self.placed())

    def test_prune_removes_locators_without_chapters(self):
        self.sync(apply=True, prune=True)
        self.assertNotIn('trippy denouement', [name for _, name, _ in self.placed()])

    def test_start_beat_offsets_every_chapter(self):
        self.sync(apply=True, start_beat=16)
        self.assertEqual([time for time, _, annotation in self.placed() if annotation == PAGE],
                         ['16', '390', '2210', '3200'])

    def test_varying_tempo_automation_is_refused(self):
        self.write(live_set(tempo_events='<FloatEvent Id="1" Time="-63072000" Value="120" />'
                                         '<FloatEvent Id="2" Time="64" Value="90" />'))
        with self.assertRaisesRegex(locators.SyncError, 'automates its tempo'):
            self.sync()

    def test_page_without_timed_headings_is_refused(self):
        self.page.write_text('- # Episode\n\t- ## Chapters\n\t\t- ### Opening\n')
        with self.assertRaisesRegex(locators.SyncError, 'no timed chapter headings'):
            self.sync()

    def test_default_graph_is_the_graph_holding_the_task(self):
        self.assertTrue((locators.GRAPH / 'pages').is_dir())
        self.assertEqual(TASK.relative_to(locators.GRAPH).parts[0], 'mise-tasks')


if __name__ == '__main__':
    unittest.main()
