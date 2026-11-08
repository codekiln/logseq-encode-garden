logseq-entity:: [[Logseq/Entity/Book/Section/Level 1]], [[Logseq/Entity/Series]]
up:: [[Launchpad/PRG]]
next:: [[Launchpad/PRG/02 Bootloader]]

- # About this Guide
	- The guide covers the MIDI implementation that Launchpad Pro [MK3] exposes over USB: lighting LEDs and reaching the device's features from software.
	- Notation:
		- Middle C is C3, note 60. MIDI channels are numbered 1-16.
		- Bytes appear in hex with an `h` suffix and the decimal value alongside, for example status byte `90h` (144) for a channel-1 Note On.
