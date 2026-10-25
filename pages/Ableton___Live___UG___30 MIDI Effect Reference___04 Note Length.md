logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/30 MIDI Effect Reference]]
prev:: [[Ableton/Live/UG/30 MIDI Effect Reference/03 Chord]]
next:: [[Ableton/Live/UG/30 MIDI Effect Reference/05 Pitch]]
- # [30.4 Note Length](https://www.ableton.com/en/live-manual/12/live-midi-effect-reference/#note-length)
	- ![The Note Length Effect](https://ableton-production.imgix.net/live-manual/12/NoteLengthL12.png?auto=&w=252)
	- Note Length changes the length of incoming notes, and can trigger notes from Note Off messages instead of Note On.
	- **Trigger Source** chooses Note On or Note Off.
	- With **Note On**, **Length** sets the base length and **Gate** scales it: 100% is the full Length, 200% doubles it, 50% halves it. The Time Mode toggles switch Length between milliseconds and synced divisions.
	- With **Note Off**, each note starts when the key is released, so it is delayed by its own held length. Gate and Length then apply. Three more controls appear:
		- **Release Velocity** — the mix of Note On and Note Off velocity used for the output note; leave at 0% if the keyboard sends no release velocity
		- **Decay Time** — how long the velocity takes to fall to zero from the Note On; the value reached at Note Off becomes the output velocity
		- **Key Scale** — positive values make notes below C3 longer and notes above C3 shorter; negative values reverse it
	- **Latch**:
		- with Note On, each note plays until the next Note On
		- with Note Off, a note triggers when all keys (or the sustain pedal) are released and a new Note Off arrives
		- in both cases Gate and Length are disabled; with Note Off, Release Velocity, Decay Time and Key Scale are disabled too