"""Synthetic comparisons; no personal or factory presets are stored here."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

import compare


def pack(data):
    data = data.ljust(4088, b'\xff')
    result = bytearray()
    for offset in range(0, len(data), 7):
        block = data[offset:offset + 7]
        result.append(sum((value >> 7) << bit for bit, value in enumerate(block)))
        result.extend(value & 127 for value in block)
    return bytes(result)


def preset(fields, tail=b''):
    records = b'#VCF'
    for name, value in fields:
        encoded = name.encode('ascii')
        records += bytes([0x40 + len(encoded)]) + encoded + b'c' + value
    return pack(records + b'@ ' + tail)


def mbp(payload):
    envelope = ('22 serialization::archive 10 0 4 3 134 9 Test Tone '
                f'2 0 0 18 000000000000000000 0 0 16 {len(payload)}')
    return (envelope + ''.join(f' {value}' for value in payload) + '\r\n').encode()


class CompareTest(unittest.TestCase):
    def test_changed_added_removed_and_tail_are_separate_observations(self):
        with tempfile.TemporaryDirectory() as directory:
            a, b = Path(directory) / 'a.bin', Path(directory) / 'b.bin'
            a.write_bytes(preset([('Cutoff', b'\x00\x34\x12'), ('Reso', b'\x00\x01\x00')]))
            b.write_bytes(preset([('Cutoff', b'\x00\xfe\xff'), ('Drive', b'\x00\x02\x00')], b'new tail'))
            original = a.read_bytes(), b.read_bytes()
            result = compare.compare(a, b)
            self.assertEqual(result['status'], 'compared')
            self.assertEqual([entry['name'] for entry in result['changed_fields']], ['VCF.Cutoff'])
            self.assertEqual(result['changed_fields'][0]['before']['raw_hex'], '003412')
            self.assertEqual(result['changed_fields'][0]['after']['value_le_signed'], -2)
            self.assertEqual([entry['name'] for entry in result['added_fields']], ['VCF.Drive'])
            self.assertEqual([entry['name'] for entry in result['removed_fields']], ['VCF.Reso'])
            self.assertTrue(result['uninterpreted_tail_changed'])
            self.assertGreater(result['changed_payload_byte_count'], 0)
            self.assertEqual((a.read_bytes(), b.read_bytes()), original)

    def test_same_payload_in_different_envelopes(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            payload = preset([('Cutoff', b'\x00\x01\x00')])
            binary = root / 'preset.bin'
            zipped = root / 'preset.mfpz'
            binary.write_bytes(payload)
            with zipfile.ZipFile(zipped, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
                archive.writestr('0_Test Tone', mbp(payload))
            result = compare.compare(binary, zipped)
            self.assertEqual(result['changed_payload_byte_count'], 0)
            self.assertEqual(result['changed_fields'], [])
            self.assertFalse(result['uninterpreted_tail_changed'])
            self.assertEqual(result['a']['payload_sha256'], result['b']['payload_sha256'])
            self.assertNotEqual(result['a']['record_sha256'], result['b']['record_sha256'])

    def test_unsupported_layout_has_no_partial_field_diff(self):
        with tempfile.TemporaryDirectory() as directory:
            a, b = Path(directory) / 'a.bin', Path(directory) / 'b.bin'
            a.write_bytes(preset([('Cutoff', b'\x00\x01\x00')]))
            b.write_bytes(pack(b'\xffunsupported'))
            result = compare.compare(a, b)
            self.assertEqual(result['status'], 'unsupported_layout')
            self.assertEqual(result['b']['status'], 'unsupported_layout')
            self.assertEqual(result['changed_fields'], [])
            self.assertIsNone(result['uninterpreted_tail_changed'])
            self.assertGreater(result['changed_payload_byte_count'], 0)

    def test_cli_is_deterministic_and_reports_invalid_input(self):
        with tempfile.TemporaryDirectory() as directory:
            a, b = Path(directory) / 'a.bin', Path(directory) / 'b.bin'
            a.write_bytes(preset([('Cutoff', b'\x00\x01\x00')]))
            b.write_bytes(preset([('Cutoff', b'\x00\x02\x00')]))
            outputs = []
            for _ in range(2):
                with contextlib.redirect_stdout(io.StringIO()) as output:
                    self.assertEqual(compare.main([str(a), str(b)]), 0)
                outputs.append(output.getvalue())
            self.assertEqual(*outputs)
            self.assertEqual(json.loads(outputs[0])['changed_fields'][0]['name'], 'VCF.Cutoff')
            b.write_bytes(b'truncated')
            with contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(compare.main([str(a), str(b)]), 2)
            self.assertEqual(json.loads(output.getvalue())['status'], 'invalid_input')


if __name__ == '__main__':
    unittest.main()
