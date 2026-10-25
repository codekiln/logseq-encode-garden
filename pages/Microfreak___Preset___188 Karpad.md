logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 188
preset-synth-microfreak-name:: Karpad
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Template]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/187 KarpluStrings]]
next:: [[Microfreak/Preset/189 Brass 1]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/05 KarplusStr]]
preset-synth-microfreak-parameter-payload-sha256:: 9fe4f6eb8912040156e720c2e8102013bd75a3b0f953e29ee6884aecb44f89d6
preset-synth-file:: [Karpad — October 25 slot 188 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___188%20Karpad___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: de181805063472a4540f60d0be94892d96e354edf1b6b37ab17f115452fe773c
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 188 over USB on October 25, 2026 with `mise run microfreak:download --slot 188`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.1 slot 218, Factory 2.1 slot 31, Factory 3.0 slot 261, Factory 6.0 slot 306). Comparison used `mise run microfreak:compare`.
		- [Download the slot 188 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___188%20Karpad___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/188 Karpad/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: KarplusStr. [[Microfreak/UG/06 Dig Osc/03 Types/05 KarplusStr]]
		- Bow: 0.205. Position: 0.000. Decay: 0.480.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.339; resonance: 0.205. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.142, decay/release 0.299, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.575, RiseSlp 0.500, FallLvl 0.512, FallSlp 0.500, Hold 0.307, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sawtooth, clock sync on; stored division code: 6. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.002.
		- LFO → Pitch: +0.001.
		- Cycling Envelope → Wave: +0.233.
		- PRESSURE → Wave: +0.167.
		- PRESSURE → Timbre: +0.155.
		- ENV → Cutoff: +0.339.
		- LFO → Assign 1 → Decay: +0.192.
		- Cycling Envelope → Assign 2 → matrix amount LFO → Assign 1: −0.233.
		- KEY/ARP → Assign 3 → Decay/Release: +0.688.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
