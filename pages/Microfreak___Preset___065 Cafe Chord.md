logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 065
preset-synth-microfreak-name:: Cafe Chord
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/064 Mood]]
next:: [[Microfreak/Preset/066 Vanarx]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
preset-synth-microfreak-parameter-payload-sha256:: 26e111aa49ade092be330cd9b664b9523f052de9474737bc245ff3591e45f818
preset-synth-file:: [Cafe Chord — October 25 slot 65 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___065%20Cafe%20Chord___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 046b7a554f3a092fcbf3eba69b107963116382e568c9a3003f1f36a314d543ee
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 65 over USB on October 25, 2026 with `mise run microfreak:download --slot 65`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 151, Factory 2.1 slot 15, Factory 3.0 slot 15, Factory 6.0 slot None). Comparison used `mise run microfreak:compare`.
		- [Download the slot 65 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___065%20Cafe%20Chord___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/065 Cafe Chord/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Chords. [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
		- Type: 5 (stored choice code). Inv/Transp: 0.197. Shape control: 0.000.
		- Keyboard octave: -1. Glide: 0.009.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.348; resonance: 0.692. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.173, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.163, RiseSlp 0.500, FallLvl 0.163, FallSlp 0.500, Hold 0.000, Amount 0.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 46877. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Cutoff: +0.312.
		- PRESSURE → Assign 1 → Decay/Release: +0.565.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
