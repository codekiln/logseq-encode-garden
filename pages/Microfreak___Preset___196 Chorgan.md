logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 196
preset-synth-microfreak-name:: Chorgan
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Template]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/195 Night Organ]]
next:: [[Microfreak/Preset/197 Fusion Lead]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
preset-synth-microfreak-parameter-payload-sha256:: 8299a2a9a0ffcf637679434166e3a4a80c89b9376a62710e3b35740359fa3fa4
preset-synth-file:: [Chorgan — October 25 slot 196 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___196%20Chorgan___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 385f9dc2e446289f8c8444587517d300a35d1d942d4c1276b73933008c40fa8f
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 196 over USB on October 25, 2026 with `mise run microfreak:download --slot 196`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 225, Factory 2.1 slot 39, Factory 3.0 slot 269, Factory 6.0 slot 193). Comparison used `mise run microfreak:compare`.
		- [Download the slot 196 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___196%20Chorgan___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/196 Chorgan/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Chords. [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
		- Type: 9 (stored choice code). Inv/Transp: 0.000. Shape control: 0.619.
		- Keyboard octave: +2. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.000; resonance: 0.154. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.148, sustain 0.495. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.000, FallLvl 0.287, FallSlp 0.448, Hold 0.000, Amount 0.999. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.132. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Cutoff: +0.864.
		- PRESSURE → Cutoff: +0.072.
		- Cycling Envelope → Assign 1 → Shape: +0.088.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
