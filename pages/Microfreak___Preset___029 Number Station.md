logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 029
preset-synth-microfreak-name:: Number Station
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/028 Daft]]
next:: [[Microfreak/Preset/030 HarmonicTuneUp]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/11 Speech]]
preset-synth-microfreak-parameter-payload-sha256:: 3da4a81275b7844f418b1118993b4f99a881f746a48e1daac7b47bce3a45d8a2
preset-synth-file:: [Number Station — October 25 slot 29 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___029%20Number%20Station___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: b2f53f47027c077151d3be14f137b4db3a687dc2aaad09ca206e0c5376527e9c
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 29 over USB on October 25, 2026 with `mise run microfreak:download --slot 29`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 105, Factory 1.1 slot 105, Factory 2.1 slot 117, Factory 3.0 slot 117, Factory 6.0 slot 431). Comparison used `mise run microfreak:compare`.
		- [Download the slot 29 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___029%20Number%20Station___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/029 Number Station/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Speech. [[Microfreak/UG/06 Dig Osc/03 Types/11 Speech]]
		- Type: 0.607. Timbre: 0.499. Word: 0.633.
		- Keyboard octave: +1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.932; resonance: 0.201. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.244, sustain 0.999. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.110, RiseSlp 0.500, FallLvl 0.111, FallSlp 0.500, Hold 0.000, Amount 0.495. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync off; stored normalized rate: 0.630. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Assign 1 → Word: +0.500.
		- PRESSURE → Assign 2 → Filter Cutoff: −0.300.
		- PRESSURE → Assign 3 → Filter Resonance: +0.585.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
