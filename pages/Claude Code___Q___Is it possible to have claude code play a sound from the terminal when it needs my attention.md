tags:: [[Claude Code]], [[Q]], [[Terminal]], [[Notification]]

- # Is it possible to have [[Claude Code]] play a sound from the terminal when it needs my attention?
	- ## Summary
		- Yes, Claude Code supports multiple methods for terminal sound notifications when it needs attention or finishes tasks
		- Options include built-in terminal bell support and customizable hooks for OS-level notifications
	- ## Built-in Terminal Bell
		- Claude Code has built-in support for terminal bell notifications
		- Configure using:
			- ~~~
			  claude config set --global preferredNotifChannel terminal_bell
			  ~~~
		- This uses the ASCII BEL character (`\a`) to trigger terminal bell sounds
		- To test if terminal bell is working:
			- ~~~
			  echo -e "\a"
			  ~~~
			- If you hear a sound, the bell is working
	- ## Terminal Bell Configuration
		- ### macOS Terminal
			- Terminal → Settings → Profiles → Advanced
			- Enable "Audible bell" under the Bell section
		- ### GNOME Terminal
			- Preferences → Profiles → Text
			- Check "Terminal bell" option
		- ### IDE Integrated Terminals (VSCode, Cursor, etc.)
			- Terminal bell **can** work in IDE terminals, but requires specific configuration
			- #### VSCode Configuration
				- Add to `settings.json`:
					- ~~~
					  {
					    "accessibility.signals.terminalBell": {
					      "sound": "on",
					      "announcement": "auto"
					    },
					    "editor.accessibilitySupport": "on",
					    "terminal.integrated.enableVisualBell": false
					  }
					  ~~~
				- For older VSCode versions, also add:
					- ~~~
					  "terminal.integrated.enableBell": true
					  ~~~
				- Test with: `echo -e "\a"` or `printf '%s' $'\a'`
			- #### Cursor Configuration
				- Settings → Features → Chat → Enable "Play sound on finish"
				- Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) → "Help: List Signal Sounds" → Enable "Task Completed"
				- Note: Cursor's built-in sounds are for chat/agent completion, not terminal bell
				- For terminal bell in Cursor, use VSCode-style settings (Cursor is VSCode-based)
					- Add to `settings.json`:
						- ~~~
						  {
						    "accessibility.signals.terminalBell": {
						      "sound": "on",
						      "announcement": "auto"
						    },
						    "editor.accessibilitySupport": "on"
						  }
						  ~~~
			- #### Alternative: Use Hooks
				- If terminal bell still doesn't work after configuration, use hooks (see Hooks section below) for reliable notifications
		- ### Windows/WSL
			- Terminal bell may not work reliably
			- Use PowerShell hooks instead (see Hooks section below)
	- ## Hooks for Custom Notifications
		- Claude Code supports hooks that can execute commands at specific events
		- Configure hooks in `~/.claude/settings.json` or `CLAUDE.md`
		- Available hook events:
			- `Stop`: Triggered when Claude finishes a task
			- `Notification`: Triggered when Claude needs your input
	- ## macOS Hook Examples
		- ### Play System Sound
			- ~~~
			  {
			    "hooks": {
			      "Stop": [
			        {
			          "hooks": [
			            {
			              "type": "command",
			              "command": "afplay /System/Library/Sounds/Funk.aiff"
			            }
			          ]
			        }
			      ],
			      "Notification": [
			        {
			          "hooks": [
			            {
			              "type": "command",
			              "command": "say \"Claude needs your input\""
			            }
			          ]
			        }
			      ]
			    }
			  }
			  ~~~
		- This configuration:
			- Plays a system sound when Claude finishes (`Stop` event)
			- Uses text-to-speech to announce when Claude needs input (`Notification` event)
	- ## Windows/WSL Hook Examples
		- ### PowerShell Beep
			- ~~~
			  {
			    "hooks": {
			      "Stop": [
			        {
			          "hooks": [
			            {
			              "type": "command",
			              "command": "powershell.exe -c \"[System.Media.SystemSounds]::Beep.Play()\""
			            }
			          ]
			        }
			      ],
			      "Notification": [
			        {
			          "hooks": [
			            {
			              "type": "command",
			              "command": "powershell.exe -c \"[System.Media.SystemSounds]::Question.Play()\""
			            }
			          ]
			        }
			      ]
			    }
			  }
			  ~~~
	- ## Common Issues and Solutions
		- ### No sound after enabling terminal_bell
			- **macOS Terminal app**: Ensure Terminal profile has Bell enabled in settings
			- **VSCode**: Verify `accessibility.signals.terminalBell.sound` is set to `"on"` and `editor.accessibilitySupport` is `"on"` in settings.json
			- **Cursor**: Enable terminal bell via settings.json (same as VSCode) - note that Cursor's built-in "Play sound on finish" is for chat completion, not terminal bell
			- **IDE terminals**: If still not working after configuration, try restarting the IDE or use hooks instead
			- **Windows/WSL**: Use PowerShell hooks instead of terminal bell
		- ### Bells are too quiet or ignored
			- Increase system volume
			- Check OS sound settings - sometimes "alert" or "system sounds" are muted
		- ### Hook commands don't run
			- Verify `~/.claude/settings.json` or `CLAUDE.md` has correct hook syntax
			- Test commands manually to ensure they work outside of Claude Code
	- ## Answer
		- Yes, it is possible to have Claude Code play a sound from the terminal when it needs attention
		- Recommended approaches:
			- **For IDE integrated terminals (VSCode, Cursor)**: 
				- Configure terminal bell in IDE settings (see Terminal Bell Configuration section)
				- Or use hooks for more reliable cross-platform notifications
			- **For standalone terminal apps (macOS Terminal, iTerm, etc.)**: Terminal bell works with proper configuration
			- **For custom sounds/announcements**: Configure hooks in `~/.claude/settings.json` or `CLAUDE.md`
			- **For macOS**: Use `afplay` with system sounds or `say` for text-to-speech
			- **For Windows/WSL**: Use PowerShell commands to play system sounds
		- **Note**: Terminal bell (`terminal_bell`) can work in IDE terminals with proper configuration, but hooks provide more flexibility and reliability across all environments
