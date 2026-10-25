logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 030
preset-synth-microfreak-name:: HarmonicTuneUp
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/029 Number Station]]
next:: [[Microfreak/Preset/031 Ixos]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
preset-synth-microfreak-parameter-payload-sha256:: 438b378625a355fa0747a39a4e5578f1802d50ad0a48fb28f906124870ae5b87
preset-synth-file:: [HarmonicTuneUp — October 25 slot 30 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___030%20HarmonicTuneUp___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 1161deb38b21ae0cab696b3533c1218cb374a16831be4c01ae843b8e5f1e34dd
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 30 over USB on October 25, 2026 with `mise run microfreak:download --slot 30`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 118, Factory 2.1 slot 118, Factory 3.0 slot 118, Factory 6.0 slot 275). Comparison used `mise run microfreak:compare`.
		- [Download the slot 30 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___030%20HarmonicTuneUp___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/030 HarmonicTuneUp/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Chords. [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
		- Type: 5 (stored choice code). Inv/Transp: 0.543. Shape control: 0.000.
		- Keyboard octave: -2. Glide: 0.394.
	- ## Filter
		- Band-pass filter. Saved cutoff: 0.212; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/02 Band Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.746, decay/release 0.794, sustain 0.650. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.129, RiseSlp 0.500, FallLvl 0.272, FallSlp 0.500, Hold 0.020, Amount 0.285. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.150. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.016.
		- PRESSURE → Wave: −0.986.
		- LFO → Timbre: +0.251.
		- ENV → Cutoff: +0.772.
		- LFO → Cutoff: +0.060.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
