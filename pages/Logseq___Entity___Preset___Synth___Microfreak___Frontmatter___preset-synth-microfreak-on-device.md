logseq-entity:: [[Logseq/Entity/Frontmatter/Definition]]
alias:: preset-synth-microfreak-on-device
- # Preset Present on Device
	- Owning type: [[Logseq/Entity/Preset/Synth/Microfreak]].
	- Boolean `true` or `false`: whether this saved preset matched a populated slot in the latest successful full inventory.
	- A failed or partial inventory cannot establish absence. `false` marks a page whose sound is no longer on the device; that page is deleted. Git history keeps it.
