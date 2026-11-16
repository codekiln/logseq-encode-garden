see-also:: [[Microfreak/CLI/Upload a preset]], [[Microfreak/Sequence/Storage]], [[Microfreak/Sequence/Research]], [[Microfreak/MIDI/Port/Arturia MicroFreak]]

- # Audition a slot's sequence
	- `mise run microfreak:audition --slot N` plays the sequence stored in slot N from the Mac. It records the notes the MicroFreak sends back over USB MIDI and the sound the [[Zoom H5/My Unit]] hears, then prints one JSON report with the notes of every step. It was added for [#434 Play a MicroFreak slot's sequence and detect its notes through the Zoom H5](https://github.com/codekiln/logseq-encode-garden/issues/434), so that [#435 Decode how a MicroFreak preset stores its sequence](https://github.com/codekiln/logseq-encode-garden/issues/435) and [#436 Write a described sequence into a MicroFreak preset](https://github.com/codekiln/logseq-encode-garden/issues/436) can compare a stored or written sequence with what the instrument plays.
	- ## Invocation
		- Run from the garden root, with MIDI Control Center closed and the H5 connected:
		- ```sh
		  mise run microfreak:audition --slot 35
		  mise run microfreak:audition --slot 113 --loops 1 --output /private/tmp/mf/slot-113.json
		  mise run microfreak:audition --slot 374 --division 1/16 --bpm 90
		  mise run microfreak:audition --slot 5 --no-audio
		  ```
		- `--slot` takes 1–512, and the slot must hold a preset.
		- `--bpm` sets the clock tempo (default 120). `--loops` sets how many times the pattern plays (default 2). `--steps` sets the pattern length, which otherwise comes from the slot's `Seq.Length`.
		- `--division` sets the step length by sending CC 92, for example `--division 1/16`. Without it, the step length comes from the slot's `Arp.Div`. `--clocks-per-step` sets it directly.
		- `--plain` sends CCs for a simple timbre before playing: Basic Waves square wave, no sub-oscillator, Spice or Glide, filter open without resonance, instant attack, full sustain, shortest release. `--cc 23=127` sends any other CC. The report lists every CC sent.
		- `--no-midi-out` leaves Arp/Seq MIDI Out as it is and relies on the audio. `--no-audio` skips the recording.
		- `--no-select` plays the sound and pattern already loaded, without a program change or CCs, for example pattern B after pressing B on the panel. It cannot be combined with `--plain`, `--cc` or `--division`.
		- `--wav-dir` chooses the folder for the recording, by default `$TMPDIR/microfreak-audition`; the task refuses a folder inside the repository. `--output` also writes the report to a file. `--device` and `--input-channel` choose the audio input, by default `H5` and input index 2.
		- `mise run microfreak:test` runs the MicroFreak unit tests with numpy, which the audio analysis tests need. Plain `python3 -m unittest` skips those tests when numpy is missing.
	- ## What the task does
		- Reads the slot's header and data the way `microfreak:download` does, for the name, `Seq.Length`, `Arp.Div`, `Arp.SeqOn` and the gate length. It writes nothing to the slot.
		- Reads four global settings: Clock Source, Arp/Seq MIDI Out, MIDI Output Destination and MIDI Input Channel. It sets Clock Source to USB unless it is USB or Auto, turns Arp/Seq MIDI Out on, and sets the output destination to Both when it leaves out USB. It reads each change back, and at the end it restores each setting and reads it back again.
		- Selects the slot, sends any CCs, starts recording, sends MIDI Start and then steps × clocks per step × loops Clocks at the tempo, then Stop.
		- Afterwards it sends All Notes Off and selects the slot again, which discards the CCs. The sequencer is left stopped.
	- ## Report
		- Top level: `slot`, `name`, `category`, `preset` (the stored settings read above and the SHA-256 of the slot's data), `tempo` (bpm, clocks per step and where that number came from, step length in ms), `instrument` (the selection messages, the global settings before, which ones were changed and restored, the CCs sent), `midi_out`, `recording`, `steps`, `summary` and `warnings`.
		- `steps` has one row per played step, in play order, with `step` (1 is the first step of the pattern) and `loop`:
			- `midi.notes`: the notes that start on this step, with MIDI note number, name (60 is C4), velocity, and gate length in clock ticks and in steps. A tick is one MIDI Clock, 24 to a quarter note. `cut_by_stop` marks a note still sounding at Stop.
			- `midi.held`: notes started on an earlier step that still sound when this step starts, as a tie does.
			- `midi.ccs`: the modulation-track values sent on this step, by CC number.
			- `audio`: `onset` (a new note started within 45 ms of the step), `level_db` relative to the loudest moment of the recording, `sounding`, the strongest pitch found by the YIN method (`f0_hz`, `midi`, `cents`, `aperiodicity`), and `chord`, up to four notes from an iterative harmonic-sum estimate, each with its salience.
			- `agreement` compares the two: `match`, `match_in_chord`, `octave`, `mismatch` or `silent` for a single note; `match` (every MIDI note heard) or `partial` for a chord; `rest`, `held` or `unexpected_onset` for a step without a new note. `chord_recall` gives the share of a chord's notes and pitch classes that the audio estimate found.
		- `midi_out.loop_differences` lists steps whose notes or velocities changed between loops. `midi_out.off_grid_notes` counts notes that started between steps, a sign that the step length is wrong. `recording.latency_ms` is the shift that lines the audio onsets up with the clock.
	- ## Selecting a slot
		- Bank select (CC 0) with (slot − 1) // 128, then program change (slot − 1) % 128, on the MicroFreak's MIDI input channel. [[Microfreak/CLI/Upload a preset]] shows the same messages selecting slot 323, and Elektroid and Freakout select presets the same way.
		- No SysEx message is known that reports which preset is selected. [Freakout's note on operation 19](https://github.com/kmorrill/freakout/blob/7e3d8ebeab3d2b41276994111d6a622da16b6a4c/docs/microfreak-sysex.md#why-operation-19-does-not-read-unsaved-current-state) explains that the preset read always returns the saved slot, not the sound being played.
		- Evidence: after selecting slot 35 FM Seq, the notes and velocities on MIDI out matched the 16 step records of its pattern A in the downloaded slot, read at the place Freakout gives for Sequence A: 13 notes and 3 rests.
	- ## Starting the sequencer
		- With Clock Source on USB or Auto, MIDI Start followed by Clock starts the selected pattern. The first step plays on Start, and each later step plays on the Clock that begins it. No held note is needed. With Clock Source on Internal, Start and Clock gave no notes and no sound.
		- Clock Source is global setting 0x2E. Operation 0x43 reads it and operation 0x42 writes it: 0 Internal, 1 USB, 2 MIDI, 3 Clock, 4 Auto. Codes and values come from [Freakout's global-setting table](https://github.com/kmorrill/freakout/blob/7e3d8ebeab3d2b41276994111d6a622da16b6a4c/src/minifreak_patch/microfreak_midi.py#L178-L221) and [value list](https://github.com/kmorrill/freakout/blob/7e3d8ebeab3d2b41276994111d6a622da16b6a4c/src/minifreak_patch/microfreak_global_specs.py#L56-L71). The reply starts `F0 00 20 6B 07 7F`, unlike preset replies, and carries the value after `02 42 <code>`. On this MicroFreak, Clock Source was already USB on [[2026-11-16 Mon]]; setting it to Internal and to Auto and back read back as sent each time.
		- Under USB clock the step length follows the stored division. Slots 5, 35 and 113 store `Arp.Sync` off and `Arp.Div` 7 (1/16) and played one step every 6 clocks; slot 374 stores `Arp.Div` 5 (1/8) and played one every 12. CC 91, the free rate, changed nothing. CC 92, the synced rate, changed the step length: 0 gave 96 clocks, 64 gave 12, 89 gave 6 and 100 gave 4. Those fit the order of divisions in [[Microfreak/UG/12 Arpeggiator/03 Arpeggio Rate]], with CC value = division index × 127 / 10. Every stored division from `1` to `1/32T` played the clocks per step that [[Microfreak/Sequence/Storage]] lists.
		- Leave the keys alone during an audition. With MIDI note 72 held on slot 35, MIDI out still listed the sequence, but every step sounded note 72: an incoming note takes priority over sequence notes ([[Microfreak/UG/13 Sequencer/01 Use]]).
	- ## MIDI out carries the sequence
		- With the global setting Arp/Seq MIDI Out on (code 0x2B, value 1), the MicroFreak sends a Note On and a Note Off for every sequencer note, all notes of a chord included, with the velocity stored in the step. It sends a CC for every modulation-track value. During playback it also sends back each Clock, and Start and Stop.
		- On this MicroFreak the setting is off. With it off, only Clock, Start and Stop come back. The task turns it on for the run and restores it.
		- The task places each message on the step grid by counting the Clocks the MicroFreak sends back. This keeps the instrument's order when USB delivers several messages at once; arrival times alone moved one note-off on slot 35 by three ticks.
		- Slot 35's pattern A stores velocities 9, 24, 25, 18 and so on, and MIDI out sent the same values, although this preset's sound ignores velocity.
		- Ties: slot 113 D3 Chords sends its first chord once and holds it for 1.5 steps; the next step lists those notes under `held`.
	- ## Pattern A and B
		- Selecting a slot loads pattern A. Slot 395 stores notes only in pattern B, and its audition produced no notes and no sound. No CC, program change or SysEx message is known that switches to pattern B; MIDI Song Select 1 (`F3 01`) left pattern A playing. Freakout's notes record that changing the values after pattern A in a saved preset did not select B either.
		- To audition pattern B, select the slot on the panel, press B, and run the task with `--no-select`. Without the panel, write a copy of the preset with B's steps in A's place to a spare slot; [[Microfreak/Sequence/Research]] records this for slot 446.
	- ## Audio analysis
		- The recording is normalized to its peak before analysis. Each step's window starts 12 ms after the step and lasts up to one step or 400 ms. YIN gives the strongest pitch. The chord estimate scores every note from MIDI 24 to 96 by the spectrum at its first 20 harmonics, keeps the best, subtracts a smoothed copy of that note's harmonics, and repeats until a note scores under 35% of the first.
		- MIDI out is the exact record. The audio shows what the instrument sounds, which can differ from the notes it sends: slot 374 sounds every second step an octave below the note on MIDI out, with a clean, periodic tone, so those steps read `octave`.
		- Single notes come out reliably on slots 5, 35 and 374. Chords come out partly: the estimate misses chord notes and adds neighbouring ones, especially with detuned oscillators such as SuperWave. Onsets come out weak for soft attacks and legato, so `onset` can be false on a played step; the pitch comparison does not depend on it.
		- The modulation tracks keep sending their CCs during playback and replace the values `--plain` sent before Start; the report warns about this. On slot 35, whose tracks send CC 12, 13, 23 and 83, `--plain` did not raise agreement.
	- ## Checked on the instrument, 2026-11-16
		- Each run used the defaults (120 BPM, two loops) under the shared hardware lock, with no one at the panel. Reports and recordings stay in the session's scratch folder.
		- [[Microfreak/Preset/005 MotivSeq]]: 64 steps of 1/16, 128 notes on MIDI out, identical in both loops. The audio pitch agreed on all 128 steps.
		- [[Microfreak/Preset/035 FM Seq]]: 16 steps of 1/16 with 3 rests per loop. The audio agreed on 23 of 26 played steps and heard an octave error on the other 3, all C1 or C2 FM bass notes. The 6 rest steps were silent.
		- [[Microfreak/Preset/113 D3 Chords]]: 64 steps of three- and four-note chords with ties, 248 notes on MIDI out. The chord estimate found every note in 28 of the 80 played steps and, on average, 73% of the notes and 84% of the pitch classes.
		- [[Microfreak/Preset/374 TMF.24.12.04.A]]: 16 steps of 1/8, 12 clocks per step, no note between steps. Half the steps agreed and half sounded an octave lower, as described above.
		- [[Microfreak/Preset/395 26.06.25]]: an empty pattern A, so no notes and no sound, as described under pattern A and B.
		- After each run, Arp/Seq MIDI Out read back as off. Clock Source stayed on USB.
