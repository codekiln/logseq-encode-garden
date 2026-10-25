logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 241
preset-synth-microfreak-name:: Numnum Yoy
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/240 Move U Head]]
next:: [[Microfreak/Preset/242 93s  Rave]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
preset-synth-microfreak-parameter-payload-sha256:: 6c0c201f52885f2f4297963162c2853a9cb1db44e6762eb013eeeddde72da14c
preset-synth-file:: [Numnum Yoy — October 25 slot 241 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___241%20Numnum%20Yoy___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 82f8f585b48f2606819e8518def145190133b415b0cc6a644ae744b2559483fe
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 241 over USB on October 25, 2026 with `mise run microfreak:download --slot 241`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 31, Factory 6.0 slot None). Comparison used `mise run microfreak:compare`.
		- [Download the slot 241 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___241%20Numnum%20Yoy___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/241 Numnum Yoy/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Bass. [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
		- Saturate: 0.052. Fold: 0.017. Noise: 0.000.
		- Keyboard octave: -2. Glide: 0.123.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.848; resonance: 0.951. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.801, sustain 0.341. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 1.000, FallLvl 0.438, FallSlp 0.000, Hold 0.447, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 12. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.003.
		- PRESSURE → Wave: +1.000.
		- Cycling Envelope → Timbre: +1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
