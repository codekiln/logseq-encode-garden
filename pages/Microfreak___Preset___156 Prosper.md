logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 156
preset-synth-microfreak-name:: Prosper
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/155 Paralex]]
next:: [[Microfreak/Preset/157 Ice Cold]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
preset-synth-microfreak-parameter-payload-sha256:: b9d8f28f016caa3694eaf12e6c048243b9ec144ff6b7db563d4f851341e7e89a
preset-synth-file:: [Prosper — October 25 slot 156 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___156%20Prosper___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: e925d56caf6aff80c6c19af4f861573d6ebe7a094a39e21c8ef1ecaf394acada
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 156 over USB on October 25, 2026 with `mise run microfreak:download --slot 156`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 130, Factory 2.1 slot 232, Factory 3.0 slot 232, Factory 6.0 slot 267). Comparison used `mise run microfreak:compare`.
		- [Download the slot 156 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___156%20Prosper___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/156 Prosper/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Noise. [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
		- Wave: 1.000. Timbre: 0.506. Shape: 1.000.
		- Keyboard octave: -1. Glide: 0.135.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.000; resonance: 0.336. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.300, sustain 0.007. Amp Mod is off. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.249, RiseSlp 1.000, FallLvl 0.246, FallSlp 0.000, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync on; stored division code: 2. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Timbre: +0.300.
		- KEY/ARP → Timbre: +0.997.
		- ENV → Cutoff: +0.763.
		- LFO → Cutoff: +0.064.
		- PRESSURE → Cutoff: +0.242.
		- KEY/ARP → Cutoff: +0.192.
		- Cycling Envelope → Assign 2 → Filter Resonance: +0.559.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
