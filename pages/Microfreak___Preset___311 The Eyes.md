logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 311
preset-synth-microfreak-name:: The Eyes
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Vocoder]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/310 Arp Sing]]
next:: [[Microfreak/Preset/312 Shy Timbre]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/22 Vocoder]]
preset-synth-microfreak-parameter-payload-sha256:: 238a4e025613e7a2d392e2cd5f54b9a6b7deb8f21659fe2b790812b910b91739
preset-synth-file:: [The Eyes — October 25 slot 311 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___311%20The%20Eyes___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 8afc19b416b723ff925de496dad74b9ed87f523baf19e5d7344b3fe78541e76e
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 311 over USB on October 25, 2026 with `mise run microfreak:download --slot 311`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.1 slot 58, Factory 3.0 slot 373, Factory 6.0 slot 345). Comparison used `mise run microfreak:compare`.
		- [Download the slot 311 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___311%20The%20Eyes___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/311 The Eyes/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Vocoder. [[Microfreak/UG/06 Dig Osc/03 Types/22 Vocoder]]
		- Wave: 0.507. Timbre: 0.168. Shape: 0.384.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.997; resonance: 0.607. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.296, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.097, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.697. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Timbre: +0.375.
		- KEY/ARP → Timbre: +1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
