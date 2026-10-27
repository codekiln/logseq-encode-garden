logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 118
preset-synth-microfreak-name:: Fight
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/117 Minor Pad]]
next:: [[Microfreak/Preset/119 NoiseBusters]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
preset-synth-microfreak-parameter-payload-sha256:: 0cd4e2b218f3673e8d6eb33e94dd4a2cba6ea9c8e89c80d5abb0538902646efe
preset-synth-file:: [Fight — October 25 slot 118 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___118%20Fight___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: bd02bf0ebb4d11593d5b864499046beb6cc4901e261eea7d725b217e758bb307
- # Notes
	- ## Saved export and provenance
		- On October 26, 2026, two further read-only USB downloads of saved slot 118 returned identical `slot-118.bin` files, matching the October 25 export and this page’s file and parameter-payload SHA-256 values. The [download protocol](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/download.py) reads saved memory without selecting the preset.
		- Saved export: read from the device's slot 118 over USB on October 25, 2026 with `mise run microfreak:download --slot 118`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 6, Factory 2.1 archive, Factory 3.0 slot 198, Factory 6.0 slot 330). Comparison used `mise run microfreak:compare`.
		- [Download the slot 118 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___118%20Fight___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/118 Fight/Asset/Device-Read-2026-10-25/bin]].
		- [Download the October 26 Fight preset export](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/GitP___A___Session___26___10___26-Mon___Asset___Preset___118-Fight.mfpz). The `.mfpz` export preserves the captured saved sound; its parser round-trip matched the raw payload. See [[GitP/A/Session/26/10/26-Mon/Asset/Preset/118-Fight/mfpz]] for format provenance and restoration limits.
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [Chords]([[Microfreak/UI/Oscillator/Knob/Type/Chords]]). [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
		- [Type]([[Microfreak/UI/Oscillator/Knob/Type/Chords/Type]]): 1 (stored choice code). [Inv/Transp]([[Microfreak/UI/Oscillator/Knob/Type/Chords/Inv Transp]]): 0.391. [Shape control]([[Microfreak/UI/Oscillator/Knob/Type/Chords/Waveform]]): 0.455.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/03 Bottom/01 Octave]]): 0. [Glide]([[Microfreak/UI/Front/Row/02 Main/01 Glide Knob]]): 0.000.
		- Type chooses the chord; Inv/Transp changes its inversion and register; Shape changes the oscillator waveform. The chord keeps its identity as Inv/Transp changes. Chords mode uses the last key as the root and disables paraphony. [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
	- ## Filter
		- [Low-pass]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Button/Type/LPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): 0.423; [resonance]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Resonance]]): 0.385. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Attack]]) 0.000, [decay/release]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Decay Rel]]) 0.285, [sustain]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Sustain]]) 0.218. [Amp Mod]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode]]): [Env]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode/Env]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise]]) 0.179, [RiseSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise/Shift]]) 0.500, [FallLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall]]) 0.421, [FallSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall/Shift]]) 0.500, [Hold]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Hold Sustain]]) 0.000, [Amount]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Amount]]) 0.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Square]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Button/Shape/Square]]), clock [sync]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Knob/Rate/Press]]) on. The stored division field is outside the supported choice range, so its musical clock division remains unknown. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- [Amounts]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Knob]]) use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- [Cycling Envelope]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope]]) → [Wave]([[Microfreak/UI/Oscillator/Knob/Wave]]): +0.223.
		- [LFO]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO]]) → [Timbre]([[Microfreak/UI/Oscillator/Knob/Timbre]]): +0.017.
		- [ENV]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope]]) → [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): +0.643.
		- [PRESSURE]([[Microfreak/UI/Front/Row/05 Keys]]) → [Cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): +0.768.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/01 Top/02 Paraphonic Button]]) mode: off.
	- ## Performance and session context
		- Play a root note to trigger the oscillator’s chord, then use Timbre to change the voicing. The saved envelope opens the low-pass filter on each note; pressure or velocity can add further cutoff modulation according to the global keyboard-expression setting. The small LFO-to-Timbre route adds movement to the inversion. [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]] · [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Fight comes in as a lead at 07:01 in [[GitP/A/Session/26/10/26-Mon]], announced on the commentary microphone as “118” followed by an indistinct word. No knobs move for the next 50 seconds; pad pressure carries the movement through the PRESSURE → Cutoff route. From 07:51, Wave and Timbre changes on that layer step through chord types and inversions. The saved capture supplies a factory baseline, not evidence of unsaved edits.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
