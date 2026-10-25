logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 084
preset-synth-microfreak-name:: Press So
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/083 Leeds Strings]]
next:: [[Microfreak/Preset/085 Arp 2ol9]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
preset-synth-microfreak-parameter-payload-sha256:: 8f665edb4121c384dd673949b6e4fc66691401b30ff85f6ac67a8045703593e1
preset-synth-file:: [Press So — October 25 slot 84 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___084%20Press%20So___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 846e1ee3c17d60f029df9e6ff6bd8b0a1e86c555cdb18a3e2c56e5a7117871f2
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 84 over USB on October 25, 2026 with `mise run microfreak:download --slot 84`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 17, Factory 1.1 slot 17, Factory 2.1 slot None, Factory 3.0 slot 167, Factory 6.0 slot 175). Comparison used `mise run microfreak:compare`.
		- [Download the slot 84 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___084%20Press%20So___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/084 Press So/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: BasicWaves. [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
		- Morph: 0.256. Sym: 0.270. Sub: 0.432.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.333; resonance: 0.380. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.332, sustain 0.665. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.169, RiseSlp 0.500, FallLvl 0.237, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync on; stored division code: 2. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Wave: +0.091.
		- Cycling Envelope → Timbre: +0.762.
		- LFO → Timbre: +0.532.
		- ENV → Cutoff: +0.240.
		- PRESSURE → Assign 2 → matrix amount Cycling Envelope → Assign 1: +0.475.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
