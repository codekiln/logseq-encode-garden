logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 401
preset-synth-microfreak-name:: Init
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Custom]]
prev:: [[Microfreak/Preset/400 Init]]
next:: [[Microfreak/Preset/402 Init]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/04 Harmo]]
preset-synth-microfreak-parameter-payload-sha256:: 120f247c3137b031cc96bfc653c7527eb76008f58b6cd4fdf3b1be2e7849654e
preset-synth-file:: [Init — October 25 slot 401 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___401%20Init___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: d08d563d245a4922f388bbfbf508f5ab23db1a44deba91ed139d2ee9afbae80f
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 401 over USB on October 25, 2026 with `mise run microfreak:download --slot 401`. Two consecutive reads returned the same file.
		- The parameter payload matches no MIDI Control Center factory archive.
		- [Download the slot 401 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___401%20Init___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/401 Init/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [Harmo]([[Microfreak/UI/Oscillator/Knob/Type/Harmo]]). [[Microfreak/UG/06 Dig Osc/03 Types/04 Harmo]]
		- [Content]([[Microfreak/UI/Oscillator/Knob/Type/Harmo/Content]]): 0.426. [Sculpting]([[Microfreak/UI/Oscillator/Knob/Type/Harmo/Sculpting]]): 0.551. [Chorus]([[Microfreak/UI/Oscillator/Knob/Type/Harmo/Chorus]]): 0.340.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/03 Bottom/01 Octave]]): -1. [Glide]([[Microfreak/UI/Front/Row/02 Main/01 Glide Knob]]): 0.000.
	- ## Filter
		- [Band-pass]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Button/Type/BPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): 0.522; [resonance]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Resonance]]): 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/02 Band Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Attack]]) 0.224, [decay/release]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Decay Rel]]) 0.259, [sustain]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Sustain]]) 1.000. [Amp Mod]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode]]): [Run]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode/Run]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise]]) 0.216, [RiseSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise/Shift]]) 0.500, [FallLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall]]) 0.163, [FallSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall/Shift]]) 0.500, [Hold]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Hold Sustain]]) 0.000, [Amount]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Amount]]) 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Triangle]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Button/Shape/Triangle]]), clock [sync]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Knob/Rate/Press]]) on; stored division code: 4. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [LFO]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO]]) → [Wave]([[Microfreak/UI/Oscillator/Knob/Wave]]): +0.104.
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope]]) → [Timbre]([[Microfreak/UI/Oscillator/Knob/Timbre]]): +0.229.
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope]]) → [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): −0.025.
		- [ENV]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope]]) → [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): +0.082.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/01 Top/02 Paraphonic Button]]) mode: on.
	- ## Customized controls
		- Compared with the nearest factory payload, [[Microfreak/Preset/304 Saw Vox]] (Factory 2.1 slot 51); 12 controls differ.
		- [Oscillator type]([[Microfreak/UI/Oscillator/Knob/Type]]): Harmo (factory Vocoder).
		- [Octave]([[Microfreak/UI/Front/Row/03 Bottom/01 Octave]]): -1 (factory 0).
		- [Filter type]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Button/Type]]): BPF (factory LPF).
		- [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): 0.522 (factory 1.000).
		- [Rise]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise]]): 0.216 (factory 0.163).
		- [Attack]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Attack]]): 0.224 (factory 0.000).
		- [LFO shape]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Button/Shape]]): Triangle (factory Sine).
		- [Arp]([[Microfreak/UI/Front/Row/03 Bottom/03 Arp Seq/Button/Arp Seq/Arp]]): on (factory off).
		- [Matrix]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Knob]]) LFO → Wave: +0.104 (factory +0.000).
		- [Matrix]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Knob]]) Cycling Envelope → Timbre: +0.229 (factory +0.000).
		- [Matrix]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Knob]]) Cycling Envelope → Cutoff: −0.025 (factory +0.000).
		- [Matrix]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Knob]]) ENV → Cutoff: +0.082 (factory +0.000).
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
