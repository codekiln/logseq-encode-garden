see-also:: [[My/Principle/Favor Readers Over Writers]], [[My/Principle/Simplify/Prefer Standards and Defaults]]

- # Configuration Comment Style
	- A [[Configuration File]] comment should say *why* a setting departs from its tool's default — the "must" behind the customization — in addition to what the setting does.
	- Record trade-offs and provenance when they aren't obvious from the setting itself (e.g. why a workaround is needed, where a block was copied from).
	- Don't restate what a setting does when its name already conveys it; let self-documenting settings stand on their own. At the same time, consider [[My/Principle/Favor Readers Over Writers]] and don't assume that the reader has memorized all the arcane configuration options of any tool. If they are not self-evident, explain them.
	- Where the format can't carry comments (e.g. [[JSON]], `package.json`)
		- possible workarounds
			- prefer to use [[mise/Config/mise.toml]] to manage [[npm]] CLI dependencies instead of `package.json`, then use [[TOML]] comments.
				- in the case of a true npm dependency, this won't work, though ...
					- Some json ecosystem tools support [[json/jsonc]] even though the file ends in `.json`
					- consider a workaround like putting `"// why": "explanation",` as a pseudo-comment (if that doesn't break the tool)
		- If those workaround aren't options, think about what to do on a case-by-case basis to achieve the same goals