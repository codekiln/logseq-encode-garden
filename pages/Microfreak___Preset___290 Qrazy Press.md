logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 290
preset-synth-microfreak-name:: Qrazy Press
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/289 Down For Bass]]
next:: [[Microfreak/Preset/291 Poisoned 0scs]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
preset-synth-microfreak-parameter-payload-sha256:: dcd1ce8570c5343e53b55ede03af1bda1032c3fa0290ff9927f253c99816051f
preset-synth-file:: [Qrazy Press — October 25 slot 290 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___290%20Qrazy%20Press___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: b8ffea4596554c84a2ca1844c903edbbc8fc8a7cbd8ee85ef448bfe4c6e2b9d3
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 290 over USB on October 25, 2026 with `mise run microfreak:download --slot 290`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 354, Factory 6.0 slot 254). Comparison used `mise run microfreak:compare`.
		- [Download the slot 290 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___290%20Qrazy%20Press___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/290 Qrazy Press/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Bass. [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
		- Saturate: 0.081. Fold: 0.250. Noise: 0.040.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.147; resonance: 0.273. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.252, sustain 0.338. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.325, FallSlp 0.000, Hold 0.000, Amount 0.259. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync on; stored division code: 2. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.001.
		- ENV → Pitch: −0.001.
		- LFO → Pitch: +0.001.
		- LFO → Wave: −0.186.
		- Cycling Envelope → Timbre: +1.000.
		- ENV → Cutoff: +0.438.
		- PRESSURE → Cutoff: +0.201.
		- KEY/ARP → Cutoff: +0.349.
		- LFO → Assign 2 → Cycling Envelope Amount: +0.137.
		- PRESSURE → Assign 3 → Filter Resonance: +0.979.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
