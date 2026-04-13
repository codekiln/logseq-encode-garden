logseq-entity:: [[Logseq/Entity/question]]
tags:: [[Question]]

- # Does [[Obsidian]] have an **official** MCP or AI agent skill collection? If not, are there any community skills or MCPs that are by far more popular and recently updated than others?
	- ## Answer
		- [[AI/Response]]
			- **Agent skills (closest to “official”):** Obsidian does not use the phrase “official skills” in its help site the same way, but the de facto standard pack is **[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)** — maintained by Steph Ango (*kepano*, Obsidian’s CEO). The repo describes **Agent Skills** for Obsidian (Markdown, Bases, JSON Canvas, CLI, Defuddle) following the [Agent Skills specification](https://agentskills.io/specification), with install paths for Claude Code, Codex CLI, OpenCode, marketplace, and `npx skills`. That is the dominant, company-led open-source skill collection for Obsidian-aware agents as of early 2026.
			- **MCP:** There is **no first-party “Obsidian MCP”** from Obsidian Ltd. bundled like vendor-official servers (compare e.g. GitHub’s official server in the [MCP servers catalog](https://github.com/modelcontextprotocol/servers)). Vault access for agents is almost entirely **community MCP servers**, usually layered on the **[Local REST API](https://github.com/coddingtonbear/obsidian-local-rest-api)** community plugin or direct filesystem access.
			- **Community MCPs — popularity vs. recency:** Nothing cleanly “wins both” today.
				- **Most popular by GitHub stars:** **[MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)** (Python, `uvx`/`uv`, REST API plugin; on the order of **3.3k** stars). It is the default recommendation in many tutorials, but **maintenance has slowed** (last significant activity in **mid‑2025** per the public default-branch timeline — verify before you depend on it).
				- **Other widely used options:** **[StevenStavrakis/obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp)** (TypeScript, direct vault path; **hundreds** of stars, **mid‑2025** last push in the public timeline) and **[cyanheads/obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server)** (TypeScript, REST API bridge; **~440** stars, **Oct 2025** last push).
				- **Smaller star count but newer commits:** **[smith-and-web/obsidian-mcp-server](https://github.com/smith-and-web/obsidian-mcp-server)** had **very low** star count relative to the leaders as of this check, but showed **2026** activity on the default branch — useful if you prioritize **fresh commits** over social proof.
			- **Practical takeaway:** For **skills**, start with **kepano/obsidian-skills**. For **MCP**, pick by **architecture** (REST API vs. filesystem), **security** (API key, vault path exposure), and **your own audit** of issues and commit dates — the **highest‑star** server is **not** automatically the most actively maintained.
			- ### Sources
				- [kepano/obsidian-skills (README)](https://github.com/kepano/obsidian-skills/blob/main/README.md)
				- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) (reference/community server index; no Obsidian‑Ltd. product MCP)
				- [MarkusPfundstein/mcp-obsidian](https://github.com/MarkusPfundstein/mcp-obsidian)
				- [cyanheads/obsidian-mcp-server](https://github.com/cyanheads/obsidian-mcp-server)
				- [StevenStavrakis/obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp)
				- [smith-and-web/obsidian-mcp-server](https://github.com/smith-and-web/obsidian-mcp-server)
				- [coddingtonbear/obsidian-local-rest-api](https://github.com/coddingtonbear/obsidian-local-rest-api) (common prerequisite for REST‑style MCP servers)
