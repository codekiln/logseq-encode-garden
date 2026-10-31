logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/30 MIDI Effect Reference]]
prev:: [[Ableton/Live/UG/30 MIDI Effect Reference/02 CC Control]]
next:: [[Ableton/Live/UG/30 MIDI Effect Reference/04 Note Length]]
- # [30.3 Chord](https://www.ableton.com/en/live-manual/12/live-midi-effect-reference/#chord)
	- ![The Chord Effect](https://ableton-production.imgix.net/live-manual/12/ChordL12.png?auto=&w=320)
	- Chord adds up to six pitches to each incoming note.
	- **Shift 1–6** each set one added pitch, up to ±36 semitones from the incoming note. Shift 1 at +4 st and Shift 2 at +7 st make a major chord on the played note. Order does not matter. An LED next to each Shift knob flashes when its note plays.
	- Two Shift controls cannot hold the same pitch; a duplicate is switched off.
	- **Learn** in the title bar sets the Shifts from a played chord: the first held key is the root and is not stored, and each further held key fills the next Shift. Hold more keys to add pitches, then turn Learn off.
	- With the **Velocity** or **Chance** toggle on, a slider under each Shift adjusts that note:
		- **Velocity** — relative to the incoming note, 1% to 200%; 100% matches it
		- **Chance** — probability, 0% to 100%, that the added note plays
	- **Strum** spreads the chord's notes over up to 400 ms. Positive values play the original note first, then Shift 1 to 6; negative values reverse that. **Play Duplicate Notes When Strumming** in the title bar's context menu allows repeated notes.
		- **Tension** — positive values start the strum slowly and speed up; negative values start fast and slow down
		- **Crescendo** — a rising (positive) or falling (negative) velocity ramp across the strum
	- **Use Current Scale** in the title bar changes Shift units from semitones to scale degrees.
	- **Send Per Note Events to Generated Notes**, in the title bar's context menu, passes MPE data to the added notes. With scale awareness on, per-note pitch bends follow the clip's scale.