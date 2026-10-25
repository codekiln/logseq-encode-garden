logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 180
preset-synth-microfreak-name:: 7th Keys
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Template]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/179 Keys 2]]
next:: [[Microfreak/Preset/181 Toy Piano]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
preset-synth-microfreak-parameter-payload-sha256:: b72271e73c61598d97f52323049a4a79f315510df589e11b24db4357cff74b08
preset-synth-file:: [7th Keys — October 25 slot 180 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___180%207th%20Keys___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: a305428e1486d7bbd0e8eff4e894c836f563997f04c79c9757ca4ab92ed3ced0
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 180 over USB on October 25, 2026 with `mise run microfreak:download --slot 180`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 210, Factory 2.1 slot 254, Factory 3.0 slot 254, Factory 6.0 slot 375). Comparison used `mise run microfreak:compare`.
		- [Download the slot 180 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___180%207th%20Keys___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/180 7th Keys/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: V.Analog. [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		- Detune: 0.617. Shape: 0.517. Wave: 0.307.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.827; resonance: 0.646. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.331, sustain 0.489. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.480, RiseSlp 0.500, FallLvl 0.163, FallSlp 0.500, Hold 0.000, Amount 0.841. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 8. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Cutoff: +0.812.
		- PRESSURE → Cutoff: +0.225.
		- KEY/ARP → Cutoff: +0.693.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
