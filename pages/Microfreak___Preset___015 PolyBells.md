logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 015
preset-synth-microfreak-name:: PolyBells
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/014 Bontempis]]
next:: [[Microfreak/Preset/016 Voidom]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/07 Waveshaper]]
preset-synth-microfreak-parameter-payload-sha256:: 71b43e757c025dce3144b0a4ac671ce31ca8233047e3f5ec926b2d522b42d4e0
preset-synth-file:: [PolyBells — October 25 slot 15 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___015%20PolyBells___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: cbfdbeacaecaf7c0c074f65e3c26932bf67015fa08a15a0b5d153b64c2ab00c8
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 15 over USB on October 25, 2026 with `mise run microfreak:download --slot 15`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0 (Factory 1.1 slot 104, Factory 2.1 slot 104, Factory 3.0 slot 104). Comparison used `mise run microfreak:compare`.
		- [Download the slot 15 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___015%20PolyBells___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/015 PolyBells/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Waveshaper. [[Microfreak/UG/06 Dig Osc/03 Types/07 Waveshaper]]
		- Wave: 0.611. Amount: 0.434. Asym: 0.000.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.178; resonance: 0.804. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.240, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.414, RiseSlp 0.500, FallLvl 0.163, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync on; stored division code: 46877. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- PRESSURE → Timbre: −0.381.
		- ENV → Cutoff: +0.575.
		- PRESSURE → Cutoff: +0.259.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
