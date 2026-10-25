logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 207
preset-synth-microfreak-name:: Bells 2
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Template]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/206 Bells 1]]
next:: [[Microfreak/Preset/208 Boarding]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
preset-synth-microfreak-parameter-payload-sha256:: 2fb218974ccfd9061963f30c1452c25240f1d29ca28d7305b2b91f07f1a1c9ef
preset-synth-file:: [Bells 2 — October 25 slot 207 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___207%20Bells%202___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 6a0b459f7adc035bf1af91c92f5d5797b1eb8944857bda36c361535ca0a6115d
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 207 over USB on October 25, 2026 with `mise run microfreak:download --slot 207`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 235, Factory 2.1 slot 50, Factory 3.0 slot 279, Factory 6.0 slot 225). Comparison used `mise run microfreak:compare`.
		- [Download the slot 207 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___207%20Bells%202___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/207 Bells 2/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Two Op. FM. [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
		- Ratio: 0.727. Amount: 0.315. Shape: 0.213.
		- Keyboard octave: 0. Glide: 0.157.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.992; resonance: 0.654. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.551, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.189, RiseSlp 0.500, FallLvl 0.163, FallSlp 0.500, Hold 0.000, Amount 0.841. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 9. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Timbre: +0.018.
		- ENV → Cutoff: +0.096.
		- PRESSURE → Cutoff: −0.405.
		- KEY/ARP → Cutoff: +0.693.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
