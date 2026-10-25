logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 161
preset-synth-microfreak-name:: Crackle Sleep
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/160 Incoming Ship]]
next:: [[Microfreak/Preset/162 Roid]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
preset-synth-microfreak-parameter-payload-sha256:: a7e7582edcf1487d29009bf1965ab0b7e2709873732f6406f7959be75cf09e10
preset-synth-file:: [Crackle Sleep — October 25 slot 161 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___161%20Crackle%20Sleep___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 0f161d54e8b7aa76e9857688d3eb0ae88960925d4c4354a017e96f0872ebd78b
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 161 over USB on October 25, 2026 with `mise run microfreak:download --slot 161`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 135, Factory 2.1 slot 237, Factory 3.0 slot 237, Factory 6.0 slot 392). Comparison used `mise run microfreak:compare`.
		- [Download the slot 161 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___161%20Crackle%20Sleep___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/161 Crackle Sleep/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Noise. [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
		- Wave: 0.041. Timbre: 0.053. Shape: 0.180.
		- Keyboard octave: 0. Glide: 0.145.
	- ## Filter
		- Low-pass filter. Saved cutoff: 1.000; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.119, decay/release 0.673, sustain 0.529. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.216, RiseSlp 0.054, FallLvl 0.617, FallSlp 0.141, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.496. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.004.
		- Cycling Envelope → Wave: +0.070.
		- Cycling Envelope → Timbre: −0.084.
		- LFO → Assign 1 → Cycling Envelope Fall: +0.304.
		- Cycling Envelope → Assign 2 → Shape: +0.062.
		- ENV → Assign 2 → Shape: +0.452.
		- LFO → Assign 3 → Sustain: +0.014.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
