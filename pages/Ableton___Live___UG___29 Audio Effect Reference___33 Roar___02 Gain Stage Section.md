logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/29 Audio Effect Reference/33 Roar]]
prev:: [[Ableton/Live/UG/29 Audio Effect Reference/33 Roar/01 Input Section]]
next:: [[Ableton/Live/UG/29 Audio Effect Reference/33 Roar/03 Modulation Section]]
- # [29.33.2 Gain Stage Section](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#gain-stage-section)
	- ![Roar’s Gain Stage Section](https://ableton-production.imgix.net/live-manual/12/RoarGainStageSectionL12.png?auto=&w=320)
	- Each routing has its own gain stages, each switched on with its **Stage** toggle. Every stage tab has **Shaper Amount**, **Shaper Bias** and **Filter Frequency**, plus shaper and filter type menus.
	- **Shaper Amount** — saturation; also drag the curve in the display. Distortion happens where the signal reaches the curve's bends.
	- **Shaper Bias** — offsets the signal for asymmetric distortion; high values sound like a broken circuit, extreme values silence it
	- **Shaper Type** — twelve curves:
		- **Soft Sine** — smooth, warm, analog-like even when pushed
		- **Digital Clip** — hard clipping with harsh upper harmonics
		- **Bit Crusher** — amplitude quantization like [[Ableton/Live/UG/29 Audio Effect Reference/30 Redux]]; more Amount means fewer bits and a stronger compander. Good with bias modulation; very audible on quiet signals.
		- **Diode Clipper** — virtual analog clipping circuit; like Soft Sine with softer highs
		- **Tube Preamp** — soft tube saturation that keeps transients and dynamics
		- **Half Wave Rectifier** — fully asymmetric; adds crunch to drums
		- **Full Wave Rectifier** — raises the signal an octave; adds harmonics to synths
		- **Polynomial** — shifts from a sine curve to more complex shapes; good for modulation and metallic sounds
		- **Fractal** — lots of high harmonics
		- **Tri Fold** — triangle wavefolder; like Fractal but harsher
		- **Noise Injection** — stereo noise then smooth distortion; saturation with grit
		- **Shards** — constantly changing stereo curve segments that break the signal apart rhythmically
	- The toggle under the display turns the shaper off; **Shaper Level** makes up level changes from the curve.
	- **Filter Frequency** — cutoff. With **Pre** on, the filter comes before the shaper and leaves the shaper's harmonics alone.
	- Filter types: **LP**, **BP**, **HP**, **Notch**, **Peak** (with **Filter Peak Gain**), **Morph** (low-pass through band-pass to high-pass, with a **Morph** control), **Comb** (notches; flanger-like when swept), **Resampling** (sample-rate artifacts like Redux), **Dispersion** (delays frequencies by different amounts without changing level, for metallic, spring-like tones). All but Resampling have **Resonance**.