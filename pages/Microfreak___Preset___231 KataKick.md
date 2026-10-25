logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 231
preset-synth-microfreak-name:: KataKick
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Percussion]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/230 Cristal Church]]
next:: [[Microfreak/Preset/232 LektrO]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
preset-synth-microfreak-parameter-payload-sha256:: e4a0a2595b254c5d521c30bc186689686ffe7708b584196e37df40db613b31fe
preset-synth-file:: [KataKick — October 25 slot 231 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___231%20KataKick___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 9fa221aca90854aaf108713df0f118a6ae42fed97e7273fcb330ecc0eb8ae661
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 231 over USB on October 25, 2026 with `mise run microfreak:download --slot 231`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 300, Factory 6.0 slot 190). Comparison used `mise run microfreak:compare`.
		- [Download the slot 231 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___231%20KataKick___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/231 KataKick/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Bass. [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
		- Saturate: 0.000. Fold: 0.000. Noise: 0.105.
		- Keyboard octave: -3. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.684; resonance: 0.396. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.340, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.373, FallSlp 0.000, Hold 0.000, Amount 0.788. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync off; stored normalized rate: 0.000. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.558.
		- ENV → Pitch: +0.149.
		- Cycling Envelope → Wave: +1.000.
		- Cycling Envelope → Timbre: +1.000.
		- LFO → Timbre: +0.107.
		- Cycling Envelope → Cutoff: −0.059.
		- ENV → Cutoff: +0.085.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
