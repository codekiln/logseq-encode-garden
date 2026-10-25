logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 112
preset-synth-microfreak-name:: Anlg
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/111 AcidFrog]]
next:: [[Microfreak/Preset/113 D3 Chords]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
preset-synth-microfreak-parameter-payload-sha256:: 880bc46d4e7f57a4db3ac87b4e16400aacd2e4d068dd4ee653170a9a929365b6
preset-synth-file:: [Anlg — October 25 slot 112 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___112%20Anlg___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: f5474bf7c6f4a596628fe5471f0c315c93d22c514d9ea7513c9b33bfa38d5b73
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 112 over USB on October 25, 2026 with `mise run microfreak:download --slot 112`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 207, Factory 2.1 slot 192, Factory 3.0 slot 192, Factory 6.0 slot 370). Comparison used `mise run microfreak:compare`.
		- [Download the slot 112 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___112%20Anlg___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/112 Anlg/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: BasicWaves. [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
		- Morph: 0.615. Sym: 0.000. Sub: 0.759.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.390; resonance: 0.875. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.445, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.181, RiseSlp 0.500, FallLvl 0.290, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold, clock sync on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.004.
		- LFO → Wave: +0.113.
		- Cycling Envelope → Timbre: +1.000.
		- PRESSURE → Timbre: −1.000.
		- ENV → Cutoff: +0.251.
		- LFO → Cutoff: +0.134.
		- PRESSURE → Cutoff: +0.183.
		- KEY/ARP → Cutoff: +1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
