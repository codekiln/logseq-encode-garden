logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/29 Audio Effect Reference]]
prev:: [[Ableton/Live/UG/29 Audio Effect Reference/28 Pedal]]
next:: [[Ableton/Live/UG/29 Audio Effect Reference/30 Redux]]
- # [29.29 Phaser-Flanger](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#phaser-flanger)
	- ![The Phaser-Flanger Effect](https://ableton-production.imgix.net/live-manual/12/PhaserFlangerL12.png?auto=&w=320)
	- Phaser-Flanger combines a phaser, a flanger and a doubler in one device, with two LFOs and an envelope follower.
	- Modes, chosen in the display:
		- **Phaser** — modulated all-pass filters feed a phase-shifted copy back in, creating moving notches. The display shows the notches. **Notches** sets how many; **Center** their center frequency; **Spread** their spacing (all-pass Q); **Blend** routes modulation between Center (0.0) and Spread (1.0).
		- **Flanger** — a modulated, fed-back delay gives a moving comb filter. **Time** sets the delay; in the display, moving right shortens the delay and left lengthens it.
		- **Doubler** — modulated delays imitate stacked takes. **Time** sets the delay; modulation is bipolar, so right lengthens and left shortens.
	- The title bar button unfolds the device, showing more LFO options, LFO2, the envelope follower, **Safe Bass** and an LFO display.
		- ![Phaser-Flanger](https://ableton-production.imgix.net/live-manual/12/Device_fold.png?auto=&w=24)
	- Main LFO:
		- **Freq/Rate** — in Hz or synced, chosen with the Modulation Sync buttons
		- **LFO Waveform** — Sine, Triangle (default), Saw Up, Saw Down, Rectangle, Random, Random S&H, plus **Triangle Analog** (a filtered square that changes shape and level with rate), **Triangle 8** and **Triangle 16** (stepped in 8 or 16)
		- **LFO Stereo Mode** — **Phase** (left/right offset; 180° is inverted) or **Spin** (different rates per side)
		- **Duty Cycle** — squeezes the wave toward the start (100%) or end (−100%) of its cycle, like pulse width; no effect on Random and Random S&H
	- LFO2 is always a triangle. **LFO2 Mix** blends it with the main LFO (0% main only, 100% LFO2 only); **LFO2 Freq/Rate** sets its speed, free or synced with Modulation Sync 2.
	- Global:
		- **Amount** — modulation depth for both LFOs
		- **Feedback** — output fed back for a stronger comb-filter sound; in Doubler it also keeps echoing after playback stops. **Ø** inverts it for a hollow sound. High feedback can jump in level quickly — protect ears and equipment.
		- **Env Fol** with **Envelope Amount** (negative inverts) turns input level into modulation; **Attack** and **Release** set its response.
		- **Safe Bass** — high-pass from 5 Hz to 3000 Hz that keeps the effect off the lows
		- **Output**, **Warmth** (slight distortion and filtering), **Dry/Wet** (100% on a return track)