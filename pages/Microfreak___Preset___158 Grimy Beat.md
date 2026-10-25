logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 158
preset-synth-microfreak-name:: Grimy Beat
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/157 Ice Cold]]
next:: [[Microfreak/Preset/159 Snow Man]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
preset-synth-microfreak-parameter-payload-sha256:: 7a5b655f2a1fe40582a3c81af53db49a3727796e958f802674b858e3bedf0d27
preset-synth-file:: [Grimy Beat — October 25 slot 158 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___158%20Grimy%20Beat___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 062de4512974b2d23400022969a70fc67e43b2cb4415819b3d6c87189b71f370
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 158 over USB on October 25, 2026 with `mise run microfreak:download --slot 158`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 132, Factory 2.1 slot 234, Factory 3.0 slot 234, Factory 6.0 slot 138). Comparison used `mise run microfreak:compare`.
		- [Download the slot 158 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___158%20Grimy%20Beat___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/158 Grimy Beat/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Noise. [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
		- Wave: 1.000. Timbre: 0.487. Shape: 1.000.
		- Keyboard octave: -2. Glide: 0.000.
	- ## Filter
		- High-pass filter. Saved cutoff: 0.000; resonance: 1.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.390, sustain 0.189. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.185, FallSlp 0.149, Hold 0.000, Amount 0.942. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Square, clock sync on; stored division code: 12. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.329.
		- LFO → Timbre: +0.550.
		- KEY/ARP → Timbre: +1.000.
		- Cycling Envelope → Cutoff: +0.212.
		- ENV → Cutoff: +0.338.
		- KEY/ARP → Cutoff: +0.146.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
