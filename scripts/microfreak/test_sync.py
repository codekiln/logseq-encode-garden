import copy
import importlib.util
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('sync', Path(__file__).with_name('sync.py'))
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


def inventory():
    return {'schema': 1, 'presets': [dict(number=i, name=f'Preset {i}', category='Keys', initialized=False)
                                      for i in range(1, 513)]}


class SyncTest(unittest.TestCase):
    def test_reject_partial_duplicate_and_invalid_inventory(self):
        for mutate in [lambda d: d['presets'].pop(),
                       lambda d: d['presets'].__setitem__(0, d['presets'][1]),
                       lambda d: d['presets'][0].update(name='../escape'),
                       lambda d: d['presets'][0].update(initialized='false')]:
            data = inventory()
            mutate(data)
            with self.assertRaises(ValueError):
                sync.validate(data)

    def test_metadata_preserves_notes_tags_origin_and_retires_rename(self):
        with tempfile.TemporaryDirectory() as tmp:
            garden = Path(tmp)
            (garden / 'pages').mkdir()
            data = inventory()
            changes = sync.plan(garden, data)
            sync.apply(garden, changes)
            self.assertEqual(sync.plan(garden, data), [])
            path = garden / 'pages/Microfreak___Preset___1 Preset 1.md'
            self.assertIn('- # Preset 1\n\t- Saved [[Microfreak]] preset in slot 1.', path.read_text())
            text = path.read_text().replace('preset-origin:: unknown', 'preset-origin:: custom')
            text = 'tags:: [[Mine]]\n' + text + '- My performance notes\n\tid:: 123\n'
            path.write_text(text)
            data['presets'][0]['category'] = 'Bass'
            sync.apply(garden, sync.plan(garden, data))
            self.assertIn('tags:: [[Mine]]\n', path.read_text())
            self.assertIn('preset-origin:: custom', path.read_text())
            self.assertIn('- My performance notes\n\tid:: 123\n', path.read_text())
            data['presets'][0]['name'] = 'Renamed'
            sync.apply(garden, sync.plan(garden, data))
            self.assertIn('preset-on-device:: false', path.read_text())
            self.assertEqual(sync.plan(garden, data), [])
            data['presets'][0]['initialized'] = True
            sync.apply(garden, sync.plan(garden, data))
            renamed = garden / 'pages/Microfreak___Preset___1 Renamed.md'
            self.assertIn('preset-on-device:: false', renamed.read_text())
            self.assertEqual(sync.plan(garden, data), [])
            journal = next((garden / 'journals').glob('*.md')).read_text()
            self.assertEqual(journal.count('[[Microfreak/Preset]]'), 1)

    def test_journal_preserves_narrative_and_is_idempotent(self):
        old = '- My own note\n- # [[Filed]]\n\t- [[Other]]\n- # [[Updated]]\n\t- Zoo\n\t\t- [[Animal]]\n'
        changes = [(Path('x'), None, 'new')]
        updated = sync.journal_text(old, changes)
        self.assertTrue(updated.startswith(old))
        self.assertEqual(updated.count('[[Microfreak/Preset]]'), 1)
        self.assertEqual(sync.journal_text(updated, changes), updated)
        self.assertEqual(sync.journal_text(old, []), old)

    def test_unmanaged_collision_fails_before_writes(self):
        with tempfile.TemporaryDirectory() as tmp:
            garden = Path(tmp)
            (garden / 'pages').mkdir()
            path = garden / 'pages/Microfreak___Preset___1 Preset 1.md'
            path.write_text('- Existing notes\n')
            with self.assertRaises(ValueError):
                sync.plan(garden, inventory())
            self.assertEqual(path.read_text(), '- Existing notes\n')

    def test_response_slot_and_sequence_validation(self):
        header = [3, 12, 0, 16, 0, 0, 0, 0, 12, 1, 2, 51] + list(b'Imit') + [0] * 19
        message = sync.PREFIX + [0, 35, 82] + header + [247]
        self.assertEqual(sync.decode_header(message, 397, 0),
                         dict(number=397, name='Imit', category='Keys', initialized=False))
        with self.assertRaises(ValueError):
            sync.decode_header(message, 396, 0)
        with self.assertRaises(ValueError):
            sync.decode_header(message, 397, 1)


if __name__ == '__main__':
    unittest.main()
