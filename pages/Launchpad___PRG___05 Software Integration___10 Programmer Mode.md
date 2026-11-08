logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Launchpad/PRG/05 Software Integration]]
prev:: [[Launchpad/PRG/05 Software Integration/09 Note Chord Buttons]]
next:: [[Launchpad/PRG/05 Software Integration/11 Programmer Layout]]

- # Programmer Mode
	- Programmer Mode is the alternative to Session Mode for scripts. Switch between Live and Programmer Mode with:
		- Hex: `F0h 00h 20h 29h 02h 0Eh 0Eh <Mode> F7h`
		- Decimal: `240 0 32 41 2 14 14 <Mode> 247`
	- `<Mode>`: 0 Live, 1 Programmer.
	- Selecting Live with this message opens the Session layout in DAW mode, or Note mode otherwise.
	- After entering Programmer Mode by SysEx the Setup menu is unreachable. To return to normal use, send a Select Layout message for any layout other than Programmer Mode.
	- To enter Programmer Mode by hand, hold Setup, press the orange bottom Scene Launch button, and release Setup. See [[Launchpad/UG/10 Setup/07 Live and Programmer Mode]].
	- The Launchpad always powers up in Live Mode.
