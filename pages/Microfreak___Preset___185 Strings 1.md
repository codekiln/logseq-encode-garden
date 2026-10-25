logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 185
preset-synth-microfreak-name:: Strings 1
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Template]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/184 Xylophone]]
next:: [[Microfreak/Preset/186 Strings 2]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
preset-synth-microfreak-parameter-payload-sha256:: 982c3d7642f1ea3d4f552151df3885362379ca0ee113f09cd5719f551982555d
preset-synth-file:: [Strings 1 — October 25 slot 185 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___185%20Strings%201___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 34ba019f3acfe2518f94ced955a667e320738a0671b5b49c2f461bb63c5c8f09
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 185 over USB on October 25, 2026 with `mise run microfreak:download --slot 185`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0 (Factory 1.1 slot 215, Factory 2.1 slot 28, Factory 3.0 slot 259). Comparison used `mise run microfreak:compare`.
		- [Download the slot 185 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___185%20Strings%201___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/185 Strings 1/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: BasicWaves. [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
		- Morph: 0.079. Sym: 0.835. Sub: 0.346.
		- Keyboard octave: 0. Glide: 0.110.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.662; resonance: 0.299. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.378, decay/release 0.331, sustain 0.724. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.163, RiseSlp 0.500, FallLvl 0.163, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.307. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Timbre: +0.213.
		- PRESSURE → Cutoff: −0.369.
		- PRESSURE → Assign 1 → Filter Resonance: +0.229.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
