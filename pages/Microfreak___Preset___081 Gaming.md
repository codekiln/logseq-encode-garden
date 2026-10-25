logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 081
preset-synth-microfreak-name:: Gaming
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/080 Traditon]]
next:: [[Microfreak/Preset/082 Over Me]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
preset-synth-microfreak-parameter-payload-sha256:: c5e43b361395bea368efaa1447f93fa9468c7e2b53b054022dc20acf52fff493
preset-synth-file:: [Gaming — October 25 slot 81 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___081%20Gaming___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: a03a1bbec5b2b6831ff282e436f6d281274f32ae41c66de34454e967d6569cf4
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 81 over USB on October 25, 2026 with `mise run microfreak:download --slot 81`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 167, Factory 1.1 slot 167, Factory 2.1 slot 164, Factory 3.0 slot 164, Factory 6.0 slot 320). Comparison used `mise run microfreak:compare`.
		- [Download the slot 81 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___081%20Gaming___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/081 Gaming/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: V.Analog. [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		- Detune: 0.525. Shape: 0.729. Wave: 0.652.
		- Keyboard octave: -1. Glide: 0.064.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.394; resonance: 0.485. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.118, sustain 0.170. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.395, RiseSlp 0.757, FallLvl 0.508, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Square, clock sync on; stored division code: 12. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.051.
		- Cycling Envelope → Timbre: +0.229.
		- ENV → Cutoff: +0.386.
		- PRESSURE → Cutoff: +0.250.
		- KEY/ARP → Cutoff: +0.251.
		- ENV → Assign 1 → Filter Resonance: +0.046.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
