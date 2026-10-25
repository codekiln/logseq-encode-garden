logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 025
preset-synth-microfreak-name:: 808 St8 M8
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/024 Stan2]]
next:: [[Microfreak/Preset/026 L9n1]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
preset-synth-microfreak-parameter-payload-sha256:: d0791bb57e199d9c1df79d57bddf69b5f6ab3e3da6d24cbb3bf78d5da9ff0ef9
preset-synth-file:: [808 St8 M8 — October 25 slot 25 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___025%20808%20St8%20M8___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 92ca11e29529ecce7ed0289f47567ab131e171fdd37ba9033f8da31afe8ab99c
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 25 over USB on October 25, 2026 with `mise run microfreak:download --slot 25`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 113, Factory 2.1 slot 113, Factory 3.0 slot 113, Factory 6.0 slot 30). Comparison used `mise run microfreak:compare`.
		- [Download the slot 25 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___025%20808%20St8%20M8___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/025 808 St8 M8/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Chords. [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
		- Type: 9 (stored choice code). Inv/Transp: 0.000. Shape control: 0.105.
		- Keyboard octave: 0. Glide: 0.163.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.000; resonance: 0.729. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.259, decay/release 0.607, sustain 0.728. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.072, RiseSlp 0.000, FallLvl 0.400, FallSlp 0.000, Hold 0.195, Amount 0.999. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.132. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Timbre: +0.080.
		- Cycling Envelope → Cutoff: +0.194.
		- ENV → Cutoff: +0.490.
		- LFO → Cutoff: +0.138.
		- PRESSURE → Cutoff: +0.072.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
