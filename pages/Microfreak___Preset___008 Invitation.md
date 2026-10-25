logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 008
preset-synth-microfreak-name:: Invitation
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/007 Brd But Arp]]
next:: [[Microfreak/Preset/009 261e]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
preset-synth-microfreak-parameter-payload-sha256:: 143c74c76b55d467968c486cfaaeb26606d5d2b8cb6897669ec32e10444201f4
preset-synth-file:: [Invitation — October 25 slot 8 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___008%20Invitation___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 6c3b8545d9de3dd1a22c493c65f44734e20f6b0fdd0123d81165f2c96694b87f
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 8 over USB on October 25, 2026 with `mise run microfreak:download --slot 8`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0 (Factory 1.1 slot 10, Factory 2.1 slot 8, Factory 3.0 slot 8). Comparison used `mise run microfreak:compare`.
		- [Download the slot 8 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___008%20Invitation___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/008 Invitation/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SuperWave. [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
		- Wave: 1 (stored choice code). Detune: 0.151. Volume: 0.256.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.247; resonance: 0.526. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.552, decay/release 0.464, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.416, RiseSlp 0.000, FallLvl 0.346, FallSlp 0.000, Hold 0.122, Amount 0.176. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.191. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Timbre: +0.376.
		- PRESSURE → Timbre: −0.520.
		- ENV → Cutoff: +0.376.
		- PRESSURE → Cutoff: +0.525.
		- LFO → Assign 1 → Filter Resonance: +0.068.
		- LFO → Assign 2 → Oscillator Type: +0.010.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
