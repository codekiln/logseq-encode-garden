logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 360
preset-synth-microfreak-name:: TMF.24.11.18.A
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Custom]]
prev:: [[Microfreak/Preset/359 Init]]
next:: [[Microfreak/Preset/361 TMF.24.11.18.B]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
preset-synth-microfreak-parameter-payload-sha256:: 371154e3feff5fd5c1be9de644c0919ac11a341819636dd7acffa9141e48bbda
preset-synth-file:: [TMF.24.11.18.A — October 25 slot 360 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___360%20TMF.24.11.18.A___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 3e155a3e0041633d008489f9f47526a224446a2219c76e28710f9a60ea5643ef
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 360 over USB on October 25, 2026 with `mise run microfreak:download --slot 360`. Two consecutive reads returned the same file.
		- The parameter payload matches no MIDI Control Center factory archive.
		- [Download the slot 360 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___360%20TMF.24.11.18.A___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/360 TMF.24.11.18.A/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [BasicWaves]([[Microfreak/UI/Oscillator/Knob/Type/BasicWaves]]). [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
		- [Morph]([[Microfreak/UI/Oscillator/Knob/Type/BasicWaves/Morph]]): 0.256. [Sym]([[Microfreak/UI/Oscillator/Knob/Type/BasicWaves/Sym]]): 0.000. [Sub]([[Microfreak/UI/Oscillator/Knob/Type/BasicWaves/Sub]]): 0.000.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/Bottom/01 Octave]]): 0. [Glide]([[Microfreak/UI/Front/Row/Middle/01 Glide Knob]]): 0.000.
	- ## Filter
		- [Low-pass]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Button/Type/LPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): 1.000; [resonance]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Resonance]]): 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Attack]]) 0.000, [decay/release]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Decay Rel]]) 0.259, [sustain]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Sustain]]) 1.000. [Amp Mod]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode]]): [Run]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode/Run]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise]]) 0.473, [RiseSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise/Shift]]) 0.500, [FallLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall]]) 0.475, [FallSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall/Shift]]) 0.500, [Hold]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Hold Sustain]]) 0.317, [Amount]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Amount]]) 0.498. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Sine]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Button/Shape/Sine]]), clock [sync]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate/Press]]) on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope]]) → Pitch: +0.250.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/Top/02 Paraphonic Button]]) mode: on.
	- ## Customized controls
		- Compared with the nearest factory payload, [[Microfreak/Preset/304 Saw Vox]] (Factory 2.1 slot 51); 6 controls differ.
		- [Oscillator type]([[Microfreak/UI/Oscillator/Knob/Type]]): BasicWaves (factory Vocoder).
		- [Rise]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise]]): 0.473 (factory 0.163).
		- [Fall]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall]]): 0.475 (factory 0.163).
		- [Hold/Sustain]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Hold Sustain]]): 0.317 (factory 0.000).
		- [Cycling Envelope amount]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Amount]]): 0.498 (factory 1.000).
		- [Matrix]([[Microfreak/UI/Front/Row/Top/01 Matrix/Knob]]) Cycling Envelope → Pitch: +0.250 (factory +0.000).
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
