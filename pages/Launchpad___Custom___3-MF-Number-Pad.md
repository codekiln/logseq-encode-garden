logseq-entity:: [[Logseq/Entity/Launchpad/Custom/Mode]]
launchpad-custom-mode-url:: https://components.novationmusic.com/launchpad-pro-mk3/custom-modes/795139

- # 3 MF Number Pad
	- [[Launchpad]] Custom Mode for keying in a [[Microfreak]] preset slot number, which a device in Live turns into a bank select and Program Change.
	- Twelve pads in rows 3 to 6 and columns 3 to 5 form a calculator layout. Every other pad and all edge buttons have nothing assigned.
	- ## Depends on
		- [[Ableton/Live/Device/Max/MF-Number-Pad]], on a MIDI track that listens to the Launchpad on channel 16 and sends to the MicroFreak.
	- ## Pads
		- Every pad is a Momentary Midi Note on channel 16. Components and Live name note 60 C3, an octave below the garden's names, so the Note column links note 60 as [[C4]].
		- ~~~
		  pad          note
		  7  8  9      67 68 69
		  4  5  6      64 65 66
		  1  2  3      61 62 63
		  C  0  E      70 60 71
		  ~~~
		- | Pad | Row, column | Note | Color |
		  |---|---|---|---|
		  | 7 | 3, 3 | 67 [[G4]] | white |
		  | 8 | 3, 4 | 68 [[G♯4]] | white |
		  | 9 | 3, 5 | 69 [[A4]] | white |
		  | 4 | 4, 3 | 64 [[E4]] | white |
		  | 5 | 4, 4 | 65 [[F4]] | white |
		  | 6 | 4, 5 | 66 [[F♯4]] | white |
		  | 1 | 5, 3 | 61 [[C♯4]] | white |
		  | 2 | 5, 4 | 62 [[D4]] | white |
		  | 3 | 5, 5 | 63 [[D♯4]] | white |
		  | Clear | 6, 3 | 70 [[A♯4]] | red |
		  | 0 | 6, 4 | 60 [[C4]] | white |
		  | Enter | 6, 5 | 71 [[B4]] | green |
		- **Controls:** no Live mapping. The device reads the notes on a MIDI track whose MIDI From is the Launchpad on channel 16.
	- ## How it works
	  collapsed:: true
		- Clear is red, bottom left. Enter is green, bottom right. The device gives the pads these meanings.
		- {{renderer :mermaid_d711e75d-08da-4a47-8fc5-5b5d9c561dce, 4}}
		  collapsed:: true
			- ```mermaid
			  flowchart TD
			      D["Digit 0 to 9, white"] --> A["Add digit, max 3"]
			      C["Clear, red, left"] --> X["Empty the number"]
			      E["Enter, green, right"] --> Q{"1 to 512?"}
			      Q -->|yes| S["Send bank and program"]
			      S --> X
			      Q -->|no| X
			      S --> M["MicroFreak loads slot"]
			      classDef red fill:#e05252,color:#fff,stroke:#a33
			      classDef green fill:#3fae5a,color:#fff,stroke:#2a7a3e
			      class C red
			      class E green
			  ```
		- Enter sends CC 0 = `(N − 1) // 128` for the bank, then Program Change `(N − 1) % 128`, on channel 1. With nothing typed, 0, or a number above 512, it only empties the number. Example: 2 5 9 Enter sends CC 0 = 2 and program 2, which loads [[Microfreak/Preset/259 Infini Pad]].
	- ## Mode settings
		- On color: yellow.
