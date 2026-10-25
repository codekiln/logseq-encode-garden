logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 120
preset-synth-microfreak-name:: Jobs 4 Rhythm
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Percussion]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/119 NoiseBusters]]
next:: [[Microfreak/Preset/121 Fat Moves]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/12 Modal]]
preset-synth-microfreak-parameter-payload-sha256:: d3c0f0781fd2f865d75ec07bb3771a306cd20defd197836307acb9ef87c8716f
preset-synth-file:: [Jobs 4 Rhythm — October 25 slot 120 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___120%20Jobs%204%20Rhythm___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 3add184b9f0d7980fb7c814c69e8b1727896f42de8e5ceb97c1370ebcfae2326
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 120 over USB on October 25, 2026 with `mise run microfreak:download --slot 120`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 8, Factory 2.1 slot 20, Factory 3.0 slot 20, Factory 6.0 slot None). Comparison used `mise run microfreak:compare`.
		- [Download the slot 120 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___120%20Jobs%204%20Rhythm___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/120 Jobs 4 Rhythm/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Modal. [[Microfreak/UG/06 Dig Osc/03 Types/12 Modal]]
		- Inharm: 0.000. Timbre: 0.536. Decay: 0.000.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 1.000; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.218, sustain 1.000. Amp Mod is off. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.226, RiseSlp 0.499, FallLvl 0.372, FallSlp 0.502, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sawtooth, clock sync off; stored normalized rate: 0.909. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: −0.001.
		- Cycling Envelope → Wave: +0.587.
		- LFO → Wave: +0.956.
		- LFO → Timbre: +1.000.
		- ENV → Cutoff: +1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
