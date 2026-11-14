logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Launchpad/PRG/04 Controlling the Surface]]
next:: [[Launchpad/PRG/04 Controlling the Surface/02 Colour Palette]]

- # Lighting LEDs via MIDI
	- Session Mode takes colours on the DAW interface. Custom Modes and Programmer Mode take colours on the MIDI interface.
	- The channel sets the lighting behaviour:
		- Channel 1, static colour: Note `90h` (144), CC `B0h` (176)
		- Channel 2, flashing colour: Note `91h` (145), CC `B1h` (177)
		- Channel 3, pulsing colour: Note `92h` (146), CC `B2h` (178)
	- For a Note On, the note number picks the pad and the velocity picks the palette colour. For a CC, the controller number picks the pad and the value picks the colour.
	- Session Mode layout, decimal (left) and hex (right). Numbers are notes unless marked CC.
		- ![Session Mode layout](../assets/.remote/logseq-encode-garden/Launchpad___PRG___04-Controlling-the-Surface___01-Lighting-LEDs___Asset___Session-layout.png)
	- The Session layout uses the same numbers as [[Launchpad/PRG/05 Software Integration/11 Programmer Layout]].
