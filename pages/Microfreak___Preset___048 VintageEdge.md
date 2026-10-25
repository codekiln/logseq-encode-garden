logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 048
preset-synth-microfreak-name:: VintageEdge
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/047 White Calx]]
next:: [[Microfreak/Preset/049 Sci Organ]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
preset-synth-microfreak-parameter-payload-sha256:: 6f9f2dfdf0128ff9e32e6155d99a3b122c5e49b01052c3813057fdfa5aea5d90
preset-synth-file:: [VintageEdge — October 25 slot 48 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___048%20VintageEdge___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 17dac9219a1617190ce9208c75634a885eb86e3dd0be1eba0a0f4267709e43bb
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 48 over USB on October 25, 2026 with `mise run microfreak:download --slot 48`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 134, Factory 1.1 slot 134, Factory 2.1 slot 134, Factory 3.0 slot 134, Factory 6.0 slot 221). Comparison used `mise run microfreak:compare`.
		- [Download the slot 48 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___048%20VintageEdge___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/048 VintageEdge/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: V.Analog. [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		- Detune: 0.000. Shape: 0.000. Wave: 0.000.
		- Keyboard octave: +1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.740; resonance: 0.754. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.629, sustain 0.000. Amp Mod is off. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.000, RiseSlp 0.563, FallLvl 0.572, FallSlp 0.519, Hold 0.141, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.340. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Wave: +0.038.
		- ENV → Timbre: +0.115.
		- ENV → Cutoff: −0.098.
		- LFO → Assign 1 → Cycling Envelope Fall: +0.067.
		- LFO → Assign 2 → Cycling Envelope Hold: +0.674.
		- Cycling Envelope → Assign 3 → Wave: +0.008.
		- LFO → Assign 3 → Wave: −0.026.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
