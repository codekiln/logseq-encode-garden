logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/31 Instrument Reference/10 Sampler]]
prev:: [[Ableton/Live/UG/31 Instrument Reference/10 Sampler/05 The Zone Tab]]
next:: [[Ableton/Live/UG/31 Instrument Reference/10 Sampler/07 The Pitch-Osc Tab]]
- # [31.10.6 The Sample Tab](https://www.ableton.com/en/live-manual/12/live-instrument-reference/#the-sample-tab)
	- Playback settings for the selected sample, around its waveform. Most values apply to that sample only; the **Sample** chooser switches layers. `Cmd`-scroll (Mac) / `Ctrl`-scroll (Win) zooms.
		- ![The Sample Tab](https://ableton-production.imgix.net/live-manual/12/SamplerSampleTabL12.png)
	- **Reverse** — global and modulatable; plays from Sample End back through the Sustain Loop to Sample Start without writing a new file.
	- **Snap** — snaps start and end points to zero crossings of the left channel to avoid clicks; a small Crossfade may still help. Right-click a loop brace for Snap Marker.
	- **RootKey**, **Detune** (±50 cents), **Volume** (up to +24 dB), **Pan**.
	- ## 31.10.6.1 Sample Playback
		- These work with the global volume envelope. Envelopes here use **Attack**, **Decay**, **Sustain**, **Release** with **A.**, **D.** and **R. Slope**; **Initial**, **Peak** and **End** levels; **Time < Vel**; **Loop** modes (Loop, Beat, Sync, Trigger); **Repeat**; and **Loop Time**, as in Operator.
		- Times show in samples or min:sec:ms, switched from any value's context menu.
		- **Sample Start** and **Sample End** — where playback starts and stops. A slow attack can delay the audible start.
		- **Sustain Mode** — no loop; a forward loop between **Loop Start** and **Loop End**; or a back-and-forth loop, each while the note sustains. **Link** sets Sample Start to Loop Start.
		- **Release Mode**, with a Sustain Loop active:
			- Off — the release happens inside the sustain loop.
			- Release — playback runs on toward Sample End.
			- Release Loop — runs to Sample End, then loops from **Release Loop** to Sample End.
			- Back-and-Forth Release Loop — the same, bouncing back and forth.
		- **Crossfade** — smooths loop joins, constant-power unless turned off in the title bar menu.
		- **Detune** — corrects the pitch shift that short loops can cause.
		- **Interpol** — transposition quality; Good and Best cost a lot of CPU.
		- **RAM** — loads the whole multisample into memory, which helps when modulating start and end points but eats RAM.
		- The waveform's context menu repeats the layer list's file and normalize options and zooms to playing or loop regions. On the right, **Vertical Zoom** and **B/M/L/R** choose display height and channels.
