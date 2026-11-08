logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Launchpad/PRG/03 MIDI]]
prev:: [[Launchpad/PRG/03 MIDI/02 SysEx Format]]

- # Selecting layouts
	- A layout is the view shown on the surface. The device's own buttons select layouts, as does this SysEx message:
		- Hex: `F0h 00h 20h 29h 02h 0Eh 00h <layout> <page> 00h F7h`
		- Decimal: `240 0 32 41 2 14 0 <layout> <page> 0 247`
	- `<layout>` values:
		- `00h` (0) Session, selectable only in DAW mode
		- `01h` (1) Fader
		- `02h` (2) Chord
		- `03h` (3) Custom Mode
		- `04h` (4) Note / Drum
		- `05h` (5) Scale Settings
		- `06h` (6) Sequencer Settings
		- `07h` (7) Sequencer Steps
		- `08h` (8) Sequencer Velocity
		- `09h` (9) Sequencer Pattern Settings
		- `0Ah` (10) Sequencer Probability
		- `0Bh` (11) Sequencer Mutation
		- `0Ch` (12) Sequencer Micro Step
		- `0Dh` (13) Sequencer Projects
		- `0Eh` (14) Sequencer Patterns
		- `0Fh` (15) Sequencer Tempo
		- `10h` (16) Sequencer Swing
		- `11h` (17) Programmer Mode
		- `12h` (18) Settings Menu
		- `13h` (19) Custom mode Settings
	- `<page>` values:
		- `00h`-`07h` (0-7): Custom Mode views, one per Custom Mode
		- `00h`-`03h` (0-3): any Sequencer view
		- `00h`-`03h` (0-3): Fader view
		- `00h`-`04h` (0-4): Settings Menu
		- `00h` (0): every other view
	- Request the current layout with `F0h 00h 20h 29h 02h 0Eh 00h F7h` (240 0 32 41 2 14 0 247).
	- The Launchpad also sends a layout-select message whenever its view changes, so a host can follow the user's navigation.
	- > [[Note/Info]] The Sequencer Projects, Sequencer Patterns, Custom Mode, and Custom mode Settings entries only switch what the surface shows. The guide documents no message that reads or writes Project, Pattern, or Custom Mode contents.
