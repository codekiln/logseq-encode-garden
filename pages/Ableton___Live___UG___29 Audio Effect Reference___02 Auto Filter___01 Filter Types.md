logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/29 Audio Effect Reference/02 Auto Filter]]
next:: [[Ableton/Live/UG/29 Audio Effect Reference/02 Auto Filter/02 Filter Display]]
- # [29.2.1 Filter Types](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#filter-types)
	- ![The Filter Type Chooser](https://ableton-production.imgix.net/live-manual/12/AutoFilterTypesL12.png?auto=&w=320)
	- **Filter Type** offers ten filters:
		- **Low-pass** — cuts above the cutoff; 12 or 24 dB slope
		- **High-pass** — cuts below the cutoff; 12 or 24 dB
		- **Band-pass** — passes a band around the cutoff; 12 or 24 dB
		- **Notch** — cuts a narrow band; 12 or 24 dB
		- **Morph** — sweeps from low-pass through band-pass to high-pass; 6, 12, 24 or 48 dB
		- **DJ** — one bipolar control: above zero removes lows, below zero removes highs, with resonance rising toward ±100%
		- **Comb** — a series of peaks or notches across the spectrum; flanger-like when modulated
		- **Resampling** — resamples at a rate set by the cutoff, giving aliasing and degradation
		- **Notch + LP** — a notch plus a low-pass roll-off; 12 or 24 dB
		- **Vowel** — emphasizes formants so the sound resembles a voice
	- **Freq** sets the cutoff. The DJ filter has **Control** instead; Vowel has **Pitch**, which shifts the formants in semitones.
	- **Res** sets emphasis at the cutoff; it does nothing on Resampling. Vowel has **Formant** instead, moving through the vowels a, e, i, o, u.
	- **Morph**, on Morph, Comb, Notch + LP and Vowel:
		- Morph filter — low values low-pass, middle band-pass, high values high-pass
		- Comb — from peaks (low) to notches (high) at multiples of the cutoff
		- Notch + LP — moves the notch closer to the low-pass cutoff as the value rises, reaching it at 100%
		- Vowel — increasingly evens out the formant gains