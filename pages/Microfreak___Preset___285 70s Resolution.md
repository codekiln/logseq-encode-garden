logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 285
preset-synth-microfreak-name:: 70s Resolution
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/284 Synz Today]]
next:: [[Microfreak/Preset/286 Driftsynchros]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
preset-synth-microfreak-parameter-payload-sha256:: 0c89a1174c8bbf4b984b50f3fbbf985b653987e012f1e6c29e696fb57eca5118
preset-synth-file:: [70s Resolution — October 25 slot 285 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___285%2070s%20Resolution___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 97e23442aae2e00104fbcb7559c9fba09449de28996fc734eec37b0e33068862
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 285 over USB on October 25, 2026 with `mise run microfreak:download --slot 285`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 35, Factory 6.0 slot None). Comparison used `mise run microfreak:compare`.
		- [Download the slot 285 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___285%2070s%20Resolution___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/285 70s Resolution/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [SawX]([[Microfreak/UI/Oscillator/Knob/Type/SAWX]]). [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
		- [Saw Mod]([[Microfreak/UI/Oscillator/Knob/Type/SAWX/Saw Mod]]): 0.000. [Shape]([[Microfreak/UI/Oscillator/Knob/Type/SAWX/Shape]]): 0.584. [Noise]([[Microfreak/UI/Oscillator/Knob/Type/SAWX/Noise]]): 0.240.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/03 Bottom/01 Octave]]): 0. [Glide]([[Microfreak/UI/Front/Row/02 Main/01 Glide Knob]]): 0.000.
	- ## Filter
		- [Low-pass]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Button/Type/LPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): 0.569; [resonance]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Resonance]]): 0.687. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Attack]]) 0.000, [decay/release]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Decay Rel]]) 0.125, [sustain]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Sustain]]) 0.688. [Amp Mod]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode]]): [Run]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode/Run]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise]]) 0.000, [RiseSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise/Shift]]) 0.500, [FallLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall]]) 0.099, [FallSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall/Shift]]) 0.500, [Hold]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Hold Sustain]]) 0.000, [Amount]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Amount]]) 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Triangle]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Button/Shape/Triangle]]), clock [sync]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Knob/Rate/Press]]) off; stored normalized [rate]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Knob/Rate]]): 0.494. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [LFO]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO]]) → [Wave]([[Microfreak/UI/Oscillator/Knob/Wave]]): +0.026.
		- [ENV]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope]]) → [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): +0.174.
		- [PRESSURE]([[Microfreak/UI/Front/Row/05 Keys]]) → [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): +0.184.
		- [KEY/ARP]([[Microfreak/UI/Front/Row/05 Keys]]) → [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): +1.000.
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope]]) → [Assign 1]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/1]]) → Unison Spread: −0.032.
		- [LFO]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO]]) → [Assign 1]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/1]]) → Unison Spread: +0.029.
		- [KEY/ARP]([[Microfreak/UI/Front/Row/05 Keys]]) → [Assign 2]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/2]]) → [LFO Rate]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Knob/Rate]]): +1.000.
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope]]) → [Assign 3]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/3]]) → [Noise]([[Microfreak/UI/Oscillator/Knob/Type/SAWX/Noise]]): +0.514.
		- [LFO]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO]]) → [Assign 3]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/3]]) → [Noise]([[Microfreak/UI/Oscillator/Knob/Type/SAWX/Noise]]): −0.172.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/01 Top/02 Paraphonic Button]]) mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
