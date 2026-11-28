logseq-entity:: [[Logseq/Entity/Term]]

- # MIDI Program Change
	- A [[MIDI/Message]] (C0h–CFh) that selects a preset, called a program or patch, by number 0–127. Menus often show it as 1–128.
	- To reach past 128 presets, a sender first sends Bank Select on [[MIDI/CC]] 0, and 32 for the fine half, then the Program Change. [[MIDI/Bank Select and Program Change]] explains how the two work together.
	- The MicroFreak selects a preset with CC 0 and a Program Change ([[Microfreak/Q/In the Microfreak, is there any documented way to send a MIDI message that would engage sequence B?]]).
	- A MIDI clip in Ableton Live can send a bank and program change when it launches ([[Ableton/Live/UG/08 Clip View/03 Extended Clip Properties/02 MIDI Clip Bank and Program Change Controls]]).
