logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 181
preset-synth-microfreak-name:: Toy Piano
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Template]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/180 7th Keys]]
next:: [[Microfreak/Preset/182 Vibra]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
preset-synth-microfreak-parameter-payload-sha256:: 4584e4628a0df939c1aa19cf1370d4c17d0729b8f039a67a661f0fd5a60dddd3
preset-synth-file:: [Toy Piano — October 25 slot 181 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___181%20Toy%20Piano___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: d49db7fc65bd7101aca4b1b3353ce2eab497a19fa7903ba0b5a8d39768e35068
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 181 over USB on October 25, 2026 with `mise run microfreak:download --slot 181`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 211, Factory 2.1 slot 255, Factory 3.0 slot 255, Factory 6.0 slot 334). Comparison used `mise run microfreak:compare`.
		- [Download the slot 181 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___181%20Toy%20Piano___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/181 Toy Piano/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Two Op. FM. [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
		- Ratio: 0.000. Amount: 0.000. Shape: 0.000.
		- Keyboard octave: +1. Glide: 0.079.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.480; resonance: 0.504. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.291, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.206, FallSlp 0.168, Hold 0.000, Amount 0.239. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync on; stored division code: 7. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.003.
		- Cycling Envelope → Timbre: +1.000.
		- PRESSURE → Timbre: +0.257.
		- ENV → Cutoff: +0.212.
		- PRESSURE → Cutoff: +1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
