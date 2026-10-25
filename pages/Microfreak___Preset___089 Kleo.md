logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 089
preset-synth-microfreak-name:: Kleo
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/088 D-Funk]]
next:: [[Microfreak/Preset/090 Guisky]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
preset-synth-microfreak-parameter-payload-sha256:: 4900abaf812d1f254ad788da47dacd9edb72b2f2270345edeb9791c273d0414d
preset-synth-file:: [Kleo — October 25 slot 89 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___089%20Kleo___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: f957c138249e42b8d376c20288aaca1e8efe77c1ed8cb957195e120d9d939bcb
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 89 over USB on October 25, 2026 with `mise run microfreak:download --slot 89`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 176, Factory 2.1 slot 171, Factory 3.0 slot 171, Factory 6.0 slot 44). Comparison used `mise run microfreak:compare`.
		- [Download the slot 89 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___089%20Kleo___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/089 Kleo/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Chords. [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
		- Type: 0 (stored choice code). Inv/Transp: 0.020. Shape control: 0.365.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.299; resonance: 0.059. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.350, decay/release 0.176, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.065, RiseSlp 0.500, FallLvl 0.981, FallSlp 0.500, Hold 0.407, Amount 0.995. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sawtooth, clock sync on; stored division code: 4. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Timbre: +0.310.
		- ENV → Cutoff: +0.378.
		- LFO → Cutoff: +0.223.
		- PRESSURE → Assign 3 → Shape: −0.238.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
