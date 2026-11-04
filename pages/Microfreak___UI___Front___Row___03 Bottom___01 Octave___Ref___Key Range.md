logseq-entity:: [[Logseq/Entity/Diataxis/Reference]]
tags:: [[Diataxis/Reference]]
up:: [[Microfreak/UI/Front/Row/03 Bottom/01 Octave]]
see-also:: [[Music/Concept/Scientific Pitch Notation]], [[Microfreak/UI/Front/Row/05 Keys]]

- # Octave key range reference
	- The notes the MicroFreak's 25 keys send at each octave shift, from -3 to +3, as the [[Microfreak/UI/Front/Row/01 Top/04 OLED]] shows it. Note names follow [[Music/Concept/Scientific Pitch Notation]], where MIDI note 60 is C4, middle C. MIDI note numbers are in parentheses.
	- ## When the OLED shows -1
		- The lowest key sends C2 (36), the C in the middle of the keyboard sends C3 (48), and the highest key sends C4 (60), middle C.
		- Arturia's manual and [[Ableton/Live]] name the same three notes C1, C2 and C3.
	- ## Every octave
		- The center key is the C in the middle of the keyboard, the 13th key from the left.
		- | OLED | Lowest key | Center key | Highest key | Arturia and Ableton names |
		  |------|------------|------------|-------------|---------------------------|
		  | -3 | C0 (12) | C1 (24) | C2 (36) | C−1, C0, C1 |
		  | -2 | C1 (24) | C2 (36) | C3 (48) | C0, C1, C2 |
		  | **-1** | **C2 (36)** | **C3 (48)** | **C4 (60)** | **C1, C2, C3** |
		  | 0 | C3 (48) | C4 (60) | C5 (72) | C2, C3, C4 |
		  | +1 | C4 (60) | C5 (72) | C6 (84) | C3, C4, C5 |
		  | +2 | C5 (72) | C6 (84) | C7 (96) | C4, C5, C6 |
		  | +3 | C6 (84) | C7 (96) | C8 (108) | C5, C6, C7 |
	- ## Arturia and Ableton octave numbers
		- Arturia's manual and Ableton Live name MIDI note 60 C3, so each of their octave numbers is one below scientific pitch notation. The MicroFreak 5.0 manual gives the full MIDI range, notes 0 to 127, as C−2 to G8 in [[Microfreak/UG/06 Dig Osc/01 as Soundgen]].
	- ## Sources
		- [[Microfreak/UG/10 Keyboard/04 Octave Buttons]] — the buttons shift the keys up to three octaves either way, and the keys reach eight octaves in all.
		- [MicroFreak user manual 1.0, section 6.1, The oscillator as a sound generator](https://downloads.arturia.net/products/microfreak/manual/MicroFreak_Manual_1_0_0_EN.pdf) — gives the range the shifted keys reach as C−1 to C7 in Arturia's names, MIDI 12 to 108. The lowest key at -3 is C−1, the highest key at +3 is C7, and octave 0 sits three octaves in from each end, at C2 to C4 in Arturia's names.
		- [[Microfreak/UG/06 Dig Osc/01 as Soundgen]] — the 5.0 manual's C−2 to G8 for MIDI 0 to 127 shows that Arturia names MIDI 60 C3.
	- ## Recorded sessions
		- [[GitP/A/Session/26/11/01-Sun]] at 05:15 — [[Microfreak/Preset/259 Infini Pad]] with the OLED at -2, as codekiln noted. The keys send G1 (31) and F1 (29), inside the -2 row.
		- [[GitP/A/Session/26/10/29-Thu]] at 10:32 — [[Microfreak/Preset/138 Metallic Talk]], saved at -2, opens on the keys with G1 (31) and F1 (29), inside the -2 row.
		- [[GitP/A/Session/26/11/01-Sun]] at 18:22 — [[Microfreak/Preset/260 8bitfi]], saved at +2, opens with C6 to E6 (84 to 88), inside the +2 row.
		- [[GitP/A/Session/26/11/01-Sun]] at 01:59 — Infini Pad, saved at 0, plays G5 to C6 (79 to 84), which sits in the +1 row. An Octave Up press before 01:59 would account for it; the MIDI does not record octave button presses.
	- ## Uncertainty
		- Arturia publishes no note number for any single key. The table reads the 1.0 manual's C−1 to C7 in the naming the 5.0 manual uses.
		- The recordings agree with the table. A range one octave higher puts G1 and F1 outside the -2 row at 05:15. A range one octave lower puts 8bitfi's opening D♯6 and E6 outside its saved +2 row.
		- A MIDI monitor settles it: at octave 0 the lowest key should send note 48.
