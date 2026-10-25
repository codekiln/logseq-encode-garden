logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 254
preset-synth-microfreak-name:: Comb-Me
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/253 Carrytron]]
next:: [[Microfreak/Preset/255 WubbliDub]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/12 Modal]]
preset-synth-microfreak-parameter-payload-sha256:: fd7d63011d9b063777e406ca97b45f4c463d3b2e34617ad658246ff46c8ea692
preset-synth-file:: [Comb-Me — October 25 slot 254 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___254%20Comb-Me___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 0e79bc96563a412a116caff632c9eb6d7703f82cb9159567c893837420f5f0ee
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 254 over USB on October 25, 2026 with `mise run microfreak:download --slot 254`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 321, Factory 6.0 slot 232). Comparison used `mise run microfreak:compare`.
		- [Download the slot 254 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___254%20Comb-Me___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/254 Comb-Me/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Modal. [[Microfreak/UG/06 Dig Osc/03 Types/12 Modal]]
		- Inharm: 0.115. Timbre: 0.594. Decay: 0.326.
		- Keyboard octave: 0. Glide: 0.255.
	- ## Filter
		- Band-pass filter. Saved cutoff: 0.000; resonance: 0.661. [[Microfreak/UG/07 Filter/01 Modifying Sound/02 Band Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.052, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.175, RiseSlp 0.500, FallLvl 0.305, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold, clock sync on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: +0.775.
		- LFO → Wave: +0.713.
		- Cycling Envelope → Timbre: +1.000.
		- LFO → Timbre: +1.000.
		- Cycling Envelope → Cutoff: +0.492.
		- ENV → Cutoff: +0.050.
		- LFO → Cutoff: +1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
