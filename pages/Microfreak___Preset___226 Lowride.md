logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 226
preset-synth-microfreak-name:: Lowride
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/225 Neutrino A]]
next:: [[Microfreak/Preset/227 Midnight Pad]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/07 Waveshaper]]
preset-synth-microfreak-parameter-payload-sha256:: e431227091385a472fb0d3cbd98fcff07540b0d3b7c601c1635fe25a4cbcf168
preset-synth-file:: [Lowride — October 25 slot 226 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___226%20Lowride___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 4f139fc68637c5241370b8703b6dea41e1c516f13297a567677840e7e30cb4ee
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 226 over USB on October 25, 2026 with `mise run microfreak:download --slot 226`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 296, Factory 6.0 slot 295). Comparison used `mise run microfreak:compare`.
		- [Download the slot 226 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___226%20Lowride___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/226 Lowride/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Waveshaper. [[Microfreak/UG/06 Dig Osc/03 Types/07 Waveshaper]]
		- Wave: 0.498. Amount: 0.498. Asym: 0.000.
		- Keyboard octave: -2. Glide: 0.089.
	- ## Filter
		- Low-pass filter. Saved cutoff: 1.000; resonance: 0.366. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.511, sustain 0.034. Amp Mod is off. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.249, RiseSlp 1.000, FallLvl 0.246, FallSlp 0.000, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync on; stored division code: 3. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Timbre: +0.300.
		- KEY/ARP → Timbre: +0.997.
		- ENV → Cutoff: +0.756.
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
