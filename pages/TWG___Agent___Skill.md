logseq-entity:: [[Logseq/Entity/Concept]]
created-by:: [[Atlassian]]
see-also:: [[TWG]], [[Agent/Skills]], [[Atlassian/MCP]]

- # [[TWG]] [[Agent/Skills]]
	- Atlassian publishes the agent skills for the `twg` CLI in [atlassian/twg-cli/skills](https://github.com/atlassian/twg-cli/tree/main/skills), as `skills/<name>/SKILL.md` "for Codex-style skill installers". The repository has no tags or releases; Atlassian syncs `skills/` from its private release export, so it can lag the latest binary.
	- The `twg` binary carries its own copy. `twg skills install` writes it to `~/.agents/skills` (Codex, Cursor, Gemini, Copilot) plus `~/.claude/skills` with `--agent claude`; `--local` writes into the current directory instead. Each installed skill gets a `.twg-install.json` marker, which `twg upgrade` uses to find skills to refresh.
	- `twg setup` installs the skills, signs in, and enables upkeep. `twg login` only signs in.
	- The root skill is `twg`; the others are per product or per workflow, for example `twg-jira`, `twg-confluence`, `twg-engineering-work`, `twg-status-rollups`.
	- Each skill ships a `LICENSE.txt` that places it under the Atlassian Customer Agreement and restricts copies outside Atlassian's services, even though the repository itself is Apache-2.0.
	- [atlassian-labs/twg-plugins](https://github.com/atlassian-labs/twg-plugins) packages TWG as marketplace plugins for Claude, Codex, Cursor and others; its `skills/` holds only `twg-setup`.
