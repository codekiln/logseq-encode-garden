logseq-entity:: [[Logseq/Entity/Launchpad/Custom/Mode]]
launchpad-custom-mode-url:: https://components.novationmusic.com/launchpad-pro-mk3/custom-modes/795139

- # 3 MF Number Pad
	- [[Launchpad]] Custom Mode for keying in a [[Microfreak]] preset slot number, which [[Launchpad/Idea/Pick-MicroFreak-Presets-through-Live/Asset/Device/MF-Number-Pad/amxd]] turns into a bank select and Program Change.
	- Twelve pads in rows 3 to 6 and columns 3 to 5 form a calculator layout. Every other pad and all edge buttons have nothing assigned.
	- ## Pads
		- Every pad is a Momentary Midi Note on channel 16. Components names notes with C3 as note 60.
		- ~~~
		  pad          note
		  7  8  9      67 68 69
		  4  5  6      64 65 66
		  1  2  3      61 62 63
		  C  0  E      70 60 71
		  ~~~
		- | Pad | Row, column | Note | Colour |
		  |---|---|---|---|
		  | 7 | 3, 3 | 67 (G3) | white |
		  | 8 | 3, 4 | 68 (G#3) | white |
		  | 9 | 3, 5 | 69 (A3) | white |
		  | 4 | 4, 3 | 64 (E3) | white |
		  | 5 | 4, 4 | 65 (F3) | white |
		  | 6 | 4, 5 | 66 (F#3) | white |
		  | 1 | 5, 3 | 61 (C#3) | white |
		  | 2 | 5, 4 | 62 (D3) | white |
		  | 3 | 5, 5 | 63 (D#3) | white |
		  | Clear | 6, 3 | 70 (A#3) | red |
		  | 0 | 6, 4 | 60 (C3) | white |
		  | Enter | 6, 5 | 71 (B3) | green |
		- **Controls:** no Live mapping. The device reads the notes on a MIDI track whose MIDI From is the Launchpad on channel 16.
	- ## Mode settings
		- On colour: yellow.
