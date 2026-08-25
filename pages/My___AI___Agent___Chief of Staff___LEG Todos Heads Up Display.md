current-as-of:: 2026-08-25T09:52:24-04:00
see-also:: [[My/AI/Agent/Chief of Staff]], [[My/AI/Agent/Fleet]], [[Logseq/Journal]]

- # LEG Todos Heads Up Display
	- What in [[My/Knowledge/Garden/logseq-encode-garden]] needs [[Person/codekiln]] rather than Hayward. An item earns a place here only if Hayward acting alone could not be undone cheaply; everything Hayward can decide is decided and recorded on [[My/AI/Agent/Chief of Staff/LEG Todos Heads Up Display/Detail]].
	- **`current-as-of::` above is the governing time.** Last swept by Hayward, first context window of [[2026-08-25 Tue]].
	- ## Waiting on you
		- TODO **An internal wiki URL carrying a page id is live in this public repository's history**, on a page deleted from the graph but present in commit `a81448b8`. This is here because a history rewrite cannot be undone: it changes every commit hash, this graph cites its own hashes in prose, and existing clones and forks keep the old objects regardless. One question decides it — is that URL, with a private AI-workspace project id, sensitive on its own?
			- ~~~sh
			  git -C ~/ghq/github.com/codekiln/logseq-encode-garden show a81448b8 -- 'pages/AI___Coding___Technique___Scoping Planning to .ai-coding dir with issue dir.md'
			  ~~~
	- ## Decided by Hayward today, reversible if wrong
		- **[[Logseq/Journal]] and [[Logseq/Journal/Editorial headings]] now say you write the narrative and an agent writes only the [[Filed]] and [[Updated]] log.** They previously instructed the blocks you delete by hand, and an agent following them reproduced the deletion twice. [[Logseq/Journal]] also now states the line form as `- # [[Filed]]`, with the bullet.
		- **[[Logseq/Entity/Agent]] exists**, covering both shapes already in the graph: your own roles under `My/AI/Agent/<Role>`, and another person's roster under `Person/<Name>/Agent/<Name> - <Role>`, which is what the 35 pages under [[Person/Steve Yegge/Agent]] are. Creating the type reclassifies nothing on its own, since a page joins a type only by carrying `logseq-entity::`.
		- **[[tmux/Keyshort/Copy Mode]] keeps that name.** It reads as a group name where `Mode/Copy` reads as a path, and it created no new namespace segment.
		- **The settings precedence question was wrong rather than open.** [[Claude/Code/Settings/Override]] is the page whose subject is precedence and it owns the detail; [[Claude/Code/Settings]] carries one summary line and already points at it. Nothing needed changing.
		- **The 235 journals whose first line lost its bullet stay as they are.** An editor save eats it, so rewriting them reintroduces the same state on the next save. Fixing the editor is the only thing that would hold.
		- **`Google/Workspace/AI` is the alias worth adding** and it is not written, because `.claude/rules/logseq-core.md` says aliases are yours to curate and an agent suggests them in conversation rather than on a page.
	- ## Repository state
		- **Level with `origin` and clean of Hayward's work.** Whatever `git status` shows is yours; Hayward stages only its own lines, even inside a file you are editing.
			- ~~~sh
			  cd ~/ghq/github.com/codekiln/logseq-encode-garden && git fetch origin && git rev-list --left-right --count origin/main...main && git status --short
			  ~~~
		- **The identity guard runs on every commit and a whole-repo scan finds nothing.** It had never run before [[2026-08-24 Mon]], because `lefthook install` was never run in this clone.
		- **`tmp/` is tracked and published here**, unlike the other gardens the fleet works in, so working notes written there are public.
	- ## Why an item is not here
		- Hayward decides anything reversible and records it on [[My/AI/Agent/Chief of Staff/LEG Todos Heads Up Display/Detail]] rather than asking. What reaches this display is work that is public, irreversible, or sets a convention across the graph.
