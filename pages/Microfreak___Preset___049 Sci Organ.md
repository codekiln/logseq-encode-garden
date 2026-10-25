logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 049
preset-synth-microfreak-name:: Sci Organ
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/048 VintageEdge]]
next:: [[Microfreak/Preset/050 Death]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
preset-synth-microfreak-parameter-payload-sha256:: cca4778d3d951ea7f70071907e7445a1fb910f21343d20509f4e47e40fd10ca9
preset-synth-file:: [Sci Organ — October 25 slot 49 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___049%20Sci%20Organ___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 1605c1bb73e155e24d92c93b2cda2079756b53e0be817abc3564f9c5b82e374f
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 49 over USB on October 25, 2026 with `mise run microfreak:download --slot 49`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 135, Factory 1.1 slot 135, Factory 2.1 slot 135, Factory 3.0 slot 135, Factory 6.0 slot 332). Comparison used `mise run microfreak:compare`.
		- [Download the slot 49 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___049%20Sci%20Organ___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/049 Sci Organ/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Chords. [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
		- Type: 1 (stored choice code). Inv/Transp: 0.321. Shape control: 0.727.
		- Keyboard octave: -1. Glide: 0.012.
	- ## Filter
		- High-pass filter. Saved cutoff: 0.320; resonance: 0.792. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.099, decay/release 0.301, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.163, RiseSlp 0.500, FallLvl 0.163, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 46877. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- PRESSURE → Timbre: +0.234.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
