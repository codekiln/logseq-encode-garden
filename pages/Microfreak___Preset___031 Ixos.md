logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 031
preset-synth-microfreak-name:: Ixos
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/030 HarmonicTuneUp]]
next:: [[Microfreak/Preset/032 Chord Bass]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
preset-synth-microfreak-parameter-payload-sha256:: 296df18a8336c951d48f5717f72563255025796061c2277be0e8fca14a3c1655
preset-synth-file:: [Ixos — October 25 slot 31 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___031%20Ixos___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: d90ab86eddeea7ad611f8e6401ea942d5d320abe9352c94d2eca4227f5b9f09b
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 31 over USB on October 25, 2026 with `mise run microfreak:download --slot 31`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 119, Factory 1.1 slot 119, Factory 2.1 slot 119, Factory 3.0 slot 119, Factory 6.0 slot 381). Comparison used `mise run microfreak:compare`.
		- [Download the slot 31 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___031%20Ixos___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/031 Ixos/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: V.Analog. [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		- Detune: 0.627. Shape: 0.658. Wave: 0.238.
		- Keyboard octave: 0. Glide: 0.149.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.133; resonance: 0.794. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.346, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.000, FallLvl 0.359, FallSlp 0.000, Hold 0.141, Amount 0.898. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 6. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Timbre: +0.094.
		- ENV → Cutoff: +0.062.
		- PRESSURE → Cutoff: +1.000.
		- LFO → Assign 1 → Sustain: −0.002.
		- PRESSURE → Assign 1 → Sustain: +1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
