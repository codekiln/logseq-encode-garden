logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 066
preset-synth-microfreak-name:: Vanarx
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/065 Cafe Chord]]
next:: [[Microfreak/Preset/067 Angels]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/07 Waveshaper]]
preset-synth-microfreak-parameter-payload-sha256:: d3ee6a38e0e478c78d02e70ba0d174f18b950ab3ba083645fc73e6dd8beab181
preset-synth-file:: [Vanarx — October 25 slot 66 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___066%20Vanarx___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 1cf2d040386b5bf187f772ba32a4d9c56e1587facc9ed993211848676548e780
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 66 over USB on October 25, 2026 with `mise run microfreak:download --slot 66`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot None, Factory 1.1 slot 153, Factory 2.1 slot 150, Factory 3.0 slot 150, Factory 6.0 slot 9). Comparison used `mise run microfreak:compare`.
		- [Download the slot 66 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___066%20Vanarx___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/066 Vanarx/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Waveshaper. [[Microfreak/UG/06 Dig Osc/03 Types/07 Waveshaper]]
		- Wave: 0.840. Amount: 0.754. Asym: 0.232.
		- Keyboard octave: -2. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.000; resonance: 0.842. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.590, sustain 0.306. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.000, FallLvl 0.080, FallSlp 0.046, Hold 0.000, Amount 0.994. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 1. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +1.000.
		- Cycling Envelope → Wave: −0.500.
		- LFO → Wave: +0.105.
		- Cycling Envelope → Timbre: +0.503.
		- ENV → Timbre: +0.410.
		- ENV → Cutoff: +0.837.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
