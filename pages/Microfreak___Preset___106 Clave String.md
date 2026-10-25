logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 106
preset-synth-microfreak-name:: Clave String
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Strings]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/105 SlowBurn]]
next:: [[Microfreak/Preset/107 Arame]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/05 KarplusStr]]
preset-synth-microfreak-parameter-payload-sha256:: db8fbcfe498100ae4f819eb49eff79ae3cdb072399da6f8bcb1210f35b78fa3e
preset-synth-file:: [Clave String — October 25 slot 106 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___106%20Clave%20String___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: e26e813ce1aaed69399714407918cb4f9144a914b5bafb369af61f9e1f446f60
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 106 over USB on October 25, 2026 with `mise run microfreak:download --slot 106`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0 (Factory 1.1 slot 198, Factory 2.1 slot 187, Factory 3.0 slot 187). Comparison used `mise run microfreak:compare`.
		- [Download the slot 106 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___106%20Clave%20String___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/106 Clave String/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: KarplusStr. [[Microfreak/UG/06 Dig Osc/03 Types/05 KarplusStr]]
		- Bow: 1.000. Position: 1.000. Decay: 1.000.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.854; resonance: 0.743. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.381, decay/release 0.259, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.414, RiseSlp 0.500, FallLvl 0.562, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.390. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- PRESSURE → Wave: −1.000.
		- Cycling Envelope → Cutoff: −0.352.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
