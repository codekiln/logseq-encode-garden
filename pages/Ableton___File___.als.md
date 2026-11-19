alias:: [[Ableton/File/.als]]

- **Purpose**: Live Set (entire project/arrangement).
- **Format**: gzipped XML.
- **Speculation**: Unzipping yields structured XML with tracks, devices, automation.
- **MIDI mappings**: MIDI Map Mode assignments are `KeyMidi`-shaped blocks inside the XML.
	- Live's own controls have named blocks: `Transport` holds `StopKeyMidi` and `RecordKeyMidi`, `Locators` holds `SetLocatorMapping`, `PreviousLocatorMapping` and `NextLocatorMapping`, and `MasterTrack` holds `KeyMidiCrossfadeEqual` for the crossfader. Other Live controls follow the same pattern, such as `TapTempoKeyMidi` and `MetronomOnKeyMidi`. A device parameter carries a `KeyMidi` block of its own.
	- Each block holds `Channel` (counted from 0, so `15` is MIDI channel 16), `NoteOrController`, `IsNote` (`false` for a CC) and `PersistentKeyString`, the computer key mapped to the same control, if any.
	- ~~~xml
	  <StopKeyMidi>
	  	<PersistentKeyString Value="&lt;" />
	  	<IsNote Value="false" />
	  	<Channel Value="15" />
	  	<NoteOrController Value="114" />
	  	...
	  </StopKeyMidi>
	  ~~~
	- To list them: `gunzip -c "Set.als" | grep -A8 -E "<(\w*KeyMidi\w*|\w*Mapping)>"`
- **Git**: Store in repo. Use a `textconv` filter to decompress for diffs.
- **See-Also:**
	- [[GitHub/codekiln/ableton-live-git-hooks]]