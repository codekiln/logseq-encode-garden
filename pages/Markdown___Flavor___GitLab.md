#  GitLab Flavored Markdown (GLFM)
	- **Why** – start with CommonMark + GFM then add diagrams, alerts, collapsible sections, color chips to match GitLab UI needs[GitLab Docs](https://docs.gitlab.com/user/markdown/)
	- **Use** – issues, epics, wikis, snippets across self-hosted and SaaS GitLab
	- **Renderers** – `gitlab-markup` Ruby gem (server) plus JavaScript client converter
	- **Interactive / data** – supports inline math, Mermaid/PlantUML, collapsible details, and front-matter for CI-templates; cross-reference links update live in UI