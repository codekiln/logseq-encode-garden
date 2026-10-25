logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 131
preset-synth-microfreak-name:: Colik
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/130 Sprt Brth]]
next:: [[Microfreak/Preset/132 Hold Riser]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
preset-synth-microfreak-parameter-payload-sha256:: c772ab3d351cd20b1c4278750643ac874fd4c80b5352c54d240d2762cfe40c3c
preset-synth-file:: [Colik — October 25 slot 131 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___131%20Colik___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 4bf67deb65d16df386a37577373fb6cc80d022ff340a8aad5f3f368be63da216
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 131 over USB on October 25, 2026 with `mise run microfreak:download --slot 131`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 108, Factory 2.1 slot 21, Factory 3.0 slot 21, Factory 6.0 slot None). Comparison used `mise run microfreak:compare`.
		- [Download the slot 131 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___131%20Colik___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/131 Colik/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Chords. [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
		- Type: 6 (stored choice code). Inv/Transp: 0.070. Shape control: 0.000.
		- Keyboard octave: 0. Glide: 0.220.
	- ## Filter
		- Low-pass filter. Saved cutoff: 1.000; resonance: 0.555. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.244, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.196, RiseSlp 0.500, FallLvl 0.210, FallSlp 0.500, Hold 0.000, Amount 0.538. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold, clock sync on; stored division code: 4. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Wave: +0.134.
		- ENV → Timbre: +0.302.
		- KEY/ARP → Cutoff: +1.000.
		- Cycling Envelope → Assign 1 → Shape: +0.897.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
