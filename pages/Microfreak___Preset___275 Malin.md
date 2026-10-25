logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 275
preset-synth-microfreak-name:: Malin
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/274 Sardine]]
next:: [[Microfreak/Preset/276 Dandi]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
preset-synth-microfreak-parameter-payload-sha256:: a31c8567e0b4c094a53830b72ca719acb7b5de79aec3f470e9837cc5b5ca5147
preset-synth-file:: [Malin — October 25 slot 275 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___275%20Malin___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 9e978877d9f020e3657a036761e6689bf57bcfa0745beade9b697b4fbb63c3a3
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 275 over USB on October 25, 2026 with `mise run microfreak:download --slot 275`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 340, Factory 6.0 slot 309). Comparison used `mise run microfreak:compare`.
		- [Download the slot 275 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___275%20Malin___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/275 Malin/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Bass. [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
		- Saturate: 0.288. Fold: 0.247. Noise: 0.098.
		- Keyboard octave: +1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.730; resonance: 0.560. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.343, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.135, FallSlp 0.500, Hold 0.000, Amount 0.211. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Square, clock sync on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +1.000.
		- Cycling Envelope → Wave: +1.000.
		- ENV → Cutoff: +0.332.
		- LFO → Cutoff: +0.229.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
