#!/usr/bin/env python3
"""Detect onsets and pitches, step by step, in a mono recording of a sequence.

The caller knows when each step starts (it sent the clock), so this module
only answers, for each step window: did a new note start, how loud is it,
what single pitch dominates (YIN), and which notes a chord holds (iterative
harmonic-sum estimation). It needs numpy.
"""
import math

import numpy as np

A4 = 440.0


def hz_to_midi(hz):
    return 69 + 12 * math.log2(hz / A4)


def midi_to_hz(note):
    return A4 * 2 ** ((note - 69) / 12)


def onset_envelope(audio, sr, hop=240, frame=1024):
    """Spectral flux of log magnitudes, one value per hop (5 ms at 48 kHz)."""
    audio = np.asarray(audio, dtype=np.float64)
    if len(audio) < frame:
        audio = np.pad(audio, (0, frame - len(audio)))
    count = 1 + (len(audio) - frame) // hop
    index = np.arange(frame)[None, :] + hop * np.arange(count)[:, None]
    frames = audio[index] * np.hanning(frame)
    magnitude = np.log1p(1000 * np.abs(np.fft.rfft(frames, axis=1)))
    flux = np.maximum(np.diff(magnitude, axis=0), 0).sum(axis=1)
    # Value i describes the change into frame i + 1, centred half a frame later.
    times = (np.arange(1, count) * hop + frame / 2) / sr
    return times, flux


def estimate_lag(times, flux, trigger_times, search):
    """Shift (seconds) that best lines the flux peaks up with trigger times."""
    trigger_times = np.asarray(trigger_times, dtype=np.float64)
    if not len(trigger_times) or not len(flux):
        return 0.0
    # A triangular smoothing gives each peak one summit, so the best lag is
    # the middle of a match, not the first lag that touches it.
    smooth = np.convolve(flux, np.array([1, 2, 3, 2, 1]) / 9, mode='same')
    lags = np.arange(-search, search + 0.0005, 0.001)
    scores = [np.interp(trigger_times + lag, times, smooth, left=0, right=0).sum() for lag in lags]
    return float(lags[int(np.argmax(scores))])


def yin(segment, sr, fmin=27.5, fmax=2000.0, threshold=0.15):
    """Return (f0 in Hz or None, aperiodicity) using de Cheveigné and Kawahara's YIN."""
    x = np.asarray(segment, dtype=np.float64)
    x = x - x.mean()
    tau_min = max(2, int(sr / fmax))
    tau_max = min(int(sr / fmin), len(x) // 2)
    if tau_max <= tau_min + 2 or not np.any(x):
        return None, 1.0
    width = len(x) - tau_max
    size = 1 << (len(x) + width).bit_length()
    spectrum = np.fft.rfft(x, size) * np.conj(np.fft.rfft(x[:width], size))
    correlation = np.fft.irfft(spectrum, size)[:tau_max + 1]
    energy = np.concatenate([[0.0], np.cumsum(x * x)])
    energy_lag = energy[np.arange(tau_max + 1) + width] - energy[np.arange(tau_max + 1)]
    difference = energy[width] + energy_lag - 2 * correlation
    difference[0] = 0.0
    cumulative = np.cumsum(difference[1:])
    normalized = np.ones(tau_max + 1)
    normalized[1:] = difference[1:] * np.arange(1, tau_max + 1) / np.maximum(cumulative, 1e-12)
    candidates = np.where(normalized[tau_min:tau_max] < threshold)[0]
    if candidates.size:
        tau = int(candidates[0]) + tau_min
        while tau + 1 < tau_max and normalized[tau + 1] < normalized[tau]:
            tau += 1
    else:
        tau = int(np.argmin(normalized[tau_min:tau_max])) + tau_min
    aperiodicity = float(normalized[tau])
    if 1 <= tau < tau_max:
        a, b, c = normalized[tau - 1], normalized[tau], normalized[tau + 1]
        shift = 0.5 * (a - c) / (a - 2 * b + c) if (a - 2 * b + c) else 0.0
    else:
        shift = 0.0
    period = tau + max(-1.0, min(1.0, shift))
    return (sr / period if aperiodicity < 0.5 else None), aperiodicity


def _spectrum(segment, sr, max_hz):
    x = np.asarray(segment, dtype=np.float64)
    x = (x - x.mean()) * np.hanning(len(x))
    size = 1 << (4 * len(x) - 1).bit_length()
    magnitude = np.abs(np.fft.rfft(x, size))
    freqs = np.fft.rfftfreq(size, 1 / sr)
    keep = freqs <= max_hz
    return freqs[keep], magnitude[keep], sr / size


def chord_notes(segment, sr, lowest=24, highest=96, max_notes=4, ratio=0.35,
                max_hz=6000.0, neighbour_ratio=0.7, tolerance=0.4):
    """Estimate up to `max_notes` simultaneous MIDI notes.

    Each pass scores every candidate note by a weighted sum of the spectrum at
    its harmonics (Klapuri 2006 weights), keeps the best, and subtracts a
    smoothed copy of that note's harmonics so a second note sharing some of its
    partials can still be found. Passes stop when a candidate scores under
    `ratio` times the first note's score.
    """
    freqs, magnitude, resolution = _spectrum(segment, sr, max_hz)
    if not np.any(magnitude):
        return []
    residual = magnitude.copy()
    candidates = np.arange(lowest, highest + 1)
    f0s = np.array([midi_to_hz(n) for n in candidates])
    harmonic_numbers = np.arange(1, 21)

    def bands(f0):
        centres = f0 * harmonic_numbers
        centres = centres[centres < freqs[-1]]
        width = np.maximum(centres * (2 ** (tolerance / 12) - 1), 1.5 * resolution)
        lo = np.searchsorted(freqs, centres - width)
        hi = np.searchsorted(freqs, centres + width, side='right')
        return centres, lo, np.maximum(hi, lo + 1)

    plans = [bands(f0) for f0 in f0s]
    found, first = [], None
    for _ in range(max_notes):
        scores = []
        for note, f0, (centres, lo, hi) in zip(candidates, f0s, plans):
            peaks = np.array([residual[a:b].max() for a, b in zip(lo, hi)])
            weights = (f0 + 27) / (centres + 320)
            score = float((weights * peaks).sum())
            # A detuned or vibrato note leaks into the semitones beside it.
            if first is not None and any(abs(int(note) - n['midi']) <= 1 for n in found) \
                    and score < neighbour_ratio * first:
                score = 0.0
            scores.append(score)
        best = int(np.argmax(scores))
        if first is None:
            first = scores[best]
        if scores[best] <= 0 or scores[best] < ratio * first:
            break
        note = int(candidates[best])
        if note in {n['midi'] for n in found}:
            break
        found.append({'midi': note, 'salience': round(scores[best] / first, 3)})
        centres, lo, hi = plans[best]
        peaks = np.array([residual[a:b].max() for a, b in zip(lo, hi)])
        smooth = np.minimum(peaks, np.convolve(np.pad(peaks, 1, mode='edge'),
                                                np.ones(3) / 3, mode='valid'))
        for (a, b), amount in zip(zip(lo, hi), smooth):
            residual[a:b] = np.maximum(residual[a:b] - amount, 0)
    return sorted(found, key=lambda n: n['midi'])


def _db(value):
    return round(20 * math.log10(max(value, 1e-9)), 1)


def analyse_steps(audio, sr, step_starts, step_seconds, noise_floor_rms,
                  onset_threshold, flux_times, flux, chords=True, silence_db=-40.0):
    """Describe every step window; `step_starts` are seconds into `audio`.

    A step counts as sounding when its level is above four times the noise
    floor and above `silence_db` relative to the recording's peak.
    """
    audio = np.asarray(audio, dtype=np.float64)
    silence = float(np.abs(audio).max(initial=0.0)) * 10 ** (silence_db / 20)
    results = []
    skip = min(0.012, step_seconds * 0.15)
    for start in step_starts:
        begin = int(round((start + skip) * sr))
        end = int(round((start + min(step_seconds, 0.4)) * sr))
        segment = audio[max(0, begin):max(0, min(end, len(audio)))]
        level = float(np.sqrt(np.mean(segment ** 2))) if segment.size else 0.0
        near = (flux_times >= start - 0.02) & (flux_times <= start + 0.045)
        strength = float(flux[near].max()) if near.any() else 0.0
        sounding = segment.size > 0 and level > max(4 * noise_floor_rms, silence)
        result = {'onset': bool(strength >= onset_threshold), 'onset_strength': round(strength, 2),
                  'level_db': _db(level), 'sounding': bool(sounding),
                  'f0_hz': None, 'midi': None, 'cents': None, 'aperiodicity': None,
                  'chord': []}
        if sounding:
            fmin = max(27.5, 2.2 * sr / max(segment.size, 1))
            f0, aperiodicity = yin(segment, sr, fmin=fmin)
            result['aperiodicity'] = round(aperiodicity, 3)
            if f0:
                exact = hz_to_midi(f0)
                result.update(f0_hz=round(f0, 2), midi=int(round(exact)),
                              cents=round(100 * (exact - round(exact)), 1))
            if chords:
                result['chord'] = chord_notes(segment, sr)
        results.append(result)
    return results


def onset_threshold(flux):
    """Flux level that separates note starts from background change."""
    median = float(np.median(flux))
    spread = float(np.median(np.abs(flux - median))) or 1e-9
    return max(median + 8 * spread, 0.25 * float(np.percentile(flux, 99.5)))
