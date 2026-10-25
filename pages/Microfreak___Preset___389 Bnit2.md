logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 389
preset-synth-microfreak-name:: Bnit2
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Custom]]
prev:: [[Microfreak/Preset/388 Anit1]]
next:: [[Microfreak/Preset/390 Cnit2]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
preset-synth-microfreak-parameter-payload-sha256:: 424cedb1b85c2cc5900f5426e3f379df0be9341f2b3994dbb0ea0b5a128a997c
preset-synth-file:: [Bnit2 — October 25 slot 389 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___389%20Bnit2___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 83c08449cb1a08dd12241558025ab7ab07d75d2ee9e60987ae386d6e3ac6f54c
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 389 over USB on October 25, 2026 with `mise run microfreak:download --slot 389`. Two consecutive reads returned the same file.
		- The parameter payload matches no MIDI Control Center factory archive.
		- [Download the slot 389 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___389%20Bnit2___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/389 Bnit2/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [Two Op. FM]([[Microfreak/UI/Oscillator/Knob/Type/Two Op.FM]]). [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
		- [Ratio]([[Microfreak/UI/Oscillator/Knob/Type/Two Op.FM/Ratio]]): 0.298. [Amount]([[Microfreak/UI/Oscillator/Knob/Type/Two Op.FM/Amount]]): 0.486. [Shape]([[Microfreak/UI/Oscillator/Knob/Type/Two Op.FM/Shape]]): 0.000.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/Bottom/01 Octave]]): +1. [Glide]([[Microfreak/UI/Front/Row/Middle/01 Glide Knob]]): 0.048.
	- ## Filter
		- [Low-pass]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Button/Type/LPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): 1.000; [resonance]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Resonance]]): 0.583. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Attack]]) 0.284, [decay/release]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Decay Rel]]) 0.283, [sustain]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Sustain]]) 0.320. [Amp Mod]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode]]): [Env]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode/Env]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise]]) 0.231, [RiseSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise/Shift]]) 0.500, [FallLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall]]) 0.238, [FallSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall/Shift]]) 0.500, [Hold]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Hold Sustain]]) 0.394, [Amount]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Amount]]) 0.477. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Triangle]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Button/Shape/Triangle]]), clock [sync]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate/Press]]) on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope]]) → Pitch: +0.040.
		- [ENV]([[Microfreak/UI/Front/Row/Bottom/05 Envelope]]) → [Cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): +0.080.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/Top/02 Paraphonic Button]]) mode: on.
	- ## Customized controls
		- No factory preset is close. The nearest factory payload, [[Microfreak/Preset/125 Amigras]] (Factory 2.0 slot 102), differs in 16 controls.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
