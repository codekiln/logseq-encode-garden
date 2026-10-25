logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 317
preset-synth-microfreak-name:: Low Square Bot
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Vocoder]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/316 PWM vox]]
next:: [[Microfreak/Preset/318 Sequenced]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/22 Vocoder]]
preset-synth-microfreak-parameter-payload-sha256:: 1ed38514dcfb8e1da0ccc0bdafaaa9b799a21d8b0500955d53888b22dfb0d293
preset-synth-file:: [Low Square Bot — October 25 slot 317 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___317%20Low%20Square%20Bot___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 6981ff82e92762ae252bdcbca67a5211f53c5d249936630a4b0fe92ccc3c4113
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 317 over USB on October 25, 2026 with `mise run microfreak:download --slot 317`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.1 slot 64, Factory 3.0 slot 379, Factory 6.0 slot 17). Comparison used `mise run microfreak:compare`.
		- [Download the slot 317 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___317%20Low%20Square%20Bot___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/317 Low Square Bot/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Vocoder. [[Microfreak/UG/06 Dig Osc/03 Types/22 Vocoder]]
		- Wave: 0.417. Timbre: 0.548. Shape: 0.246.
		- Keyboard octave: -2. Glide: 0.342.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.841; resonance: 0.341. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.259, sustain 0.997. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.163, RiseSlp 0.500, FallLvl 0.163, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.588. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Wave: +0.131.
		- ENV → Cutoff: +0.012.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
