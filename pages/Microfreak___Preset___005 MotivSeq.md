logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 005
preset-synth-microfreak-name:: MotivSeq
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/004 Ether]]
next:: [[Microfreak/Preset/006 Aft-WavPad]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
preset-synth-microfreak-parameter-payload-sha256:: c55113dcba9f69be07cce9b198668cac4e4808c21fdd488a68b18573d851f175
preset-synth-file:: [MotivSeq — October 25 slot 5 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___005%20MotivSeq___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: dac9a9cf6946b22c516b3db5b18be1ad869f6c375b7fa7999d258ca66f980d04
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 5 over USB on October 25, 2026 with `mise run microfreak:download --slot 5`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 5, Factory 2.1 slot 5, Factory 3.0 slot 5, Factory 6.0 slot None). Comparison used `mise run microfreak:compare`.
		- [Download the slot 5 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___005%20MotivSeq___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/005 MotivSeq/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SuperWave. [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
		- Wave: 0 (stored choice code). Detune: 0.471. Volume: 0.655.
		- Keyboard octave: 0. Glide: 0.034.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.996; resonance: 0.805. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.025, decay/release 0.296, sustain 0.281. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.498, FallSlp 0.000, Hold 0.000, Amount 0.550. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold, clock sync on; stored division code: 8. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- KEY/ARP → Wave: +0.501.
		- Cycling Envelope → Timbre: +1.000.
		- ENV → Timbre: −0.472.
		- ENV → Cutoff: +0.186.
		- PRESSURE → Cutoff: −0.445.
		- LFO → Assign 1 → Glide: +0.111.
		- LFO → Assign 2 → Decay/Release: +0.142.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
