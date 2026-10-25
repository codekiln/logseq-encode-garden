logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 284
preset-synth-microfreak-name:: Synz Today
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/283 Far Away]]
next:: [[Microfreak/Preset/285 70s Resolution]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
preset-synth-microfreak-parameter-payload-sha256:: af06688a4f375933ef784829e09f4b00dbb05ab03c755300ff72a122b56ff21d
preset-synth-file:: [Synz Today — October 25 slot 284 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___284%20Synz%20Today___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 757e6fc7db662cc32e80317f8518340f75920bbb5177f7359497a964f12bce18
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 284 over USB on October 25, 2026 with `mise run microfreak:download --slot 284`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0 (Factory 3.0 slot 349). Comparison used `mise run microfreak:compare`.
		- [Download the slot 284 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___284%20Synz%20Today___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/284 Synz Today/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SawX. [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
		- Saw Mod: 0.000. Shape: 0.085. Noise: 0.128.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.108; resonance: 0.056. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.384, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.175, RiseSlp 0.500, FallLvl 0.163, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sawtooth, clock sync off; stored normalized rate: 0.483. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Wave: +0.060.
		- ENV → Cutoff: +0.501.
		- PRESSURE → Cutoff: +0.443.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
