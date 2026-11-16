logseq-entity:: [[Logseq/Entity/Definition]]

- # Software Feature
	- In this garden, **Software Feature** pages model one capability of a [[Logseq/Entity/Software/Project]] that has its own vocabulary, limits or documentation, such as vaults in [[Claude/Managed Agents]].
	- ## What counts as a Software Feature
		- A named capability the vendor documents on its own page, which notes or other pages refer to apart from the product as a whole.
		- A capability that fits in one bullet of its project's page stays there.
		- A setting with a name and accepted values is a [[Logseq/Entity/Software/Option]]; an add-on from a marketplace is a [[Logseq/Entity/Software/Plugin]].
	- ## Naming and identity
		- Instances live under the owning project's namespace: `{software}/{Feature}`, using the vendor's name for the feature in the singular, as in [[Claude/Managed Agents/Vault]].
	- ## Frontmatter
		- Set `logseq-entity:: [[Logseq/Entity/Software/Feature]]` to mark an instance.
		- Shared frontmatter conventions live on [[Logseq/Frontmatter]].
	- ## Page shape
		- The H1 links the vendor's documentation page for the feature.
		- Child bullets say what the feature does, its parts and limits, and where the garden touches it.
	- ## Examples in this garden
		- [[Claude/Managed Agents/Vault]]
