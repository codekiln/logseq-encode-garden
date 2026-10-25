logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 222
preset-synth-microfreak-name:: Systemshock
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/SFX]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/221 My Sweet Ai]]
next:: [[Microfreak/Preset/223 Aphexian Kick]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
preset-synth-microfreak-parameter-payload-sha256:: 94ed6152d5645a646973ab823dcf3662ab5859200431c15018f126247759a901
preset-synth-file:: [Systemshock — October 25 slot 222 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___222%20Systemshock___Asset___Device-Read-2026-10-25.bin)
preset-synth-file-sha256:: c562f72f82bea35434413c0d11e50ba1a04f9d51f7031a95bfd0af5c95c3c708
- # Notes
	- ## Saved export and provenance
		- Saved export: read from the device's slot 222 over USB on October 25, 2026 with `mise run microfreak:download --slot 222`. Two consecutive reads returned the same file.
		- The parameter payload matches the MIDI Control Center archives Factory 3.0, Factory 6.0 (Factory 3.0 slot 292, Factory 6.0 slot 401). Comparison used `mise run microfreak:compare`.
		- [Download the slot 222 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___222%20Systemshock___Asset___Device-Read-2026-10-25.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[Microfreak/Preset/222 Systemshock/Asset/Device-Read-2026-10-25/bin]].
	- ## Oscillator
		- Model: V.Analog. [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		- Detune: 0.498. Shape: 0.498. Wave: 0.000.
		- Keyboard octave: 0. Glide: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.209; resonance: 0.452. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.516, sustain 0.133. Amp Mod is on, so the main envelope controls loudness. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: Env. Stored RiseLvl 0.208, RiseSlp 0.500, FallLvl 0.125, FallSlp 0.016, Hold 0.425, Amount 0.728. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- Square, clock sync on; stored division code: 9. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Cycling Envelope → Pitch: +0.999.
		- LFO → Pitch: +1.000.
		- LFO → Wave: +0.614.
		- LFO → Timbre: −0.595.
		- KEY/ARP → Timbre: +0.849.
		- Cycling Envelope → Cutoff: +0.554.
		- ENV → Cutoff: +1.000.
		- All other saved matrix amounts are zero.
	- ## Voice and keyboard
		- Paraphonic mode: on.
	- ## Evidence and interpretation
		- Values describe saved base settings before modulation. Controls use normalized 0…1 values unless a stored choice code is shown; they are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py). Mode, LFO shape, filter type and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js).
