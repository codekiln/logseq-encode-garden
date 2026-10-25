logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 095
preset-synth-microfreak-name:: Boers
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/094 Gloudal]]
next:: [[Microfreak/Preset/096 Trapeurz]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
preset-synth-microfreak-parameter-payload-sha256:: 7cc4641e082acdd2c471769401c5d30a3c22931117228f0fd1bb867b7ef81124
preset-synth-file:: [Boers — October 25 slot 95 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___095%20Boers___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 617aeb51f6f306b0526aa3c0c1d8b4ec9dce78ebb4d7c469189c4c61f38de480
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 95 over USB on October 25, 2026 with `mise run microfreak:download --slot 95`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 182, Factory 2.1 slot 177, Factory 3.0 slot 177, Factory 6.0 slot 354). Comparison used `mise run microfreak:compare`.
		- [Download the slot 95 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___095%20Boers___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/095 Boers/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Wavetable. [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
		- Table: 13 (stored choice code). Position: 0.000. Chorus: 1.000.
		- Keyboard octave: -2. Glide: 0.208.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.203; resonance: 0.243. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.756, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.547, RiseSlp 0.500, FallLvl 0.538, FallSlp 0.500, Hold 0.000, Amount 0.718. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Timbre: +1.000.
		- LFO → Timbre: +0.042.
		- ENV → Cutoff: +0.663.
		- PRESSURE → Cutoff: +0.400.
		- PRESSURE → Assign 1 → `LFO.Div`: −0.196.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
