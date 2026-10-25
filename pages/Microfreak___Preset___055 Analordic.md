logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 055
preset-synth-microfreak-name:: Analordic
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/054 Michtack]]
next:: [[Microfreak/Preset/056 PowerStab]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
preset-synth-microfreak-parameter-payload-sha256:: aede901f3328a7e6b904dfe38136b2db87287a96410385913c0c7e881e82f178
preset-synth-file:: [Analordic — October 25 slot 55 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___055%20Analordic___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: b78c7457446b24b25421e14efa174d91d5d3b25e45080fb726b200ef0f96e18d
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 55 over USB on October 25, 2026 with `mise run microfreak:download --slot 55`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 140, Factory 2.1 slot 140, Factory 3.0 slot 140, Factory 6.0 slot 436). Comparison used `mise run microfreak:compare`.
		- [Download the slot 55 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___055%20Analordic___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/055 Analordic/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: V.Analog. [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		- Detune: 0.498. Shape: 0.030. Wave: 0.000.
		- Keyboard octave: +1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.151; resonance: 0.441. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.249, decay/release 0.822, sustain 0.959. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.146, RiseSlp 0.500, FallLvl 0.514, FallSlp 0.500, Hold 0.000, Amount 0.798. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Square, clock sync on; stored division code: 11. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.001.
		- PRESSURE → Timbre: +0.858.
		- Cycling Envelope → Cutoff: +0.208.
		- ENV → Cutoff: +0.814.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
