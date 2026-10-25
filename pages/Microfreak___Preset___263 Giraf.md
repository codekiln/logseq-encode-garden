logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 263
preset-synth-microfreak-name:: Giraf
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/262 Pled]]
next:: [[Microfreak/Preset/264 Disaster]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: e205f63d7e1a0d42b50b6f5f8ee3b8effd653cabc8c1d61d15492b32cb956345
preset-synth-file:: [Giraf — October 25 slot 263 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___263%20Giraf___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 99b47aa88f3fa6655dc2865f485225a81f38283d76409c5a24951a1c47eb6045
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 263 over USB on October 25, 2026 with `mise run microfreak:download --slot 263`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 33, Factory 6.0 slot None). Comparison used `mise run microfreak:compare`.
		- [Download the slot 263 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___263%20Giraf___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/263 Giraf/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 0.390. Rectification: 0.276. Noise: 0.215.
		- Keyboard octave: +1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.512; resonance: 0.664. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.938, decay/release 0.609, sustain 0.609. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.116, RiseSlp 0.500, FallLvl 0.345, FallSlp 0.500, Hold 0.000, Amount 0.680. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 1. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Wave: +0.068.
		- PRESSURE → Timbre: +1.000.
		- Cycling Envelope → Cutoff: +0.142.
		- LFO → Assign 1 → Cycling Envelope Fall: +0.193.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
