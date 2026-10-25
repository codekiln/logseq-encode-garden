logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/12 Editing MPE]]
prev:: [[Ableton/Live/UG/12 Editing MPE/01 Viewing MPE Data]]
next:: [[Ableton/Live/UG/12 Editing MPE/03 Drawing Envelopes]]

- # [12.2 Editing MPE Data](https://www.ableton.com/en/live-manual/12/editing-mpe/#editing-mpe-data)
	- Click a note while the Note Expression tab is open to bring its Pitch, Slide and Pressure envelopes forward; Velocity and Release Velocity appear as markers. Other notes are greyed out.
		- ![A selected note showing its expression envelopes](https://ableton-production.imgix.net/live-manual/12/MPESelectedNote.png?auto=&w=320)
	- ## Breakpoints and segments
		- Click a line segment to add a breakpoint; click a breakpoint to delete it. Values show while creating, hovering or dragging.
		- Right-click a breakpoint → Edit Value to type an exact value; right-click a preview breakpoint → Add Value to create one at an exact value.
		- Drag a breakpoint or segment to move it. Selected breakpoints move together.
		- `Option`-drag (Mac) / `Alt`-drag (Windows) a segment to curve it; double-click with the same modifier to straighten it.
			- ![A curved envelope segment](https://ableton-production.imgix.net/live-manual/12/MPECurvedSegment.png?auto=&w=320)
		- Hold `Shift` while dragging to lock to one axis, or to fine-tune vertically.
		- Dragging a breakpoint horizontally over its neighbour removes the neighbour.
	- ## Grid
		- The grid is off by default in this tab and its settings are saved with the clip, separate from the other tabs. Turn it on with Snap to Grid or `Cmd+4` (Mac) / `Ctrl+4` (Windows).
	- ## Whole-note edits
		- Slide, Pressure, Velocity and Release Velocity envelopes can be scaled across the whole note: click outside the note, hover until the envelope turns blue, then drag up or down. Pitch can't be scaled this way.
		- `Cmd+A` / `Ctrl+A` on an envelope selects all its breakpoints so they can be shifted by the same amount.
		- Moving or stretching a note moves or stretches its expression with it.
		- Pitch breakpoints snap to the nearest semitone while holding `Cmd` (Mac) / `Alt` (Windows) with the grid off.
		- Pitch envelopes hide when Fold is on; `Z` zooms to fit the pitch bend in the time selection; Clear All Envelopes in the context menu removes a selected note's expression.
