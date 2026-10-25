logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 073
preset-synth-microfreak-name:: S.H Ld
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/072 Buzzsaw]]
next:: [[Microfreak/Preset/074 Sneaker]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
preset-synth-microfreak-parameter-payload-sha256:: d11abee2edd328488214f47e80d93aab2f1a8e72c6c59ae935ff83ed961ad217
preset-synth-file:: [S.H Ld — October 25 slot 73 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___073%20S.H%20Ld___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: a68271e5a409339d443f300027539e98283c337dc6336792d60f03315e70d5e4
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 73 over USB on October 25, 2026 with `mise run microfreak:download --slot 73`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 16, Factory 2.1 slot None, Factory 3.0 slot 157, Factory 6.0 slot 200). Comparison used `mise run microfreak:compare`.
		- [Download the slot 73 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___073%20S.H%20Ld___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/073 S.H Ld/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: V.Analog. [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		- Detune: 0.391. Shape: 0.590. Wave: 0.863.
		- Keyboard octave: 0. Glide: 0.165.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.872; resonance: 0.803. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.276, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.000, FallLvl 0.405, FallSlp 0.000, Hold 0.000, Amount 0.510. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold, clock sync on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Timbre: +0.010.
		- LFO → Timbre: +0.384.
		- Cycling Envelope → Cutoff: +0.396.
		- LFO → Cutoff: +0.457.
		- PRESSURE → Cutoff: −0.362.
		- KEY/ARP → Cutoff: +0.739.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
