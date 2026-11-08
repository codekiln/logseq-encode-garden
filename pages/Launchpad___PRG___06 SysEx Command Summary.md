logseq-entity:: [[Logseq/Entity/Book/Section/Level 1]], [[Logseq/Entity/Series]]
up:: [[Launchpad/PRG]]
prev:: [[Launchpad/PRG/05 Software Integration]]
next:: [[Launchpad/PRG/07 Mode Hierarchy]]

- # SysEx command summary
	- All commands share the header `F0h 00h 20h 29h 02h 0Eh` (240 0 32 41 2 14).
	- The guide's summary table:
		- `00h` (0) Select Layout: `<layout>`
		- `01h` (1) DAW Fader Setup: bank, `<orientation>`, then repeatable `<fader>` entries. The table prints the bank byte as `00h`.
		- `03h` (3) LED Lighting: repeatable `<colourspec>`
		- `0Eh` (14) Live/Programmer Toggle: `<mode>`
		- `10h` (16) DAW / Standalone: `<mode>`
		- `19h` (25) Stop Faders for Bank: `<bank index>`
	- Commands documented in the body but missing from the table:
		- `0Fh` (15) DAW Note / Drumrack mode select: [[Launchpad/PRG/05 Software Integration/07 Note Drumrack Select]]
		- `17h` (23) DAW Note mode Active colour: [[Launchpad/PRG/05 Software Integration/08 Note Active Colour]]
	- The table also omits Select Layout's `<page>` byte and trailing `00h`; the full form is in [[Launchpad/PRG/03 MIDI/03 Selecting Layouts]].
	- No command reads or writes sequencer Projects, Patterns, Scenes, or steps, uploads Custom Modes, or backs up or restores device data.
