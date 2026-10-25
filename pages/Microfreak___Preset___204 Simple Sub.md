logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 204
preset-synth-microfreak-name:: Simple Sub
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Template]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/203 Acid Bass 1]]
next:: [[Microfreak/Preset/205 Exotic Perc]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/07 Waveshaper]]
preset-synth-microfreak-parameter-payload-sha256:: 0778bb30dc7551f44e8ae7b76fba72a1b3899b1b36e8d5774b6fd7bac6fd195f
preset-synth-file:: [Simple Sub — October 25 slot 204 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___204%20Simple%20Sub___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 37e4079fc7d06e7641a99001d75acce5a08a0ae57be8ab27e9cf9db2a6d4117f
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 204 over USB on October 25, 2026 with `mise run microfreak:download --slot 204`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 232, Factory 2.1 slot 47, Factory 3.0 slot 276, Factory 6.0 slot 373). Comparison used `mise run microfreak:compare`.
		- [Download the slot 204 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___204%20Simple%20Sub___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/204 Simple Sub/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Waveshaper. [[Microfreak/UG/06 Dig Osc/03 Types/07 Waveshaper]]
		- Wave: 0.395. Amount: 0.015. Asym: 0.000.
		- Keyboard octave: -2. Glide: 0.000.
	- ## Filter
		- High-pass filter. Saved cutoff: 0.277; resonance: 1.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.031, sustain 0.000. Amp Mod is off. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.000, RiseSlp 0.000, FallLvl 0.279, FallSlp 0.000, Hold 0.000, Amount 0.480. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync on; stored division code: 5. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Pitch: +0.999.
		- ENV → Cutoff: +0.891.
		- PRESSURE → Cutoff: +1.000.
		- KEY/ARP → Cutoff: +0.797.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
