logseq-entity:: [[Logseq/Entity/Term]]

- # MIDI Note
	- The pair of [[MIDI/Message]] types that start and end a note: **Note On** (90h–9Fh) and **Note Off** (80h–8Fh). Each carries a note number and a velocity, both 0–127.
	- The note number picks the pitch. 60 is middle C, [[Music/Note/4/C]], and each step is a semitone. Note pages in this garden record it as [[Logseq/Entity/Music/Note/Frontmatter/midi-note]].
	- Velocity is how hard the key was struck. A Note On with velocity 0 counts as a Note Off, and some devices send it in place of one, as the Launchpad Pro MK3 does ([[Launchpad/PRG/03 MIDI]]).
	- A receiver pairs each Note Off with the last Note On for the same note number on the same channel. A lost Note Off leaves a stuck note, which All Notes Off ([[MIDI/CC]] 123) clears.
	- Notes can trigger more than pitches. Live can map a note to a button or switch ([[Ableton/Live/UG/34 MIDI and Key Remote/02 The Mapping Browser/02 Mapping to MIDI Notes]]).
