logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 210
preset-synth-microfreak-name:: Movie Chase
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/209 Dirty]]
next:: [[Microfreak/Preset/211 Motorway]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: 2fcab0c9a05257a5f8dd8487ecbf792405b1709710e510e300bb295b081a5d4b
preset-synth-file:: [Movie Chase — October 25 slot 210 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___210%20Movie%20Chase___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 1f73ca7f4491fa9ef2241fbb14e6f45846794727f2325b259620133ee03755de
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 210 over USB on October 25, 2026 with `mise run microfreak:download --slot 210`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 281, Factory 6.0 slot 132). Comparison used `mise run microfreak:compare`.
		- [Download the slot 210 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___210%20Movie%20Chase___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/210 Movie Chase/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 0.355. Rectification: 0.389. Noise: 0.178.
		- Keyboard octave: -2. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.383; resonance: 0.529. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.335, sustain 0.806. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.000, RiseSlp 0.000, FallLvl 0.159, FallSlp 0.479, Hold 0.555, Amount 0.602. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 12. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Wave: +0.004.
		- Cycling Envelope → Timbre: +0.017.
		- LFO → Timbre: −0.025.
		- Cycling Envelope → Cutoff: +0.152.
		- ENV → Cutoff: +1.000.
		- Cycling Envelope → Assign 2 → Cycling Envelope Amount: −0.051.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
