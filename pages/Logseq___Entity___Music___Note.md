logseq-entity:: [[Logseq/Entity/Definition]]
see-also:: [[Music/Concept/Scientific Pitch Notation]], [[Music/Note]]

- # Music Note
	- In this garden, **Music Note** pages model one pitch at one octave, such as G8, with a page for each MIDI note number from 0 to 127.
	- ## What counts
		- A pitch at a fixed octave in twelve-tone equal temperament. G7 and G8 are two notes with two pages.
		- A pitch class without an octave, such as the F of an F-minor chord, stays plain text. Scales have pages of their own under [[Logseq/Entity/Music/Scale]].
	- ## Naming and placement
		- A note lives at `Music/Note/<octave>/<letter>` under [[Music/Note]], named in [[Music/Concept/Scientific Pitch Notation]]. MIDI note 60 is [[Music/Note/4/C]], middle C.
		- A black key takes its sharp spelling, written with `♯`: [[Music/Note/4/C♯]]. The page body gives the flat spelling.
		- The lowest octave is `-1`. MIDI note 0 is [[Music/Note/-1/C]].
	- ## Alias — the note name
		- Every instance takes its letter and octave as its `alias::`, so `[[G8]]` links [[Music/Note/8/G]] and `[[C♯4]]` links [[Music/Note/4/C♯]].
	- ## Names from Ableton Live and Arturia
		- [[Ableton/Live]] and Arturia's MicroFreak manual name MIDI note 60 C3, so their octave numbers run one lower. Add one to their octave number before linking a note: a drum pad Live labels D♯2 is [[D♯3]].
		- [[Microfreak/UI/Front/Row/03 Bottom/01 Octave/Ref/Key Range]] gives the MicroFreak's keys in both namings at each octave shift.
	- ## Frontmatter
		- The page carries `logseq-entity:: [[Logseq/Entity/Music/Note]]` and the `alias::` above.
		- [[Logseq/Entity/Music/Note/Frontmatter/midi-note]] records the MIDI note number.
		- `prev::` and `next::` link the notes a semitone below and above.
	- ## Page shape
		- One H1 with the note name, then one line giving the MIDI note number, the frequency at A440, the flat spelling of a black key, and the name Live and Arturia use.
	- ## Examples
		- [[Music/Note/4/A]], the 440 Hz tuning note. [[Music/Note/7/G]], the low-battery chirp of [[Microfreak/Preset/399 FireAlarmLoBat]]. [[Music/Note/9/G]], MIDI note 127, the top of the range.
