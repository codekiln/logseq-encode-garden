logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 128
preset-synth-microfreak-name:: KickBass
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Percussion]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/127 Filicophyta]]
next:: [[Microfreak/Preset/129 Opst]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/07 Waveshaper]]
preset-synth-microfreak-parameter-payload-sha256:: ccbe516de4717761958ba4e8c458c14b138e02df9c2460e26a4cfb097589fd13
preset-synth-file:: [KickBass — October 25 slot 128 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___128%20KickBass___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 213a55b9cfc9dda7261a4f5668d7359d834ce5b5846e48145387de8c35c81c61
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 128 over USB on October 25, 2026 with `mise run microfreak:download --slot 128`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 2.0, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 2.0 slot 105, Factory 2.1 slot 207, Factory 3.0 slot 207, Factory 6.0 slot 188). Comparison used `mise run microfreak:compare`.
		- [Download the slot 128 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___128%20KickBass___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/128 KickBass/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Waveshaper. [[Microfreak/UG/06 Dig Osc/03 Types/07 Waveshaper]]
		- Wave: 0.723. Amount: 0.804. Asym: 0.318.
		- Keyboard octave: -2. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.002; resonance: 0.000. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.618, sustain 0.432. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.278, FallSlp 0.259, Hold 0.000, Amount 0.850. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sine, clock sync off; stored normalized rate: 0.372. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +1.000.
		- Cycling Envelope → Wave: −0.790.
		- ENV → Timbre: −0.809.
		- LFO → Timbre: −0.085.
		- PRESSURE → Timbre: +1.000.
		- Cycling Envelope → Cutoff: +0.617.
		- ENV → Cutoff: +1.000.
		- PRESSURE → Assign 1 → LFO Rate: −0.561.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
