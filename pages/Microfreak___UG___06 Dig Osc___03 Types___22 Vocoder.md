logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Microfreak/UG/06 Dig Osc/03 Types]]
prev:: [[Microfreak/UG/06 Dig Osc/03 Types/21 Hit Grains]]
- # 06.03.22 Vocoder Oscillator (Vocoder)
	- Vocoder Oscillator Model
		- ![01 Vocoder Oscillator Model](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___UG___06%20Dig%20Osc___03%20Types___22%20Vocoder___Asset___01-Vocoder-Oscillator-Model.png)
	- This oscillator acts as the Vocoder's carrier and provides waves rich in overtones. Select the waveform with the Wave encoder.
	- **Wave:** At 0%, it produces a sawtooth. Around 11%, it becomes a pulse wave with a 50% duty cycle. From there the pulse width increases clockwise until it reaches a 99% duty cycle at 90%. From 91% to 100%, it produces noise.
	- **Timbre:** Changes the frequency range used for analysis and resynthesis. Voice formants are frequency peaks; for example, a “U” often has peaks near 330 Hz and 1260 Hz, with variation across speakers and cultures. The synthesis filters recreate the input loudness contour in the selected range. Narrowing the range reduces the frequencies the Vocoder monitors, improving response time and frequency output.
	- **Shape:** Sets the bandwidth of the individual bandpass filters. Higher settings narrow the frequency response, emphasizing more pronounced harmonics.
	- > [[Note/Info]] Oscillator type cannot be modulated while the Vocoder oscillator is active.
