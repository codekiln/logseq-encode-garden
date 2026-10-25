logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/29 Audio Effect Reference]]
prev:: [[Ableton/Live/UG/29 Audio Effect Reference/37 Spectral Time]]
next:: [[Ableton/Live/UG/29 Audio Effect Reference/39 Tuner]]
- # [29.38 Spectrum](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#spectrum)
	- ![The Spectrum Device](https://ableton-production.imgix.net/live-manual/12/SpectrumL12.png?auto=&w=320)
	- Spectrum analyzes frequencies in real time and draws level (dB, vertical) against frequency or pitch (horizontal). Peaks stay on the graph until the song restarts. It measures only and never changes the sound.
	- **Block** — samples per measurement; more is more accurate and uses more CPU
	- **Channel** — left, right or both
	- **Refresh** — how often it analyzes; faster is more accurate and uses more CPU
	- **Avg** — how many blocks are averaged per update. 1 shows every block, good for finding short peaks; higher values give a smoother view closer to how we hear.
	- **Graph** — a smooth line or discrete frequency bins
	- **Max** — shows the accumulated maximum; click the display to reset it
	- **Scale X** — linear, logarithmic or semitone. Log and semitone are the same scale with Hz or note names along the top; linear helps when studying the highs.
	- Hovering shows level, frequency and note name at the pointer.
	- **Range/Auto** — Range lets you scroll (drag vertically) and zoom (drag horizontally) on the level legend, or set limits with the Range sliders; Auto scales to the input and disables those.
	- The title bar button, or double-clicking the display, moves the display into Live's main window.
		- ![button in Spectrum’s title bar or by double-clicking in the display](https://ableton-production.imgix.net/live-manual/12/Device_unfold.png?auto=&w=24)