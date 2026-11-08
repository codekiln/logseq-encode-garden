logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Launchpad/PRG/05 Software Integration]]
prev:: [[Launchpad/PRG/05 Software Integration/01 DAW Mode]]
next:: [[Launchpad/PRG/05 Software Integration/03 DAW Faders]]

- # The DAW In/Out interface
	- DAWs talk to the Launchpad on the USB DAW In/Out interface.
	- Messages the Launchpad accepts there:
		- Channel 1: static colour in Session view. Note `90h` (144), CC `B0h` (176)
		- Channel 2: flashing colour in Session view. Note `91h` (145), CC `B1h` (177)
		- Channel 3: pulsing colour in Session view. Note `92h` (146), CC `B2h` (178)
		- Channel 5: set DAW fader positions. CC `B4h` (180)
		- Channel 6: set DAW fader colours. CC `B5h` (181)
		- Channel 9: static colour in Drum Rack. Note `98h` (152)
		- Channel 10: flashing colour in Drum Rack. Note `99h` (153)
		- Channel 11: pulsing colour in Drum Rack. Note `9Ah` (154)
		- Channel 16: external note injection on all external MIDI channels. Note `9Fh`. The PDF prints its decimal as 154; `9Fh` is 159.
	- Messages the Launchpad sends there:
		- Channel 1: Session layout pads and buttons. Note `90h` (144), CC `B0h` (176)
		- Channel 5: DAW fader movements. CC `B4h` (180)
		- Channel 9: Drum Rack layout pads. Note `98h` (152)
	- Aftertouch, polyphonic or channel pressure depending on settings, goes out on channel 1 for Session and channel 9 for Drum Rack.
	- These messages work whichever layout is showing. State set while a layout is hidden is kept and appears when the layout is shown.
