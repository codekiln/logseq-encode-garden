logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 070
preset-synth-microfreak-name:: Cliched Things
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/069 3opeR]]
next:: [[Microfreak/Preset/071 Sweep SQ]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
preset-synth-microfreak-parameter-payload-sha256:: 2b557f97d34a2766b338450f713ef1a037b8a36d7ded08186b52b96e4fbc46ab
preset-synth-file:: [Cliched Things — October 25 slot 70 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___070%20Cliched%20Things___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: eac013b4b08704e6933dd5545f76f26fc0f942f4aa57ded47167871f98014ff4
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 70 over USB on October 25, 2026 with `mise run microfreak:download --slot 70`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 157, Factory 1.1 slot 157, Factory 2.1 slot 154, Factory 3.0 slot 154, Factory 6.0 slot 384). Comparison used `mise run microfreak:compare`.
		- [Download the slot 70 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___070%20Cliched%20Things___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/070 Cliched Things/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: V.Analog. [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		- Detune: 0.479. Shape: 0.565. Wave: 0.555.
		- Keyboard octave: -2. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.578; resonance: 0.550. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.203, sustain 0.635. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.163, RiseSlp 0.500, FallLvl 0.968, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 2. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- PRESSURE → Wave: −0.006.
		- LFO → Timbre: +0.060.
		- PRESSURE → Cutoff: +0.200.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
