import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

LIB = Path(__file__).parent
sys.path.insert(0, str(LIB))
spec = importlib.util.spec_from_file_location('audition', LIB / 'audition.py')
audition = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audition)


class FakeMicroFreak:
    """One object stands in for both MIDI ports of the instrument."""

    def __init__(self, settings=None, frozen=()):
        self.settings = {0x2E: 1, 0x2B: 0, 0x25: 5, 0x20: 0, **(settings or {})}
        self.frozen = set(frozen)
        self.sent, self.pending, self.closed = [], [], 0

    def get_message(self):
        return (self.pending.pop(0), 0.0) if self.pending else None

    def send_message(self, message):
        self.sent.append(list(message))
        if message[:6] == audition.REQUEST_PREFIX and message[8] == 0x43:
            code = message[9]
            self.pending.append(audition.GLOBAL_PREFIX + [0x7F, 9, 2, 0x42, code,
                                                          self.settings[code], 0xF7])
        elif message[:6] == audition.REQUEST_PREFIX and message[8] == 0x42:
            if message[9] not in self.frozen:
                self.settings[message[9]] = message[10]
        elif message == [0xF8]:
            self.pending.append([0xF8])

    def ignore_types(self, **kwargs):
        pass

    def close_port(self):
        self.closed += 1


def args(*extra):
    return audition.build_parser().parse_args(['--slot', '35', '--no-audio', *extra])


PRESET = {'name': 'FM Seq', 'category': 'Sequence', 'data_sha256': '0' * 64, 'seq_length': 4,
          'gate_length': 41, 'arp_enable': 0, 'seq_on': 1, 'arp_div': 7, 'division': '1/16',
          'paraphonic': 0}


def fake_play(midi_in, midi_out, clocks, bpm, settle):
    events = [{'t': 0.0, 'host_clocks': 0, 'data': [0xFA]},
              {'t': 0.0, 'host_clocks': 0, 'data': [0x90, 36, 9]}]
    for tick in range(clocks):
        events.append({'t': 0.0, 'host_clocks': tick + 1, 'data': [0xF8]})
        if tick == 2:
            events.append({'t': 0.0, 'host_clocks': tick + 1, 'data': [0x80, 36, 64]})
    events.append({'t': 0.0, 'host_clocks': clocks, 'data': [0xFC]})
    return 0.0, events, [0.0] * clocks


class RunTests(unittest.TestCase):
    def run_with(self, device, play=fake_play, extra=()):
        with mock.patch.object(audition.download, 'open_ports', return_value=(device, device, 'Fake')), \
                mock.patch.object(audition.download, 'read_patch',
                                  return_value=({'name': 'FM Seq', 'category': 'Sequence'}, b'', b'')), \
                mock.patch.object(audition, 'preset_summary', return_value=dict(PRESET)), \
                mock.patch.object(audition, 'play', side_effect=play), \
                mock.patch.object(audition.time, 'sleep'):
            return audition.run(args(*extra))

    def test_selects_slot_enables_midi_out_and_restores_it(self):
        device = FakeMicroFreak()
        report = self.run_with(device)
        self.assertIn([0xB0, 0, 0], device.sent)
        self.assertIn([0xC0, 34], device.sent)
        self.assertEqual(device.settings[0x2B], 0)
        self.assertEqual(report['instrument']['globals_changed'],
                         [{'setting': 'midi.arp_seq_notes_out', 'value': 0,
                           'temporary_value': 1, 'restored': True}])
        self.assertEqual(report['tempo']['clocks_sent'], 4 * 6 * 2)
        self.assertEqual(report['steps'][0]['midi']['notes'][0]['note'], 36)
        self.assertEqual((report['midi_out']['notes'], report['midi_out']['note_messages']), (1, 2))
        stop = device.sent.index([0xFC])
        self.assertIn([0xC0, 34], device.sent[stop:])
        self.assertEqual(device.closed, 2)

    def test_internal_clock_source_is_switched_to_usb_and_back(self):
        device = FakeMicroFreak({0x2E: 0, 0x2B: 1})
        report = self.run_with(device)
        self.assertEqual(device.settings, {0x2E: 0, 0x2B: 1, 0x25: 5, 0x20: 0})
        self.assertEqual([c['setting'] for c in report['instrument']['globals_changed']], ['clock.source'])
        writes = [m[9:11] for m in device.sent if m[:6] == audition.REQUEST_PREFIX and m[8] == 0x42]
        self.assertEqual(writes, [[0x2E, 1], [0x2E, 0]])

    def test_failure_during_playback_still_stops_and_restores(self):
        device = FakeMicroFreak()

        def broken(*_):
            raise RuntimeError('port vanished')

        with self.assertRaises(RuntimeError):
            self.run_with(device, play=broken)
        self.assertEqual(device.settings[0x2B], 0)
        stop = device.sent.index([0xFC])
        self.assertIn([0xC0, 34], device.sent[stop:])

    def test_unchanged_readback_stops_before_selecting(self):
        device = FakeMicroFreak(frozen={0x2B})
        with self.assertRaises(audition.AuditionError):
            self.run_with(device)
        self.assertNotIn([0xC0, 34], device.sent[:device.sent.index([0xFC])])

    def test_failed_restore_is_reported_as_an_error(self):
        device = FakeMicroFreak({0x2E: 0})
        original = device.send_message

        def freeze_after_playback(message):
            if message == [0xFC]:
                device.frozen = {0x2E, 0x2B}
            original(message)

        device.send_message = freeze_after_playback
        with self.assertRaisesRegex(audition.AuditionError, 'clock.source .was 0.'):
            self.run_with(device)
        self.assertEqual(device.closed, 2)

    def test_plain_and_division_ccs_are_sent_and_reported(self):
        device = FakeMicroFreak()
        report = self.run_with(device, extra=('--plain', '--division', '1/8', '--cc', '23=100'))
        self.assertIn([0xB0, 9, 10], device.sent)
        self.assertIn([0xB0, 23, 100], device.sent)
        self.assertIn([0xB0, 92, 64], device.sent)
        self.assertEqual(report['tempo']['clocks_per_step'], 12)
        self.assertEqual(report['instrument']['ccs_sent'][-1], {'cc': 92, 'value': 64,
                                                                'label': 'ARP/SEQ rate (sync)'})


    def test_no_select_plays_what_is_loaded(self):
        device = FakeMicroFreak()
        report = self.run_with(device, extra=('--no-select',))
        self.assertFalse([m for m in device.sent if m[0] & 0xF0 == 0xC0 or m[:2] == [0xB0, 0]])
        self.assertFalse(report['instrument']['slot_reselected'])
        self.assertEqual(device.settings[0x2B], 0)
        with self.assertRaisesRegex(audition.AuditionError, 'leave out --plain'):
            self.run_with(FakeMicroFreak(), extra=('--no-select', '--plain'))


class HelperTests(unittest.TestCase):
    def test_select_slot_uses_bank_select_and_program_change(self):
        device = FakeMicroFreak()
        self.assertEqual(audition.select_slot(device, 1, 0), (0, 0))
        self.assertEqual(audition.select_slot(device, 512, 2), (3, 127))
        self.assertEqual(device.sent, [[0xB0, 0, 0], [0xC0, 0], [0xB2, 0, 3], [0xC2, 127]])

    def test_plan_globals(self):
        on = {0x2E: 1, 0x2B: 1, 0x25: 5}
        self.assertEqual(audition.plan_globals(on, True), [])
        self.assertEqual(audition.plan_globals({0x2E: 4, 0x2B: 0, 0x25: 1}, True), [(0x2B, 1)])
        self.assertEqual(audition.plan_globals({0x2E: 2, 0x2B: 0, 0x25: 4}, False), [(0x2E, 1)])
        self.assertEqual(audition.plan_globals({0x2E: 0, 0x2B: 0, 0x25: 0}, True),
                         [(0x2E, 1), (0x2B, 1), (0x25, 5)])

    def test_input_channel(self):
        self.assertEqual(audition.input_channel(127), 0)
        self.assertEqual(audition.input_channel(3), 3)
        with self.assertRaises(audition.AuditionError):
            audition.input_channel(126)

    def test_timing_comes_from_arp_div_or_flags(self):
        parser = audition.build_parser()
        base = parser.parse_args(['--slot', '1'])
        self.assertEqual(audition.choose_timing({'arp_div': 7}, base)[0], 6)
        self.assertEqual(audition.choose_timing({'arp_div': 5}, base)[0], 12)
        self.assertEqual(audition.choose_timing({'arp_div': None}, base)[0], 6)
        forced = parser.parse_args(['--slot', '1', '--division', '1/16T'])
        self.assertEqual(audition.choose_timing({'arp_div': 7}, forced)[:3:2], (4, 8))
        override = parser.parse_args(['--slot', '1', '--clocks-per-step', '3'])
        self.assertEqual(audition.choose_timing({'arp_div': 7}, override)[0], 3)

    def test_wav_dir_must_be_outside_the_repository(self):
        with self.assertRaises(audition.AuditionError):
            audition.guard_wav_dir(audition.REPO_ROOT / 'assets')
        with tempfile.TemporaryDirectory() as folder:
            self.assertEqual(audition.guard_wav_dir(Path(folder) / 'wav'),
                             (Path(folder) / 'wav').resolve())

    def test_play_sends_start_clocks_and_stop(self):
        device = FakeMicroFreak()
        start, events, clock_times = audition.play(device, device, 12, 300, 0.01)
        self.assertEqual(device.sent[0], [0xFA])
        self.assertEqual(device.sent[-1], [0xFC])
        self.assertEqual(device.sent.count([0xF8]), 12)
        self.assertEqual(len(clock_times), 12)
        self.assertEqual(sum(1 for e in events if e['data'] == [0xF8]), 12)
        self.assertEqual(events[-1]['host_clocks'], 12)


if __name__ == '__main__':
    unittest.main()
