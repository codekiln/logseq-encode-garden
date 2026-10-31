logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/23 Instruments and Effects]]
prev:: [[Ableton/Live/UG/23 Instruments and Effects/01 Device View]]
next:: [[Ableton/Live/UG/23 Instruments and Effects/03 Device Delay Compensation]]

- # [23.2 Using Devices](https://www.ableton.com/en/live-manual/12/working-with-instruments-and-effects/#using-devices)
	- The browser sidebar has labels for Live's devices, Max for Live devices and plug-ins.
		- ![Device labels in the browser sidebar](https://ableton-production.imgix.net/live-manual/12/DeviceCategoriesBrowserL12.png?auto=&w=320)
	- Double-click a device to add it to the selected track (or a new track), select it and press `Enter`, or drag it to a track, a drop area or the Device View. Dropping a sample into a MIDI track's Device View creates a [[Ableton/Instrument/Simpler]] with it.
	- With Auto monitoring, a track must be armed to hear an external input through its devices; adding an instrument to a MIDI track usually arms it. See [[Ableton/Live/UG/17 Routing and IO/01 Monitoring]] for other setups.
	- Signals run left to right, so order matters. In a MIDI track, everything before the instrument is MIDI and everything after is audio, so a chain can go MIDI effects → instrument → audio effects.
		- ![A MIDI track's device chain with all three device types](https://ableton-production.imgix.net/live-manual/12/DeviceSignalFlowMIDITrackL12.png?auto=&w=320)
	- Select a device's title bar and press `Delete` to remove it; drag title bars to reorder, or into another track to move. Cut, copy, paste and duplicate work too; pasted devices go before the selected one, or at the end if you click after the last device. Changes don't interrupt the audio.
	- Meters between devices show where a signal drops out or gets too hot.
		- ![Level meters between devices in a chain](https://ableton-production.imgix.net/live-manual/12/MetersBetweenDevicesL12.png?auto=&w=320)
	- There's no clipping between devices; it only happens at physical outputs or in rendered files.
	- Clip envelopes can automate or modulate device parameters per clip; see [[Ableton/Live/UG/27 Clip Envelopes]].
	- {{embed [[Ableton/Live/UG/23 Instruments and Effects/02 Using Devices/01 Device Title Bar]]}}
	- {{embed [[Ableton/Live/UG/23 Instruments and Effects/02 Using Devices/02 Device A-B Comparison]]}}
	- {{embed [[Ableton/Live/UG/23 Instruments and Effects/02 Using Devices/03 Live Device Presets]]}}
	- {{embed [[Ableton/Live/UG/23 Instruments and Effects/02 Using Devices/04 Hot-Swapping Presets]]}}
	- {{embed [[Ableton/Live/UG/23 Instruments and Effects/02 Using Devices/05 Saving Presets]]}}
	- {{embed [[Ableton/Live/UG/23 Instruments and Effects/02 Using Devices/06 Defaults]]}}
