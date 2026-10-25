logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 291
preset-synth-microfreak-name:: Poisoned 0scs
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/290 Qrazy Press]]
next:: [[Microfreak/Preset/292 Moving Cars]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: 1f57eced4686d725ab53c7207605bec00235d559808a96f3bea14774aaa6a15e
preset-synth-file:: [Poisoned 0scs — October 25 slot 291 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___291%20Poisoned%200scs___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: bbc91862cd9c10fcfe0e2640d6a03e34af9ea02ba4f53ad889604edb67f2df1a
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 291 over USB on October 25, 2026 with `mise run microfreak:download --slot 291`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 355, Factory 6.0 slot 141). Comparison used `mise run microfreak:compare`.
		- [Download the slot 291 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___291%20Poisoned%200scs___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/291 Poisoned 0scs/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [Harm]([[Microfreak/UI/Oscillator/Knob/Type/HARM]]). [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- [Spread]([[Microfreak/UI/Oscillator/Knob/Type/HARM/Spread]]): 0.177. [Rectification]([[Microfreak/UI/Oscillator/Knob/Type/HARM/Rectification]]): 0.000. [Noise]([[Microfreak/UI/Oscillator/Knob/Type/HARM/Noise]]): 0.488.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/03 Bottom/01 Octave]]): 0. [Glide]([[Microfreak/UI/Front/Row/02 Main/01 Glide Knob]]): 0.000.
	- ## Filter
		- [Low-pass]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Button/Type/LPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): 0.169; [resonance]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Resonance]]): 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Attack]]) 0.000, [decay/release]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Decay Rel]]) 0.257, [sustain]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Sustain]]) 0.405. [Amp Mod]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode]]): [Loop]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode/Loop]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise]]) 0.647, [RiseSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise/Shift]]) 0.000, [FallLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall]]) 1.000, [FallSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall/Shift]]) 1.000, [Hold]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Hold Sustain]]) 0.000, [Amount]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Amount]]) 0.242. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Sample-and-Hold]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Button/Shape/Random Stepped]]), clock [sync]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Knob/Rate/Press]]) off; stored normalized [rate]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Knob/Rate]]): 0.999. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope]]) → Pitch: +0.005.
		- [KEY/ARP]([[Microfreak/UI/Front/Row/05 Keys]]) → Pitch: −0.001.
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope]]) → [Wave]([[Microfreak/UI/Oscillator/Knob/Wave]]): −0.331.
		- [LFO]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO]]) → [Wave]([[Microfreak/UI/Oscillator/Knob/Wave]]): +0.188.
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope]]) → [Timbre]([[Microfreak/UI/Oscillator/Knob/Timbre]]): −1.000.
		- [LFO]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO]]) → [Timbre]([[Microfreak/UI/Oscillator/Knob/Timbre]]): +0.727.
		- [KEY/ARP]([[Microfreak/UI/Front/Row/05 Keys]]) → [Timbre]([[Microfreak/UI/Oscillator/Knob/Timbre]]): +1.000.
		- [ENV]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope]]) → [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): +0.585.
		- [PRESSURE]([[Microfreak/UI/Front/Row/05 Keys]]) → [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): +0.360.
		- [KEY/ARP]([[Microfreak/UI/Front/Row/05 Keys]]) → [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): +0.605.
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope]]) → [Assign 1]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/1]]) → [LFO Rate]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Knob/Rate]]): −1.000.
		- [LFO]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO]]) → [Assign 1]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/1]]) → [LFO Rate]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Knob/Rate]]): +0.379.
		- [KEY/ARP]([[Microfreak/UI/Front/Row/05 Keys]]) → [Assign 1]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/1]]) → [LFO Rate]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Knob/Rate]]): +1.000.
		- [LFO]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO]]) → [Assign 2]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/2]]) → [Cycling Envelope Amount]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Amount]]): +0.410.
		- [LFO]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO]]) → [Assign 3]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/3]]) → [Cycling Envelope Fall]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall]]): +0.302.
		- [KEY/ARP]([[Microfreak/UI/Front/Row/05 Keys]]) → [Assign 3]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/3]]) → [Cycling Envelope Fall]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall]]): +0.014.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/01 Top/02 Paraphonic Button]]) mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
