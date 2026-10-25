logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 228
preset-synth-microfreak-name:: Last Days
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/227 Midnight Pad]]
next:: [[Microfreak/Preset/229 Japan Xeno]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
preset-synth-microfreak-parameter-payload-sha256:: 6a5b7615b8edd2f28cde23c069570cb1360e206e29dfc818a9109001b2e6d8e0
preset-synth-file:: [Last Days — October 25 slot 228 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___228%20Last%20Days___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 057978b633e8c5600883e25affcaa7e2d70e94af5ee0e2fc816f165bd8e1b25b
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 228 over USB on October 25, 2026 with `mise run microfreak:download --slot 228`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 298, Factory 6.0 slot 387). Comparison used `mise run microfreak:compare`.
		- [Download the slot 228 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___228%20Last%20Days___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/228 Last Days/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Bass. [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
		- Saturate: 0.923. Fold: 0.298. Noise: 0.047.
		- Keyboard octave: 0. Glide: 0.106.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.763; resonance: 0.676. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.532, sustain 0.758. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.232, FallSlp 0.500, Hold 0.539, Amount 0.086. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync on; stored division code: 0. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.005.
		- ENV → Wave: +0.199.
		- LFO → Timbre: +0.063.
		- PRESSURE → Cutoff: +0.339.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
