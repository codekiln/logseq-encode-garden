logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/33 Max for Live Devices/03 Max for Live MIDI Effects]]
prev:: [[Ableton/Live/UG/33 Max for Live Devices/03 Max for Live MIDI Effects/04 MPE Control]]
next:: [[Ableton/Live/UG/33 Max for Live Devices/03 Max for Live MIDI Effects/06 Shaper MIDI]]
- # [33.3.5 Note Echo](https://www.ableton.com/en/live-manual/12/max-for-live-devices/#note-echo)
	- ![The Note Echo Effect](https://ableton-production.imgix.net/live-manual/12/MaxNoteEchoL12.png?auto=&w=320)
	- A MIDI echo: repeats each note at set intervals with falling velocity.
	- **Sync** on — the delay is chosen in 16th notes from numbered switches; 4 is one beat. The **Delay Time** percentage nudges the repeats off the grid for a drum-machine swing.
	- **Sync** off — the delay is in milliseconds; drag the Delay Time slider or type a value.
	- **Input** — **Thru** plays the original note and the echoes; **Mute** plays only the echoes.
	- **Pitch** — transposition added on each repeat
	- **Delay** — velocity of the echoes; **Fback** — how much output feeds back into the delay
	- **MPE** — echoes MPE data with the notes (otherwise it is filtered out). **Press**, **Slide** and **Note PB** then set feedback for each; below 100% the echoed MPE data fades with each repeat.