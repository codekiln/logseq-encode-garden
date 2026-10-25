logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 264
preset-synth-microfreak-name:: Disaster
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/263 Giraf]]
next:: [[Microfreak/Preset/265 Bliss]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: e536b39abb7c79086eeb2bf0a780cbd64e6270ae1b3a3aba2ef4a4574af49825
preset-synth-file:: [Disaster — October 25 slot 264 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___264%20Disaster___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: f32b9095401714da6f4623ca229833087c54b82152bac538b28d09f461567cf9
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 264 over USB on October 25, 2026 with `mise run microfreak:download --slot 264`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 330, Factory 6.0 slot 300). Comparison used `mise run microfreak:compare`.
		- [Download the slot 264 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___264%20Disaster___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/264 Disaster/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 0.551. Rectification: 0.690. Noise: 0.000.
		- Keyboard octave: 0. Glide: 0.104.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.142; resonance: 0.494. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.025, decay/release 0.301, sustain 0.338. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.212, FallSlp 0.500, Hold 0.000, Amount 0.742. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 0. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Wave: +0.139.
		- Cycling Envelope → Timbre: +0.457.
		- ENV → Cutoff: +0.547.
		- LFO → Cutoff: +0.158.
		- Cycling Envelope → Assign 1 → Noise: +0.862.
		- PRESSURE → Assign 2 → Noise: +0.897.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
