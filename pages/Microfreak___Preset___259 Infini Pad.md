logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 259
preset-synth-microfreak-name:: Infini Pad
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/258 Glip]]
next:: [[Microfreak/Preset/260 8bitfi]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
preset-synth-microfreak-parameter-payload-sha256:: 9b2503974270c4796ded1ed0289d44b49ad71db24c3d9077bd6a32fa87391221
preset-synth-file:: [Infini Pad — October 25 slot 259 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___259%20Infini%20Pad___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: fb4599873da27fceabd67a5108a96e95c33e0dcb0d07b3e52fe9164ee84cc1a7
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 259 over USB on October 25, 2026 with `mise run microfreak:download --slot 259`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 326, Factory 6.0 slot 19). Comparison used `mise run microfreak:compare`.
		- [Download the slot 259 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___259%20Infini%20Pad___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/259 Infini Pad/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Bass. [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
		- Saturate: 0.000. Fold: 0.135. Noise: 0.054.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.101; resonance: 0.512. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.669, decay/release 0.579, sustain 0.781. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.213, RiseSlp 0.500, FallLvl 0.637, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sawtooth, clock sync on; stored division code: 8. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.004.
		- PRESSURE → Wave: +0.170.
		- ENV → Timbre: +0.968.
		- PRESSURE → Timbre: +0.486.
		- ENV → Cutoff: +0.328.
		- PRESSURE → Cutoff: +0.187.
		- LFO → Assign 1 → Noise: +0.203.
		- PRESSURE → Assign 2 → Noise: −0.125.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
