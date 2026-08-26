current-as-of:: 2026-08-26T12:10:48-04:00 ET
see-also:: [[My/AI/Agent/Chief of Staff/LEG Todos Heads Up Display]], [[My/AI/Agent/Chief of Staff/LEG Todos Heads Up Display/Detail]], [[My/AI/Agent/Chief of Staff]]

- # LEG Parked
	- Work in [[My/Knowledge/Garden/logseq-encode-garden]] that Hayward went looking for and found, where the next step is a decision rather than more measuring. [[My/AI/Agent/Chief of Staff/LEG Todos Heads Up Display]] holds what [[Person/codekiln]] asked for; this page holds what nobody has asked for yet.
	- **The order below is Hayward's guess at your priority, and that guess is the only thing ranking these.** `current-as-of::` above is the governing time.
	- ## A dead formatter hook sits in `.rulesync/hooks.json` and cannot fire
		- The file declares a `postToolUse` hook on `Write|Edit` running `.rulesync/hooks/format.sh`. That script is absent — `.rulesync/hooks/` is not a directory — and `hooks` is missing from the `features` list in `rulesync.jsonc`, so a generate would not emit it either. Inert since [f18285e2 a bunch of rulesync skill updates](https://github.com/codekiln/logseq-encode-garden/commit/f18285e2). Deleting the file costs nothing; keeping it means someone eventually writes the script. Measured at source 2026-08-26.
			- ~~~sh
			  cd ~/ghq/github.com/codekiln/logseq-encode-garden && cat .rulesync/hooks.json && ls .rulesync/hooks/ ; grep -n -A9 '"features"' rulesync.jsonc
			  ~~~
	- ## The links to `docs.claude.com` all still work, so repairing them is tidying rather than repair
		- Fifteen unique addresses across fourteen pages redirect rather than break, and they split two ways: Claude Code slugs land on `code.claude.com/docs/en/<slug>` and everything else on `platform.claude.com/docs/en/<path>`, so a single host substitution would send three of them to the wrong place. Measured 2026-08-26 by following three of them with `curl -L`, each returning 200. The `claude config` half of this is the part that is genuinely broken and it is on the display.
			- ~~~sh
			  cd ~/ghq/github.com/codekiln/logseq-encode-garden && git grep -o -h -P 'https://docs\.claude\.com[^\s\)\]`"]*' -- pages journals .rulesync | sort -u
			  ~~~
	- ## Two aliases are worth adding and one is not, and all three are yours to write
		- `.claude/rules/logseq-core.md` treats aliases as human-curated, so these stay suggestions. [[Google/Workspace/AI]] is the one Hayward recommends. A relative-path phrasing for the Google Drive Markdown question would help it surface. `Claude/Google Drive` would be skipped, because the pages it would gather already sit under names people search. Neither `pages/Google___Workspace___AI.md` nor `pages/Claude___Google Drive.md` exists on disk today.
	- ## A current list of Claude Code tools has no home
		- The stale tools table came off [[Claude/Code/Settings]] and nothing replaced it. A current list would be useful and belongs on its own page rather than back inside the settings page, where it went stale the first time. `pages/Claude___Code___Tool___ccusage.md` and `pages/Claude___Code___Tool___Claude Code Terragon.md` are the only two pages under that namespace today.
	- ## The fullest statement of your pointer rule lives in a dotfiles agent record, in a file that says it should not
		- `agent-records/seneschal-seat.md:250` in [[My/Dotfiles]] carries all three parts of the rule plus the identifier distinction, and a few bullets below it the same file says lasting opinions belong in the knowledge garden rather than in a repository. [[My/AI/Rule/How to Communicate Effectively With Me/A pointer carries a link, an id with a slug, and a reason]] now exists here, so that bullet can be cut to a link at it. The file belongs to another repository and another seat.
			- ~~~sh
			  sed -n '245,258p' ~/ghq/github.com/codekiln/dotfiles/agent-records/seneschal-seat.md
			  ~~~
	- ## Two ticket placeholders are in use, and one of them looks like a live project key
		- [[git/commit/Conventional/gitmoji]] and the `git-conventions` skill both illustrate the ticket line with `PD-12345`, while [[My/Pref/Dev/Tool/SCM/Commit Message Style Preferences]] and [[My/Pref/Dev/Tool/git/Worktree]] use `AB-1234`. Whether `PD` is a project key you actually file against decides whether the public repository cares about this; Hayward did not establish that either way.
			- ~~~sh
			  cd ~/ghq/github.com/codekiln/logseq-encode-garden && git grep -n 'PD-1' -- pages .rulesync
			  ~~~
	- ## The sweep for bare commit hashes needs a check that works before it needs a decision
		- [[My/AI/Rule/How to Communicate Effectively With Me/A pointer carries a link, an id with a slug, and a reason]] makes a bare hash measurable, and the two patterns Hayward tried both produced unusable lists: `[0-9a-f]{7,8}` matches ordinary words spelled in a-f, and adding a git word to the line matches the UUID fragments inside `share.snipd.com` links. One instance is confirmed by hand, the `84f0092` on [[git/reflog]] that the rule page cites as its own example. A count of the rest is a job for a contractor with a real check.
			- ~~~sh
			  cd ~/ghq/github.com/codekiln/logseq-encode-garden && grep -n '84f0092' pages/git___reflog.md
			  ~~~
