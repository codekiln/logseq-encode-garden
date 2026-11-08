logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Launchpad/PRG/05 Software Integration]]
prev:: [[Launchpad/PRG/05 Software Integration/04 DAW Fader Bank Setup]]
next:: [[Launchpad/PRG/05 Software Integration/06 DAW Drumrack]]

- # DAW Stop Fader for Bank
	- Stops any fader in a bank that is currently moving.
		- Hex: `F0h 00h 20h 29h 02h 0Eh 19h <Bank> F7h`
		- Decimal: `240 0 32 41 2 14 25 <Bank> 247`
	- `<Bank>`: 0 Volumes, 1 Pans, 2 Sends, 3 Devices.
