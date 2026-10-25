logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 200
preset-synth-microfreak-name:: Saw Bass
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Template]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/199 FM Bass]]
next:: [[Microfreak/Preset/201 Square Bass]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
preset-synth-microfreak-parameter-payload-sha256:: 8447598585e1109de23d6171ba3571ddb058e494abb85a04c293d54e361916c1
preset-synth-file:: [Saw Bass — October 25 slot 200 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___200%20Saw%20Bass___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: e09624549b55a1fda405b7ff5a3388c3fcfaacebfe0ab79116b3bf5ad4ac9ad0
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 200 over USB on October 25, 2026 with `mise run microfreak:download --slot 200`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0 (Factory 1.1 slot 229, Factory 2.1 slot 43, Factory 3.0 slot 272). Comparison used `mise run microfreak:compare`.
		- [Download the slot 200 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___200%20Saw%20Bass___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/200 Saw Bass/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: BasicWaves. [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
		- Morph: 0.538. Sym: 0.709. Sub: 0.293.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.287; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.148, sustain 0.145. Amp Mod is off. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.163, RiseSlp 0.500, FallLvl 0.163, FallSlp 0.500, Hold 0.000, Amount 0.745. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 9. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Cutoff: +1.000.
		- PRESSURE → Cutoff: +0.396.
		- PRESSURE → Assign 1 → matrix amount LFO → Pitch: +0.028.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
