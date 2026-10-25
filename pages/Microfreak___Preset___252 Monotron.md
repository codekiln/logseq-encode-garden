logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 252
preset-synth-microfreak-name:: Monotron
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/251 Trinity]]
next:: [[Microfreak/Preset/253 Carrytron]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
preset-synth-microfreak-parameter-payload-sha256:: 65d1fd64220d65dfd7cb0b6a2895b03427965a509becb0e2b6c99cfc7ff238fc
preset-synth-file:: [Monotron — October 25 slot 252 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___252%20Monotron___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 7cfb1539166288336d5891bb96043bdab345c75c09f8b2d9c8bdd1d257dde983
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 252 over USB on October 25, 2026 with `mise run microfreak:download --slot 252`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 32, Factory 6.0 slot None). Comparison used `mise run microfreak:compare`.
		- [Download the slot 252 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___252%20Monotron___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/252 Monotron/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [SawX]([[Microfreak/UI/Oscillator/Knob/Type/SAWX]]). [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
		- [Saw Mod]([[Microfreak/UI/Oscillator/Knob/Type/SAWX/Saw Mod]]): 0.000. [Shape]([[Microfreak/UI/Oscillator/Knob/Type/SAWX/Shape]]): 0.000. [Noise]([[Microfreak/UI/Oscillator/Knob/Type/SAWX/Noise]]): 0.000.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/03 Bottom/01 Octave]]): -1. [Glide]([[Microfreak/UI/Front/Row/02 Main/01 Glide Knob]]): 0.000.
	- ## Filter
		- [Low-pass]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Button/Type/LPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): 0.102; [resonance]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Resonance]]): 0.499. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Attack]]) 0.000, [decay/release]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Decay Rel]]) 0.365, [sustain]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Sustain]]) 0.203. [Amp Mod]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode]]): [Env]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode/Env]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise]]) 0.046, [RiseSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise/Shift]]) 0.872, [FallLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall]]) 0.228, [FallSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall/Shift]]) 0.500, [Hold]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Hold Sustain]]) 0.000, [Amount]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Amount]]) 0.152. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Sine]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Button/Shape/Sine]]), clock [sync]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Knob/Rate/Press]]) on; stored division code: 3. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [PRESSURE]([[Microfreak/UI/Front/Row/05 Keys]]) → Pitch: +0.205.
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope]]) → [Wave]([[Microfreak/UI/Oscillator/Knob/Wave]]): +0.537.
		- [PRESSURE]([[Microfreak/UI/Front/Row/05 Keys]]) → [Wave]([[Microfreak/UI/Oscillator/Knob/Wave]]): +0.178.
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope]]) → [Timbre]([[Microfreak/UI/Oscillator/Knob/Timbre]]): +1.000.
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope]]) → [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): +0.564.
		- [ENV]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope]]) → [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): +0.310.
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope]]) → [Assign 3]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/3]]) → [Decay/Release]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Decay Rel]]): −0.238.
		- [PRESSURE]([[Microfreak/UI/Front/Row/05 Keys]]) → [Assign 3]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/3]]) → [Decay/Release]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Decay Rel]]): +0.056.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/01 Top/02 Paraphonic Button]]) mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
