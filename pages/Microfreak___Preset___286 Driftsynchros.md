logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 286
preset-synth-microfreak-name:: Driftsynchros
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Bass]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/285 70s Resolution]]
next:: [[Microfreak/Preset/287 Holistic]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
preset-synth-file-sha256:: 2236cbd6f76189c9a461df30ee320a638ec97fa84f85e60813d629af5946c049
preset-synth-microfreak-parameter-payload-sha256:: 7e218a9f937e60fdcf6ccbb384f1058691bb809ccab486114413a81ea17ada87
preset-synth-file:: [Driftsynchros — October 25 slot 286 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Microfreak___Preset___286%20Driftsynchros___Asset___Device-Read-2026-10-25.bin)
- # Notes
	- SawX patch with a looping envelope closing the filter and expression increasing saw modulation.
	- ## Saved export and provenance
		- Saved export: September 28, 2026 MIDI Control Center user-bank archive, computer-bank slot 350, file `350-09282026 6h14-A350.mbp`. The computer-bank slot differs from this page’s observed device slot.
		- The parameter payload matches Factory 3.0 and 6.0. This is an archived factory-equivalent baseline; it does not establish the instrument’s saved or unsaved state during a later session.
	- ## Oscillator
		- Model: SAWX. Saw Mod controls a modulus stage; Shape controls chorus amount; Noise adds phase modulation from subsampled white noise.
		- Saw Mod: 0.000.
		- Shape: 0.000.
		- Noise: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.661; resonance: 0.234. Cutoff and resonance are normalized settings, not hertz or instrument display values.
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.621, sustain 0.000. Amp Mod is off; the envelope can still affect its matrix destinations.
		- Cycling Envelope mode: Loop. Stored RiseLvl 0.000, FallLvl 0.492, Hold 0.000, Amount 1.000. These are normalized stored fields; rise/fall times in milliseconds remain unverified.
	- ## LFO
		- Saw; clock sync on. Stored normalized rate: 0.148; division code: 8. The rate is not a hertz reading, and the musical division has not been converted.
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. The assignment destinations below resolve the saved Assign columns.
		- Cycling Envelope → Pitch: −0.001. A small envelope route changes pitch.
		- PRESSURE → Wave / Saw Mod: +0.357. Expression increases saw modulation.
		- Cycling Envelope → Cutoff: −0.904. The looping envelope strongly closes the filter.
		- LFO → Cutoff: −0.031. The saw LFO changes filter brightness.
		- PRESSURE → Cutoff: +0.021. Expression slightly opens the filter.
		- Cycling Envelope → Assign 1 → Cycling Envelope FallLvl: −0.378. The envelope modulates its own stored fall control.
		- ENV → Assign 1 → Cycling Envelope FallLvl: +0.120. The main envelope also changes that fall control.
		- All other saved matrix amounts are zero.
	- ## Performance and session context
		- Amp Mod is off, so the main envelope does not shape loudness through Amp Mod; it still changes the cycling envelope through the matrix. The looping envelope supplies the strongest filter movement.
		- Paraphonic mode is on in the saved export. The PRESSURE matrix row uses pressure or velocity according to the instrument’s global Utility setting; the export does not establish which expression source was used in the session.
		- [[GitP/A/Session/26/10/12-Mon]] references this sound. The session context does not identify which recording passages use it.
	- ## Evidence and interpretation
		- Base controls use normalized 0…1 values unless a stored choice code is shown; matrix amounts use −1…+1. These describe saved base settings, before modulation, and are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix columns and assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py#L21-L107) and [assignment decoder](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_structured.py#L152-L173). Mode and waveform labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js#L1782-L1946).
		- [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]] describes oscillator controls. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]] explains the matrix and expression row.
