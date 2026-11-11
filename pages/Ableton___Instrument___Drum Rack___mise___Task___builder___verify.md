logseq-entity:: [[Logseq/Entity/Mise/Task]]
task-owner:: [[Person/codekiln/GitHub/logseq-encode-garden]]
task-config-root:: .
task-name:: ableton:drumrack:builder:verify
source-link:: https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/ableton/drumrack/builder/verify
see-also:: [[Ableton/Instrument/Drum Rack/mise/Task/builder/up]]

- # Check a Drum Rack preset's samples
	- Lists every pad of an `.adg` [[Ableton/Instrument/Drum Rack]] with its note, name, devices and choke group, and flags each sample file that is missing. With `--base`, it also reports whether rack-level settings (macros, chain selector) match another preset, such as the rack a copy came from.
	- ## Invocation
		- ~~~sh
		  mise run ableton:drumrack:builder:verify "$HOME/Music/Ableton/User Library/Presets/Instruments/Drum Rack/Builder/Kit.adg" --base "$HOME/Music/Ableton/User Library/Presets/Instruments/Drum Rack/Kit Original.adg"
		  ~~~
	- ## Result
		- Read-only. Exits 0 when every sample exists and, with `--base`, the rack-level settings match; 1 when it finds a problem; 2 when the file is not a Drum Rack preset.
		- Samples from Live's Factory Packs count as present when the file exists, even though only Live can decode them.
	- ## Help
		- ~~~sh
		  mise run ableton:drumrack:builder:verify --help
		  ~~~
