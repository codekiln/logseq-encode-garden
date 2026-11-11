"""Drive the Launchpad code through real CoreMIDI virtual ports standing in for the device."""

import sys
import threading
import time

import pytest

mido = pytest.importorskip("mido")
pytest.importorskip("rtmidi")
pytestmark = pytest.mark.skipif(sys.platform != "darwin", reason="virtual MIDI ports are tested on macOS")

from drumrack_builder import launchpad as lp  # noqa: E402

NAME = "Builder Test LPProMK3 MIDI"


class FakeDevice:
    """Virtual ports named like the Launchpad: answers the layout query and records what it is sent."""

    def __init__(self):
        self.to_host = mido.open_output(NAME, virtual=True)
        # Polled rather than given a callback: a Python callback on an in-process virtual destination
        # deadlocks with CoreMIDI when the sending port closes.
        self.from_host = mido.open_input(NAME, virtual=True)
        self.received = []
        self.running = True
        self.thread = threading.Thread(target=self.poll, daemon=True)
        self.thread.start()

    def poll(self):
        while self.running:
            for message in self.from_host.iter_pending():
                self.received.append(message)
                if message.type == "sysex" and list(message.data) == lp.LAYOUT_QUERY:
                    self.to_host.send(mido.Message("sysex", data=lp.SYSEX_HEADER + [0x00, 0x00, 0x00, 0x00]))
            time.sleep(0.005)

    def close(self):
        self.running = False
        self.thread.join()
        self.to_host.close()
        self.from_host.close()


class FakePlayer:
    def __init__(self):
        self.played = threading.Event()
        self.paths = []

    def start(self):
        pass

    def stop(self):
        pass

    def load(self, path):
        self.paths.append(path)
        return path

    def play(self, audio):
        self.played.set()


def wait_for(condition, timeout=2.0):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if condition():
            return True
        time.sleep(0.01)
    return False


def test_connect_light_play_and_restore():
    device = FakeDevice()
    pad = lp.Launchpad("Builder Test LPProMK3", 36)
    pad.player = FakePlayer()
    try:
        time.sleep(0.2)  # CoreMIDI publishes new virtual endpoints asynchronously
        pad.connect()
        assert pad.previous_layout == [0x00, 0x00]  # Session layout, as the fake device reported
        assert wait_for(lambda: any(m.type == "sysex" and list(m.data) == lp.PROGRAMMER_MODE for m in device.received))
        pad.set_pads({36: {"path": "/kick.wav", "state": "assigned"}, 99: {"path": None, "state": "shortlist"}})
        assert wait_for(
            lambda: any(m.type == "note_on" and m.note == 11 and m.velocity == lp.GREEN for m in device.received)
        )
        assert wait_for(
            lambda: any(m.type == "note_on" and m.note == 88 and m.velocity == lp.YELLOW for m in device.received)
        )
        device.to_host.send(mido.Message("note_on", note=11, velocity=90))
        assert pad.player.played.wait(2.0)
        assert pad.events[-1]["note"] == 36
        device.to_host.send(mido.Message("control_change", control=lp.UP, value=127))
        assert wait_for(lambda: pad.base == 52)
        pad.disconnect()
        restore = lp.SYSEX_HEADER + [0x00, 0x00, 0x00, 0x00]
        assert wait_for(lambda: any(m.type == "sysex" and list(m.data) == restore for m in device.received))
    finally:
        if pad.connected:
            pad.disconnect()
        device.close()
