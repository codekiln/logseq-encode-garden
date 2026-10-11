logseq-entity:: [[Logseq/Entity/Frontmatter/Definition]]
alias:: [[performer]]

- # `performer::` — who plays on a recording
	- The person or group credited as the performing artist of a [[Logseq/Entity/Music/Recording]]. The first value is the primary artist, whose namespace holds the recording page.
	- ## Values
		- One or more comma-separated links to person pages (`Person/<Name>`) or group pages (`Group/<Name>`), as `performer:: [[Group/Beak]]`.
		- List the credited artist of the release. Session players and ensemble members belong in the page body.
	- ## Other entities that use it
		- [[Logseq/Entity/Music/Performance]] uses `performer::` with the same values for the people and groups who played at the event.
