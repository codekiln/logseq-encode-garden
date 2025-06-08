tags:: [[Diataxis/How To]]

- # How To Manage Monitor Layouts with Mise and a Unified Task
	- ## Goal
		- Use a single Mise task to save and restore multiple monitor layouts (e.g., sitting or standing) by profile name.
	- ## Preconditions
		- Mise is installed and activated in your shell.
		- [`displayplacer`](https://github.com/jakehilborn/displayplacer) is installed via Homebrew:
			- `brew install displayplacer`
		- `displayplacer` should be globally available in `PATH`. **Do not use `mise link` for this case**, as versioning or plugin behavior is unnecessary for helper CLIs.
	- ## Procedure
		- ### 1. Create a storage directory for layouts
			- ```bash
			  mkdir -p ~/.config/mise-monitor-layouts
			  ```
		- ### 2. Define the `monitors-home` task in `~/mise.toml`
			- Add the following:
			  ~~~toml
			  [tasks.monitors-home]
			  description = "Save or restore monitor layout by profile (e.g. standing, sitting)"
			  run = """
			  #!/usr/bin/env bash
			  set -euo pipefail
			  
			  PROFILE="${1:-}"
			  FLAG="${2:-}"
			  
			  if [[ -z "$PROFILE" ]]; then
			    echo "Usage: monitors-home <profile> [--save]"
			    exit 1
			  fi
			  
			  LAYOUT_FILE="$HOME/.config/mise-monitor-layouts/${PROFILE}.layout"
			  
			  if [[ "$FLAG" == "--save" ]]; then
			    displayplacer list > "$LAYOUT_FILE"
			    echo "Saved layout: $PROFILE"
			  else
			    if [[ ! -f "$LAYOUT_FILE" ]]; then
			      echo "No layout saved for profile: $PROFILE"
			      exit 1
			    fi
			    displayplacer "$(cat "$LAYOUT_FILE")"
			  fi
			  """
			  ~~~
		- ### 3. Save layout profiles
			- Save the *standing* configuration:
			  ```bash
			  mise run monitors-home standing --save
			  ```
			- Save the *sitting* configuration:
			  ```bash
			  mise run monitors-home sitting --save
			  ```
		- ### 4. Restore layout profiles
			- To restore standing:
			  ```bash
			  mise run monitors-home standing
			  ```
			- To restore sitting:
			  ```bash
			  mise run monitors-home sitting
			  ```
	- ## Troubleshooting
		- *Command not found: displayplacer* → Run `brew install displayplacer`.
		- *No layout saved for profile* → Run with `--save` to store layout before restoring.
		- *Permission denied* → Make sure the layout directory and file are writable and readable.
	- ## References
		- [displayplacer GitHub](https://github.com/jakehilborn/displayplacer)
		- [TOML Tasks Reference – Mise](https://mise.jdx.dev/tasks/toml-tasks.html)