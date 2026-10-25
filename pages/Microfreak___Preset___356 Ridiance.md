logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 356
preset-synth-microfreak-name:: Ridiance
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Brass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Custom]]
prev:: [[Microfreak/Preset/355 PersnikT]]
next:: [[Microfreak/Preset/357 2024-11-10_Sun]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
preset-synth-microfreak-parameter-payload-sha256:: d81ef669dda44854a32938ee0201bf7ed300c6b123bdd92e55b3ce38121366b4
preset-synth-file:: [Ridiance — October 25 slot 356 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___356%20Ridiance___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 846dfd47c90c101f49f92f8475423890be10ecb9c396acb8f654c778fdc4d4f3
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 356 over USB on October 25, 2026 with `mise run microfreak:download --slot 356`. Two consecutive reads returned the same file.
		- The parameter payload matches no MIDI Control Center factory archive.
		- [Download the slot 356 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___356%20Ridiance___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/356 Ridiance/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [Two Op. FM]([[Microfreak/UI/Oscillator/Knob/Type/Two Op.FM]]). [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
		- [Ratio]([[Microfreak/UI/Oscillator/Knob/Type/Two Op.FM/Ratio]]): 0.314. [Amount]([[Microfreak/UI/Oscillator/Knob/Type/Two Op.FM/Amount]]): 0.373. [Shape]([[Microfreak/UI/Oscillator/Knob/Type/Two Op.FM/Shape]]): 0.047.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/03 Bottom/01 Octave]]): -1. [Glide]([[Microfreak/UI/Front/Row/02 Main/01 Glide Knob]]): 0.000.
	- ## Filter
		- [Low-pass]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Button/Type/LPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): 0.388; [resonance]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Resonance]]): 0.142. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Attack]]) 0.241, [decay/release]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Decay Rel]]) 0.266, [sustain]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Sustain]]) 0.681. [Amp Mod]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode]]): [Env]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode/Env]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise]]) 0.321, [RiseSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise/Shift]]) 0.800, [FallLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall]]) 0.785, [FallSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall/Shift]]) 0.500, [Hold]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Hold Sustain]]) 0.599, [Amount]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Amount]]) 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Sine]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Button/Shape/Sine]]), clock [sync]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Knob/Rate/Press]]) off; stored normalized [rate]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Knob/Rate]]): 0.396. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [LFO]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO]]) → [Timbre]([[Microfreak/UI/Oscillator/Knob/Timbre]]): +0.006.
		- [ENV]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope]]) → [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): +0.345.
		- [LFO]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO]]) → [Assign 1]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/1]]) → [Decay/Release]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Decay Rel]]): +0.291.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/01 Top/02 Paraphonic Button]]) mode: on.
	- ## Customized controls
		- No factory preset is close. The nearest factory payload, [[Microfreak/Preset/135 No Sleep]] (Factory 2.0 slot 111), differs in 20 controls.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
