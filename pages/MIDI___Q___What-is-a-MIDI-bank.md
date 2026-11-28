logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[MIDI/Bank-Select-and-Program-Change]]

- # What is a [[MIDI]] bank?
	- ## [[AI Answer]]
		- **Short answer:** a group of up to 128 presets. A [[MIDI/Program Change]] can only count from 0 to 127, so an instrument with more presets splits them into banks, and a Bank Select message on [[MIDI/CC]] 0 says which bank the next Program Change reads from.
		- What a bank holds is up to the instrument. On the [[Microfreak]], the four banks are ranges of its 512 slots: bank 0 is slots 1 to 128, bank 1 is 129 to 256, bank 2 is 257 to 384 and bank 3 is 385 to 512.
		- The wavetable and sample banks in MIDI Control Center are folders, unrelated to Bank Select ([[Microfreak/UG/14 Config/02 MIDI Control Center/02 Wavetables Tab/01 Management]]).
		- [[Answer/Official]] from [MIDI 1.0 Control Change Messages](https://midi.org/midi-1-0-control-change-messages): controller 0 is Bank Select, and controller 32 is its fine value.
