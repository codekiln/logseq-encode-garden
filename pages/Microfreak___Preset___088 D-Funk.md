logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 088
preset-synth-microfreak-name:: D-Funk
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/087 ATSpookBass]]
next:: [[Microfreak/Preset/089 Kleo]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
preset-synth-microfreak-parameter-payload-sha256:: 47322db9cb35bac9ca7875080663bd389768da8b3329e70a5de152b9c5db2425
preset-synth-file:: [D-Funk — October 25 slot 88 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___088%20D-Funk___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 08cbd590edc62f8c0c680384cca90e97118ff9830303b2dccee8a881ac19b9bc
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 88 over USB on October 25, 2026 with `mise run microfreak:download --slot 88`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 175, Factory 1.1 slot 175, Factory 2.1 slot 170, Factory 3.0 slot 170, Factory 6.0 slot 239). Comparison used `mise run microfreak:compare`.
		- [Download the slot 88 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___088%20D-Funk___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/088 D-Funk/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: BasicWaves. [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
		- Morph: 0.104. Sym: 0.164. Sub: 0.851.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.327; resonance: 0.364. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.236, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.090, RiseSlp 0.500, FallLvl 0.325, FallSlp 0.500, Hold 0.179, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync off; stored normalized rate: 0.167. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Wave: +0.066.
		- Cycling Envelope → Cutoff: +0.243.
		- PRESSURE → Cutoff: +0.227.
		- KEY/ARP → Cutoff: +0.500.
		- Cycling Envelope → Assign 1 → Filter Resonance: +0.382.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
