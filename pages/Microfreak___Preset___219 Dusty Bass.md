logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 219
preset-synth-microfreak-name:: Dusty Bass
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Unknown]]
prev:: [[Microfreak/Preset/218 Metal Sequence]]
next:: [[Microfreak/Preset/220 Planetary Dial]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-file-sha256:: 4ba79b678cc705ffebf0ec3b667113c4129164b04ba5f28aa4ac7b58da9669f8
- # Notes
	- Harmonic bass with a resonant filter, changing partials and envelope-controlled brightness.
	- ## Saved export and provenance
		- Saved export: September 28, 2026 MIDI Control Center user-bank archive, computer-bank slot 29, file `29-09282026 6h14-A29.mbp`. The computer-bank slot differs from this page’s observed device slot.
		- The parameter payload matches Factory 3.0 and 6.0. This is an archived factory-equivalent baseline; it does not establish the instrument’s saved or unsaved state during a later session.
	- ## Oscillator
		- Model: HARM. Spread sets the spacing of partials; Rectification reshapes each partial; Noise adds phase-modulated noise and affects clipping.
		- Spread: 0.500.
		- Rectification: 0.471.
		- Noise: 0.452.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.157; resonance: 0.720. Cutoff and resonance are normalized settings, not hertz or instrument display values.
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.661, sustain 0.924. Amp Mod is on, so the main envelope controls loudness.
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.180, FallLvl 0.134, Hold 0.521, Amount 0.186. These are normalized stored fields; rise/fall times in milliseconds remain unverified.
	- ## LFO
		- Smoothed random; clock sync on. Stored normalized rate: 0.148; division code: 0. The rate is not a hertz reading, and the musical division has not been converted.
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. The assignment destinations below resolve the saved Assign columns.
		- Cycling Envelope → Wave / Spread: −0.001. A small envelope route changes partial spacing.
		- LFO → Wave / Spread: +0.111. Smoothed random modulation changes partial spacing.
		- Cycling Envelope → Timbre / Rectification: +0.017. The envelope changes partial rectification.
		- ENV → Cutoff: +1.000. The main envelope strongly opens the filter.
		- Cycling Envelope → Assign 2 → Cycling Envelope Amount: −0.051. The envelope modulates its own output amount.
		- All other saved matrix amounts are zero.
	- ## Performance and session context
		- The main envelope sustains above zero and opens the filter. The cycling envelope and smoothed random LFO change the oscillator spectrum.
		- Paraphonic mode is off in the saved export. The PRESSURE matrix row uses pressure or velocity according to the instrument’s global Utility setting; the export does not establish which expression source was used in the session.
		- [[GitP/A/Session/26/10/12-Mon]] references this sound. The session context does not identify which recording passages use it.
	- ## Evidence and interpretation
		- Base controls use normalized 0…1 values unless a stored choice code is shown; matrix amounts use −1…+1. These describe saved base settings, before modulation, and are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix columns and assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py#L21-L107) and [assignment decoder](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_structured.py#L152-L173). Mode and waveform labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js#L1782-L1946).
		- [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]] describes oscillator controls. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]] explains the matrix and expression row.
