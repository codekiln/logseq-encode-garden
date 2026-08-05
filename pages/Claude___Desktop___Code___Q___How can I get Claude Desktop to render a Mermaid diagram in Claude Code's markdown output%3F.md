tags:: [[Claude/Desktop]], [[Claude/Code]], [[Q]]
logseq-entity:: [[Logseq/Entity/Question]]
title:: Claude/Desktop/Code/Q/How can I get Claude Desktop to render a Mermaid diagram in Claude Code's markdown output?
see-also:: [[Claude/Desktop/Code/Browser]], [[Mermaid/mmdc]]

- # How can I get [[Claude/Desktop/Code]] to render a [[Mermaid]] diagram in Claude Code's markdown output?
	- ## [[AI Answer]]
		- **Short answer:** Not in the transcript. The Code tab prints a ` ```mermaid ` fence as raw source text — same as the CLI — and there is no Code/Preview toggle for it. To see a rendered diagram you have to route the fence out of the chat into a surface that does render Mermaid: an **artifact**, the **Browser pane**, or a **pre-rendered image**.
		- ### Why the transcript won't do it
			- Native rendering in the desktop Code tab is an open **enhancement**, not a shipped feature: [#52517 — Mermaid code blocks not rendered in Claude Code tab](https://github.com/anthropics/claude-code/issues/52517) (opened April 2026, `area:desktop`, no maintainer response). It asks for exactly the Code/Preview toggle claude.ai artifacts have, defaulting to Preview. The sibling request for the terminal TUI, [#14375](https://github.com/anthropics/claude-code/issues/14375), proposes `mermaid-ascii` instead and is also open.
			- Clicking a `.md` path in the chat opens the **file pane** — an editor showing the source. Only `HTML`, `PDF`, image, and video paths open in the [[Claude/Desktop/Code/Browser]] pane, which is the surface that actually renders. That routing rule is what the workarounds below exploit.
		- ### Publish it as an artifact (best fit)
			- [[Answer/Official]] from [Share session output as artifacts](https://code.claude.com/docs/en/artifacts). Ask Claude to publish the document as an artifact. Artifacts render Mermaid natively — a ` ```mermaid ` fence in a published `.md`, or a `<pre class="mermaid">` block in a published `.html` — with no external library, so the strict artifact CSP is not a problem.
			- The page opens in the browser on publish; `Ctrl+]` reopens the most recent artifact. Republishing the same file path updates the same URL, so an evolving diagram stays at one link.
			- **Requirements:** Pro / Max / Team / Enterprise, a session signed in to claude.ai, Anthropic API as the model provider (**not** available on [[Claude/Code/Bedrock]], Vertex, or Foundry), and desktop app `1.13576.0`+. Published file must be `.html`, `.htm`, or `.md`.
		- ### Pre-render to an image with `mmdc`
			- Use [[Mermaid/mmdc]] to turn the fence into SVG or PNG, then click the image path in the chat — image paths open in the Browser pane.
				- ~~~bash
				  mmdc -i diagram.mmd -o diagram.svg
				  ~~~
			- Works with any plan and any model provider, since nothing leaves the machine.
		- ### Self-contained HTML in the Browser pane
			- Write the diagram into a single `.html` file — either the `mmdc` SVG inlined, or a `<pre class="mermaid">` block with `mermaid.js` bundled locally rather than pulled from a CDN — and click its path. Useful when the diagram belongs alongside other prose or several diagrams on one page and you don't want it published to claude.ai.
		- ### Live preview via MCP
			- [veelenga/claude-mermaid](https://github.com/veelenga/claude-mermaid) is an MCP server that renders Mermaid in a browser and hot-reloads as Claude edits the source. Good for iterating on a diagram's layout; adds a server to maintain.
