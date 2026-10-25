logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 002
preset-synth-microfreak-name:: Punisher
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
preset-synth-microfreak-parameter-payload-sha256:: 1c600055f38d742904241c11459a455acdad5eb551160f102bcde71b577f5153
preset-synth-microfreak-vco-type-raw-hex:: 0x0c2a15
preset-synth-microfreak-vcf-cutoff-raw-hex:: 0x00bb5d
preset-synth-microfreak-vcf-reso-raw-hex:: 0x00c361
prev:: [[Microfreak/Preset/001 NervousKeys]]
next:: [[Microfreak/Preset/003 Trance]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
preset-synth-file:: [Punisher — October 25 slot 2 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___002%20Punisher___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 77b8b2dc4e0e0996d5461ec1f9acb1759a955c5fdd70fb9256c3ba3dc995154d
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 2 over USB on October 25, 2026 with `mise run microfreak:download --slot 2`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0 (Factory 1.1 slot 2, Factory 2.1 slot 2, Factory 3.0 slot 2). Comparison used `mise run microfreak:compare`.
		- [Download the slot 2 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___002%20Punisher___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/002 Punisher/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SuperWave. [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
		- Wave: 1 (stored choice code). Detune: 0.433. Volume: 0.496.
		- Keyboard octave: -2. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.732; resonance: 0.764. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.126, sustain 0.000. Amp Mod is off. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 1.000, FallLvl 0.228, FallSlp 1.000, Hold 0.016, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.047. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Pitch: +1.000.
		- Cycling Envelope → Timbre: +0.999.
		- PRESSURE → Timbre: +0.921.
		- LFO → Cutoff: +1.000.
		- PRESSURE → Cutoff: +1.000.
		- LFO → Assign 1 → LFO Rate: +1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
