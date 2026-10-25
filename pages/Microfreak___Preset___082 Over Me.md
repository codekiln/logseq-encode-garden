logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 082
preset-synth-microfreak-name:: Over Me
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/081 Gaming]]
next:: [[Microfreak/Preset/083 Leeds Strings]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
preset-synth-microfreak-parameter-payload-sha256:: 27fbb1488f224313d448e56c57a24dd1cc8a299ad9257c7d852a3c037d6e1955
preset-synth-file:: [Over Me — October 25 slot 82 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___082%20Over%20Me___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: d70a8a2d021d0abd90b305149dcb1f1bb82abd41c0d38e40cad61ba87780c493
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 82 over USB on October 25, 2026 with `mise run microfreak:download --slot 82`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 168, Factory 1.1 slot 168, Factory 2.1 slot 165, Factory 3.0 slot 165, Factory 6.0 slot 265). Comparison used `mise run microfreak:compare`.
		- [Download the slot 82 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___082%20Over%20Me___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/082 Over Me/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: BasicWaves. [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
		- Morph: 0.697. Sym: 0.256. Sub: 0.419.
		- Keyboard octave: 0. Glide: 0.145.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.051; resonance: 0.655. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.231, sustain 0.644. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.094, RiseSlp 0.500, FallLvl 0.324, FallSlp 0.500, Hold 0.000, Amount 0.050. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync on; stored division code: 4. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Timbre: +0.393.
		- ENV → Cutoff: +0.565.
		- LFO → Cutoff: +0.353.
		- KEY/ARP → Cutoff: +0.507.
		- KEY/ARP → Assign 1 → Cycling Envelope Rise: −0.157.
		- KEY/ARP → Assign 2 → `Mat.Assign2`: +0.647.
		- PRESSURE → Assign 3 → `LFO.Div`: +0.461.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
