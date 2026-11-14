logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 399
preset-synth-microfreak-name:: FireAlarmLoBat
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Custom]]
prev:: [[Microfreak/Preset/398 Init]]
next:: [[Microfreak/Preset/400 Init]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
preset-synth-microfreak-parameter-payload-sha256:: 56ad9ed9134424d81e00b1f841c072239e5cfbd5611f464941c90be07d0df519
preset-synth-file:: [FireAlarmLoBat — November 12 slot 399 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___399%20FireAlarmLoBat___Asset___Device-Read-2026-11-12.bin)
preset-synth-file-sha256:: c1fd8141fd618369eedab241e3df0de7e8699f8d51e9e72b60a9580872d57a51
- # Notes
	- Simulates the low-battery chirp of a smoke or fire alarm. Made as a timing cue for the [[Ghost in the Patch Ceremony]] *Foreveter* on [[2026-11-14 Sat]], following the alarm-cue idea in [[Making/Music/Log/26/11/11-Wed]].
	- ## Sound
		- [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]] with the waves set to sine.
		- Each chirp is the highest G on the keyboard with octave +3 (G8), at the minimum sequencer gate length of 10 ms. Attack and decay are at zero.
	- ## Sequences
		- Set the tempo to 60 BPM for the intervals below.
		- Sequence A chirps once every 60 seconds.
		- Sequence B chirps once every 30 seconds.
		- Low-battery alarms commonly chirp at one of these two intervals.
	- ## Saved export and provenance
		- Saved export: read from the device's slot 399 over USB on November 12, 2026 with `mise run microfreak:download --slot 399`. Two consecutive reads returned the same file.
		- The parameter payload matches no MIDI Control Center factory archive.
		- [Download the slot 399 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___399%20FireAlarmLoBat___Asset___Device-Read-2026-11-12.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/399 FireAlarmLoBat/Asset/Device-Read-2026-11-12/bin]].
	- ## Oscillator
		- [Model]([[Microfreak/UI/Oscillator/Knob/Type]]): [SuperWave]([[Microfreak/UI/Oscillator/Knob/Type/SuperWave]]). [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
		- [Wave]([[Microfreak/UI/Oscillator/Knob/Type/SuperWave/Wave]]): 3 (stored choice code). [Detune]([[Microfreak/UI/Oscillator/Knob/Type/SuperWave/Detune]]): 0.500. [Volume]([[Microfreak/UI/Oscillator/Knob/Type/SuperWave/Volume]]): 0.500.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/03 Bottom/01 Octave]]): +3. [Glide]([[Microfreak/UI/Front/Row/02 Main/01 Glide Knob]]): 0.000.
	- ## Filter
		- [Low-pass]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Button/Type/LPF]]) filter. Saved [cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): 1.000; [resonance]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Resonance]]): 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Attack]]) 0.000, [decay/release]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Decay Rel]]) 0.000, [sustain]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Sustain]]) 1.000. [Amp Mod]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope [mode]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode]]): [Run]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode/Run]]). Stored [RiseLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise]]) 0.163, [RiseSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Rise/Shift]]) 0.500, [FallLvl]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall]]) 0.163, [FallSlp]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Fall/Shift]]) 0.500, [Hold]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Hold Sustain]]) 0.000, [Amount]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Amount]]) 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Sine]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Button/Shape/Sine]]), clock [sync]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Knob/Rate/Press]]) on; stored division code: 3. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- All saved matrix [amounts]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Knob]]) are zero.
	- ## Voice and keyboard
		- [Paraphonic]([[Microfreak/UI/Front/Row/01 Top/02 Paraphonic Button]]) mode: off.
	- ## Customized controls
		- Compared with the nearest factory payload, [[Microfreak/Preset/304 Saw Vox]] (Factory 2.1 slot 51); 5 controls differ.
		- [Oscillator type]([[Microfreak/UI/Oscillator/Knob/Type]]): SuperWave (factory Vocoder).
		- [Octave]([[Microfreak/UI/Front/Row/03 Bottom/01 Octave]]): +3 (factory 0).
		- [Decay/Release]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Decay Rel]]): 0.000 (factory 0.259).
		- [Paraphonic]([[Microfreak/UI/Front/Row/01 Top/02 Paraphonic Button]]): off (factory on).
		- [Seq]([[Microfreak/UI/Front/Row/03 Bottom/03 Arp Seq/Button/Arp Seq/Seq]]): on (factory off).
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
