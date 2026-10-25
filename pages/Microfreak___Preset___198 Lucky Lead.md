logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 198
preset-synth-microfreak-name:: Lucky Lead
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Template]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/197 Fusion Lead]]
next:: [[Microfreak/Preset/199 FM Bass]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
preset-synth-microfreak-parameter-payload-sha256:: d10e198325a1c9eef1774c39c2abef43d6dfbde20144505eec12fb3df7c08ee5
preset-synth-file:: [Lucky Lead — October 25 slot 198 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___198%20Lucky%20Lead___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 0738b4bc2e57ef4ef96e4faee615522f2992881f88b5e800eee125527232d034
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 198 over USB on October 25, 2026 with `mise run microfreak:download --slot 198`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 227, Factory 2.1 slot 41, Factory 3.0 slot 270, Factory 6.0 slot 115). Comparison used `mise run microfreak:compare`.
		- [Download the slot 198 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___198%20Lucky%20Lead___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/198 Lucky Lead/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SuperWave. [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
		- Wave: 1 (stored choice code). Detune: 0.363. Volume: 0.500.
		- Keyboard octave: 0. Glide: 0.150.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.661; resonance: 0.661. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.259, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.197, RiseSlp 0.500, FallLvl 0.163, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 9. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Timbre: −0.049.
		- PRESSURE → Cutoff: +0.629.
		- KEY/ARP → Cutoff: +1.000.
		- PRESSURE → Assign 1 → matrix amount LFO → Pitch: +0.011.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
