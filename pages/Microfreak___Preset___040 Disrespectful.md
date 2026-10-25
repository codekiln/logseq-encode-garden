logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 040
preset-synth-microfreak-name:: Disrespectful
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/039 Nostromo]]
next:: [[Microfreak/Preset/041 Madtraker]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
preset-synth-microfreak-parameter-payload-sha256:: a9b70974a725dd0a9ee1ca3ad2bbc6208aeede999148d8721490f6b2444ee582
preset-synth-file:: [Disrespectful — October 25 slot 40 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___040%20Disrespectful___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: de69847d0dacfbc3482a82ebd342126cbf6085a0962277750ef0ad0996a12b4d
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 40 over USB on October 25, 2026 with `mise run microfreak:download --slot 40`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 1, Factory 1.1 slot 1, Factory 2.1 slot None, Factory 3.0 slot 127, Factory 6.0 slot 424). Comparison used `mise run microfreak:compare`.
		- [Download the slot 40 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___040%20Disrespectful___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/040 Disrespectful/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Two Op. FM. [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
		- Ratio: 0.745. Amount: 0.325. Shape: 0.395.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- High-pass filter. Saved cutoff: 0.283; resonance: 1.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.294, sustain 0.000. Amp Mod is off. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.000, RiseSlp 0.000, FallLvl 0.131, FallSlp 0.000, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync on; stored division code: 0. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Pitch: +1.000.
		- Cycling Envelope → Timbre: +0.779.
		- ENV → Cutoff: +0.999.
		- PRESSURE → Cutoff: +0.271.
		- KEY/ARP → Cutoff: +0.796.
		- LFO → Assign 1 → Cycling Envelope Fall: +0.501.
		- LFO → Assign 2 → Shape: +0.688.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
