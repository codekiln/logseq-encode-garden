alias:: [[rg -P]]

- `-P, --pcre2`
	- When this flag is present, ripgrep will use the PCRE2 regex engine instead of its default regex engine.
	- This is generally useful when you want to use features such as look-around or backreferences.
	- Using this flag is the same as passing `--engine=pcre2`. Users may instead elect to use `--engine=auto` to ask ripgrep to automatically select the right regex engine based on the patterns given. This flag and the `--engine` flag override one another.
	- Note that PCRE2 is an optional ripgrep feature. If PCRE2 was not included in your build of ripgrep, then using this flag will result in ripgrep printing an error message and exiting. PCRE2 may also have worse user experience in some cases, since it has fewer introspection APIs than ripgrep's default regex engine. For example, if you use a `\n` in a PCRE2 regex without the `-U/--multiline` flag, then ripgrep will silently fail to match anything instead of reporting an error immediately (like it does with the default regex engine).
	- This flag can be disabled with `--no-pcre2`.
	- Option text matches `rg --help` / `man rg` (see [[rg/manpage]]).
