logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 059
preset-synth-microfreak-name:: Suby Rainbow
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/058 Junk.J]]
next:: [[Microfreak/Preset/060 Unstable Solo]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
preset-synth-microfreak-parameter-payload-sha256:: 4302f04f61e00f005abfb7cb7af6b733a566729e76e6fe7528982fe6e481b223
preset-synth-file:: [Suby Rainbow — October 25 slot 59 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___059%20Suby%20Rainbow___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: be27f12ac2e4db40291a11489039ccf0e5691f7b7017f7c5a089404eb51fcd8f
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 59 over USB on October 25, 2026 with `mise run microfreak:download --slot 59`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 1.0, Factory 1.1, Factory 2.1, Factory 3.0, Factory 6.0 (Factory 1.0 slot 144, Factory 1.1 slot 144, Factory 2.1 slot 144, Factory 3.0 slot 144, Factory 6.0 slot 18). Comparison used `mise run microfreak:compare`.
		- [Download the slot 59 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___059%20Suby%20Rainbow___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/059 Suby Rainbow/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: Chords. [[Microfreak/UG/06 Dig Osc/03 Types/10 Chords]]
		- Type: 5 (stored choice code). Inv/Transp: 0.000. Shape control: 0.059.
		- Keyboard octave: -1. Glide: 0.000.
	- ## Filter
		- High-pass filter. Saved cutoff: 0.190; resonance: 0.996. [[Microfreak/UG/07 Filter/01 Modifying Sound/03 High Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.154, sustain 0.000. Amp Mod is off. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Run. Stored RiseLvl 0.758, RiseSlp 0.565, FallLvl 0.639, FallSlp 0.196, Hold 0.000, Amount 1.000. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Sawtooth, clock sync on; stored division code: 2. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- ENV → Pitch: +0.976.
		- Cycling Envelope → Timbre: +0.686.
		- ENV → Cutoff: +0.604.
		- KEY/ARP → Cutoff: +0.797.
		- LFO → Assign 1 → Cycling Envelope Rise: +1.000.
		- LFO → Assign 2 → Cycling Envelope Fall: +1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: off.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
