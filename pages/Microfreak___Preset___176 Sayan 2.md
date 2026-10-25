logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 176
preset-synth-microfreak-name:: Sayan 2
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/175 Wuuut]]
next:: [[Microfreak/Preset/177 Square Poly]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/05 KarplusStr]]
preset-synth-microfreak-parameter-payload-sha256:: f1ff40d798db41ece28d2bf5def04726044fb5d836c7f3f66ab9d22759085aad
preset-synth-file:: [Sayan 2 — October 25 slot 176 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___176%20Sayan%202___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 346b6a2d311d4ad0ce72a14abef306b81e04d7c85b5454d64097677bf9bdba1c
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 176 over USB on October 25, 2026 with `mise run microfreak:download --slot 176`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 149, Factory 2.1 slot 250, Factory 3.0 slot 250, Factory 6.0 slot 260). Comparison used `mise run microfreak:compare`.
		- [Download the slot 176 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___176%20Sayan%202___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/176 Sayan 2/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: KarplusStr. [[Microfreak/UG/06 Dig Osc/03 Types/05 KarplusStr]]
		- Bow: 0.357. Position: 0.474. Decay: 0.234.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.915; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.262, decay/release 0.348, sustain 0.298. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.163, RiseSlp 0.500, FallLvl 0.163, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sawtooth, clock sync on; stored division code: 12. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.214.
		- Cycling Envelope → Wave: +0.747.
		- Cycling Envelope → Timbre: −0.073.
		- PRESSURE → Timbre: +0.593.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
