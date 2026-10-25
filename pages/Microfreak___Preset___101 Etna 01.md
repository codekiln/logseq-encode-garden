logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 101
preset-synth-microfreak-name:: Etna 01
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/100 Tinnendo]]
next:: [[Microfreak/Preset/102 Braine Storm]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/07 Waveshaper]]
preset-synth-microfreak-parameter-payload-sha256:: f1078bb42d271d6356423c7266be74ebf5bfde148efc2d37a8063cdc710fedd6
preset-synth-file:: [Etna 01 — October 25 slot 101 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___101%20Etna%2001___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 69b6d07aa9285558c421848b3ab7d3e37dba9614d2e5e0ad6c57fb8c30ded59d
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 101 over USB on October 25, 2026 with `mise run microfreak:download --slot 101`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 190, Factory 1.1 slot 190, Factory 2.1 slot 182, Factory 3.0 slot 182, Factory 6.0 slot 237). Comparison used `mise run microfreak:compare`.
		- [Download the slot 101 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___101%20Etna%2001___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/101 Etna 01/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Waveshaper. [[Microfreak/UG/06 Dig Osc/03 Types/07 Waveshaper]]
		- Wave: 0.315. Amount: 0.483. Asym: 0.189.
		- Keyboard octave: 0. Glide: 0.313.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.636; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.137, sustain 0.483. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.000, FallLvl 0.000, FallSlp 0.000, Hold 0.000, Amount 0.573. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.178. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Timbre: +0.418.
		- ENV → Cutoff: +0.302.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
