"""Exercise the public inspector with synthetic saved presets only."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
import zipfile

import parameters
from test_parameters import mbp, pack

TASK = Path(__file__).resolve().parents[1] / 'inspect'


def synthetic_payload():
    def field(name, descriptor, value):
        return bytes([0x40 | len(name)]) + name.encode() + b'c' + bytes([descriptor]) + value.to_bytes(2, 'little')
    return pack(b'#VCO' + field('Type', 22, 2979) + field('Param1', 3, 10922)
                + field('Param2', 238, 2500) + field('Param3', 238, 5119) + b'@'
                + b'#VCF' + field('Cutoff', 238, 16384) + b'@'
                + b'!X' + field('Unknown', 238, 45000) + b'@ ')


class InspectorCliTests(unittest.TestCase):
    def run_task(self, file, *args, usage=False):
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
        for key in ('usage_file', 'usage_slot', 'usage_interpret_fw5'):
            env.pop(key, None)
        if usage:
            env['usage_file'] = str(file)
            env['usage_interpret_fw5'] = 'true' if '--interpret-fw5' in args else 'false'
            if '--slot' in args:
                env['usage_slot'] = args[args.index('--slot') + 1]
            command = ['bash', str(TASK)]
        else:
            command = ['bash', str(TASK), str(file), *args]
        result = subprocess.run(command, env=env, text=True, capture_output=True)
        self.assertEqual(result.stderr, '')
        return result.returncode, json.loads(result.stdout)

    def test_option_reaches_helper_and_preserves_entire_raw_report(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / 'synthetic.bin'
            original = bytes(35) + synthetic_payload()
            file.write_bytes(original)
            code, raw = self.run_task(file)
            self.assertEqual(code, 0)
            self.assertEqual(raw, parameters.inspect(file))
            self.assertNotIn('interpretations', raw)
            self.assertEqual(self.run_task(file, usage=True), (code, raw))
            for usage in (False, True):
                with self.subTest(usage=usage):
                    code, interpreted = self.run_task(file, '--interpret-fw5', usage=usage)
                    self.assertEqual(code, 0)
                    extra = interpreted.pop('interpretations')
                    self.assertEqual(interpreted, raw)
                    self.assertEqual(extra['firmware_assumption'], '5')
                    self.assertFalse(extra['firmware_detected_from_export'])
                    self.assertEqual(extra['oscillator']['model'], 'SuperWave')
                    values = {item['name']: item for item in extra['fields']}
                    self.assertEqual([values[f'VCO.Param{i}']['label'] for i in (1, 2, 3)],
                                     ['Wave', 'Detune', 'Volume'])
                    self.assertEqual(values['VCF.Cutoff']['kind'], 'normalized_0_1')
                    self.assertEqual(values['X.Unknown']['kind'], 'raw_only')
                    self.assertEqual(values['X.Unknown']['value'], 45000)
                    for field in extra['fields']:
                        for evidence in field['evidence']:
                            self.assertTrue(extra['evidence_sources'][evidence].startswith('https://'))
                    self.assertEqual(interpreted['display_conversions'], 'unverified')
            self.assertEqual(file.read_bytes(), original)

    def test_option_and_project_slot_work_through_mise_usage_arguments(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory) / 'synthetic.mfprojz'
            with zipfile.ZipFile(project, 'w') as archive:
                archive.writestr('02-Synthetic-A2.mbp', mbp(synthetic_payload()))
                archive.writestr('03-Initialized-A3.mbp', mbp(initialized=True))
            original = project.read_bytes()
            code, report = self.run_task(project, '--slot', '2', '--interpret-fw5', usage=True)
            self.assertEqual(code, 0)
            self.assertEqual(report['metadata']['project_slot'], 2)
            self.assertEqual(report['interpretations']['oscillator']['model'], 'SuperWave')
            code, initialized = self.run_task(project, '--slot', '3', '--interpret-fw5', usage=True)
            self.assertEqual(code, 0)
            self.assertEqual(initialized, parameters.inspect(project, 3))
            self.assertNotIn('interpretations', initialized)
            self.assertEqual(project.read_bytes(), original)

    def test_unknown_type_and_missing_type_do_not_gain_model_names(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / 'unknown.bin'
            for value in (b'#VCODTypec\x16\x50\xc3FParam1c\xee\0\0@ ',
                          b'#VCOFParam1c\xee\0\0@ '):
                with self.subTest(value=value):
                    file.write_bytes(pack(value))
                    code, report = self.run_task(file, '--interpret-fw5')
                    self.assertEqual(code, 0)
                    self.assertIsNone(report['interpretations']['oscillator'])
                    fields = {item['name']: item for item in report['interpretations']['fields']}
                    self.assertEqual(fields['VCO.Param1']['label'], 'VCO.Param1')
                    if 'VCO.Type' in fields:
                        self.assertEqual(fields['VCO.Type']['kind'], 'raw_only')

    def test_unsupported_and_invalid_inputs_keep_raw_failure_behavior(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / 'unsupported.bin'
            for original, status in ((pack(b'\xff'), 'unsupported_layout'), (b'invalid', 'invalid_input')):
                with self.subTest(status=status):
                    file.write_bytes(original)
                    raw_code, raw = self.run_task(file)
                    code, report = self.run_task(file, '--interpret-fw5')
                    self.assertEqual((code, report), (raw_code, raw))
                    self.assertEqual(code, 2)
                    self.assertEqual(report['status'], status)
                    self.assertNotIn('interpretations', report)
                    self.assertNotIn('fields', report)
                    self.assertEqual(file.read_bytes(), original)


if __name__ == '__main__':
    unittest.main()
