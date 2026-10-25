logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 299
preset-synth-microfreak-name:: I Saw It B4
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Keys]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/298 King Snap]]
next:: [[Microfreak/Preset/300 MfCheese]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
preset-synth-microfreak-parameter-payload-sha256:: a2841bedf1c87ee061d781e7d5f183e114f987afcd27142dff4dd7a4a0fa77a3
preset-synth-file:: [I Saw It B4 — October 25 slot 299 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___299%20I%20Saw%20It%20B4___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 301c4830df4953dd20cfd52447dce43255e87a58e60983701640ffd6e6eb23cc
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 299 over USB on October 25, 2026 with `mise run microfreak:download --slot 299`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 362, Factory 6.0 slot 176). Comparison used `mise run microfreak:compare`.
		- [Download the slot 299 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___299%20I%20Saw%20It%20B4___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/299 I Saw It B4/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SawX. [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
		- Saw Mod: 0.000. Shape: 0.000. Noise: 0.050.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.237; resonance: 0.266. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.504, sustain 0.672. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.223, RiseSlp 0.500, FallLvl 0.295, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync on; stored division code: 4. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: −0.005.
		- LFO → Pitch: +0.002.
		- KEY/ARP → Pitch: +0.025.
		- Cycling Envelope → Wave: +0.030.
		- ENV → Timbre: +0.285.
		- LFO → Timbre: +0.050.
		- ENV → Cutoff: +0.440.
		- PRESSURE → Cutoff: +0.090.
		- ENV → Assign 1 → Noise: +0.275.
		- LFO → Assign 1 → Noise: +0.049.
		- PRESSURE → Assign 3 → Decay/Release: +1.000.
		- KEY/ARP → Assign 3 → Decay/Release: +0.189.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
