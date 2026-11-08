logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Launchpad/PRG/05 Software Integration]]
next:: [[Launchpad/PRG/05 Software Integration/02 DAW Interface]]

- # Accessing Session Mode (Enabling / disabling DAW mode)
	- Session Mode needs DAW Mode. This message switches DAW Mode on or off; the Session button lights while DAW Mode is on.
		- Hex: `F0h 00h 20h 29h 02h 0Eh 10h <Mode> F7h`
		- Decimal: `240 0 32 41 2 14 16 <Mode> 247`
	- `<Mode>`: 0 Standalone, 1 DAW, which enables the Session and DAW Fader layouts.
	- Software should return the Launchpad to Standalone when it exits, which clears its state and leaves the device usable on its own.
