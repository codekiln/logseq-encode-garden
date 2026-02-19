tags:: [[Diataxis/How To]]

- # How To Manage Monitor Layouts with Mise and [[CLI/Tool/displayplacer]]
	- ## Goal
		- Use a single Mise task with proper argument parsing to save, restore, list, and edit multiple monitor layouts (e.g., sitting or standing) by profile name.
	- ## Preconditions
		- Mise is installed and activated in your shell.
		- [[CLI/Tool/displayplacer]] [`displayplacer`](https://github.com/jakehilborn/displayplacer) is installed via Homebrew:
			- `brew install displayplacer`
		- `displayplacer` should be globally available in `PATH`. **Do not use `mise link` for this case**, as versioning or plugin behavior is unnecessary for helper CLIs.
		- Environment variables [[EnvVar/VISUAL]] or [[EnvVar/EDITOR]] should be set for the edit functionality.
	- ## Procedure
		- ### 1. Create a storage directory for layouts
			- ```bash
			  mkdir -p ~/.config/mise-monitor-layouts
			  ```
		- ### 2. Define the enhanced `monitors-home` task in `~/.config/mise/config.toml`
			- Add the following with proper usage spec and argument handling:
			  ~~~toml
			  [tasks.monitors-home]
			  description = """Save or restore monitor layout by profile (e.g. standing, sitting) - 
			  see [[CLI/Tool/displayplacer/How To/Save and Restore Monitor Configurations with mise]]
			  """
			  usage = '''
			  arg "action" "Action to perform: list, save, restore, or edit"
			  arg "profile" "Profile name (e.g., standing, sitting)"
			  flag "-s --save" "Save current layout (alternative to 'save' action)"
			  flag "-l --list" "List available profiles (alternative to 'list' action)"
			  '''
			  run = """
			  #!/usr/bin/env bash
			  set -euo pipefail
			  
			  # Create layouts directory if it doesn't exist
			  mkdir -p "$HOME/.config/mise-monitor-layouts"
			  
			  # Determine action and profile
			  ACTION="{{arg(name='action')}}"
			  PROFILE="{{arg(name='profile')}}"
			  SAVE_FLAG="{{flag(name='save')}}"
			  LIST_FLAG="{{flag(name='list')}}"
			  
			  # Handle flag-based actions
			  if [[ "$LIST_FLAG" == "true" ]]; then
			    ACTION="list"
			  fi
			  
			  if [[ "$SAVE_FLAG" == "true" ]]; then
			    ACTION="save"
			  fi
			  
			  # Handle list action
			  if [[ "$ACTION" == "list" ]]; then
			    LAYOUT_DIR="$HOME/.config/mise-monitor-layouts"
			    if [[ ! -d "$LAYOUT_DIR" ]] || [[ -z "$(ls -A "$LAYOUT_DIR" 2>/dev/null)" ]]; then
			      echo "No saved layouts found."
			      echo "Use 'mise run monitors-home save <profile>' to save a layout."
			      exit 0
			    fi
			    
			    echo "Available profiles:"
			    for file in "$LAYOUT_DIR"/*.layout; do
			      if [[ -f "$file" ]]; then
			        basename "$file" .layout
			      fi
			    done
			    exit 0
			  fi
			  
			  # Handle save action
			  if [[ "$ACTION" == "save" ]]; then
			    if [[ -z "$PROFILE" ]]; then
			      echo "Error: Profile name required for save action"
			      echo "Usage: mise run monitors-home save <profile>"
			      echo "   or: mise run monitors-home <profile> --save"
			      exit 1
			    fi
			    
			    LAYOUT_FILE="$HOME/.config/mise-monitor-layouts/${PROFILE}.layout"
			    displayplacer list > "$LAYOUT_FILE"
			    echo "Saved layout: $PROFILE"
			    exit 0
			  fi
			  
			  # Handle restore action
			  if [[ "$ACTION" == "restore" ]]; then
			    if [[ -z "$PROFILE" ]]; then
			      echo "Error: Profile name required for restore action"
			      echo "Usage: mise run monitors-home restore <profile>"
			      exit 1
			    fi
			    
			    LAYOUT_FILE="$HOME/.config/mise-monitor-layouts/${PROFILE}.layout"
			    if [[ ! -f "$LAYOUT_FILE" ]]; then
			      echo "No layout saved for profile: $PROFILE"
			      echo "Use 'mise run monitors-home list' to see available profiles"
			      exit 1
			    fi
			    
			    # Read the layout file and extract the displayplacer command
			    LAYOUT_CONFIG="$(cat "$LAYOUT_FILE")"
			    echo "Applying layout for profile: $PROFILE"
			    
			    # Extract the displayplacer command from the end of the file
			    # The command is on the last line that starts with "displayplacer"
			    DISPLAYPLACER_CMD="$(echo "$LAYOUT_CONFIG" | grep '^displayplacer ' | tail -n1)"
			    
			    if [[ -z "$DISPLAYPLACER_CMD" ]]; then
			      echo "Error: Could not find displayplacer command in layout file"
			      echo "The layout file may be corrupted or in an unexpected format"
			      exit 1
			    fi
			    
			    echo "Executing: $DISPLAYPLACER_CMD"
			    
			    # Execute the displayplacer command
			    eval "$DISPLAYPLACER_CMD"
			    
			    if [[ $? -eq 0 ]]; then
			      echo "Successfully restored layout: $PROFILE"
			    else
			      echo "Error: Failed to apply layout for profile: $PROFILE"
			      echo "The saved layout may be invalid or incompatible with current display setup"
			      exit 1
			    fi
			    exit 0
			  fi
			  
			  # Handle edit action
			  if [[ "$ACTION" == "edit" ]]; then
			    if [[ -z "$PROFILE" ]]; then
			      echo "Error: Profile name required for edit action"
			      echo "Usage: mise run monitors-home edit <profile>"
			      exit 1
			    fi
			    
			    LAYOUT_FILE="$HOME/.config/mise-monitor-layouts/${PROFILE}.layout"
			    if [[ ! -f "$LAYOUT_FILE" ]]; then
			      echo "No layout saved for profile: $PROFILE"
			      echo "Use 'mise run monitors-home list' to see available profiles"
			      exit 1
			    fi
			    
			    # Determine which editor to use
			    EDITOR_CMD=""
			    if [[ -n "${VISUAL:-}" ]]; then
			      EDITOR_CMD="$VISUAL"
			    elif [[ -n "${EDITOR:-}" ]]; then
			      EDITOR_CMD="$EDITOR"
			    else
			      echo "Error: No editor found. Please set VISUAL or EDITOR environment variable."
			      exit 1
			    fi
			    
			    echo "Opening layout file for profile '$PROFILE' with $EDITOR_CMD"
			    $EDITOR_CMD "$LAYOUT_FILE"
			    exit 0
			  fi
			  
			  echo "Unknown action: $ACTION"
			  echo "Valid actions: list, save, restore, edit"
			  exit 1
			  """
			  ~~~
		- ### 3. List available profiles
			- View existing layouts:
			  ```bash
			  mise run monitors-home list
			  ```
			- Or use the flag:
			  ```bash
			  mise run monitors-home --list
			  ```
		- ### 4. Save layout profiles
			- Save the *standing* configuration:
			  ```bash
			  mise run monitors-home save standing
			  ```
			- Save the *sitting* configuration:
			  ```bash
			  mise run monitors-home save sitting
			  ```
			- Alternative using flags:
			  ```bash
			  mise run monitors-home standing --save
			  ```
		- ### 5. Restore layout profiles
			- To restore standing:
			  ```bash
			  mise run monitors-home restore standing
			  ```
			- To restore sitting:
			  ```bash
			  mise run monitors-home restore sitting
			  ```
		- ### 6. Edit layout files (optional)
			- Edit a layout file directly:
			  ```bash
			  mise run monitors-home edit standing
			  ```
			- This opens the layout file in your preferred editor (uses [[EnvVar/VISUAL]] or falls back to [[EnvVar/EDITOR]])
	- ## Troubleshooting
		- *Command not found: displayplacer* → Run `brew install displayplacer`.
		- *No layout saved for profile* → Run with `save` action to store layout before restoring.
		- *Permission denied* → Make sure the layout directory and file are writable and readable.
		- *Failed to parse KDL document* → The layout file may be corrupted; try recreating it with the save action.
		- *No editor found* → Set [[EnvVar/VISUAL]] or [[EnvVar/EDITOR]] environment variable for the edit functionality.
		- *Argument parsing error* → Ensure you're using the correct action syntax (e.g., `mise run monitors-home restore standing`).
	- ## References
		- [displayplacer GitHub](https://github.com/jakehilborn/displayplacer)
		- [TOML Tasks Reference – Mise](https://mise.jdx.dev/tasks/toml-tasks.html)
		- [Usage Spec Documentation](https://usage.jdx.dev/spec/)