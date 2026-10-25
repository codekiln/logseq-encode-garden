logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 223
preset-synth-microfreak-name:: Aphexian Kick
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Percussion]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/222 Systemshock]]
next:: [[Microfreak/Preset/224 Talk About D]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: 2e1805669c568f53db1fcaca7f6877539c2f953626b6738ccff42997ad6b797e
preset-synth-file:: [Aphexian Kick — October 25 slot 223 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___223%20Aphexian%20Kick___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 745263f9096995f514d63be714627262769dc779797a11066f867d42656b0073
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 223 over USB on October 25, 2026 with `mise run microfreak:download --slot 223`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 293, Factory 6.0 slot 116). Comparison used `mise run microfreak:compare`.
		- [Download the slot 223 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___223%20Aphexian%20Kick___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/223 Aphexian Kick/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 0.588. Rectification: 0.402. Noise: 0.487.
		- Keyboard octave: -2. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.000; resonance: 1.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.244, sustain 0.484. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.331, FallSlp 0.016, Hold 0.000, Amount 0.963. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold, clock sync off; stored normalized rate: 0.989. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.940.
		- Cycling Envelope → Wave: −0.600.
		- ENV → Wave: +0.254.
		- LFO → Timbre: +0.237.
		- KEY/ARP → Timbre: +0.849.
		- ENV → Cutoff: +1.000.
		- Cycling Envelope → Assign 1 → Cycling Envelope Rise: +0.941.
		- LFO → Assign 1 → Cycling Envelope Rise: +0.568.
		- LFO → Assign 2 → LFO Rate: +0.745.
		- ENV → Assign 3 → matrix amount ENV → Cutoff: +0.028.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
