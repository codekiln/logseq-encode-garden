logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/31 Instrument Reference/02 Collision]]
prev:: [[Ableton/Live/UG/31 Instrument Reference/02 Collision/05 LFO Tab]]
next:: [[Ableton/Live/UG/31 Instrument Reference/02 Collision/07 Sound Design Tips]]
- # [31.2.6 MIDI/MPE Tab](https://www.ableton.com/en/live-manual/12/live-instrument-reference/#midimpe-tab)
	- Maps pitch bend (including per-note), mod wheel, pressure and slide to two destinations each, with amounts.
		- ![Collision's MIDI/MPE Tab](https://ableton-production.imgix.net/live-manual/12/CollisionMIDIMPEL12.png)
	- Key and Vel sliders let note pitch and velocity modulate further Mallet, Noise, resonator and LFO parameters.
	- ## 31.2.6.1 The Global Section
		- ![Collision's Global Section](https://ableton-production.imgix.net/live-manual/12/CollisionGlobalL12.png)
		- **Voices** — maximum polyphony.
		- **Retrig.** — retriggers a playing note instead of adding a voice, saving CPU.
		- **Structure** — 1 > 2 (serial): both exciters feed Resonator 1, whose mono mix also feeds Resonator 2 while Resonator 1 reaches its own mixer in stereo. 1 + 2 (parallel): the exciter mix feeds both resonators.
		- **Volume** — overall output.
