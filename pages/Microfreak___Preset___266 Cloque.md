logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 266
preset-synth-microfreak-name:: Cloque
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/265 Bliss]]
next:: [[Microfreak/Preset/267 Tracteur]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
preset-synth-microfreak-parameter-payload-sha256:: 512012ced36827de75fd8b23aec39833697b713dca66271ddef16448f08baef8
preset-synth-file:: [Cloque — October 25 slot 266 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___266%20Cloque___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: cd186e44c09b49802c288e013c93eb6b3bd328c2025d0423612b9956d6cca656
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 266 over USB on October 25, 2026 with `mise run microfreak:download --slot 266`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 332, Factory 6.0 slot 281). Comparison used `mise run microfreak:compare`.
		- [Download the slot 266 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___266%20Cloque___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/266 Cloque/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Bass. [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
		- Saturate: 0.400. Fold: 0.172. Noise: 0.000.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.305; resonance: 0.383. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.437, decay/release 0.621, sustain 0.984. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.538, RiseSlp 0.500, FallLvl 0.601, FallSlp 0.500, Hold 0.337, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 6. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.008.
		- PRESSURE → Wave: +0.358.
		- Cycling Envelope → Timbre: +0.255.
		- Cycling Envelope → Cutoff: +0.326.
		- ENV → Cutoff: +0.287.
		- LFO → Assign 1 → Cycling Envelope Amount: −0.753.
		- LFO → Assign 2 → Cycling Envelope Fall: −0.119.
		- Cycling Envelope → Assign 3 → `LFO.Div`: −0.471.
		- LFO → Assign 3 → `LFO.Div`: −0.410.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
