logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 092
preset-synth-microfreak-name:: Smooth Pd
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/091 Cathil]]
next:: [[Microfreak/Preset/093 Blind]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
preset-synth-microfreak-parameter-payload-sha256:: d0ec7375b362dc73ed4324e945801c0bf399067f3420658288ff43d28af11d4c
preset-synth-file:: [Smooth Pd — October 25 slot 92 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___092%20Smooth%20Pd___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: c172ea78426120346757b0fd154a8df9f1c956aacf57b72e78abd3cf75ac4a46
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 92 over USB on October 25, 2026 with `mise run microfreak:download --slot 92`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 179, Factory 2.1 slot 174, Factory 3.0 slot 174, Factory 6.0 slot 37). Comparison used `mise run microfreak:compare`.
		- [Download the slot 92 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___092%20Smooth%20Pd___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/092 Smooth Pd/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SuperWave. [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
		- Wave: 0 (stored choice code). Detune: 0.428. Volume: 0.574.
		- Keyboard octave: 0. Glide: 0.275.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.475; resonance: 0.826. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.259, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.000, FallLvl 0.742, FallSlp 0.000, Hold 0.147, Amount 0.510. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.484. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Timbre: +0.094.
		- PRESSURE → Timbre: +0.695.
		- Cycling Envelope → Cutoff: +0.573.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
