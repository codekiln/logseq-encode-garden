logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/34 MIDI and Key Remote/01 MIDI Remote Control]]
prev:: [[Ableton/Live/UG/34 MIDI and Key Remote/01 MIDI Remote Control/01 Natively Supported Control Surfaces]]
next:: [[Ableton/Live/UG/34 MIDI and Key Remote/01 MIDI Remote Control/03 Takeover Mode]]
- # [34.1.2 Manual Control Surface Setup](https://www.ableton.com/en/live-manual/12/midi-and-key-remote-control/#manual-control-surface-setup)
	- A controller that is not in the Control Surface chooser can still be mapped by hand from the MIDI Ports section of the Link, Tempo & MIDI tab.
	- ![Defining Control Surfaces Manually](https://ableton-production.imgix.net/live-manual/12/MIDIActivePorts.png?auto=&w=320)
	- To use an input port for remote control, set its **Remote** switch to On. Any number of ports can be on; Live merges their MIDI.
	- For a controller with motorized faders or LEDs, also turn on Remote for its output port so Live can send changed values back to it.
	- To test, send MIDI from the controller: the Control Bar's MIDI indicators flash when Live receives a message.
	- The manual suggests choosing a Takeover Mode before leaving Settings — [[Ableton/Live/UG/34 MIDI and Key Remote/01 MIDI Remote Control/03 Takeover Mode]]. Mapping then happens one parameter at a time.