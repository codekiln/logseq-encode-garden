logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/30 MIDI Effect Reference]]
prev:: [[Ableton/Live/UG/30 MIDI Effect Reference/06 Random]]
next:: [[Ableton/Live/UG/30 MIDI Effect Reference/08 Velocity]]
- # [30.7 Scale](https://www.ableton.com/en/live-manual/12/live-midi-effect-reference/#scale)
	- ![The Scale Effect](https://ableton-production.imgix.net/live-manual/12/ScaleL12.png?auto=&w=320)
	- Scale remaps each incoming note to an outgoing note through a matrix, so every C can become a D, for example.
	- The **Note Matrix** is a 13 × 13 grid: columns are incoming notes in an octave, rows are outgoing notes. Black squares match the keyboard's black keys. Highlighted squares show the mapping, starting from the root in the bottom left.
	- **Base** sets the root and **Scale Name** the scale. **Use Current Scale** in the title bar takes both from the clip and disables those choosers.
	- Choosing **User** in Scale Name allows a custom mapping: drag highlighted squares to move them or click to delete them. A removed note is never output.
	- **Transpose** shifts notes by up to ±36 semitones; +7 st moves a C major melody to G major.
	- **Fold**, with User selected, folds any note mapped more than six semitones away back toward the original: a C3 mapped to A3 plays A2 instead.
	- **Lowest** and **Range** limit which notes are remapped (and transposed); notes outside pass unchanged. Lowest C2 with Range +36 affects only C2 to B4.