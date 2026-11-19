logseq-entity:: [[Logseq/Entity/Software/Project]]

- # [github/gh-actions-lock](https://github.com/github/gh-actions-lock)
	- [[GitHub/Star]]: 392 (checked [[2026-11-19 Thu]]).
	- [[GitHub/CLI/Extension]] that generates and verifies `.github/workflows/actions.lock`, the [[Lockfile]] for [[GitHub/Action]] dependencies. It pins every direct and transitive action a repository's workflows use to a commit SHA, so a moved tag or a hijacked action shows up in a pull request diff instead of running.
	- GitHub made the workflow lockfile generally available on 2026-10-28.
	- ## Commands
		- `gh actions-lock` — scan every workflow under `.github/workflows/`, pin each resolvable action, and write the lockfile. Rerun it after adding a workflow or changing a `uses:`.
		- `gh actions-lock --relock` — advance moved refs such as `main` or `v4` to their current upstream commit.
		- `gh actions-lock --verify` — CI check that writes nothing and fails when the lockfile is incomplete.
		- `gh actions-lock --verify-local` — offline pre-commit check that every `uses:` has a lockfile entry. Checks coverage only, not provenance.
		- `gh actions-lock --no-fix` — read-only report; add `--json` for structured output.
	- A freshly pinned partial ref such as `actions/checkout@v4` narrows to the highest matching full semver tag, such as `v4.2.1`. `--no-narrow` keeps the partial ref.
	- ## Limits
		- Reusable workflows called at `jobs.<id>.uses` from another repository are not locked.
		- Container images are not locked; an image without an `@sha256:` digest is a warning.
		- Supports github.com and GitHub Enterprise Cloud with data residency (`*.ghe.com`), not GitHub Enterprise Server.
	- ## Install
		- ~~~bash
		  gh extension install github/gh-actions-lock
		  ~~~
		- Declared in the dotfiles at `chezmoi/dot_config/gh/extensions.txt`, alongside [[gh-dash]] and [[GitHub/CLI/Extension/gh-sub-issue]].
	- MIT, [v0.5.0](https://github.com/github/gh-actions-lock/releases/tag/v0.5.0) released 2026-11-19.
	- Written in [[Go]].
