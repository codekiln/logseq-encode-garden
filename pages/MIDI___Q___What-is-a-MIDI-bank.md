logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[MIDI/Bank-Select-and-Program-Change]]

- # What is a [[MIDI]] bank?
	- ## [[AI Answer]]
		- **Short answer:** a bank is a number sent just before a [[MIDI/Program-Change]], so the program number can reach more than 128 sounds. Bank Select travels as [[MIDI/CC]] 0, CC 32, or both.
		- The MIDI standard leaves it to each receiving instrument to decide what a bank number corresponds to. [[MIDI/Bank]] has examples:
			- The Sequential OB-6 and Korg minilogue xd use banks as blocks of 100 programs.
			- The [[Microfreak]] uses them as blocks of 128 slots.
			- Roland GS modules use the bank number to pick a variation of the same instrument.
			- Yamaha XG modules use it to choose between ordinary instruments, sound effects and drum kits.
			- The Korg monologue has only 100 programs and ignores Bank Select.
		- The bank number changes no sound by itself. It takes effect at the next Program Change ([[MIDI/Q/How-do-Bank-Select-and-Program-Change-messages-work-together]]).
		- [[Answer/Official]] from [MIDI 1.0 Control Change Messages](https://midi.org/midi-1-0-control-change-messages): controller 0 is Bank Select, and controller 32 is its fine value.
