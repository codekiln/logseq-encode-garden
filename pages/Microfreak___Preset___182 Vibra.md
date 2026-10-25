logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 182
preset-synth-microfreak-name:: Vibra
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Template]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/181 Toy Piano]]
next:: [[Microfreak/Preset/183 JP Strings]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
preset-synth-microfreak-parameter-payload-sha256:: cb601c1f67112b4969c19f0716bbe2c1c40a56d5116996e1064b76c22635401f
preset-synth-file:: [Vibra — October 25 slot 182 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___182%20Vibra___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: c32512fbc53f083d5cc67760fb68d8ca01160cbffb5d0e38f7cd24bf8fe011e0
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 182 over USB on October 25, 2026 with `mise run microfreak:download --slot 182`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0 (Factory 1.1 slot 212, Factory 2.1 slot 256, Factory 3.0 slot 256). Comparison used `mise run microfreak:compare`.
		- [Download the slot 182 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___182%20Vibra___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/182 Vibra/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Two Op. FM. [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
		- Ratio: 1.000. Amount: 0.094. Shape: 0.528.
		- Keyboard octave: +1. Glide: 0.000.
	- ## Filter
		- High-pass filter. Saved cutoff: 0.094; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.260, sustain 0.197. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.354, FallSlp 0.168, Hold 0.000, Amount 0.402. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Timbre: +1.000.
		- PRESSURE → Timbre: +0.257.
		- ENV → Cutoff: +0.062.
		- LFO → Cutoff: +0.108.
		- PRESSURE → Cutoff: +1.000.
		- KEY/ARP → Cutoff: +1.000.
		- ENV → Assign 1 → matrix amount LFO → Cutoff: −0.114.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
