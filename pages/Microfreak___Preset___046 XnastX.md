logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 046
preset-synth-microfreak-name:: XnastX
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/045 Lottreux]]
next:: [[Microfreak/Preset/047 White Calx]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
preset-synth-microfreak-parameter-payload-sha256:: 64ac933d5bc23389237cc3a73142e0e0cc40140bc1cedbd9825e031762082f23
preset-synth-file:: [XnastX — October 25 slot 46 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___046%20XnastX___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 326bb0d6c37609483407e6d29f675b5106d5e98dd405a350719ef193fa76ce89
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 46 over USB on October 25, 2026 with `mise run microfreak:download --slot 46`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0 (Factory 1.0 slot 132, Factory 1.1 slot 132, Factory 2.1 slot 132, Factory 3.0 slot 132). Comparison used `mise run microfreak:compare`.
		- [Download the slot 46 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___046%20XnastX___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/046 XnastX/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Wavetable. [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
		- Table: 15 (stored choice code). Position: 0.462. Chorus: 0.398.
		- Keyboard octave: -2. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.773; resonance: 0.516. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.998, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.000, FallSlp 0.500, Hold 0.277, Amount 0.486. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync off; stored normalized rate: 0.194. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Wave: +0.009.
		- LFO → Timbre: +0.178.
		- ENV → Cutoff: +0.412.
		- LFO → Cutoff: −0.885.
		- LFO → Assign 1 → Chorus: +0.910.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
