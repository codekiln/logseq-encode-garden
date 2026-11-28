tags:: [[Idea]]
date-created:: [[2026-11-28 Sat]]
see-also:: [[Launchpad/Custom/Available/3-MF-Number-Pad]], [[Launchpad/Custom/Available/2-MF-Presets]], [[Launchpad/Idea/Pick-MicroFreak-Presets-through-Live]], [[Person/codekiln/GitHub/logseq-gardener/Idea/Custom-Block-and-Static-Site-Rendering]], [[GitP/A/Log/26/11/28-Sat]]

- # Control Rendering With Ableton and MIDI
	- [[My Notes]]
		- ### The Custom Mode as an 8x8 display
			- Right now [[Launchpad/Custom/Available/3-MF-Number-Pad]] looks like a little number pad, and the way it works is powered by an Ableton Live [[Ableton/Max for Live]] device placed in a track. We can do arbitrary things with Max for Live devices.
			- It occurred to me that it would be really cool if we treated the Custom Mode as a very, very limited display that has an 8x8 pixel grid. The pixel grid does need to be configured ahead of time in [[Novation/Components]]: each pad has to have a certain on color and off color, and we have to decide ahead of time whether it's a toggle or a momentary trigger.
		- ### A number pad with presets around it
			- My main idea was that the center 4x4 grid could function as a number pad, and a lot of the empty pads that are unassigned around it could be presets, sort of like [[Launchpad/Custom/Available/2-MF-Presets]].
			- But Custom Mode 2 does a literal translation, at least I think it does. Using Max for Live or some other Ableton customization method, I might make the Custom Mode more interactive. For example, I might have arrow keys in the lower right corner, and presets stored around the edges.
		- ### A game?
			- Would it be theoretically possible to create a little game using nothing but a Launchpad Custom Mode? Can Max for Live plus Novation Components let me turn any pad on and off at will, so that I could use six of them as interface buttons and the rest as pixels?
	- [[AI/Response]]
		- ## Short answer
			- Probably yes for the 64 grid pads, and that is what Custom Modes 7 and 8 ship for. The pads you light have to be Midi Note pads in Components, and Live reaches them through a MIDI track whose MIDI To is the Launchpad. The edge buttons are less certain. Nothing below has been tried on the hardware.
		- ## What the documentation supports
			- A Custom Mode pad takes a colour from a Note On sent to the Launchpad's MIDI port: the note number picks the pad and the velocity picks one of 128 palette colours. Channel 1 is static, 2 flashing, 3 pulsing ([[Launchpad/PRG/04 Controlling the Surface/01 Lighting LEDs]]).
			- Factory Custom Modes 7 and 8 exist for this. Mode 8 has all 64 pads as notes 11 to 88, numbered like Programmer Mode, with the pads unlit until something lights them ([[Launchpad/PRG/05 Software Integration/12 Factory Custom Modes]], [[Launchpad/UG/08 Custom Modes/05 Lighting Pads with External MIDI]]).
			- One SysEx message can set up to 106 LEDs at once, each with a palette colour or a full RGB value, and its LED numbers are the Programmer Mode numbers "whatever layout is selected" ([[Launchpad/PRG/04 Controlling the Surface/06 LED Lighting SysEx]]). That would redraw a whole frame in one message, and it might reach the edge buttons too.
		- ## How a display would work
			- Components holds the layout: which pads exist, the note each one sends, and its idle colour. The idle colours are what the grid shows before Live has sent anything, so they work as a fallback picture, such as the plain number pad.
			- The Max for Live device holds the meaning. A press arrives as a note; the device updates its state and works out the colour every pad should show.
			- A second MIDI track sends the colours back. A device's MIDI output goes to its own track's output, which in [[Launchpad/Custom/Available/3-MF-Number-Pad]] feeds the MicroFreak, so the lights need a track whose MIDI To is `Launchpad Pro MK3 (LPProMK3 MIDI)`. [[Launchpad/Idea/Pick-MicroFreak-Presets-through-Live]] sketches this as `MF picker lights`.
			- Each tick, the device compares the new frame to the last one and sends a Note On only for the pads that changed.
			- Every pad should be [[Launchpad/Custom/Pad/Mode/Momentary]]. A [[Launchpad/Custom/Pad/Mode/Toggle]] pad keeps its own on/off state on the Launchpad, which can disagree with what the device thinks the pad is. A held pad still shows the mode's On colour while your finger is on it, so a press briefly covers the pixel underneath.
		- ## The number pad with presets around it
			- A 4x4 number pad in the centre, a ring of preset pads around the edge, and arrows in the lower right corner.
			- | |1|2|3|4|5|6|7|8|
			  |---|---|---|---|---|---|---|---|---|
			  |1|🟨|🟦|🟫|🟨|🟦|🟨|🟫|🟦|
			  |2|🟦|⬛|⬛|⬛|⬛|⬛|⬛|🟨|
			  |3|🟨|⬛|⬜ 7|⬜ 8|⬜ 9|🟧 ⌫|⬛|🟫|
			  |4|🟫|⬛|⬜ 4|⬜ 5|⬜ 6|🟧 ↩|⬛|🟦|
			  |5|🟦|⬛|⬜ 1|⬜ 2|⬜ 3|🟧 ★|⬛|🟨|
			  |6|🟨|⬛|🟥 C|⬜ 0|🟩 E|🟩 E|⬛|🟦|
			  |7|🟦|⬛|⬛|⬛|⬛|⬛|🟪 ▲|⬛|
			  |8|🟫|🟨|🟦|🟨|⬛|🟪 ◀|🟪 ▼|🟪 ▶|
			- Legend
				- ⬜ digits, 🟥 Clear, 🟩 Enter (two pads wide), as in Custom Mode 3 today.
				- 🟧 ⌫ drops the last digit, ↩ goes back to the previous preset, ★ adds the current preset to the ring.
				- 🟨 🟦 🟫 the ring: 24 presets in their category colours. The preset playing now flashes.
				- 🟪 ▲ and ▼ step to the next or previous filled slot. ◀ and ▶ turn the ring to the next page of 24 presets.
				- ⬛ unlit.
			- The difference from [[Launchpad/Custom/Available/2-MF-Presets]] is where the preset list lives. Custom Mode 2 stores a fixed Program Change in each pad, so changing a preset means a trip to Components. Here every ring pad sends a plain note, and the device decides which preset it stands for and what colour it shows, from a table built from the `Microfreak/Preset/*` pages. Enter can also show the category colour of the number typed so far before you commit.
		- ## A game on 58 pixels
			- Six pads as buttons and the rest as pixels fits an 8x7 playfield above a control row. Snake is the simplest fit:
			- | |1|2|3|4|5|6|7|8|
			  |---|---|---|---|---|---|---|---|---|
			  |1|⬛|⬛|⬛|⬛|⬛|⬛|⬛|⬛|
			  |2|⬛|⬛|🟥|⬛|⬛|⬛|⬛|⬛|
			  |3|⬛|⬛|⬛|⬛|⬛|⬛|⬛|⬛|
			  |4|⬛|⬛|⬛|⬛|🟩|🟩|🟩|⬛|
			  |5|⬛|⬛|⬛|⬛|🟩|⬛|⬛|⬛|
			  |6|⬛|⬛|⬛|⬛|🟢|⬛|⬛|⬛|
			  |7|⬛|⬛|⬛|⬛|⬛|⬛|⬛|⬛|
			  |8|🟪 ◀|🟪 ▼|🟪 ▲|🟪 ▶|⬛|⬛|🟧 A|🟧 B|
			- 🟢 the snake's head, 🟩 its body, 🟥 the apple, 🟪 direction pads, 🟧 A starts or pauses, B restarts.
			- The device runs a timer, moves the snake each tick, and sends the few pads that changed. Pong, a falling-block game eight pads wide, and a breakout game fit the same frame. Since the pixels are note pads too, a game can also treat a press on any pixel as input.
			- A game in the Set can also do musical work: each apple could send a note to the MicroFreak, or each tick could follow Live's tempo.
		- ## Open questions for the hardware
			- Whether a pad that is unassigned in Components can be lit at all. If not, the display has to start from a mode where all 64 pads are notes, like factory Custom Mode 8, and Custom Mode 3's notes 60 to 71 would move to the 11 to 88 numbering.
			- After a held pad shows the On colour and is released, whether it goes back to the colour Live sent or to its Components colour.
			- Whether colours sent from Live survive leaving the Custom Mode and coming back.
			- Which channel lights a pad that sends on channel 16, and whether a lights track can send on channel 1 while the pads send on 16.
			- Whether a Max for Live device can send SysEx at all. If it can, one message draws a frame, and it may light the edge buttons, which do nothing in a Custom Mode ([[Launchpad/Q/Do Custom Modes have pagination for selecting more MicroFreak presets?]]).
		- ## Next steps
			- TODO Light one pad of Custom Mode 3 from Live: on a MIDI track with MIDI To `Launchpad Pro MK3 (LPProMK3 MIDI)` on channel 1, play a clip with note 60 at velocity 5 and see whether the 0 pad turns red. Then try a note for an unassigned pad.
			- TODO If that works, make a copy of Custom Mode 3 in Components with all 64 pads as Momentary Midi Notes 11 to 88 on channel 16, keeping the number pad's colours.
			- TODO Build a toy in a Max for Live device: one lit pixel that the four direction pads move around the grid.
