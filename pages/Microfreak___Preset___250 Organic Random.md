logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 250
preset-synth-microfreak-name:: Organic Random
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/249 RisoLFO]]
next:: [[Microfreak/Preset/251 Trinity]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
preset-synth-microfreak-parameter-payload-sha256:: 96a27a38e3e063d347bc924e6ea8908c7eb943d849ee8f176ff63433dcc096a6
preset-synth-file:: [Organic Random — October 25 slot 250 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___250%20Organic%20Random___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 685ccc18b1ece9f1c49acd2033945d7ab2163099ad57acb50e63155da416dae4
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 250 over USB on October 25, 2026 with `mise run microfreak:download --slot 250`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 318, Factory 6.0 slot 217). Comparison used `mise run microfreak:compare`.
		- [Download the slot 250 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___250%20Organic%20Random___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/250 Organic Random/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Two Op. FM. [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
		- Ratio: 0.892. Amount: 0.177. Shape: 0.000.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Band-pass filter. Saved cutoff: 0.522; resonance: 0.771. [[Microfreak/UG/07 Filter/01 Modifying Sound/02 Band Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.078, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.089, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold, clock sync on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +1.000.
		- LFO → Pitch: −0.800.
		- LFO → Wave: +0.179.
		- LFO → Timbre: +0.277.
		- ENV → Cutoff: +0.234.
		- LFO → Cutoff: +0.224.
		- LFO → Assign 1 → Cycling Envelope Fall: +0.915.
		- LFO → Assign 2 → Shape: +0.489.
		- Cycling Envelope → Assign 3 → Decay/Release: −0.021.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
