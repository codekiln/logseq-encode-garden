logseq-entity:: [[Logseq/Entity/software-project]]
tags:: [[Software/Library]]
see-also:: [[diagrams]], [[D2]], [[Diagram/Mermaid]]

- # [Structurizr](https://structurizr.com/)
	- **Architecture-as-code** toolkit aligned with **[[C4]]**: define architecture in a **[Structurizr DSL](https://docs.structurizr.com/dsl)** workspace and derive multiple consistent views (system context, container, component, deployment, etc.).
	- Intentionally **not [[UML]]**; constrained **box-centric** notation with **styles**, **themes**, groups, and element-level icons—suited to **rigorous software architecture modeling** rather than a rich vendor-icon “architecture board” look (compare [[diagrams]], [[D2]], [[Diagram/Mermaid]]).
	- ## Core idea
		- **Precise, maintainable** architecture models; **reproducible diagrams** from source; fits **developer workflows** (repos, CI/CD).
	- ## Mental model
		- Think in **three layers**—same underlying model, different surfaces:
		- ### 1. Core engine (free, open source)
			- DSL **parser**, **validation**, **diagram generation**, **export** (PlantUML, Mermaid, PNG/SVG, static site).
			- **Local-first**: usable **without** any server; the engine is the center of gravity.
		- ### 2. Delivery modes (interfaces over the engine)
			- **CLI-style**: `export`, `validate`, etc.
			- **Local viewer** (`local`): lightweight **local web UI**.
			- **Static export**: pure **HTML/JS** output.
			- **Server** (`server`): multi-user **workspace** hosting (see licensing).
			- **vNext direction**: tooling consolidated toward a **single binary / Docker image**—you pick a **command mode** (`local`, `server`, `export`, …) rather than a separate “product” name.
		- ### 3. Structurizr server (optional, commercialized)
			- **Workspace storage**, **collaboration**, **auth**, **APIs**.
			- Prebuilt **server** binaries are **licensed**; the **core** modeling/export path stays **free** without it.
	- ## Free workflows (no server, no license)
		- You do **not** need a server, a license, or a hosted UI to use the **core** toolchain.
		- ### A. Diagrams only
			- ~~~
			  export -workspace workspace.dsl -format plantuml
			  ~~~
			- Or raster output, e.g.:
			- ~~~
			  export -workspace workspace.dsl -format png
			  ~~~
		- ### B. Static site
			- ~~~
			  export -workspace workspace.dsl -format static -output site
			  ~~~
			- Produces `index.html` plus JS/CSS—**no backend**, **client-side** interactive diagrams; host on GitHub Pages, S3, or any static host.
		- ### C. Optional local UI
			- ~~~
			  local /path/to/workspace
			  ~~~
			- Runs a **local** viewer only when you want it.
	- ## [[Structurizr/export/Static site]] export vs layout
		- Static export supports **zoom/pan**, **view navigation**, **tooltips**, **perspectives**.
		- Does **not** bundle full **documentation** or **ADR** workflows by itself—those live outside or in other tooling.
		- **Layout**: the **DSL** does **not** persist manual layout; **JSON** workspace format **does**. So **auto-layout** can stay DSL-only; **hand-tuned layout** → prefer **JSON** (or a JSON-backed workflow).
	- ## [[Structurizr/MCP/Server]]
		- A **stateless HTTP-oriented wrapper** around Structurizr capabilities for **agents and automation**—**not** the same as the multi-user **Structurizr server**, and **not** a paid component by itself.
		- **Typical**: parse DSL → JSON, **validate**, **export** diagrams (PlantUML, Mermaid), **inspect** models.
		- **Optional**: proxy **CRUD** against a **Structurizr server** (then **server licensing** applies).
		- **Local-only MCP** use → **core engine** only, no license for normal open-source/local paths.
	- ## How the pieces relate
		- ~~~
		  DSL → Core engine → Output
		           ↑
		    CLI / Docker / MCP
		  
		  Optional:
		  MCP → Structurizr server (licensed)
		  ~~~
	- ## Typical pipelines
		- **Minimal**: [[DSL]] → export → [[png]] / [[Mermaid]] / [[PlantUML]]
		- **Docs site**: [[DSL]] → export static → [[GitHub/Pages]] (or any static host)
		- **Interactive local**: `DSL → local`
		- **Automation / AI**: `DSL → MCP → pipeline or agent → diagrams`
	- ## Strengths and trade-offs
		- **Strengths**: **C4** rigor, **consistent multi-view** models, **architecture as code**.
		- **Trade-offs**: less **visually free-form** than general diagram languages; weaker fit than some tools for **dense vendor/service icon** boards (again vs [[diagrams]], [[D2]], [[Diagram/Mermaid]]).
	- ## Summary
		- **Core** = **DSL → compiler → diagrams** (free, local-first).
		- **Server** = optional **hosted** collaboration layer (**licensed** where applicable).
		- **MCP** = **programmable** wrapper for integration—not required for everyday use.