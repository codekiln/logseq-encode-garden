logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 355
preset-synth-microfreak-name:: PersnikT
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Custom]]
prev:: [[Microfreak/Preset/354 Fjit]]
next:: [[Microfreak/Preset/356 Ridiance]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/20 Cloud Grains]]
preset-synth-microfreak-parameter-payload-sha256:: 3cda515cddeb25f9101af9a2a284ae728b65e7da1f53dd9ce3d2a4b4abf116b0
preset-synth-file:: [PersnikT — October 25 slot 355 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___355%20PersnikT___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: e65c9bd02612b6afa44a058fe9b9ca7bb5f2af22c78ee1759033ddc5856d734e
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 355 over USB on October 25, 2026 with `mise run microfreak:download --slot 355`. Two consecutive reads returned the same file.
		- The parameter payload matches no MIDI Control Center factory archive.
		- [Download the slot 355 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___355%20PersnikT___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/355 PersnikT/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [Cloud Grains]([[Microfreak/UI/Oscillator/Knob/Type/Cloud Grains]]). [[Microfreak/UG/06 Dig Osc/03 Types/20 Cloud Grains]]
		- [Starts]([[Microfreak/UI/Oscillator/Knob/Type/Cloud Grains/Starts]]): 0.108. [Density]([[Microfreak/UI/Oscillator/Knob/Type/Cloud Grains/Density]]): 0.461. [Chaos]([[Microfreak/UI/Oscillator/Knob/Type/Cloud Grains/Chaos]]): 0.664.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/03 Bottom/01 Octave]]): -1. [Glide]([[Microfreak/UI/Front/Row/02 Main/01 Glide Knob]]): 0.000.
	- ## Filter
		- [Low-pass]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Button/Type/LPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): 0.593; [resonance]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Resonance]]): 0.916. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Attack]]) 0.316, [decay/release]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Decay Rel]]) 0.259, [sustain]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Sustain]]) 1.000. [Amp Mod]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode]]): [Run]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode/Run]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise]]) 0.462, [RiseSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise/Shift]]) 0.500, [FallLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall]]) 0.288, [FallSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall/Shift]]) 0.500, [Hold]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Hold Sustain]]) 0.000, [Amount]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Amount]]) 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Sample-and-Hold Filtered]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Button/Shape/Random Gliding]]), clock [sync]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Knob/Rate/Press]]) on; stored division code: 8. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [PRESSURE]([[Microfreak/UI/Front/Row/05 Keys]]) → [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): +0.053.
		- [LFO]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO]]) → [Assign 1]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/1]]) → [Density]([[Microfreak/UI/Oscillator/Knob/Type/Cloud Grains/Density]]): +0.678.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/01 Top/02 Paraphonic Button]]) mode: off.
	- ## Customized controls
		- Compared with the nearest factory payload, [[Microfreak/Preset/309 Low Noisy Vox]] (Factory 2.1 slot 56); 11 controls differ.
		- [Oscillator type]([[Microfreak/UI/Oscillator/Knob/Type]]): Cloud Grains (factory Vocoder).
		- [Octave]([[Microfreak/UI/Front/Row/03 Bottom/01 Octave]]): -1 (factory 0).
		- [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): 0.593 (factory 1.000).
		- [Resonance]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Resonance]]): 0.916 (factory 0.607).
		- [Rise]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise]]): 0.462 (factory 0.163).
		- [Fall]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall]]): 0.288 (factory 0.163).
		- [Attack]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Attack]]): 0.316 (factory 0.000).
		- [LFO shape]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Button/Shape]]): Random Gliding (factory Sine).
		- [Matrix]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Knob]]) PRESSURE → Cutoff: +0.053 (factory −0.367).
		- [Matrix]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Knob]]) LFO → Assign 1: +0.678 (factory +0.000).
		- [Assign 1]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/1]]) destination: [Density]([[Microfreak/UI/Oscillator/Knob/Type/Cloud Grains/Density]]) (factory [Shape]([[Microfreak/UI/Oscillator/Knob/Type/Vocoder/Shape]])).
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
