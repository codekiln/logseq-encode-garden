logseq-entity:: [[Logseq/Entity/Preset/Synth/Microfreak]]
preset-synth-microfreak-number:: 151
preset-synth-microfreak-name:: The Unstable
preset-synth-microfreak-category:: [[Logseq/Entity/Preset/Synth/Microfreak/Frontmatter/preset-synth-microfreak-category/Pad]]
preset-synth-microfreak-initialized:: false
preset-synth-microfreak-on-device:: true
preset-synth-origin:: [[Logseq/Entity/Preset/Synth/Frontmatter/preset-synth-origin/Factory]]
prev:: [[Microfreak/Preset/150 Stab One]]
next:: [[Microfreak/Preset/152 B3]]
preset-synth-microfreak-oscillator-type:: [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
preset-synth-file:: [The Unstable — October 24 slot 151 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/GitP___A___Session___26___10___24-Sat___Asset___Preset___The-Unstable-Live-2026-10-24.bin)
preset-synth-file-sha256:: 80d2c3b0312e9a2588dd969619d8e417e2d66e8655961ef064cfacc809b72365
preset-synth-microfreak-parameter-payload-sha256:: fbd5336466e244efd086246d66b7c760b9c8763b0134763a01c154636510fcf7
- # Notes
	- Paraphonic V.Analog pad with a slow attack, pressure-controlled pulse shape, and a looping cycling envelope that pushes filter resonance.
	- ## Saved export and provenance
		- Saved export: read from the device's slot 151 over USB on October 24, 2026 at 19:10 ET, after [[GitP/A/Session/26/10/24-Sat]], with `mise run microfreak:download --slot 151`. Two consecutive reads returned the same file, `slot-151.bin`.
		- The parameter payload matches the Factory 2.0, 2.1, 3.0 and 6.0 MIDI Control Center archives and the September 28, 2026 user-bank archive (computer-bank slot 228). Factory 1.0 and 1.1 do not contain this preset. Comparison used `mise run microfreak:compare`.
		- The slot still holds the factory payload, so the edits made during the session were not saved. codekiln says so at 14:35 in the episode.
		- [Download the slot 151 capture](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/GitP___A___Session___26___10___24-Sat___Asset___Preset___The-Unstable-Live-2026-10-24.bin). It is the raw device format (header plus data packets), not an `.mbp` file; see [[GitP/A/Session/26/10/24-Sat/Asset/Preset/The-Unstable-Live-2026-10-24/bin]].
	- ## Oscillator
		- Model: [V.Analog]([[Microfreak/UI/Oscillator/Knob/Type/VAnalog]]). [Detune]([[Microfreak/UI/Oscillator/Knob/Type/VAnalog/Detune]]) sets the detuning between two waves; [Shape]([[Microfreak/UI/Oscillator/Knob/Type/VAnalog/Shape]]) morphs a variable square from narrow pulse through full square to hard-sync formants; [Wave]([[Microfreak/UI/Oscillator/Knob/Type/VAnalog/Wave]]) morphs a saw from triangle to sawtooth with a widening notch. [[Microfreak/UG/06 Dig Osc/03 Types/06 VAnalog]]
		- On the panel, V.Analog puts Detune on the [Wave knob]([[Microfreak/UI/Oscillator/Knob/Wave]]) (CC 10), Shape on the [Timbre knob]([[Microfreak/UI/Oscillator/Knob/Timbre]]) (CC 12) and Wave on the [Shape knob]([[Microfreak/UI/Oscillator/Knob/Shape]]) (CC 13). In the session codekiln worked this out by ear: "So timbre is the shape."
		- Detune: 0.013. Shape: 0.024. Wave: 0.175. The saved sound starts almost undetuned, with a narrow pulse and a mostly triangular wave.
		- Pitch bend range: stored as 12; the unit is not verified.
		- [Keyboard octave]([[Microfreak/UI/Front/Row/03 Bottom/01 Octave]]): +2, per the [MicroFreak Reader octave table](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js#L1783-L1797). [Glide]([[Microfreak/UI/Front/Row/02 Main/01 Glide Knob]]): 0.
	- ## Filter
		- [Low-pass filter]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Button/Type/LPF]]). Saved [cutoff]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Cutoff]]): 0.099; [resonance]([[Microfreak/UI/Front/Row/02 Main/03 Analog Filter/Knob/Resonance]]): 0.000. Cutoff and resonance are normalized settings, not hertz or display values. [[Microfreak/UG/07 Filter/01 Modifying Sound/01 Low Pass Filter]]
		- The low cutoff leaves the filter mostly closed until the main envelope and the cycling envelope's resonance route open it up (see the modulation matrix).
	- ## Envelopes
		- Main envelope: [attack]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Attack]]) 0.431, [decay/release]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Decay Rel]]) 0.672, [sustain]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Knob/Sustain]]) 0.996. [Amp Mod]([[Microfreak/UI/Front/Row/03 Bottom/05 Envelope/Button/Amp Mod]]) is on, so the main envelope controls loudness: notes swell in and hold at nearly full level. [[Microfreak/UG/09 Envelope Gen/03 Envelope Stages]]
		- Cycling Envelope mode: [Loop]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Button/Mode/Loop]]). Stored RiseLvl 0.000, RiseSlp 0.500, FallLvl 0.211, FallSlp 0.500, Hold 0.000, [Amount]([[Microfreak/UI/Front/Row/02 Main/04 Cycling Envelope/Knob/Amount]]) 0.695. These are normalized stored fields; rise and fall times in milliseconds remain unverified. [[Microfreak/UG/09 Envelope Gen/06 Cycling Envelope]]
	- ## LFO
		- [Sample-and-Hold]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Button/Shape/Random Stepped]]), clock sync off, so the free rate applies. Stored normalized [rate]([[Microfreak/UI/Front/Row/03 Bottom/04 LFO/Knob/Rate]]): 0.764; stored division code: 5. The rate is not a hertz reading. [[Microfreak/UG/08 LFO/01 LFO Shape]] · [[Microfreak/UG/08 LFO/02 LFO Rate]]
	- ## Modulation matrix
		- Amounts use the signed normalized range −1…+1. The Assign columns resolve to the destinations shown.
		- PRESSURE → Timbre (V.Analog Shape): +0.669. Pressing harder widens the pulse toward square and sync formants.
		- ENV → Cutoff: +0.605. The main envelope opens the filter as each note swells in.
		- Cycling Envelope → [Assign 1]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/1]]) → Filter Resonance: +1.000. The looping envelope keeps changing the resonance.
		- PRESSURE → [Assign 2]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/2]]) → LFO Rate: +0.180. Pressure speeds up the Sample-and-Hold steps slightly.
		- LFO → [Assign 3]([[Microfreak/UI/Front/Row/01 Top/01 Matrix/Button/Assn/3]]) → Wave: +0.199. Sample-and-Hold steps the saw/triangle morph.
		- All other saved matrix amounts are zero; nothing routes to pitch.
	- ## Performance and session context
		- Play the saved sound with sustained notes and varying pressure. Pressure changes the pulse shape and the LFO speed, while the cycling envelope keeps resonance moving underneath.
		- [Paraphonic]([[Microfreak/UI/Front/Row/01 Top/02 Paraphonic Button]]) mode is on in the saved export. The PRESSURE row uses pressure or velocity according to the instrument's global Utility setting; the export does not establish which one was active.
		- In [[GitP/A/Session/26/10/24-Sat]], the recorded MIDI shows edits away from this baseline: Wave and Shape sweeps, cycling-envelope rise, fall, hold and amount changes, main-envelope attack, decay and sustain changes, a cutoff raise, and detune from about 10:00. Launchpad pad pressure, recorded as per-note pressure, arrives mainly from 11:00. None of these edits were saved.
		- Before the recording, codekiln heard pressure "really impact the volume." The saved matrix has no pressure route to level, so that impression may come from the Shape modulation or from the session's edits; the export cannot settle it.
	- ## Evidence and interpretation
		- Base controls use normalized 0…1 values unless a stored choice code is shown; matrix amounts use −1…+1. These describe saved base settings before modulation, not OLED percentages, hertz or milliseconds.
		- The [saved-parameter inspector](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/PARAMETERS.md) preserves the original fields. Oscillator interpretation assumes the documented firmware 5 layout; firmware is not detected from the export.
		- Matrix columns and assignments follow the [Freakout live map](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_live_map.py#L21-L107) and [assignment decoder](https://github.com/kmorrill/freakout/blob/main/src/minifreak_patch/microfreak_structured.py#L152-L173). Mode, LFO shape and octave labels follow the [MicroFreak Reader definitions](https://github.com/francoisgeorgy/microfreak-reader/blob/master/src/model/index.js#L1782-L1946).
		- [[Microfreak/UG/05 Connections/02 Matrix and Encoder/01 Sources and Destinations]] explains matrix sources, destinations and the expression row.
