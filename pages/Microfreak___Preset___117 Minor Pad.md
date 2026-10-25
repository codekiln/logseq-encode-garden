logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 117
preset-synth-microfreak-name:: Minor Pad
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/116 Analog Chaser]]
next:: [[Microfreak/Preset/118 Fight]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
preset-synth-microfreak-parameter-payload-sha256:: 7604b80c5e5c9913d50072c4e4dde0cd6d92b86a095ee7c6166fb42e69b0165a
preset-synth-file:: [Minor Pad — October 25 slot 117 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___117%20Minor%20Pad___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: ef85661e67217efa9764ec5ee852b5442811a7685ef78fb39781ca28c9414879
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 117 over USB on October 25, 2026 with `mise run microfreak:download --slot 117`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 5, Factory 2.1 slot None, Factory 3.0 slot 197, Factory 6.0 slot 389). Comparison used `mise run microfreak:compare`.
		- [Download the slot 117 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___117%20Minor%20Pad___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/117 Minor Pad/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SuperWave. [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
		- Wave: 1 (stored choice code). Detune: 0.573. Volume: 0.667.
		- Keyboard octave: 0. Glide: 0.264.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.482; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.173, decay/release 0.215, sustain 0.623. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.238, FallSlp 0.100, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 8. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: −0.179.
		- ENV → Timbre: +0.156.
		- ENV → Cutoff: +0.797.
		- LFO → Assign 1 → Sustain: +0.188.
		- Cycling Envelope → Assign 2 → Volume: +0.529.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
