logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 067
preset-synth-microfreak-name:: Angels
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/066 Vanarx]]
next:: [[Microfreak/Preset/068 Canadian Bass]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
preset-synth-microfreak-parameter-payload-sha256:: d269e68c016a056caa49a67b9e5060993bb82ae1a0702f62d02403e3263dd1dc
preset-synth-file:: [Angels — October 25 slot 67 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___067%20Angels___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 2706d4ad67f2fb0acfd8ee8ea9ef8dd886309f37d2fb6dececb8492e03d15a37
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 67 over USB on October 25, 2026 with `mise run microfreak:download --slot 67`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0 (Factory 1.1 slot 154, Factory 2.1 slot 151, Factory 3.0 slot 151). Comparison used `mise run microfreak:compare`.
		- [Download the slot 67 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___067%20Angels___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/067 Angels/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SuperWave. [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
		- Wave: 2 (stored choice code). Detune: 0.572. Volume: 0.514.
		- Keyboard octave: 0. Glide: 0.126.
	- ## Filter
		- Band-pass filter. Saved cutoff: 0.153; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/02 Band Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.086, decay/release 0.546, sustain 0.495. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.163, RiseSlp 0.500, FallLvl 0.163, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sawtooth, clock sync on; stored division code: 8. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Timbre: −0.002.
		- ENV → Cutoff: +0.749.
		- PRESSURE → Assign 1 → matrix amount LFO → Timbre: −0.788.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
