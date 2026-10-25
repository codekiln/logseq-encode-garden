logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 033
preset-synth-microfreak-name:: Organism
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Organ]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/032 Chord Bass]]
next:: [[Microfreak/Preset/034 Corrosion]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
preset-synth-microfreak-parameter-payload-sha256:: bcca4986fe629f90d1d16d6b9eb7a09e2e7d7d0ec103c7bf6696c208c5988ed1
preset-synth-file:: [Organism — October 25 slot 33 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___033%20Organism___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 2ea793197a9e9b2c54ab332283b805cbe969fe908e2a627819b69d2c78c156db
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 33 over USB on October 25, 2026 with `mise run microfreak:download --slot 33`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0 (Factory 1.0 slot 201, Factory 1.1 slot 201, Factory 2.1 slot 120, Factory 3.0 slot 120). Comparison used `mise run microfreak:compare`.
		- [Download the slot 33 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___033%20Organism___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/033 Organism/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Chords. [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
		- Type: 0 (stored choice code). Inv/Transp: 0.300. Shape control: 0.700.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- High-pass filter. Saved cutoff: 0.000; resonance: 0.499. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.167, decay/release 0.237, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.163, RiseSlp 0.500, FallLvl 0.163, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- PRESSURE → Cutoff: +0.500.
		- PRESSURE → Assign 1 → Shape: −0.010.
		- PRESSURE → Assign 3 → matrix amount LFO → Pitch: +0.007.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
