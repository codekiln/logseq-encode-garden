logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 052
preset-synth-microfreak-name:: Ringussion
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/051 Solitude]]
next:: [[Microfreak/Preset/053 Crystal]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/12 Modal]]
preset-synth-microfreak-parameter-payload-sha256:: f4925935668171ceaa4e7be6cd9120242a5beb4c95f9c33779211ac2be7974f2
preset-synth-file:: [Ringussion — October 25 slot 52 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___052%20Ringussion___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: a6721b4ddf46015792a1e9a2d2de889e6b1443cb94bba6d2d7e152f0e400d7ee
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 52 over USB on October 25, 2026 with `mise run microfreak:download --slot 52`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 101, Factory 1.1 slot 101, Factory 2.1 slot 138, Factory 3.0 slot 138, Factory 6.0 slot 21). Comparison used `mise run microfreak:compare`.
		- [Download the slot 52 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___052%20Ringussion___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/052 Ringussion/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Modal. [[Microfreak/UG/06 Dig Osc/03 Types/12 Modal]]
		- Inharm: 0.786. Timbre: 0.589. Decay: 1.000.
		- Keyboard octave: -2. Glide: 0.000.
	- ## Filter
		- High-pass filter. Saved cutoff: 0.303; resonance: 0.861. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.000, sustain 0.314. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.414, RiseSlp 0.500, FallLvl 0.000, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold, clock sync off; stored normalized rate: 0.000. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- PRESSURE → Pitch: +0.913.
		- LFO → Wave: +0.507.
		- ENV → Cutoff: +0.137.
		- LFO → Cutoff: −0.110.
		- Cycling Envelope → Assign 1 → Sustain: −0.782.
		- Cycling Envelope → Assign 2 → Decay/Release: +0.337.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
