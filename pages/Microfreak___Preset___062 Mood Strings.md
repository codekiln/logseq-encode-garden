logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 062
preset-synth-microfreak-name:: Mood Strings
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Strings]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/061 AftrBlush]]
next:: [[Microfreak/Preset/063 Kendrok]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
preset-synth-microfreak-parameter-payload-sha256:: 1696b3f12e4362ff654f70515b0124ff3a40f20a97fcb076bd5818fd51667439
preset-synth-file:: [Mood Strings — October 25 slot 62 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___062%20Mood%20Strings___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: b02adfd8de9f63c178ca2eea5d29455cea54630900694bb40d0679183adbe673
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 62 over USB on October 25, 2026 with `mise run microfreak:download --slot 62`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 148, Factory 2.1 slot 147, Factory 3.0 slot 147, Factory 6.0 slot 109). Comparison used `mise run microfreak:compare`.
		- [Download the slot 62 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___062%20Mood%20Strings___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/062 Mood Strings/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SuperWave. [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
		- Wave: 0 (stored choice code). Detune: 0.533. Volume: 0.498.
		- Keyboard octave: +1. Glide: 0.272.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.293; resonance: 0.133. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.742, decay/release 0.953, sustain 0.998. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.827, RiseSlp 0.500, FallLvl 0.737, FallSlp 0.500, Hold 0.005, Amount 0.995. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 46877. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Timbre: +0.644.
		- PRESSURE → Timbre: −0.641.
		- ENV → Cutoff: +0.645.
		- PRESSURE → Cutoff: −0.215.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
