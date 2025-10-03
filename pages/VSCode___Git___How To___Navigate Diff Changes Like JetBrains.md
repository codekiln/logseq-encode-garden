tags:: [[VSCode]], [[Diataxis/How To]]

- # How To Navigate Diff Changes Like [[JetBrains]] or [[PyCharm]] IDEs in [[VSCode]] and [[git]] [[CLI/Tool]]s
	- ## Overview
		- This guide helps developers who are accustomed to JetBrains/PyCharm diff navigation quickly implement equivalent functionality in VSCode and CLI environments
		- Provides step-by-step instructions for navigating between diff hunks/changes in VSCode's diff viewer and popular CLI diff tools
		- Focuses on practical, keyboard-driven workflows that match JetBrains: F7 for next change, Shift+F7 for previous change
	- ## Prerequisites
		- VSCode installed and configured
		- Familiarity with JetBrains keyboard shortcuts (F7/Shift+F7)
		- Basic understanding of Git workflows
		- Terminal/CLI access for CLI tool options
	- ## Research
		- ### VSCode Diff Navigation Shortcuts
			- VSCode has built-in accessible diff viewer shortcuts that match JetBrains behavior
			- Commands: `editor.action.accessibleDiffViewer.next` and `editor.action.accessibleDiffViewer.prev`
			- Default keybindings: `F7` and `Shift+F7` (requires diff editor context)
			- Context requirement: `when: "isInDiffEditor"` - shortcuts only work when viewing diffs
		- ### Current Issue Analysis
			- User reports "Current editor isn't a diff editor" error when trying `Alt+J`/`Alt+K`
			- This occurs because `Alt+J/K` shortcuts are specific to GitHub Pull Requests extension (`pr.goToNextDiffInPr`/`pr.goToPreviousDiffInPr`)
			- These shortcuts only work in GitHub PR review context, not general diff viewing
		- ### Available Options
			- **VSCode Built-in**: Accessible diff viewer with F7/Shift+F7
			- **VSCode Extensions**: GitLens for enhanced Git diff viewing
			- **CLI Tools**: LazyGit, delta, git difftool with vim-like editors
			- **Alternative IDE Approach**: Use VSCode's Git functionality more strategically
	- ## Steps: VSCode Solution
		- ### 1. Verify Current Diff Navigation Shortcuts
			- Open VSCode Command Palette (`Cmd+Shift+P` on macOS)
			- Type: "Preferences: Open Keyboard Shortcuts"
			- Search for: "diff.next" and "diff.prev"
			- Confirm shortcuts are set to `F7` and `Shift+F7`
		- ### 2. Configure Custom Keybindings (if needed)
			- Open your keybindings.json file: "Preferences: Open Keyboard Shortcuts (JSON)"
			- Add custom bindings if defaults not working:
			  ~~~
			  {
			   "key": "f7",
			   "command": "editor.action.accessibleDiffViewer.next",
			   "when": "isInDiffEditor"
			  },
			  {
			   "key": "shift+f7", 
			   "command": "editor.action.accessibleDiffViewer.prev",
			   "when": "isInDiffEditor"
			  }
			  ~~~
		- ### 3. Access Diff Views Correctly
			- #### Method A: Source Control Panel
				- Open Source Control (`Cmd+Shift+G`)
				- Click on changed file in Changes section
				- Diff view opens with F7/Shift+F7 navigation available
			- #### Method B: GitLens Branch Comparison
				- Follow existing guide: [[VSCode___How To___Diff a file with another branch]]
				- Use "Open Changes with Working File" option
				- Diff viewer supports F7/Shift+F7 navigation
		- ### 4. Enable Accessible Diff Viewer Features
			- Ensure "Editor: Accessible Diff Viewer" setting is enabled
			- Command Palette: "Preferences: Open Settings (UI)"
			- Search: "accessible diff"
			- Enable: "Editor › Accessible Diff Viewer"
	- ## Steps: CLI Alternative Solutions
		- ### 1. LazyGit Configuration
			- Install LazyGit: `brew install lazygit` (macOS) or appropriate package manager
			- Launch: `lazygit` in terminal
			- Navigate changes panel with arrow keys, Enter to view file diff
			- Within diff view: `j`/`k` for navigation, `Space` for page down
			- `q` to exit diff, `Esc` to return to main view
		- ### 2. Delta Enhanced Git Diff
			- Install delta: `brew install git-delta`
			- Configure in `~/.gitconfig`:
				- `git config --global core.pager delta`
				- `git config --global interactive.diffFilter 'delta --color-only'`
			- Use standard git diff: `git diff` (pager handles navigation)
		- ### 3. Git Difftool Integration
			- Configure difftool: `git config --global diff.tool vimdiff`
			- Launch diff: `git difftool HEAD~1`
			- Navigate with: `]c` (next change), `[c` (previous change)
	- ## Alternative Approaches
		- ### VSCode Files Explorer Integration
			- Highlight changed files in Explorer panel
			- Right-click → "Open Changes" for git diff view
			- Use F7/Shift+F7 within diff view
		- ### Command Palette Diff Creation
			- `Cmd+Shift+P`: "File: Compare Active File With..."
			- Select comparison target (clipboard, saved file, etc.)
			- Diff opens with F7/Shift+F7 navigation
	- ## Troubleshooting
		- ### "Current editor isn't a diff editor" Error
			- **Cause**: Trying to use GitHub PR shortcuts (`Alt+J`/`Alt+K`) outside PR context
			- **Solution**: Use VSCode's native diff shortcuts (`F7`/`Shift+F7`) in proper diff context
			- **Verification**: Ensure you're in diff editor by checking tab title or editor mode
		- ### Shortcuts Not Working in Diff View
			- Check keyboard shortcuts configuration
			- Verify `isInDiffEditor` context condition
			- Try alternative: Command Palette → search "Diff Editor: Next Change"
		- ### CLI Tools Integration Issues
			- Ensure tools properly configured in PATH
			- Check Git configuration: `git config --list | grep diff`
			- Verify pager settings don't conflict
	- ## Verification Checklist
		- [ ] F7 navigates to next diff hunk in VSCode diff view
		- [ ] Shift+F7 navigates to previous diff hunk in VSCode diff view
		- [ ] Navigation works in Source Control diff view
		- [ ] Navigation works in branch comparison diff view
		- [ ] CLI tool (LazyGit/delta) provides equivalent functionality
		- [ ] Smooth transition from JetBrains workflow achieved
	- ## Related
		- [[VSCode/How To/Diff a file with another branch]]
		- [[VSCode/Docs/User Guide/Code Navigation]]
		- [[VSCode/How To/Go To Next and Previous Changes When Reviewing Github Pull Requests]]
