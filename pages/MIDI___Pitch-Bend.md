logseq-entity:: [[Logseq/Entity/Term]]

- # MIDI Pitch Bend
	- A [[MIDI/Message]] (E0h–EFh) that sends the position of the pitch bend wheel or lever as one value from 0 to 16,383, split across two data values.
	- 8,192 (2000h) is the center, with no bend. Lower values bend down and higher values bend up.
	- The message doesn't say how far a full bend goes; the receiver decides. A sender can set the range with RPN 0 on [[MIDI/CC]], and General MIDI makes ±2 semitones the default.
	- Pitch Bend applies to the whole channel. MPE gives each note its own channel so each can bend on its own.
