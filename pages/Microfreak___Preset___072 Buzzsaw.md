logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 072
preset-synth-microfreak-name:: Buzzsaw
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/071 Sweep SQ]]
next:: [[Microfreak/Preset/073 S.H Ld]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
preset-synth-microfreak-parameter-payload-sha256:: c28ee410f274e1ec7ab27be03d209a5e3948b8a26e731d97be56e46d84e84fb5
preset-synth-file:: [Buzzsaw — October 25 slot 72 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___072%20Buzzsaw___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 3ff4078425e701ac095e3c479caf4e96bdb28c9a7a63a11193fe8ec2c5d069c7
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 72 over USB on October 25, 2026 with `mise run microfreak:download --slot 72`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 159, Factory 2.1 slot 156, Factory 3.0 slot 156, Factory 6.0 slot 319). Comparison used `mise run microfreak:compare`.
		- [Download the slot 72 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___072%20Buzzsaw___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/072 Buzzsaw/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Two Op. FM. [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
		- Ratio: 0.354. Amount: 0.487. Shape: 0.742.
		- Keyboard octave: 0. Glide: 0.113.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.359; resonance: 0.349. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.192, sustain 0.631. Amp Mod is off. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.163, RiseSlp 0.500, FallLvl 0.163, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync off; stored normalized rate: 0.355. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- PRESSURE → Wave: +0.331.
		- LFO → Timbre: +0.317.
		- ENV → Cutoff: +0.528.
		- LFO → Assign 1 → `Mat.Assign1`: +0.051.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
