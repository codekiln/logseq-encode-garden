tags:: [[GitHub/CLI/Extension/gh-dash]], [[Diataxis/Tutorial]]
see-also:: [[GitHub/CLI/Extension]], [[GitHub/CLI]], [[GitHub/PR]]
- # Tutorial: Triage Pull Requests in the Terminal with [[GitHub/CLI/Extension/gh-dash]]
	- ## What You'll Create
		- We will open a pull-request dashboard for one repository, move through its three section tabs, narrow and widen the search behind a section, learn the review keys from the built-in help, and read a PR diff — all without leaving the terminal.
	- ## Prerequisites
		- [[GitHub/CLI]] authenticated. `gh auth status` should report `Logged in to github.com`.
		- gh-dash installed. `gh dash --version` should print a version banner.
		- A local checkout of a GitHub repository that has at least one open pull request. We will `cd` into it in step 1.
	- ## Learning Goals
		- Launch the dashboard and read its layout.
		- Recognize the three default pull-request sections and the search behind each one.
		- Control whether a section is scoped to one repository or to all of them.
		- Edit a section's filter for the current session.
		- Find any action's key from the help overlay, and read a diff.
	- ## Steps
		- ### 1. Launch the dashboard
			- `cd` into a repository checkout with open pull requests, then run
				- ```sh
				  gh dash
				  ```
			- Running with no arguments picks a configuration file in this order: a `.gh-dash.yml` in the current git repo, then `$GH_DASH_CONFIG`, then `~/.config/gh-dash/config.yml`. With none of the first two present, the global file is used.
			- You will see a tab strip across the top, a search bar in a rounded box, a table of pull requests on the left, and a preview pane on the right. The bottom bar shows `PRs`, `Issues`, the repo name, and `? help`.
		- ### 2. Read the three section tabs
			- The tab strip reads `My Pull Requests`, `Needs My Review`, `Involved`, each with a live count. Each tab is one saved GitHub search, defined in `~/.config/gh-dash/config.yml` under `prSections`.
				- | Tab                | Filter in `config.yml`                | Answers                                       |
				  | ------------------ | ------------------------------------- | --------------------------------------------- |
				  | My Pull Requests   | `is:open author:@me`                  | What have I got open?                          |
				  | Needs My Review    | `is:open review-requested:@me`        | Who is waiting on me?                          |
				  | Involved           | `is:open involves:@me -author:@me`    | What am I in, that I did not write?            |
			- Press `l` or `→` to move to the next section, `h` or `←` to move back. Notice the search bar text changes as you move — each tab really is a different query.
			- Press `j` and `k` (or `↓` and `↑`) to move down and up the list. The preview pane on the right follows the selection.
		- ### 3. Notice that every section is scoped to this repository
			- Look closely at the search bar on `My Pull Requests`. It reads something like
				- ```text
				  is:pr repo:codekiln/hiking-knowledge is:open author:@me
				  ```
			- The `repo:` term is not in `config.yml`. gh-dash added it because `smartFilteringAtLaunch: true` is set, which prepends the repository you launched from to **every** section's filter.
			- Press `l` to move to `Needs My Review` and confirm the same `repo:` term is there. Smart filtering is applied to all sections, not just the one in view.
		- ### 4. Widen the scope, then narrow it again
			- Press `t` to toggle smart filtering off. The `repo:` term disappears, the filter falls back to exactly what `config.yml` says, and the counts jump — every repository you have access to is now in scope.
			- Press `t` again to restore the repository scope.
			- This is the whole point of launching from a checkout: `gh dash` in a repo is a review queue for that repo, and `t` turns it into your review queue everywhere.
		- ### 5. Edit a section's filter
			- Press `/`. The search bar becomes an editable input, pre-filled with the full effective filter — including the `repo:` term smart filtering added.
				- A suggestion list opens under it, with its own footer: `↓/ctrl+n next • ↑/ctrl+p previous • ctrl+y select • ctrl+f refresh • ctrl+h toggle`.
			- Type a space and then `sort:created-asc` to append it, and press Enter.
			- The section refetches and the oldest pull request is now first. Any [[GitHub/Search]] syntax works here, so `draft:false`, `label:bug`, and `review:required` all narrow the same way.
			- Press `/` and then Escape to leave the filter untouched.
			- The edit lives in this session only — `~/.config/gh-dash/config.yml` is not rewritten. To keep a filter, edit `prSections` in that file yourself.
		- ### 6. Learn the review keys from the help overlay
			- Press `?`. A key map opens along the bottom of the screen. Press `?` again to close it.
				- | Key       | Action                       | Key       | Action                        |
				  | --------- | ---------------------------- | --------- | ----------------------------- |
				  | `v`       | approve                      | `c`       | comment                       |
				  | `m`       | merge                        | `d`       | diff                          |
				  | `C`/Space | checkout                     | `o`       | open in GitHub                |
				  | `a`       | assign                       | `y`       | copy number                   |
				  | `A`       | unassign                     | `Y`       | copy url                      |
				  | `L`       | label                        | `w`       | watch checks                  |
				  | `W`       | ready for review             | `V`       | approve all workflows         |
				  | `x`       | close                        | `u`       | update pr from base branch    |
				  | `X`       | reopen                       | `s`       | switch to issues              |
			- Navigation and view keys sit in the same overlay: `r` refresh, `R` refresh all, `p` toggle preview, `P` toggle preview position, `[` and `]` move through the preview's own tabs (`Overview`, `Activity`, `Commits`, `Checks`, `Files Changed`), `Ctrl+d` and `Ctrl+u` page the preview, `g` and `G` jump to the first and last item.
			- Press `s` to switch to the issues view. The tab strip becomes `My Issues`, `Assigned`, `Involved`, and the filter reads `is:issue …`. Press `s` again to return to pull requests.
		- ### 7. Read a diff
			- Select a pull request and press `d`.
			- The full diff opens in a pager, filling the terminal. Move a line at a time with `j` and `k`, search with `/`, and press `q` to return to the dashboard with your selection intact.
			- The pager is gh-dash's own default. Set `pager.diff` in `~/.config/gh-dash/config.yml` to route diffs through something else — `delta` is the usual choice.
		- ### 8. Leave
			- Press `q`. With `confirmQuit: false` in the config, gh-dash exits straight to the shell.
	- ## What You've Learned
		- `gh dash` launched from a repository checkout gives a review queue for that repository, because `smartFilteringAtLaunch` prepends `repo:` to every section.
		- `h`/`l` move between the three sections; each is a stored GitHub search, and `config.yml` is where their definitions live.
		- `t` toggles between "this repo" and "everywhere" without editing anything.
		- `/` edits the current section's filter for this session; Enter applies it, Escape cancels, and the config file is untouched either way.
		- `?` is the reference for every action — `v` approve, `m` merge, `d` diff, `C` checkout — and `s` swaps the whole dashboard between pull requests and issues.
