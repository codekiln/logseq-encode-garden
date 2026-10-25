logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 274
preset-synth-microfreak-name:: Sardine
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/273 Good]]
next:: [[Microfreak/Preset/275 Malin]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: f2f1c808be07d49cc65114e06a5066f5979ed933ade553e7498973546a77339e
preset-synth-file:: [Sardine — October 25 slot 274 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___274%20Sardine___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 3d4a19ecb98ef6536bde7cdbfa5ddfc857c7fae7bfde72a24a3894b53850074c
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 274 over USB on October 25, 2026 with `mise run microfreak:download --slot 274`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 34, Factory 6.0 slot None). Comparison used `mise run microfreak:compare`.
		- [Download the slot 274 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___274%20Sardine___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/274 Sardine/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 0.410. Rectification: 0.127. Noise: 0.062.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.517; resonance: 0.443. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.222, decay/release 0.608, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.103, RiseSlp 0.500, FallLvl 0.210, FallSlp 0.500, Hold 0.000, Amount 0.593. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 2. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Wave: +0.304.
		- Cycling Envelope → Timbre: +0.652.
		- Cycling Envelope → Cutoff: +0.322.
		- ENV → Cutoff: +0.091.
		- PRESSURE → Cutoff: +0.654.
		- LFO → Assign 1 → Cycling Envelope Rise: +0.160.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
