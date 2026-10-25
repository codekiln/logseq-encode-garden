logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 068
preset-synth-microfreak-name:: Canadian Bass
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/067 Angels]]
next:: [[Microfreak/Preset/069 3opeR]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
preset-synth-microfreak-parameter-payload-sha256:: d863ee9ec96e2fa88d8d195119b2d766ec80c5a2c198bfa5b560556b30c775f7
preset-synth-file:: [Canadian Bass — October 25 slot 68 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___068%20Canadian%20Bass___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: b68ab4f39418b3170791b6df3ee2197bed72a649c5aba19874465ffd681f0172
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 68 over USB on October 25, 2026 with `mise run microfreak:download --slot 68`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 155, Factory 1.1 slot 155, Factory 2.1 slot 152, Factory 3.0 slot 152, Factory 6.0 slot 165). Comparison used `mise run microfreak:compare`.
		- [Download the slot 68 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___068%20Canadian%20Bass___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/068 Canadian Bass/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: V.Analog. [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		- Detune: 0.384. Shape: 0.292. Wave: 0.410.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.000; resonance: 0.810. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.594, sustain 0.562. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.163, RiseSlp 0.500, FallLvl 0.771, FallSlp 0.500, Hold 0.195, Amount 0.010. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 8. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Wave: +0.021.
		- ENV → Cutoff: +0.813.
		- PRESSURE → Cutoff: +0.275.
		- KEY/ARP → Assign 1 → Sustain: −1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
