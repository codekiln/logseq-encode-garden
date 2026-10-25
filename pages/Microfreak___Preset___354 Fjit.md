logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 354
preset-synth-microfreak-name:: Fjit
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Custom]]
prev:: [[Microfreak/Preset/353 Work]]
next:: [[Microfreak/Preset/355 PersnikT]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/20 Cloud Grains]]
preset-synth-microfreak-parameter-payload-sha256:: 14f11c3b98d53c99545447340f68a2e3f63e53b7d8a9703bd268e184b9aacd33
preset-synth-file:: [Fjit — October 25 slot 354 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___354%20Fjit___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 21bef2aad81360c70309bc5fdd287ad1c4cde09dae311627948b278ebfd92e32
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 354 over USB on October 25, 2026 with `mise run microfreak:download --slot 354`. Two consecutive reads returned the same file.
		- The parameter payload matches no MIDI Control Center factory archive.
		- [Download the slot 354 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___354%20Fjit___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/354 Fjit/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [Cloud Grains]([[Microfreak/UI/Oscillator/Knob/Type/Cloud Grains]]). [[Microfreak/UG/06 Dig Osc/03 Types/20 Cloud Grains]]
		- [Starts]([[Microfreak/UI/Oscillator/Knob/Type/Cloud Grains/Starts]]): 0.539. [Density]([[Microfreak/UI/Oscillator/Knob/Type/Cloud Grains/Density]]): 0.336. [Chaos]([[Microfreak/UI/Oscillator/Knob/Type/Cloud Grains/Chaos]]): 0.156.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/Bottom/01 Octave]]): 0. [Glide]([[Microfreak/UI/Front/Row/Middle/01 Glide Knob]]): 0.205.
	- ## Filter
		- [Low-pass]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Button/Type/LPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): 0.314; [resonance]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Resonance]]): 0.087. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Attack]]) 0.890, [decay/release]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Decay Rel]]) 0.676, [sustain]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Sustain]]) 0.375. [Amp Mod]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode]]): [Run]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode/Run]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise]]) 0.000, [RiseSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise/Shift]]) 0.500, [FallLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall]]) 0.000, [FallSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall/Shift]]) 0.500, [Hold]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Hold Sustain]]) 0.988, [Amount]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Amount]]) 0.548. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Triangle]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Button/Shape/Triangle]]), clock [sync]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate/Press]]) off; stored normalized [rate]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate]]): 0.387. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [ENV]([[Microfreak/UI/Front/Row/Bottom/05 Envelope]]) → [Wave]([[Microfreak/UI/Oscillator/Knob/Wave]]): −0.244.
		- [ENV]([[Microfreak/UI/Front/Row/Bottom/05 Envelope]]) → [Timbre]([[Microfreak/UI/Oscillator/Knob/Timbre]]): −0.042.
		- [PRESSURE]([[Microfreak/UI/Front/Row/Bottom/06 Keyboard]]) → [Timbre]([[Microfreak/UI/Oscillator/Knob/Timbre]]): −0.274.
		- [ENV]([[Microfreak/UI/Front/Row/Bottom/05 Envelope]]) → [Cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): +0.635.
		- [LFO]([[Microfreak/UI/Front/Row/Bottom/04 LFO]]) → [Cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): +0.048.
		- [PRESSURE]([[Microfreak/UI/Front/Row/Bottom/06 Keyboard]]) → [Cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): +0.216.
		- [PRESSURE]([[Microfreak/UI/Front/Row/Bottom/06 Keyboard]]) → [Assign 1]([[Microfreak/UI/Front/Row/Top/01 Matrix/Button/Assn/1]]) → [Filter Resonance]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Resonance]]): +0.730.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/Top/02 Paraphonic Button]]) mode: off.
	- ## Customized controls
		- No factory preset is close. The nearest factory payload, [[Microfreak/Preset/247 Laity]] (Factory 3.0 slot 315), differs in 17 controls.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
