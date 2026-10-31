logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/34 MIDI and Key Remote/02 The Mapping Browser]]
prev:: [[Ableton/Live/UG/34 MIDI and Key Remote/02 The Mapping Browser/02 Mapping to MIDI Notes]]
next:: [[Ableton/Live/UG/34 MIDI and Key Remote/02 The Mapping Browser/04 Mapping to Relative MIDI Controllers]]
- # [34.2.3 Mapping to Absolute MIDI Controllers](https://www.ableton.com/en/live-manual/12/midi-and-key-remote-control/#mapping-to-absolute-midi-controllers)
	- Absolute controllers send values from 0 to 127. The result depends on what they are mapped to:
		- **Session View slots** — 64 and above act as Note On, 63 and below as Note Off.
		- **Track activators and device on/off switches** — a value inside the mapping's Min–Max range turns the switch on; outside it turns it off. Setting Min above Max reverses that.
		- **Other switches**, such as transport controls — 64 and above on, below 64 off.
		- **Radio buttons** — 0–127 is spread across the options.
		- **Continuous controls** — 0–127 is spread across the parameter's range.
	- Pitch bend and 14-bit absolute controllers (0–16383) work the same way, with the center at 8191/8192.