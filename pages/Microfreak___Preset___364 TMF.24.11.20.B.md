logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 364
preset-synth-microfreak-name:: TMF.24.11.20.B
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Custom]]
prev:: [[Microfreak/Preset/363 TMF.24.11.20.A]]
next:: [[Microfreak/Preset/365 TMF.24.11.21.A]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
preset-synth-microfreak-parameter-payload-sha256:: bc14c217bf2052397e1be851b1510425c425dc3c0df95ec70d163591fe7bb970
preset-synth-file:: [TMF.24.11.20.B — October 25 slot 364 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___364%20TMF.24.11.20.B___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 00789f209b73c0dbfd2493b80d08d4390cc7d2312884284539f2bbd30b46778c
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 364 over USB on October 25, 2026 with `mise run microfreak:download --slot 364`. Two consecutive reads returned the same file.
		- The parameter payload matches no MIDI Control Center factory archive.
		- [Download the slot 364 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___364%20TMF.24.11.20.B___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/364 TMF.24.11.20.B/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [BasicWaves]([[Microfreak/UI/Oscillator/Knob/Type/BasicWaves]]). [[Microfreak/UG/06 Dig Osc/03 Types/01 BasicWaves]]
		- [Morph]([[Microfreak/UI/Oscillator/Knob/Type/BasicWaves/Morph]]): 0.664. [Sym]([[Microfreak/UI/Oscillator/Knob/Type/BasicWaves/Sym]]): 0.055. [Sub]([[Microfreak/UI/Oscillator/Knob/Type/BasicWaves/Sub]]): 0.398.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/Bottom/01 Octave]]): -1. [Glide]([[Microfreak/UI/Front/Row/Middle/01 Glide Knob]]): 0.234.
	- ## Filter
		- [High-pass]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Button/Type/HPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): 0.776; [resonance]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Resonance]]): 0.429. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Attack]]) 0.501, [decay/release]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Decay Rel]]) 0.660, [sustain]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Sustain]]) 0.489. [Amp Mod]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode]]): [Run]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode/Run]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise]]) 0.332, [RiseSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise/Shift]]) 0.500, [FallLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall]]) 0.228, [FallSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall/Shift]]) 0.500, [Hold]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Hold Sustain]]) 0.357, [Amount]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Amount]]) 0.879. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Sawtooth]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Button/Shape/Rising Sawtooth]]), clock [sync]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate/Press]]) on; stored division code: 7. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [LFO]([[Microfreak/UI/Front/Row/Bottom/04 LFO]]) → [Timbre]([[Microfreak/UI/Oscillator/Knob/Timbre]]): +0.751.
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope]]) → [Cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): −0.591.
		- [ENV]([[Microfreak/UI/Front/Row/Bottom/05 Envelope]]) → [Cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): −0.953.
		- [LFO]([[Microfreak/UI/Front/Row/Bottom/04 LFO]]) → [Assign 1]([[Microfreak/UI/Front/Row/Top/01 Matrix/Button/Assn/1]]) → [Cycling Envelope Rise]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise]]): +0.862.
		- [KEY/ARP]([[Microfreak/UI/Front/Row/Bottom/06 Keyboard]]) → [Assign 2]([[Microfreak/UI/Front/Row/Top/01 Matrix/Button/Assn/2]]) → [Cycling Envelope Amount]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Amount]]): −0.228.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/Top/02 Paraphonic Button]]) mode: on.
	- ## Customized controls
		- No factory preset is close. The nearest factory payload, “SubOscTemplate” (Factory 1.1 slot 236), differs in 22 controls.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
