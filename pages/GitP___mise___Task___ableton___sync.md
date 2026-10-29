- # Compile a Live Set from a Logseq page
	- A page with an Ableton Session block declares a Live 11 Set. An episode can inherit [[GitP/A/Template/Pattern A and B]] through its `ableton-template::` property.
	- Run from the logseq-encode-garden checkout containing the declaration.
	- Preview today's session:
	  ~~~sh
	  mise run gitpa:ableton:sync -- --page 'GitP/A/Session/26/10/29-Thu' --output "$HOME/Documents/ableton/GitP/26.10.29 Project/26.10.29.als" --fresh
	  ~~~
	- Add `--apply` to write the new Set. Existing output files are refused. Close or save the current Set in Live before opening a new compiled copy.
	- `--fresh` prepares a new performance: it clears clips, takes and recorded automation, resets the transport, and selects the declared tracks. Device chains and return effects come from the source template.
	- For a later revision, supply a new output filename. Use `--base-template /path/to/saved.als` to retain a saved performance while changing supported declarations; omit `--fresh` to preserve recorded material. A declaration that drops existing tracks or replaces locators requires a fresh build.
	- The `intention::` property inside Ableton Session appears in Live’s Set Info Text.
	- The declaration supports track names, existing track IDs, audio/MIDI routing targets, monitoring, arm state, colors, tempo, 4/4, scene labels, planned locators, and MIDI CC controls. Tracks and groups must already exist in the base Set.
	- `track-key::` gives each track a unique name within the declaration; `source-track-id::` selects the existing track to edit in the base Set. Template inheritance replaces whole sections, so a Tracks override declares the complete desired track list.
	- Live preferences select the audio interface and enable Remote on the Launchpad MIDI input. Custom Mode pad assignments are stored on the Launchpad separately from the Set's MIDI mappings.
	- Source and declaration details: [Ableton compiler README](../mise-tasks/gitpa/ableton/README.md). The approach follows [[Ableton/Live/Idea/Declare a Live Set in Logseq]].
