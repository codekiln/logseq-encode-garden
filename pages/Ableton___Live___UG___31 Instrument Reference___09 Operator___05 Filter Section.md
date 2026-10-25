logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/31 Instrument Reference/09 Operator]]
prev:: [[Ableton/Live/UG/31 Instrument Reference/09 Operator/04 Envelopes]]
next:: [[Ableton/Live/UG/31 Instrument Reference/09 Operator/06 Global Controls]]
- # [31.9.5 Filter Section](https://www.ableton.com/en/live-manual/12/live-instrument-reference/#filter-section-2)
	- The filter shapes the oscillators' output; with classic waveforms Operator can work as a subtractive synth.
		- ![Operator's Filter Display and Shell Parameters](https://ableton-production.imgix.net/live-manual/12/OperatorFilterL12.png)
	- Types: low-pass, high-pass, band-pass, notch and **Morph**, at 12 or 24 dB, with circuit models made with Cytomic:
		- **Clean** — efficient, same as EQ Eight's filters; all types.
		- **OSR** — state variable with a hard-clipping diode, from a rare British mono synth; all types.
		- **MS2** — Sallen-Key with soft clipping, from a famous Japanese semi-modular; low- and high-pass.
		- **SMP** — a custom design between MS2 and PRD; low- and high-pass.
		- **PRD** — a ladder with no resonance limiting, from an American dual-oscillator mono synth; low- and high-pass.
	- **Frequency** and **Resonance**; non-Clean low-, high- and band-pass add **Drive**.
	- **Morph** sweeps low-pass → band-pass → high-pass → notch → low-pass; its context menu snaps to each.
	- The display switches between filter envelope and response curve; drag the curve to set cutoff and resonance.
	- Cutoff modulation: **Freq < Vel**, **Freq < Key**, **Envelope**, and the LFO via Dest. A "FIL" or Dest. B. **Play by Key** in the Frequency context menu sets Freq < Key to 100% and cutoff to 466 Hz.
	- **Shaper** curve with **Shp. Drive** and **Dry/Wet** after the filter; 0% wet bypasses it.
