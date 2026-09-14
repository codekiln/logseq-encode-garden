logseq-entity:: [[Logseq/Entity/Question]]

- # What configuration options does [[tuicr]] have for review comment types?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [docs/CONFIG.md — Comment types](https://github.com/agavra/tuicr/blob/main/docs/CONFIG.md#comment-types)
		- **Short answer:** a top-level `comment_types` array in `config.toml` defines named categories (e.g. `praise`, `nit`); each entry drives the TUI badge, the `[TYPE]` export/submit tag, and the Tab cycle order.
		- **Where:** `~/.config/tuicr/config.toml` (`$XDG_CONFIG_HOME/tuicr/config.toml` on Linux/macOS, `%APPDATA%\tuicr\config.toml` on Windows).
		- **Fields per entry:**
			- `id` — required, stable internal value saved in sessions and used for matching.
			- `label` — optional, visible tag shown in the UI/export/submitted comment (e.g. `[NITPICK]`); defaults to `id` uppercased.
			- `definition` — optional guidance text for LLMs, included in the exported `Comment types:` legend.
			- `color` — optional badge/border color (terminal name like `yellow` or hex `#RRGGBB`).
		- **Example from the docs:**
		  ~~~toml
		  comment_types = [
		    { id = "note", label = "question", definition = "ask for clarification", color = "yellow" },
		    { id = "suggestion", definition = "possible improvements" },
		    { id = "issue", definition = "problems to fix" },
		    { id = "praise", definition = "positive feedback" },
		    { id = "nit", label = "nitpick", definition = "small optional tweaks", color = "#d19a66" },
		  ]
		  ~~~
		- **Defaults and the `None` type:** if `comment_types` is omitted, comments are untyped (`None`) — no `[TYPE]` tag and no badge. `None` always stays available at the end of the Tab cycle so an untyped comment is always possible.
		- **Replacement, not merge:** `comment_types` fully replaces the configured set; the first configured type becomes the default, and invalid entries are dropped with a startup warning (falling back to `None` only if all entries are invalid).
		- **`tuicr review add --type <id>`** warns on stderr (but still exits `0`) if `<id>` isn't a configured type, listing valid ids.
		- **Related `[forge]` setting:** `comment_type_prefix` (default `true`) controls whether `[TYPE] ` is prepended to the comment body on submit, e.g. `[ISSUE] Magic number should be a constant`; set to `false` to submit the raw text.
		- **Related `[export]` setting:** `legend` (default `true`) controls whether the `Comment types:` legend is included in exported Markdown.
