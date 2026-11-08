logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Launchpad/PRG/04 Controlling the Surface]]
prev:: [[Launchpad/PRG/04 Controlling the Surface/04 Pulsing Colour]]
next:: [[Launchpad/PRG/04 Controlling the Surface/06 LED Lighting SysEx]]

- # Examples
	- These assume Programmer Mode.
	- Lower-left pad static red: `90h 0Bh 05h` (144 11 5). Channel 1 means static, note 11 is the lower-left pad, velocity 5 is red.
	- Upper-left pad flashing green: `91h 51h 13h` (145 81 19). Channel 2 means flashing, note 81 is the upper-left pad, velocity 19 is green.
	- Lower-right pad pulsing blue: `92h 12h 2Dh` (146 18 45). Channel 3 means pulsing, note 18 is the lower-right pad, velocity 45 is blue.
	- Turn the lower-right pad off: `90h 12h 00h` (144 18 0), or the Note Off `80h 12h 00h` (128 18 0). Either clears the pulsing colour set above.
