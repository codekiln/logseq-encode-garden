logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 282
preset-synth-microfreak-name:: Cosy Evening
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/281 Smooth IPA]]
next:: [[Microfreak/Preset/283 Far Away]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
preset-synth-microfreak-parameter-payload-sha256:: 13b9f0e5cdd341ce9eea059e019eb95ffb5a43012daa4193f36914ff492d5b35
preset-synth-file:: [Cosy Evening — October 25 slot 282 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___282%20Cosy%20Evening___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: f8116cc58fffbd0e0d6813f183c8fe944d3bd65a7d26fefa1e5d2702873fc200
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 282 over USB on October 25, 2026 with `mise run microfreak:download --slot 282`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 347, Factory 6.0 slot 288). Comparison used `mise run microfreak:compare`.
		- [Download the slot 282 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___282%20Cosy%20Evening___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/282 Cosy Evening/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SawX. [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
		- Saw Mod: 0.064. Shape: 0.241. Noise: 0.293.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.000; resonance: 0.120. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.069, decay/release 0.459, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.461, RiseSlp 0.500, FallLvl 0.486, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 4. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.006.
		- ENV → Timbre: −0.171.
		- ENV → Cutoff: +0.711.
		- LFO → Cutoff: −0.018.
		- PRESSURE → Cutoff: +0.339.
		- KEY/ARP → Cutoff: −0.366.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
