logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 287
preset-synth-microfreak-name:: Holistic
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/286 Driftsynchros]]
next:: [[Microfreak/Preset/288 Solo Trancer]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
preset-synth-microfreak-parameter-payload-sha256:: d8922948e512f6658ab1a53d7c75e8bb449ae853ba2d7235f6015c061faf2621
preset-synth-file:: [Holistic — October 25 slot 287 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___287%20Holistic___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: dc3cc6ab34f6bbb472b0e92a5eec9d322b6a2cfa86a502354bbc9e5d9927f87a
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 287 over USB on October 25, 2026 with `mise run microfreak:download --slot 287`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 351, Factory 6.0 slot 262). Comparison used `mise run microfreak:compare`.
		- [Download the slot 287 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___287%20Holistic___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/287 Holistic/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Bass. [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
		- Saturate: 0.166. Fold: 0.054. Noise: 0.017.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.678; resonance: 0.113. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.639, decay/release 0.557, sustain 0.947. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.469, RiseSlp 0.500, FallLvl 0.539, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync off; stored normalized rate: 0.100. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.002.
		- ENV → Pitch: −0.002.
		- LFO → Pitch: −0.002.
		- Cycling Envelope → Wave: +0.003.
		- LFO → Wave: −0.001.
		- PRESSURE → Wave: +0.454.
		- Cycling Envelope → Timbre: +0.023.
		- LFO → Timbre: −0.006.
		- PRESSURE → Timbre: +0.123.
		- ENV → Cutoff: +0.209.
		- LFO → Cutoff: −0.020.
		- PRESSURE → Cutoff: −0.091.
		- KEY/ARP → Cutoff: +0.413.
		- LFO → Assign 1 → Cycling Envelope Hold: +0.520.
		- Cycling Envelope → Assign 2 → Filter Resonance: +0.097.
		- ENV → Assign 2 → Filter Resonance: −0.055.
		- LFO → Assign 2 → Filter Resonance: −0.130.
		- Cycling Envelope → Assign 3 → LFO Rate: +0.316.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
