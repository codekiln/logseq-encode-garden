logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Launchpad/PRG/05 Software Integration]]
prev:: [[Launchpad/PRG/05 Software Integration/03 DAW Faders]]
next:: [[Launchpad/PRG/05 Software Integration/05 DAW Stop Faders]]

- # DAW Fader bank set-up
	- Set up a fader bank with:
		- Hex: `F0h 00h 20h 29h 02h 0Eh 01h <Bank> <Orientation> <Fader> [<Fader> ...] F7h`
		- Decimal: `240 0 32 41 2 14 1 <Bank> <Orientation> <Fader> [<Fader> ...] 247`
	- `<Bank>`: 0 Volumes, 1 Pans, 2 Sends, 3 Devices.
	- `<Orientation>`: 0 vertical, 1 horizontal.
	- Each `<Fader>` is four bytes, and a message may hold up to eight:
		- Index 0-7, left to right when vertical or top to bottom when horizontal
		- Type: 0 unipolar, 1 bipolar
		- CC number the fader sends
		- Colour, a palette index. Colour 0 hides the fader.
	- Example:
		- `F0h 00h 20h 29h 02h 0Eh 01h 00h 00h 00h 00h 07h 25h 01h 01h 08h 15h F7h` (240 0 32 41 2 14 1 0 0 0 0 7 37 1 1 8 21 247) sets up the Volumes bank vertically, with a turquoise unipolar fader on CC 7 in the leftmost column and a green bipolar fader on CC 8 next to it.
		- The guide follows it with `F0h 00h 20h 29h 02h 0Eh 00h 0Dh F7h` (240 0 32 41 2 14 0 13 247) to show the bank. As printed, that layout byte is `0Dh`, which the layout table names Sequencer Projects, and the page byte is missing; the Fader layout is `01h`. See [[Launchpad/PRG/03 MIDI/03 Selecting Layouts]].
	- Fader positions and colours then arrive as CCs on channels 5 and 6 of the DAW interface: [[Launchpad/PRG/05 Software Integration/02 DAW Interface]].
