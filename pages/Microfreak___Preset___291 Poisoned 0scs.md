logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 291
preset-synth-microfreak-name:: Poisoned 0scs
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/290 Qrazy Press]]
next:: [[Microfreak/Preset/292 Moving Cars]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: 1f57eced4686d725ab53c7207605bec00235d559808a96f3bea14774aaa6a15e
preset-synth-file:: [Poisoned 0scs — October 25 slot 291 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___291%20Poisoned%200scs___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: bbc91862cd9c10fcfe0e2640d6a03e34af9ea02ba4f53ad889604edb67f2df1a
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 291 over USB on October 25, 2026 with `mise run microfreak:download --slot 291`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 355, Factory 6.0 slot 141). Comparison used `mise run microfreak:compare`.
		- [Download the slot 291 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___291%20Poisoned%200scs___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/291 Poisoned 0scs/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 0.177. Rectification: 0.000. Noise: 0.488.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.169; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.257, sustain 0.405. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.647, RiseSlp 0.000, FallLvl 1.000, FallSlp 1.000, Hold 0.000, Amount 0.242. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold, clock sync off; stored normalized rate: 0.999. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.005.
		- KEY/ARP → Pitch: −0.001.
		- Cycling Envelope → Wave: −0.331.
		- LFO → Wave: +0.188.
		- Cycling Envelope → Timbre: −1.000.
		- LFO → Timbre: +0.727.
		- KEY/ARP → Timbre: +1.000.
		- ENV → Cutoff: +0.585.
		- PRESSURE → Cutoff: +0.360.
		- KEY/ARP → Cutoff: +0.605.
		- Cycling Envelope → Assign 1 → LFO Rate: −1.000.
		- LFO → Assign 1 → LFO Rate: +0.379.
		- KEY/ARP → Assign 1 → LFO Rate: +1.000.
		- LFO → Assign 2 → Cycling Envelope Amount: +0.410.
		- LFO → Assign 3 → Cycling Envelope Fall: +0.302.
		- KEY/ARP → Assign 3 → Cycling Envelope Fall: +0.014.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
