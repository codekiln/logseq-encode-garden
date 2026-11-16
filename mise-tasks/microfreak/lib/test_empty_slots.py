"""Fake header reads only: no instrument needed."""
import contextlib
import io
import json
import unittest
from unittest import mock

import empty_slots as E


class RangesTests(unittest.TestCase):
    def test_runs_of_slots_become_ranges(self):
        self.assertEqual(E.ranges([321, 322, 323, 383, 403, 404, 512]),
                         ['321-323', '383', '403-404', '512'])
        self.assertEqual(E.ranges([]), [])


class ReadTests(unittest.TestCase):
    def test_initialized_headers_are_the_empty_slots(self):
        calls = []

        def read_header(midi_in, midi_out, slot, sequence):
            calls.append((slot, sequence))
            return {'initialized': slot in (3, 4, 6)}, b''

        with mock.patch.object(E.time, 'sleep'):
            self.assertEqual(E.empty_slots(None, None, 2, 6, read_header), [3, 4, 6])
        self.assertEqual(calls, [(2, 1), (3, 2), (4, 3), (5, 4), (6, 5)])

    def test_prints_the_empty_slots_as_ranges_and_closes_the_ports(self):
        port = mock.Mock()
        with mock.patch.object(E.download, 'open_ports', return_value=(port, port, 'MicroFreak')), \
                mock.patch.object(E, 'empty_slots', return_value=[5, 6, 9]), \
                contextlib.redirect_stdout(io.StringIO()) as out:
            self.assertEqual(E.main(['--first', '1', '--last', '10']), 0)
        self.assertEqual(json.loads(out.getvalue()),
                         {'slots_read': '1-10', 'empty_count': 3, 'empty': ['5-6', '9']})
        self.assertEqual(port.close_port.call_count, 2)

    def test_slots_outside_the_instrument_are_refused(self):
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(E.main(['--first', '0']), 1)
            self.assertEqual(E.main(['--first', '9', '--last', '3']), 1)
            self.assertEqual(E.main(['--last', '513']), 1)


if __name__ == '__main__':
    unittest.main()
