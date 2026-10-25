logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/29 Audio Effect Reference]]
prev:: [[Ableton/Live/UG/29 Audio Effect Reference/41 Vinyl Distortion]]
- # [29.42 Vocoder](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#vocoder)
	- ![The Vocoder Effect](https://ableton-production.imgix.net/live-manual/12/VocoderL12.png?auto=&w=320)
	- Vocoder is not in the Intro and Lite editions.
	- A vocoder imposes the level contour of one signal, the **modulator** (usually speech or drums), onto the frequencies of another, the **carrier** (usually a rich synth such as strings or a pad). The classic result is a talking synth or robot voice.
	- Both signals pass through banks of band-pass filters; the level in each modulator band sets the level of the matching carrier band.
	- Put Vocoder on the modulator's track. **Carrier** options:
		- **Noise** — internal noise; its X-Y display sets downsampling (horizontal, left lowers the sample rate) and density (vertical, down thins it)
		- **External** — any internal routing point; the usual choice for robot voices
		- **Modulator** — the modulator carries itself, a resynthesized version shaped by Vocoder's controls
		- **Pitch Tracking** — a monophonic oscillator that follows the modulator's pitch, limited by **High** and **Low**. Saw or three pulse waves, with **Pitch** for coarse tuning. It holds each detected pitch until it finds a new one, so changing its settings or resetting it (for instance by grouping the track) can change the sound unexpectedly. Best on single melodic lines or voice; unpredictable but interesting on chords and drums.
	- **Enhance** — normalizes the carrier's spectrum and dynamics for a brighter sound, useful with external carriers
	- **Unvoiced** — level of an extra noise source for pitchless sounds like "f" and "s"; **Sens.** sets detection (100% always on, 0% off); **Fast/Slow** how quickly it switches
	- The center display shows each band's level; click in it to lower bands.
	- **Bands** — number of filters; more is more accurate and uses more CPU
	- **Range** — frequency span of the filters; narrow it if the sound gets too piercing or boomy
	- **BW** — filter bandwidth; 100% is most accurate, other values can be interesting
	- **Precise/Retro** — equal gain and width for every band, or narrower, louder bands toward the top
	- **Gate** — bands below the threshold are silent
	- **Level** — output boost or cut
	- **Depth** — how much of the modulator's envelope reaches the carrier; 0% none, 100% classic vocoding, 200% only the loudest peaks
	- **Attack** and **Release** — response speed; very fast keeps transients but can distort
	- Channel switches — **Mono** (both mono), **Stereo** (mono modulator, stereo carrier), **L/R** (both stereo)
	- **Formant** — shifts the carrier's filter bank; small changes on a voice can change its apparent gender
	- **Dry/Wet** — balance of processed and dry signal
	- {{embed [[Ableton/Live/UG/29 Audio Effect Reference/42 Vocoder/01 Vocoder Tips]]}}