logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 395
preset-synth-microfreak-name:: 26.06.25
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Custom]]
prev:: [[Microfreak/Preset/394 Jing A]]
next:: [[Microfreak/Preset/396 Anit]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/04 Harmo]]
preset-synth-microfreak-parameter-payload-sha256:: c23364fc86a76fea6c544cf4c490acdd61eddb673e5da9c4cd1b83df6b631da5
preset-synth-file:: [26.06.25 — October 25 slot 395 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___395%2026.06.25___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 4904a76593e2f0004ce0b427faddf81638034ed2302e621dcbf38a0e54a71eaf
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 395 over USB on October 25, 2026 with `mise run microfreak:download --slot 395`. Two consecutive reads returned the same file.
		- The parameter payload matches no MIDI Control Center factory archive.
		- [Download the slot 395 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___395%2026.06.25___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/395 26.06.25/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [Harmo]([[Microfreak/UI/Oscillator/Knob/Type/Harmo]]). [[Microfreak/UG/06 Dig Osc/03 Types/04 Harmo]]
		- [Content]([[Microfreak/UI/Oscillator/Knob/Type/Harmo/Content]]): 0.379. [Sculpting]([[Microfreak/UI/Oscillator/Knob/Type/Harmo/Sculpting]]): 0.000. [Chorus]([[Microfreak/UI/Oscillator/Knob/Type/Harmo/Chorus]]): 0.314.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/Bottom/01 Octave]]): -1. [Glide]([[Microfreak/UI/Front/Row/Middle/01 Glide Knob]]): 0.000.
	- ## Filter
		- [Low-pass]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Button/Type/LPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): 0.870; [resonance]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Resonance]]): 0.452. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Attack]]) 0.196, [decay/release]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Decay Rel]]) 0.646, [sustain]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Sustain]]) 0.504. [Amp Mod]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode]]): [Loop]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode/Loop]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise]]) 0.276, [RiseSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise/Shift]]) 0.500, [FallLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall]]) 0.205, [FallSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall/Shift]]) 0.500, [Hold]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Hold Sustain]]) 0.208, [Amount]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Amount]]) 0.892. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Sine]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Button/Shape/Sine]]), clock [sync]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate/Press]]) on; stored division code: 3. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope]]) → Pitch: −0.005.
		- [LFO]([[Microfreak/UI/Front/Row/Bottom/04 LFO]]) → [Timbre]([[Microfreak/UI/Oscillator/Knob/Timbre]]): +0.700.
		- [ENV]([[Microfreak/UI/Front/Row/Bottom/05 Envelope]]) → [Cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): +0.195.
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope]]) → [Assign 1]([[Microfreak/UI/Front/Row/Top/01 Matrix/Button/Assn/1]]) → [Chorus]([[Microfreak/UI/Oscillator/Knob/Type/Harmo/Chorus]]): +0.873.
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope]]) → [Assign 2]([[Microfreak/UI/Front/Row/Top/01 Matrix/Button/Assn/2]]) → [Arp/Seq Rate]([[Microfreak/UI/Front/Row/Bottom/03 Arp Seq/Knob/Rate]]): +0.301.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/Top/02 Paraphonic Button]]) mode: on.
	- ## Customized controls
		- No factory preset is close. The nearest factory payload, [[Microfreak/Preset/135 No Sleep]] (Factory 2.0 slot 111), differs in 20 controls.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
