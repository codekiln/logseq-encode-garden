logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/31 Instrument Reference/02 Collision]]
prev:: [[Ableton/Live/UG/31 Instrument Reference/02 Collision/03 Noise Section]]
next:: [[Ableton/Live/UG/31 Instrument Reference/02 Collision/05 LFO Tab]]
- # [31.2.4 Resonator Tabs](https://www.ableton.com/en/live-manual/12/live-instrument-reference/#resonator-tabs)
	- The resonators define most of the sound. Each tab has an on switch; with both off there is no sound.
		- ![Collision's Resonators](https://ableton-production.imgix.net/live-manual/12/CollisionResonatorsL12.png)
	- **Resonance Type**:
		- **Beam** — beams of various materials and sizes.
		- **Marimba** — a Beam variant with the overtone tuning of arch-cut marimba bars.
		- **String** — strings of various materials and sizes.
		- **Membrane** — a rectangular membrane like a drum head.
		- **Plate** — a flat rectangular plate.
		- **Pipe** — a tube open at one end with an adjustable opening at the other.
		- **Tube** — a tube closed at both ends.
	- **Quality** — Eco to High, trading overtone detail for CPU. Not on Pipe or Tube.
	- **1 → 2** / **2 → 1** — copy one resonator's settings to the other.
	- **X-Y Controller** — horizontal sets decay, vertical sets Material or Radius.
	- **Decay** — internal damping.
	- **Material** — low values let lows ring longer (wood, rubber, nylon); high values let highs ring longer (glass, metal). Pipe and Tube use **Radius** instead: larger means longer decay and more sustained highs, and at extremes a pitch change.
	- **Ratio** (Membrane, Plate) — proportion of the object's two sides.
	- **Brightness** — louder highs at higher values. Not on Pipe or Tube.
	- **Inharm** — negative compresses partials downward, positive stretches them upward. Not on Pipe or Tube.
	- **Opening** (Pipe) — 0% closed at one end, 100% open at both.
	- **Hit** — strike point, center at 0% toward the edge at higher values; **Rnd** randomizes it. Not on Pipe or Tube.
	- **Note Off** — how much note-off mutes the resonance; 0% ignores it like a real marimba, 100% mutes at once.
	- **Pos. L / Pos. R** — where vibrations are picked up on each side, center to edge. Pipe and Tube are always measured at the open end.
	- Decay, Material/Radius, Inharm and Opening can be modulated in the MIDI tab.
	- ## 31.2.4.1 Tuning Section
		- ![Resonator Tuning Parameters](https://ableton-production.imgix.net/live-manual/12/CollisionTuningL12.png)
		- **Tune** in semitones and **Fine** in cents, up to ±50.
		- **Key** in the MIDI tab sets keyboard tracking: 100% is equal temperament, 200% makes each half step a whole step, negative values fall in pitch as you play higher.
		- **Pitch Env** and **Time** — a starting pitch that glides to the final pitch; velocity can scale the start.
	- ## 31.2.4.2 Mixer Section
		- ![Resonator Mixer](https://ableton-production.imgix.net/live-manual/12/CollisionMixerL12.png)
		- **Gain** and **Pan** per resonator; pan can follow note pitch.
		- **Bleed** — mixes in the dry exciter signal, which helps restore highs lost at low tuning or quality.
