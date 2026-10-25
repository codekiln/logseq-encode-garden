logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 019
preset-synth-microfreak-name:: BrightBinary
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/018 Chip]]
next:: [[Microfreak/Preset/020 Arp-fi]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
preset-synth-microfreak-parameter-payload-sha256:: c69352e95a80d3c886fae40ec7232358524bdd41b1da0fba7369d932a357d722
preset-synth-file:: [BrightBinary — October 25 slot 19 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___019%20BrightBinary___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 6553558a0fcadec6add790dcffb7b70e166ad0c386a46a05fd942007ce4dd53d
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 19 over USB on October 25, 2026 with `mise run microfreak:download --slot 19`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 108, Factory 2.1 slot 108, Factory 3.0 slot 108, Factory 6.0 slot 126). Comparison used `mise run microfreak:compare`.
		- [Download the slot 19 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___019%20BrightBinary___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/019 BrightBinary/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: V.Analog. [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		- Detune: 0.500. Shape: 0.731. Wave: 0.511.
		- Keyboard octave: 0. Glide: 0.181.
	- ## Filter
		- High-pass filter. Saved cutoff: 0.397; resonance: 0.865. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.515, sustain 0.786. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.318, RiseSlp 0.500, FallLvl 0.753, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Square, clock sync on; stored division code: 3. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Wave: +0.113.
		- Cycling Envelope → Timbre: −0.562.
		- ENV → Cutoff: −0.374.
		- PRESSURE → Cutoff: +1.000.
		- KEY/ARP → Cutoff: −0.388.
		- Cycling Envelope → Assign 1 → `LFO.Div`: +0.691.
		- PRESSURE → Assign 1 → `LFO.Div`: +0.456.
		- PRESSURE → Assign 2 → matrix amount LFO → Cutoff: +0.310.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
