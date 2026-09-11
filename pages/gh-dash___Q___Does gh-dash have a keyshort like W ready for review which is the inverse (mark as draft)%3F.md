logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[gh-dash/Wishlist]]

- # Does [[gh-dash]] have a [[Keyshort]] like `W` ready for review which is the inverse (mark as draft)?
	- ## [[AI Answer]]
		- **Short answer:** No. There is a built-in `W` / `builtin: ready` that runs `gh pr ready`, but no inverse key or builtin that converts a PR back to draft.
		- ### What exists
			- Default binding: `W` → help text `"ready for review"` (`PRKeys.Ready` in `internal/tui/keys/prKeys.go`).
			- Rebindable only as `builtin: ready` — the PR builtin list has `ready`, not draft/undo.
			- Under the hood, `tasks.PRReady` shells out to `gh pr ready <n> -R <repo>` with no `--undo`.
			- Official docs document only [`W` — Mark PR as Ready for Review](https://gh-dash.dev/getting-started/keybindings/selected-pr/), which converts draft → ready.
		- ### Workaround: custom keybinding
			- `gh pr ready` accepts `--undo` to convert a ready PR back to draft (plan-dependent). Bind that yourself under `keybindings.prs`:
			- ~~~yaml
			  keybindings:
			    prs:
			      - key: D
			        name: convert to draft
			        command: gh pr ready --undo --repo {{.RepoName}} {{.PrNumber}}
			  ~~~
			- Pick any free key (`D` is only an example — lowercase `d` is already `diff`). Keep `--repo {{.RepoName}}` so it works when the dashboard is not launched from that checkout.
			- After the custom command, refresh (`r` / `R`) if the draft icon does not update immediately — unlike the built-in `ready` path, a custom command does not push `ReadyForReview` into the in-memory PR row.
		- [[Answer/Official]] from [Selected PR keybindings](https://gh-dash.dev/getting-started/keybindings/selected-pr/) and [Custom Keybindings — PR builtins](https://gh-dash.dev/configuration/keybindings/) (builtins list includes `ready`, not draft); undo via [`gh pr ready --undo`](https://cli.github.com/manual/gh_pr_ready).