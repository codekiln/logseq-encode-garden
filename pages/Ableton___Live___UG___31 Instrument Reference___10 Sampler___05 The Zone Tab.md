logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/31 Instrument Reference/10 Sampler]]
prev:: [[Ableton/Live/UG/31 Instrument Reference/10 Sampler/04 Sampler's Tabs]]
next:: [[Ableton/Live/UG/31 Instrument Reference/10 Sampler/06 The Sample Tab]]
- # [31.10.5 The Zone Tab](https://www.ableton.com/en/live-manual/12/live-instrument-reference/#the-zone-tab)
	- The Zone tab opens the Zone Editor above the Device View, for mapping samples across key, velocity and sample-select ranges.
		- ![The Key Zone Editor](https://ableton-production.imgix.net/live-manual/12/SamplerZoneEditorL12.png)
	- The **sample layer list** on the left holds every sample, or layer, of the multisample. Buttons above it:
		- **Auto** — selects the layers that play each incoming note while it sounds.
		- **Lin/Pow** — linear or constant-power zone fades.
		- **RR** — Round Robin on or off.
		- **Key/Vel/Sel** — which zone editor to show. Right-click an editor to zoom Small, Medium or Large.
	- ## 31.10.5.1 Round Robin Sample Playback
		- Plays a different sample on each note, cycling through layers that share a key zone; good for natural variation in repeated drums or notes, or for deliberate surprises.
			- ![Using Different Samples for Round Robin Playback](https://ableton-production.imgix.net/live-manual/12/SamplerRoundRobinL12.png)
		- **Round Robin Mode** — Forward (top to bottom), Backward, Other (random, never the same twice running), Random (repeats allowed).
		- **Reset Interval** — restarts the cycle at a set interval, such as each bar, from the first sample of the mode.
	- ## 31.10.5.2 The Sample Layer List
		- Layers can be named, for example by root key; hovering shows details in the Status Bar, and selecting one opens it in the Sample tab.
		- Context menu: Delete, Duplicate, Rename; **Distribute Ranges Equally** (C-2 to G8) and **Distribute Ranges Around Root Key**; zoom; Show in Browser; Manage Sample; **Normalize Volume** (peaks to full headroom); **Normalize Pan** (an even stereo spread, not necessarily center); **Select All With Same Range**; and sorting by name, key, velocity or selector, ascending or descending.
	- ## 31.10.5.3 Key Zones
		- The note range, up to all 127, that triggers each sample. A sample stays accurate a few semitones around its root key, and other samples cover the rest.
			- ![The Key Zone Editor](https://ableton-production.imgix.net/live-manual/12/SamplerKeyZoneEditorL12.png)
		- New samples span the full range. Move and resize zones like Arrangement clips; drag a top corner to fade across semitones and crossfade neighbors, linear or exponential per Lin/Pow.
	- ## 31.10.5.4 Velocity Zones
		- The note-on velocities, 1–127, each sample answers, so different dynamics can use different recordings. Edited like key zones.
			- ![The Velocity Zone Editor](https://ableton-production.imgix.net/live-manual/12/SamplerVelocityZoneEditorL12.png)
	- ## 31.10.5.5 Sample Select Zones
		- A 0–127 filter not tied to any MIDI input, like a Rack's Chain Select zones. Only samples whose zone overlaps the **sample selector** can play.
			- ![The Sample Selector](https://ableton-production.imgix.net/live-manual/12/SamplerSampleSelectorL12.png)
		- Moving the selector doesn't switch a sample already playing.
