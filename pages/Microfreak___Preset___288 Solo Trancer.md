logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 288
preset-synth-microfreak-name:: Solo Trancer
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/287 Holistic]]
next:: [[Microfreak/Preset/289 Down For Bass]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
preset-synth-microfreak-parameter-payload-sha256:: 8cd862c4f5feffb672bc906775626aa42427b4162735b6968f0f7f413acb96ce
preset-synth-file:: [Solo Trancer — October 25 slot 288 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___288%20Solo%20Trancer___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 30fc1d759b41b17a3390bbc2d1bccbe45c6d3f14119ac14259acd94411d45242
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 288 over USB on October 25, 2026 with `mise run microfreak:download --slot 288`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 352, Factory 6.0 slot 228). Comparison used `mise run microfreak:compare`.
		- [Download the slot 288 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___288%20Solo%20Trancer___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/288 Solo Trancer/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Harm. [[Microfreak/UG/06 Dig Osc/03 Types/16 HARM]]
		- Spread: 0.500. Rectification: 0.466. Noise: 0.000.
		- Keyboard octave: -2. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.706; resonance: 0.401. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.235, sustain 0.000. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.167, RiseSlp 0.500, FallLvl 0.163, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Square, clock sync on; stored division code: 12. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Pitch: +0.002.
		- KEY/ARP → Pitch: −0.001.
		- Cycling Envelope → Wave: +0.004.
		- LFO → Wave: −0.030.
		- KEY/ARP → Wave: +0.135.
		- Cycling Envelope → Timbre: +0.004.
		- LFO → Timbre: +0.030.
		- KEY/ARP → Timbre: −0.300.
		- Cycling Envelope → Cutoff: −0.007.
		- ENV → Cutoff: +0.550.
		- PRESSURE → Cutoff: −0.628.
		- Cycling Envelope → Assign 1 → Noise: +0.047.
		- Cycling Envelope → Assign 2 → Cycling Envelope Amount: +0.028.
		- ENV → Assign 2 → Cycling Envelope Amount: +0.003.
		- LFO → Assign 2 → Cycling Envelope Amount: −0.021.
		- PRESSURE → Assign 2 → Cycling Envelope Amount: +0.764.
		- KEY/ARP → Assign 2 → Cycling Envelope Amount: +0.009.
		- Cycling Envelope → Assign 3 → matrix amount ENV → Cutoff: +0.147.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
