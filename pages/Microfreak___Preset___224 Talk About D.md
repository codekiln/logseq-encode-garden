logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 224
preset-synth-microfreak-name:: Talk About D
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/223 Aphexian Kick]]
next:: [[Microfreak/Preset/225 Neutrino A]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: ac697e0381b311f88b6fe332a43e11f8e8a12ec910f58138e16f9e126a935475
preset-synth-file:: [Talk About D — October 25 slot 224 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___224%20Talk%20About%20D___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: b5dd05469491b16c2a7759b2b35cde5233d93c1a6538e6191e871e6a7b455591
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 224 over USB on October 25, 2026 with `mise run microfreak:download --slot 224`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 294, Factory 6.0 slot 178). Comparison used `mise run microfreak:compare`.
		- [Download the slot 224 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___224%20Talk%20About%20D___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/224 Talk About D/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 1.000. Rectification: 0.665. Noise: 0.294.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.278; resonance: 0.455. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.305, sustain 0.240. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.247, RiseSlp 0.500, FallLvl 0.134, FallSlp 0.500, Hold 0.521, Amount 0.341. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync on; stored division code: 9. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Wave: +0.107.
		- Cycling Envelope → Timbre: +0.250.
		- ENV → Cutoff: +1.000.
		- LFO → Cutoff: +0.401.
		- LFO → Assign 1 → Noise: +0.065.
		- Cycling Envelope → Assign 2 → Cycling Envelope Amount: −0.051.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
