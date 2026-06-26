alias:: [[Logseq/Entity/software-project]]
logseq-entity:: [[Logseq/Entity/Definition]]

- # Software Project
	- In this garden, **Software Project** pages model software products: applications for end users, libraries, frameworks, CLIs, desktop or web apps, editors, runtimes, and the like.
	- ## Examples in this garden
		- [[Yamtrack]], [[nvim]], [[Lazygit]], and [[tmux]] show how we name and shape software project pages. Use them as reference.
	- ## How to name the main page for a software project
		- Give a software entity a root-level one-word or short main page when its primary name is not confusing and it is either reputable or nascent but likely to grow sub-namespaces for shortcuts, config, docs, or related notes. A short main name leaves room; long names (`owner/repo` or `person/project`) make every child path longer and harder to work with. Example: [[Lazygit]] rather than `Person/Jesse Duffield/GitHub/Lazygit`. Aliases can point from other namespaces, such as `Programming/Language/Rust` or `Person/Name/GitHub/Project`, to that main page when useful.
		- When the garden is tracking a company or person context, some projects may stay under that sub-namespace for situational awareness. If one of those sub-namespace pages is a software entity and later becomes heavily used in the garden, refactor it: give it a root-level page and add an alias from the old path. Example: this garden originally had `Anthropic/App/Claude Code` because the focus was on the company; after more content and Claude Code becoming a cultural force, it got its own [[Claude/Code]] page with an alias to the old location.
		- Having more than one rule here is intentional but can feel confusing. The aim is to avoid spamming the top level with every similar piece of software, and to use placement as a subtle signal: root-level primacy for software that has "arrived" or is clearly going to grow; under company or person when we're tracking it in context of that entity.
	- ## When we treat something as a software project
		- Strong signals: GitHub or similar repo links, official project homepages, article or post titles that name a software project, or notes that describe a tool, editor, library, app, CLI, or server. We may infer a software entity from context; when we do, we note that in the report.
	- ## Finding and deduplicating
		- Check in this order: exact main page name, exact alias, partial title match, repo owner and repo name, then page-body mentions of the same homepage, repo, or description. Classify as: existing, similar, new, or blocked.
	- ## Frontmatter
		- Shared frontmatter conventions live on [[Logseq/Frontmatter]].
		- To mark a page as a software project instance, add `logseq-entity::` pointing at this type page (the namespace uses nested segments: Logseq/Entity/Software/Project). The type page then gets backlinks to all software project pages.
		- Software-project-specific frontmatter can include `created-by::` pointing to a **person** or **company** page when the creator entity is clear.
	- ## Page shape
		- File: `pages/<ProjectName>.md`. In links, use the main page name with forward slashes for namespaces where we use them (e.g. `Lazygit/Keyshort/Some action`). First block: H1 with the project title (or a reference link to the project). Keep the page lean: title plus a few descriptive bullets.
	- ## Creator (person or company) handling
		- If the creator is clear and is an individual, create or use a `Person/...` page and point `created-by::` there. If the creator is clearly an organization tracked in the garden, create or use a company entity page and point `created-by::` there.
		- If it is not clear who the creator is, do not guess—ask the human (e.g. create the software page without creator metadata, create the entity page first, or skip until the identity is clarified).