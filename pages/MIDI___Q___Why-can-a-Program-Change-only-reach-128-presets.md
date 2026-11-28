logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[MIDI/Bank-Select-and-Program-Change]]

- # Why can a [[MIDI/Program Change]] only reach 128 presets?
	- ## [[AI Answer]]
		- **Short answer:** a Program Change carries one data value, and every MIDI 1.0 data value runs from 0 to 127 ([[MIDI/Message]]). To reach more presets, a sender first picks a bank with Bank Select on [[MIDI/CC]] 0.
		- [[Answer/Official]] from [Summary of MIDI 1.0 Messages](https://midi.org/summary-of-midi-1-0-messages): Program Change is `1100nnnn 0ppppppp`, where `nnnn` is the channel and the seven `p` bits are the program number.
		- Menus often show programs as 1 to 128, one higher than the number sent.
