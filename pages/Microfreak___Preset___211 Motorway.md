logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 211
preset-synth-microfreak-name:: Motorway
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/210 Movie Chase]]
next:: [[Microfreak/Preset/212 Raver]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: 793cb10f5eb7e74e1283afd3a0fd7cdc3a5604c6b7e7f1b390de1266a9f09e0d
preset-synth-file:: [Motorway — October 25 slot 211 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___211%20Motorway___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: f97a57692e3ae9fad220bfb61957e7a2d8e1d145ca9488464e63437f1474a487
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 211 over USB on October 25, 2026 with `mise run microfreak:download --slot 211`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 282, Factory 6.0 slot 361). Comparison used `mise run microfreak:compare`.
		- [Download the slot 211 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___211%20Motorway___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/211 Motorway/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 0.526. Rectification: 0.726. Noise: 0.334.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.602; resonance: 0.570. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.329, sustain 0.279. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.371, RiseSlp 0.000, FallLvl 0.290, FallSlp 0.479, Hold 0.364, Amount 0.206. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync off; stored normalized rate: 0.175. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Wave: +0.060.
		- LFO → Wave: +0.003.
		- Cycling Envelope → Timbre: +0.144.
		- LFO → Timbre: −0.218.
		- Cycling Envelope → Cutoff: −0.660.
		- ENV → Cutoff: +1.000.
		- ENV → Assign 1 → Cycling Envelope Amount: +0.213.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
