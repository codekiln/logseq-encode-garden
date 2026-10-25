logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 388
preset-synth-microfreak-name:: Anit1
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Custom]]
prev:: [[Microfreak/Preset/387 Enit]]
next:: [[Microfreak/Preset/389 Bnit2]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
preset-synth-microfreak-parameter-payload-sha256:: ecce34ad034e11bc8c93534fb2e6d4464bf230a4d5aee45d5b2e2ea97b8feb30
preset-synth-file:: [Anit1 — October 25 slot 388 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___388%20Anit1___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: fcc39832d43f5f17cffa374a57229305aa0ed024fd56a8660567d3bc8991c1b4
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 388 over USB on October 25, 2026 with `mise run microfreak:download --slot 388`. Two consecutive reads returned the same file.
		- The parameter payload matches no MIDI Control Center factory archive.
		- [Download the slot 388 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___388%20Anit1___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/388 Anit1/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [Two Op. FM]([[Microfreak/UI/Oscillator/Knob/Type/Two Op.FM]]). [[Microfreak/UG/06 Dig Osc/03 Types/08 Two Op.FM]]
		- [Ratio]([[Microfreak/UI/Oscillator/Knob/Type/Two Op.FM/Ratio]]): 0.306. [Amount]([[Microfreak/UI/Oscillator/Knob/Type/Two Op.FM/Amount]]): 0.486. [Shape]([[Microfreak/UI/Oscillator/Knob/Type/Two Op.FM/Shape]]): 0.000.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/Bottom/01 Octave]]): -1. [Glide]([[Microfreak/UI/Front/Row/Middle/01 Glide Knob]]): 0.197.
	- ## Filter
		- [Low-pass]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Button/Type/LPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): 0.522; [resonance]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Resonance]]): 0.489. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Attack]]) 0.326, [decay/release]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Decay Rel]]) 0.283, [sustain]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Sustain]]) 0.320. [Amp Mod]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode]]): [Env]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode/Env]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise]]) 0.316, [RiseSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise/Shift]]) 1.000, [FallLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall]]) 0.435, [FallSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall/Shift]]) 0.000, [Hold]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Hold Sustain]]) 0.520, [Amount]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Amount]]) 0.480. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Sine]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Button/Shape/Sine]]), clock [sync]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate/Press]]) on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope]]) → Pitch: −0.929.
		- [ENV]([[Microfreak/UI/Front/Row/Bottom/05 Envelope]]) → [Cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): +0.133.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/Top/02 Paraphonic Button]]) mode: on.
	- ## Customized controls
		- No factory preset is close. The nearest factory payload, [[Microfreak/Preset/122 Simon Says]] (Factory 2.0 slot 10), differs in 18 controls.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
