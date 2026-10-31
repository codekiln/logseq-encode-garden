logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
alias:: [[Microfreak/Preset/399]]
preset-synth-microfreak-number:: 399
preset-synth-microfreak-name:: Init
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Custom]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
preset-synth-microfreak-parameter-payload-sha256:: 3cde09c95eb96546d8b1ab9b6f80681fefa4fa607b2a2134a30b084ebb88f581
preset-synth-file:: [399 Init.mfpz](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/GitP___A___Session___26___10___09-Fri___Asset___Preset___399.mfpz)
preset-synth-file-sha256:: 88510c0e198e80eaa6e6fa9b6566806427a02b3996c334a8b9fb904ad1f9ab14
prev:: [[Microfreak/Preset/398 Init]]
next:: [[Microfreak/Preset/400 Init]]
- # Notes
	- Quick-saved to slot 399 during [[GitP/A/Session/26/10/09-Fri]], at 22:19 in the recording.
	- Custom Bass patch with wavefolding and expression-controlled noise.
	- ## Saved export and provenance
		- The existing downloadable preset 399 export matches this page’s file and parameter-payload digests. It is a populated custom preset named Init, not an initialized empty slot.
		- The saved export preserves this preset’s identity independently of similarly named patches or later device-slot changes. It does not capture unsaved edits elsewhere in the recording.
	- ## Oscillator
		- Model: BASS. Saturate changes cosine-oscillator saturation; Fold applies asymmetric wavefolding; Noise phase-modulates the oscillators and adds noise between fold stages.
		- Saturate: 0.000.
		- Fold: 0.512.
		- Noise: 0.332.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.351; resonance: 0.282. Cutoff and resonance are normalized settings, not hertz or instrument display values.
	- ## Envelopes
		- Main envelope: attack 0.198, decay/release 0.255, sustain 0.463. Amp Mod is on, so the main envelope controls loudness.
		- Cycling Envelope mode: Run. Stored RiseLvl 0.163, FallLvl 0.163, Hold 0.000, Amount 1.000. These are normalized stored fields; rise/fall times in milliseconds remain unverified.
	- ## LFO
		- Sine; clock sync on. Stored normalized rate: 0.148; division code: 10. The rate is not a hertz reading, and the musical division has not been converted.
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. The assignment destinations below resolve the saved Assign columns.
		- ENV → Cutoff: +0.050. The main envelope opens the filter slightly.
		- PRESSURE → Cutoff: −0.112. Expression closes the filter.
		- PRESSURE → Assign 1 → Noise: +0.977. Expression strongly increases oscillator noise.
		- All other saved matrix amounts are zero.
	- ## Performance and session context
		- The saved oscillator combines folding and noise. Expression adds noise while lowering cutoff, and the main envelope shapes loudness and filter brightness.
		- Paraphonic mode is off in the saved export. The PRESSURE matrix row uses pressure or velocity according to the instrument’s global Utility setting; the export does not establish which expression source was used in the session.
		- [[GitP/A/Session/26/10/09-Fri]] records this sound’s quick save. The preserved quick-save note above identifies the recording passage.
	- ## Evidence and interpretation
		- Base controls use normalized 0…1 values unless a stored choice code is shown; matrix amounts use −1…+1. These describe saved base settings, before modulation, and are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix columns and assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py#L21-L107) and [assignment decoder](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_structured.py#L152-L173). Mode and waveform labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js#L1782-L1946).
		- [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]] describes oscillator controls. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]] explains the matrix and expression row.
