logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 187
preset-synth-microfreak-name:: KarpluStrings
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Template]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/186 Strings 2]]
next:: [[Microfreak/Preset/188 Karpad]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/05 KarplusStr]]
preset-synth-microfreak-parameter-payload-sha256:: a9d5c973b7cd06cbe1786afadb81af7fe99b293cfcaff5f81d294abe224426ef
preset-synth-file:: [KarpluStrings — October 25 slot 187 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___187%20KarpluStrings___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 4d59308b23f06a069bf06b16395eb09b9188ca816aac84d8e4139b4f34c53a0b
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 187 over USB on October 25, 2026 with `mise run microfreak:download --slot 187`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 217, Factory 2.1 slot 30, Factory 3.0 slot 260, Factory 6.0 slot 119). Comparison used `mise run microfreak:compare`.
		- [Download the slot 187 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___187%20KarpluStrings___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/187 KarpluStrings/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: KarplusStr. [[Microfreak/UG/06 Dig Osc/03 Types/05 KarplusStr]]
		- Bow: 0.236. Position: 0.591. Decay: 0.921.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.591; resonance: 0.748. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.520, sustain 0.386. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.276, FallSlp 0.222, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.386. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Wave: +0.728.
		- PRESSURE → Wave: −1.000.
		- Cycling Envelope → Cutoff: +0.253.
		- ENV → Cutoff: +0.638.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
