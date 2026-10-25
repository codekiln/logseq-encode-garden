logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 102
preset-synth-microfreak-name:: Braine Storm
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/101 Etna 01]]
next:: [[Microfreak/Preset/103 Padel]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
preset-synth-microfreak-parameter-payload-sha256:: b2880bbf256214cf4e77e9982e8a372c6d98108253cd852cea2e8d29e8d95034
preset-synth-file:: [Braine Storm — October 25 slot 102 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___102%20Braine%20Storm___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: c08b361b3e45a948793432640d1bbe9b0f65b7ad40a7194afc905aaf725d5a68
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 102 over USB on October 25, 2026 with `mise run microfreak:download --slot 102`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 191, Factory 2.1 slot 183, Factory 3.0 slot 183, Factory 6.0 slot 42). Comparison used `mise run microfreak:compare`.
		- [Download the slot 102 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___102%20Braine%20Storm___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/102 Braine Storm/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: V.Analog. [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		- Detune: 0.859. Shape: 0.546. Wave: 0.542.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.918; resonance: 0.047. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.693, sustain 0.000. Amp Mod is off. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.163, RiseSlp 0.500, FallLvl 0.138, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync on; stored division code: 8. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Wave: +0.014.
		- ENV → Timbre: +0.349.
		- PRESSURE → Timbre: +0.287.
		- ENV → Cutoff: −0.445.
		- LFO → Assign 1 → matrix amount Cycling Envelope → Cutoff: +0.697.
		- LFO → Assign 2 → `LFO.Div`: +0.582.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
