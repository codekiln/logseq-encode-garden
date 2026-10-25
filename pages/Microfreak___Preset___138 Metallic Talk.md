logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 138
preset-synth-microfreak-name:: Metallic Talk
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/137 Solide]]
next:: [[Microfreak/Preset/139 Long FM Bass]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/11 Speech]]
preset-synth-microfreak-parameter-payload-sha256:: d1054bfa9c5ef1a687d54fa4a2adc1c29d6f25fb33a71fe307d30b06dce1aae9
preset-synth-file:: [Metallic Talk — October 25 slot 138 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___138%20Metallic%20Talk___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: ea3383634d12b816fbf0dabfff57e0f212515c36cc9392888c554c26db7f8621
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 138 over USB on October 25, 2026 with `mise run microfreak:download --slot 138`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 114, Factory 2.1 slot 216, Factory 3.0 slot 216, Factory 6.0 slot 185). Comparison used `mise run microfreak:compare`.
		- [Download the slot 138 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___138%20Metallic%20Talk___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/138 Metallic Talk/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Speech. [[Microfreak/UG/06 Dig Osc/03 Types/11 Speech]]
		- Type: 0.247. Timbre: 0.180. Word: 0.228.
		- Keyboard octave: -2. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.926; resonance: 0.555. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.035, decay/release 0.398, sustain 1.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.210, RiseSlp 0.500, FallLvl 0.323, FallSlp 0.500, Hold 0.308, Amount 0.306. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold Filtered, clock sync on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Timbre: +1.000.
		- ENV → Cutoff: +0.386.
		- LFO → Cutoff: −0.771.
		- LFO → Assign 1 → Word: +1.000.
		- PRESSURE → Assign 2 → Arp/Seq Rate: +0.254.
		- PRESSURE → Assign 3 → Filter Resonance: +0.355.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
