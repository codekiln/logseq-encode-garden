logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 353
preset-synth-microfreak-name:: Work
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Custom]]
prev:: [[Microfreak/Preset/352 Lait]]
next:: [[Microfreak/Preset/354 Fjit]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/19 Scan Grains]]
preset-synth-microfreak-parameter-payload-sha256:: 42ac85227967b5aa3e66e3b90200ef9b24ff7d32783b4533771f4243e8528f68
preset-synth-file:: [Work — October 25 slot 353 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___353%20Work___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: bac9e4dc5d6305136e6276caa77903f8d61f0afcec9a674cfe0a30f6492b6fb2
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 353 over USB on October 25, 2026 with `mise run microfreak:download --slot 353`. Two consecutive reads returned the same file.
		- The parameter payload matches no MIDI Control Center factory archive.
		- [Download the slot 353 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___353%20Work___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/353 Work/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [Scan Grains]([[Microfreak/UI/Oscillator/Knob/Type/Scan Grains]]). [[Microfreak/UG/06 Dig Osc/03 Types/19 Scan Grains]]
		- [Scan]([[Microfreak/UI/Oscillator/Knob/Type/Scan Grains/Scan]]): 0.273. [Density]([[Microfreak/UI/Oscillator/Knob/Type/Scan Grains/Density]]): 0.207. [Chaos]([[Microfreak/UI/Oscillator/Knob/Type/Scan Grains/Chaos]]): 0.262.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/Bottom/01 Octave]]): 0. [Glide]([[Microfreak/UI/Front/Row/Middle/01 Glide Knob]]): 0.101.
	- ## Filter
		- [Low-pass]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Button/Type/LPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): 0.327; [resonance]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Resonance]]): 0.109. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Attack]]) 0.526, [decay/release]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Decay Rel]]) 0.401, [sustain]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Sustain]]) 0.560. [Amp Mod]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode]]): [Run]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode/Run]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise]]) 0.564, [RiseSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise/Shift]]) 0.500, [FallLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall]]) 0.311, [FallSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall/Shift]]) 0.500, [Hold]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Hold Sustain]]) 0.000, [Amount]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Amount]]) 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Sawtooth]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Button/Shape/Rising Sawtooth]]), clock [sync]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate/Press]]) off; stored normalized [rate]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate]]): 0.388. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [ENV]([[Microfreak/UI/Front/Row/Bottom/05 Envelope]]) → [Wave]([[Microfreak/UI/Oscillator/Knob/Wave]]): −0.244.
		- [ENV]([[Microfreak/UI/Front/Row/Bottom/05 Envelope]]) → [Timbre]([[Microfreak/UI/Oscillator/Knob/Timbre]]): −0.042.
		- [PRESSURE]([[Microfreak/UI/Front/Row/Bottom/06 Keyboard]]) → [Timbre]([[Microfreak/UI/Oscillator/Knob/Timbre]]): −0.274.
		- [ENV]([[Microfreak/UI/Front/Row/Bottom/05 Envelope]]) → [Cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): +0.118.
		- [LFO]([[Microfreak/UI/Front/Row/Bottom/04 LFO]]) → [Cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): +0.048.
		- [PRESSURE]([[Microfreak/UI/Front/Row/Bottom/06 Keyboard]]) → [Cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): +0.216.
		- [PRESSURE]([[Microfreak/UI/Front/Row/Bottom/06 Keyboard]]) → [Assign 1]([[Microfreak/UI/Front/Row/Top/01 Matrix/Button/Assn/1]]) → [Filter Resonance]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Resonance]]): +0.730.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/Top/02 Paraphonic Button]]) mode: on.
	- ## Customized controls
		- Compared with the nearest factory payload, [[Microfreak/Preset/247 Laity]] (Factory 3.0 slot 315); 12 controls differ.
		- [Oscillator type]([[Microfreak/UI/Oscillator/Knob/Type]]): Scan Grains (factory SawX).
		- [Glide]([[Microfreak/UI/Front/Row/Middle/01 Glide Knob]]): 0.101 (factory 0.000).
		- [Octave]([[Microfreak/UI/Front/Row/Bottom/01 Octave]]): 0 (factory +1).
		- [Cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): 0.327 (factory 0.409).
		- [Resonance]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Resonance]]): 0.109 (factory 0.000).
		- [Rise]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise]]): 0.564 (factory 0.167).
		- [Fall]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall]]): 0.311 (factory 0.163).
		- [Attack]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Attack]]): 0.526 (factory 0.000).
		- [LFO shape]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Button/Shape]]): Rising Sawtooth (factory Triangle).
		- [LFO sync]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate/Press]]): off (factory on).
		- [LFO rate]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate]]): 0.388 (factory 0.148).
		- [Arp/Seq rate]([[Microfreak/UI/Front/Row/Bottom/03 Arp Seq/Knob/Rate]]): 0.413 (factory 0.412).
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
