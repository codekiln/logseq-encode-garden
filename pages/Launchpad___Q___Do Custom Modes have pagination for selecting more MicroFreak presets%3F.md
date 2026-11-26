logseq-entity:: [[Logseq/Entity/Question]]
up:: [[Launchpad/Custom]]
see-also:: [[Launchpad/Q/Can Custom Mode select MicroFreak presets by bank and program change?]]

- # Do [[Launchpad]] Custom Modes have pagination for selecting more [[Microfreak]] presets?
	- The Launchpad Pro has eight Custom Modes, picked from the bottom row, and the arrow buttons do nothing in a Custom Mode. With Custom Mode 1 kept for controlling [[Ableton/Live]], Custom Modes 2 to 8 have 448 pads, 64 in each, for selecting MicroFreak presets.
	- ## [[AI Answer]]
		- **Short answer:** No. Each Custom Mode is a single 8 × 8 page, and Novation documents no button that pages through a Custom Mode or adds a ninth one. Pads alone also fall short of 448 presets: a Program Change pad sends one program number from 0 to 127 and no bank, so 448 program pads reach at most 128 presets. Four bank select pads and 128 program pads, spread over three Custom Modes, reach all 512 MicroFreak slots, with a slot in another bank taking two presses.
		- ### Choosing a Custom Mode
			- [[Answer/Official]] from Novation's [Launchpad Pro MK3 interface guide](https://userguides.novationmusic.com/hc/en-gb/articles/25494530115346-Launchpad-Pro-MK3-interface): the Launchpad Pro has eight Custom Modes. The Custom button opens the last one used, and the Track Select buttons below the grid choose among the eight ([[Launchpad/UG/08 Custom Modes/02 Default Custom Modes]]).
			- The user guide gives the arrow buttons work in Session, Note, Drum and Sequencer modes, and none in a Custom Mode. [[Launchpad/UI/Area/1-Left/1-Up-Button]] lists what the Up button does in each mode.
			- Shift with Custom sets each Custom Mode's master MIDI channel ([[Launchpad/UG/08 Custom Modes/03 Master MIDI Channel]]). A pad set to Global Channel in Components sends on that channel, so the same pads can be pointed at another device. It adds no presets on one MicroFreak.
			- Novation's [Custom Mode Editor Guide](https://support.novationmusic.com/hc/en-gb/articles/360009860380-Launchpad-Components-Custom-Mode-Editor-Guide) describes arrow-button octave and semitone transposition in Custom Modes for the Launchpad Mini MK3 and Launchpad X only. It transposes Note messages, so Program Change pads would send the same programs even on those models.
		- ### Switching Custom Modes from software
			- [[Answer/Official]] from Novation's [Launchpad Pro MK3 Programmer's Reference](https://fael-downloads-prod.focusrite.com/customer/prod/s3fs-public/downloads/LPP3_prog_ref_guide_200415.pdf): the Select Layout message `F0h 00h 20h 29h 02h 0Eh 00h 03h <page> 00h F7h` shows Custom Mode 1 to 8 for `<page>` 0 to 7, and the Launchpad sends the same message whenever its view changes ([[Launchpad/PRG/03 MIDI/03 Selecting Layouts]]).
			- Software on the computer can use it to switch among the eight stored modes, for example when it hears a particular pad. The reference documents no message that writes a Custom Mode's pads, so software can switch between modes but can't add more of them; [[Novation/Components]] sends a whole mode to a slot.
		- ### What a Custom Mode holds
			- [[Answer/Official]] from the interface guide and the Custom Mode Editor Guide:
				- Each pad of the 8 × 8 grid sends a Note, a CC or a Program Change. Novation describes Custom Mode contents for the grid only.
				- A **CC Button** has a CC number, an on value, an off value, a MIDI channel and a behavior: Momentary, Toggle or Trigger ([[Launchpad/Custom/Pad/Mode]]).
				- A **Program Change** pad sends a program change on a chosen channel. Factory Custom 5 sends programs 0 to 63 and Custom 6 sends 64 to 127. The guide describes no bank setting on it.
				- A **fader** fills a whole row or column, vertical or horizontal, unipolar or bipolar, and sends a CC on a chosen channel. A unipolar fader starts low and moves to the highest value. The guides list no Program Change fader.
				- Notes, CCs, Program Changes and faders can share one Custom Mode, and each control can have its own MIDI channel.
		- ### Reaching more MicroFreak presets
			- The MicroFreak has 512 slots. Slot N is selected by CC 0 with value (N − 1) // 128, then program (N − 1) % 128 ([[Microfreak/CLI/Upload a preset]]). In a Custom Mode that is four CC Button pads on CC 0 with Trigger behavior and values 0 to 3, one per bank, plus 128 Program Change pads.
			- With the four bank pads repeated in each mode, 60 program pads fit beside them. Custom Modes 2 and 3 can then hold programs 0 to 119 and Custom Mode 4 the last eight, which reaches every slot and leaves Custom Modes 5 to 8 free. A slot in the current bank takes one press; a slot in another bank takes a bank press and then a program press.
			- A fader reaches presets only through software, because Custom Mode faders send CC. A [[Ableton/Max for Live]] device on the track that feeds the MicroFreak could turn each fader value into a bank select and a program change, so one fader could step through a list such as every Bass preset. This is untested.
			- A fader on CC 0 sent straight to the MicroFreak makes a poor bank control. It sweeps up to the highest CC value while the MicroFreak has banks 0 to 3, and a bank select changes nothing until the next program change. The CC Button pads send the exact bank values.
			- One press for any of the 512 slots needs a pad that sends a bank select and a program change together, and the editor guide lists no such control. [[Launchpad/Q/Can Custom Mode select MicroFreak presets by bank and program change?]] describes mapping a pad to a Live clip that sends both.
		- ### Still open
			- Whether the MicroFreak keeps the last bank select for later program changes. The two-press layout depends on it, and [[Microfreak/CLI/Upload a preset]] sent a bank select right before each program change.
			- How many distinct values a Custom Mode fader sends across its eight pads. That number sets how many presets one fader could step through, and Novation's guides leave it out.
