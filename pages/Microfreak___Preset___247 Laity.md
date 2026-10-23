logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 247
preset-synth-microfreak-name:: Laity
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Lead]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Unknown]]
prev:: [[Microfreak/Preset/246 Queity]]
next:: [[Microfreak/Preset/248 GrowLing]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]]
preset-synth-file-sha256:: ca28de15bbb4a3e33817d4fe70bfc3585fd6f0bd169cd91bb3d7449a4422811d
- # Notes
	- SawX lead with envelope-shaped saw modulation, chorus and expression-controlled filter resonance.
	- ## Saved export and provenance
		- Saved export: September 28, 2026 MIDI Control Center user-bank archive, computer-bank slot 315, file `315-09282026 6h14-A315.mbp`. The computer-bank slot differs from this page’s observed device slot.
		- The parameter payload matches Factory 3.0 and 6.0. This is an archived factory-equivalent baseline; it does not establish the instrument’s saved or unsaved state during a later session.
	- ## Oscillator
		- Model: SAWX. Saw Mod controls a modulus stage; Shape controls chorus amount; Noise adds phase modulation from subsampled white noise.
		- Saw Mod: 0.120.
		- Shape: 0.113.
		- Noise: 0.000.
	- ## Filter
		- Low-pass filter. Saved cutoff: 0.409; resonance: 0.000. Cutoff and resonance are normalized settings, not hertz or instrument display values.
	- ## Envelopes
		- Main envelope: attack 0.000, decay/release 0.401, sustain 0.560. Amp Mod is on, so the main envelope controls loudness.
		- Cycling Envelope mode: Run. Stored RiseLvl 0.167, FallLvl 0.163, Hold 0.000, Amount 1.000. These are normalized stored fields; rise/fall times in milliseconds remain unverified.
	- ## LFO
		- Triangle; clock sync on. Stored normalized rate: 0.148; division code: 7. The rate is not a hertz reading, and the musical division has not been converted.
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. The assignment destinations below resolve the saved Assign columns.
		- ENV → Wave / Saw Mod: −0.244. The main envelope reduces saw modulation.
		- ENV → Timbre / Shape: −0.042. The main envelope reduces chorus amount.
		- PRESSURE → Timbre / Shape: −0.274. Expression reduces chorus amount.
		- ENV → Cutoff: +0.118. The main envelope opens the filter.
		- LFO → Cutoff: +0.048. The triangle LFO changes filter brightness.
		- PRESSURE → Cutoff: +0.216. Expression opens the filter.
		- PRESSURE → Assign 1 → Resonance: +0.730. Expression increases filter resonance.
		- All other saved matrix amounts are zero.
	- ## Performance and session context
		- Expression increases cutoff and resonance while reducing chorus amount. The main envelope changes the saw modulation, chorus and filter together.
		- Paraphonic mode is on in the saved export. The PRESSURE matrix row uses pressure or velocity according to the instrument’s global Utility setting; the export does not establish which expression source was used in the session.
		- [[GitP/A/Session/26/10/12-Mon]] references this sound. The session context does not identify which recording passages use it.
	- ## Evidence and interpretation
		- Base controls use normalized 0…1 values unless a stored choice code is shown; matrix amounts use −1…+1. These describe saved base settings, before modulation, and are not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix columns and assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py#L21-L107) and [assignment decoder](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_structured.py#L152-L173). Mode and waveform labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js#L1782-L1946).
		- [[Microfreak/UG/06 Dig Osc/03 Types/15 SAWX]] describes oscillator controls. [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]] explains the matrix and expression row.
