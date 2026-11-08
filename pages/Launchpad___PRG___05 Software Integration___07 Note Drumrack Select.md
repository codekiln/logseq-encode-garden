logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Launchpad/PRG/05 Software Integration]]
prev:: [[Launchpad/PRG/05 Software Integration/06 DAW Drumrack]]
next:: [[Launchpad/PRG/05 Software Integration/08 Note Active Colour]]

- # DAW Note / Drumrack mode select
	- Chooses whether Note mode shows the note layout or the Drumrack. Available only in DAW mode.
		- Hex: `F0h 00h 20h 29h 02h 0Eh 0Fh <Mode> F7h`
		- Decimal: `240 0 32 41 2 14 15 <Mode> 247`
	- `<Mode>`: 0 Note mode, 1 Drumrack.
	- The message does not change layout. If Note mode is showing, the change appears at once; otherwise it appears the next time Note mode is selected.
