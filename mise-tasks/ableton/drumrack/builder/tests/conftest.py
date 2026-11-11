"""Synthetic samples, racks and configs, so the tests never read a personal library."""

from __future__ import annotations

import copy
import hashlib
import textwrap
from collections.abc import Callable
from pathlib import Path

import numpy as np
import pytest
import soundfile as sf

from drumrack_builder import adg, config


def tone(
    path: Path,
    hz: float = 220.0,
    seconds: float = 0.5,
    rate: int = 44100,
    level: float = 0.5,
    channels: int = 1,
    fmt: str | None = None,
) -> Path:
    t = np.arange(int(seconds * rate)) / rate
    wave = level * np.sin(2 * np.pi * hz * t) * np.exp(-3 * t)
    data = np.stack([wave] * channels, axis=1) if channels > 1 else wave
    path.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(path), data, rate, format=fmt)
    return path


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


@pytest.fixture
def make_tone() -> Callable[..., Path]:
    return tone


@pytest.fixture
def library(tmp_path: Path) -> Path:
    """A fake Ableton User Library with a few samples."""
    root = tmp_path / "User Library"
    samples = root / "Samples" / "Kit"
    for i, hz in enumerate([55, 110, 220, 440, 880, 1760]):
        tone(samples / f"tone {i:02d} {hz}Hz.wav", hz=hz, seconds=0.2 + 0.2 * i)
    tone(samples / "stereo.aif", hz=330, channels=2, fmt="AIFF")
    return root


def sample_file(path: Path) -> adg.SampleFile:
    info = sf.info(str(path))
    return adg.SampleFile.from_path(path, frames=info.frames, sample_rate=info.samplerate)


@pytest.fixture
def base_rack(tmp_path: Path, library: Path) -> Path:
    """A Drum Rack with four simple pads, one choke group, one non-default Detune and one layered pad."""
    samples = sorted((library / "Samples" / "Kit").glob("*.wav"))
    output = library / "Presets" / "Instruments" / "Drum Rack" / "Base.adg"
    plan = [
        adg.PadPlan(note=36 + i, name=f"pad {i}" if i % 2 else "", sample=sample_file(samples[i])) for i in range(4)
    ]
    root = adg.build_rack(None, plan, output, user_library=library)
    group = adg.branches(root)
    pads = group.findall("DrumBranchPreset")
    adg.set_value(pads[1], "ZoneSettings/ChokeGroup", 2)
    part = adg.simple_part(pads[2])
    assert part is not None
    adg.set_value(part, "Detune", 7)
    adg.set_value(pads[2], "DevicePresets/AbletonDevicePreset/Device/OriginalSimpler/Globals/NumVoices", 3)
    # Two sample zones stand in for a layered or nested pad (a Sampler or an Instrument Rack).
    layered = copy.deepcopy(pads[3])
    adg.set_value(layered, "ZoneSettings/ReceivingNote", 128 - 48)
    adg.set_value(layered, "ZoneSettings/ChokeGroup", 1)
    zones = layered.find(".//MultiSampleMap/SampleParts")
    assert zones is not None
    zones.append(copy.deepcopy(zones[0]))
    group.append(layered)
    macro = root.find("GroupDevicePreset/Device/DrumGroupDevice/MacroControls.0/Manual")
    assert macro is not None
    macro.set("Value", "42")
    adg.write_rack(root, output)
    return output


@pytest.fixture
def make_config(tmp_path: Path, library: Path) -> Callable[..., config.Config]:
    def build(**overrides: str) -> config.Config:
        text = textwrap.dedent(f"""
            [library]
            user_library = "{library}"
            sample_folders = ["{library / "Samples"}"]
            rack_folders = ["{library / "Presets"}"]
            extensions = ["wav", "aif", "aiff", "flac"]
            [output]
            folder = "{overrides.get("output", library / "Presets" / "Instruments" / "Drum Rack" / "Builder")}"
            [state]
            folder = "{tmp_path / "state"}"
            [launchpad]
            port = "Test LPProMK3 MIDI"
            base_note = 36
        """)
        path = tmp_path / "config.toml"
        path.write_text(text)
        return config.load([path])

    return build
