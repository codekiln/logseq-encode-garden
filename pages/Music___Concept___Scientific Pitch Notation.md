logseq-entity:: [[Logseq/Entity/Concept]]
tags:: [[Diataxis/Concept]]
alias:: [[Scientific Pitch Notation]], [[American Standard Pitch Notation]]
see-also:: [[Microfreak/UI/Front/Row/03 Bottom/01 Octave/Ref/Key Range]], [[Ableton/Live/UG]]

- # Scientific pitch notation
	- ## Overview
		- Scientific pitch notation names a pitch with a letter and an octave number: C4, G1, F♯5. The letter names the note, and the number says which octave of the whole audible range it sits in.
		- Middle C is C4, about 261.63 Hz. The A above it, A4, is the 440 Hz tuning note.
		- It is also called American standard pitch notation (ASPN) and international pitch notation (IPN).
	- ## How the octave number counts
		- The number goes up by one at each C. B3 is the note just below C4, and every note from C4 up through B4 carries the 4.
		- Each octave doubles the frequency: C3 is about 130.81 Hz, C4 about 261.63 Hz, C5 about 523.25 Hz.
		- An 88-key piano runs from A0 (27.5 Hz) to C8 (about 4186 Hz).
		- So a "low G" can be any of several notes. G1 (49 Hz) is a deep bass note near the bottom of a bass guitar's range; G3 (196 Hz) sits just below middle C.
	- ## MIDI note numbers
		- MIDI sends a note as a number from 0 to 127 and leaves naming to the software. In scientific pitch notation, note 60 is C4, note 69 is A4, note 0 is C−1 and note 127 is G9.
		- Note number = 12 × (octave + 1) + semitones above C. G1 is 12 × 2 + 7 = 31, and F1 is 12 × 2 + 5 = 29.
		- The frequency of note m at A440 tuning is 440 × 2^((m − 69) / 12) Hz.
		- A note number carries no sharp or flat spelling. MIDI note 34 is both A♯1 and B♭1; the musical key decides which name to write.
	- ## Ableton and Arturia number octaves one lower
		- [[Ableton/Live]] labels MIDI note 60 as C3, so every note name in Live's piano roll has an octave number one below scientific pitch notation.
		- Arturia's MicroFreak manual counts the same way. [[Microfreak/UI/Front/Row/03 Bottom/01 Octave/Ref/Key Range]] gives the MicroFreak's keys in both namings at each octave shift.
		- The bass notes that open the 05:12 chapter of [[GitP/A/Session/26/11/01-Sun]] are G1 and F1 in scientific pitch notation. Live's piano roll shows the same notes as G0 and F0.
		- To compare a note name from any app or synth with one written here, find out what that app calls MIDI note 60. If it says C3, add one to its octave number.
	- ## Helmholtz notation
		- Older scores and organ writing use Helmholtz notation, which marks octaves with letter case and prime marks. Middle C is c′, the C below it is c, and the C below that is C.
	- ## Sources
		- [Scientific pitch notation, Wikipedia](https://en.wikipedia.org/wiki/Scientific_pitch_notation)
