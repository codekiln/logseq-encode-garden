logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/29 Audio Effect Reference]]
prev:: [[Ableton/Live/UG/29 Audio Effect Reference/20 Gate]]
next:: [[Ableton/Live/UG/29 Audio Effect Reference/22 Grain Delay]]
- # [29.21 Glue Compressor](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#glue-compressor)
	- ![The Glue Compressor Effect](https://ableton-production.imgix.net/live-manual/12/GlueL12.png?auto=&w=320)
	- Glue Compressor is an analog-modeled bus compressor made with Cytomic, based on the bus compressor of a famous 1980s mixing console. It works on single tracks but is aimed at the Main track or Group Tracks, to "glue" several sources into one mix.
	- **Threshold** and **Ratio** work as in [[Ableton/Live/UG/29 Audio Effect Reference/09 Compressor]]. There is no knee control; the knee gets harder as the ratio rises.
	- **Attack** — in ms
	- **Release** — in seconds. **A** (Auto) uses a slow release for the overall level and a fast one for transients; gentle on most material but slow on sudden level changes.
	- **Dry/Wet** — 0% bypasses, 100% fully compressed
	- **Range** — limits how much compression can happen. −60 to −70 dB behaves like the original hardware; −40 to −15 dB works as an alternative to Dry/Wet; 0 dB does nothing.
	- **Makeup** — set it near the needle's reading to get back roughly the original level.
	- **Soft** clip — a fixed waveshaper capping output at −0.5 dB to catch loud transients. It colors and distorts the sound, so the manual suggests leaving it off unless that is wanted. With Oversampling, peaks can still pass 0 dB.
	- The needle shows gain reduction in dB. The **Clip** LED turns red above 0 dB, or yellow when Soft clip is catching peaks.
	- {{embed [[Ableton/Live/UG/29 Audio Effect Reference/21 Glue Compressor/01 Sidechain Parameters]]}}