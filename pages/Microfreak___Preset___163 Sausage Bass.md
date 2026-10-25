logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 163
preset-synth-microfreak-name:: Sausage Bass
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/162 Roid]]
next:: [[Microfreak/Preset/164 Space Alert]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
preset-synth-microfreak-parameter-payload-sha256:: 5ed770b695d0fddab9a5007fc9668229bef31e41629e6a4f3b0874228fd3d4ea
preset-synth-file:: [Sausage Bass — October 25 slot 163 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___163%20Sausage%20Bass___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 4c053c7c7411dc5ad32a4c494dbb0ebe2040a756c343ee61d9e71018d6570375
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 163 over USB on October 25, 2026 with `mise run microfreak:download --slot 163`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 137, Factory 2.1 slot 239, Factory 3.0 slot 239, Factory 6.0 slot 367). Comparison used `mise run microfreak:compare`.
		- [Download the slot 163 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___163%20Sausage%20Bass___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/163 Sausage Bass/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Wavetable. [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
		- Table: 8 (stored choice code). Position: 0.374. Chorus: 0.698.
		- Keyboard octave: -2. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.454; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.571, decay/release 0.758, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.000, FallSlp 0.500, Hold 0.000, Amount 0.992. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 4. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.004.
		- ENV → Timbre: +0.814.
		- Cycling Envelope → Cutoff: +0.384.
		- PRESSURE → Assign 1 → `LFO.Div`: +1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
