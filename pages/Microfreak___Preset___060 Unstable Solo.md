logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 060
preset-synth-microfreak-name:: Unstable Solo
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/059 Suby Rainbow]]
next:: [[Microfreak/Preset/061 AftrBlush]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
preset-synth-microfreak-parameter-payload-sha256:: fdb084b975b7f2db7d630df8cf54c86bff6862ac26aff24f4311d700f7fdd7f0
preset-synth-file:: [Unstable Solo — October 25 slot 60 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___060%20Unstable%20Solo___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: cd210939f110ea128e4a8f933066c8f3d0dfd8c3c8672c85681735250385c5c1
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 60 over USB on October 25, 2026 with `mise run microfreak:download --slot 60`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 145, Factory 2.1 slot 145, Factory 3.0 slot 145, Factory 6.0 slot 382). Comparison used `mise run microfreak:compare`.
		- [Download the slot 60 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___060%20Unstable%20Solo___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/060 Unstable Solo/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: V.Analog. [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		- Detune: 0.428. Shape: 0.185. Wave: 0.865.
		- Keyboard octave: +1. Glide: 0.183.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.721; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.143, decay/release 0.450, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.239, RiseSlp 0.500, FallLvl 0.376, FallSlp 0.500, Hold 0.000, Amount 0.868. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.339. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.004.
		- Cycling Envelope → Timbre: +0.483.
		- PRESSURE → Cutoff: +0.304.
		- Cycling Envelope → Assign 1 → Wave: −0.589.
		- LFO → Assign 2 → Cycling Envelope Fall: +0.177.
		- PRESSURE → Assign 3 → LFO Rate: +0.297.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
