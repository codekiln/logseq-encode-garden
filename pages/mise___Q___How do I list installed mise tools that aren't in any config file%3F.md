logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[mise]], [[mise/ls]], [[mise/ls/--installed]], [[mise/uninstall]], [[mise/Task/File]], [[mise/Task/File/Group]], [[usageCLI/spec]], [[mise/Q/How do I remove a mise tool?]], [[mise/Q/What's the difference between mise unuse, mise uninstall, and mise cache clear?]]

- # How do I list installed [[mise]] tools that aren't in any [[mise/Config/mise.toml]] (or other config) file?
	- ## [[AI Answer]]
		- **Short answer:** Orphan installs are on disk but not pinned in any merged config—`mise ls --installed` shows a blank config column, and JSON has empty `source.path`. Use global [[mise/Task/File]] tasks: `mise run tool:missing:ls` to list `TOOL@VERSION` lines, then `mise run tool:missing:uninstall` (preview with `--dry-run`). Remove with [[mise/uninstall]], not [[mise/unuse]] (config-only).
		- **Tasks** (under `~/.config/mise/tasks/tool/missing/`, group `tool:missing:*` per [[mise/Task/File/Group]]):
			- `mise run tool:missing:ls` — prints orphans, one per line
			- `mise run tool:missing:uninstall` — uninstalls every orphan; `mise run tool:missing:uninstall --dry-run` first
		- **Task sources** ([[usageCLI/spec]] `#USAGE` docstrings for `mise run … --help`):
			- `tool/missing/ls`:
				- ~~~
				  #!/usr/bin/env bash
				  set -euo pipefail
				  #MISE description="List installed mise tools not referenced in any config"
				  mise ls --installed --json | jq -r '
				    to_entries[] | .key as $tool | .value[] |
				    select((.source.path // "") == "") |
				    "\($tool)@\(.version)"
				  '
				  ~~~
			- `tool/missing/uninstall`:
				- ~~~
				  #!/usr/bin/env bash
				  set -euo pipefail
				  #MISE description="Uninstall mise tools not referenced in any config"
				  #USAGE flag "-n --dry-run" help="Show what would be removed without uninstalling"
				  orphans=()
				  while IFS= read -r line; do
				    [[ -n "$line" ]] && orphans+=("$line")
				  done < <(mise ls --installed --json | jq -r '
				    to_entries[] | .key as $tool | .value[] |
				    select((.source.path // "") == "") |
				    "\($tool)@\(.version)"
				  ')
				  if [[ ${#orphans[@]} -eq 0 ]]; then
				    echo "No orphan tools installed."
				    exit 0
				  fi
				  if [[ "${usage_dry_run:-false}" == "true" ]]; then
				    mise uninstall --dry-run "${orphans[@]}"
				  else
				    mise uninstall "${orphans[@]}"
				  fi
				  ~~~
		- **Related:** `mise ls --current` is the inverse (config-only). `mise ls --prunable` is for stale versions of *pinned* tools ([[mise/Q/What's the difference between mise unuse, mise uninstall, and mise cache clear?]]). [mise ls](https://mise.jdx.dev/cli/ls.html)
