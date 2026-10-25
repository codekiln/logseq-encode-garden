logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 373
preset-synth-microfreak-name:: TMF.24.11.25.C
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Custom]]
prev:: [[Microfreak/Preset/372 TMF.24.11.25.B]]
next:: [[Microfreak/Preset/374 TMF.24.12.04.A]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
preset-synth-microfreak-parameter-payload-sha256:: 1caba704586161998b1962565a0f26eca262d0342bb2fae7a02ff782aa475c8f
preset-synth-file:: [TMF.24.11.25.C — October 25 slot 373 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___373%20TMF.24.11.25.C___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 96e24277641cddaf731300eeb6ff8bd6e42ceea33df6580e0554d29086cef79e
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 373 over USB on October 25, 2026 with `mise run microfreak:download --slot 373`. Two consecutive reads returned the same file.
		- The parameter payload matches no MIDI Control Center factory archive.
		- [Download the slot 373 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___373%20TMF.24.11.25.C___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/373 TMF.24.11.25.C/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [BasicWaves]([[Microfreak/UI/Oscillator/Knob/Type/BasicWaves]]). [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
		- [Morph]([[Microfreak/UI/Oscillator/Knob/Type/BasicWaves/Morph]]): 0.475. [Sym]([[Microfreak/UI/Oscillator/Knob/Type/BasicWaves/Sym]]): 0.832. [Sub]([[Microfreak/UI/Oscillator/Knob/Type/BasicWaves/Sub]]): 0.000.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/Bottom/01 Octave]]): -1. [Glide]([[Microfreak/UI/Front/Row/Middle/01 Glide Knob]]): 0.099.
	- ## Filter
		- [Band-pass]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Button/Type/BPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): 0.630; [resonance]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Resonance]]): 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/02 Band Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Attack]]) 0.364, [decay/release]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Decay Rel]]) 0.440, [sustain]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Sustain]]) 0.320. [Amp Mod]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode]]): [Run]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode/Run]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise]]) 0.537, [RiseSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise/Shift]]) 0.500, [FallLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall]]) 0.665, [FallSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall/Shift]]) 0.500, [Hold]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Hold Sustain]]) 0.000, [Amount]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Amount]]) 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Sine]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Button/Shape/Sine]]), clock [sync]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate/Press]]) off; stored normalized [rate]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate]]): 0.148. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [LFO]([[Microfreak/UI/Front/Row/Bottom/04 LFO]]) → [Cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): +0.359.
		- [PRESSURE]([[Microfreak/UI/Front/Row/Bottom/06 Keyboard]]) → [Assign 1]([[Microfreak/UI/Front/Row/Top/01 Matrix/Button/Assn/1]]) → [LFO Rate]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate]]): +0.765.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/Top/02 Paraphonic Button]]) mode: on.
	- ## Customized controls
		- No factory preset is close. The nearest factory payload, [[Microfreak/Preset/304 Saw Vox]] (Factory 2.1 slot 51), differs in 15 controls.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
