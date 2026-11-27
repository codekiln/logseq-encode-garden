see-also:: [[Logseq/Pref/Page/Name]], [[My/Principle/Referential-Transparency]]

- # Identifier segments keep their spelling
	- A namespace segment that is an identifier keeps the identifier's spelling, including its case and whether it is plural. Title Case and singular titles apply to the words the garden chooses for itself.
	- ## What counts as an identifier
		- A string you type for a program to read, in a terminal, a configuration file or a source file. Spell it the way that program's documentation does, even where the program would accept another spelling.
		- Examples in this garden:
			- An executable: [[git]], [[tmux]].
			- A subcommand or flag: [[mise/cache/clear]], [[mise/tasks/add]], [[git/clean/--force]].
			- A configuration key or attribute name: [[git/attributes/filter/clean]], and the `Frontmatter/<literal-key>` pages described on [[Logseq/Entity/Frontmatter/Definition]].
			- A file extension: the format segment of an asset page, per [[Logseq/Entity/Asset]].
	- ## Why
		- The page name matches what you type, as [[My/Principle/Referential-Transparency]] asks. Knowing the command or key is enough to find its page, and the page title shows the spelling that works.
	- ## Each segment is judged on its own
		- Segments the garden adds below an identifier go back to Title Case, as in [[git/How To/Discard Changes to Working Dir]].
		- An identifier keeps its spelling under a Title Case parent, as a `Frontmatter/<literal-key>` segment does.
	- ## What is not an identifier
		- A name people read but no program reads, such as a label printed on a hardware panel. It follows Title Case, as [[Logseq/Entity/UI/Area]] asks for area names.
