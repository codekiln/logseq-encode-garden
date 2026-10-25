logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 283
preset-synth-microfreak-name:: Far Away
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/282 Cosy Evening]]
next:: [[Microfreak/Preset/284 Synz Today]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: 830a057ead14e6d7856a447ee9d1923911f2903387b1e3166ab715b7086564c3
preset-synth-file:: [Far Away — October 25 slot 283 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___283%20Far%20Away___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: cca1ab6529fa0f8db5d6bfbb22bcfe22d71361ae19b2acc6ac255a5a5add1549
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 283 over USB on October 25, 2026 with `mise run microfreak:download --slot 283`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 348, Factory 6.0 slot 3). Comparison used `mise run microfreak:compare`.
		- [Download the slot 283 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___283%20Far%20Away___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/283 Far Away/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 0.379. Rectification: 0.160. Noise: 0.063.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.346; resonance: 0.512. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.004, decay/release 0.636, sustain 0.356. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.826, RiseSlp 0.500, FallLvl 1.000, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 6. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: −0.002.
		- ENV → Wave: +0.083.
		- LFO → Timbre: +0.162.
		- ENV → Cutoff: +0.199.
		- PRESSURE → Cutoff: +0.252.
		- KEY/ARP → Cutoff: +0.324.
		- Cycling Envelope → Assign 1 → Noise: +0.641.
		- PRESSURE → Assign 1 → Noise: +1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
