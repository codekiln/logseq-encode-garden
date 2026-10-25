logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 197
preset-synth-microfreak-name:: Fusion Lead
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Template]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/196 Chorgan]]
next:: [[Microfreak/Preset/198 Lucky Lead]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
preset-synth-microfreak-parameter-payload-sha256:: 4d64d4ad6163a473962b5d04276278083f3b820ac103a9f5b7e7ab384ca24983
preset-synth-file:: [Fusion Lead — October 25 slot 197 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___197%20Fusion%20Lead___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: a1c4a24a975655bd6083a313916af5d65588032a0bee1fd329796e7c4ba55f80
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 197 over USB on October 25, 2026 with `mise run microfreak:download --slot 197`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 226, Factory 2.1 slot 40, Factory 3.0 slot 27, Factory 6.0 slot None). Comparison used `mise run microfreak:compare`.
		- [Download the slot 197 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___197%20Fusion%20Lead___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/197 Fusion Lead/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: V.Analog. [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		- Detune: 0.259. Shape: 0.579. Wave: 0.622.
		- Keyboard octave: 0. Glide: 0.190.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.480; resonance: 0.441. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.371, sustain 0.642. Amp Mod is off. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.197, RiseSlp 0.500, FallLvl 0.163, FallSlp 0.500, Hold 0.000, Amount 0.841. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 9. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Cutoff: +0.863.
		- PRESSURE → Cutoff: +0.225.
		- KEY/ARP → Cutoff: +0.693.
		- PRESSURE → Assign 1 → matrix amount LFO → Pitch: +0.012.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
