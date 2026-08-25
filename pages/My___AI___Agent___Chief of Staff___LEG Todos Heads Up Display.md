current-as-of:: 2026-08-25T09:41:51-04:00
see-also:: [[My/AI/Agent/Chief of Staff]], [[My/AI/Agent/Fleet]], [[Logseq/Journal]]

- # LEG Todos Heads Up Display
	- One line per item, ordered by priority, each with a path to open or a command to run. Reasoning and history live on [[My/AI/Agent/Chief of Staff/LEG Todos Heads Up Display/Detail]].
	- **`current-as-of::` above is the governing time.** Hayward sweeps it; if it is not from today, nothing here has been re-checked. Last swept by Hayward, first context window of [[2026-08-25 Tue]].
	- ## Waiting on you
		- TODO **Nine commits are unpushed, and `git push` sends all nine or none, because the held `e6ac3123` sits at the bottom of the stack.** You asked on [[2026-08-24 Mon]] to see those card pages before they reached a public repository, and no push has been instructed since.
			- ~~~sh
			  git -C ~/ghq/github.com/codekiln/logseq-encode-garden log --oneline origin/main..main && git -C ~/ghq/github.com/codekiln/logseq-encode-garden show e6ac3123
			  ~~~
		- TODO **`journals/2026_08_24.md` carries no [[Filed]] lines for the three card pages committed that day**, so Monday's record is short by three entries and one [[Updated]] line. Held because [[Logseq]] is running and your own edits are uncommitted in that file.
			- ~~~sh
			  nvim ~/ghq/github.com/codekiln/logseq-encode-garden/journals/2026_08_24.md
			  ~~~
		- TODO **An internal wiki URL carrying a page id is live in this public repository's history**, on a page deleted from the graph but present in commit `a81448b8`. One question decides it: is that URL plus a private AI-workspace project id sensitive on its own? If yes, a history rewrite plus a GitHub support purge is the only thing that reaches it, and it changes every commit hash this graph cites in its own prose.
			- ~~~sh
			  git -C ~/ghq/github.com/codekiln/logseq-encode-garden show a81448b8 -- 'pages/AI___Coding___Technique___Scoping Planning to .ai-coding dir with issue dir.md'
			  ~~~
		- TODO **[[Logseq/Journal]] and [[Logseq/Journal/Editorial headings]] instruct the narrative journal blocks you delete by hand**, so an agent following them reproduces the error, as this seat did on [[2026-08-24 Mon]]. Recommendation: delete [[Logseq/Journal/Editorial headings]] and cut the narrative instruction from [[Logseq/Journal]].
			- ~~~sh
			  nvim ~/ghq/github.com/codekiln/logseq-encode-garden/pages/Logseq___Journal.md ~/ghq/github.com/codekiln/logseq-encode-garden/'pages/Logseq___Journal___Editorial headings.md'
			  ~~~
		- TODO **235 of 450 journals have a first line with no bullet, and an editor save is what eats it** — today's journal went from `- # [[Filed]]` to `# [[Filed]]` during your own session on [[2026-08-24 Mon]]. Which editor is still open. Recommendation for the line form: `- # [[Filed]]`, the plurality and the only common form satisfying the bullet rule in `.claude/rules/logseq-core.md`.
			- ~~~sh
			  cd ~/ghq/github.com/codekiln/logseq-encode-garden && for f in journals/*.md; do head -1 "$f" | grep -qv '^- ' && echo "$f"; done
			  ~~~
		- TODO **35 `Person/Steve Yegge/Agent/*` pages become instances of `Logseq/Entity/Agent` the moment that type exists**, which is why creating it sets a convention rather than filing a page. Held since 2026-08-13.
			- ~~~sh
			  ls ~/ghq/github.com/codekiln/logseq-encode-garden/pages/Person___Steve\ Yegge___Agent___*
			  ~~~
		- TODO **[[Claude/Code/Settings]] and [[Claude/Code/Settings/Override]] both carry the settings precedence list**, both are right today, and they will come apart. Say which page owns it.
			- ~~~sh
			  nvim ~/ghq/github.com/codekiln/logseq-encode-garden/pages/Claude___Code___Settings.md ~/ghq/github.com/codekiln/logseq-encode-garden/pages/Claude___Code___Settings___Override.md
			  ~~~
		- TODO **`tmux/Keyshort/Copy Mode` uses a different word order from [[tmux/Mode/Copy]], which the graph already uses for the mode itself.** Say which name you want before the page accumulates references. Also on that page: a card answering `ENTER` for leaving copy mode already has live review state on [[tmux/Q/How do I get out of copy mode in tmux?]], and the new `Escape` card is about dropping a selection while staying in copy mode, which is easy to confuse under review.
			- ~~~sh
			  nvim ~/ghq/github.com/codekiln/logseq-encode-garden/'pages/tmux___Keyshort___Copy Mode.md'
			  ~~~
		- TODO **`Google/Workspace/AI` is the one alias worth adding of three considered**, and aliases are yours to curate. The other two: a relative-path phrasing for the Google Drive Markdown question, and `Claude/Google Drive`, which this seat would skip.
			- ~~~sh
			  grep -rn 'alias::' ~/ghq/github.com/codekiln/logseq-encode-garden/pages/ | grep -i google
			  ~~~
	- ## Repository state
		- **Nine commits ahead of `origin`, nothing behind, and four of your own files uncommitted** — `journals/2026_08_24.md`, `journals/2026_08_25.md`, [[Word/Salad]], [[My/Pref/Dev/Tool/git/Worktree]], plus the untracked `pages/ChatGPT___Remote___Voice.md`. Any count written here is stale the moment the seat commits again.
			- ~~~sh
			  cd ~/ghq/github.com/codekiln/logseq-encode-garden && git fetch origin && git rev-list --left-right --count origin/main...main && git status --short
			  ~~~
		- **The identity guard runs on every commit now, and a whole-repo scan finds nothing.** It had never executed once before [[2026-08-24 Mon]], because `lefthook install` was never run in this clone.
			- ~~~sh
			  cd ~/ghq/github.com/codekiln/logseq-encode-garden && ls .git/hooks | grep -v sample && mise run secrets:scan
			  ~~~
		- **`tmp/` is tracked and published in this repository**, unlike the other gardens the fleet works in, so working notes written there are public.
			- ~~~sh
			  cd ~/ghq/github.com/codekiln/logseq-encode-garden && git ls-files tmp/
			  ~~~
		- **This checkout is shared and you edit in it live**, so any clean reading here describes a moment rather than a state that holds.
	- ## Closed, with the reasoning kept
		- Every call this seat settled rather than asked, and why, is on [[My/AI/Agent/Chief of Staff/LEG Todos Heads Up Display/Detail]]. Items leave this display when they close and keep their reasoning there.
