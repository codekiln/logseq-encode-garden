logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 312
preset-synth-microfreak-name:: Shy Timbre
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Vocoder]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/311 The Eyes]]
next:: [[Microfreak/Preset/313 Tremolo Saw]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/22 Vocoder]]
preset-synth-microfreak-parameter-payload-sha256:: c805583f300d64869b98b54ad143bbcc9d4103a727d494d134d6faf50379807f
preset-synth-file:: [Shy Timbre — October 25 slot 312 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___312%20Shy%20Timbre___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 3af688305bff2fc9f6b8ab5e77557feeecf0a33f933e6bfce97d8152ca49e602
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 312 over USB on October 25, 2026 with `mise run microfreak:download --slot 312`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.1 slot 59, Factory 3.0 slot 374, Factory 6.0 slot 159). Comparison used `mise run microfreak:compare`.
		- [Download the slot 312 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___312%20Shy%20Timbre___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/312 Shy Timbre/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Vocoder. [[Microfreak/UG/06 Dig Osc/03 Types/22 Vocoder]]
		- Wave: 1.000. Timbre: 0.523. Shape: 0.001.
		- Keyboard octave: -2. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.860; resonance: 0.541. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.265, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.214, RiseSlp 0.500, FallLvl 0.498, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync off; stored normalized rate: 0.810. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- All saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
