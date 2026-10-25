logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 209
preset-synth-microfreak-name:: Dirty
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/208 Boarding]]
next:: [[Microfreak/Preset/210 Movie Chase]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: 3168f7fa6b9518cce77741dc4bc080afe6d05218351d95795c0371c4fb73854c
preset-synth-file:: [Dirty — October 25 slot 209 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___209%20Dirty___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 48d5561bf615faabad46a7ccde6903bdd98c488274cbc87135a60ad1518c6f0c
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 209 over USB on October 25, 2026 with `mise run microfreak:download --slot 209`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 280, Factory 6.0 slot 195). Comparison used `mise run microfreak:compare`.
		- [Download the slot 209 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___209%20Dirty___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/209 Dirty/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 0.588. Rectification: 0.282. Noise: 0.332.
		- Keyboard octave: +1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.660; resonance: 0.437. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.110, sustain 0.277. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.192, RiseSlp 0.500, FallLvl 0.384, FallSlp 0.500, Hold 0.237, Amount 0.466. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.999. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.448.
		- Cycling Envelope → Wave: +0.242.
		- Cycling Envelope → Cutoff: +0.751.
		- ENV → Cutoff: +0.291.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
