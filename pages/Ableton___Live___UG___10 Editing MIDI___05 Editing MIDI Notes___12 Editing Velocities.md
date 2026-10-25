logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/10 Editing MIDI/05 Editing MIDI Notes]]
prev:: [[Ableton/Live/UG/10 Editing MIDI/05 Editing MIDI Notes/11 Quantizing Notes]]
next:: [[Ableton/Live/UG/10 Editing MIDI/05 Editing MIDI Notes/13 Editing Probabilities]]
- # [10.5.12 Editing Velocities](https://www.ableton.com/en/live-manual/12/editing-midi/#editing-velocities)
	- Velocity, roughly a note's loudness, shows as color saturation: paler notes are softer. Edit it in the Velocity Editor by dragging a note's marker; the value shows in the lane header, and hovering a note highlights its marker.
	- `Shift`-click to select several markers. Drag a group to the top or bottom to make them equal, then set the value.
	- `Cmd`-drag (Mac) / `Alt`-drag (Win) a selected note vertically to change velocity without the lane. Or select a marker, type a value and press `Enter`; `Cmd` (Mac) / `Ctrl` (Win) with up and down change it by 10, with `Shift` for fine steps.
	- Velocity controls below the lanes: Randomize, with Randomization Amount setting how far values may move up or down; Ramp Start and End values spread a ramp across the selection; Velocity Deviation gives each note a range played at random each time, for example 60 with +20 plays between 60 and 80.
	- A shaded area and a dot on the marker show a deviation range; double-click the marker to reset it. With several notes, the slider shows each note's limit. `Cmd`-drag (Mac) / `Ctrl`-drag (Win) from a marker also sets the range.
	- ## 10.5.12.1 Drawing Velocities
		- In Draw Mode (`B`), draw in the Velocity Editor to set values. Drawing affects the notes within each grid step, only selected ones when there's a selection; affected notes highlight blue.
		- Turn snapping off with `Cmd+4` (Mac) / `Ctrl+4` (Win), or hold `Cmd` (Mac) / `Alt` (Win), to draw markers one by one, for a crescendo. `Option`-drag (Mac) / `Alt`-drag (Win) draws a straight line; add `Shift` for a flat one.
		- Click a piano key to select one key track's notes, then draw a ramp just for them.
	- ## 10.5.12.2 Note Off Velocity
		- The Release Velocity Editor shows Note Off velocity, the speed of releasing a key. Only some devices use it; Sampler can route it to many parameters.
