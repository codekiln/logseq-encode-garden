logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[MIDI/Bank-Select-and-Program-Change]]

- # How do [[MIDI]] Bank Select and [[MIDI/Program-Change]] messages work together?
	- ## [[AI Answer]]
		- **Short answer:** send Bank Select first, then Program Change. Bank Select ([[MIDI/CC]] 0) changes no sound; the instrument holds the bank number until a Program Change arrives, then loads that program from that bank.
		- **Example:** [[Microfreak]] slot 323 is bank 2, program 66. On channel 1 that is `B0 00 02`, then `C0 42`. [[Microfreak/CLI/Upload a preset]] selected slot 323 with these messages on [[2026-11-16 Mon]].
		- **Formula on the MicroFreak:** slot = bank × 128 + program + 1, with bank and program counted from 0.
		- [[Launchpad/Custom/Available/2-MF-Presets]] puts the two messages on separate pads: a white pad for the bank, then a coloured pad for the program.
