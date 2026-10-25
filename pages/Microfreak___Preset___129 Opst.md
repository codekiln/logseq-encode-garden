logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 129
preset-synth-microfreak-name:: Opst
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Percussion]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Custom]]
prev:: [[Microfreak/Preset/128 KickBass]]
next:: [[Microfreak/Preset/130 Sprt Brth]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
preset-synth-microfreak-parameter-payload-sha256:: 756b87640a690e882d766897d297dfe7ca606990ad45fb20ad1312cf2793c5e9
preset-synth-file:: [Opst — October 25 slot 129 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___129%20Opst___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 5f60d89a40b9ff7301fa3c20eee7888bca45fff34a6e4f1f1734b7dcde91fdb3
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 129 over USB on October 25, 2026 with `mise run microfreak:download --slot 129`. Two consecutive reads returned the same file.
		- The parameter payload matches no MIDI Control Center factory archive.
		- [Download the slot 129 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___129%20Opst___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/129 Opst/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [BasicWaves]([[Microfreak/UI/Oscillator/Knob/Type/BasicWaves]]). [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
		- [Morph]([[Microfreak/UI/Oscillator/Knob/Type/BasicWaves/Morph]]): 0.418. [Sym]([[Microfreak/UI/Oscillator/Knob/Type/BasicWaves/Sym]]): 0.046. [Sub]([[Microfreak/UI/Oscillator/Knob/Type/BasicWaves/Sub]]): 0.103.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/Bottom/01 Octave]]): +1. [Glide]([[Microfreak/UI/Front/Row/Middle/01 Glide Knob]]): 0.104.
	- ## Filter
		- [Low-pass]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Button/Type/LPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): 0.481; [resonance]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Resonance]]): 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Attack]]) 0.631, [decay/release]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Decay Rel]]) 0.412, [sustain]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Sustain]]) 0.682. [Amp Mod]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode]]): [Loop]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode/Loop]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise]]) 0.444, [RiseSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise/Shift]]) 0.311, [FallLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall]]) 0.108, [FallSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall/Shift]]) 0.647, [Hold]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Hold Sustain]]) 0.000, [Amount]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Amount]]) 0.279. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Sample-and-Hold Filtered]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Button/Shape/Random Gliding]]), clock [sync]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate/Press]]) off; stored normalized [rate]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate]]): 0.839. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope]]) → Pitch: −0.040.
		- [LFO]([[Microfreak/UI/Front/Row/Bottom/04 LFO]]) → Pitch: +0.003.
		- [PRESSURE]([[Microfreak/UI/Front/Row/Bottom/06 Keyboard]]) → [Cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): −0.068.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/Top/02 Paraphonic Button]]) mode: on.
	- ## Customized controls
		- Compared with the nearest factory payload, [[Microfreak/Preset/027 Nost]] (Factory 1.1 slot 203); 7 controls differ.
		- [Octave]([[Microfreak/UI/Front/Row/Bottom/01 Octave]]): +1 (factory 0).
		- [Cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): 0.481 (factory 0.699).
		- [Rise]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise]]): 0.444 (factory 0.508).
		- [Fall]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall]]): 0.108 (factory 0.457).
		- [Cycling Envelope amount]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Amount]]): 0.279 (factory 0.164).
		- [Attack]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Attack]]): 0.631 (factory 0.119).
		- [Decay/Release]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Decay Rel]]): 0.412 (factory 0.648).
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
