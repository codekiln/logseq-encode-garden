logseq-entity:: [[Logseq/Entity/Frontmatter/Definition]]
alias:: preset-synth-microfreak-initialized
- # Initialized Preset
	- Owning type: [[Logseq/Entity/Preset/Synth/Microfreak]].
	- Boolean `true` or `false`: the initialization bit in the last saved header. Initialized slots are omitted from the populated preset inventory.
	- The decoded bit is `header[3] & 0x08`; see [Elektroid preset download](https://github.com/dagargo/elektroid/blob/6f3d50e2588f0236afb3510e1c55bbb292446aa2/src/connectors/microfreak.c#L322).
