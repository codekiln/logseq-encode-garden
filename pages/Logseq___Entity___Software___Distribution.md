alias:: [[Logseq/Entity/Software/Distro]]
logseq-entity:: [[Logseq/Entity/Definition]]

- # Software Distribution
	- In this garden, **Software Distribution** pages model a complete, standalone, opinionated curated system built on a base platform (a "distro"). A distribution ships defaults plus a curated set of packages/plugins and (often) its own configuration framework, and you adopt it *as the whole base experience* — not as an add-on to one.
	- ## Vocabulary
		- **Distribution / distro** — the term used in both operating systems (Debian, Ubuntu, Arch) and editors (Neovim distros like LazyVim/AstroNvim, Emacs distros like Doom/Spacemacs). Canonical type name is `Distribution`; `Distro` is an alias.
	- ## Examples in this garden
		- [[LazyVim]] — a [[nvim]] distribution built on [[lazy.nvim]] (also reachable via the `nvim/Distro/LazyVim` alias). Reference for naming and shape.
	- ## When a page might be modeling a distribution
		- Strong signals: described as a "distribution" or "distro"; a complete, ready-to-use configuration of a base platform (OS kernel, editor, runtime) with opinionated defaults; you install/adopt it *as the base*, replacing a vanilla setup; it curates a set of packages/plugins + config; it is typically extensible via its own composable modules (extras / layers / metapackages — see [[Logseq/Entity/Software/Plugin/Collection]] once that exists).
		- Not this type: a single plugin or extension (use [[Logseq/Entity/Software/Plugin]]); a partial, composable sub-collection added *into* a host (use a plugin collection); a plain library, CLI, or app (use [[Logseq/Entity/Software/Project]]).
	- ## Relationship to [[Logseq/Entity/Software/Project]] and to collections
		- A distribution is a specialization of [[Logseq/Entity/Software/Project]] — still a software project, but whose identity is "the complete curated system." A page may declare both, primary first (see [[Logseq/Entity]] → multiple entity membership).
		- A distribution is the **maximal** curated collection: it ships or composes smaller, partial collections (a distro's extras / modules / layers). Contrast: **Distribution** = complete & standalone; a plugin collection = partial & composed into a host.
	- ## How to name the page
		- Follows [[Logseq/Entity/Software/Project]] naming: give a well-known distro a root-level main page (e.g. [[LazyVim]]) and add an alias from the host namespace when useful (e.g. `nvim/Distro/LazyVim`).
	- ## Finding and deduplicating
		- Check in this order: exact main page name, exact alias, host-namespace distro alias (`<host>/Distro/<Name>`), then page-body mentions of the same homepage or repo. Classify as: existing, similar, new, or blocked.
	- ## Frontmatter
		- Shared frontmatter conventions live on [[Logseq/Frontmatter]].
		- Mark an instance with `logseq-entity:: [[Logseq/Entity/Software/Distribution]]`. It is additive — a distro page may also declare [[Logseq/Entity/Software/Project]] (and any other entity it models), comma-separated with the primary entity first.
		- `created-by::` — optional; link to the person or company page when the creator is clear.
	- ## Page shape
		- H1: a Markdown link to the distribution's homepage. Lean descriptive bullets: the base platform it builds on, what it curates (plugins/packages + defaults), and how it is extended.