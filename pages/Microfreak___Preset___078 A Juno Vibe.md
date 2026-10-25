logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 078
preset-synth-microfreak-name:: A Juno Vibe
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/077 Eonz]]
next:: [[Microfreak/Preset/079 ArpZap]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
preset-synth-microfreak-parameter-payload-sha256:: 8773f12ba413306f386dc9946e0eb9f8b2b4b7bb2e5b510b392ce945bad911f4
preset-synth-file:: [A Juno Vibe — October 25 slot 78 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___078%20A%20Juno%20Vibe___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 0c5d32b201609ea426fa66852fdd0e12195116f0c90f5bbf5519a2cec42827c9
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 78 over USB on October 25, 2026 with `mise run microfreak:download --slot 78`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 164, Factory 2.1 slot 161, Factory 3.0 slot 161, Factory 6.0 slot 209). Comparison used `mise run microfreak:compare`.
		- [Download the slot 78 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___078%20A%20Juno%20Vibe___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/078 A Juno Vibe/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SuperWave. [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
		- Wave: 1 (stored choice code). Detune: 0.327. Volume: 0.001.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.000; resonance: 0.712. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.066, decay/release 0.883, sustain 0.320. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.106, FallSlp 0.500, Hold 0.005, Amount 0.993. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 9. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Cutoff: +0.645.
		- PRESSURE → Cutoff: +0.172.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
