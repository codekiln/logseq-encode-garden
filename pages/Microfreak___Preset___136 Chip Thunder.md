logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 136
preset-synth-microfreak-name:: Chip Thunder
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/135 No Sleep]]
next:: [[Microfreak/Preset/137 Solide]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
preset-synth-microfreak-parameter-payload-sha256:: 63c3d008729b0e1c56d60b17d4b61dacce15c0c6ae9555b4cf2640507d2a9126
preset-synth-file:: [Chip Thunder — October 25 slot 136 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___136%20Chip%20Thunder___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: fec270a520652b9ac69203308d28d7d3cf5122dfd3b351d821146ea1072c1c99
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 136 over USB on October 25, 2026 with `mise run microfreak:download --slot 136`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0 (Factory 2.0 slot 112, Factory 2.1 slot 214, Factory 3.0 slot 214). Comparison used `mise run microfreak:compare`.
		- [Download the slot 136 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___136%20Chip%20Thunder___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/136 Chip Thunder/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [Noise]([[Microfreak/UI/Oscillator/Knob/Type/Noise]]). [[Microfreak/UG/06 Dig Osc/03 Types/13 Noise]]
		- [Wave]([[Microfreak/UI/Oscillator/Knob/Type/Noise/Wave]]): 0.289. [Timbre]([[Microfreak/UI/Oscillator/Knob/Type/Noise/Timbre]]): 0.375. [Shape]([[Microfreak/UI/Oscillator/Knob/Type/Noise/Shape]]): 0.000.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/03 Bottom/01 Octave]]): -1. [Glide]([[Microfreak/UI/Front/Row/02 Main/01 Glide Knob]]): 0.000.
	- ## Filter
		- [Low-pass]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Button/Type/LPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): 0.144; [resonance]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Resonance]]): 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Attack]]) 0.000, [decay/release]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Decay Rel]]) 0.885, [sustain]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Sustain]]) 0.119. [Amp Mod]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode]]): [Env]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode/Env]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise]]) 0.002, [RiseSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise/Shift]]) 0.500, [FallLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall]]) 0.477, [FallSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall/Shift]]) 0.177, [Hold]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Hold Sustain]]) 0.000, [Amount]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Amount]]) 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Sine]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Button/Shape/Sine]]), clock [sync]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Knob/Rate/Press]]) on; stored division code: 46877. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope]]) → [Timbre]([[Microfreak/UI/Oscillator/Knob/Timbre]]): +0.554.
		- [KEY/ARP]([[Microfreak/UI/Front/Row/05 Keys]]) → [Timbre]([[Microfreak/UI/Oscillator/Knob/Timbre]]): +1.000.
		- [ENV]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope]]) → [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): +1.000.
		- [ENV]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope]]) → [Assign 1]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/1]]) → [Decay/Release]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Decay Rel]]): −0.225.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/01 Top/02 Paraphonic Button]]) mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
