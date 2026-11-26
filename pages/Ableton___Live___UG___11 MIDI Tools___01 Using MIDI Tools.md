logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/11 MIDI Tools]]
next:: [[Ableton/Live/UG/11 MIDI Tools/02 Transformation Tools]]
- # [11.1 Using MIDI Tools](https://www.ableton.com/en/live-manual/12/midi-tools/#using-midi-tools)
	- MIDI Tools live in the [Clip View]([[Ableton/Live/UI/Clip-View]])'s [Transform]([[Ableton/Live/UI/Clip-View/Transform-Panel]]) and [Generate]([[Ableton/Live/UI/Clip-View/Generate-Panel]]) panels. Transformations need selected notes and replace them; MPE tools are transformations that add or change note expression, visible in the [MPE Editor]([[Ableton/Live/UI/Clip-View/MPE-Editor]]). Generators need no input and create notes.
	- Native tools are built in and fixed; Max for Live tools can be edited, built, or installed from other makers, and show under the [browser]([[Ableton/Live/UI/Browser]])'s [MIDI Tools filter group]([[Ableton/Live/UI/Browser/Filter-View/MIDI-Tools-Filter-Group]]) or the [MIDI Tool tag]([[Ableton/Live/UI/Browser/Filter-View/Content-Filter-Group/Tag/MIDI-Tool]]).
	- Pick a tool from the panel's selector and adjust it. Auto Apply, on by default, applies changes immediately; turn it off, which restores the original notes, to adjust first and then press Apply. `Cmd+Enter` (Mac) / `Ctrl+Enter` (Win) [applies from the editor]([[Ableton/Live/Keyshort/Apply-Current-MIDI-Tool-Settings]]).
		- Transform panel: [Transformation Selector]([[Ableton/Live/UI/Clip-View/Transform-Panel/Chooser/Transformation-Selector]]), [Auto Apply]([[Ableton/Live/UI/Clip-View/Transform-Panel/Button/Auto-Apply]]), [Apply]([[Ableton/Live/UI/Clip-View/Transform-Panel/Button/Apply]]), [Reset]([[Ableton/Live/UI/Clip-View/Transform-Panel/Button/Reset]])
		- Generate panel: [Generator Selector]([[Ableton/Live/UI/Clip-View/Generate-Panel/Chooser/Generator-Selector]]), [Auto Apply]([[Ableton/Live/UI/Clip-View/Generate-Panel/Button/Auto-Apply]]), [Apply]([[Ableton/Live/UI/Clip-View/Generate-Panel/Button/Apply]]), [Reset]([[Ableton/Live/UI/Clip-View/Generate-Panel/Button/Reset]])
	- Transformations act on the time selection, the note selection, or the whole loop. Generators fill the time selection or loop, keeping existing notes they don't overlap and replacing those they do.
	- With a clip scale, pitch parameters use scale degrees.
	- Undo and Redo affect notes, not tool settings; Reset returns a tool's parameters to default without touching notes.
	- {{embed [[Ableton/Live/UG/11 MIDI Tools/01 Using MIDI Tools/01 Using Max for Live MIDI Tools]]}}
