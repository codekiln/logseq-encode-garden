"""Measure the properties used to sort and group samples: length, loudness, pitch and brightness."""

from __future__ import annotations

import math
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy import signal

from .adg import NOTE_NAMES

# Pitch and brightness only need the start of a long recording; a full read of a ten-minute
# field recording would stall the background analysis.
FEATURE_SECONDS = 20.0
SILENCE_DB = -120.0


@dataclass
class Analysis:
    duration: float
    frames: int
    sample_rate: int
    channels: int
    peak_db: float
    rms_db: float
    lufs: float | None
    pitch_hz: float | None
    pitch_midi: float | None
    pitch_confidence: float
    centroid_hz: float | None

    def as_dict(self) -> dict:
        return asdict(self)


def db(value: float) -> float:
    return SILENCE_DB if value <= 1e-6 else max(SILENCE_DB, 20 * math.log10(value))


def k_weighting(sample_rate: int) -> np.ndarray:
    """ITU-R BS.1770 K-weighting (high shelf, then high pass) as second-order sections at any rate."""
    # Pre-filter: shelving filter, from the BS.1770 analog prototype via the bilinear transform.
    f0, gain_db, q = 1681.974450955533, 3.999843853973347, 0.7071752369554196
    k = math.tan(math.pi * f0 / sample_rate)
    vh = 10 ** (gain_db / 20)
    vb = vh**0.4996667741545416
    a0 = 1 + k / q + k * k
    shelf = [
        (vh + vb * k / q + k * k) / a0,
        2 * (k * k - vh) / a0,
        (vh - vb * k / q + k * k) / a0,
        1.0,
        2 * (k * k - 1) / a0,
        (1 - k / q + k * k) / a0,
    ]
    f0, q = 38.13547087602444, 0.5003270373238773
    k = math.tan(math.pi * f0 / sample_rate)
    a0 = 1 + k / q + k * k
    high_pass = [1.0, -2.0, 1.0, 1.0, 2 * (k * k - 1) / a0, (1 - k / q + k * k) / a0]
    return np.array([shelf, high_pass])


def loudness(audio: np.ndarray, sample_rate: int) -> float | None:
    """Integrated loudness in LUFS with BS.1770 gating; a clip under 400 ms is measured ungated."""
    if audio.shape[0] < sample_rate // 100:
        return None
    weighted = signal.sosfilt(k_weighting(sample_rate), audio, axis=0)
    block, step = int(0.4 * sample_rate), int(0.1 * sample_rate)
    if weighted.shape[0] < block:
        power = float(np.mean(weighted**2, axis=0).sum())
        return None if power <= 0 else -0.691 + 10 * math.log10(power)
    starts = range(0, weighted.shape[0] - block + 1, step)
    powers = np.array([float(np.mean(weighted[s : s + block] ** 2, axis=0).sum()) for s in starts])
    powers = powers[powers > 0]
    if powers.size == 0:
        return None
    louder = powers[-0.691 + 10 * np.log10(powers) > -70]
    if louder.size == 0:
        return None
    relative = -0.691 + 10 * math.log10(float(louder.mean())) - 10
    gated = louder[-0.691 + 10 * np.log10(louder) > relative]
    return -0.691 + 10 * math.log10(float(gated.mean())) if gated.size else None


def yin(frame: np.ndarray, sample_rate: int, low: float = 40.0, high: float = 2000.0) -> tuple[float, float]:
    """Return (frequency, confidence) for one frame using the YIN difference function."""
    max_tau = min(int(sample_rate / low), frame.size // 2)
    min_tau = max(2, int(sample_rate / high))
    if max_tau <= min_tau + 2:
        return 0.0, 0.0
    width = frame.size - max_tau
    x = frame.astype(np.float64)
    energy = np.concatenate([[0.0], np.cumsum(x * x)])
    size = 1 << int(math.ceil(math.log2(frame.size * 2)))
    spectrum = np.fft.rfft(x, size)
    head = np.fft.rfft(x[:width], size)
    cross = np.fft.irfft(spectrum * np.conj(head), size)[:max_tau]
    taus = np.arange(max_tau)
    diff = energy[width] + (energy[taus + width] - energy[taus]) - 2 * cross
    diff[0] = 0.0
    cumulative = np.cumsum(diff[1:])
    normalized = np.ones(max_tau)
    with np.errstate(divide="ignore", invalid="ignore"):
        normalized[1:] = np.where(cumulative > 0, diff[1:] * np.arange(1, max_tau) / cumulative, 1.0)
    below = np.nonzero(normalized[min_tau:] < 0.15)[0]
    if below.size:
        tau = int(below[0]) + min_tau
        while tau + 1 < max_tau and normalized[tau + 1] < normalized[tau]:
            tau += 1
    else:
        tau = int(np.argmin(normalized[min_tau:])) + min_tau
    if 0 < tau < max_tau - 1:
        a, b, c = normalized[tau - 1], normalized[tau], normalized[tau + 1]
        shift = 0.5 * (a - c) / (a - 2 * b + c) if (a - 2 * b + c) != 0 else 0.0
    else:
        shift = 0.0
    confidence = float(max(0.0, 1.0 - normalized[tau]))
    return sample_rate / (tau + shift), confidence


def pitch(mono: np.ndarray, sample_rate: int) -> tuple[float | None, float]:
    """Median YIN estimate over the loud frames after the attack."""
    frame = 2048 if sample_rate <= 48000 else 4096
    hop = frame // 2
    if mono.size < frame:
        return None, 0.0
    level = float(np.max(np.abs(mono)))
    if level <= 1e-4:
        return None, 0.0
    estimates = []
    for start in range(0, min(mono.size - frame, sample_rate * 2) + 1, hop):
        chunk = mono[start : start + frame]
        if float(np.max(np.abs(chunk))) < level * 0.1:
            continue
        hz, confidence = yin(chunk, sample_rate)
        if hz > 0:
            estimates.append((hz, confidence))
    if not estimates:
        return None, 0.0
    confident = [e for e in estimates if e[1] >= 0.5] or estimates
    hz = float(np.median([e[0] for e in confident]))
    return hz, float(np.median([e[1] for e in confident]))


def centroid(mono: np.ndarray, sample_rate: int) -> float | None:
    if mono.size < 64 or float(np.max(np.abs(mono))) <= 1e-5:
        return None
    window = mono[: sample_rate * 2] * np.hanning(min(mono.size, sample_rate * 2))
    magnitude = np.abs(np.fft.rfft(window))
    if magnitude.sum() <= 0:
        return None
    freqs = np.fft.rfftfreq(window.size, 1 / sample_rate)
    return float((freqs * magnitude).sum() / magnitude.sum())


class LiveOnlyError(ValueError):
    """Ableton's packs ship AIFF-C files in an encoding that only Live decodes."""


def live_only(path: Path) -> bool:
    with open(path, "rb") as handle:
        head = handle.read(64)
    return head[:4] == b"FORM" and head[8:12] == b"AIFC" and b"able" in head


def analyze(path: Path) -> Analysis:
    if live_only(path):
        raise LiveOnlyError("encoded for Ableton Live only; audition it in Live")
    info = sf.info(str(path))
    limit = min(info.frames, int(FEATURE_SECONDS * info.samplerate)) if info.frames > 0 else -1
    audio, sample_rate = sf.read(str(path), frames=limit, dtype="float32", always_2d=True)
    frames = info.frames if info.frames > 0 else audio.shape[0]
    mono = audio.mean(axis=1)
    peak = float(np.max(np.abs(audio))) if audio.size else 0.0
    rms = float(np.sqrt(np.mean(mono.astype(np.float64) ** 2))) if mono.size else 0.0
    hz, confidence = pitch(mono, sample_rate)
    return Analysis(
        duration=frames / sample_rate,
        frames=frames,
        sample_rate=sample_rate,
        channels=info.channels,
        peak_db=round(db(peak), 2),
        rms_db=round(db(rms), 2),
        lufs=None if (lufs := loudness(audio.astype(np.float64), sample_rate)) is None else round(lufs, 2),
        pitch_hz=None if hz is None else round(hz, 2),
        pitch_midi=None if hz is None else round(69 + 12 * math.log2(hz / 440.0), 2),
        pitch_confidence=round(confidence, 3),
        centroid_hz=None if (c := centroid(mono, sample_rate)) is None else round(c, 1),
    )


# ---------------------------------------------------------------------------- grouping

PITCH_CONFIDENCE = 0.6
DURATION_BUCKETS = [
    (0.1, "under 0.1 s"),
    (0.3, "0.1–0.3 s"),
    (1.0, "0.3–1 s"),
    (3.0, "1–3 s"),
    (10.0, "3–10 s"),
    (math.inf, "over 10 s"),
]
BRIGHTNESS_BUCKETS = [
    (500, "dark (under 500 Hz)"),
    (2000, "mid (500 Hz–2 kHz)"),
    (5000, "bright (2–5 kHz)"),
    (math.inf, "very bright (over 5 kHz)"),
]
GROUPS = ("folder", "duration", "pitch", "register", "loudness", "brightness")


def bucket(value: float, buckets: list[tuple[float, str]]) -> tuple[int, str]:
    for index, (limit, label) in enumerate(buckets):
        if value < limit:
            return index, label
    return len(buckets), buckets[-1][1]


def group_key(sample: dict, by: str) -> tuple[float, str]:
    """A sortable key and a label for one sample under one grouping."""
    if by == "folder":
        return 0, sample.get("folder") or ""
    if sample.get("duration") is None:
        return math.inf, "not analyzed"
    if by == "duration":
        return bucket(sample["duration"], DURATION_BUCKETS)
    if by in ("pitch", "register"):
        midi = sample.get("pitch_midi")
        if midi is None or (sample.get("pitch_confidence") or 0) < PITCH_CONFIDENCE:
            return 1000, "unpitched"
        note = int(round(midi))
        if by == "pitch":
            return note % 12, NOTE_NAMES[note % 12]
        octave = note // 12 - 2
        return octave, f"octave {octave}"
    if by == "loudness":
        level = sample.get("lufs") if sample.get("lufs") is not None else sample.get("rms_db")
        if level is None or level <= SILENCE_DB:
            return 1000, "silent"
        top = 6 * math.ceil(level / 6)
        return -top, f"{top - 6} to {top} {'LUFS' if sample.get('lufs') is not None else 'dB RMS'}"
    if by == "brightness":
        if sample.get("centroid_hz") is None:
            return 1000, "silent"
        return bucket(sample["centroid_hz"], BRIGHTNESS_BUCKETS)
    raise ValueError(f"unknown grouping {by!r}; choose one of {', '.join(GROUPS)}")


def group(samples: list[dict], by: str) -> list[dict]:
    groups: dict[str, dict] = {}
    for sample in samples:
        order, label = group_key(sample, by)
        entry = groups.setdefault(label, {"label": label, "order": order, "samples": []})
        entry["samples"].append(sample)
    return sorted(groups.values(), key=lambda g: (g["order"], g["label"]))
