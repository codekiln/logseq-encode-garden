logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 154
preset-synth-microfreak-name:: Old Tapes
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/153 Pig]]
next:: [[Microfreak/Preset/155 Paralex]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
preset-synth-microfreak-parameter-payload-sha256:: 1969f21b5f030d7debef65723026676d5e574fbd71398ef4bc24bcfd182923d8
preset-synth-file:: [Old Tapes — October 25 slot 154 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___154%20Old%20Tapes___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 3e3191443befbbb6f10baaa06c22ef1d26fde7ab6c2289480a2dac0a68416f67
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 154 over USB on October 25, 2026 with `mise run microfreak:download --slot 154`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 129, Factory 2.1 slot 230, Factory 3.0 slot 230, Factory 6.0 slot 249). Comparison used `mise run microfreak:compare`.
		- [Download the slot 154 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___154%20Old%20Tapes___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/154 Old Tapes/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Two Op. FM. [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
		- Ratio: 0.466. Amount: 0.367. Shape: 0.957.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Band-pass filter. Saved cutoff: 0.369; resonance: 0.195. [[Microfreak/UG/07 Filter/01 Modifying Sound/02 Band Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.456, decay/release 0.506, sustain 0.248. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.168, RiseSlp 0.500, FallLvl 0.169, FallSlp 0.500, Hold 0.000, Amount 0.828. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync off; stored normalized rate: 0.682. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.012.
		- PRESSURE → Wave: −0.222.
		- ENV → Cutoff: +0.218.
		- LFO → Cutoff: +0.045.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
