see-also:: [[Microfreak/Sequence/Storage]], [[Microfreak/Sequence/Research]], [[Microfreak/CLI/Audition a sequence]], [[Microfreak/CLI/Upload a preset]], [[Microfreak/UG/13 Sequencer]]

- # Write a sequence into a MicroFreak slot
	- I describe a sequence in words, such as "in slot 483, a 16-step minor arpeggio on A with a rest every fourth step, pattern B the same an octave up, accent the downbeats". These steps put it into a preset on my MicroFreak and check that the instrument plays it as described.
	- Two mise tasks do the work. `mise run microfreak:write-sequence` writes a description file into a preset and uploads it to a slot. `mise run microfreak:verify-sequence` does the same write, then plays the slot, records what the MicroFreak sends over MIDI and what the [[Zoom H5/My Unit]] hears, downloads the slot again, and reports for every step what the description expects, what the instrument sent and what it sounded.
	- ## What you need
		- The MicroFreak connected to the Mac by USB. The Mac lists it as the MIDI port `Arturia MicroFreak` ([[Microfreak/MIDI/Port/Arturia MicroFreak]]).
		- [[Arturia/MCC]] (MIDI Control Center) closed. It talks to the MicroFreak over the same port.
		- The [[Zoom H5/My Unit]] connected by USB and recording the MicroFreak, for the audio check. Without it, add `--no-audio` to `verify-sequence`.
		- [[mise]] and [[uv]] installed. The tasks are mise tasks, and each runs its Python with `uv run`.
		- Hands off the keys while a task runs: a held key takes over from the sequence. One person or agent drives the MicroFreak at a time.
	- ## Steps
		- ### 1. Open a garden checkout on current `main`
			- In a terminal, go to the garden checkout and update it. On my Mac, `ghq list` finds the checkout:
			- ```sh
			  cd "$(ghq list --full-path --exact github.com/codekiln/logseq-encode-garden)"
			  git pull --ff-only
			  ```
			- `git pull` prints `Already up to date.` or the files it updated. A worktree of `origin/main` works too. Each task runs the code of the checkout you start it from, so an older branch runs older code.
			- Run every command below from this folder.
		- ### 2. Make a folder outside the repository
			- The repository is public and the backups hold my presets, so the description, backups, recordings and reports go in a folder outside it. `$TMPDIR` is the Mac's temporary folder for your user:
			- ```sh
			  mkdir -p "$TMPDIR/microfreak-seq"
			  ```
			- `ls -d "$TMPDIR/microfreak-seq"` prints the folder's path once it exists.
		- ### 3. Write the request as a description file
			- A description lists the sequence step by step. Write it in a text editor and save it as `$TMPDIR/microfreak-seq/seq.yaml`. The task reads a file ending `.yaml` or `.yml` as YAML and any other file as JSON.
			- This description plays A3, C4, a rest, then an A minor chord, and loops every four steps:
			- ```yaml
			  name: First Seq
			  category: Sequence
			  length: 4
			  patterns:
			    A:
			      steps:
			        - {notes: [A3]}
			        - {notes: [C4]}
			        - {}
			        - {notes: [A3, C4, E4]}
			    B: {steps: []}
			  ```
			- `name`: the name the MicroFreak shows for the preset, up to 14 characters.
			- `category`: the preset's category, such as Sequence, Bass or Lead.
			- `length`: how many steps play before the pattern starts again, 1 to 64.
			- `patterns`: the MicroFreak's two patterns, `A` and `B`. Selecting a slot plays pattern A.
			- `steps`: one entry per step, in order from step 1. With slot 358 as the base, each step is a sixteenth note.
			- `notes`: the notes a step plays, by name. Middle C is C4. Two to four notes in one step make a chord.
			- `{}`: a rest. The step starts no note.
			- `B: {steps: []}`: pattern B is empty.
			- Each note plays at velocity 100 unless its step gives a `velocity`. For every key, including velocity, ties and modulation tracks, see Description keys below. To turn the words of a request into steps, see Read musical words, and for one example of each kind of request, see Worked examples.
			- To change a sequence a slot already holds, follow Change a sequence already in a slot, below, to save the slot's current sequence as your description file.
		- ### 4. Pick the slot and the base
			- Use the slot I name. My own presets fill slots 1–320 and 350–402; write to one of those only when I name it.
			- When I name no slot, pick an empty one and tell me which. `microfreak:empty-slots` reads every slot's header and changes nothing:
			- ```sh
			  mise run microfreak:empty-slots
			  ```
			- After about five seconds it prints the empty slots as ranges, such as `{"slots_read": "1-512", "empty_count": 94, "empty": ["325-329", "340-349", "383", "403-430", "447-480", "497-512"]}`. `--first` and `--last` read part of the range.
			- The base gives the sound. The new preset keeps every setting of the base except the ones under What the write changes, below. Pass `--base` a slot number, which the task reads and leaves unchanged, or a `.bin` file from `microfreak:download`; with a file, the preview needs no instrument.
			- Use the base I name. Otherwise use slot 358, [[Microfreak/Preset/358 20241116.1]]: Basic Waves, paraphony on, no glide or pitch modulation, one step per sixteenth. Every check behind this page used it. A base whose pitch moves still stores and sends the right notes, but the audio check reads them off pitch: with [[Microfreak/Preset/382 Anit]] as the base, held notes read a semitone sharp. A base whose Scale is set ([[Microfreak/Patch/Storage]]) sounds each note outside the scale as a scale note, while MIDI out still sends the stored note.
		- ### 5. Preview
			- Without `--slot`, `write-sequence` reads the base, prints what it would store and changes nothing:
			- ```sh
			  mise run microfreak:write-sequence "$TMPDIR/microfreak-seq/seq.yaml" --base 358
			  ```
			- It prints one JSON report. `sequence` shows the steps as the preset would store them, and `"differences": []` near the end means the stored sequence matches the description. If `differences` names a step, or the task prints a line starting `error:`, fix the description and preview again.
		- ### 6. Write, play and check
			- Put your slot number after `--slot`:
			- ```sh
			  mise run microfreak:verify-sequence "$TMPDIR/microfreak-seq/seq.yaml" --base 358 --slot 483 \
			    --backup-dir "$TMPDIR/microfreak-seq/backup-1" --out-dir "$TMPDIR/microfreak-seq/verify"
			  ```
			- The task writes the slot, plays the pattern twice at 120 BPM while it records, downloads the slot again and compares every step. By default you hear the pattern in a plain square-wave sound; add `--preset-sound` to hear it with the preset's own sound. It prints a summary and one line per played step, and saves the full report and the recording in `--out-dir`. Afterwards the slot stays selected with its own sound, and the sequencer is stopped.
			- `echo $?` right after the run prints `0` when MIDI out and the downloaded slot both match the description.
			- When the slot holds a preset, the task saves it in `--backup-dir` first as `slot-NNN.bin`, then writes. Without `--backup-dir` it refuses to write over a preset. It also stops when the folder already holds a backup of that slot, so each rewrite of a slot, your own earlier write included, needs a new folder: `backup-2`, `backup-3` and so on. macOS clears old files out of `$TMPDIR`, so copy a backup you want to keep to a lasting folder outside the repository.
			- `mise run microfreak:upload BACKUP.bin --slot N --backup-dir NEW_FOLDER` puts a backup back, as [[Microfreak/CLI/Upload a preset]] describes.
		- ### 7. Read the report
			- From a run of the arpeggio example in slot 500 with `--preset-sound`:
			- ```text
			  "sound": "preset",
			  "played_at": "1/16 steps, 6 clocks per step, 120.0 BPM",
			  "summary": {
			    "played_steps": 32,
			    "midi_out_matching_steps": 32,
			    "midi_out_mismatches": [],
			    "audio_checks": {"match": 8, "match_in_chord": 12, "rest": 8, "octave": 4},
			    "levels_db": {
			      "A3/127": -6.8,
			      "C4/80": -8.8,
			      "E4/80": -8.7,
			      "A4/127": -6.7,
			      "C5/80": -8.8,
			      "E5/80": -8.9,
			      "A5/127": -6.8
			    },
			    "download_matches_description": true,
			    "download_differences": [],
			    "download_equals_upload": true
			  },
			  "steps": [
			    "1.01 expected [A3/127] midi [A3/127] ok audio [A3; A3] -6.8 dB match",
			    "1.02 expected [C4/80] midi [C4/80] ok audio [F1; A3 C4] -8.5 dB match_in_chord",
			    "1.04 expected [rest] midi [rest] ok audio [C2; C4 E4] -17.2 dB rest",
			  ```
			- A step line gives the loop and step (`1.04` is loop 1, step 4), the notes the description expects with their velocities, the notes MIDI out carried, `ok` or `DIFFERS`, then the pitch the audio heard, a chord estimate, the step's level and the audio check. `ok` means that the notes, velocities, held notes and modulation CCs all matched.
			- The run passed when the exit status is 0: `midi_out_mismatches` is empty and `download_matches_description` is true. `download_equals_upload` true says the slot still holds what was sent.
			- MIDI out records every note the sequencer played. The audio check confirms that the instrument sounded: `match`, `rest` and `held` agree with the description. `rest` means that no new note started; the level shows whether the step was silent. `octave`, `mismatch` or `silent` on a step whose MIDI reads `ok` comes from the sound, such as a modulation track that closes the filter or a base whose pitch moves. Chords often read `partial`, because the chord estimate misses notes; [[Microfreak/CLI/Audition a sequence]] explains the audio labels.
			- Levels are in dB below the loudest moment of the recording. `levels_db` gives the mean level of the steps that start each note at each velocity. A level is measured over its step, so a note that sounds for more of its step, such as the first step of a tie, reads louder; compare steps with the same gate and ties.
			- The check plays pattern A, as Pattern B, below, explains, and `played_at` gives the division it played. The plain sound has the shortest release, so each pitch reads cleanly and every rest reads silent. Use `--preset-sound` to check accents, rests and releases with the preset's own sound. With it, a note's release carries into the next step, so the audio also hears the previous note and the strongest pitch can miss the new one: those steps read `match_in_chord`, as above.
			- A step marked `DIFFERS`: make sure nobody touched the keys and no other program sent MIDI, then run `verify-sequence` again without `--base`, which plays and checks the slot as it is. A line in `download_differences` names a step the slot stores differently from the description; fix the description and write again.
		- ### 8. Tell me what the slot holds
			- Give me the slot number and the name it shows, the base whose sound it uses, the step length when it is other than a sixteenth, each pattern as notes step by step, the choices you made where my request left one open, the verify result, where any backup is, and how to hear pattern B. For the arpeggio example:
			- > Slot 483 now holds A min Arp (Sequence), with the sound of slot 358, 20241116.1. Pattern A, 16 steps: A3 C4 E4 rest, A4 C5 E5 rest, A5 E5 C5 rest, A4 E4 C4 rest. Pattern B is the same an octave up. The downbeats, steps 1, 5, 9 and 13, have velocity 127 and the other notes 80, and Velo Amp Mod is 10 so the accents sound louder. I chose the climb over two octaves and back. verify-sequence: MIDI out matched all 32 played steps of pattern A, the recording heard 24 notes and 8 rests as written, and a fresh download holds both patterns. The slot was empty, so there is no backup. To hear B, select 483 and press B.
	- ## Read musical words
		- Read my requests this way unless I say otherwise:
			- A step is a sixteenth note. Slot 358 stores `division: 1/16`, so 4 steps make a beat and 16 steps a bar of 4/4. `division` sets another step length.
			- "Eighth notes" can mean one step at `division: 1/8`, or two sixteenth steps: the note with `tie: true`, then the same note. Choose this way:
				- The request numbers its steps: keep its numbers. Eighth notes that start on every second step (1, 3, 5 …) take two sixteenth steps each. Eighth notes on consecutive steps make every step an eighth: `division: 1/8`.
				- No step numbers, and no note shorter than an eighth: `division: 1/8`, one step per eighth note, 8 steps to a bar. Worked examples has one.
				- No step numbers, and sixteenths as well: keep 1/16 and tie each eighth note over two steps.
				- The two readings sound for different lengths at the same gate. At 50%, two tied sixteenths sound for 1.5 sixteenths and one 1/8 step for 1 sixteenth. For 1/8 notes that fill their step, raise `gate_percent`.
			- Downbeats are the first step of each beat: steps 1, 5, 9 and 13 of a 16-step bar. "Every fourth step" is steps 4, 8, 12 and 16.
			- An accent is velocity 127 on the accented steps, with `velo_amp_mod: 10` so that velocity changes loudness. Slot 358 stores Velo Amp Mod 0, which plays every velocity at the same level.
				- Every other note gets velocity 80, in both patterns, including a pattern with no accents of its own.
				- A tie continuation, the step that repeats a tied note, takes the velocity of the step it continues. It starts no note, so its velocity is not heard.
				- An accent instruction applies to the patterns it names, and to both when it names none. "Pattern B the same an octave up" copies A's velocities with its notes.
				- On slot 358's sound, velocity 127 played 3.5–3.7 dB louder than 80 on E2, E3, A3 and A4 when rests separated the notes. Where each note follows the last, the previous note's release adds to every step and the difference measures smaller: 1.0–1.2 dB on E2 in the slot 490 bass line, E Octave Bass.
			- Middle C, MIDI note 60, is C4. When the request names no octave, start the root in octave 3: A3 is MIDI 57.
			- An arpeggio plays the chord's notes from the root upward. To fill a longer pattern, continue an octave higher, then come back down.
			- "Held", "tied" or "sustained over" several steps is a tie: `tie: true` on every step but the last, with the same notes on each.
			- A note tied into a different note, such as "C4 tied into D4": `tie: true` on the C4 step and D4 on the next step. C4 then sounds for its whole step, whatever the gate length, and D4 starts on its own step with a new note. Worked examples has one.
			- A rest, `{}`, starts no note. The step is silent only once the previous note's release has ended: on slot 358's sound the release sounded through the rest step, 8 dB below the note. The release belongs to the base's sound, which the description leaves as it is. `verify-sequence --preset-sound` shows it in the rest step's level.
			- "The same an octave up" adds 12 to every note: A3 becomes A4.
			- Short or staccato notes: `gate_percent: 25`. Long or legato notes: `gate_percent: 90`. One gate length applies to every step of both patterns.
			- A pattern the request does not mention gets `steps: []`, which erases it. A pattern left out of the description keeps the base's steps, and slot 358's pattern A holds my own chords.
			- The description has no tempo. `verify-sequence --bpm` sets the tempo of the check only.
		- When my request leaves a choice open, make the choice and tell me which one you made.
	- ## Description keys
		- `name`: 1–14 letters, digits, spaces, periods, underscores or hyphens. `category`: Bass, Brass, Keys, Lead, Organ, Pad, Percussion, Sequence, SFX, Strings, Template or Vocoder. Without them the base's name and category stay. `--name` and `--category` on the command line override both.
		- `length`: the number of steps, 1–64, shared by both patterns. Steps after the last one listed are rests. The instrument's shortest length is 4, so a 1–3 step loop is stored repeated, 1 and 2 steps as 4 and 3 steps as 6, which plays the same; the report's `stored_as` says so.
		- `division`: the length of a step, shared by both patterns: `1`, `1/2`, `1/2T`, `1/4`, `1/4T`, `1/8`, `1/8T`, `1/16`, `1/16T`, `1/32` or `1/32T`, where `T` is a triplet. Each was written to a slot and played; [[Microfreak/Sequence/Storage]] lists the clocks per step. `verify-sequence` plays at the stored division and prints it as `played_at`.
		- `gate_percent`: 10–90. `smoothing`: four booleans, one per modulation track. `velo_amp_mod`: 0–10, how much velocity changes loudness, which the panel shows as Velo Amp Mod in Utility > Preset. Each is optional; the base's value stays when it is left out.
		- `patterns`: `A` and `B`, each with `steps`, a list of up to 64 steps, and optional `mod_tracks`.
		- A step has `notes`, up to four, by name (C4, F#3, Eb2) or MIDI number; `velocity`, 1–127, one value or one per note, default 100; `tie: true`, which holds the notes into the next step; and `mod`, four values 0–255 or `null`, one per modulation track. `{}` is a rest.
		- `mod_tracks` gives each modulation track's destination id, or `null`. [[Microfreak/Preset/005 MotivSeq]] and [[Microfreak/Preset/035 FM Seq]] use `"0x0101"` VCF.Cutoff, `"0x0102"` VCF.Reso, `"0x0602"` EG2.DecRel (envelope decay), `"0x0003"` VCO.Param2 and `"0x0005"` VCO.Param3. With smoothing off, a track on `"0x0101"` sends CC 23 at half the stored value, and values near 0 close the filter and silence the note. To find the id of another control, download a preset whose modulation track moves it and read `mod_tracks` in `mise run microfreak:inspect FILE --sequence`.
		- [[Microfreak/Sequence/Storage]] describes how each key is stored.
	- ## Worked examples
		- Each example passed the preview against slot 358 with `differences` empty. The eighth-note and tie examples also passed `verify-sequence` in slots 497 and 498.
		- ### Arpeggio with rests, accents, and pattern B an octave up
			- "In slot 483, a 16-step minor arpeggio on A with a rest every fourth step, pattern B the same an octave up, accent the downbeats." The arpeggio climbs over two octaves and comes back down:
			- ```yaml
			  name: A min Arp
			  category: Sequence
			  length: 16
			  velo_amp_mod: 10
			  patterns:
			    A:
			      steps:
			        - {notes: [A3], velocity: 127}
			        - {notes: [C4], velocity: 80}
			        - {notes: [E4], velocity: 80}
			        - {}
			        - {notes: [A4], velocity: 127}
			        - {notes: [C5], velocity: 80}
			        - {notes: [E5], velocity: 80}
			        - {}
			        - {notes: [A5], velocity: 127}
			        - {notes: [E5], velocity: 80}
			        - {notes: [C5], velocity: 80}
			        - {}
			        - {notes: [A4], velocity: 127}
			        - {notes: [E4], velocity: 80}
			        - {notes: [C4], velocity: 80}
			        - {}
			    B:
			      steps:
			        - {notes: [A4], velocity: 127}
			        - {notes: [C5], velocity: 80}
			        - {notes: [E5], velocity: 80}
			        - {}
			        - {notes: [A5], velocity: 127}
			        - {notes: [C6], velocity: 80}
			        - {notes: [E6], velocity: 80}
			        - {}
			        - {notes: [A6], velocity: 127}
			        - {notes: [E6], velocity: 80}
			        - {notes: [C6], velocity: 80}
			        - {}
			        - {notes: [A5], velocity: 127}
			        - {notes: [E5], velocity: 80}
			        - {notes: [C5], velocity: 80}
			        - {}
			  ```
		- ### Scale with a held note
			- "A C major scale from C4 up to C5, then hold the C5 for four more steps." C5 sounds from step 8 through step 12:
			- ```yaml
			  name: C Maj Climb
			  length: 12
			  patterns:
			    A:
			      steps:
			        - {notes: [C4]}
			        - {notes: [D4]}
			        - {notes: [E4]}
			        - {notes: [F4]}
			        - {notes: [G4]}
			        - {notes: [A4]}
			        - {notes: [B4]}
			        - {notes: [C5], tie: true}
			        - {notes: [C5], tie: true}
			        - {notes: [C5], tie: true}
			        - {notes: [C5], tie: true}
			        - {notes: [C5]}
			    B: {steps: []}
			  ```
		- ### Eighth notes
			- "A bar of eighth notes: E2 E2 G2 E2 A2 G2 E2 D2." Every note is an eighth and the request numbers no steps, so each step is an eighth note. At slot 358's 50% gate each note sounds for a sixteenth:
			- ```yaml
			  name: Eighth Bass
			  category: Bass
			  length: 8
			  division: 1/8
			  patterns:
			    A:
			      steps:
			        - {notes: [E2]}
			        - {notes: [E2]}
			        - {notes: [G2]}
			        - {notes: [E2]}
			        - {notes: [A2]}
			        - {notes: [G2]}
			        - {notes: [E2]}
			        - {notes: [D2]}
			    B: {steps: []}
			  ```
			- "An eighth-note E2, then sixteenths G2 and A2" mixes note values, so it keeps 1/16 and ties the eighth: `{notes: [E2], tie: true}`, `{notes: [E2]}`, `{notes: [G2]}`, `{notes: [A2]}`.
		- ### Tie into a different note
			- "C4 tied into D4, then E4 and G4." C4 sounds for all of step 1 and D4 starts on step 2 with its own note:
			- ```yaml
			  name: Tie Into D4
			  length: 4
			  patterns:
			    A:
			      steps:
			        - {notes: [C4], tie: true}
			        - {notes: [D4]}
			        - {notes: [E4]}
			        - {notes: [G4]}
			    B: {steps: []}
			  ```
		- ### Chords
			- "Am, F, C, G, one bar each." Each chord is held over four steps. A step with more than one note turns paraphony on:
			- ```yaml
			  name: Am F C G
			  length: 16
			  patterns:
			    A:
			      steps:
			        - {notes: [A3, C4, E4], tie: true}
			        - {notes: [A3, C4, E4], tie: true}
			        - {notes: [A3, C4, E4], tie: true}
			        - {notes: [A3, C4, E4]}
			        - {notes: [F3, A3, C4], tie: true}
			        - {notes: [F3, A3, C4], tie: true}
			        - {notes: [F3, A3, C4], tie: true}
			        - {notes: [F3, A3, C4]}
			        - {notes: [C4, E4, G4], tie: true}
			        - {notes: [C4, E4, G4], tie: true}
			        - {notes: [C4, E4, G4], tie: true}
			        - {notes: [C4, E4, G4]}
			        - {notes: [G3, B3, D4], tie: true}
			        - {notes: [G3, B3, D4], tie: true}
			        - {notes: [G3, B3, D4], tie: true}
			        - {notes: [G3, B3, D4]}
			    B: {steps: []}
			  ```
		- ### Modulation track
			- "An 8-step bass line on E2 with the filter opening across the pattern." Track 1 moves the filter cutoff, starting at 60 so the first note sounds:
			- ```yaml
			  name: E Bass Sweep
			  length: 8
			  patterns:
			    A:
			      mod_tracks: ["0x0101", null, null, null]
			      steps:
			        - {notes: [E2], mod: [60, null, null, null]}
			        - {notes: [E2], mod: [88, null, null, null]}
			        - {notes: [E3], mod: [116, null, null, null]}
			        - {notes: [E2], mod: [144, null, null, null]}
			        - {notes: [E2], mod: [172, null, null, null]}
			        - {notes: [G2], mod: [200, null, null, null]}
			        - {notes: [E2], mod: [228, null, null, null]}
			        - {notes: [D3], mod: [255, null, null, null]}
			    B: {steps: []}
			  ```
		- ### Short loop
			- "C4, E4, G4, looping." The 3-step loop is stored as 6 steps, C4 E4 G4 C4 E4 G4:
			- ```yaml
			  name: Three Note
			  length: 3
			  patterns:
			    A:
			      steps:
			        - {notes: [C4]}
			        - {notes: [E4]}
			        - {notes: [G4]}
			    B: {steps: []}
			  ```
		- ### 64 steps
			- "64 steps of the C minor pentatonic scale, up two octaves and back down, with a rest every eighth step." A short script writes the 64 entries:
			- ```sh
			  python3 - <<'EOF' > "$TMPDIR/microfreak-seq/pent64.json"
			  import json
			  notes = ['C3', 'Eb3', 'F3', 'G3', 'Bb3', 'C4', 'Eb4', 'F4', 'G4', 'Bb4', 'C5']
			  walk = notes + notes[-2:0:-1]              # up two octaves and back down: 20 steps
			  steps = [{'notes': [walk[i % len(walk)]]} for i in range(64)]
			  for i in range(7, 64, 8):
			      steps[i] = {}                          # a rest on every eighth step
			  print(json.dumps({'name': 'Pent 64', 'length': 64,
			                    'patterns': {'A': {'steps': steps}, 'B': {'steps': []}}}))
			  EOF
			  ```
	- ## Change a sequence already in a slot
		- An empty description changes nothing, so previewing it prints the slot's current sequence in the description format. Save that as the file to edit:
			- ```sh
			  echo '{}' > "$TMPDIR/microfreak-seq/empty.json"
			  mise run microfreak:write-sequence "$TMPDIR/microfreak-seq/empty.json" --base N \
			    | python3 -c 'import json, sys; print(json.dumps(json.load(sys.stdin)["sequence"], indent=1))' \
			    > "$TMPDIR/microfreak-seq/seq.json"
			  ```
		- Edit the steps in `seq.json`, preview it with `--base N`, then run `verify-sequence` with `--base N --slot N` and a new `--backup-dir`. The preset keeps everything else slot N held. A pattern listed in the file replaces all of that pattern's steps, so keep both patterns in the file.
	- ## Pattern B
		- The write stores pattern B, and `download_matches_description` compares it. Only the panel switches to B: selecting a slot loads pattern A, and no MIDI or SysEx message found so far switches to B. [[Microfreak/Sequence/Research]] lists what was tried.
		- To hear B, select the slot and press the B icon in the sequencer row ([[Microfreak/UI/Front/Row/04 Icon Strip/Button/Order B]]), or ask me to when you aren't at the MicroFreak. The display shows Sequence B Loaded. The preset loads with the sequencer on; if the icon strip shows the arpeggiator instead, hold Shift and press Arp | Seq first.
		- After that press, `mise run microfreak:audition --slot N --no-select` plays the loaded pattern without a program change, and `mise run microfreak:verify-sequence seq.yaml --slot N --pattern B --keep-selection --out-dir DIR` compares it with the description step by step.
	- ## What the write changes
		- The steps, modulation-track destinations and in-use marker of each pattern the description lists. A pattern with no notes or modulation values is marked erased.
		- `Seq.Length`; and `Arp.Div` (division), `Seq.GateLen`, `Seq.Smooth1`–`Seq.Smooth4` and `Kbd.PresAmp` (Velo Amp Mod) when the description gives them.
		- `Arp.SeqOn` on, so the preset starts in sequencer mode.
		- `Gen.Parafon` (paraphony) on when a step holds more than one note. With paraphony off, the sequencer sounds only the lowest note of a step.
		- `write-sequence` prints one JSON report: `settings_changed` with each changed setting's old and new value, `sequence` decoded again from the new preset in the description format, `differences` between that and the description, and under `upload` the slot, what it held before (`was`), any backup file and whether the read-back matched. It exits with status 1 when it refuses to write or finds a difference. `verify-sequence` saves the same under `write` in its full report.
		- `--output new.bin` also saves the result as a file in `microfreak:download`'s format.
		- Uploading leaves the sound being played alone. Select the slot on the panel, or over MIDI as in [[Microfreak/CLI/Upload a preset]], to hear it; `verify-sequence` leaves it selected.
	- ## Source
		- [[Microfreak/Sequence/Research]] lists the runs on the instrument behind this page.
		- [#436 Write a described sequence into a MicroFreak preset and verify it on the instrument](https://github.com/codekiln/logseq-encode-garden/issues/436) added both tasks.
