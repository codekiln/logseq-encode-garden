logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/31 Instrument Reference/10 Sampler]]
prev:: [[Ableton/Live/UG/31 Instrument Reference/10 Sampler/06 The Sample Tab]]
next:: [[Ableton/Live/UG/31 Instrument Reference/10 Sampler/08 The Filter-Global Tab]]
- # [31.10.7 The Pitch/Osc Tab](https://www.ableton.com/en/live-manual/12/live-instrument-reference/#the-pitchosc-tab)
	- ![The Pitch/Osc Tab](https://ableton-production.imgix.net/live-manual/12/SamplerPitchTabL12.png)
	- ## 31.10.7.1 The Modulation Oscillator (Osc)
		- One modulation oscillator per voice performs **FM** or **AM** on the samples; it is never heard directly. Subsonic AM varies volume; audible AM creates composite waves.
		- 21 waveforms in **Type**, a loopable amplitude envelope with the usual levels, and:
			- **Volume** — modulation depth; **Vol < Vel** scales it with velocity.
			- **Fixed** with **Freq** × **Multi** — a constant frequency.
			- **Coarse** (0.125–48) and **Fine** (0–1000) — tuning when not fixed.
	- ## 31.10.7.2 The Pitch Envelope
		- A multi-stage envelope on the sample's pitch, and the modulation oscillator's; drag breakpoints or use sliders. **Amount** sets its range in semitones.
		- Global controls on the right:
			- **Spread** — two detuned voices per note; doubles CPU.
			- **Transp** (semitones) and **Detune** (cents).
			- **Zn Shft** — shifts which key zone plays without changing pitch, for interesting multisample artifacts.
			- **Glide** — Glide is monophonic, Portamento polyphonic; **Time** sets duration.
