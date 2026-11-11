"""Audition a rack's pads from a Launchpad Pro MK3 in Programmer Mode.

The grid follows Live's own Launchpad drum layout: the left four columns hold 32 notes rising four per
row from the bottom, and the right four columns hold the next 32. The Up and Down arrows shift the
64-note window by 16 notes. Pads play through this computer's audio output, not through Live.

Needs the optional ``launchpad`` extra (mido, python-rtmidi, sounddevice).
"""

from __future__ import annotations

import logging
import threading
import time
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

import numpy as np
import soundfile as sf

log = logging.getLogger(__name__)

SYSEX_HEADER = [0x00, 0x20, 0x29, 0x02, 0x0E]
PROGRAMMER_MODE = SYSEX_HEADER + [0x0E, 0x01]
LIVE_MODE = SYSEX_HEADER + [0x0E, 0x00]
LAYOUT_QUERY = SYSEX_HEADER + [0x00]
NOTE_LAYOUT = 0x04
UP, DOWN = 80, 70
SHIFT = 16

# Launchpad palette indexes (Programmer Reference Guide, colour palette).
OFF, WHITE, RED, YELLOW, GREEN, BLUE, PURPLE = 0, 3, 5, 13, 21, 45, 53
COLORS = {"kept": BLUE, "assigned": GREEN, "shortlist": YELLOW, "focus": PURPLE, "missing": RED}


def grid_to_note(pad: int, base: int) -> int | None:
    """Programmer-mode pad number (10*row + column) to a Drum Rack note."""
    row, column = divmod(pad, 10)
    if not (1 <= row <= 8 and 1 <= column <= 8):
        return None
    half = 0 if column <= 4 else 32
    return base + half + (row - 1) * 4 + (column - 1) % 4


def note_to_grid(note: int, base: int) -> int | None:
    offset = note - base
    if not 0 <= offset < 64:
        return None
    half, within = divmod(offset, 32)
    row, column = divmod(within, 4)
    return 10 * (row + 1) + column + 1 + 4 * half


@dataclass
class Voice:
    audio: np.ndarray
    position: int = 0


@dataclass
class Player:
    """A small polyphonic mixer on one PortAudio output stream."""

    device: str = ""
    sample_rate: int = 48000
    voices: list[Voice] = field(default_factory=list)
    lock: threading.Lock = field(default_factory=threading.Lock)
    stream: object = None

    def start(self) -> None:
        import sounddevice as sd

        device = self.device or None
        self.sample_rate = int(sd.query_devices(device, "output")["default_samplerate"])
        self.stream = sd.OutputStream(
            samplerate=self.sample_rate,
            channels=2,
            dtype="float32",
            device=device,
            callback=self.callback,
            latency="low",
        )
        self.stream.start()  # type: ignore[attr-defined]

    def stop(self) -> None:
        if self.stream is not None:
            self.stream.stop()  # type: ignore[attr-defined]
            self.stream.close()  # type: ignore[attr-defined]
            self.stream = None

    def load(self, path: str) -> np.ndarray:
        audio, rate = sf.read(path, dtype="float32", always_2d=True)
        if audio.shape[1] == 1:
            audio = np.repeat(audio, 2, axis=1)
        audio = audio[:, :2]
        if rate != self.sample_rate and audio.shape[0] > 1:
            length = int(audio.shape[0] * self.sample_rate / rate)
            x = np.linspace(0, audio.shape[0] - 1, length)
            audio = np.stack([np.interp(x, np.arange(audio.shape[0]), audio[:, c]) for c in range(2)], axis=1)
        return audio.astype(np.float32)

    def play(self, audio: np.ndarray) -> None:
        with self.lock:
            self.voices = self.voices[-15:] + [Voice(audio)]

    def callback(self, out, frames, _time, _status) -> None:  # PortAudio thread
        out.fill(0)
        with self.lock:
            alive = []
            for voice in self.voices:
                chunk = voice.audio[voice.position : voice.position + frames]
                out[: len(chunk)] += chunk
                voice.position += frames
                if voice.position < len(voice.audio):
                    alive.append(voice)
            self.voices = alive
        np.clip(out, -1, 1, out=out)


class Launchpad:
    """Owns the Launchpad's MIDI port while connected and restores its previous layout on disconnect."""

    def __init__(self, port_match: str, base_note: int, audio_device: str = ""):
        self.port_match = port_match
        self.base = base_note
        self.player = Player(device=audio_device)
        self.inport: Any = None
        self.outport: Any = None
        self.previous_layout: list[int] | None = None
        self.pads: dict[int, dict] = {}  # note -> {"path", "state", "label"}
        self.cache: dict[str, np.ndarray] = {}
        self.focus: dict[int, str] = {}  # note -> sample path overriding the pad while comparing
        self.events: list[dict] = []
        self.error = ""
        self.on_press: Callable[[int], None] | None = None

    # ------------------------------------------------------------------ discovery

    @staticmethod
    def available() -> tuple[bool, str]:
        try:
            import mido  # noqa: F401
            import rtmidi  # noqa: F401
            import sounddevice  # noqa: F401
        except Exception as error:  # ImportError, or PortAudio missing at import time
            return False, f"install the launchpad extra ({error})"
        return True, ""

    def ports(self) -> list[str]:
        import mido

        return [n for n in mido.get_input_names() if self.port_match in n]

    @property
    def connected(self) -> bool:
        return self.inport is not None

    def status(self) -> dict:
        ok, why = self.available()
        return {
            "available": ok,
            "reason": why,
            "connected": self.connected,
            "ports": self.ports() if ok else [],
            "base_note": self.base,
            "error": self.error,
            "events": self.events[-20:],
        }

    # ------------------------------------------------------------------ connection

    def connect(self) -> None:
        import mido

        ok, why = self.available()
        if not ok:
            raise RuntimeError(why)
        if self.connected:
            return
        inputs = self.ports()
        outputs = [n for n in mido.get_output_names() if self.port_match in n]
        if not inputs or not outputs:
            raise RuntimeError(f"no MIDI port matching {self.port_match!r}; is the Launchpad connected?")
        self.outport = mido.open_output(outputs[0])
        self.inport = mido.open_input(inputs[0])
        self.previous_layout = self.query_layout()
        self.player.start()
        self.inport.callback = self.receive
        self.send_sysex(PROGRAMMER_MODE)
        self.cache.clear()
        self.light_all()
        threading.Thread(target=self.warm, daemon=True).start()
        self.error = ""

    def disconnect(self) -> None:
        # Close the input before sending anything: rtmidi delivers input on CoreMIDI's thread through a
        # Python callback, and closing a port while CoreMIDI is still delivering can deadlock on the GIL.
        if self.inport is not None:
            self.inport.callback = None
            self.inport.close()
        if self.outport is not None:
            self.clear_lights()
            # Leaving Programmer Mode needs a layout select; return to where the user was.
            layout = self.previous_layout or [NOTE_LAYOUT, 0]
            if layout[0] == 0x11:  # the user was already in Programmer Mode
                layout = [NOTE_LAYOUT, 0]
            self.send_sysex(SYSEX_HEADER + [0x00, *layout, 0x00])
            time.sleep(0.1)  # let CoreMIDI deliver the last messages before the port goes away
            self.outport.close()
        self.player.stop()
        self.inport = self.outport = None

    def query_layout(self, timeout: float = 0.5) -> list[int] | None:
        """Ask the Launchpad which layout is showing: replies are F0 header 00 <layout> <page> F7."""
        assert self.inport is not None
        for _ in self.inport.iter_pending():
            pass
        self.send_sysex(LAYOUT_QUERY)
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            for message in self.inport.iter_pending():
                data = list(getattr(message, "data", []))
                if message.type == "sysex" and data[:6] == SYSEX_HEADER + [0x00] and len(data) >= 8:
                    return data[6:8]
            time.sleep(0.01)
        return None

    def send_sysex(self, data: list[int]) -> None:
        import mido

        assert self.outport is not None
        self.outport.send(mido.Message("sysex", data=data))

    # ------------------------------------------------------------------ pads and lights

    def set_pads(self, pads: dict[int, dict]) -> None:
        self.pads = pads
        if self.connected:
            self.light_all()
            threading.Thread(target=self.warm, daemon=True).start()

    def warm(self) -> None:
        """Decode every pad's sample ahead of time so the first press plays without a delay."""
        for path in [p.get("path") for p in self.pads.values()] + list(self.focus.values()):
            if path and path not in self.cache:
                try:
                    self.cache[path] = self.player.load(path)
                except Exception as error:
                    log.warning("cannot load %s: %s", path, error)

    def set_focus(self, note: int, path: str | None) -> None:
        if path is None:
            self.focus.pop(note, None)
        else:
            self.focus[note] = path
        if self.connected:
            self.light_all()

    def color(self, note: int) -> int:
        if note in self.focus:
            return COLORS["focus"]
        pad = self.pads.get(note)
        return OFF if pad is None else COLORS.get(pad["state"], OFF)

    def light_all(self) -> None:
        import mido

        if self.outport is None:
            return
        for row in range(1, 9):
            for column in range(1, 9):
                pad = 10 * row + column
                note = grid_to_note(pad, self.base)
                assert note is not None
                self.outport.send(mido.Message("note_on", note=pad, velocity=self.color(note)))
        self.outport.send(mido.Message("control_change", control=UP, value=WHITE if self.base + SHIFT <= 64 else 0))
        self.outport.send(mido.Message("control_change", control=DOWN, value=WHITE if self.base - SHIFT >= 0 else 0))

    def clear_lights(self) -> None:
        import mido

        if self.outport is None:
            return
        for row in range(1, 9):
            for column in range(1, 9):
                self.outport.send(mido.Message("note_on", note=10 * row + column, velocity=0))
        for control in (UP, DOWN):
            self.outport.send(mido.Message("control_change", control=control, value=0))

    # ------------------------------------------------------------------ input

    def receive(self, message) -> None:  # mido's MIDI thread
        try:
            if message.type == "note_on" and message.velocity > 0:
                note = grid_to_note(message.note, self.base)
                if note is not None:
                    self.press(note)
            elif message.type == "control_change" and message.value > 0 and message.control in (UP, DOWN):
                step = SHIFT if message.control == UP else -SHIFT
                self.base = max(0, min(64, self.base + step))
                self.light_all()
        except Exception as error:  # an exception here would silently kill the MIDI callback
            log.exception("Launchpad input failed")
            self.error = str(error)

    def press(self, note: int) -> None:
        path = self.focus.get(note) or (self.pads.get(note) or {}).get("path")
        self.events = self.events[-50:] + [{"note": note, "time": time.time(), "path": path}]
        if self.on_press is not None:
            self.on_press(note)
        if not path:
            return
        audio = self.cache.get(path)
        if audio is None:
            audio = self.cache[path] = self.player.load(path)
        self.player.play(audio)
