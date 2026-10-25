logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/33 Max for Live Devices/03 Max for Live MIDI Effects]]
next:: [[Ableton/Live/UG/33 Max for Live Devices/03 Max for Live MIDI Effects/02 Expression Control]]
- # [33.3.1 Envelope MIDI](https://www.ableton.com/en/live-manual/12/max-for-live-devices/#envelope-midi)
	- ![The Envelope MIDI Effect](https://ableton-production.imgix.net/live-manual/12/MaxEnvelopeMIDIL12.png?auto=&w=320)
	- A modulator that drives mapped parameters with an ADSR envelope triggered by notes.
	- Mapping, Mod, polarity and Min/Max work as in the audio-effect modulators.
	- **Loop Mode**, with an LED that flashes on each trigger:
		- **Free** — triggers on every note
		- **Sync** — retriggers at the **Sync Rate** division
		- **Loop** — loops at the rate set by **Global Time**
		- **Echo** — repeats every **Env Echo Time**; **Env Feedback** sets how long the echoes last
	- **Global Time** scales the whole envelope: 1.00 matches the ADSR times, higher stretches, lower compresses.
	- **Amount** — modulation amount for all targets
	- **Attack**, **Decay**, **Sustain**, **Release**, each with a **Slope** slider for curved stages; the handles in the display can be dragged too.
	- **Velocity** — scales the envelope peak by note velocity
	- **Sustain** toggle — off makes the envelope one-shot: Attack, Decay, then Release however long the note is held