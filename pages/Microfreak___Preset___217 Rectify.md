logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 217
preset-synth-microfreak-name:: Rectify
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/216 Rubber Band]]
next:: [[Microfreak/Preset/218 Metal Sequence]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: fd13c4d6914dc45ca29f0b4f3833b902382fbb6d6c11f04054c295689a739965
preset-synth-file:: [Rectify — October 25 slot 217 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___217%20Rectify___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 06acda365e886330e87de3e0b41100016061daeb84db51428e3bb692cc370800
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 217 over USB on October 25, 2026 with `mise run microfreak:download --slot 217`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 288, Factory 6.0 slot 101). Comparison used `mise run microfreak:compare`.
		- [Download the slot 217 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___217%20Rectify___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/217 Rectify/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 0.570. Rectification: 0.516. Noise: 0.308.
		- Keyboard octave: -1. Glide: 0.145.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.420; resonance: 0.509. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.065, sustain 0.128. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.000, FallSlp 0.500, Hold 0.293, Amount 0.829. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.997. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Wave: +0.452.
		- Cycling Envelope → Timbre: −1.000.
		- LFO → Timbre: +0.393.
		- Cycling Envelope → Cutoff: +0.074.
		- ENV → Cutoff: +0.919.
		- LFO → Cutoff: −0.626.
		- KEY/ARP → Cutoff: −0.405.
		- KEY/ARP → Assign 1 → LFO Rate: −0.523.
		- KEY/ARP → Assign 2 → `Mat.Assign2`: +0.507.
		- PRESSURE → Assign 3 → `LFO.Div`: +0.461.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
