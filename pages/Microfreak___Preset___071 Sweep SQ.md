logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 071
preset-synth-microfreak-name:: Sweep SQ
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/070 Cliched Things]]
next:: [[Microfreak/Preset/072 Buzzsaw]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
preset-synth-microfreak-parameter-payload-sha256:: b7902fd406249ca2ab740bbb3894d0aee49d305105a93f2c0241b903ccf21478
preset-synth-file:: [Sweep SQ — October 25 slot 71 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___071%20Sweep%20SQ___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 677dcc4d1f4743769c59ddccf783a5138afdada7a286648aaf7b5e639755eb77
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 71 over USB on October 25, 2026 with `mise run microfreak:download --slot 71`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0 (Factory 1.0 slot 158, Factory 1.1 slot 158, Factory 2.1 slot 155, Factory 3.0 slot 155). Comparison used `mise run microfreak:compare`.
		- [Download the slot 71 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___071%20Sweep%20SQ___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/071 Sweep SQ/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Two Op. FM. [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
		- Ratio: 0.797. Amount: 0.179. Shape: 0.605.
		- Keyboard octave: 0. Glide: 0.366.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.819; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.476, sustain 0.248. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.000, FallLvl 0.297, FallSlp 0.000, Hold 0.060, Amount 0.094. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync on; stored division code: 9. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.005.
		- ENV → Timbre: +0.521.
		- LFO → Timbre: +0.040.
		- Cycling Envelope → Cutoff: +<0.001.
		- ENV → Cutoff: +0.315.
		- LFO → Cutoff: −0.048.
		- PRESSURE → Cutoff: +1.000.
		- LFO → Assign 1 → Sustain: +0.848.
		- LFO → Assign 2 → `Mat.Assign2`: +0.001.
		- PRESSURE → Assign 3 → Cycling Envelope Amount: +0.503.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
