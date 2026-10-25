logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 394
preset-synth-microfreak-name:: Jing A
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Custom]]
prev:: [[Microfreak/Preset/393 answ er]]
next:: [[Microfreak/Preset/395 26.06.25]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
preset-synth-microfreak-parameter-payload-sha256:: 2ccb2fd485c65dcc003fa434b9577cdcdb3c557a0ae340f835158e135cac86d7
preset-synth-file:: [Jing A — October 25 slot 394 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___394%20Jing%20A___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: abfc0bc6faafac92b900b079f448b648b2acac7770258212847cc98cda9865b7
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 394 over USB on October 25, 2026 with `mise run microfreak:download --slot 394`. Two consecutive reads returned the same file.
		- The parameter payload matches no MIDI Control Center factory archive.
		- [Download the slot 394 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___394%20Jing%20A___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/394 Jing A/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [Wavetable]([[Microfreak/UI/Oscillator/Knob/Type/Wavetable]]). [[Microfreak/UG/06 Dig Osc/03 Types/03 Wavetable]]
		- [Table]([[Microfreak/UI/Oscillator/Knob/Type/Wavetable/Table]]): 0 (stored choice code). [Position]([[Microfreak/UI/Oscillator/Knob/Type/Wavetable/Position]]): 0.000. [Chorus]([[Microfreak/UI/Oscillator/Knob/Type/Wavetable/Chorus]]): 1.000.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/03 Bottom/01 Octave]]): -2. [Glide]([[Microfreak/UI/Front/Row/02 Main/01 Glide Knob]]): 0.000.
	- ## Filter
		- [Low-pass]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Button/Type/LPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): 1.000; [resonance]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Resonance]]): 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Attack]]) 0.000, [decay/release]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Decay Rel]]) 0.259, [sustain]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Sustain]]) 1.000. [Amp Mod]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode]]): [Loop]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode/Loop]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise]]) 0.425, [RiseSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise/Shift]]) 0.500, [FallLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall]]) 0.606, [FallSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall/Shift]]) 0.500, [Hold]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Hold Sustain]]) 0.734, [Amount]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Amount]]) 0.690. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Sine]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Button/Shape/Sine]]), clock [sync]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Knob/Rate/Press]]) on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope]]) → [Assign 1]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/1]]) → [Chorus]([[Microfreak/UI/Oscillator/Knob/Type/Wavetable/Chorus]]): −0.951.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/01 Top/02 Paraphonic Button]]) mode: off.
	- ## Customized controls
		- Compared with the nearest factory payload, [[Microfreak/Preset/304 Saw Vox]] (Factory 2.1 slot 51); 11 controls differ.
		- [Oscillator type]([[Microfreak/UI/Oscillator/Knob/Type]]): Wavetable (factory Vocoder).
		- [Octave]([[Microfreak/UI/Front/Row/03 Bottom/01 Octave]]): -2 (factory 0).
		- [Cycling Envelope mode]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode]]): Loop (factory Run).
		- [Rise]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise]]): 0.425 (factory 0.163).
		- [Fall]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall]]): 0.606 (factory 0.163).
		- [Hold/Sustain]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Hold Sustain]]): 0.734 (factory 0.000).
		- [Cycling Envelope amount]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Amount]]): 0.690 (factory 1.000).
		- [Paraphonic]([[Microfreak/UI/Front/Row/01 Top/02 Paraphonic Button]]): off (factory on).
		- [Seq]([[Microfreak/UI/Front/Row/03 Bottom/03 Arp Seq/Button/Arp Seq/Seq]]): on (factory off).
		- [Arp/Seq rate]([[Microfreak/UI/Front/Row/03 Bottom/03 Arp Seq/Knob/Rate]]): 0.414 (factory 0.412).
		- [Matrix]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Knob]]) Cycling Envelope → Assign 1: −0.951 (factory +0.000).
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
