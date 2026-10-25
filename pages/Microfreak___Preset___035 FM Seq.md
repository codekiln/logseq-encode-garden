logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 035
preset-synth-microfreak-name:: FM Seq
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/034 Corrosion]]
next:: [[Microfreak/Preset/036 Rollie Lov]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
preset-synth-microfreak-parameter-payload-sha256:: 53f6bb092f01825ab77a2e3e95145bb459abb0b66408227594243c21b63597d2
preset-synth-file:: [FM Seq — October 25 slot 35 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___035%20FM%20Seq___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 61f9ba813ed00940e0e655223a02af528bd1ef4715a92cb0cfc169cd7f04c0fc
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 35 over USB on October 25, 2026 with `mise run microfreak:download --slot 35`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0 (Factory 1.0 slot 122, Factory 1.1 slot 122, Factory 2.1 slot 122, Factory 3.0 slot 122). Comparison used `mise run microfreak:compare`.
		- [Download the slot 35 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___035%20FM%20Seq___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/035 FM Seq/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Two Op. FM. [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
		- Ratio: 1.000. Amount: 0.574. Shape: 0.996.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- High-pass filter. Saved cutoff: 0.453; resonance: 0.840. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.193, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.414, RiseSlp 0.500, FallLvl 0.788, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sawtooth, clock sync on; stored division code: 2. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Cutoff: −0.070.
		- LFO → Assign 1 → Decay/Release: +0.462.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
