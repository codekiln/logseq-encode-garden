logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 061
preset-synth-microfreak-name:: AftrBlush
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/060 Unstable Solo]]
next:: [[Microfreak/Preset/062 Mood Strings]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/12 Modal]]
preset-synth-microfreak-parameter-payload-sha256:: 59fb6b5a3694cd0cb231bcd6af4a9ce01357cfd4bf0f84a10a089ebcae02759e
preset-synth-file:: [AftrBlush — October 25 slot 61 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___061%20AftrBlush___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 4003f2bd8bb04d55e95326ab610378e209972fbec561cbf0911afb66cee9698c
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 61 over USB on October 25, 2026 with `mise run microfreak:download --slot 61`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 146, Factory 2.1 slot 146, Factory 3.0 slot 146, Factory 6.0 slot 174). Comparison used `mise run microfreak:compare`.
		- [Download the slot 61 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___061%20AftrBlush___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/061 AftrBlush/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Modal. [[Microfreak/UG/06 Dig Osc/03 Types/12 Modal]]
		- Inharm: 0.510. Timbre: 0.926. Decay: 0.973.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.696; resonance: 0.757. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.371, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.163, RiseSlp 0.500, FallLvl 0.163, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 46877. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Cutoff: +0.605.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
