logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 314
preset-synth-microfreak-name:: Gliding Vox
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Vocoder]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/313 Tremolo Saw]]
next:: [[Microfreak/Preset/315 Crying]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/22 Vocoder]]
preset-synth-microfreak-parameter-payload-sha256:: ac8da850c3e18fdf556e2001235d3863b8630e361a8025419d398cbfe2fd0453
preset-synth-file:: [Gliding Vox — October 25 slot 314 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___314%20Gliding%20Vox___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 57bb5a507cd973b1a52ee298fba370b15f781316431935c1bfd683611ec76c9e
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 314 over USB on October 25, 2026 with `mise run microfreak:download --slot 314`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.1 slot 61, Factory 3.0 slot 376, Factory 6.0 slot 201). Comparison used `mise run microfreak:compare`.
		- [Download the slot 314 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___314%20Gliding%20Vox___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/314 Gliding Vox/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Vocoder. [[Microfreak/UG/06 Dig Osc/03 Types/22 Vocoder]]
		- Wave: 0.635. Timbre: 0.563. Shape: 0.628.
		- Keyboard octave: 0. Glide: 0.410.
	- ## Filter
		- Low-pass filter. Saved cutoff: 1.000; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.085, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.208, RiseSlp 0.500, FallLvl 0.207, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 46877. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.009.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
