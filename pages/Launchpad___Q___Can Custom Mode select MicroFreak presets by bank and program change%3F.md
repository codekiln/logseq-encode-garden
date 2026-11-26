logseq-entity:: [[Logseq/Entity/Question]]
up:: [[Launchpad/Custom]]
see-also:: [[GitP/A/Template/LPP-Seq]], [[Microfreak/CLI/Upload a preset]]

- # Can Launchpad Custom Mode select MicroFreak presets by bank and program change?
	- ## [[AI Answer]]
		- Yes, a Custom Mode can send the messages needed for preset selection. Use a CC button to select a bank and a Program Change pad to choose a preset within that bank. This takes two pad presses when changing banks. A single pad sending both messages has not been established in the Components documentation.
		- ### Set up the controls
			- In [[Novation/Components]], create or edit a Custom Mode. Add CC Button widgets with CC number `0`, Trigger behavior, and on values `0`, `1`, `2`, and `3` for the four banks. Add Program Change widgets for the desired presets. Set their MIDI channels to the MicroFreak's input channel. Novation documents separate CC and Program Change widgets and their channel settings in its [Custom Mode editor guide](https://support.novationmusic.com/hc/en-gb/articles/360009860380-Launchpad-Components-Custom-Mode-Editor-Guide).
			- For a preset in slot `N`, select bank `(N − 1) // 128`, then program `(N − 1) % 128`. For example, slot 323 uses CC 0 value 2, followed by program 66. [[Microfreak/CLI/Upload a preset]] records a successful selection of slot 323 using those messages. The bank and program numbers here are MIDI values starting at zero; check the numbering shown in Components when setting up a pad.
			- Factory Custom 5 sends programs 0–63 and Custom 6 sends 64–127 ([[Launchpad/UG/08 Custom Modes/02 Default Custom Modes]]). A tailored layout can keep bank buttons and chosen programs together, but check and back up the current Custom Mode before replacing it.
		- ### Routing and recording
			- For a direct hardware test, connect Launchpad MIDI Out 1 to MicroFreak MIDI In using each device's appropriate adapter and a MIDI cable, and match the output channel to the MicroFreak input channel. [[Launchpad/UG/02 Getting Up and Running/05 Standalone]] describes Custom Mode output through the MIDI ports. Verify the exact cabling and channel in the current setup before changing connections.
			- The [[GitP/A/Template/LPP-Seq]] already routes Launchpad sequencer channels through Live to the MicroFreak. A Custom Mode's MIDI channel and input port must also reach the MicroFreak. Verify both messages with a MIDI monitor and check the selected preset on the MicroFreak; the existing route has not been tested with this Custom Mode.
			- Sending the messages directly changes the sound, but does not by itself establish a chapter marker in Live's Arrangement. Test what the chosen routing records. For a named, repeatable chapter marker, a separate approach is to MIDI-map a Custom pad to a Session clip that has its bank and program settings filled in. Ableton says the clip sends its bank and program when launched ([Ableton's Program Change guide](https://help.ableton.com/hc/en-us/articles/209070489-Sending-Program-Change-messages-from-Ableton-Live)). Check Live's displayed bank and program numbering against the MicroFreak before relying on it.
	- [[AI/Response]] [[2026-11-26 Thu]]
		- ### Experiment
			- #### Custom Mode 2
				- Custom Mode 2 on the Launchpad now holds `2 MF Presets`, which is also saved under My Custom Modes in [[Novation/Components]]. Reading the mode back from the Launchpad in Components showed the same pads and values.
				- Every pad sends on MIDI channel 16. The Launchpad's sequencer tracks play on channels 1 to 4, so `mf1-MIDI` to `mf4-MIDI` don't pick these messages up.
				- The top row holds four white bank pads. Each is a CC Button set to Trigger that sends CC 0, with values 0, 1, 2 and 3 from left to right.
				- Below each bank pad, starting two rows down, a column of Program Change pads holds presets from that bank. Rows count from the top of the grid.
					- | Bank pad | Row | Preset | Program | GitP sessions | Colour |
					  |---|---|---|---|---|---|
					  | 0 | 3 | [[Microfreak/Preset/016 Voidom]] | 15 | 2 | yellow |
					  | 1 | 3 | [[Microfreak/Preset/151 The Unstable]] | 22 | 2 | yellow |
					  | 1 | 4 | [[Microfreak/Preset/245 GivemeSub]] | 116 | 1 | blue |
					  | 1 | 5 | [[Microfreak/Preset/247 Laity]] | 118 | 2 | yellow |
					  | 1 | 6 | [[Microfreak/Preset/248 GrowLing]] | 119 | 1 | blue |
					  | 2 | 3 | [[Microfreak/Preset/259 Infini Pad]] | 2 | 3 | red |
					  | 2 | 4 | [[Microfreak/Preset/297 Shiny Hat]] | 40 | 1 | blue |
					  | 3 | 3 | [[Microfreak/Preset/399 FireAlarmLoBat]] | 14 | 1 | blue |
				- GitP sessions counts the [[GitP/A/Session]] days whose pages link the preset. Red marks three, yellow two and blue one; Infini Pad is the only preset with three.
			- #### What Components offers
				- Program Change: a program number counted from 0, a MIDI channel (1 to 16, or the mode's Global channel) and a colour. The pad sends its program when pressed and has no Momentary, Toggle or Trigger setting. It sends no bank select, so changing bank takes its own press.
				- CC Button: Momentary, Toggle or Trigger, a CC number, an on value, a MIDI channel and a colour. Momentary also takes an off value; Trigger sends only the on value.
				- Faders: Vertical and Horizontal, each Unipolar or Bipolar, filling a column or row. The Vertical Unipolar Fader takes a CC number, a MIDI channel and a colour, with no value range. A fader can sweep a CC; turning that sweep into bank and program messages would take something in Live, such as a Max for Live device.
				- Notes: Chromatic Keyboard, Scale Keyboard, Drum Grid and Midi Note.
				- Each pad takes its own colour from a palette of 27; one On colour serves the whole mode.
				- In the editor, Space grabs the selected widget, the arrow keys move it and Space drops it. Option-Space drops a copy. A fader dropped onto the grid removed the pads it landed on, and Undo restored them.
			- #### Live track
				- Producer Pal couldn't reach the open Set, so the track still needs adding by hand. Create a MIDI track named `LPP CM2 to MF` and set:
					- MIDI From: `Launchpad Pro MK3 (LPProMK3 MIDI)`, `Ch. 16`
					- Monitor: `In`, so messages pass while the track is unarmed
					- MIDI To: `Arturia MicroFreak (unknown mididevice)`, `Ch. 1`, the channel `LPP to MF` and the garden's MicroFreak tasks use
				- The LPProMK3 MIDI input needs Track on in Live's MIDI settings; [[Launchpad/MIDI/Port/LPProMK3 MIDI]] records it on. That page also records Note mode playing through `LPProMK3 DAW` while Live was connected, so if the track hears nothing, try that port as MIDI From.
				- Another track that listens to the Launchpad on All Channels or Ch. 16 with monitoring on would pass the same messages to its own output.
			- #### What I checked
				- The MicroFreak follows a bank select and Program Change sent from the Mac over USB. On [[2026-11-16 Mon]], CC 0 = 2 followed by program 66 on channel 1 selected slot 323, and recordings showed the sound change ([[Microfreak/CLI/Upload a preset]]). Selecting slot 35 the same way played its pattern A ([[Microfreak/CLI/Audition a sequence]]). Those messages went straight to the MicroFreak, with no Live track in between.
				- I sent nothing to the MicroFreak today. `sendmidi` and `receivemidi` aren't installed, and a program change would replace whatever sound is loaded.
				- No garden task reads which preset the MicroFreak is playing. The `microfreak:*` tasks read saved slots, and [[Microfreak/CLI/Audition a sequence]] notes that no SysEx message reports the selected preset. The MicroFreak's screen is the check.
				- Untested: a pad press, whether Live passes a Program Change from `LPP CM2 to MF` to the MicroFreak, and what a clip recorded on that track holds.
			- #### What Live records
				- A MIDI clip recorded from a controller keeps its CCs as MIDI Ctrl clip envelopes ([Using MIDI CC in Live](https://help.ableton.com/hc/en-us/articles/360010389480-Using-MIDI-CC-in-Live)). Live sends its own bank and sub-bank changes as CC 0 and CC 32, so those two controllers are missing from the MIDI Ctrl chooser ([Sending Program Change messages from Ableton Live](https://help.ableton.com/hc/en-us/articles/209070489-Sending-Program-Change-messages-from-Ableton-Live)). A recorded bank press would have no envelope to show it.
				- Ableton documents Program Change only as a clip setting sent at launch ([[Ableton/Live/UG/08 Clip View/03 Extended Clip Properties/02 MIDI Clip Bank and Program Change Controls]]). Chapter 19 of the Live 12 manual and those help articles say nothing about recording an incoming Program Change. A December 2024 [forum thread](https://forum.ableton.com/viewtopic.php?p=1830381) asks whether Program Changes pass through unrecorded and doesn't settle it.
				- On that evidence, pad presses would change the MicroFreak's preset and leave nothing readable in the Set. Step 2 of [#501 Record which MicroFreak preset is playing in GitP Sets, from Launchpad Custom Modes](https://github.com/codekiln/logseq-encode-garden/issues/501) probably needs the Session-clip alternative under Routing and recording. Recording a clip on `LPP CM2 to MF` while pressing pads would show whether Live keeps anything.
			- #### Test
				- 1. Add `LPP CM2 to MF` as above. On the Launchpad, press Custom, then the second button of the bottom row to open Custom Mode 2.
				- 2. Press the third white pad in the top row (bank 2), then the red pad two rows below it. The MicroFreak should show 259 Infini Pad.
				- 3. Press the second white pad (bank 1), then the yellow pad two rows below it. The MicroFreak should show 151 The Unstable. To see what Live keeps, arm the track and record a Session clip during this step, then open the clip.