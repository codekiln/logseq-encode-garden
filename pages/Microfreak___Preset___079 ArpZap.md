logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 079
preset-synth-microfreak-name:: ArpZap
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/078 A Juno Vibe]]
next:: [[Microfreak/Preset/080 Traditon]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
preset-synth-microfreak-parameter-payload-sha256:: 88661f285ed2bebead9e01b3d0ca1a79876d2db9a0065d0d3fd64c0cd13a2f25
preset-synth-file:: [ArpZap — October 25 slot 79 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___079%20ArpZap___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 8cc5fef304473d060422ddd1aea102be7c1e128c3814525751b7bf66229c42c6
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 79 over USB on October 25, 2026 with `mise run microfreak:download --slot 79`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 165, Factory 1.1 slot 165, Factory 2.1 slot 162, Factory 3.0 slot 162, Factory 6.0 slot 102). Comparison used `mise run microfreak:compare`.
		- [Download the slot 79 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___079%20ArpZap___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/079 ArpZap/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: BasicWaves. [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
		- Morph: 0.256. Sym: 0.000. Sub: 0.000.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.000; resonance: 1.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.377, sustain 0.000. Amp Mod is off. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.043, RiseSlp 1.000, FallLvl 0.409, FallSlp 0.000, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold, clock sync on; stored division code: 46877. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Pitch: +0.506.
		- Cycling Envelope → Cutoff: +1.000.
		- ENV → Cutoff: +0.405.
		- PRESSURE → Cutoff: +0.104.
		- KEY/ARP → Cutoff: +0.659.
		- ENV → Assign 1 → Decay/Release: −0.274.
		- LFO → Assign 1 → Decay/Release: +0.030.
		- Cycling Envelope → Assign 2 → Cycling Envelope Fall: −0.346.
		- PRESSURE → Assign 2 → Cycling Envelope Fall: −0.023.
		- LFO → Assign 3 → matrix amount ENV → Cutoff: −0.277.
		- PRESSURE → Assign 3 → matrix amount ENV → Cutoff: +0.273.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
