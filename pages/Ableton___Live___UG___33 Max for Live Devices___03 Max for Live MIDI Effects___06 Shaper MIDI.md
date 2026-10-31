logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/33 Max for Live Devices/03 Max for Live MIDI Effects]]
prev:: [[Ableton/Live/UG/33 Max for Live Devices/03 Max for Live MIDI Effects/05 Note Echo]]
- # [33.3.6 Shaper MIDI](https://www.ableton.com/en/live-manual/12/max-for-live-devices/#shaper-midi)
	- ![The Shaper MIDI Effect](https://ableton-production.imgix.net/live-manual/12/MaxShaperMIDIL12.png?auto=&w=320)
	- A modulator with a breakpoint envelope that restarts on every MIDI note and can respond to velocity — unlike the audio-effect Shaper.
	- Mapping, Mod, polarity and Min/Max work as in the audio-effect modulators.
	- Drawing:
		- click to add a breakpoint; `Cmd`-click (Mac) or `Ctrl`-click (Windows) adds the single **sustain breakpoint**, drawn larger. The envelope holds there while the note is held.
			- ![Use a Sustain Breakpoint to Keep the Envelope at a Specific Level While a Note is Held](https://ableton-production.imgix.net/live-manual/12/MaxShaperMIDISustainL12.png?auto=&w=320)
		- `Option`-drag (Mac) or `Alt`-drag (Windows) between points to curve a segment; `Shift`-click a point to delete it
		- **Clear** erases the envelope; six presets next to it start a new one
		- **Grid** and **Snap** as in Shaper
	- The small display shows the output; its LED flashes on each trigger.
	- **Jitter** adds randomness; **Smooth** softens sudden changes.
	- **Velocity** — how much note velocity scales the envelope; 0% ignores velocity
	- **Offset** — moves the center of the output up or down
		- ![You Can Shift the Center Point of the Envelope Output Using Offset](https://ableton-production.imgix.net/live-manual/12/MaxShaperMIDIOffsetL12.png?auto=&w=320)
	- **Loop** — repeats the envelope at **Rate** while a note is held, ignoring the sustain breakpoint
	- **Rate** — in Hz or synced divisions
	- **Depth** — modulation amount for all targets
	- **Echo** — how much each echo of the envelope feeds the next; **Time** — the echo interval
		- ![Use the Echo and Time Controls to Add Echoes to the Envelope Output](https://ableton-production.imgix.net/live-manual/12/MaxShaperMIDIEchoL12.png?auto=&w=320)