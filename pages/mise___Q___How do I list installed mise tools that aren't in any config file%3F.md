logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[mise]], [[mise/ls]], [[mise/ls/--installed]], [[mise/uninstall]], [[mise/Task/File]], [[mise/Task/File/Group]], [[usageCLI/spec]], [[mise/Q/How do I remove a mise tool?]], [[mise/Q/What's the difference between mise unuse, mise uninstall, and mise cache clear?]], [[chezmoi]]

- # How do I list installed [[mise]] tools that aren't in any [[mise/Config/mise.toml]] (or other config) file?
	- ## [[My Answer]]
		- use user-defined [[mise/Task/File]]s
			- ((6a16c6fd-7c8e-4b04-b96d-a2138b61561c))
			- ((6a16c6fd-3e2e-4303-8610-8b62be2aa4b9))
			- ((6a16cd70-54d2-4bf9-889f-018ee1327e2d))
		- for installation, put in [[mise/Config/mise.toml/Global]]
			- {{embed ((6a16c6fd-b004-4a25-84a8-24de5a7c3ed0))}}
			- {{embed ((6a16c6fd-c3c3-4b53-a2fb-84eac38c58a1))}}
	- ## [[AI Answer]]
		- **Short answer:** Orphan installs are on disk but not pinned in any merged config—`mise ls --installed` shows a blank config column, and JSON has `source: null` (or empty `source.path`). Use global [[mise/Task/File]] tasks: `mise run tool:missing:ls` to list `TOOL@VERSION` lines, preview with `mise run tool:missing:uninstall -- --preview`, then `mise run tool:missing:uninstall` to remove. Use [[mise/uninstall]], not [[mise/unuse]] (config-only).
		- **Chezmoi source:** Managed in [[dotfiles]] at `chezmoi/dot_config/mise/tasks/tool/missing/` (`executable_ls` → `~/.config/mise/tasks/tool/missing/ls`, `executable_uninstall` → `…/uninstall`). Apply with `chezmoi apply`.
		- **Tasks** (under `~/.config/mise/tasks/tool/missing/`, group `tool:missing:*` per [[mise/Task/File/Group]]):
			- `mise run tool:missing:ls` — prints orphans, one per line
			  id:: 6a16c6fd-7c8e-4b04-b96d-a2138b61561c
			- `mise run tool:missing:uninstall -- --preview` (or `-n`) — same list as `ls`; does not uninstall
			  id:: 6a16c6fd-3e2e-4303-8610-8b62be2aa4b9
			- `mise run tool:missing:uninstall` — uninstalls each orphan one at a time, verifies none remain
			  id:: 6a16cd70-54d2-4bf9-889f-018ee1327e2d
		- **Do not use `--dry-run` on the task:** `mise run --dry-run` is a *runner* flag (“print the command, don't execute”). It collides with a task flag named `--dry-run` and produces only a line like `[tool:missing:uninstall] $ …/uninstall --dry-run` with no output. The task uses `--preview` instead ([[usageCLI/spec]] `#USAGE flag "-n --preview"`).
		- **Task sources**
			- `tool/missing/ls`:
			  id:: 6a16c6fd-b004-4a25-84a8-24de5a7c3ed0
				- ~~~bash
				  #!/usr/bin/env bash
				  set -euo pipefail
				  #MISE description="List installed mise tools not referenced in any config"
				  mise ls --installed --json | jq -r '
				    to_entries[] | .key as $tool | .value[] |
				    select(.source == null or (.source.path // "") == "") |
				    "\($tool)@\(.version)"
				  '
				  ~~~
			- `tool/missing/uninstall`:
			  id:: 6a16c6fd-c3c3-4b53-a2fb-84eac38c58a1
				- ~~~bash
				  #!/usr/bin/env bash
				  set -euo pipefail
				  #MISE description="Uninstall mise tools not referenced in any config"
				  #USAGE flag "-n --preview" help="List orphans only; do not uninstall"
				  
				  orphan_specs() {
				    mise ls --installed --json | jq -r '
				      to_entries[] | .key as $tool | .value[] |
				      select(.source == null or (.source.path // "") == "") |
				      "\($tool)@\(.version)"
				    '
				  }
				  
				  orphans=()
				  while IFS= read -r line; do
				    [[ -n "$line" ]] && orphans+=("$line")
				  done < <(orphan_specs)
				  
				  if [[ ${#orphans[@]} -eq 0 ]]; then
				    echo "No orphan tools installed."
				    exit 0
				  fi
				  
				  preview=false
				  [[ "${usage_preview:-false}" == "true" || "${usage_n:-false}" == "true" ]] && preview=true
				  
				  if $preview; then
				    printf '%s\n' "${orphans[@]}"
				    exit 0
				  fi
				  
				  exit_code=0
				  for spec in "${orphans[@]}"; do
				    echo "Uninstalling ${spec}..."
				    if ! out=$(command mise uninstall "$spec" 2>&1); then
				      printf '%s\n' "$out" >&2
				      echo "error: failed to uninstall ${spec}" >&2
				      exit_code=1
				    elif [[ -n "$out" ]]; then
				      printf '%s\n' "$out"
				    fi
				  done
				  
				  remaining=()
				  while IFS= read -r line; do
				    [[ -n "$line" ]] && remaining+=("$line")
				  done < <(orphan_specs)
				  
				  if [[ ${#remaining[@]} -gt 0 ]]; then
				    echo "Still installed (not removed):" >&2
				    printf '  %s\n' "${remaining[@]}" >&2
				    exit 1
				  fi
				  
				  if [[ $exit_code -ne 0 ]]; then
				    exit "$exit_code"
				  fi
				  
				  echo "Uninstalled ${#orphans[@]} orphan(s)."
				  ~~~
		- **Related:** `mise ls --current` is the inverse (config-only). `mise ls --prunable` is for stale versions of *pinned* tools ([[mise/Q/What's the difference between mise unuse, mise uninstall, and mise cache clear?]]). [mise ls](https://mise.jdx.dev/cli/ls.html)