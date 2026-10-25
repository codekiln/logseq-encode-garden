logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/09 Audio Clips Tempo and Warping/02 Warping]]
prev:: [[Ableton/Live/UG/09 Audio Clips Tempo and Warping/02 Warping/02 Importing Samples]]
next:: [[Ableton/Live/UG/09 Audio Clips Tempo and Warping/02 Warping/04 Warping Short Samples]]

- # [9.2.3 Warp Markers](https://www.ableton.com/en/live-manual/12/audio-clips-tempo-and-warping/#warp-markers)
	- An [[Ableton/Warp/Marker]] pins a point in the sample, such as a transient, to a place on the timeline, to map the audio's timing or change its rhythm. Import adds some; add as many as you need.
	- Double-click the upper half of the Sample Editor to add one, or press `Cmd+I` (Mac) / `Ctrl+I` (Win) to add one at the insert marker. Move markers with the arrow keys or by dragging.
	- With a marker selected, `Shift`-drag moves the waveform under it to fine-tune the start point.
	- Double-click a marker, or select its time and press `Delete` (Mac) / `Backspace` (Win), to remove it.
	- [[Ableton/Live/UI/Control Bar/Switch/Follow]] scrolls the editor during playback; it pauses on edits.
	- ## 9.2.3.1 Transients and Pseudo-Warp Markers
		- Live finds [[Ableton/Transients]] on load: amplitude peaks where notes or beats begin, shown as small gray markers at the top of the editor, and usually good spots for Warp Markers.
		- Add or remove transients from the Create menu, or with `Cmd+Shift+I` and `Cmd+Shift+Delete` (Mac) / `Ctrl+Shift+I` and `Ctrl+Shift+Backspace` (Win). Reset Transients removes the ones you added.
		- With a time selection, Insert Warp Markers, `Cmd+I` (Mac) / `Ctrl+I` (Win), puts a marker on every transient in it, or at its ends if there are none.
		- Hovering a transient shows a gray [[Ableton/Warp/Marker/Pseudo]]. Double-click or drag it to make a real marker; if no marker follows, the clip's tempo changes. `Cmd` (Mac) / `Ctrl` (Win) also makes markers at the neighbouring transients; `Shift`-drag moves the transient itself.
	- ## 9.2.3.2 Saving Warp Markers with a Sample File
		- Warp Markers save with the Set. The Save button in the clip's title bar also stores them with the sample, so they return whenever the file is used. Only your own samples, not Core Library or Pack content.
		- A sample saved with markers isn't auto-warped, though the Warp From… commands still run Auto-Warp by hand.
