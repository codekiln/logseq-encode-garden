logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Person/Matt Pocock]]
see-also:: [[Agent/Skills]], [[rulesync]]

- # [mattpocock/skills](https://github.com/mattpocock/skills)
	- [[Person/Matt Pocock]]'s [[Agent/Skills]], grouped in category directories: `skills/engineering/<name>/SKILL.md`, `skills/productivity/<name>/SKILL.md`, and others.
	- `skills/engineering/wayfinder` plans work too large for one agent session as a map of decision tickets on the issue tracker; see [[Latent Space/Blog/26/08/The wayfinder Skill: Navigating the "Fog of War" of Planning]]. It calls `grilling` (in `skills/productivity`) and `domain-modeling`, `research` and `prototype` (in `skills/engineering`), and sends the user to `setup-matt-pocock-skills` to record which issue tracker a repository uses.
	- [[Claude/Code/Skill/Grill Me]] came from this repository.
	- [[My/Dotfiles]] installs `wayfinder` and the five skills it calls globally through [[rulesync]] `sources` in `chezmoi/dot_aiglobal/rulesync.jsonc`.
