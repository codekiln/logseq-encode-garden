logseq-entity:: [[Logseq/Entity/Abbreviation]], [[Logseq/Entity/Term]]
alias:: [[MIDI/Control-Change]]

- # MIDI CC
	- **Control Change** — a [[MIDI/Message]] (B0h–BFh) that sets one controller to a value. It carries a controller number and a value, both 0–127.
	- The controller number names the control: 1 is the modulation wheel, 7 channel volume, 64 the sustain pedal, 74 brightness by default. On/off controllers such as 64 read 63 and below as off, 64 and above as on.
	- **Fine values.** Controllers 0–31 can each be paired with 32–63 for the fine half of a 0–16,383 range: 0 Bank Select with 32, 1 Modulation with 33.
	- **RPN and NRPN.** Controllers 101 and 100 (RPN) or 99 and 98 (NRPN) pick a parameter, and Data Entry, 6 and 38, sets its value. RPN 0 sets the [[MIDI/Pitch-Bend]] range.
	- **Channel mode messages.** 120–127 are reserved: All Sound Off (120), Reset All Controllers (121), Local Control (122), All Notes Off (123), Omni Off and On (124, 125), Mono (126) and Poly (127).
	- The numbers the spec leaves undefined, and so free for custom mappings, are on [[MIDI/Q/Which-MIDI-CC-numbers-are-free-for-custom-mappings]].
	- In this garden: [[Microfreak/UG/17 Ext Gear/09 MIDI CC Control]], [[Microfreak/UG/21 Appendix D - CC Values]], [[Launchpad/Custom/Available/1-Arrangement]].
	- Source: [MIDI 1.0 Control Change Messages](https://midi.org/midi-1-0-control-change-messages)
