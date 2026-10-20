logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 077
preset-synth-microfreak-name:: Eonz
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/076 AutoCHILL]]
next:: [[Microfreak/Preset/078 A Juno Vibe]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]]
preset-synth-file:: [Eonz — September 28 MCC export](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/GitP___A___Session___26___10___20-Tue___Asset___Preset___Eonz-Archived-2026-09-28.mbp)
preset-synth-file-sha256:: 919e785b1427854c339994cdaf9d1bf51404801d6905d5ce5edfe1de81c67b61
- # Notes
	- [[Microfreak/UG/06 Dig Osc/03 Types/02 SuperWave]] duplicates a waveform and detunes the copies. Wave chooses saw, square, triangle or sine; Timbre adjusts detuning; Shape sets the volume of the detuned copies.
	- The digital twin is the September 28 MIDI Control Center user-bank export, stored in bank slot 160. Its parameter payload matches the Eonz supplied in Factory 1.1, 2.1, 3.0 and 6.0.
	- [[GitP/A/Session/26/10/20-Tue]] explores Eonz with the Launchpad and MicroFreak sequencers.
	- Modulation matrix — signed amounts normalized to −1…+1
		- PRESSURE → Wave: −1.000. In SuperWave, Wave selects the waveform.
		- ENV → Timbre: −0.430. The main envelope reduces SuperWave detuning.
		- ENV → Cutoff: +0.471. The main envelope opens the filter.
		- PRESSURE → Assign 1 → Decay/Release: +0.561. The expression input lengthens the main envelope decay/release.
		- All other matrix amounts are zero, including Cycling Envelope, LFO and Key/Arp routes.
		- The PRESSURE row responds to pressure or velocity according to the global Utility setting. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]]
		- Stored columns and assignment IDs follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py#L21-L67), [assignment interpreter](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_structured.py#L152-L173) and [MicroFreak Reader destination definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js#L458-L527).
