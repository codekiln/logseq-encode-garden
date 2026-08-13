logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[tmux/Pane/Q/How can I display the names of the panes in tmux?]], [[herdr/Q/Can herdr show the current session name, and how do I switch sessions?]]

- # What does `ui.show_agent_labels_on_pane_borders` do?
	- ## [[AI Answer]]
		- Read from the `herdrdev/herdr` source at `preview-2026-08-04-…-90-g952729ee`, checked against the installed `0.8.0` binary.
		- **Short answer:** it enables a fallback label. When a pane in a split has no reported title and no manual name, herdr writes the agent's own name — `claude`, `codex`, whatever detection or the integration hook reports — into the top border of that pane. Default is `false`; the key landed in `0.5.8` (2026-05-12), so `0.8.0` accepts it.
		- ### What the border title shows, in order
			- One chain feeds every split pane border title, and this flag only enables its last link:
				- 1. **Reported metadata title** — `herdr pane report-metadata <pane> --title …`. Wins over everything, including a manual rename.
				- 2. **Manual pane label** — `herdr pane rename <pane> <label>`, `prefix+shift+p`, the right-click pane menu, or the `pane.rename` socket API.
				- 3. **Agent name, only when this flag is true** — the reported display name (`report-metadata --display-agent …`) when there is one, otherwise the detected or hook-reported agent label.
			- With the flag `false` the third step is skipped and a pane nobody named stays blank. Turning it on costs nothing where a name already exists, since the first two steps still win.
		- ### Where the label appears
			- **Splits only.** herdr draws pane borders only when a tab holds more than one pane, so a lone pane carries no label however much the agent reports.
			- Needs `ui.pane_borders = true` (the default). Under `ui.pane_outer_borders = false` the outer edges drop their borders, so the top row of panes loses the border the title is drawn on.
			- The title sits at the left end of the top border as ` name `, truncated with `…` to the pane width minus four — narrow panes show a stub, and a pane four columns wide or less shows nothing.
			- Focused panes render it bold in the accent color, unfocused panes in the dim border color.
		- ### Two near misses
			- **`herdr agent rename <target> <name>` does not change the border.** It sets the agent's unique name, which is how the CLI and sidebar address that agent; the border reads the display-agent metadata field instead. `herdr pane rename` is the one that renames a border.
			- **A screen-detected label vanishes the moment the agent process exits**, rather than leaving a stale `claude` sitting over a plain shell. Hook-reported agents keep their label while the hook authority is live.