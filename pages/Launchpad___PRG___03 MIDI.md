logseq-entity:: [[Logseq/Entity/Book/Section/Level 1]], [[Logseq/Entity/Series]]
up:: [[Launchpad/PRG]]
prev:: [[Launchpad/PRG/02 Bootloader]]
next:: [[Launchpad/PRG/04 Controlling the Surface]]

- # MIDI on Launchpad Pro [MK3]
	- The Launchpad presents three USB MIDI interfaces. On Windows they appear as the first, second, and third interface.
		- `LPProMK3 MIDI In/Out`: MIDI from Note, Chord, and Custom modes; external MIDI input; LED lighting in Custom Modes and Programmer Mode.
		- `LPProMK3 DIN In/Out`: MIDI passed to and from the DIN ports.
		- `LPProMK3 DAW In/Out`: DAW and similar software driving Session mode.
	- The Launchpad sends Note On (`90h`-`9Fh`) with velocity 0 as its Note Off. It accepts either Note Off (`80h`-`8Fh`) or Note On with velocity 0.
	- {{embed [[Launchpad/PRG/03 MIDI/01 Device Inquiry]]}}
	- {{embed [[Launchpad/PRG/03 MIDI/02 SysEx Format]]}}
	- {{embed [[Launchpad/PRG/03 MIDI/03 Selecting Layouts]]}}
