logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 292
preset-synth-microfreak-name:: Moving Cars
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/291 Poisoned 0scs]]
next:: [[Microfreak/Preset/293 Digital Roads]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: 9eb235b596850b8dbb98a575ccf625acc5318effab52f25843f1c9d7fde79a5f
preset-synth-file:: [Moving Cars — October 25 slot 292 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___292%20Moving%20Cars___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: b4d2ec3ec68120526514c0c1f4b072e4f47f778d56f024c477eb28aeed25a8d0
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 292 over USB on October 25, 2026 with `mise run microfreak:download --slot 292`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 356, Factory 6.0 slot 296). Comparison used `mise run microfreak:compare`.
		- [Download the slot 292 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___292%20Moving%20Cars___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/292 Moving Cars/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 0.150. Rectification: 0.684. Noise: 0.000.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- High-pass filter. Saved cutoff: 0.408; resonance: 0.319. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.533, decay/release 0.904, sustain 0.112. Amp Mod is off. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.727, RiseSlp 0.500, FallLvl 0.000, FallSlp 0.500, Hold 0.000, Amount 0.326. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold, clock sync off; stored normalized rate: 0.000. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +1.000.
		- PRESSURE → Pitch: −0.120.
		- Cycling Envelope → Wave: −0.149.
		- ENV → Cutoff: −0.426.
		- LFO → Cutoff: +0.061.
		- LFO → Assign 2 → Cycling Envelope Hold: +0.104.
		- Cycling Envelope → Assign 3 → Unison Spread: +1.000.
		- ENV → Assign 3 → Unison Spread: +0.358.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
