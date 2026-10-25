logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 208
preset-synth-microfreak-name:: Boarding
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/207 Bells 2]]
next:: [[Microfreak/Preset/209 Dirty]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: 937ca13fb01ca16a0025e7fabac67f896e00a945e47ff21798f599a7e7d4f7c6
preset-synth-file:: [Boarding — October 25 slot 208 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___208%20Boarding___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: b0cbdcfd69e7e34baa3d03dca93537feebf84e87fcbca9d0d302090ee4cd3d21
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 208 over USB on October 25, 2026 with `mise run microfreak:download --slot 208`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 28, Factory 6.0 slot None). Comparison used `mise run microfreak:compare`.
		- [Download the slot 208 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___208%20Boarding___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/208 Boarding/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 0.547. Rectification: 0.402. Noise: 0.255.
		- Keyboard octave: 0. Glide: 0.025.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.772; resonance: 0.226. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.252, decay/release 0.530, sustain 0.923. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.692, RiseSlp 0.500, FallLvl 0.438, FallSlp 0.500, Hold 0.000, Amount 0.459. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold, clock sync on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Wave: +0.219.
		- LFO → Timbre: +0.659.
		- ENV → Cutoff: +0.732.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
