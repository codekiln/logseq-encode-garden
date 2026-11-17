see-also:: [[Microfreak/Patch/Storage]], [[Microfreak/Patch/Research]], [[Microfreak/CLI/Probe a patch]], [[Microfreak/Sequence/Write a sequence]]

- # Write a patch into a MicroFreak slot
	- I describe a sound in words, such as "in slot 508, a dark pluck bass in E minor with a short glide and vibrato when I press harder". These steps turn the request into a description file, write it into a preset on my MicroFreak, and play it back through the [[Zoom H5/My Unit]] to check it.
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
			- Save it as `$TMPDIR/microfreak-patch/patch.yaml`. For the pluck bass above:
			- ```yaml
			  name: Dark Pluck
			  category: Bass
			  start: plain
			  oscillator: {wave: 0.5, shape: 0.4}
			  filter: {cutoff_hz: 300, resonance: 0.35}
			  envelope: {decay_seconds: 0.5, sustain: 0.0, filter_amount: 0.2}
			  glide: {mode: Time, seconds: 0.1}
			  keyboard: {scale: Minor, root: E}
			  lfo: {shape: Sine, hz: 3}
			  matrix:
			    - {source: Pressure, destination: Co1.LFO, amount: 0.006}
			  ```
			- `start: plain` first sets a plain sound, below, so the patch keeps nothing from the base but what the description names. Without it the base keeps every setting the description leaves out.
			- Description keys, below, lists every key. Read musical words, below, says how to turn a request into values.
		- ### 3. Pick the slot and the base
			- Use the slot I name. My own presets fill slots 1–320 and 350–402; write to one of those only when I name it. Otherwise run `mise run microfreak:empty-slots` and pick an empty slot; slots 497–512 are my test slots.
			- Use the base I name. Otherwise use slot 359, [[Microfreak/Preset/359 Init]]: it was saved on firmware 5, so it holds every field, and the task refuses a field an older base lacks.
			- Slot 359 is not a plain sound. It stores Basic Waves at Wave 0.05, a high-pass filter at cutoff 0.37, decay 0.8 with sustain 0.23, the Cycling Envelope looping at full amount into Timbre, the LFO synced to the clock, paraphony on with Unison count 4 stored, bend range ±12, keyboard octave −1, and Assign 1 and Assign 3 aimed at the Envelope → Cutoff amount. Begin with `start: plain` unless the request builds on that sound.
			- `start: plain` sets: Basic Waves sawtooth (Wave 0.5, Timbre 0, Shape 0); low-pass filter open, no resonance; attack 0, decay 0.3, sustain 1, Amp Mod on, Legato and Snap off; Cycling Envelope Env mode at amount 0; sine LFO at about 2.2 Hz, Sync and Retrig off; no glide; bend range 2, keyboard octave 0, Scale Off, Press Mode Aftertouch, Key/Arp Linear, Velo Amp Mod 0; paraphony off, preset volume 0; arpeggiator off; every matrix amount 0.
		- ### 4. Preview
			- ```sh
			  mise run microfreak:write-patch "$TMPDIR/microfreak-patch/patch.yaml" --base 359
			  ```
			- It prints `settings_changed`: each stored field it would change, before and after, in the panel's terms where they are known (`±2 semitones`, `about 300 Hz`, `about 0.5 s decay to -20 dB`) and as 0–1 values elsewhere. A line starting `error:` names the key to fix.
		- ### 5. Write
			- ```sh
			  mise run microfreak:write-patch "$TMPDIR/microfreak-patch/patch.yaml" --base 359 --slot 508 \
			    --backup-dir "$TMPDIR/microfreak-patch/backup-1"
			  ```
			- When the slot holds a preset the task saves it to `--backup-dir` first and refuses without it; each rewrite of a slot needs a new folder. `upload.read_back_matches: true` means the slot holds what was sent. `mise run microfreak:upload BACKUP.bin --slot N --backup-dir NEW_FOLDER` puts a backup back.
		- ### 6. Listen
			- `mise run microfreak:probe --slot 508 --no-write --note E2` plays E2 for 1.5 seconds and reports its pitch, level and brightness. A script plays what the request is about; save it as `$TMPDIR/microfreak-patch/script.yaml`. For the pluck, a plain note, a note with full pressure, then a glide:
			- ```yaml
			  events:
			    - {t: 0.0, on: E2}
			    - {t: 1.0, off: E2}
			    - {t: 1.2, pressure: 127}
			    - {t: 1.25, on: E2}
			    - {t: 2.2, off: E2}
			    - {t: 2.25, pressure: 0}
			    - {t: 2.4, on: E2}
			    - {t: 2.6, on: B2}
			    - {t: 2.65, off: E2}
			    - {t: 3.4, off: B2}
			  tail: 0.5
			  ```
			- ```sh
			  mise run microfreak:probe --slot 508 --no-write --script "$TMPDIR/microfreak-patch/script.yaml" \
			    --output "$TMPDIR/microfreak-patch/report.json" --wav-dir "$TMPDIR/microfreak-patch/wav"
			  ```
			- The report's `notes` gives each note's pitch, level and brightness. `--output` keeps every 10 ms frame: vibrato shows as the pitch swinging, glide as the pitch sliding between notes, a filter envelope or LFO as `centroid_hz` falling or swinging, and a decay as `db` falling.
			- A sub-oscillator (Basic Waves Shape above 0) makes the waveform repeat at the sub's period, so `pitch` reads an octave low and `cents_from_note` near −1200. That is the sub, not a wrong note.
		- ### 7. Tell me what the slot holds
			- The slot and the name it shows, the base, each setting the description changed in the panel's terms, the choices you made where my request left one open, what the probe heard, and where any backup is.
	- ## Description keys
		- `name`: 1–14 letters, digits, spaces, periods, underscores or hyphens. `category`: Bass, Brass, Keys, Lead, Organ, Pad, Percussion, Sequence, SFX, Strings, Template or Vocoder.
		- `start`: `plain` sets the plain sound in step 3 before everything else in the description.
		- `oscillator`: `type`, one of BasicWaves, SuperWave, Wavetable, Harmo, KarplusStr, V.Analog, Waveshaper, Two Op. FM, Formant, Chords, Speech, Modal, Noise, Vocoder, Bass, SawX, Harm, WaveUser, Sample, Scan Grains, Cloud Grains, Hit Grains; `wave`, `timbre` and `shape`, 0–1, the three oscillator knobs ([[Microfreak/UG/06 Dig Osc/03 Types]] says what each does per type).
			- Basic Waves: `wave` 0.5 is a sawtooth whatever `timbre` is. `wave` 0 with `timbre` 0 is a square; raising `timbre` narrows the pulse. `wave` 1.0 with `timbre` 0 is a sawtooth an octave up; with `timbre` 1.0, a sawtooth at pitch. `shape` adds a sine an octave below.
		- `filter`: `type` LPF, BPF or HPF; `cutoff`, 0–1, or `cutoff_hz`, 140–6460 Hz for the low-pass; `resonance`, 0–1.
		- `envelope`: `attack`, `decay` and `sustain`, 0–1, or `attack_seconds` (0.03–1.8 s to full level) and `decay_seconds` (0.11–2.5 s to 20 dB down with sustain 0); `filter_amount`, −1 to 1, the panel's Filter Amt, how far the envelope opens the cutoff; `amp_mod`, on or off (on: the envelope shapes loudness); `legato` and `snap`, on or off ([[Microfreak/Patch/Storage]]).
		- `cycling_envelope`: `mode` Env, Run or Loop; `rise`, `fall`, `hold`, `amount`, `rise_shape` and `fall_shape`, 0–1.
		- `lfo`: `shape` Sine, Triangle, Saw, Square, Random Stepped or Random Gliding; `hz`, 0.14–22, or `rate`, 0–1; `division`, 8 bars, 4 bars, 2 bars, 1 bar, 1/2, 1/2T, 1/4, 1/4T, 1/8, 1/8T, 1/16, 1/16T or 1/32 of the MIDI clock's tempo; `retrig` Off, On or Legato; `sync` on or off. A `hz` or `rate` turns sync off and a `division` turns it on, unless `sync` is given.
		- `glide`: `off`, or `mode` Time with `seconds` (0–10), Rate with `seconds_per_octave`, or Sync with `division` (1/32, 1/16T, 1/16, 1/8T, 1/8, 1/4T, 1/4 or 1/2 at the Arp/Seq tempo).
		- `keyboard`: `bend_range` 0–24 semitones; `press_mode` Aftertouch or Velocity; `key_arp_mode` Linear or Random; `velo_amp_mod` 0–10; `scale` Global, Off, Major, Minor, Harmonic Minor, Dorian, Mixolydian, Blues or Pentatonic; `root` C to B; `octave` −3 to +3, which shifts only the MicroFreak's own keys.
		- `voice`: `paraphonic` on or off; `mode` Paraphonic, Chord or Unison, which turns paraphony on; `unison_voices` 2–4; `unison_spread` in semitones, 0.001–12; `chord`, up to three offsets in semitones from the played note, such as `[3, 7, 10]`; `volume` −12 to +12, half a decibel a step.
		- `arp`: `on`, on or off (on also turns the sequencer off); `direction` Up, Order, Random or Pattern; `octaves` 1–4; `swing` 50–75 percent; `division` 1, 1/2, 1/2T, 1/4, 1/4T, 1/8, 1/8T, 1/16, 1/16T, 1/32 or 1/32T; `bpm` 30–240, the tempo when the MicroFreak runs on its own clock.
		- `matrix`: the whole matrix, as a list of routes; every amount it does not list becomes 0, and `envelope.filter_amount` is set after it. A route has `source` (CycEnv, Envelope, LFO, Pressure or Key/Arp), `destination` and `amount` (−1 to 1). Pitch, Wave, Timbre and Cutoff are fixed columns; on Pitch, `semitones` can replace `amount` (1.0 is 48 semitones at the source's full value). Any other destination takes one of the three Assign columns: Shape, Resonance, Glide, LFO Rate, Attack, Decay, Sustain, Rise, Fall, Hold, CycEnv Amount, Unison Spread, Arp Rate, or a field name such as `Co1.LFO`, which modulates another route's amount. `matrix: []` clears it.
		- `fields`: stored fields by name, for anything the sections do not cover: an integer is a choice, a decimal a 0–1 value, `raw:N` a stored value.
		- `sequence`: a sequence in the format of [[Microfreak/Sequence/Write a sequence]], written after the patch.
	- ## Read musical words
		- Vibrato is LFO → Pitch: `{source: LFO, destination: Pitch, semitones: 0.3}` swings ±0.3 semitones. Slow vibrato is about 3 Hz (`lfo: {shape: Sine, hz: 3}`), an ordinary one 5–6 Hz, a fast one 7–8 Hz.
		- Vibrato that comes in as I press harder is Pressure aimed at that route's amount: `{source: Pressure, destination: Co1.LFO, amount: 0.006}` gives ±0.3 semitones at full pressure, with no LFO → Pitch route of its own. On a pluck with no sustain, a press after the attack meets a note already 20–30 dB down; a longer decay leaves room to hear it.
		- Detuned or thick: `voice: {mode: Unison, unison_voices: 4, unison_spread: 0.1}`. Four voices sit at ±spread and ±2 × spread, so 0.05–0.15 sounds detuned and 0.5 or more sounds like separate pitches.
		- Glide or portamento: `glide: {mode: Time, seconds: 0.1}`. Every note glides from the last pitch, overlapping or not.
		- A chord from one key: `voice: {mode: Chord, chord: [3, 7, 10]}` plays a minor seventh on the key held.
		- A key and a scale, such as "in A minor": `keyboard: {scale: Minor, root: A}`. The MicroFreak then plays every note outside the scale, from MIDI and from the sequencer alike, as a scale note.
		- Pluck or stab: attack 0, sustain 0 and a short decay. `decay_seconds` 0.2 is a very short pluck, 0.5 a bass pluck, 1–2 a ringing one.
		- Dark, mostly closed: `cutoff_hz` 150–300. Muffled but open: 500–1200. Bright: 3000 and up. "Some" resonance: 0.3–0.4; a squelchy or ringing filter: 0.6 or more.
		- The envelope opening the filter: `envelope.filter_amount`. On a cutoff of 300 Hz, 0.2 put E2's spectral centroid at 382 Hz 50 ms in and 203 Hz at 200 ms.
		- Wobble: an LFO on the cutoff, such as `lfo: {shape: Square, hz: 2}` with `{source: LFO, destination: Cutoff, amount: 0.4}` and the cutoff at 0.25. A wobble locked to the song's tempo uses `lfo: {division: 1/8}`, which follows MIDI clock from the Mac or a DAW.
		- An arpeggio: `arp: {on: on, direction: Up, octaves: 2, division: 1/16}`. It plays the notes held or sent over MIDI at the clock it receives, or at `bpm` when the MicroFreak's Clock Source is Internal.
		- An octave up or down for notes I send over MIDI belongs in the notes themselves; `keyboard.octave` shifts only the MicroFreak's own keys.
		- Choose a value for any word not covered here, listen with the probe, and tell me what you chose.
	- ## Worked examples
		- Each was written from slot 359 with `write-patch` and played with `probe` on [[2026-11-17 Tue]].
		- ### Dark pluck bass in E minor, slot 508
			- The description in step 2. E2 sounded at −27 dBFS and fell 20 dB in 0.48 s. Its spectral centroid read 382 Hz 50 ms in and 203 Hz at 200 ms as the filter envelope closed. The probe named the note E1 because of the sub.
		- ### Unison lead, slot 503
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
			- Written without `start: plain`, so slot 359's Timbre of 0 makes `wave: 0.0` a square. A2 held without pressure stayed at A2; under full pressure it swung about 0.9 semitones either way; full bend raised it 2.0 semitones; A2 to A3 glided over about 0.1–0.15 s. The fourth harmonic showed the four voices at −0.21, −0.09, +0.12 and +0.19 semitones.
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
			- A2 alone played A, C, E and G and fell from −29 to −71 dBFS over 1.5 s. Wave 1.0 with slot 359's Timbre of 0 is a sawtooth an octave up, so the spectrum shows A3, C4, E4 and G4.
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
			- A square wave. C2 held: the spectral centroid jumped between about 750 Hz and 2.8 kHz, rising every 0.50 s. E2 sounded as E♭2.
	- ## Source
		- [#454 Add microfreak:write-patch and a page for writing a described patch](https://github.com/codekiln/logseq-encode-garden/issues/454) and [#462 Close the gaps the fresh-agent MicroFreak patch test found](https://github.com/codekiln/logseq-encode-garden/issues/462), part of [#448 Let an agent set any MicroFreak patch setting from a description](https://github.com/codekiln/logseq-encode-garden/issues/448). The code is [lib/patch.py](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/patch.py), using the conversions in [lib/patch_fields.py](https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/microfreak/lib/patch_fields.py).
