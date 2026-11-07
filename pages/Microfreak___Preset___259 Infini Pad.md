logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 259
preset-synth-microfreak-name:: Infini Pad
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/258 Glip]]
next:: [[Microfreak/Preset/260 8bitfi]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
preset-synth-microfreak-parameter-payload-sha256:: 9b2503974270c4796ded1ed0289d44b49ad71db24c3d9077bd6a32fa87391221
preset-synth-file:: [Infini Pad — October 25 slot 259 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___259%20Infini%20Pad___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: fb4599873da27fceabd67a5108a96e95c33e0dcb0d07b3e52fe9164ee84cc1a7
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 259 over USB on October 25, 2026 with `mise run microfreak:download --slot 259`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 326, Factory 6.0 slot 19). Comparison used `mise run microfreak:compare`.
		- [Download the slot 259 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___259%20Infini%20Pad___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/259 Infini Pad/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [Bass]([[Microfreak/UI/Oscillator/Knob/Type/BASS]]). [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
		- [Saturate]([[Microfreak/UI/Oscillator/Knob/Type/BASS/Saturate]]): 0.000. [Fold]([[Microfreak/UI/Oscillator/Knob/Type/BASS/Fold]]): 0.135. [Noise]([[Microfreak/UI/Oscillator/Knob/Type/BASS/Noise]]): 0.054.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/03 Bottom/01 Octave]]): 0. [Glide]([[Microfreak/UI/Front/Row/02 Main/01 Glide Knob]]): 0.000.
	- ## Filter
		- [Low-pass]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Button/Type/LPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): 0.101; [resonance]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Resonance]]): 0.512. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Attack]]) 0.669, [decay/release]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Decay Rel]]) 0.579, [sustain]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Sustain]]) 0.781. [Amp Mod]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode]]): [Loop]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode/Loop]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise]]) 0.213, [RiseSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise/Shift]]) 0.500, [FallLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall]]) 0.637, [FallSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall/Shift]]) 0.500, [Hold]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Hold Sustain]]) 0.000, [Amount]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Amount]]) 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Sawtooth]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Button/Shape/Rising Sawtooth]]), clock [sync]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Knob/Rate/Press]]) on; stored division code: 8. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope]]) → Pitch: +0.004.
		- [PRESSURE]([[Microfreak/UI/Front/Row/05 Keys]]) → [Wave]([[Microfreak/UI/Oscillator/Knob/Wave]]): +0.170.
		- [ENV]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope]]) → [Timbre]([[Microfreak/UI/Oscillator/Knob/Timbre]]): +0.968.
		- [PRESSURE]([[Microfreak/UI/Front/Row/05 Keys]]) → [Timbre]([[Microfreak/UI/Oscillator/Knob/Timbre]]): +0.486.
		- [ENV]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope]]) → [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): +0.328.
		- [PRESSURE]([[Microfreak/UI/Front/Row/05 Keys]]) → [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): +0.187.
		- [LFO]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO]]) → [Assign 1]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/1]]) → [Noise]([[Microfreak/UI/Oscillator/Knob/Type/BASS/Noise]]): +0.203.
		- [PRESSURE]([[Microfreak/UI/Front/Row/05 Keys]]) → [Assign 2]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/2]]) → [Noise]([[Microfreak/UI/Oscillator/Knob/Type/BASS/Noise]]): −0.125.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/01 Top/02 Paraphonic Button]]) mode: on.
	- ## Performance and session context
		- Held notes swell in slowly. The main envelope adds Fold (+0.968) and opens the cutoff (+0.328) as each note opens. Key pressure adds Saturate (+0.170), Fold (+0.486) and cutoff (+0.187) and lowers Noise through Assign 2 (−0.125); the synced sawtooth LFO adds Noise through Assign 1 (+0.203).
		- The PRESSURE matrix row follows the instrument's global expression setting, which the export does not record.
		- Turning [Shape]([[Microfreak/UI/Oscillator/Knob/Shape]]) up raises Noise and makes the pad work as a noisy bass in the low register, as heard from 05:15 in [[GitP/A/Session/26/11/01-Sun]].
		- In [[GitP/A/Session/26/11/06-Fri]] it was the only preset for the whole session: low C and G pedals swelled with key pressure, a high G5, and a C-major third at 22:39. Recorded knob changes covered Fold, Saturate, Noise, cutoff and resonance, filter amount, and the main and cycling envelopes. A read of slot 259 on November 7, 2026 again matched the October 25 export.
		- In [[GitP/A/Session/26/11/01-Sun]] the Launchpad Pro played it from 00:00 to 18:17. Recorded knob changes covered the main and cycling envelopes, filter amount, Spice, LFO rate and the three oscillator controls, with brief cutoff and resonance changes. A read of slot 259 after the session matched the October 25 export, so the slot still holds the factory sound. The session MIDI holds those knob changes as controller messages.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
