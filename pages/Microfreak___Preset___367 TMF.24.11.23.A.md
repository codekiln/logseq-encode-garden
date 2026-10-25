logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 367
preset-synth-microfreak-name:: TMF.24.11.23.A
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Custom]]
prev:: [[Microfreak/Preset/366 TMF.24.11.21.B]]
next:: [[Microfreak/Preset/368 TMF.24.11.23.B]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
preset-synth-microfreak-parameter-payload-sha256:: cd0c1893657f709da96b00642e7ac1cb7403518a46b5a768657c3ef8b457ae1b
preset-synth-file:: [TMF.24.11.23.A — October 25 slot 367 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___367%20TMF.24.11.23.A___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 4e9fbd4069f9d5447f7eb733b6709240212b4d97450cbba81f97f1390f30bdd1
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 367 over USB on October 25, 2026 with `mise run microfreak:download --slot 367`. Two consecutive reads returned the same file.
		- The parameter payload matches no MIDI Control Center factory archive.
		- [Download the slot 367 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___367%20TMF.24.11.23.A___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/367 TMF.24.11.23.A/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [SuperWave]([[Microfreak/UI/Oscillator/Knob/Type/SuperWave]]). [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
		- [Wave]([[Microfreak/UI/Oscillator/Knob/Type/SuperWave/Wave]]): 2 (stored choice code). [Detune]([[Microfreak/UI/Oscillator/Knob/Type/SuperWave/Detune]]): 0.500. [Volume]([[Microfreak/UI/Oscillator/Knob/Type/SuperWave/Volume]]): 0.500.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/Bottom/01 Octave]]): -1. [Glide]([[Microfreak/UI/Front/Row/Middle/01 Glide Knob]]): 0.000.
	- ## Filter
		- [Low-pass]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Button/Type/LPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): 1.000; [resonance]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Resonance]]): 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Attack]]) 0.300, [decay/release]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Decay Rel]]) 0.212, [sustain]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Sustain]]) 0.262. [Amp Mod]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode]]): [Run]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode/Run]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise]]) 0.163, [RiseSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise/Shift]]) 0.500, [FallLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall]]) 0.163, [FallSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall/Shift]]) 0.500, [Hold]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Hold Sustain]]) 0.000, [Amount]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Amount]]) 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Sine]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Button/Shape/Sine]]), clock [sync]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate/Press]]) on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- All saved matrix [amounts]([[Microfreak/UI/Front/Row/Top/01 Matrix/Knob]]) are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/Top/02 Paraphonic Button]]) mode: off.
	- ## Customized controls
		- Compared with the nearest factory payload, [[Microfreak/Preset/304 Saw Vox]] (Factory 2.1 slot 51); 6 controls differ.
		- [Oscillator type]([[Microfreak/UI/Oscillator/Knob/Type]]): SuperWave (factory Vocoder).
		- [Octave]([[Microfreak/UI/Front/Row/Bottom/01 Octave]]): -1 (factory 0).
		- [Attack]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Attack]]): 0.300 (factory 0.000).
		- [Decay/Release]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Decay Rel]]): 0.212 (factory 0.259).
		- [Sustain]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Sustain]]): 0.262 (factory 1.000).
		- [Paraphonic]([[Microfreak/UI/Front/Row/Top/02 Paraphonic Button]]): off (factory on).
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
