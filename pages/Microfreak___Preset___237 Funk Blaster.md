logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 237
preset-synth-microfreak-name:: Funk Blaster
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/236 Fastrun]]
next:: [[Microfreak/Preset/238 Deep Sea Call]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
preset-synth-microfreak-parameter-payload-sha256:: 5e9fc23bde2711d2e0375656668519607b566f93ca7b7fca989202e0f98ed152
preset-synth-file:: [Funk Blaster — October 25 slot 237 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___237%20Funk%20Blaster___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: b40f60e85aec4b4c26febddb35a07e8e5d08265e204d5a0c63b9ea73a686e89a
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 237 over USB on October 25, 2026 with `mise run microfreak:download --slot 237`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 306, Factory 6.0 slot 325). Comparison used `mise run microfreak:compare`.
		- [Download the slot 237 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___237%20Funk%20Blaster___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/237 Funk Blaster/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Bass. [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
		- Saturate: 0.001. Fold: 1.000. Noise: 0.212.
		- Keyboard octave: -3. Glide: 0.130.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.115; resonance: 0.846. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.154, decay/release 0.366, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.288, RiseSlp 0.248, FallLvl 0.717, FallSlp 0.996, Hold 1.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync on; stored division code: 7. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Wave: +0.740.
		- Cycling Envelope → Timbre: +0.985.
		- ENV → Cutoff: +0.750.
		- PRESSURE → Cutoff: −0.436.
		- LFO → Assign 1 → Unison Spread: +0.003.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
