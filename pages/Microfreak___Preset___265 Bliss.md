logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 265
preset-synth-microfreak-name:: Bliss
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/264 Disaster]]
next:: [[Microfreak/Preset/266 Cloque]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: 60359896f557f3f916cee508995a007ea832b17e309dc38e7e7aab9e94da3cbd
preset-synth-file:: [Bliss — October 25 slot 265 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___265%20Bliss___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 177ee9c5a91f43f833c71c1835880faa00ef03bd408132d2d5fa8c8135e13e2c
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 265 over USB on October 25, 2026 with `mise run microfreak:download --slot 265`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 331, Factory 6.0 slot 219). Comparison used `mise run microfreak:compare`.
		- [Download the slot 265 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___265%20Bliss___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/265 Bliss/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 0.352. Rectification: 0.323. Noise: 0.000.
		- Keyboard octave: +1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.300; resonance: 0.159. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.796, decay/release 0.734, sustain 0.966. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.117, RiseSlp 0.500, FallLvl 0.115, FallSlp 0.500, Hold 0.000, Amount 0.977. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync on; stored division code: 12. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Wave: −0.093.
		- LFO → Timbre: −0.174.
		- PRESSURE → Timbre: +0.485.
		- KEY/ARP → Timbre: +0.563.
		- ENV → Cutoff: +0.512.
		- LFO → Assign 1 → Arp/Seq Rate: −0.340.
		- PRESSURE → Assign 1 → Arp/Seq Rate: −0.322.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
