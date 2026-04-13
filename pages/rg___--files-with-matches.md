alias:: [[rg/-l]]

- `-l, --files-with-matches`
	- Print only the paths with at least one match and suppress match contents.
	- Note that it is possible for this flag to have results inconsistent with the output of `-c/--count`. Notably, by default, ripgrep tries to avoid searching files with binary data. With this flag, ripgrep might stop searching before the binary data is observed. But with `-c/--count`, ripgrep has to search the entire contents to determine the match count, which means it might see binary data that causes it to skip searching that file. To avoid this inconsistency without disabling binary detection, use the `--binary` flag.
	- This overrides `--files-without-match`.
	- Option text matches `rg --help` / `man rg` (see [[rg/manpage]]).
