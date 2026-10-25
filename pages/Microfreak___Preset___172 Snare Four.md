logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 172
preset-synth-microfreak-name:: Snare Four
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Percussion]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/171 Prof]]
next:: [[Microfreak/Preset/173 AfterBurner]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
preset-synth-microfreak-parameter-payload-sha256:: 8b08d10bf74d4380de4b39df7485ca124bee2b9bfa5d32216a62695aec4df949
preset-synth-file:: [Snare Four — October 25 slot 172 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___172%20Snare%20Four___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 7a760462961462a57695fb51617b107c2436aeca60adfc7553eb3c75ec979908
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 172 over USB on October 25, 2026 with `mise run microfreak:download --slot 172`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 145, Factory 2.1 slot 247, Factory 3.0 slot 247, Factory 6.0 slot 28). Comparison used `mise run microfreak:compare`.
		- [Download the slot 172 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___172%20Snare%20Four___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/172 Snare Four/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Noise. [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
		- Wave: 0.333. Timbre: 0.785. Shape: 0.000.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.629; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.136, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.163, RiseSlp 0.500, FallLvl 0.163, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 46877. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Cutoff: +1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
