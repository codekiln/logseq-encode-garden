logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 249
preset-synth-microfreak-name:: RisoLFO
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/248 GrowLing]]
next:: [[Microfreak/Preset/250 Organic Random]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
preset-synth-microfreak-parameter-payload-sha256:: 767ebafe0a7fa24a307db4610fc283bfd550555747a728413caa55ffc2b652d7
preset-synth-file:: [RisoLFO — October 25 slot 249 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___249%20RisoLFO___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 1144efd8db7987294c278dadd2853dd3b33e0a660ff393b3bd09229f455c3ca9
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 249 over USB on October 25, 2026 with `mise run microfreak:download --slot 249`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 317, Factory 6.0 slot 403). Comparison used `mise run microfreak:compare`.
		- [Download the slot 249 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___249%20RisoLFO___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/249 RisoLFO/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Two Op. FM. [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
		- Ratio: 0.309. Amount: 0.739. Shape: 0.990.
		- Keyboard octave: 0. Glide: 0.003.
	- ## Filter
		- Band-pass filter. Saved cutoff: 0.367; resonance: 0.694. [[Microfreak/UG/07 Filter/01 Modifying Sound/02 Band Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.259, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.953, RiseSlp 0.636, FallLvl 0.333, FallSlp 0.109, Hold 0.320, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.570.
		- Cycling Envelope → Wave: −0.057.
		- Cycling Envelope → Timbre: +0.324.
		- Cycling Envelope → Cutoff: −0.594.
		- Cycling Envelope → Assign 2 → Shape: +0.754.
		- Cycling Envelope → Assign 3 → Unison Spread: +0.701.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
