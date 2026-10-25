logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 179
preset-synth-microfreak-name:: Keys 2
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Template]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/178 Keys 1]]
next:: [[Microfreak/Preset/180 7th Keys]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
preset-synth-microfreak-parameter-payload-sha256:: 8bf50c1a24f4ed00cd4a1c2f2c89838a29e5e3a4b9a9648f9f5d8cd6f2ab2ceb
preset-synth-file:: [Keys 2 — October 25 slot 179 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___179%20Keys%202___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: bb68977751f411b7dde06fc96abce8396b7a764032669b0e73843b84eb2d0dfe
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 179 over USB on October 25, 2026 with `mise run microfreak:download --slot 179`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 21, Factory 2.1 slot None, Factory 3.0 slot 253, Factory 6.0 slot 287). Comparison used `mise run microfreak:compare`.
		- [Download the slot 179 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___179%20Keys%202___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/179 Keys 2/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Two Op. FM. [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
		- Ratio: 0.472. Amount: 0.106. Shape: 0.609.
		- Keyboard octave: +1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 1.000; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.136, sustain 0.402. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.350, FallSlp 0.000, Hold 0.000, Amount 0.172. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.488. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.001.
		- Cycling Envelope → Timbre: +0.299.
		- LFO → Timbre: +0.029.
		- PRESSURE → Assign 1 → Decay/Release: +0.150.
		- PRESSURE → Assign 2 → Cycling Envelope Amount: +0.912.
		- PRESSURE → Assign 3 → Shape: +0.196.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
