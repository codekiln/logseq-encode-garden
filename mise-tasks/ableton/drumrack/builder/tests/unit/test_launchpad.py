from types import SimpleNamespace

import numpy as np
import pytest

from drumrack_builder import launchpad as lp


@pytest.mark.parametrize(
    "pad, note",
    [(11, 36), (14, 39), (21, 40), (81, 64), (84, 67), (15, 68), (18, 71), (88, 99)],
)
def test_grid_matches_lives_drum_layout(pad, note):
    # Programmer Reference Guide, DAW Drumrack: left half 36-67, right half 68-99, four notes per row.
    assert lp.grid_to_note(pad, 36) == note
    assert lp.note_to_grid(note, 36) == pad


def test_grid_round_trip_and_bounds():
    for base in (0, 16, 64):
        notes = {lp.grid_to_note(10 * r + c, base) for r in range(1, 9) for c in range(1, 9)}
        assert notes == set(range(base, base + 64))
    assert lp.grid_to_note(19, 36) is None  # a side button, not a pad
    assert lp.note_to_grid(35, 36) is None and lp.note_to_grid(100, 36) is None


class FakePlayer:
    def __init__(self):
        self.played = []

    def load(self, path):
        return np.zeros((10, 2), dtype=np.float32) + len(path)

    def play(self, audio):
        self.played.append(float(audio[0, 0]))


def make(monkeypatch):
    pad = lp.Launchpad("x", 36)
    pad.player = FakePlayer()
    monkeypatch.setattr(pad, "light_all", lambda: None)
    return pad


def test_press_plays_the_pad_then_the_focused_candidate(monkeypatch):
    pad = make(monkeypatch)
    pad.pads = {36: {"path": "/a.wav", "state": "assigned"}}
    pad.receive(SimpleNamespace(type="note_on", note=11, velocity=100))
    pad.set_focus(36, "/candidate-b.wav")
    pad.receive(SimpleNamespace(type="note_on", note=11, velocity=100))
    pad.receive(SimpleNamespace(type="note_on", note=11, velocity=0))  # note off
    assert pad.player.played == [len("/a.wav"), len("/candidate-b.wav")]
    assert [e["note"] for e in pad.events] == [36, 36]


def test_arrows_shift_the_window_within_range(monkeypatch):
    pad = make(monkeypatch)
    for _ in range(5):
        pad.receive(SimpleNamespace(type="control_change", control=lp.UP, value=127))
    assert pad.base == 64
    for _ in range(9):
        pad.receive(SimpleNamespace(type="control_change", control=lp.DOWN, value=127))
    assert pad.base == 0


def test_colors_reflect_pad_state(monkeypatch):
    pad = make(monkeypatch)
    pad.pads = {36: {"state": "kept"}, 37: {"state": "shortlist"}}
    assert pad.color(36) == lp.BLUE and pad.color(37) == lp.YELLOW and pad.color(38) == lp.OFF
    pad.set_focus(37, "/x.wav")
    assert pad.color(37) == lp.PURPLE


def test_mixer_sums_and_retires_voices():
    player = lp.Player()
    player.play(np.full((3, 2), 0.25, dtype=np.float32))
    player.play(np.full((5, 2), 0.5, dtype=np.float32))
    out = np.zeros((4, 2), dtype=np.float32)
    player.callback(out, 4, None, None)
    assert out[0, 0] == pytest.approx(0.75) and out[3, 0] == pytest.approx(0.5)
    player.callback(out, 4, None, None)
    assert out[0, 0] == pytest.approx(0.5) and not player.voices
