logseq-entity:: [[Logseq/Entity/Question]]

- # How do I do the equivalent of Merge without waiting for requirements to be met (bypass rules) or use `--admin` in [[gh-dash]]?
	- ## [[AI Answer]]
		- **Short answer:** The built-in `m` merge (`builtin: merge`) shells out to plain `gh pr merge` — it has no admin/bypass option. Override `m` (or bind another key) with a custom PR command that passes `--admin`, using the same template vars the official examples use.
		- ### Config override
			- In `~/.config/gh-dash/config.yml` (or a repo-local `.gh-dash.yml`):
			- ~~~yaml
			  keybindings:
			    prs:
			      - key: m
			        name: merge admin
			        command: gh pr merge --admin --repo {{.RepoName}} {{.PrNumber}}
			  ~~~
			- `{{.RepoName}}` and `{{.PrNumber}}` are the standard PR keybinding placeholders; keep `--repo` so the merge works when the dashboard is not launched from that checkout.
			- Prefer a different key (e.g. `M`) if you want to keep the default interactive merge on `m` and reserve admin merge for an explicit chord.
		- ### Why the checkbox is missing
			- GitHub's web UI "Merge without waiting for requirements to be met (bypass rules)" maps to administrator privileges on the API side — the CLI equivalent is `gh pr merge --admin`.
			- gh-dash's built-in merge action does not surface that flag; only a custom `command:` can.
		- [[Answer/Official]] from [PR Keybindings](https://gh-dash.dev/configuration/keybindings/) and the [configuration examples](https://gh-dash.dev/configuration/examples/) (the docs' own sample binds `m` to `gh pr merge --admin --repo {{.RepoName}} {{.PrNumber}}`).