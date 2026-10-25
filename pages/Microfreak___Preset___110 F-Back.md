logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 110
preset-synth-microfreak-name:: F-Back
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/109 VeloSparklz]]
next:: [[Microfreak/Preset/111 AcidFrog]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
preset-synth-microfreak-parameter-payload-sha256:: d3c217e62534baeeea19d883bcc9c431b9a8267aab1d3851fdbe084921f27a42
preset-synth-file:: [F-Back — October 25 slot 110 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___110%20F-Back___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 692166f3056b804581afe15374e7b963d6763868fd8fb4e87075c4ac9bf2e243
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 110 over USB on October 25, 2026 with `mise run microfreak:download --slot 110`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0 (Factory 1.1 slot 205, Factory 2.1 slot 190, Factory 3.0 slot 190). Comparison used `mise run microfreak:compare`.
		- [Download the slot 110 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___110%20F-Back___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/110 F-Back/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Two Op. FM. [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
		- Ratio: 0.000. Amount: 0.770. Shape: 0.000.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.192; resonance: 0.334. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.208, sustain 0.329. Amp Mod is off. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.106, RiseSlp 0.500, FallLvl 0.283, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.166. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.003.
		- LFO → Pitch: +0.002.
		- PRESSURE → Wave: +0.061.
		- ENV → Cutoff: +0.587.
		- LFO → Cutoff: +0.063.
		- PRESSURE → Cutoff: +0.481.
		- Cycling Envelope → Assign 1 → Shape: +0.852.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
