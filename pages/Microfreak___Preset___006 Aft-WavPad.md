logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 006
preset-synth-microfreak-name:: Aft-WavPad
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/005 MotivSeq]]
next:: [[Microfreak/Preset/007 Brd But Arp]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
preset-synth-microfreak-parameter-payload-sha256:: 18ffeee1cd4ff83de78e5551b2084dfb72ceaec1b1ac3a56845c4fb7ed577f9a
preset-synth-file:: [Aft-WavPad — October 25 slot 6 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___006%20Aft-WavPad___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 25bd41e5ce7e418689c968eeb4db89fe31291918869cfc72147f8ef0b3bdf960
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 6 over USB on October 25, 2026 with `mise run microfreak:download --slot 6`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0 (Factory 1.1 slot 6, Factory 2.1 slot 6, Factory 3.0 slot 6). Comparison used `mise run microfreak:compare`.
		- [Download the slot 6 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___006%20Aft-WavPad___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/006 Aft-WavPad/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Wavetable. [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
		- Table: 9 (stored choice code). Position: 0.344. Chorus: 1.000.
		- Keyboard octave: 0. Glide: 0.319.
	- ## Filter
		- High-pass filter. Saved cutoff: 0.000; resonance: 0.699. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.543, decay/release 0.614, sustain 0.201. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.536, RiseSlp 0.000, FallLvl 0.674, FallSlp 0.000, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.320. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Timbre: +0.449.
		- LFO → Timbre: +0.070.
		- PRESSURE → Timbre: −0.994.
		- ENV → Cutoff: +0.208.
		- PRESSURE → Cutoff: +0.798.
		- PRESSURE → Assign 1 → matrix amount LFO → Timbre: +0.114.
		- PRESSURE → Assign 2 → LFO Rate: +0.166.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
