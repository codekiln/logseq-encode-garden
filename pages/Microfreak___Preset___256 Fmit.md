logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 256
preset-synth-microfreak-name:: Fmit
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/255 WubbliDub]]
next:: [[Microfreak/Preset/257 Power Touch]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/12 Modal]]
preset-synth-microfreak-parameter-payload-sha256:: 1939d1499956f947c366a23e36ac711f32f6cf77566b80950e2f64053cc3e4b7
preset-synth-file:: [Fmit — October 25 slot 256 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___256%20Fmit___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 3c985ffc5b3f28e288244d31a83afa2f4d0ef32ef9f99b1da3d91e8978deb252
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 256 over USB on October 25, 2026 with `mise run microfreak:download --slot 256`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 323, Factory 6.0 slot 183). Comparison used `mise run microfreak:compare`.
		- [Download the slot 256 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___256%20Fmit___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/256 Fmit/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Modal. [[Microfreak/UG/06 Dig Osc/03 Types/12 Modal]]
		- Inharm: 1.000. Timbre: 1.000. Decay: 0.998.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Band-pass filter. Saved cutoff: 0.259; resonance: 0.563. [[Microfreak/UG/07 Filter/01 Modifying Sound/02 Band Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.000, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.095, RiseSlp 0.500, FallLvl 0.093, FallSlp 0.000, Hold 0.000, Amount 0.200. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold, clock sync on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +1.000.
		- ENV → Pitch: +0.265.
		- Cycling Envelope → Wave: +1.000.
		- LFO → Wave: +0.052.
		- Cycling Envelope → Timbre: +0.878.
		- LFO → Timbre: +0.001.
		- ENV → Cutoff: +0.274.
		- PRESSURE → Cutoff: +0.176.
		- KEY/ARP → Cutoff: +0.866.
		- PRESSURE → Assign 2 → Decay/Release: −0.055.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
