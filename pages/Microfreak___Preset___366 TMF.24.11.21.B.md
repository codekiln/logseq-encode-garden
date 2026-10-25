logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 366
preset-synth-microfreak-name:: TMF.24.11.21.B
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Custom]]
prev:: [[Microfreak/Preset/365 TMF.24.11.21.A]]
next:: [[Microfreak/Preset/367 TMF.24.11.23.A]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
preset-synth-microfreak-parameter-payload-sha256:: 39a785c4a72879203ced446ad5736c95cef8755dfc560aa37babecb09aacdfa9
preset-synth-file:: [TMF.24.11.21.B — October 25 slot 366 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___366%20TMF.24.11.21.B___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 4cfb158d80647c2589324d927953bf4ab92db3351727136d3846eb704f70e9c4
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 366 over USB on October 25, 2026 with `mise run microfreak:download --slot 366`. Two consecutive reads returned the same file.
		- The parameter payload matches no MIDI Control Center factory archive.
		- [Download the slot 366 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___366%20TMF.24.11.21.B___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/366 TMF.24.11.21.B/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [SuperWave]([[Microfreak/UI/Oscillator/Knob/Type/SuperWave]]). [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
		- [Wave]([[Microfreak/UI/Oscillator/Knob/Type/SuperWave/Wave]]): 2 (stored choice code). [Detune]([[Microfreak/UI/Oscillator/Knob/Type/SuperWave/Detune]]): 0.000. [Volume]([[Microfreak/UI/Oscillator/Knob/Type/SuperWave/Volume]]): 0.000.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/Bottom/01 Octave]]): -2. [Glide]([[Microfreak/UI/Front/Row/Middle/01 Glide Knob]]): 0.000.
	- ## Filter
		- [Low-pass]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Button/Type/LPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): 0.779; [resonance]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Resonance]]): 0.207. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Attack]]) 0.000, [decay/release]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Decay Rel]]) 0.499, [sustain]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Sustain]]) 0.700. [Amp Mod]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode]]): [Run]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Button/Mode/Run]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise]]) 0.113, [RiseSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Rise/Shift]]) 0.500, [FallLvl]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall]]) 0.510, [FallSlp]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Fall/Shift]]) 0.500, [Hold]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Hold Sustain]]) 0.445, [Amount]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Amount]]) 0.294. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Sample-and-Hold]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Button/Shape/Random Stepped]]), clock [sync]([[Microfreak/UI/Front/Row/Bottom/04 LFO/Knob/Rate/Press]]) on; stored division code: 8. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [LFO]([[Microfreak/UI/Front/Row/Bottom/04 LFO]]) → Pitch: +0.008.
		- [LFO]([[Microfreak/UI/Front/Row/Bottom/04 LFO]]) → [Timbre]([[Microfreak/UI/Oscillator/Knob/Timbre]]): +0.586.
		- [ENV]([[Microfreak/UI/Front/Row/Bottom/05 Envelope]]) → [Cutoff]([[Microfreak/UI/Front/Row/Middle/03 Analog Filter/Knob/Cutoff]]): +0.205.
		- [LFO]([[Microfreak/UI/Front/Row/Bottom/04 LFO]]) → [Assign 1]([[Microfreak/UI/Front/Row/Top/01 Matrix/Button/Assn/1]]) → [Attack]([[Microfreak/UI/Front/Row/Bottom/05 Envelope/Knob/Attack]]): +0.582.
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope]]) → [Assign 2]([[Microfreak/UI/Front/Row/Top/01 Matrix/Button/Assn/2]]) → matrix amount [ENV]([[Microfreak/UI/Front/Row/Bottom/05 Envelope]]) → Cutoff: −0.235.
		- [LFO]([[Microfreak/UI/Front/Row/Bottom/04 LFO]]) → [Assign 3]([[Microfreak/UI/Front/Row/Top/01 Matrix/Button/Assn/3]]) → [Cycling Envelope Amount]([[Microfreak/UI/Front/Row/Middle/04 Cycling Envelope/Knob/Amount]]): +0.522.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/Top/02 Paraphonic Button]]) mode: on.
	- ## Customized controls
		- No factory preset is close. The nearest factory payload, [[Microfreak/Preset/061 AftrBlush]] (Factory 1.0 slot 146), differs in 22 controls.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
