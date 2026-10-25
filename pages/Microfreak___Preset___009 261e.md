logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 009
preset-synth-microfreak-name:: 261e
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/008 Invitation]]
next:: [[Microfreak/Preset/010 Raverz]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/07 Waveshaper]]
preset-synth-microfreak-parameter-payload-sha256:: 5e9f6a5d31c85acd334937190ec9f7b9a8974c979b8195e27adc9dcaafc86887
preset-synth-file:: [261e — October 25 slot 9 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___009%20261e___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 6d38c8fc5fa7214d5e3c0d01dbbd1b6dc831bd228d9363dceece2b1063d69b7d
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 9 over USB on October 25, 2026 with `mise run microfreak:download --slot 9`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 9, Factory 2.1 slot 9, Factory 3.0 slot 9, Factory 6.0 slot None). Comparison used `mise run microfreak:compare`.
		- [Download the slot 9 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___009%20261e___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/009 261e/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [Waveshaper]([[Microfreak/UI/Oscillator/Knob/Type/Waveshaper]]). [[Microfreak/UG/06 Dig Osc/03 Types/07 Waveshaper]]
		- [Wave]([[Microfreak/UI/Oscillator/Knob/Type/Waveshaper/Wave]]): 0.935. [Amount]([[Microfreak/UI/Oscillator/Knob/Type/Waveshaper/Amount]]): 0.000. [Asym]([[Microfreak/UI/Oscillator/Knob/Type/Waveshaper/Asym]]): 0.361.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/03 Bottom/01 Octave]]): -2. [Glide]([[Microfreak/UI/Front/Row/02 Main/01 Glide Knob]]): 0.183.
	- ## Filter
		- [Low-pass]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Button/Type/LPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): 1.000; [resonance]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Resonance]]): 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Attack]]) 0.000, [decay/release]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Decay Rel]]) 0.176, [sustain]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Sustain]]) 0.591. [Amp Mod]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode]]): [Env]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode/Env]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise]]) 0.000, [RiseSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise/Shift]]) 0.500, [FallLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall]]) 0.419, [FallSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall/Shift]]) 0.500, [Hold]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Hold Sustain]]) 0.000, [Amount]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Amount]]) 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Sine]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Button/Shape/Sine]]), clock [sync]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Knob/Rate/Press]]) off; stored normalized [rate]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Knob/Rate]]): 0.338. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope]]) → [Timbre]([[Microfreak/UI/Oscillator/Knob/Timbre]]): +0.597.
		- [PRESSURE]([[Microfreak/UI/Front/Row/05 Keys]]) → [Timbre]([[Microfreak/UI/Oscillator/Knob/Timbre]]): −1.000.
		- [PRESSURE]([[Microfreak/UI/Front/Row/05 Keys]]) → [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): −1.000.
		- [LFO]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO]]) → [Assign 1]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/1]]) → [Asym]([[Microfreak/UI/Oscillator/Knob/Type/Waveshaper/Asym]]): +0.051.
		- [PRESSURE]([[Microfreak/UI/Front/Row/05 Keys]]) → [Assign 1]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/1]]) → [Asym]([[Microfreak/UI/Oscillator/Knob/Type/Waveshaper/Asym]]): +1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/01 Top/02 Paraphonic Button]]) mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
