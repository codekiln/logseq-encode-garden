logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 189
preset-synth-microfreak-name:: Brass 1
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Template]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/188 Karpad]]
next:: [[Microfreak/Preset/190 Brass 2]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
preset-synth-microfreak-parameter-payload-sha256:: 694ddbb1a9c5ba8a2cee86140d9d13cdb74b42af759c58cabb492a1a89f5816a
preset-synth-file:: [Brass 1 — October 25 slot 189 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___189%20Brass%201___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: eb55a86354cd146caa967f6c5ab40c8aa85e6b84c709163856a2f341811f4b0c
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 189 over USB on October 25, 2026 with `mise run microfreak:download --slot 189`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0 (Factory 1.1 slot 219, Factory 2.1 slot 32, Factory 3.0 slot 262). Comparison used `mise run microfreak:compare`.
		- [Download the slot 189 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___189%20Brass%201___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/189 Brass 1/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: BasicWaves. [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
		- Morph: 0.496. Sym: 0.000. Sub: 0.000.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.000; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.260, decay/release 0.260, sustain 0.772. Amp Mod is off. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.163, RiseSlp 0.500, FallLvl 0.163, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 9. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Cutoff: +1.000.
		- ENV → Cutoff: +0.640.
		- PRESSURE → Cutoff: +0.793.
		- PRESSURE → Assign 1 → matrix amount LFO → Pitch: +0.014.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
