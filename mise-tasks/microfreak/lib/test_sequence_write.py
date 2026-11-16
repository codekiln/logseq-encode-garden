"""Synthetic presets and a fake instrument only: no user or factory patch data."""
import contextlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest import mock

import sequence as Q
import sequence_write as W
from test_sequence import synthetic
from test_upload import fake, saved_header, upload

TASK = Path(__file__).resolve().parents[1] / 'write-sequence'
DESCRIPTION = {'name': 'Seq Test', 'length': 4,
               'patterns': {'A': {'steps': [{'notes': ['C4', 'G4']}, {}, {'notes': ['D4']}]}}}


def run(argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = W.main([str(a) for a in argv])
    return code, out.getvalue(), err.getvalue()


class FileTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.dir = Path(self.tmp.name)
        self.base = self.dir / 'slot-005.bin'
        self.base.write_bytes(bytes(saved_header(5, 'Base Seq')) + synthetic(switches=(0, 0)))
        self.spec = self.dir / 'seq.json'
        self.spec.write_text(json.dumps(DESCRIPTION))

    def test_writes_a_new_file_and_prints_the_decoded_result(self):
        out = self.dir / 'new.bin'
        code, text, _ = run([self.spec, '--base', self.base, '--output', out])
        self.assertEqual(code, 0)
        report = json.loads(text)
        self.assertEqual(report['differences'], [])
        self.assertEqual(report['settings_changed'],
                         {'Arp.SeqOn': [0, 32767], 'Gen.Parafon': [0, 32767]})
        self.assertEqual(report['kept_from_base'], ['B'])
        self.assertEqual(report['sequence']['patterns']['A']['steps'][0],
                         {'notes': ['C4', 'G4'], 'velocity': 100})
        raw = out.read_bytes()
        base = self.base.read_bytes()
        self.assertEqual(raw[:10] + raw[11:12] + raw[26:35], base[:10] + base[11:12] + base[26:35])
        self.assertEqual(upload.preset_name(raw[:35]), 'Seq Test')
        self.assertEqual(Q.decode_sequence(raw[35:])['patterns']['A']['steps'][2]['notes'], [62])

    def test_name_and_category_flags_override_the_description(self):
        out = self.dir / 'new.bin'
        code, text, _ = run([self.spec, '--base', self.base, '--output', out,
                             '--name', 'Other', '--category', 'Keys'])
        self.assertEqual(code, 0)
        header = out.read_bytes()[:35]
        self.assertEqual((upload.preset_name(header), header[10]), ('Other', 2))
        self.assertEqual(json.loads(text)['category'], 'Keys')

    def test_refuses_to_overwrite_a_file(self):
        out = self.dir / 'new.bin'
        out.write_bytes(b'keep')
        code, _, err = run([self.spec, '--base', self.base, '--output', out])
        self.assertEqual((code, out.read_bytes()), (1, b'keep'))
        self.assertIn('already exists', err)

    def test_reports_values_the_instrument_cannot_hold(self):
        self.spec.write_text(json.dumps({'length': 4, 'patterns': {'A': {'steps': [
            {'notes': ['C4'], 'velocity': 0}]}}}))
        code, _, err = run([self.spec, '--base', self.base])
        self.assertEqual(code, 1)
        self.assertIn('velocity', err)

    @unittest.skipUnless(shutil.which('uv'), 'the task runs through uv')
    def test_task_passes_its_arguments(self):
        out = self.dir / 'task.bin'
        env = {k: v for k, v in os.environ.items() if not k.startswith('usage_')}
        result = subprocess.run(['bash', str(TASK), str(self.spec), '--base', str(self.base),
                                 '--output', str(out)], env=env, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['differences'], [])


class SlotTests(unittest.TestCase):
    def setUp(self):
        patcher = mock.patch.object(upload.time, 'sleep')
        patcher.start()
        self.addCleanup(patcher.stop)
        base = (saved_header(382, 'Base Seq', 7), synthetic(switches=(32767, 32767)))
        self.midi_in, self.device = fake({382: base,
                                          431: (saved_header(431, 'Init', 0, True), b''),
                                          432: (saved_header(432, 'Keep Me', 2), synthetic())})
        ports = mock.patch('download.open_ports',
                           return_value=(self.midi_in, self.device, 'Fake MicroFreak'))
        ports.start()
        self.addCleanup(ports.stop)
        self.midi_in.close_port = self.device.close_port = lambda: None

    def test_reads_the_base_slot_and_writes_an_initialized_slot(self):
        report = W.write(DESCRIPTION, '382', slot=431)
        header, data = self.device.slots[431]
        self.assertEqual(upload.preset_name(header), 'Seq Test')
        self.assertEqual(report['base'], {'slot': 382, 'name': 'Base Seq'})
        self.assertEqual(report['upload']['was'], None)
        self.assertTrue(report['upload']['read_back_matches'])
        self.assertEqual(Q.differences(DESCRIPTION, Q.decode_sequence(data)), [])
        self.assertEqual(self.device.slots[382][1], synthetic(switches=(32767, 32767)))

    def test_refuses_a_populated_slot_without_a_backup(self):
        with self.assertRaisesRegex(ValueError, 'pass --backup-dir'):
            W.write(DESCRIPTION, '382', slot=432)
        self.assertEqual(upload.preset_name(self.device.slots[432][0]), 'Keep Me')

    def test_backs_up_a_populated_slot_first(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = W.write(DESCRIPTION, '382', slot=432, backup_dir=Path(tmp))
            self.assertTrue(Path(report['upload']['backup']).exists())
        self.assertEqual(report['upload']['was'], 'Keep Me (Keys)')


class DumpsTests(unittest.TestCase):
    def test_short_values_stay_on_one_line(self):
        text = W.dumps({'steps': [{'notes': ['C4'], 'velocity': 100}, {}], 'long': list(range(40))})
        self.assertEqual(json.loads(text), {'steps': [{'notes': ['C4'], 'velocity': 100}, {}],
                                            'long': list(range(40))})
        self.assertIn('"steps": [{"notes": ["C4"], "velocity": 100}, {}]', text)


if __name__ == '__main__':
    unittest.main()
