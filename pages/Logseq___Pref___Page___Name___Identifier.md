see-also:: [[Logseq/Pref/Page/Name]], [[My/Principle/Referential-Transparency]]

- # Commands, flags, settings and file extensions keep their documented spelling
	- Most page names in this garden use Title Case and singular nouns, per [[Logseq/Pref/Page/Name]]. The exception is a command, a flag, a setting or a file extension. That part of the page name keeps the spelling from the software's documentation, including lowercase letters and plurals.
	- Programmers call these names identifiers.
	- ## Examples
		- The command `git` has the page [[git]], and `tmux` has [[tmux]].
		- The command `mise tasks add` has the page [[mise/tasks/add]]. The documentation writes `tasks`, so the page name keeps the plural.
		- The flag in `git clean --force` has the page [[git/clean/--force]].
		- The git setting `filter.<driver>.clean` has the page [[git/attributes/filter/clean]]. Git ignores the case of setting names, so `Clean` would work too, but the documentation writes `clean`.
		- A Logseq property such as `see-also::` gets a page ending in `Frontmatter/see-also`, as [[Logseq/Entity/Frontmatter/Definition]] describes.
		- An image's file extension ends its asset page name, as in `Asset/Image/Shape-Clip/png`, per [[Logseq/Entity/Asset]].
	- ## Why
		- A page name that matches the command lets a person or an AI agent find the page from the command alone, and shows them the spelling the software expects. [[My/Principle/Referential-Transparency]] holds that a name should read the same everywhere it shows up.
	- ## Words the garden chooses still use Title Case
		- In [[git/How To/Discard Changes to Working Dir]], `git` is the command and `How To` is the garden's own words.
		- A property name keeps its documented spelling under the Title Case `Frontmatter` before it.
		- Labels printed on hardware use Title Case, because they never appear in a command or a settings file. [[Logseq/Entity/UI/Area]] names the areas of a hardware panel this way.
