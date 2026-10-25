logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 212
preset-synth-microfreak-name:: Raver
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Brass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/211 Motorway]]
next:: [[Microfreak/Preset/213 Hypno Chaos]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
preset-synth-microfreak-parameter-payload-sha256:: 749e39706fff55ec6a0deb265ebdd653a7677ad9d6ce038ca43565a83fce154d
preset-synth-file:: [Raver — October 25 slot 212 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___212%20Raver___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 621c59c71a92492dc26f7a3e7b15684facc043712779e1ef4d4e565536dc36c6
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 212 over USB on October 25, 2026 with `mise run microfreak:download --slot 212`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 283, Factory 6.0 slot 242). Comparison used `mise run microfreak:compare`.
		- [Download the slot 212 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___212%20Raver___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/212 Raver/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SawX. [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
		- Saw Mod: 0.160. Shape: 0.365. Noise: 0.389.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.280; resonance: 0.309. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.345, sustain 0.660. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.221, RiseSlp 0.500, FallLvl 0.274, FallSlp 0.500, Hold 0.004, Amount 0.357. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sawtooth, clock sync on; stored division code: 1. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.003.
		- Cycling Envelope → Wave: +0.110.
		- LFO → Wave: +0.001.
		- ENV → Cutoff: +0.691.
		- LFO → Cutoff: +0.117.
		- PRESSURE → Cutoff: +0.172.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
