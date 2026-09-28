"""Synthetic fixtures only: no user or factory patch data."""
import contextlib
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

import parameters


def pack(data):
    data = data.ljust(4088, b'\xff')
    assert len(data) == 4088
    result = bytearray()
    for start in range(0, len(data), 7):
        block = data[start:start + 7]
        result.append(sum((v >> 7) << bit for bit, v in enumerate(block)))
        result.extend(v & 127 for v in block)
    return bytes(result)


def fixture(value=b'\x00\x34\x12'):
    return pack(b'#VCFFCutoffc' + value + b'@ ')


def mbp(payload=None, initialized=False):
    if payload is None:
        payload = b'' if initialized else fixture()
    envelope = ('22 serialization::archive 10 0 4 3 134 9 Test Tone '
                f'2 0 0 18 000000000000000000 {int(initialized)} 0 16 {len(payload)}')
    return (envelope + ''.join(f' {v}' for v in payload) + '\r\n').encode()


class ParameterTest(unittest.TestCase):
    def test_known_mask_bits_and_value_endianness(self):
        # A hand-authored transport block checks each high-bit position.
        raw = bytes([0x55, 1, 2, 3, 4, 5, 6, 7]) + bytes(4664)
        self.assertEqual(parameters.unpack_payload(raw)[:7], bytes([129, 2, 131, 4, 133, 6, 135]))
        parsed = parameters.parse_parameters(fixture(b'\xee\x34\xfe'))
        field = parsed['fields'][0]
        self.assertEqual(field['name'], 'VCF.Cutoff')
        self.assertEqual(field['control_label'], 'Filter Cutoff')
        self.assertEqual(field['descriptor'], 238)
        self.assertEqual(field['raw_hex'], 'ee34fe')
        self.assertEqual(field['value_le_unsigned'], 65076)
        self.assertEqual(field['value_le_signed'], -460)
        self.assertEqual(parsed['parameter_end_offset'], 17)

    def test_stops_at_root_and_preserves_unknown_tail(self):
        data = b'#VCFFCutoffc\0\0\0@ ' + b'unknown stale bytes'
        parsed = parameters.parse_parameters(pack(data))
        self.assertEqual(len(parsed['fields']), 1)
        self.assertEqual(parsed['uninterpreted_tail_size'], 4088 - 17)

    def test_rejects_unsupported_layouts_without_partial_fields(self):
        cases = [b'\xff', b'#VCFFCutoffb\0\0@ ',
                 b'#VCFFCutoffc\0\0\0FCutoffc\0\0\0@ ',
                 b'#VCFFCutoffc\0\0\0 ', b'#VCF@ ',
                 b'#VCFFCutoffc\0\0\0@', b'#VCFFCutoff\xc3\0\0\0@ ']
        for data in cases:
            with self.subTest(data=data), self.assertRaises(parameters.UnsupportedLayout):
                parameters.parse_parameters(pack(data))
        with self.assertRaises(parameters.UnsupportedLayout):
            parameters.parse_parameters(bytes(12))
        with self.assertRaises(parameters.UnsupportedLayout):
            parameters.parse_parameters(b'\x80' + bytes(4671))

    def test_archive_envelope_and_invalid_lengths(self):
        payload, metadata = parameters.parse_mbp(mbp())
        self.assertEqual(payload, fixture())
        self.assertEqual(metadata['name'], 'Test Tone')
        self.assertEqual(metadata['format_version'], '134')
        payload, metadata = parameters.parse_mbp(mbp(initialized=True))
        self.assertEqual(payload, b'')
        self.assertTrue(metadata['initialized'])
        for data in (mbp()[:-15], mbp() + b'extra', mbp().replace(b' 4672 ', b' 9999999999 ', 1),
                     mbp().replace(b' 4672 ', b' 4671 ', 1), mbp(payload=b'\xff' * 4672)):
            with self.subTest(data=data[:80]):
                if data == mbp(payload=b'\xff' * 4672):
                    payload, _ = parameters.parse_mbp(data)
                    with self.assertRaises(parameters.UnsupportedLayout):
                        parameters.parse_parameters(payload)
                else:
                    with self.assertRaises(ValueError):
                        parameters.parse_mbp(data)

    def test_binary_and_project_match_and_never_modify_input(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            binary = root / 'preset.bin'
            binary.write_bytes(bytes(35) + fixture())
            project = root / 'presets.mfprojz'
            with zipfile.ZipFile(project, 'w') as archive:
                archive.writestr('Example/01-Example-A1.mbp', mbp())
                archive.writestr('Example/02-Example-A2.mbp', mbp(initialized=True))
            before = {p: p.read_bytes() for p in (binary, project)}
            live = parameters.inspect(binary)
            exported = parameters.inspect(project, 1)
            self.assertEqual(live['fields'], exported['fields'])
            self.assertEqual(live['metadata']['payload_sha256'], hashlib.sha256(fixture()).hexdigest())
            self.assertEqual(exported['display_conversions'], 'unverified')
            self.assertEqual(exported['value_context'], 'saved_base_setting')
            self.assertEqual(parameters.inspect(project, 2)['status'], 'initialized')
            for slot in (None, 3, 0, 513):
                with self.assertRaises(ValueError):
                    parameters.inspect(project, slot)
            with self.assertRaises(ValueError):
                parameters.inspect(binary, 1)
            self.assertEqual(before, {p: p.read_bytes() for p in before})

    def test_ambiguous_project_slots_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory) / 'presets.mfprojz'
            with zipfile.ZipFile(project, 'w') as archive:
                archive.writestr('BankA/01-Example-A1.mbp', mbp())
                archive.writestr('BankB/01-Example-B1.mbp', mbp())
            with self.assertRaisesRegex(ValueError, 'exactly one'):
                parameters.inspect(project, 1)

    def test_cli_reports_unsupported_and_invalid_inputs(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'unknown.bin'
            path.write_bytes(pack(b'\x4a\xc2unsupported'))
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                code = parameters.main([str(path)])
            report = json.loads(output.getvalue())
            self.assertEqual(code, 2)
            self.assertEqual(report['status'], 'unsupported_layout')
            self.assertNotIn('fields', report)
            self.assertIn('record_sha256', report['metadata'])
            path.write_bytes(b'truncated')
            with contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(parameters.main([str(path)]), 2)
            self.assertEqual(json.loads(output.getvalue())['status'], 'invalid_input')


if __name__ == '__main__':
    unittest.main()
