logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 134
preset-synth-microfreak-name:: Qbit Brass
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/133 Malfunction]]
next:: [[Microfreak/Preset/135 No Sleep]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
preset-synth-microfreak-parameter-payload-sha256:: 89104f4b6a88d0f5aeb238ee6f601ab2526ddafe1926834a5afb5f219958766c
preset-synth-file:: [Qbit Brass — October 25 slot 134 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___134%20Qbit%20Brass___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 913909de7e897290264ed0bc80f0b59312191f4a7afbd742f8d5c7e1c39edcbf
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 134 over USB on October 25, 2026 with `mise run microfreak:download --slot 134`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 110, Factory 2.1 slot 212, Factory 3.0 slot 212, Factory 6.0 slot 227). Comparison used `mise run microfreak:compare`.
		- [Download the slot 134 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___134%20Qbit%20Brass___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/134 Qbit Brass/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: V.Analog. [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		- Detune: 1.000. Shape: 0.340. Wave: 1.000.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.088; resonance: 0.101. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.209, decay/release 0.716, sustain 0.566. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.024, RiseSlp 0.500, FallLvl 0.356, FallSlp 0.500, Hold 0.052, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync off; stored normalized rate: 0.148. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.001.
		- Cycling Envelope → Wave: −0.010.
		- LFO → Wave: +0.009.
		- KEY/ARP → Wave: +0.100.
		- Cycling Envelope → Timbre: +0.092.
		- LFO → Timbre: +0.007.
		- ENV → Cutoff: +0.537.
		- KEY/ARP → Cutoff: +0.036.
		- ENV → Assign 1 → Wave: −1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
