logseq-entity:: [[Logseq/Entity/Definition]]
alias:: [[Logseq/Entity/Person/Music/ian]], [[Logseq/Entity/Person/Musician]]

- # Musician
	- In this garden, **Musician** pages model a real person who makes music: who composes it, performs it or produces it. Marking, works and hub shape follow [[Logseq/Entity/Person/Maker]].
	- ## What counts as an instance
		- A person who makes music in any role, when making music is a significant part of their public identity and of what the garden records about them.
		- A page carries this entity itself only when the person's role in music is unknown: `logseq-entity:: [[Logseq/Entity/Person/Maker/Music]]`. When the role is known, the page carries the child entity for it.
		- A music teacher, critic, historian, broadcaster, curator or label owner who makes no music leaves Musician out. One who published theory, a theory textbook or a teaching method carries [[Logseq/Entity/Person/Maker/Music/Theory]], as Guido of Arezzo does for his solmization syllables. Everyone else in this list stays a [[Logseq/Entity/Person]].
	- ## Child entities
		- Kinds of Musician; a page marked with one of them leaves Musician out:
			- [[Logseq/Entity/Person/Maker/Music/Composition]] — Composer, with [[Logseq/Entity/Person/Maker/Music/Composition/Song]] beneath it
			- [[Logseq/Entity/Person/Maker/Music/Performance]] — Performer, with [[Logseq/Entity/Person/Maker/Music/Performance/Conducting]] beneath it
			- [[Logseq/Entity/Person/Maker/Music/Production]] — Music Producer
		- Makers whose field is music and who make something other than music:
			- [[Logseq/Entity/Person/Maker/Music/Theory]] — Music Theorist
			- [[Logseq/Entity/Person/Maker/Music/Tech]] — Music Technologist
		- A Music Theorist or Music Technologist is a Musician only when the page also carries Musician or one of its kinds. A technologist who also makes music in an unknown role carries both: `logseq-entity:: [[Logseq/Entity/Person/Maker/Music/Tech]], [[Logseq/Entity/Person/Maker/Music]]`.
	- ## Naming and identity
		- A stage name or project name the person releases music under goes in `alias::` on the hub, as [[Person/Daniel Lopatin]] carries Oneohtrix Point Never.
		- A band or ensemble with its own identity has a page separate from its members' hubs.
