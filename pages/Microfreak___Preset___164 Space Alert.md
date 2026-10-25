logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 164
preset-synth-microfreak-name:: Space Alert
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/163 Sausage Bass]]
next:: [[Microfreak/Preset/165 Kick N Hard]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
preset-synth-microfreak-parameter-payload-sha256:: 91369cffda4bf0b303d2d431c0a61c2fe4cee156511f14d3b5cd4cb178e30fb5
preset-synth-file:: [Space Alert — October 25 slot 164 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___164%20Space%20Alert___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: ca1c840682e63e2a867e21de7a68cc9027cf57aeeab69b830288302f7295dfec
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 164 over USB on October 25, 2026 with `mise run microfreak:download --slot 164`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 138, Factory 2.1 slot 24, Factory 3.0 slot 24, Factory 6.0 slot None). Comparison used `mise run microfreak:compare`.
		- [Download the slot 164 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___164%20Space%20Alert___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/164 Space Alert/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: V.Analog. [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		- Detune: 0.000. Shape: 0.248. Wave: 0.656.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.000; resonance: 0.186. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.200, sustain 0.952. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.254, RiseSlp 0.326, FallLvl 0.497, FallSlp 0.500, Hold 0.286, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sawtooth, clock sync off; stored normalized rate: 0.395. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.982.
		- LFO → Timbre: +1.000.
		- Cycling Envelope → Cutoff: +0.542.
		- ENV → Cutoff: +0.361.
		- Cycling Envelope → Assign 1 → LFO Rate: +0.821.
		- PRESSURE → Assign 1 → LFO Rate: −0.174.
		- Cycling Envelope → Assign 3 → Wave: +0.236.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
