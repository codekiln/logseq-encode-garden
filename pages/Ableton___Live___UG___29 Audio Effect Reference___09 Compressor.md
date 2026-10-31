logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/29 Audio Effect Reference]]
prev:: [[Ableton/Live/UG/29 Audio Effect Reference/08 Chorus-Ensemble]]
next:: [[Ableton/Live/UG/29 Audio Effect Reference/10 Corpus]]
- # [29.9 Compressor](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#compressor)
	- ![The Compressor Effect](https://ableton-production.imgix.net/live-manual/12/CompressorL12.png?auto=&w=320)
	- ![Compressor’s Collapsed View](https://ableton-production.imgix.net/live-manual/12/CompressorCollapsedL12.png?auto=&w=320)
	- ![Compressor’s Transfer Curve](https://ableton-production.imgix.net/live-manual/12/CompressorTransferCurveL12.png?auto=&w=320)
	- ![Compression Activity Display, Showing Input and Output](https://ableton-production.imgix.net/live-manual/12/CompressorOutputL12.png?auto=&w=320)
	- A compressor turns down signal above a threshold. Lower peaks leave room to raise the overall level, so the result sounds louder and punchier.
	- **Threshold** sets where compression starts. **Ratio** sets how much: at 3, a 3 dB rise above the threshold comes out as 1 dB. A ratio of 1 does nothing.
	- The orange **Gain Reduction** meter shows the current reduction. The manual warns that more than about 6 dB changes the sound a lot and can flatten dynamics in a way that cannot be undone later — especially on the Main track.
	- **Out** raises the level again after compression; **Makeup** does it automatically as Threshold and Ratio change.
	- **Dry/Wet** — 0% bypasses, 100% is fully compressed
	- **Knee** — how gradually compression starts. 0 dB is a hard knee, which can sound harsh at high ratios. A 10 dB knee with a −20 dB threshold starts gently at −30 dB and reaches full compression at −10 dB.
	- Display views, chosen in the corners of the display:
		- **Collapsed** — only the main controls
		- **Transfer Curve** — input level against output level, with the knee as dotted lines
		- **Activity** — input level in light gray, with **GR** or **Output** showing reduction in orange or output in dark gray over time
	- **Attack** — time to reach full compression once over the threshold; **Release** — time to recover after the signal drops. **Auto Release** sets release from the material.
		- 10–50 ms of attack lets the start of each hit through and keeps it lively; very short attack can sound lifeless or buzzy.
		- Short release can cause pumping, sometimes used on drums on purpose.
		- The manual suggests practicing with a drum loop, adjusting Attack, Release, Threshold and Gain.
	- **Lookahead** — 0, 1 or 10 ms of delay so compression can start on time
	- Mode:
		- **Peak** — reacts to short peaks; precise, good for limiting
		- **RMS** — reacts only to sustained level; closer to perceived loudness and usually more musical
		- **Expand** — raises level above the threshold instead: at 1:2, each dB over becomes 2 dB. See [[Ableton/Live/UG/29 Audio Effect Reference/26 Multiband Dynamics]] for the types of dynamics processing.
	- Envelope shape (hidden in Collapsed view):
		- **Lin** — speed set entirely by Attack and Release
		- **Log** — heavily compressed peaks release faster, for smoother, less obvious compression
	- {{embed [[Ableton/Live/UG/29 Audio Effect Reference/09 Compressor/01 Sidechain Parameters]]}}
	- {{embed [[Ableton/Live/UG/29 Audio Effect Reference/09 Compressor/02 Compressor Tips]]}}