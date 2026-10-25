logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 270
preset-synth-microfreak-name:: Emo
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Brass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/269 Poireau]]
next:: [[Microfreak/Preset/271 Debout]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
preset-synth-microfreak-parameter-payload-sha256:: 0075989a3d8159def1c0c0d9826df639a4e3becac5249087b8ba63ef4e20da9a
preset-synth-file:: [Emo — October 25 slot 270 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___270%20Emo___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: e429350c1a6520b51c3eb9480e37f71f908b7d5921f5a8f07e3042fe82f8f30d
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 270 over USB on October 25, 2026 with `mise run microfreak:download --slot 270`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 336, Factory 6.0 slot 411). Comparison used `mise run microfreak:compare`.
		- [Download the slot 270 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___270%20Emo___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/270 Emo/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SawX. [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
		- Saw Mod: 0.073. Shape: 0.000. Noise: 0.343.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.130; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.316, decay/release 0.208, sustain 0.528. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.374, RiseSlp 0.500, FallLvl 0.428, FallSlp 0.500, Hold 0.000, Amount 0.253. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync on; stored division code: 3. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.008.
		- Cycling Envelope → Wave: +0.823.
		- Cycling Envelope → Timbre: +0.156.
		- ENV → Cutoff: +1.000.
		- PRESSURE → Cutoff: +0.226.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
