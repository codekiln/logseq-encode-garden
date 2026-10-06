logseq-entity:: [[Logseq/Entity/UX/Pattern]]

- # Feature Version Support
	- A UX pattern in which documentation navigation shows the minimum product version that supports each feature, often as a compact label such as `v0.17+`.
	- ## Interaction
		- Feature entries in a sidebar carry version metadata alongside their names.
		- The version label turns compatibility into part of feature discovery, so a reader can tell whether a feature is available in the version they use without opening a changelog.
	- ## Example
		- [[secretspec]] uses this affordance in its website sidebar: scopes are marked as supported from `v0.17+`, while secret generation is marked as supported from `v0.7+`.
	- ## Relation to version management
		- The pattern translates SemVer release history into an actionable compatibility signal. It helps readers choose a version baseline and understand when a feature entered the product without reconstructing that history from release notes.
	- ## Related
		- [[secretspec]]
