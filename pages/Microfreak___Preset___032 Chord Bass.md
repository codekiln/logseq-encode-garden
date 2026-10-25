logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 032
preset-synth-microfreak-name:: Chord Bass
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/031 Ixos]]
next:: [[Microfreak/Preset/033 Organism]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
preset-synth-microfreak-parameter-payload-sha256:: d131e9070c2ec98f051a680d27adabe167ec210e16261afc0fba90d69ba73647
preset-synth-file:: [Chord Bass — October 25 slot 32 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___032%20Chord%20Bass___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 97e157b8dd61e62d6537fd55923c22e213ce355bec65cc533a85e3940cbd7d01
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 32 over USB on October 25, 2026 with `mise run microfreak:download --slot 32`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 12, Factory 2.1 slot 12, Factory 3.0 slot 12, Factory 6.0 slot None). Comparison used `mise run microfreak:compare`.
		- [Download the slot 32 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___032%20Chord%20Bass___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/032 Chord Bass/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [Chords]([[Microfreak/UI/Oscillator/Knob/Type/Chords]]). [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
		- [Type]([[Microfreak/UI/Oscillator/Knob/Type/Chords/Type]]): 3 (stored choice code). [Inv/Transp]([[Microfreak/UI/Oscillator/Knob/Type/Chords/Inv Transp]]): 0.686. [Shape control]([[Microfreak/UI/Oscillator/Knob/Type/Chords/Waveform]]): 0.260.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/03 Bottom/01 Octave]]): -1. [Glide]([[Microfreak/UI/Front/Row/02 Main/01 Glide Knob]]): 0.000.
	- ## Filter
		- [High-pass]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Button/Type/HPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): 0.277; [resonance]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Resonance]]): 1.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Attack]]) 0.000, [decay/release]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Decay Rel]]) 0.038, [sustain]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Sustain]]) 0.000. [Amp Mod]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Button/Amp Mod]]) is off. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode]]): [Loop]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode/Loop]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise]]) 0.000, [RiseSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise/Shift]]) 0.000, [FallLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall]]) 0.279, [FallSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall/Shift]]) 0.000, [Hold]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Hold Sustain]]) 0.000, [Amount]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Amount]]) 0.480. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Triangle]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Button/Shape/Triangle]]), clock [sync]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Knob/Rate/Press]]) on; stored division code: 5. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [ENV]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope]]) → Pitch: +0.999.
		- [ENV]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope]]) → [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): +0.372.
		- [PRESSURE]([[Microfreak/UI/Front/Row/05 Keys]]) → [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): +1.000.
		- [KEY/ARP]([[Microfreak/UI/Front/Row/05 Keys]]) → [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): +0.797.
		- [LFO]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO]]) → [Assign 1]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/1]]) → matrix amount [Cycling Envelope]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope]]) → Pitch: +0.037.
		- [LFO]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO]]) → [Assign 2]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/2]]) → matrix amount [Cycling Envelope]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope]]) → Timbre: +0.999.
		- [LFO]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO]]) → [Assign 3]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/3]]) → [Cycling Envelope Fall]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall]]): −0.053.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/01 Top/02 Paraphonic Button]]) mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
