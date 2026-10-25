logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 013
preset-synth-microfreak-name:: Pikdown
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/012 Darkstream]]
next:: [[Microfreak/Preset/014 Bontempis]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
preset-synth-microfreak-parameter-payload-sha256:: 13acf2fa7d72c07100d62b15afbf21c76b7e93c701e9c9b2f0d1a343f7826416
preset-synth-file:: [Pikdown — October 25 slot 13 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___013%20Pikdown___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 432d2007b6c0e08bc0d59c8d9256946630b0bd8c93a5189f526e51c9e72e8b57
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 13 over USB on October 25, 2026 with `mise run microfreak:download --slot 13`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 102, Factory 2.1 slot 102, Factory 3.0 slot 102, Factory 6.0 slot 337). Comparison used `mise run microfreak:compare`.
		- [Download the slot 13 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___013%20Pikdown___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/013 Pikdown/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Chords. [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
		- Type: 3 (stored choice code). Inv/Transp: 0.818. Shape control: 0.238.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.113; resonance: 0.103. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.614, decay/release 0.965, sustain 0.066. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.000, RiseSlp 0.000, FallLvl 0.000, FallSlp 1.000, Hold 0.101, Amount 0.256. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sawtooth, clock sync on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.978.
		- PRESSURE → Wave: −1.000.
		- ENV → Timbre: −0.650.
		- PRESSURE → Timbre: −1.000.
		- Cycling Envelope → Cutoff: +0.951.
		- ENV → Cutoff: +0.749.
		- PRESSURE → Cutoff: +1.000.
		- KEY/ARP → Cutoff: +1.000.
		- ENV → Assign 1 → Cycling Envelope Rise: +0.341.
		- KEY/ARP → Assign 1 → Cycling Envelope Rise: +1.000.
		- ENV → Assign 2 → Shape: +0.264.
		- ENV → Assign 3 → LFO Rate: +1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
