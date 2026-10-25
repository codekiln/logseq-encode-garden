logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 111
preset-synth-microfreak-name:: AcidFrog
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/110 F-Back]]
next:: [[Microfreak/Preset/112 Anlg]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/09 Formant]]
preset-synth-microfreak-parameter-payload-sha256:: a344eee3ad63ed78466b3b9383cf29fc8e8d03c4f26eb607e052db6e1a717f0c
preset-synth-file:: [AcidFrog — October 25 slot 111 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___111%20AcidFrog___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: cb3b59b5904094c57a5dabde9fca5d3764d5e8e5d6578b49e04e50dd1a637db1
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 111 over USB on October 25, 2026 with `mise run microfreak:download --slot 111`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 206, Factory 2.1 slot 191, Factory 3.0 slot 191, Factory 6.0 slot 206). Comparison used `mise run microfreak:compare`.
		- [Download the slot 111 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___111%20AcidFrog___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/111 AcidFrog/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Formant. [[Microfreak/UG/06 Dig Osc/03 Types/09 Formant]]
		- Interval: 0.057. Formant: 0.818. Shape: 0.448.
		- Keyboard octave: -1. Glide: 0.149.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.719; resonance: 0.096. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.286, sustain 0.902. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.339, RiseSlp 0.500, FallLvl 0.704, FallSlp 0.500, Hold 1.000, Amount 0.194. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.397. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Wave: +1.000.
		- Cycling Envelope → Timbre: −0.868.
		- LFO → Timbre: +0.101.
		- PRESSURE → Timbre: +0.017.
		- PRESSURE → Assign 1 → LFO Rate: +0.194.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
