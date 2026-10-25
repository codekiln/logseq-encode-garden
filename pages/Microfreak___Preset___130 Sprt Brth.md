logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 130
preset-synth-microfreak-name:: Sprt Brth
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Custom]]
prev:: [[Microfreak/Preset/129 Opst]]
next:: [[Microfreak/Preset/131 Colik]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
preset-synth-microfreak-parameter-payload-sha256:: b11765181a98c90b9441408d429bf8147216e70737583bd752de110a362a5a1c
preset-synth-file:: [Sprt Brth — October 25 slot 130 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___130%20Sprt%20Brth___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: bc2653331cc2c567f41c54999dce4956ec48452155bd5921dbd33a1c1a364f92
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 130 over USB on October 25, 2026 with `mise run microfreak:download --slot 130`. Two consecutive reads returned the same file.
		- The parameter payload matches no MIDI Control Center factory archive.
		- [Download the slot 130 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___130%20Sprt%20Brth___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/130 Sprt Brth/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [Wavetable]([[Microfreak/UI/Oscillator/Knob/Type/Wavetable]]). [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
		- [Table]([[Microfreak/UI/Oscillator/Knob/Type/Wavetable/Table]]): 9 (stored choice code). [Position]([[Microfreak/UI/Oscillator/Knob/Type/Wavetable/Position]]): 0.405. [Chorus]([[Microfreak/UI/Oscillator/Knob/Type/Wavetable/Chorus]]): 0.350.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/Bottom/01 Octave]]): +1. [Glide]([[Microfreak/UI/Front/Row/Middle/01 Glide Knob]]): 0.104.
	- ## Filter
		- [Low-pass]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Button/Type/LPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): 0.382; [resonance]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Resonance]]): 0.553. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Attack]]) 0.631, [decay/release]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Decay Rel]]) 0.412, [sustain]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Sustain]]) 0.682. [Amp Mod]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode]]): [Loop]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode/Loop]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise]]) 0.571, [RiseSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise/Shift]]) 0.648, [FallLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall]]) 0.657, [FallSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall/Shift]]) 0.036, [Hold]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Hold Sustain]]) 0.506, [Amount]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Amount]]) 0.187. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Sample-and-Hold Filtered]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Button/Shape/Random Gliding]]), clock [sync]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate/Press]]) off; stored normalized [rate]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate]]): 0.839. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope]]) → Pitch: −0.040.
		- [LFO]([[Microfreak/UI/Front/Row/Bottom/04 LFO]]) → [Wave]([[Microfreak/UI/Oscillator/Knob/Wave]]): +0.044.
		- [LFO]([[Microfreak/UI/Front/Row/Bottom/04 LFO]]) → [Cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): −0.040.
		- [PRESSURE]([[Microfreak/UI/Front/Row/Bottom/06 Keyboard]]) → [Cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): −0.068.
		- [LFO]([[Microfreak/UI/Front/Row/Bottom/04 LFO]]) → [Assign 1]([[Microfreak/UI/Front/Row/Top/01 Matrix/Button/Assn/1]]) → [Glide]([[Microfreak/UI/Front/Row/Middle/01 Glide Knob]]): +0.071.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/Top/02 Paraphonic Button]]) mode: on.
	- ## Customized controls
		- No factory preset is close. The nearest factory payload, [[Microfreak/Preset/027 Nost]] (Factory 1.1 slot 203), differs in 17 controls.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
