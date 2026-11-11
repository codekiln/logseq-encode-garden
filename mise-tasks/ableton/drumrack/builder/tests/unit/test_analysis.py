from pathlib import Path

import numpy as np
import pytest
import soundfile as sf

from drumrack_builder import analysis


@pytest.mark.parametrize("hz", [55.0, 110.0, 261.63, 440.0, 1000.0])
def test_pitch_of_a_decaying_sine(tmp_path: Path, make_tone, hz):
    result = analysis.analyze(make_tone(tmp_path / "t.wav", hz=hz, seconds=0.6))
    assert result.pitch_hz == pytest.approx(hz, rel=0.01)
    assert result.pitch_confidence > 0.8


def test_bs1770_reference_level(tmp_path: Path):
    # A 997 Hz sine at -20 dBFS on one channel measures -23.0 LUFS (ITU-R BS.1770-4 compliance signal).
    rate = 48000
    t = np.arange(rate * 5) / rate
    sf.write(str(tmp_path / "ref.wav"), 0.1 * np.sin(2 * np.pi * 997 * t), rate)
    assert analysis.analyze(tmp_path / "ref.wav").lufs == pytest.approx(-23.0, abs=0.1)


def test_noise_is_unpitched_and_bright(tmp_path: Path):
    rng = np.random.default_rng(1)
    sf.write(str(tmp_path / "n.wav"), rng.uniform(-0.5, 0.5, 44100), 44100)
    result = analysis.analyze(tmp_path / "n.wav")
    assert result.pitch_confidence < analysis.PITCH_CONFIDENCE
    assert result.centroid_hz > 5000


def test_silence_short_stereo_and_aiff(tmp_path: Path, make_tone):
    sf.write(str(tmp_path / "s.wav"), np.zeros(4410), 44100)
    silent = analysis.analyze(tmp_path / "s.wav")
    assert silent.peak_db == analysis.SILENCE_DB and silent.pitch_hz is None and silent.lufs is None
    short = analysis.analyze(make_tone(tmp_path / "short.wav", seconds=0.02))
    assert short.duration == pytest.approx(0.02, abs=1e-3) and short.lufs is not None
    stereo = analysis.analyze(make_tone(tmp_path / "st.aif", hz=330, channels=2, fmt="AIFF"))
    assert stereo.channels == 2 and stereo.pitch_hz == pytest.approx(330, rel=0.01)


def test_long_files_are_measured_for_duration_but_read_partly(tmp_path: Path, monkeypatch, make_tone):
    monkeypatch.setattr(analysis, "FEATURE_SECONDS", 1.0)
    result = analysis.analyze(make_tone(tmp_path / "long.wav", seconds=3.0))
    assert result.duration == pytest.approx(3.0)


def sample(**fields):
    return {
        "folder": "/x",
        "duration": 0.5,
        "pitch_midi": 45.0,
        "pitch_confidence": 0.9,
        "lufs": -14.0,
        "rms_db": -16.0,
        "centroid_hz": 800.0,
        **fields,
    }


def test_groupings():
    assert analysis.group_key(sample(duration=0.05), "duration")[1] == "under 0.1 s"
    assert analysis.group_key(sample(duration=12), "duration")[1] == "over 10 s"
    assert analysis.group_key(sample(), "pitch")[1] == "A"
    assert analysis.group_key(sample(), "register")[1] == "octave 1"
    assert analysis.group_key(sample(pitch_confidence=0.2), "pitch")[1] == "unpitched"
    assert analysis.group_key(sample(), "loudness")[1] == "-18 to -12 LUFS"
    assert analysis.group_key(sample(lufs=None), "loudness")[1] == "-18 to -12 dB RMS"
    assert analysis.group_key(sample(centroid_hz=6000), "brightness")[1].startswith("very bright")
    assert analysis.group_key(sample(duration=None), "brightness")[1] == "not analyzed"
    with pytest.raises(ValueError):
        analysis.group_key(sample(), "colour")


def test_group_orders_buckets():
    rows = [sample(duration=d) for d in (5, 0.05, 0.5, 0.06)]
    groups = analysis.group(rows, "duration")
    assert [g["label"] for g in groups] == ["under 0.1 s", "0.3–1 s", "3–10 s"]
    assert len(groups[0]["samples"]) == 2


def test_live_only_pack_files_are_recognized(tmp_path: Path):
    # The header Live's Factory Packs use: an AIFF-C whose compression chunk names Ableton's codec.
    pack = tmp_path / "pack.aif"
    pack.write_bytes(b"FORM\x00\x00\xff\xabAIFCFVER\x00\x00\x00\x04\xa2\x80Q@able\x00\x00\x01T" + bytes(64))
    assert analysis.live_only(pack)
    with pytest.raises(analysis.LiveOnlyError):
        analysis.analyze(pack)
