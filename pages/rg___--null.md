alias:: [[rg/-0]]

- `rg -0, rg --null`
	- Whenever a file path is printed, follow it with a [[ASCII/C0/NUL]] byte. This includes printing file paths before matches, and when printing a list of matching files such as with `-c/--count`, [[rg/-l]] aka [[rg/--files-with-matches]] and `--files`. This option is useful for use with [[xargs]].
	- Option text matches `rg --help` / `man rg` (see [[rg/manpage]]).