logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Person/David Rogers]]

- # [aistat](https://github.com/drogers0/aistat)
	- GitHub repository: [drogers0/aistat](https://github.com/drogers0/aistat) — 14 [[GitHub/Star]]s, checked [[2026/10/16 Fri]].
	- A Go command-line tool that reports Claude Code, Codex, and GitHub Copilot usage limits from their existing credential stores; it can also switch stored Claude and Codex accounts.
	- Runs on macOS, Linux, and Windows through Git Bash or WSL.
	- ## Security review
		- Review required before installation or use; the small adoption footprint makes independent inspection especially important.
		- The installer downloads a release archive and checksum file from the same GitHub release, verifies the SHA-256 checksum, then removes macOS quarantine from the installed binary. Verify the release and installation path independently before running it.
		- The CLI reads provider credentials and sends authenticated requests to provider usage endpoints. Its account-switch command can rewrite the active Claude or Codex credential shared by other sessions on the device; review token handling and credential writes before using that command.
		- Review sources: [installer](https://github.com/drogers0/aistat/blob/main/install.sh), [README and authentication behavior](https://github.com/drogers0/aistat#authentication).
