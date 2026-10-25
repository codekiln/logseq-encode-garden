logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/31 Instrument Reference/01 Analog]]
prev:: [[Ableton/Live/UG/31 Instrument Reference/01 Analog/01 Architecture and Interface]]
next:: [[Ableton/Live/UG/31 Instrument Reference/01 Analog/03 Noise Generator]]
- # [31.1.2 Oscillators](https://www.ableton.com/en/live-manual/12/live-instrument-reference/#oscillators)
	- Modeled oscillators, so no aliasing. Each has an on switch (Osc 1, Osc 2) and a level slider.
		- ![Display and Shell Parameters for the two Oscillators](https://ableton-production.imgix.net/live-manual/12/AnalogOscillatorsL12.png)
	- **F1/F2** — balance between Filter 1 and Filter 2; centered sends equally.
	- **Shape** — sine, sawtooth, rectangular or white noise. Rectangular enables **Pulse Width** (100% is a square with odd harmonics only; low values sound thin), which an LFO can modulate.
	- **Octave**, **Semi**, **Detune** — tuning; Detune moves in cents, up to 300 cents either way.
	- **Pitch Mod** — LFO amount, and **Key**: how far pitch follows the keyboard. 100% is equal temperament, 0% ignores note pitch. C3 always plays the same frequency, so oscillators with different Key values drift apart away from C3.
	- **Pitch Env** — **Initial** pitch and the **Time** to glide to the final pitch.
	- **Sub/Sync** — Sub adds an oscillator an octave down (square for saw or rectangle, sine for sine, off for noise) at a set **Level**. Sync restarts the waveform from a hidden oscillator whose rate rises with **Ratio**; 0% has no effect. Mapping Ratio to a mod wheel is a suggested use.
