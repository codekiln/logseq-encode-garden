logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 297
preset-synth-microfreak-name:: Shiny Hat
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Percussion]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/296 Kick It]]
next:: [[Microfreak/Preset/298 King Snap]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: bc3bda682db3d9a5a1f579e2d69f9ba9af73886130c24b10d8e272c377250eb8
preset-synth-file:: [Shiny Hat — October 25 slot 297 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___297%20Shiny%20Hat___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 86f2110553d788052ee9ef5a480c41ed1cabb5e86b59430097412e0abae8321d
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 297 over USB on October 25, 2026 with `mise run microfreak:download --slot 297`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 360, Factory 6.0 slot 192). Comparison used `mise run microfreak:compare`.
		- [Download the slot 297 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___297%20Shiny%20Hat___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/297 Shiny Hat/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 0.000. Rectification: 1.000. Noise: 1.000.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- High-pass filter. Saved cutoff: 0.835; resonance: 1.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.018, decay/release 0.010, sustain 0.036. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.163, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Cutoff: +0.057.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
