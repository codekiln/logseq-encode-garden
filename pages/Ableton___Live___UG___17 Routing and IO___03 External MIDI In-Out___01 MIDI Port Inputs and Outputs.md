logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/17 Routing and IO/03 External MIDI In-Out]]
next:: [[Ableton/Live/UG/17 Routing and IO/03 External MIDI In-Out/02 Playing MIDI With the Computer Keyboard]]

- # [17.3.1 MIDI Port Inputs and Outputs](https://www.ableton.com/en/live-manual/12/routing-and-i-o/#midi-port-inputs-and-outputs)
	- Settings → Link, Tempo & MIDI lists every MIDI input and output port. Each can be used by any number of tracks.
		- ![The MIDI port inputs and outputs list in the Settings](https://ableton-production.imgix.net/live-manual/12/MidiPreferencesDeviceList.png?auto=&w=320)
	- ## 17.3.1.1 Track
		- Sends or receives notes and CC messages.
		- Turn it on for an input to play or record notes, or to record CC from a hardware synth into clips.
		- Turn it on for an output to play external hardware, send notes to another app through a virtual MIDI bus, or send CC automation out.
		- A controller's output port needs Track only if the controller makes its own sound.
	- ## 17.3.1.2 Sync
		- Sends or receives MIDI Clock, or receives MIDI Timecode. A controller needs it only if it has a sequencer or arpeggiator.
		- Input: to follow an external sequencer, drum machine, groovebox or another DAW. Output: to drive those from Live, or to sync an external synth's LFO and arpeggiator.
		- Expanding an output port with Sync on shows more options:
			- ![Sync output options](https://ableton-production.imgix.net/live-manual/12/MIDIOutputPortSyncOptions.png?auto=&w=320)
			- **MIDI Clock Sync Delay** — delays outgoing sync in milliseconds to fix timing offsets.
			- **MIDI Clock Type** — Song sends Song Position Pointer and Continue whenever the play position changes; Pattern sends only Start, at the next bar, for devices that ignore SPP.
			- **Hardware Resync** — what the Control Bar's Resync External Hardware button sends when drifting gear needs pulling back in time: Stop and Start (default), Start Only, or Don't Resync.
			- ![The Resync External Hardware button in the Control Bar](https://ableton-production.imgix.net/live-manual/12/ResyncExternalHardwareIndicator.png?auto=&w=320)
	- ## 17.3.1.3 Remote
		- Lets a controller map to Live's parameters, and sends feedback back to it.
		- Input: for custom MIDI mappings, or to launch clips from a keyboard. [[Launchpad/Custom/Mode/1 Arrangement]] needs Remote on for the Launchpad's input.
		- Output: for controllers whose LEDs or motorised faders show the state of mapped parameters.
