logseq-entity:: [[Logseq/Entity/question]]
tags:: [[Question]]
see-also:: [[VSCode/Extension]], [[VSCode/Command/Markdown/Open Preview]]
via:: [[2026-04-09 Thu]]

- # Is there a [[VSCode/Extension]] that helps obsidian users have an obsidian-compatible view of obsidian markdown files and navigate between wiki links?
	- ## My Notes
		- “Obsidian-compatible” here means wiki-style `[[links]]`, optional backlinks/embeds, and navigating notes on disk like a vault—not pixel-perfect Obsidian UI.
	- ## Answer
		- [[AI/Response]]
			- **Yes.** Several [[VSCode/Extension]]s add Obsidian-like **wikilinks**, **navigation** (go to definition / Ctrl/Cmd+click), **autocomplete** on `[[`, and sometimes **backlinks** or **embeds**. None fully replicate Obsidian’s reading view, but many teams combine one of these with the built-in Markdown preview ([[VSCode/Command/Markdown/Open Preview]] / preview to the side).
			- ### Strong general options
				- **[Foam](https://marketplace.visualstudio.com/items?itemName=foam.foam-vscode)** ([repo](https://github.com/foambubble/foam)) — Large install base; **wikilink** completion, **go to definition**, **peek references**, **graph**, daily notes, optional **link reference definitions** for standard Markdown compatibility, and **navigation in the Markdown preview** (per marketplace/docs). Good default if you want an Obsidian-adjacent *workspace* inside VS Code.
				- **[Markdown Notes](https://marketplace.visualstudio.com/items?itemName=kortina.vscode-markdown-notes)** ([repo](https://github.com/kortina/vscode-markdown-notes)) — Longstanding **`[[wiki-links]]`**, **backlinks** panel, **peek/go to definition**, autocomplete, piped links; explicitly aimed at Obsidian/Roam-style workflows.
				- **[WikiLens](https://marketplace.visualstudio.com/items?itemName=lostintangent.wikilens)** ([repo](https://github.com/lostintangent/wikilens)) — **Roam/Obsidian-like** UX: page-centric explorer, **backlinks**, `![[embeds]]`, daily pages. Check repo activity if you care about ongoing maintenance.
			- ### Obsidian-branded or narrow extensions
				- **[Obsidian Navigation](https://marketplace.visualstudio.com/items?itemName=GeoffreyOlsonJr.obsidian-navigation)** — Click/hover to open linked `.md` files for **`[[FileName]]`** in the **editor**; marketplace notes **Markdown preview pane link navigation is not implemented yet** (planned).
				- **[obsidian-vscode-extension](https://marketplace.visualstudio.com/items?itemName=contradiction29.obsidian-vscode-extension)** — Click wikilinks, **create missing notes**, `[[` completion, **hover** shows linked file content (smaller extension by install count).
			- ### Commercial / fuller “vault in VS Code”
				- **[AS Notes](https://www.appsoftware.com/products/knowledge-management/as-notes)** — Wikilinks, backlinks, rename propagation; claims **Markdown preview** resolves **nested wikilinks** for navigation-style reading (verify in trial against your vault layout).
			- ### Caveats
				- **Vault layout matters**: Obsidian often uses flat or folder notes with unique names; some extensions assume **unique filenames** vs **path-relative** wikilinks—match extension settings to how your vault is stored.
				- **Preview vs editor**: Built-in preview follows standard Markdown; wikilink **clicking** in preview is extension-dependent (Foam documents preview navigation; Obsidian Navigation explicitly does not yet).
			- ### Sources
				- [Foam — Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=foam.foam-vscode)
				- [foambubble/foam](https://github.com/foambubble/foam)
				- [Markdown Notes — GitHub](https://github.com/kortina/vscode-markdown-notes)
				- [WikiLens — GitHub](https://github.com/lostintangent/wikilens)
				- [Obsidian Navigation — Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=GeoffreyOlsonJr.obsidian-navigation)
				- [obsidian-vscode-extension — Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=contradiction29.obsidian-vscode-extension)
				- [AS Notes product page](https://www.appsoftware.com/products/knowledge-management/as-notes)
