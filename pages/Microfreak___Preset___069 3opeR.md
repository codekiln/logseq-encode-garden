logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 069
preset-synth-microfreak-name:: 3opeR
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/068 Canadian Bass]]
next:: [[Microfreak/Preset/070 Cliched Things]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
preset-synth-microfreak-parameter-payload-sha256:: c59ad1a9206c73614698e6b3a2bbb407348818f0044dcca40feb712fa9819d48
preset-synth-file:: [3opeR — October 25 slot 69 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___069%203opeR___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 1becb62f71456f781b4fd2d1ed397a22015ce1729634c9d19a7371381dddbaec
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 69 over USB on October 25, 2026 with `mise run microfreak:download --slot 69`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 156, Factory 1.1 slot 156, Factory 2.1 slot 153, Factory 3.0 slot 153, Factory 6.0 slot 408). Comparison used `mise run microfreak:compare`.
		- [Download the slot 69 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___069%203opeR___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/069 3opeR/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Two Op. FM. [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
		- Ratio: 0.247. Amount: 0.480. Shape: 0.436.
		- Keyboard octave: 0. Glide: 0.218.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.490; resonance: 0.723. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.330, sustain 0.520. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.088, RiseSlp 0.882, FallLvl 0.233, FallSlp 0.000, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 1.000. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.742.
		- PRESSURE → Timbre: +0.275.
		- Cycling Envelope → Cutoff: +0.175.
		- ENV → Cutoff: +0.145.
		- LFO → Cutoff: +0.010.
		- PRESSURE → Cutoff: +0.129.
		- KEY/ARP → Cutoff: +1.000.
		- PRESSURE → Assign 1 → Shape: +0.355.
		- LFO → Assign 2 → matrix amount LFO → Assign 2: +1.000.
		- PRESSURE → Assign 3 → Sustain: +0.405.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
