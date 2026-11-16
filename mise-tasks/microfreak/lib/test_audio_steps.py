import importlib.util
import unittest
from pathlib import Path

try:
    import numpy as np
except ImportError:  # `mise run microfreak:test` provides numpy
    raise unittest.SkipTest('numpy is not installed; run mise run microfreak:test')

spec = importlib.util.spec_from_file_location('audio_steps', Path(__file__).with_name('audio_steps.py'))
audio_steps = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audio_steps)

SR = 48000


def tone(note, seconds, harmonics=12, gate=None):
    """A sawtooth-like note: harmonics at 1/h amplitude, 3 ms attack, fast release."""
    t = np.arange(int(seconds * SR)) / SR
    f0 = audio_steps.midi_to_hz(note)
    wave = sum(np.sin(2 * np.pi * f0 * h * t) / h for h in range(1, harmonics + 1) if f0 * h < SR / 2)
    envelope = np.minimum(1, t / 0.003)
    if gate is not None:
        envelope = envelope * np.where(t < gate, 1.0, np.exp(-(t - gate) / 0.01))
    return 0.3 * wave * envelope


def sequence(pattern, step, latency, lead=0.4, tail=0.3):
    """Place each step's notes on a grid that starts `lead + latency` seconds in."""
    audio = np.zeros(int((lead + latency + step * len(pattern) + tail) * SR))
    for index, notes in enumerate(pattern):
        start = int((lead + latency + index * step) * SR)
        for note in notes:
            sound = tone(note, step, gate=step * 0.6)
            audio[start:start + len(sound)] += sound
    rng = np.random.default_rng(7)
    return audio + rng.normal(0, 1e-4, len(audio))


class PitchTests(unittest.TestCase):
    def test_yin_finds_low_and_high_fundamentals(self):
        for note in (24, 36, 48, 60, 81):
            f0, aperiodicity = audio_steps.yin(tone(note, 0.11), SR)
            self.assertIsNotNone(f0, note)
            self.assertLess(abs(audio_steps.hz_to_midi(f0) - note), 0.1, note)
            self.assertLess(aperiodicity, 0.2)

    def test_yin_returns_none_for_noise(self):
        noise = np.random.default_rng(3).normal(0, 0.1, 5000)
        f0, aperiodicity = audio_steps.yin(noise, SR)
        self.assertIsNone(f0)
        self.assertGreater(aperiodicity, 0.5)

    def test_chord_notes_finds_a_triad_and_a_single_note(self):
        triad = tone(60, 0.11) + tone(64, 0.11) + tone(67, 0.11)
        self.assertEqual({n['midi'] for n in audio_steps.chord_notes(triad, SR)}, {60, 64, 67})
        self.assertEqual([n['midi'] for n in audio_steps.chord_notes(tone(55, 0.11), SR)], [55])

    def test_chord_notes_finds_four_spread_notes(self):
        chord = tone(48, 0.11) + tone(55, 0.11) + tone(64, 0.11) + tone(70, 0.11)
        self.assertEqual({n['midi'] for n in audio_steps.chord_notes(chord, SR)}, {48, 55, 64, 70})


class StepTests(unittest.TestCase):
    pattern = [[48], [55], [], [60], [64, 67, 72], [], [43], [52]]
    step = 0.125
    latency = 0.023

    def analyse(self):
        audio = sequence(self.pattern, self.step, self.latency)
        nominal = [0.4 + i * self.step for i in range(len(self.pattern))]
        times, flux = audio_steps.onset_envelope(audio, SR)
        triggers = [t for t, notes in zip(nominal, self.pattern) if notes]
        lag = audio_steps.estimate_lag(times, flux, triggers, 0.05)
        noise = float(np.sqrt(np.mean(audio[:int(0.3 * SR)] ** 2)))
        results = audio_steps.analyse_steps(audio, SR, [t + lag for t in nominal], self.step, noise,
                                            audio_steps.onset_threshold(flux), times, flux)
        return lag, results

    def test_lag_recovers_the_recording_latency(self):
        lag, _ = self.analyse()
        self.assertAlmostEqual(lag, self.latency, delta=0.004)

    def test_steps_report_onsets_rests_and_pitches(self):
        _, results = self.analyse()
        self.assertEqual([r['onset'] for r in results], [bool(notes) for notes in self.pattern])
        for notes, result in zip(self.pattern, results):
            if len(notes) == 1:
                self.assertEqual(result['midi'], notes[0])
                self.assertLess(abs(result['cents']), 15)
        self.assertTrue({64, 67, 72} <= {c['midi'] for c in results[4]['chord']})
        self.assertFalse(results[2]['sounding'])


if __name__ == '__main__':
    unittest.main()
