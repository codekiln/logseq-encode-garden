logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 289
preset-synth-microfreak-name:: Down For Bass
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/288 Solo Trancer]]
next:: [[Microfreak/Preset/290 Qrazy Press]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
preset-synth-microfreak-parameter-payload-sha256:: c3830dc14c988b86fa4b86d348a61a3b2f3ed905c8d119329eae701d5c609ac9
preset-synth-file:: [Down For Bass — October 25 slot 289 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___289%20Down%20For%20Bass___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 7756ccfda0bd2c38cf5c8e22e1faf51748be734adb434570323f03700964d8a8
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 289 over USB on October 25, 2026 with `mise run microfreak:download --slot 289`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 353, Factory 6.0 slot 29). Comparison used `mise run microfreak:compare`.
		- [Download the slot 289 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___289%20Down%20For%20Bass___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/289 Down For Bass/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Bass. [[Microfreak/UG/06 Dig Osc/03 Types/14 BASS]]
		- Saturate: 0.000. Fold: 0.078. Noise: 0.155.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.000; resonance: 0.456. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.032, decay/release 0.264, sustain 0.044. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.249, FallSlp 0.500, Hold 0.353, Amount 0.827. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sample-and-Hold, clock sync on; stored division code: 10. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Pitch: −0.005.
		- LFO → Wave: +0.054.
		- PRESSURE → Timbre: +0.277.
		- Cycling Envelope → Cutoff: +1.000.
		- ENV → Cutoff: −0.054.
		- LFO → Cutoff: +0.330.
		- PRESSURE → Cutoff: +0.427.
		- KEY/ARP → Cutoff: +0.344.
		- PRESSURE → Assign 1 → Noise: +0.130.
		- LFO → Assign 2 → Oscillator Type: +0.054.
		- LFO → Assign 3 → matrix amount ENV → Cutoff: −0.309.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
