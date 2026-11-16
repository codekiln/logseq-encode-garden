import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

LIB = Path(__file__).parent
sys.path.insert(0, str(LIB))
spec = importlib.util.spec_from_file_location('upload', LIB / 'upload.py')
upload = importlib.util.module_from_spec(spec)
spec.loader.exec_module(upload)
download = upload.sys.modules['download']

HEADER_LEN, PARTS, PART_LEN = download.HEADER_LEN, download.PARTS, download.PART_LEN


def saved_header(slot, name, category=7, initialized=False):
    """A header shaped like the ones the MicroFreak returns."""
    bank, program = download.slot_address(slot)
    header = [0] * HEADER_LEN
    header[0], header[1], header[8], header[9] = bank, program, program, (slot - 1) // 256
    header[3] = 8 if initialized else 0
    header[10], header[11] = category, 0x10
    header[12:26] = list(name.encode('ascii').ljust(14, b'\0'))
    return header


def synthetic_data(seed):
    return bytes((seed + index * 7) % 128 for index in range(PARTS * PART_LEN))


class FakeMidiIn:
    def __init__(self):
        self.pending = []

    def get_message(self):
        return (self.pending.pop(0), 0) if self.pending else None


class FakeMicroFreak:
    """Answers the header, read and write requests the way the instrument did on 2026-11-16."""

    def __init__(self, midi_in, slots, *, bad_ack_at=None):
        self.midi_in = midi_in
        self.slots = slots
        self.bad_ack_at = bad_ack_at
        self.requests = []
        self.reading = None
        self.staged = None

    def reply(self, sequence, op, payload=()):
        self.midi_in.pending.append(download.PREFIX + [sequence, len(payload), op]
                                    + list(payload) + [0xF7])

    def send_message(self, message):
        self.requests.append(message)
        sequence, op, payload = message[6], message[8], message[9:-1]
        if op == 0x19:
            slot = payload[0] * 128 + payload[1] + 1
            if payload[2] == 0:
                header, _ = self.slots[slot]
                self.reply(sequence, 0x52, header)
            else:
                self.reading = (slot, 0)
                self.reply(sequence, 0x15)
        elif op == 0x18:
            slot, part = self.reading
            data = self.slots[slot][1]
            self.reading = (slot, part + 1)
            self.reply(sequence, 0x17 if part == PARTS - 1 else 0x16,
                       data[part * PART_LEN:(part + 1) * PART_LEN])
        else:
            if self.bad_ack_at == len(self.requests):
                self.reply(sequence, 0x7F)
                return
            if op == 0x52 and len(payload) == HEADER_LEN:
                self.staged = [list(payload), b'']
            elif op == 0x52:
                self.staged.append(payload[0] * 128 + payload[1] + 1)
            elif op in (0x16, 0x17):
                self.staged[1] += bytes(payload)
                if op == 0x17:
                    header, data, slot = self.staged
                    header[9] = (slot - 1) // 256
                    self.slots[slot] = (header, data)
            self.reply(sequence, 0x18)

    def writes(self):
        return [r for r in self.requests if r[8] not in (0x18, 0x19)]


def fake(slots, **kwargs):
    midi_in = FakeMidiIn()
    return midi_in, FakeMicroFreak(midi_in, slots, **kwargs)


class LoadPatchTest(unittest.TestCase):
    def write(self, folder, raw):
        path = Path(folder) / 'slot-005.bin'
        path.write_bytes(bytes(raw))
        return path

    def test_reads_a_download_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            raw = bytes(saved_header(5, 'TestSeq')) + synthetic_data(1)
            header, data = upload.load_patch(self.write(tmp, raw))
        self.assertEqual(header + data, raw)

    def test_rejects_files_upload_cannot_send(self):
        good = saved_header(5, 'TestSeq')
        cases = {
            'bytes long': bytes(good) + synthetic_data(1)[:-1],
            'above 0x7F': bytes(good) + b'\x80' + synthetic_data(1)[1:],
            'initialized': bytes(saved_header(5, 'Init', initialized=True)) + synthetic_data(1),
            'category': bytes(saved_header(5, 'TestSeq', category=12)) + synthetic_data(1),
            'Preset names': bytes(saved_header(5, ' Spaced')) + synthetic_data(1),
        }
        for message, raw in cases.items():
            with self.subTest(message), tempfile.TemporaryDirectory() as tmp:
                with self.assertRaisesRegex(ValueError, message):
                    upload.load_patch(self.write(tmp, raw))


class BuildHeaderTest(unittest.TestCase):
    def test_keeps_name_category_and_flags_for_the_target_slot(self):
        source = bytes(saved_header(5, 'TestSeq'))
        source = source[:4] + b'\x11' + source[5:]
        header = upload.build_header(source, 321)
        expected = saved_header(321, 'TestSeq')
        self.assertEqual(header, expected)

    def test_name_and_category_override(self):
        header = upload.build_header(bytes(saved_header(5, 'TestSeq')), 1,
                                     name='New Name 12345', category='Keys')
        self.assertEqual(bytes(header[12:26]), b'New Name 12345')
        self.assertEqual(header[10], 2)
        self.assertEqual(header[:2] + header[8:10], [0, 0, 0, 0])

    def test_rejects_names_the_instrument_cannot_store(self):
        source = bytes(saved_header(5, 'TestSeq'))
        for name in ['', 'Fifteen chars!!', 'Tab\tname', ' lead', 'Ümlaut']:
            with self.subTest(name), self.assertRaisesRegex(ValueError, 'Preset names'):
                upload.build_header(source, 321, name=name)


class UploadTest(unittest.TestCase):
    def setUp(self):
        patcher = mock.patch.object(upload.time, 'sleep')
        patcher.start()
        self.addCleanup(patcher.stop)
        self.data = synthetic_data(3)
        self.header = upload.build_header(bytes(saved_header(5, 'TestSeq')), 321)

    def test_writes_an_initialized_slot_and_reads_it_back(self):
        midi_in, device = fake({321: (saved_header(321, 'Init', 0, True), b'')})
        result = upload.upload(midi_in, device, 321, self.header, self.data)
        self.assertEqual(device.slots[321], (self.header, self.data))
        self.assertEqual(result['after']['name'], 'TestSeq')
        self.assertNotIn('backup', result)
        writes = device.writes()
        self.assertEqual(len(writes), 3 + PARTS)
        self.assertEqual(writes[0][7:9], [HEADER_LEN, 0x52])
        self.assertEqual(writes[1][7:-1], [3, 0x52, 2, 64, 1])
        self.assertEqual(writes[2][7:-1], [0, 0x15])
        self.assertEqual([w[8] for w in writes[3:]], [0x16] * (PARTS - 1) + [0x17])
        self.assertEqual({w[7] for w in writes[3:]}, {PART_LEN})

    def test_refuses_a_populated_slot_without_a_backup_dir(self):
        old = (saved_header(321, 'Keep Me', 2), synthetic_data(9))
        midi_in, device = fake({321: old})
        with self.assertRaisesRegex(ValueError, 'holds Keep Me .Keys.; pass --backup-dir'):
            upload.upload(midi_in, device, 321, self.header, self.data)
        self.assertEqual(device.writes(), [])
        self.assertEqual(device.slots[321], old)

    def test_saves_a_populated_slot_before_writing(self):
        old = (saved_header(321, 'Keep Me', 2), synthetic_data(9))
        midi_in, device = fake({321: old})
        with tempfile.TemporaryDirectory() as tmp:
            result = upload.upload(midi_in, device, 321, self.header, self.data,
                                   backup_dir=tmp, device='Test MicroFreak')
            self.assertEqual(result['backup'].read_bytes(), bytes(old[0]) + old[1])
        self.assertEqual(device.slots[321], (self.header, self.data))

    def test_existing_backup_stops_before_writing(self):
        old = (saved_header(321, 'Keep Me', 2), synthetic_data(9))
        midi_in, device = fake({321: old})
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / 'slot-321.bin').write_bytes(b'earlier backup')
            with self.assertRaises(FileExistsError):
                upload.upload(midi_in, device, 321, self.header, self.data, backup_dir=tmp)
        self.assertEqual(device.writes(), [])

    def test_unexpected_acknowledgement_stops_the_transfer(self):
        midi_in, device = fake({321: (saved_header(321, 'Init', 0, True), b'')}, bad_ack_at=5)
        with self.assertRaisesRegex(ValueError, 'Unexpected response'):
            upload.upload(midi_in, device, 321, self.header, self.data)
        self.assertEqual(len(device.writes()), 4)

    def test_readback_mismatch_is_an_error(self):
        midi_in, device = fake({321: (saved_header(321, 'Init', 0, True), b'')})
        original = device.send_message

        def corrupt(message):
            # The header, the store request and 0x15 come first; corrupt data packet 7.
            if message[8] == 0x16 and len(device.writes()) == 3 + 6:
                message = message[:9] + [(message[9] + 1) % 128] + message[10:]
            original(message)
        device.send_message = corrupt
        with self.assertRaisesRegex(ValueError, 'differs from the file from packet 7 of 146'):
            upload.upload(midi_in, device, 321, self.header, self.data)


if __name__ == '__main__':
    unittest.main()
