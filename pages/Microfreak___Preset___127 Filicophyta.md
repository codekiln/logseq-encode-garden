logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 127
preset-synth-microfreak-name:: Filicophyta
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/126 Snitch 5]]
next:: [[Microfreak/Preset/128 KickBass]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
preset-synth-microfreak-parameter-payload-sha256:: a4c6aa226a5956cfef88b9a1301e0be74b69df6d17816d71838f9ac88dbed769
preset-synth-file:: [Filicophyta — October 25 slot 127 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___127%20Filicophyta___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: a0fc9707d27347015863958ce138a8b0af0796c6761ced5f4dc94251b1abee33
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 127 over USB on October 25, 2026 with `mise run microfreak:download --slot 127`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 104, Factory 2.1 slot 206, Factory 3.0 slot 206, Factory 6.0 slot 321). Comparison used `mise run microfreak:compare`.
		- [Download the slot 127 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___127%20Filicophyta___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/127 Filicophyta/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Wavetable. [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
		- Table: 8 (stored choice code). Position: 0.198. Chorus: 0.482.
		- Keyboard octave: +1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.216; resonance: 0.399. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.332, decay/release 0.358, sustain 0.646. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.318, RiseSlp 0.500, FallLvl 0.618, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.459. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Timbre: −0.380.
		- ENV → Timbre: +0.730.
		- LFO → Timbre: +0.808.
		- Cycling Envelope → Cutoff: +0.153.
		- ENV → Cutoff: +0.405.
		- LFO → Cutoff: +0.023.
		- PRESSURE → Cutoff: −0.167.
		- LFO → Assign 1 → Cycling Envelope Fall: +0.218.
		- Cycling Envelope → Assign 2 → LFO Rate: +0.287.
		- KEY/ARP → Assign 2 → LFO Rate: +0.634.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
