logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/32 Max for Live]]
prev:: [[Ableton/Live/UG/32 Max for Live/02 Using Max for Live Devices]]
next:: [[Ableton/Live/UG/32 Max for Live/04 Building Max for Live MIDI Tools]]
- # [32.3 Editing Max for Live Devices](https://www.ableton.com/en/live-manual/12/max-for-live/#editing-max-for-live-devices)
	- A Max device, or "patch", is a set of objects passing data to each other through virtual cables. In the default Max Audio Effect, the `plugin~` object takes audio in from the device's place in the chain and passes it to `plugout~`, which sends it on to the next device.
		- ![The Default Max Audio Effect Preset](https://ableton-production.imgix.net/live-manual/12/MaxAudioEffectL12.png?auto=&w=320)
	- To start a new device, drag Max Instrument, Max MIDI Effect or Max Audio Effect from the browser into the Set. Any existing Max device can be edited the same way.
	- Open the Max editor, also called the patcher, with **Edit in Max** from the context menu or from the Show Options menu in the device title bar.
		- ![The Edit in Max Command](https://ableton-production.imgix.net/live-manual/12/MaxEditCommandL12.png?auto=&w=320)
		- ![The Default Max Audio Effect in the Max Editor](https://ableton-production.imgix.net/live-manual/12/MaxPatcherL12.png?auto=&w=320)
		- Before Live 12.2 devices had an Edit button in the title bar instead. Adding `-MaxForLiveDeveloperMode` to `Options.txt` brings it back.
	- Save from Max's File menu.
		- **Save** updates every instance of that device in the Set.
		- **Save As** asks whether the change applies to the edited preset only or to all instances.
	- Max devices are saved as separate [[Ableton/File/.amxd]] files, not inside the Live Set. By default each type goes to its own folder in the User Library, such as Max Audio Effect or Max MIDI Effect. Keep that default: moving or renaming an AMXD file breaks the path stored in the Set. The File Manager can find a missing file.