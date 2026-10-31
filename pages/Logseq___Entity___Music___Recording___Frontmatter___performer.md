logseq-entity:: [[Logseq/Entity/Frontmatter/Definition]]
alias:: [[performer]]

- # `performer::` — who plays on a recording
	- The known people or groups who perform on a [[Logseq/Entity/Music/Recording]]. Published artist identities are recorded separately through [[Logseq/Frontmatter/created-by-identities]]; when present, its first identity supplies the recording namespace.
	- ## Values
		- One or more comma-separated links to person pages (`Person/<Name>`) or group pages (`Group/<Name>`), as `performer:: [[Group/Beak]]`.
		- Record performers whose participation on this recording is known. Session-player details and instruments belong in the page body; identity membership alone does not establish participation.
	- ## Other entities that use it
		- [[Logseq/Entity/Music/Performance]] uses `performer::` with the same values for the people and groups who played at the event.
