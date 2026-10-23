logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
alias:: [[Microfreak/Preset/398]]
preset-synth-microfreak-number:: 398
preset-synth-microfreak-name:: Init
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Custom]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
preset-synth-microfreak-parameter-payload-sha256:: bbe541db43587badabc7aff9e98a9c0e450cc6074d55d831ae24d0f6dd865588
preset-synth-file:: [398 Init.mfpz](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/GitP___A___Session___26___10___09-Fri___Asset___Preset___398.mfpz)
preset-synth-file-sha256:: 028abd3d20159adb8d1d1b1fd134ebf1411aaa592fcd0021e9198c11641bd759
prev:: [[Microfreak/Preset/397 Imit]]
next:: [[Microfreak/Preset/399 Init]]
- # Notes
	- Quick-saved over slot 398 by holding Save during [[GitP/A/Session/26/10/09-Fri]], at 03:40 in the recording.
	- Custom Bass patch with an open filter and no saved modulation-matrix routes.
	- ## Saved export and provenance
		- The existing downloadable preset 398 export matches this page’s file and parameter-payload digests. It is a populated custom preset named Init, not an initialized empty slot.
		- The saved export preserves this preset’s identity independently of similarly named patches or later device-slot changes. It does not capture unsaved edits elsewhere in the recording.
	- ## Oscillator
		- Model: BASS. Saturate changes cosine-oscillator saturation; Fold applies asymmetric wavefolding; Noise phase-modulates the oscillators and adds noise between fold stages.
		- Saturate: 0.000.
		- Fold: 0.000.
		- Noise: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 1.000; resonance: 0.000. Cutoff and resonance are normalized settings, not hertz or instrument display values.
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.259, sustain 1.000. Amp Mod is on, so the main envelope controls loudness.
		- Cycling Envelope mode: Run. Stored RiseLvl 0.163, FallLvl 0.163, Hold 0.000, Amount 1.000. These are normalized stored fields; rise/fall times in milliseconds remain unverified.
	- ## LFO
		- Sine; clock sync on. Stored normalized rate: 0.148; division code: 10. The rate is not a hertz reading, and the musical division has not been converted.
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. The assignment destinations below resolve the saved Assign columns.
		- All saved matrix amounts are zero, including the Assign columns. Unused assignment destinations do not create modulation routes.
	- ## Performance and session context
		- The saved oscillator controls and matrix amounts are zero, but this is a populated custom preset named Init. Its main envelope has an immediate attack and full sustain.
		- Paraphonic mode is off in the saved export. The PRESSURE matrix row uses pressure or velocity according to the instrument’s global Utility setting; the export does not establish which expression source was used in the session.
		- [[GitP/A/Session/26/10/09-Fri]] records this sound’s quick save. The preserved quick-save note above identifies the recording passage.
	- ## Evidence and interpretation
		- Base controls use normalized 0…1 values unless a stored choice code is shown; matrix amounts use −1…+1. These describe saved base settings, before modulation, and are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix columns and assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py#L21-L107) and [assignment decoder](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_structured.py#L152-L173). Mode and waveform labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js#L1782-L1946).
		- [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]] describes oscillator controls. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]] explains the matrix and expression row.
