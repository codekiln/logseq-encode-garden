logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 104
preset-synth-microfreak-name:: Wait...
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/103 Padel]]
next:: [[Microfreak/Preset/105 SlowBurn]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/07 Waveshaper]]
preset-synth-microfreak-parameter-payload-sha256:: 92dafb78131c9e152200ec6454f569da5e0cbd1b5cd95b575de1aa493676ba2d
preset-synth-file:: [Wait... — October 25 slot 104 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___104%20Wait...___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: e266aabdf69d57c45d2571b0cb1e19991b6e8b7b583a739a88c77b0673e74a77
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 104 over USB on October 25, 2026 with `mise run microfreak:download --slot 104`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 193, Factory 1.1 slot 193, Factory 2.1 slot 185, Factory 3.0 slot 185, Factory 6.0 slot 15). Comparison used `mise run microfreak:compare`.
		- [Download the slot 104 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___104%20Wait...___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/104 Wait.../Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Waveshaper. [[Microfreak/UG/06 Dig Osc/03 Types/07 Waveshaper]]
		- Wave: 0.141. Amount: 0.313. Asym: 0.000.
		- Keyboard octave: -1. Glide: 0.158.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.512; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.371, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.000, FallLvl 0.907, FallSlp 0.000, Hold 0.063, Amount 0.618. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync off; stored normalized rate: 0.547. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Wave: +1.000.
		- Cycling Envelope → Timbre: +0.003.
		- LFO → Timbre: +0.258.
		- ENV → Cutoff: +0.314.
		- LFO → Cutoff: +0.001.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
