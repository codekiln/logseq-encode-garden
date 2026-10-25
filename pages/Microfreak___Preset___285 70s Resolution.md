logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 285
preset-synth-microfreak-name:: 70s Resolution
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Sequence]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/284 Synz Today]]
next:: [[Microfreak/Preset/286 Driftsynchros]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
preset-synth-microfreak-parameter-payload-sha256:: 0c89a1174c8bbf4b984b50f3fbbf985b653987e012f1e6c29e696fb57eca5118
preset-synth-file:: [70s Resolution — October 25 slot 285 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___285%2070s%20Resolution___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: 97e23442aae2e00104fbcb7559c9fba09449de28996fc734eec37b0e33068862
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 285 over USB on October 25, 2026 with `mise run microfreak:download --slot 285`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 35, Factory 6.0 slot None). Comparison used `mise run microfreak:compare`.
		- [Download the slot 285 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___285%2070s%20Resolution___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/285 70s Resolution/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: SawX. [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
		- Saw Mod: 0.000. Shape: 0.584. Noise: 0.240.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.569; resonance: 0.687. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.125, sustain 0.688. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.099, FallSlp 0.500, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Triangle, clock sync off; stored normalized rate: 0.494. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- LFO → Wave: +0.026.
		- ENV → Cutoff: +0.174.
		- PRESSURE → Cutoff: +0.184.
		- KEY/ARP → Cutoff: +1.000.
		- Cycling Envelope → Assign 1 → Unison Spread: −0.032.
		- LFO → Assign 1 → Unison Spread: +0.029.
		- KEY/ARP → Assign 2 → LFO Rate: +1.000.
		- Cycling Envelope → Assign 3 → Noise: +0.514.
		- LFO → Assign 3 → Noise: −0.172.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
