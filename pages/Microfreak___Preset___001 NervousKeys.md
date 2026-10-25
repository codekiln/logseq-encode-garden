logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 001
preset-synth-microfreak-name:: NervousKeys
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
preset-synth-microfreak-parameter-payload-sha256:: 68b942f127af824c033e552cd3807c69f13cde9a2641fcc27f7a57460de195f6
preset-synth-microfreak-vco-type-raw-hex:: 0x0cff5f
preset-synth-microfreak-vcf-cutoff-raw-hex:: 0x00da3c
preset-synth-microfreak-vcf-reso-raw-hex:: 0x006851
next:: [[Microfreak/Preset/002 Punisher]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/09 Formant]]
preset-synth-file:: [NervousKeys — October 25 slot 1 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___001%20NervousKeys___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 7ddbc3e577cac6cf965d35c5c403bb292c67495c033fc10443ef8aae2b787a8d
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 1 over USB on October 25, 2026 with `mise run microfreak:download --slot 1`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0 (Factory 1.0 slot 138, Factory 1.1 slot 138, Factory 2.1 slot 1, Factory 3.0 slot 1). Comparison used `mise run microfreak:compare`.
		- [Download the slot 1 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___001%20NervousKeys___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/001 NervousKeys/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Formant. [[Microfreak/UG/06 Dig Osc/03 Types/09 Formant]]
		- Interval: 0.208. Formant: 0.456. Shape: 0.896.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.475; resonance: 0.636. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.396, sustain 0.230. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.550, FallSlp 0.500, Hold 0.595, Amount 0.637. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.642. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: −0.029.
		- ENV → Cutoff: +0.109.
		- PRESSURE → Cutoff: +0.157.
		- PRESSURE → Assign 1 → matrix amount ENV → Cutoff: +0.263.
		- Cycling Envelope → Assign 2 → matrix amount LFO → Pitch: +0.050.
		- PRESSURE → Assign 3 → Sustain: +0.108.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
