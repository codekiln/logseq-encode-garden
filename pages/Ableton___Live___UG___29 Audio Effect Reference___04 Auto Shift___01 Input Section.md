logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/29 Audio Effect Reference/04 Auto Shift]]
next:: [[Ableton/Live/UG/29 Audio Effect Reference/04 Auto Shift/02 Quantizer Tab]]
- # [29.4.1 Input Section](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#input-section)
	- ![Auto Shift’s Input Section](https://ableton-production.imgix.net/live-manual/12/AutoShiftInputSectionL12.png?auto=&w=320)
	- Auto Shift takes both audio and MIDI input.
	- **Input Pitch** shows the detected pitch in notes and cents.
	- **Pitch Range** — **High**, **Mid** or **Bass**, to match the source; each has an LED that lights when the input falls in its range. Each range has a different latency.
		- ![The Pitch Range LED Flashes to Indicate the Range for the Incoming Signal](https://ableton-production.imgix.net/live-manual/12/AutoShiftInputLEDL12.png?auto=&w=126)
	- **Input Gain** — −24 to +24 dB
	- The **Latency Readout** shows latency in ms. **Live Mode** in the title bar lowers latency for performance, at the cost of small glitches at note starts and fast pitch changes.
		- ![Enable Live Mode to Reduce Latency](https://ableton-production.imgix.net/live-manual/12/AutoShiftLiveModeL12.png?auto=&w=320)
	- ### [29.4.1.1 MIDI Input](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#midi-input)
		- MIDI input corrects pitch to notes from another MIDI track instead of to a scale.
			- ![Auto Shift’s MIDI Input Panel](https://ableton-production.imgix.net/live-manual/12/AutoShiftMIDIInputL12.png?auto=&w=320)
		- **MIDI In** shows the MIDI Input panel; **MIDI On** turns MIDI input on and swaps the Quantizer tab for the MIDI tab.
		- **External Source** picks the track; **Tapping Point** takes the notes before (Pre FX) or after (Post FX, Post Mixer) that track's MIDI effects.
		- Voice mode:
			- **Mono** — one note at a time; **Glide** sets how long overlapping notes take to slide
			- **Poly** — up to 2, 4 or 8 voices (**Voice Count**), for harmonies
		- With MIDI input on, Auto Shift is silent unless notes arrive.