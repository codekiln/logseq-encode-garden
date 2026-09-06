alias:: [[rg/--glob]]

- `-g GLOB, --glob=GLOB`
	- Include or exclude files and directories for searching that match the given glob. This always overrides any other ignore logic. Multiple glob flags may be used. Globbing rules match `.gitignore` globs. Precede a glob with a `!` to exclude it. If multiple globs match a file or directory, the glob given later in the command line takes precedence.
	- Globs support specifying alternatives: `-g'ab{c,d}*'` is equivalent to `-g'abc' -g'abd'`.
	- Matching a directory such as `foo` with `-g foo` does not also match `foo/bar`; use `-g 'foo/**'` to match everything under a directory.
	- Option text matches `rg --help` / `man rg` (see [[rg/manpage]]).
