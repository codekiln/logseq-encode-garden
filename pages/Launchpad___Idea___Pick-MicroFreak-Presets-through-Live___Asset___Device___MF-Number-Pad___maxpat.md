logseq-entity:: [[Logseq/Entity/Asset]]

- # MF Number Pad patcher
	- [MF Number Pad patcher JSON](../assets/Launchpad___Idea___Pick-MicroFreak-Presets-through-Live___Asset___Device___MF-Number-Pad.maxpat)
	- The Max patcher inside [[Launchpad/Idea/Pick-MicroFreak-Presets-through-Live/Asset/Device/MF-Number-Pad/amxd]], as editable JSON. A `midiin` feeds a `v8.codebox` that holds the device's JavaScript. The codebox feeds `midiout` and two `live.comment` boxes that show the slot being typed and the last slot sent.
	- The `.amxd` is this JSON behind a short `ampf` header for a MIDI Effect, whose `ptch` field gives the length of the JSON that follows.
