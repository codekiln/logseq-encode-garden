logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/29 Audio Effect Reference]]
prev:: [[Ableton/Live/UG/29 Audio Effect Reference/33 Roar]]
next:: [[Ableton/Live/UG/29 Audio Effect Reference/35 Shifter]]
- # [29.34 Saturator](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#saturator)
	- ![The Saturator Effect](https://ableton-production.imgix.net/live-manual/12/SaturatorL12.png?auto=&w=320)
	- Saturator is a waveshaper that adds dirt, punch or warmth, from soft saturation to heavy coloring. Each sample is mapped to a new value through a curve, so the effect depends on the signal's level at each moment.
	- **Curve Type** — eight curves:
		- **Analog Clip** — clips smoothly around the clipping point; **Digital Clip** clips hard. Both stay clean below it.
		- **Soft Sine**, **Medium Curve**, **Hard Curve** — saturation with different characters
		- **Sinoid Fold** — wavefolding: louder input folds back on itself
		- **Bass Shaper** — like Analog Clip with smoother harmonics on heavily driven lows; made for 808 kicks and synth bass. **Bass Shaper Threshold** (0 to −50 dB) goes from soft clipping (low values, best for bass with high Drive) to hard clipping (high values).
		- **Waveshaper** — the most extreme, with its own controls in the expanded view (title bar button)
	- The **Shaper Curve** display shows the curve and the live input against it.
	- **Post Clip Mode** — **Soft Clip** or **Hard Clip** keeps the output under the Output level, catching extra boost from negative Color settings. Soft Clip applies an Analog Clip curve to the output.
	- **Color** — two color filters: an EQ before the shaper and its inverse after. For example, cut the bass before saturating so only mids and highs distort while the bass comes through intact.
		- **Amt Lo** — more or less saturation in the lows
		- In the expanded view's **Color Curve** display: **Amt Hi**, **Frequency** and **Width** for the second filter. Drag the first handle for Amt Lo, the second sideways for Frequency or up and down for Amt Hi.
		- ![The Color Curve Display and Color Filter Parameters](https://ableton-production.imgix.net/live-manual/12/SaturatorColorCurveL12.png?auto=&w=320)
	- **Drive** — input gain; its effect shows in the curve display
	- **Output** — final level
	- **Dry/Wet** — set to 100% on a return track
	- ### [29.34.0.1 Saturator's Waveshaper Controls](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#saturators-waveshaper-controls)
		- Six more controls appear in the expanded view with the Waveshaper curve.
			- ![The Waveshaper Controls](https://ableton-production.imgix.net/live-manual/12/SaturatorWaveshaperL12.png?auto=&w=320)
		- **Drive** — how much the controls below shape the curve, 0% to 100%
		- **Curve** — adds mostly third-order harmonics
		- **Depth** — level of a sine wave added to the curve
		- **Linear** — with Curve and Depth, changes the curve's linear part
		- **Damp** — flattens signal near zero, like a very fast noise gate
		- **Period** — how many ripples the added sine has
	- ### [29.34.0.2 Context Menu Options for Saturator](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#context-menu-options-for-saturator)
		- **Hi-Quality** — less aliasing, especially in the highs, for slightly more CPU
		- **Pre-DC Filter** — removes DC offset at the input