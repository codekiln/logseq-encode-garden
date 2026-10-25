logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 260
preset-synth-microfreak-name:: 8bitfi
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/259 Infini Pad]]
next:: [[Microfreak/Preset/261 Eurgon Lead]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
preset-synth-microfreak-parameter-payload-sha256:: 6a7529172fe436752a9d2d0eaa11500a7f284469f3d81e20de3fe3239b066a7b
preset-synth-file:: [8bitfi — October 25 slot 260 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___260%208bitfi___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 067f77828a7647e4a203b8fcad2102de1eebd2a4563580cff8a75a4c38dfe8e2
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 260 over USB on October 25, 2026 with `mise run microfreak:download --slot 260`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 327, Factory 6.0 slot 177). Comparison used `mise run microfreak:compare`.
		- [Download the slot 260 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___260%208bitfi___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/260 8bitfi/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Bass. [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
		- Saturate: 0.146. Fold: 0.201. Noise: 0.000.
		- Keyboard octave: +2. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.370; resonance: 0.158. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.369, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.256, RiseSlp 0.311, FallLvl 0.278, FallSlp 0.647, Hold 0.000, Amount 0.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Square, clock sync off; stored normalized rate: 0.804. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.011.
		- LFO → Pitch: +0.073.
		- PRESSURE → Wave: +0.373.
		- PRESSURE → Timbre: +1.000.
		- Cycling Envelope → Cutoff: +0.005.
		- ENV → Cutoff: +0.444.
		- KEY/ARP → Assign 3 → `Mat.Assign3`: −0.137.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
