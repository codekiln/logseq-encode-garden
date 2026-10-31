import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import refresh  # noqa: E402

PAGE = '''logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: {slot:03d}
preset-synth-microfreak-name:: {name}
preset-synth-microfreak-on-device:: true
{payload}- # Notes
'''


class RefreshTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        pages = Path(self.tmp.name) / 'pages'
        pages.mkdir()
        for slot, name, sha in ((1, 'One', 'aa'), (2, 'Two', None), (3, 'Three', 'cc')):
            payload = f'preset-synth-microfreak-parameter-payload-sha256:: {sha}\n' if sha else ''
            (pages / f'Microfreak___Preset___{slot:03d} {name}.md').write_text(
                PAGE.format(slot=slot, name=name, payload=payload))
        (pages / 'Microfreak___Preset___001 One___Asset___Device-Read-2026-10-25___bin.md').write_text('x')
        self.pages = refresh.page_index(self.tmp.name)

    def tearDown(self):
        self.tmp.cleanup()

    def read(self, name, sha):
        return {'name': name, 'category': 'Bass', 'payload_sha256': sha}

    def test_index_skips_asset_pages(self):
        self.assertEqual(sorted(self.pages), [1, 2, 3])
        self.assertEqual(self.pages[1]['page'], 'Microfreak/Preset/001 One')

    def test_classify(self):
        self.assertIsNone(refresh.classify(1, self.read('One', 'aa'), self.pages))
        self.assertEqual(refresh.classify(1, self.read('One', 'bb'), self.pages)['status'], 'changed')
        self.assertEqual(refresh.classify(1, self.read('Uno', 'aa'), self.pages)['status'], 'renamed')
        self.assertEqual(refresh.classify(2, self.read('Two', 'dd'), self.pages)['status'], 'not backed up')
        self.assertEqual(refresh.classify(9, self.read('Nine', 'ee'), self.pages)['status'], 'new')
        self.assertEqual(refresh.classify(3, None, self.pages)['status'], 'emptied')
        self.assertIsNone(refresh.classify(9, None, self.pages))

    def test_file_digest_matches_raw_read(self):
        self.pages[2]['file_sha256'] = 'raw'
        self.assertIsNone(refresh.classify(2, dict(self.read('Two', 'dd'), raw_sha256='raw'), self.pages))
        self.assertEqual(refresh.classify(2, dict(self.read('Two', 'dd'), raw_sha256='other'), self.pages)['status'],
                         'no payload digest')


class ReadOnlyTest(unittest.TestCase):
    def test_reads_use_only_download_requests(self):
        source = Path(refresh.__file__).read_text()
        self.assertNotIn('send_message', source)
        self.assertIn('download.read_patch', source)


if __name__ == '__main__':
    unittest.main()
