logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 004
preset-synth-microfreak-name:: Ether
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/003 Trance]]
next:: [[Microfreak/Preset/005 MotivSeq]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
preset-synth-microfreak-parameter-payload-sha256:: f2095974f6f3d5b480447c5cb426d8f220e91b4f4102f65f298f0a6b7a7ff563
preset-synth-file:: [Ether — October 25 slot 4 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___004%20Ether___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: b5c4c87698cc579bc6b25671c3585ddf4b674f48a35fdeee0c556da0ea5a59a0
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 4 over USB on October 25, 2026 with `mise run microfreak:download --slot 4`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0 (Factory 1.1 slot 4, Factory 2.1 slot 4, Factory 3.0 slot 4). Comparison used `mise run microfreak:compare`.
		- [Download the slot 4 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___004%20Ether___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/004 Ether/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SuperWave. [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
		- Wave: 3 (stored choice code). Detune: 1.000. Volume: 0.735.
		- Keyboard octave: +1. Glide: 0.000.
	- ## Filter
		- High-pass filter. Saved cutoff: 0.230; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.051, decay/release 0.414, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.473, FallSlp 0.275, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- PRESSURE → Wave: −1.000.
		- Cycling Envelope → Timbre: −1.000.
		- ENV → Cutoff: −0.355.
		- PRESSURE → Assign 1 → matrix amount LFO → Cutoff: +1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
