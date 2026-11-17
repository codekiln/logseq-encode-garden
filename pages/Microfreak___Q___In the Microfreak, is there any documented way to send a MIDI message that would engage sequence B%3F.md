logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Microfreak/Sequence/Research]], [[Microfreak/Q/In the Microfreak, how can I copy a sequence from sequence A to sequence B?]]

- # In the [[Microfreak]], is there any documented way to send a MIDI message that would engage sequence B?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [[Microfreak/UG/13 Sequencer/01 Use/01 Select & Play]] and [[Microfreak/UG/21 Appendix D - CC Values]], the garden's copy of the Arturia MicroFreak user guide
		- **Short answer:** no. The user guide selects pattern A or B only with the A and B icons on the panel, and its list of MIDI CCs has no control for the pattern.
		- **What the guide documents:** Shift + Seq turns the icon strip into Tie/Rest, A, B, Record/Stop and Play/Stop ([[Microfreak/UG/13 Sequencer/01 Use]]). Pressing A or B loads that pattern, also during playback, and Shift + A or B reloads the saved pattern.
		- **What MIDI reaches:** the guide's CCs that touch the sequencer are ARP/SEQ rate free (91) and sync (92). On my instrument, CC 0 with a program change selects a preset, which always starts on pattern A, and MIDI Start with Clock plays the selected pattern.
		- **Tried on my instrument and not documented anywhere:** none of these switched to B ([[Microfreak/Sequence/Research]], section Pattern B):
			- Song Select 0, 1 and 2, before Start and during playback
			- every CC from 1 to 119 sent during playback, except 32 and 64
			- swapping trailer values 10 and 11 in a stored preset, which [Freakout's SysEx notes](https://github.com/kmorrill/freakout/blob/main/docs/microfreak-sysex.md) also record as failing
			- writing the unnamed global settings 0x2C, 0x48 and 0x4B: the instrument ignored the writes
		- **Freakout's firmware reading:** Freakout traced the firmware's SysEx operations and found none that reads or writes the active Sequence A/B ([Freakout's SysEx notes](https://github.com/kmorrill/freakout/blob/main/docs/microfreak-sysex.md)).
		- **Not tried:** writing the unnamed global settings 0x00–0x1F. What the firmware does with a write there is unknown, so it was left alone.
		- **Ways around it:**
			- Select the slot, press B on the panel, then play it from the Mac without reselecting: `mise run microfreak:audition --slot N --no-select` ([[Microfreak/CLI/Audition a sequence]]).
			- Put the steps meant for B into pattern A of a copy in another slot and play that slot. Slot 446 holds slot 445's pattern B this way, and it played as written.
		- A web search on 2026-11-17 found no Arturia page or forum post describing a MIDI message for pattern B.
