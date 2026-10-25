logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 392
preset-synth-microfreak-name:: Blithrifi
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Custom]]
prev:: [[Microfreak/Preset/391 Dnit2]]
next:: [[Microfreak/Preset/393 answ er]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
preset-synth-microfreak-parameter-payload-sha256:: 85e22e54799157d0ccdf72d183844bc454d4e5a31c91a93a01c765f867723805
preset-synth-file:: [Blithrifi — October 25 slot 392 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___392%20Blithrifi___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 31de2531e90e670a1abd96c58d757ed8320b10cf9bd3b750ce1a750dd4e2354e
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 392 over USB on October 25, 2026 with `mise run microfreak:download --slot 392`. Two consecutive reads returned the same file.
		- The parameter payload matches no MIDI Control Center factory archive.
		- [Download the slot 392 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___392%20Blithrifi___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/392 Blithrifi/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [V.Analog]([[Microfreak/UI/Oscillator/Knob/Type/VAnalog]]). [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		- [Detune]([[Microfreak/UI/Oscillator/Knob/Type/VAnalog/Detune]]): 0.498. [Shape]([[Microfreak/UI/Oscillator/Knob/Type/VAnalog/Shape]]): 0.498. [Wave]([[Microfreak/UI/Oscillator/Knob/Type/VAnalog/Wave]]): 0.103.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/Bottom/01 Octave]]): -1. [Glide]([[Microfreak/UI/Front/Row/Middle/01 Glide Knob]]): 0.284.
	- ## Filter
		- [Low-pass]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Button/Type/LPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): 0.228; [resonance]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Resonance]]): 0.544. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Attack]]) 0.410, [decay/release]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Decay Rel]]) 0.351, [sustain]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Sustain]]) 0.350. [Amp Mod]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode]]): [Loop]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode/Loop]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise]]) 0.269, [RiseSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise/Shift]]) 0.500, [FallLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall]]) 0.190, [FallSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall/Shift]]) 0.500, [Hold]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Hold Sustain]]) 0.444, [Amount]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Amount]]) 0.704. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Sine]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Button/Shape/Sine]]), clock [sync]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate/Press]]) off; stored normalized [rate]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate]]): 0.505. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope]]) → Pitch: +0.031.
		- [KEY/ARP]([[Microfreak/UI/Front/Row/Bottom/06 Keyboard]]) → [Wave]([[Microfreak/UI/Oscillator/Knob/Wave]]): +0.068.
		- [PRESSURE]([[Microfreak/UI/Front/Row/Bottom/06 Keyboard]]) → [Timbre]([[Microfreak/UI/Oscillator/Knob/Timbre]]): +0.993.
		- [ENV]([[Microfreak/UI/Front/Row/Bottom/05 Envelope]]) → [Cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): +0.569.
		- [LFO]([[Microfreak/UI/Front/Row/Bottom/04 LFO]]) → [Cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): +0.148.
		- [PRESSURE]([[Microfreak/UI/Front/Row/Bottom/06 Keyboard]]) → [Assign 1]([[Microfreak/UI/Front/Row/Top/01 Matrix/Button/Assn/1]]) → [Glide]([[Microfreak/UI/Front/Row/Middle/01 Glide Knob]]): +0.222.
		- [PRESSURE]([[Microfreak/UI/Front/Row/Bottom/06 Keyboard]]) → [Assign 2]([[Microfreak/UI/Front/Row/Top/01 Matrix/Button/Assn/2]]) → [LFO Rate]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate]]): +0.392.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/Top/02 Paraphonic Button]]) mode: off.
	- ## Customized controls
		- No factory preset is close. The nearest factory payload, [[Microfreak/Preset/313 Tremolo Saw]] (Factory 2.1 slot 60), differs in 25 controls.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
