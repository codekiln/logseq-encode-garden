logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/31 Instrument Reference/09 Operator]]
prev:: [[Ableton/Live/UG/31 Instrument Reference/09 Operator/01 General Overview]]
next:: [[Ableton/Live/UG/31 Instrument Reference/09 Operator/03 LFO Section]]
- # [31.9.2 Oscillator Section](https://www.ableton.com/en/live-manual/12/live-instrument-reference/#oscillator-section-1)
	- ![Oscillator A's Display and Shell Parameters](https://ableton-production.imgix.net/live-manual/12/OperatorPartialsL12.png)
	- ## 31.9.2.1 Built-in Waveforms
		- From the **Wave** chooser: pure Sine, the usual first choice for FM; Sine 4 Bit and Sine 8 Bit for a C64-style sound; Saw D and Square D digital shapes for bass; resynthesized square, triangle and saw whose number (e.g. Square 6) is the harmonic count, with lower numbers mellower and less prone to aliasing; Noise Looped, a noise loop; and Noise White, true random noise.
	- ## 31.9.2.2 User Waveforms
		- **User**, or any built-in wave, can be edited by drawing harmonic amplitudes with the pencil; `Shift` locks to one harmonic. The status bar shows harmonic number and amplitude.
		- Edit the first 16, 32 or 64 harmonics. **Repeat** extends them upward with a fade: low values are brighter, high values roll off more and favor the fundamental; Off truncates.
		- The context menu limits drawing to even or odd harmonics and toggles **Normalize**, which keeps level constant; with it off, output can get very loud.
		- Export as [[Ableton/File/.ams]] to Samples/Waveforms in the User Library; drop .ams files back on an oscillator, or into Simpler or Sampler. The Osc Preview's context menu copies waves between oscillators.
	- ## 31.9.2.3 More Oscillator Parameters
		- **Coarse** and **Fine** set frequency relative to the note. **Fixed** ignores note pitch and uses **Freq** times **Multi**, down to 0.1 Hz; only the timbre changes across keys, as for drums.
		- **Osc < Vel** shifts frequency with velocity; **Q** quantizes the shift to whole ratios, otherwise it detunes into inharmonic tones.
		- Amplitude comes from **Level** and the oscillator's envelope, scaled by **Vel** and **Key**.
		- **Phase**, and **R** to restart the phase per note or run free.
		- When modulating, the modulator's level and the frequency ratio set the result. An oscillator nothing modulates can modulate itself with **Feedback**.
	- ## 31.9.2.4 Aliasing
		- Digital synthesis aliases at high frequencies, and FM, with its many harmonics, does so readily; complex waves like Saw 32 more than sines. A little can be useful; too much makes high notes fold to unrelated pitches.
		- **Antialias** mode, on by default for new patches, reduces it. **Tone** in the global section also tames it, sometimes like a low-pass filter. To hear aliasing, turn Tone up and play very high notes.
