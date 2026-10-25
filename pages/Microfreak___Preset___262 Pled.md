logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 262
preset-synth-microfreak-name:: Pled
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/261 Eurgon Lead]]
next:: [[Microfreak/Preset/263 Giraf]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
preset-synth-microfreak-parameter-payload-sha256:: 0b6d367183feafc753db7285052080abf1798e6405c332b685ef63cc6c066a22
preset-synth-file:: [Pled — October 25 slot 262 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___262%20Pled___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 8bf99a6396a725453a7e6880ca70a15bb9bf9d6f74ebdf9f98fd2d37918354e4
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 262 over USB on October 25, 2026 with `mise run microfreak:download --slot 262`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 329, Factory 6.0 slot 107). Comparison used `mise run microfreak:compare`.
		- [Download the slot 262 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___262%20Pled___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/262 Pled/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SawX. [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
		- Saw Mod: 0.608. Shape: 0.356. Noise: 0.274.
		- Keyboard octave: +1. Glide: 0.136.
	- ## Filter
		- Low-pass filter. Saved cutoff: 1.000; resonance: 0.557. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.283, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.189, RiseSlp 0.500, FallLvl 0.978, FallSlp 0.500, Hold 0.000, Amount 0.392. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 1. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Wave: −0.889.
		- LFO → Timbre: +0.308.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
