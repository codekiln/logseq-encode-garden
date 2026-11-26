logseq-entity:: [[Logseq/Entity/Software/Feature]]
see-also:: [[git/attributes/filter]]

- # [gitattributes: defining attributes per path](https://git-scm.com/docs/gitattributes)
	- A `gitattributes` file gives attributes to paths in a [[git]] repository. Each line is a pattern followed by attributes, such as `*.als filter=als -merge`. Patterns follow `.gitignore` rules, except that negative patterns are not allowed and a directory pattern does not match the files inside it.
	- An attribute is set (`text`), unset (`-text`), set to a value (`filter=als`) or unspecified. When several lines match a path, the later line wins, attribute by attribute.
	- ## Where attributes are read from
		- `.gitattributes` files in the working tree are committed, so every clone has them. A file in a deeper directory takes precedence over one nearer the root.
		- `$GIT_DIR/info/attributes` takes precedence over all of them and applies to one repository; it is never committed.
		- The file named by `core.attributesFile` applies to every repository of one user, and the system-wide file applies last.
	- ## Attributes that name a driver
		- `filter`, `diff` and `merge` can each be set to the name of a driver. The driver's commands are defined in git configuration, such as `.git/config` or `~/.gitconfig`, and configuration is not committed. A clone has the attribute without the commands until its own configuration defines them.
		- A clone's configuration can read a committed file through an include. A relative `include.path` is resolved from the configuration file that names it, so `git config include.path ../.gitconfig` in a clone reads `.gitconfig` at the repository root. [git-config: Includes](https://git-scm.com/docs/git-config#_includes)
	- ## `filter`
		- Converts a file between the form in the working tree and the form git stores: [[git/attributes/filter]].
	- ## `diff`
		- Unset (`-diff`), `git diff` prints `Binary files differ`.
		- Set to a driver with `diff.<driver>.textconv`, git runs that command on each version and diffs the text it prints. The conversion is one-way and is for reading: only `git diff` and the `git log` family use it, and `git format-patch` never does. `diff.<driver>.cachetextconv = true` caches the output in `refs/notes/textconv/<driver>`. [Performing text diffs of binary files](https://git-scm.com/docs/gitattributes#_performing_text_diffs_of_binary_files)
	- ## `merge`
		- Unset (`-merge`), a merge keeps the current branch's version and reports a conflict. This suits files whose lines can't be merged meaningfully.
	- ## `binary`
		- A built-in macro attribute that equals `-diff -merge -text`. Custom macros are defined with `[attr]<name>` lines, only in top-level attribute files.
