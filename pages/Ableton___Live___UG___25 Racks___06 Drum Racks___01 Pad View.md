logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/25 Racks/06 Drum Racks]]

- # [25.6.1 Pad View](https://www.ableton.com/en/live-manual/12/instrument-drum-and-effect-racks/#pad-view)
	- ![Pad View](https://ableton-production.imgix.net/live-manual/12/DrumRackPadView.png?auto=&w=320)
	- Pad View shows one pad per MIDI note (128 in all). Shift the visible 16 pads by dragging in the overview or with the arrow keys; hold `Cmd` (Mac) / `Alt` (Windows) to move one row.
	- Drop almost anything from the browser on a pad and it maps to that note: a sample makes a chain with a [[Ableton/Instrument/Simpler]]; an audio effect goes after it; another sample replaces only the Simpler and its sample, keeping effects. In Hot-Swap, `D` switches the target between the Rack and the last selected pad.
	- Dropping several samples maps them upward chromatically from the pad. `Cmd`/`Alt`-dragging them layers all on one pad in a nested Instrument Rack.
	- Dragging one pad onto another swaps their notes, so existing clips play different sounds; `Cmd`/`Alt`-dragging layers both pads. See also [[Ableton/How To/Preserve Name of Clip when Dragging into Drum Rack]].
	- Receive choosers in the chain list remap notes too; chains sharing a note all fire from its pad.
	- A pad stands for a note, not a chain — every chain at any depth that receives that note:
		- an empty pad shows its note, and its General MIDI suggestion in the Status Bar;
		- a pad with one chain shows its name and gives mute, solo, preview, Hot-Swap, rename and delete;
		- a pad with several shows "Multi"; mute, solo, preview and delete affect them all.
	- With a natively supported pad controller selected in Settings → Link, Tempo & MIDI, its pads play the pads visible on screen and follow when you scroll.
