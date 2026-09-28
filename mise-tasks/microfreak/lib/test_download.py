import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('download', Path(__file__).with_name('download.py'))
download = importlib.util.module_from_spec(spec)
spec.loader.exec_module(download)


class FakeMidiIn:
    def __init__(self):
        self.pending = []

    def get_message(self):
        return (self.pending.pop(0), 0) if self.pending else None


class FakeMidiOut:
    def __init__(self, midi_in, *, initialized=False, wrong_final_op=False):
        self.midi_in = midi_in
        self.initialized = initialized
        self.wrong_final_op = wrong_final_op
        self.requests = []

    def send_message(self, message):
        self.requests.append(message)
        sequence = message[6]
        if len(self.requests) == 1:
            header = [0] * download.HEADER_LEN
            header[3] = 8 if self.initialized else 0
            header[10] = 2  # Keys
            header[12:19] = b'TestKey'
            op, payload = 0x52, header
        elif len(self.requests) == 2:
            op, payload = 0x15, []
        else:
            part = len(self.requests) - 3
            op = 0x17 if part == download.PARTS - 1 and not self.wrong_final_op else 0x16
            payload = [part % 128] * download.PART_LEN
        self.midi_in.pending.append(download.PREFIX + [sequence, len(payload), op]
                                    + list(payload) + [0xF7])


class DownloadTest(unittest.TestCase):
    def test_reads_every_part_and_saves_exact_bytes(self):
        midi_in = FakeMidiIn()
        midi_out = FakeMidiOut(midi_in)
        metadata, header, data = download.read_patch(midi_in, midi_out, 1)
        self.assertEqual(metadata['name'], 'TestKey')
        self.assertEqual(len(header), download.HEADER_LEN)
        self.assertEqual(len(data), download.PARTS * download.PART_LEN)
        self.assertEqual(data[:32], bytes(32))
        self.assertEqual(data[-32:], bytes([145 % 128]) * 32)
        self.assertEqual(len(midi_out.requests), download.PARTS + 2)
        self.assertEqual(midi_out.requests[1][8:12], [0x19, 0, 0, 1])
        self.assertEqual(midi_out.requests[-1][8:11], [0x18, 0, 0xF7])
        with tempfile.TemporaryDirectory() as tmp:
            raw_path, manifest_path, manifest = download.save_patch(
                Path(tmp), metadata, header, data, 'Test MicroFreak')
            self.assertEqual(raw_path.read_bytes(), header + data)
            self.assertEqual(json.loads(manifest_path.read_text()), manifest)
            self.assertEqual(manifest['raw_bytes'], 4707)
            with self.assertRaises(FileExistsError):
                download.save_patch(Path(tmp), metadata, header, data, 'Test MicroFreak')

    def test_initialized_slot_stops_after_header(self):
        midi_in = FakeMidiIn()
        midi_out = FakeMidiOut(midi_in, initialized=True)
        with self.assertRaisesRegex(ValueError, 'initialized'):
            download.read_patch(midi_in, midi_out, 1)
        self.assertEqual(len(midi_out.requests), 1)

    def test_wrong_final_packet_is_rejected(self):
        midi_in = FakeMidiIn()
        midi_out = FakeMidiOut(midi_in, wrong_final_op=True)
        with self.assertRaisesRegex(ValueError, 'Unexpected response'):
            download.read_patch(midi_in, midi_out, 1)


if __name__ == '__main__':
    unittest.main()
