logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/38 Computer Audio Resources/01 Managing the CPU Load]]
prev:: [[Ableton/Live/UG/38 Computer Audio Resources/01 Managing the CPU Load/03 CPU Load from Tracks and Devices]]
- # [38.1.4 Track Freeze](https://www.ableton.com/en/live-manual/12/computer-audio-resources-and-strategies/#track-freeze)
	- **Freeze Track** renders every Session and Arrangement clip on a track to a sample file, so playback stops recomputing its devices and clip settings. Run it from the Edit menu, a track or clip context menu, or `Cmd+Option+Shift+F` (Mac) / `Ctrl+Alt+Shift+F` (Win).
		- ![A Frozen Track in the Arrangement View](https://ableton-production.imgix.net/live-manual/12/FrozenArrangementTrackL12.png)
	- Only tracks holding clips can be frozen, so Group Tracks, return tracks and the Main track cannot. Tracks using External Audio Effect or External Instrument freeze in real time.
	- A frozen track's device and clip settings are locked until **Unfreeze Track**. **Bounce Track in Place** commits a track to new audio for good, and also works on Group Tracks.
	- Still available on frozen tracks: clip launching, volume, pan and sends, and also:
		- cutting, copying, pasting, duplicating and trimming clips
		- drawing mixer automation and mixer clip envelopes
		- consolidating clips
		- recording Session launches into the Arrangement
		- creating, moving and duplicating scenes
		- dragging frozen MIDI clips onto audio tracks
	- Edits to a frozen track with time-based effects can sound different after unfreezing, because those effects are recomputed then.
	- Frozen Arrangement tracks keep effect tails as crosshatched temporary clips beside the original clips; select the tail along with its clip when moving it. Frozen Session clips hold only two loop cycles.
	- Dragging a frozen clip into a drop area makes a new frozen track with that clip, or only its selected part.
	- Freeze files go in the project's `Samples/Processed/Freeze` folder, or the Temporary Folder for an unsaved Set. Freezing also lets a slower computer, or one missing a device, play a Set.
