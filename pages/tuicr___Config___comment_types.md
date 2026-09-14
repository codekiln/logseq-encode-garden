see-also:: [[tuicr/Config]], [[tuicr/Comment/Type]]

- # [[tuicr]] `comment_types` config
	- The top-level `comment_types` array in `config.toml` defines the review-comment categories [[tuicr]] offers — see [[tuicr/Comment/Type]] for what the feature is and its limits.
	- ## Fields per entry
		- `id` — required; stable internal value saved in sessions and used for matching.
		- `label` — optional; visible tag shown in the UI, export, and submitted comment (e.g. `[NITPICK]`); defaults to `id` uppercased.
		- `definition` — optional guidance text for LLMs, included in the exported `Comment types:` legend.
		- `color` — optional badge/border color; terminal name (`yellow`) or hex (`#RRGGBB`).
	- ## Example
	  ~~~toml
	  comment_types = [
	    { id = "note", label = "question", definition = "ask for clarification", color = "yellow" },
	    { id = "suggestion", definition = "possible improvements" },
	    { id = "issue", definition = "problems to fix" },
	    { id = "praise", definition = "positive feedback" },
	    { id = "nit", label = "nitpick", definition = "small optional tweaks", color = "#d19a66" },
	  ]
	  ~~~
	- ## Defaults
		- If `comment_types` is omitted, comments are untyped (`None`): no `[TYPE]` tag on submit/export, no badge in the TUI.
		- `None` always stays available at the end of the Tab cycle, configured or not, so an untyped comment is always possible.
		- `comment_types` is a full **replacement** of the configured set, not a merge with any built-in defaults; the first configured entry becomes the default type. Invalid entries are dropped with a startup warning; if every entry is invalid, tuicr falls back to `None` only.
	- ## Related settings
		- `[forge].comment_type_prefix` (default `true`) — prepends `[TYPE] ` to the comment body on submit (e.g. `[ISSUE] Magic number should be a constant`); `false` submits the raw text.
		- `[export].legend` (default `true`) — includes the `Comment types:` legend in exported Markdown.
		- `tuicr review add --type <id>` warns on stderr (still exits `0`) when `<id>` isn't a configured type, listing the valid ids.
	- Source: [docs/CONFIG.md — Comment types](https://github.com/agavra/tuicr/blob/main/docs/CONFIG.md#comment-types).
