logseq-entity:: [[Logseq/Entity/Question]]
tags:: [[Question]]

- # What [[Obsidian]] tools are there for integrating with Atlassian [[Jira]] to easily make a digital twin of any ticket?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** There is no official Obsidian↔Jira product integration. For a **per-ticket digital twin** (a real note in the vault that mirrors Jira fields and stays queryable in the graph), prioritize **Jira Shadow**; for **edit-in-Obsidian, push-back-to-Jira** twins, use **Jira Issue Manager** (plugin id `jira-sync`, repo [Alamion/obsidian-jira-sync](https://github.com/Alamion/obsidian-jira-sync)). **Jira Issue** ([marc0l92/obsidian-jira-issue](https://github.com/marc0l92/obsidian-jira-issue)) is the mature choice for **live embeds** in notes, not one markdown file per issue.
			- **Closest to “digital twin” (file per issue)**
				- **[Jira Shadow](https://github.com/walievi/obsidian-jira-shadow)** — Syncs (“shadows”) issues into **actual markdown files** under folders you configure; Jira fields land in **YAML frontmatter** so **Dataview**, links, and graph view work on twins. JQL-based filters (e.g. sprint, assignee) target a destination folder. Designed to run **alongside** Jira Issue for dynamic views. Newer/smaller project (verify release maturity before production).
			- **Twin you edit locally, then sync to Jira**
				- **Jira Issue Manager** — Community name; plugin id **`jira-sync`**. Fork/evolution of [obsidian-to-jira](https://github.com/angelperezasenjo/obsidian-to-jira). Commands such as fetch issue by key into a note, edit with template/indicator syntax, then **Update issue in Jira**; supports **custom fields**, partial updates, conflict handling, worklog batching. Best when the twin must stay **writable** and authoritative in Jira after sync.
				- **Obsidian to Jira** ([angelperezasenjo/obsidian-to-jira](https://github.com/angelperezasenjo/obsidian-to-jira)) — Simpler: import issue to `jira-issues/`, create/update from frontmatter (`key`, `priority`, `summary`). Good minimal baseline; superseded feature-wise by Jira Issue Manager for heavy workflows.
			- **Live Jira data inside notes (not a vault file per ticket)**
				- **Jira Issue** — Plugin id **`jira-issue`**. Blocks: `jira-issue`, `jira-search`, `jira-count`; inline `JIRA:PROJ-123` and browse URLs render as chips. ~295 GitHub stars; active releases through **2025**. Strong for dashboards and meeting notes; weak fit if every ticket must be its **own** linked note in the graph.
			- **Practical pick for your goal**
				- **Easiest “one file = one ticket” twin:** try **Jira Shadow** first (JQL filter + destination folder + API token for Atlassian Cloud).
				- **Easiest “I work the ticket in Obsidian and push status/fields back”:** **Jira Issue Manager** (`jira-sync`).
				- **Hybrid:** Jira Shadow for file twins + Jira Issue for inline status in daily notes (Jira Shadow docs claim compatibility).
			- **Outside Obsidian plugins**
				- **Atlassian MCP** (e.g. [[Atlassian/MCP]]) plus an **Obsidian MCP** server can script fetch/update via agents, but that is not “one click, one twin file” inside Obsidian unless you build templates/automation yourself.
			- **Auth note:** Cloud instances typically use **email + API token** ([id.atlassian.com](https://id.atlassian.com/manage-profile/security/api-tokens)); Server/Data Center may differ per plugin docs.
			- ### Sources
				- [marc0l92/obsidian-jira-issue](https://github.com/marc0l92/obsidian-jira-issue) — [docs](https://marc0l92.github.io/obsidian-jira-issue/)
				- [walievi/obsidian-jira-shadow](https://github.com/walievi/obsidian-jira-shadow)
				- [Alamion/obsidian-jira-sync](https://github.com/Alamion/obsidian-jira-sync) — Obsidian Stats: [Jira Issue Manager](https://www.obsidianstats.com/plugins/jira-sync)
				- [angelperezasenjo/obsidian-to-jira](https://github.com/angelperezasenjo/obsidian-to-jira)
