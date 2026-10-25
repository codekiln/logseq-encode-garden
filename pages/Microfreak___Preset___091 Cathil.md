logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 091
preset-synth-microfreak-name:: Cathil
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/090 Guisky]]
next:: [[Microfreak/Preset/092 Smooth Pd]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/09 Formant]]
preset-synth-microfreak-parameter-payload-sha256:: 9993c59d04e34d9d92e11aa59adb272edd214f96e8375aeee142739727323dfb
preset-synth-file:: [Cathil — October 25 slot 91 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___091%20Cathil___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 9ccf7edf1179d7fdca70f48a1825dc43de02bfb55a56991748744f0ec2a5e84e
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 91 over USB on October 25, 2026 with `mise run microfreak:download --slot 91`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 178, Factory 1.1 slot 178, Factory 2.1 slot 173, Factory 3.0 slot 173, Factory 6.0 slot 434). Comparison used `mise run microfreak:compare`.
		- [Download the slot 91 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___091%20Cathil___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/091 Cathil/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Formant. [[Microfreak/UG/06 Dig Osc/03 Types/09 Formant]]
		- Interval: 0.312. Formant: 0.481. Shape: 0.549.
		- Keyboard octave: +2. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.212; resonance: 0.663. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.404, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 1.000, FallLvl 0.733, FallSlp 0.000, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync on; stored division code: 46877. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Timbre: +0.381.
		- ENV → Cutoff: +0.663.
		- ENV → Assign 1 → Cycling Envelope Amount: +0.643.
		- KEY/ARP → Assign 1 → Cycling Envelope Amount: +1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
