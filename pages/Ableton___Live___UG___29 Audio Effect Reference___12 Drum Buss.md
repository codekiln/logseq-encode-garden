logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/29 Audio Effect Reference]]
prev:: [[Ableton/Live/UG/29 Audio Effect Reference/11 Delay]]
next:: [[Ableton/Live/UG/29 Audio Effect Reference/13 Dynamic Tube]]
- # [29.12 Drum Buss](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#drum-buss)
	- ![The Drum Buss Effect](https://ableton-production.imgix.net/live-manual/12/DrumBussL12.png?auto=&w=320)
	- Drum Buss is an analog-style processor for adding body and character to a group of drums and holding them together in a mix.
	- **Trim** — lowers the input before processing
	- **Comp** — a fixed compressor before the distortion, tuned for drum groups: fast attack, medium release, moderate ratio, plenty of makeup gain
	- Distortion types, increasingly strong:
		- **Soft** — waveshaping
		- **Medium** — limiting
		- **Hard** — clipping with a bass boost
	- **Drive** — how hard the input hits the distortion
	- ### [29.12.0.1 Mid-High Frequency Shaping](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#mid-high-frequency-shaping)
		- For clarity and presence on snares and hats.
		- **Crunch** — sine-shaped distortion on the mid-highs
		- **Damp** — low-pass filter to remove harsh highs after distortion
		- **Transients** — above 100 Hz: positive values add attack and sustain for a fuller, punchier sound; negative values add attack but cut sustain for tighter, drier drums
	- ### [29.12.0.2 Low-End Enhancement](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#low-end-enhancement)
		- A resonant filter that strongly boosts the bass, plus a decay control.
		- **Boom** — amount of low-end boost; the **Bass Meter** shows it even when it is hard to hear
		- **Freq** — frequency of the boost; **Force To Note** snaps it to the nearest MIDI note
		- **Decay** — how fast the lows decay. At Boom 0% it affects only the incoming (post-distortion) signal; above 0% it also affects the boost.
		- **Boom Audition** (headphone icon) — solos the low-end boost
	- ### [29.12.0.3 Output](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#output)
		- **Dry/Wet** — balance of processed and dry signal
		- **Output Gain** — output level