see-also:: [[Microfreak/Patch/Storage]], [[Microfreak/Patch/Research]], [[Microfreak/CLI/Probe a patch]], [[Microfreak/Sequence/Write a sequence]]

- # Write a patch into a MicroFreak slot
	- I describe a sound in words, such as "in slot 503, a four-voice unison lead, slightly detuned, short glide, vibrato when I press harder, bend range two semitones". These steps turn the request into a description file, write it into a preset on my MicroFreak, and play it back through the [[Zoom H5/My Unit]] to check it.
	- `mise run microfreak:write-patch` writes a description into a preset and uploads it to a slot. `mise run microfreak:probe` plays notes, pressure or bend into the slot and measures pitch, level and brightness, as [[Microfreak/CLI/Probe a patch]] describes. Both run from a garden checkout on current `main`, like the sequence tasks in [[Microfreak/Sequence/Write a sequence]].
	- ## What you need
		- The MicroFreak and the H5 connected by USB, [[Arturia/MCC]] closed, and [[mise]] and [[uv]] installed.
		- Hands off the keys while a task runs.
	- ## Steps
		- ### 1. Open a garden checkout on current `main`
			- ```sh
			  cd "$(ghq list --full-path --exact github.com/codekiln/logseq-encode-garden)"
			  git pull --ff-only
			  mkdir -p "$TMPDIR/microfreak-patch"
			  ```
			- Keep descriptions, backups and recordings in `$TMPDIR/microfreak-patch`, outside the repository: the repository is public and the backups hold my presets.
		- ### 2. Write the request as a description file
			- Save it as `$TMPDIR/microfreak-patch/patch.yaml`. Every section is optional; the base keeps whatever the description leaves out.
			- ```yaml
			  name: Unison Lead
			  category: Lead
			  oscillator: {type: BasicWaves, wave: 0.0}
			  filter: {type: LPF, cutoff: 0.6, resonance: 0.1}
			  envelope: {attack: 0.0, decay: 0.3, sustain: 0.8, amp_mod: on}
			  cycling_envelope: {amount: 0.0}
			  glide: {mode: Time, seconds: 0.1}
			  keyboard: {bend_range: 2, press_mode: Aftertouch, scale: Off}
			  voice: {mode: Unison, unison_voices: 4, unison_spread: 0.1}
			  lfo: {shape: Sine, rate: 0.55, retrig: Off}
			  matrix:
			    - {source: Pressure, destination: Co1.LFO, amount: 0.02}
			  ```
			- Description keys, below, lists every key. Read musical words, below, says how to turn a request into values.
		- ### 3. Pick the slot and the base
			- Use the slot I name. My own presets fill slots 1–320 and 350–402; write to one of those only when I name it. Otherwise run `mise run microfreak:empty-slots` and pick an empty slot; slots 497–512 are my test slots.
			- Use the base I name. Otherwise use slot 359, [[Microfreak/Preset/359 Init]]: it was saved on firmware 5, so it holds every field, and the task refuses a field an older base lacks. Slot 359 stores a high-pass filter, Cycling Envelope → Timbre at full amount and LFO Sync on, so start the description with `filter`, `matrix` and `lfo` when the sound should not have those.
		- ### 4. Preview
			- ```sh
			  mise run microfreak:write-patch "$TMPDIR/microfreak-patch/patch.yaml" --base 359
			  ```
			- It prints `settings_changed`: each stored field it would change, before and after, in the panel's terms where they are known (`±2 semitones`, `Unison`, `about 2 Hz`) and as 0–1 values elsewhere. A line starting `error:` names the key to fix.
		- ### 5. Write
			- ```sh
			  mise run microfreak:write-patch "$TMPDIR/microfreak-patch/patch.yaml" --base 359 --slot 503 \
			    --backup-dir "$TMPDIR/microfreak-patch/backup-1"
			  ```
			- When the slot holds a preset the task saves it to `--backup-dir` first and refuses without it; each rewrite of a slot needs a new folder. `upload.read_back_matches: true` means the slot holds what was sent. `mise run microfreak:upload BACKUP.bin --slot N --backup-dir NEW_FOLDER` puts a backup back.
		- ### 6. Listen
			- `mise run microfreak:probe --slot 503 --no-write` plays C4 for 1.5 seconds and reports its pitch, level and brightness. A script plays what the request is about; for the lead above:
			- ```yaml
			  events:
			    - {t: 0.0, on: A2}
			    - {t: 0.05, pressure: 0}
			    - {t: 1.5, pressure: 127}
			    - {t: 3.0, pressure: 0}
			    - {t: 3.2, bend: 1.0}
			    - {t: 4.0, bend: 0}
			    - {t: 4.4, on: A3}
			    - {t: 4.45, off: A2}
			    - {t: 5.2, off: A3}
			  tail: 0.4
			  ```
			- ```sh
			  mise run microfreak:probe --slot 503 --no-write --script "$TMPDIR/microfreak-patch/lead-script.yaml" \
			    --output "$TMPDIR/microfreak-patch/lead.json" --wav-dir "$TMPDIR/microfreak-patch/wav"
			  ```
			- The report's `notes` gives each note's pitch and level; `--output` keeps every 10 ms frame, where vibrato shows as the pitch swinging, glide as the pitch sliding between notes and a filter LFO as `centroid_hz` rising and falling.
		- ### 7. Tell me what the slot holds
			- The slot and the name it shows, the base, each setting the description changed in the panel's terms, the choices you made where my request left one open, what the probe heard, and where any backup is.
	- ## Description keys
		- `name`: 1–14 letters, digits, spaces, periods, underscores or hyphens. `category`: Bass, Brass, Keys, Lead, Organ, Pad, Percussion, Sequence, SFX, Strings, Template or Vocoder.
		- `oscillator`: `type`, one of BasicWaves, SuperWave, Wavetable, Harmo, KarplusStr, V.Analog, Waveshaper, Two Op. FM, Formant, Chords, Speech, Modal, Noise, Vocoder, Bass, SawX, Harm, WaveUser, Sample, Scan Grains, Cloud Grains, Hit Grains; `wave`, `timbre` and `shape`, 0–1, the three oscillator knobs ([[Microfreak/UG/06 Dig Osc/03 Types]] says what each does per type).
		- `filter`: `type` LPF, BPF or HPF; `cutoff` and `resonance`, 0–1.
		- `envelope`: `attack`, `decay` and `sustain`, 0–1; `amp_mod`, on or off (on: the envelope shapes loudness); `legato` and `snap`, on or off ([[Microfreak/Patch/Storage]]).
		- `cycling_envelope`: `mode` Env, Run or Loop; `rise`, `fall`, `hold`, `amount`, `rise_shape` and `fall_shape`, 0–1.
		- `lfo`: `shape` Sine, Triangle, Saw, Square, Random Stepped or Random Gliding; `hz`, 0.14–22, or `rate`, 0–1; `retrig` Off, On or Legato; `sync` on or off. A `hz` or `rate` turns sync off unless `sync` is given.
		- `glide`: `off`, or `mode` Time with `seconds` (0–10), Rate with `seconds_per_octave`, or Sync with `division` (1/32, 1/16T, 1/16, 1/8T, 1/8, 1/4T, 1/4 or 1/2 at the Arp/Seq tempo).
		- `keyboard`: `bend_range` 0–24 semitones; `press_mode` Aftertouch or Velocity; `key_arp_mode` Linear or Random; `velo_amp_mod` 0–10; `scale` Global, Off, Major, Minor, Harmonic Minor, Dorian, Mixolydian, Blues or Pentatonic; `root` C to B; `octave` −3 to +3, which shifts only the MicroFreak's own keys.
		- `voice`: `paraphonic` on or off; `mode` Paraphonic, Chord or Unison, which turns paraphony on; `unison_voices` 2–4; `unison_spread` in semitones, 0.001–12; `chord`, up to three offsets in semitones from the played note, such as `[3, 7, 10]`; `volume` −12 to +12, half a decibel a step.
		- `arp`: `bpm` 30–240, the Arp/Seq tempo when the MicroFreak runs on its own clock.
		- `matrix`: the whole matrix, as a list of routes; every amount it does not list becomes 0. A route has `source` (CycEnv, Envelope, LFO, Pressure or Key/Arp), `destination` and `amount` (−1 to 1). Pitch, Wave, Timbre and Cutoff are fixed columns; on Pitch, `semitones` can replace `amount` (1.0 is 48 semitones at the source's full value). Any other destination takes one of the three Assign columns: Shape, Resonance, Glide, LFO Rate, Attack, Decay, Sustain, Rise, Fall, Hold, CycEnv Amount, Unison Spread, Arp Rate, or a field name such as `Co1.LFO`, which modulates another route's amount. `matrix: []` clears it.
		- `fields`: stored fields by name, for anything the sections do not cover: an integer is a choice, a decimal a 0–1 value, `raw:N` a stored value.
		- `sequence`: a sequence in the format of [[Microfreak/Sequence/Write a sequence]], written after the patch.
	- ## Read musical words
		- Vibrato is LFO → Pitch: `{source: LFO, destination: Pitch, semitones: 0.3}` swings ±0.3 semitones, with `lfo: {shape: Sine, hz: 5}`. Vibrato that comes in as I press harder is Pressure aimed at that route's amount: `{source: Pressure, destination: Co1.LFO, amount: 0.006}` gives ±0.3 semitones at full pressure, with no LFO → Pitch route of its own.
		- Detuned or thick: `voice: {mode: Unison, unison_voices: 4, unison_spread: 0.1}`. Four voices sit at ±spread and ±2 × spread, so 0.05–0.15 sounds detuned and 0.5 or more sounds like separate pitches.
		- Glide or portamento: `glide: {mode: Time, seconds: 0.1}`. Every note glides from the last pitch, overlapping or not.
		- A chord from one key: `voice: {mode: Chord, chord: [3, 7, 10]}` plays a minor seventh on the key held.
		- A key and a scale, such as "in A minor": `keyboard: {scale: Minor, root: A}`. The MicroFreak then plays every note outside the scale, from MIDI and from the sequencer alike, as a scale note.
		- Pluck or stab: `envelope: {attack: 0.0, decay: 0.3, sustain: 0.0}`. On slot 359's oscillator a decay of 0.45 fell 20 dB in 0.95 s and 40 dB in 1.65 s.
		- Wobble: an LFO on the cutoff, such as `lfo: {shape: Square, hz: 2}` with `{source: LFO, destination: Cutoff, amount: 0.4}` and the cutoff at 0.25.
		- Brighter or darker is `filter.cutoff`; more bite is `filter.resonance`. Their hertz and the envelope's seconds are not measured yet ([[Microfreak/Patch/Storage]] lists what is), so choose a value, listen with the probe, and tell me what you chose.
		- An octave up or down for notes I send over MIDI belongs in the notes themselves; `keyboard.octave` shifts only the MicroFreak's own keys.
	- ## Worked examples
		- Each was written from slot 359 with `write-patch` and played with `probe` on [[2026-11-17 Tue]].
		- ### Unison lead, slot 503
			- The description in step 2. A2 held without pressure stayed at A2; under full pressure it swung about 0.9 semitones either way; full bend raised it 2.0 semitones; A2 to A3 glided over about 0.1–0.15 s. The fourth harmonic showed the four voices at −0.21, −0.09, +0.12 and +0.19 semitones.
		- ### Minor seventh stab, slot 504
			- ```yaml
			  name: Min7 Stab
			  category: Keys
			  oscillator: {type: BasicWaves, wave: 1.0}
			  filter: {type: LPF, cutoff: 0.45, resonance: 0.0}
			  envelope: {attack: 0.0, decay: 0.3, sustain: 0.0, amp_mod: on}
			  cycling_envelope: {amount: 0.0}
			  glide: off
			  keyboard: {scale: Off}
			  voice: {mode: Chord, chord: [3, 7, 10]}
			  matrix: []
			  ```
			- A2 alone played A, C, E and G and fell from −29 to −71 dBFS over 1.5 s. With this wave the energy sits in each note's second harmonic, so the spectrum shows A3, C4, E4 and G4.
		- ### Wobble bass in C minor, slot 505
			- ```yaml
			  name: Wobble Bass
			  category: Bass
			  oscillator: {type: BasicWaves, wave: 0.0}
			  filter: {type: LPF, cutoff: 0.25, resonance: 0.4}
			  envelope: {attack: 0.0, decay: 0.3, sustain: 1.0, amp_mod: on}
			  cycling_envelope: {amount: 0.0}
			  glide: off
			  lfo: {shape: Square, hz: 2, retrig: On}
			  keyboard: {scale: Minor, root: C}
			  voice: {paraphonic: off}
			  matrix:
			    - {source: LFO, destination: Cutoff, amount: 0.4}
			  ```
			- C2 held: the spectral centroid jumped between about 750 Hz and 2.8 kHz, rising every 0.50 s. E2 sounded as E♭2.
	- ## Source
		- [#454 Add microfreak:write-patch and a page for writing a described patch](https://github.com/codekiln/logseq-encode-garden/issues/454), part of [#448 Let an agent set any MicroFreak patch setting from a description](https://github.com/codekiln/logseq-encode-garden/issues/448). The code is [lib/patch.py](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/patch.py), using the conversions in [lib/patch_fields.py](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/patch_fields.py).
