logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 162
preset-synth-microfreak-name:: Roid
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/161 Crackle Sleep]]
next:: [[Microfreak/Preset/163 Sausage Bass]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
preset-synth-microfreak-parameter-payload-sha256:: a91a9af59db3012d1be62048396a7df342dede6f339b600d84ae10626f81a8d7
preset-synth-file:: [Roid — October 25 slot 162 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___162%20Roid___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 3718cc52e1b6970cca4d803bdcb2c4feb656c9565a068573cca93d55c9bb4e9c
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 162 over USB on October 25, 2026 with `mise run microfreak:download --slot 162`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 136, Factory 2.1 slot 238, Factory 3.0 slot 238, Factory 6.0 slot 20). Comparison used `mise run microfreak:compare`.
		- [Download the slot 162 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___162%20Roid___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/162 Roid/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Noise. [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
		- Wave: 0.060. Timbre: 0.500. Shape: 0.709.
		- Keyboard octave: 0. Glide: 0.169.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.232; resonance: 0.100. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.359, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.132, RiseSlp 0.864, FallLvl 0.139, FallSlp 0.009, Hold 0.041, Amount 0.540. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sawtooth, clock sync on; stored division code: 2. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.002.
		- LFO → Wave: −0.052.
		- Cycling Envelope → Timbre: +0.945.
		- Cycling Envelope → Cutoff: −0.086.
		- ENV → Cutoff: +0.661.
		- PRESSURE → Cutoff: +0.690.
		- KEY/ARP → Cutoff: +0.566.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
