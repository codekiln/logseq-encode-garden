logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Obsidian/Q/Can a custom Obsidian plugin live in the same repository as its vault and be installed locally on desktop and iPhone?]], [[Logseq/Plugin/logseq-fenced-code-plus]]

- # Does [[Obsidian]]'s public API support fenced-code renderers? If so, how can I make use of them?
	- ## [[AI Answer]]
		- [[Answer/Official]] from [Markdown post processing](https://docs.obsidian.md/Plugins/Editor/Markdown+post+processing) and [registerMarkdownCodeBlockProcessor](https://docs.obsidian.md/Reference/TypeScript+API/Plugin/registerMarkdownCodeBlockProcessor).
		- **Short answer:** Yes — `registerMarkdownCodeBlockProcessor` on the `Plugin` class is precisely that, described in the API reference as a post processor "that handles fenced code given a language and a handler". Obsidian strips the `<pre><code>` element for you and hands the handler an empty `<div>` to fill with whatever you like. Unlike a plain markdown post processor, a registered code block processor renders in **both** Reading view and Live Preview.
		- ### Signature
			- ~~~ts
			  registerMarkdownCodeBlockProcessor(
			    language: string,
			    handler: (source: string, el: HTMLElement, ctx: MarkdownPostProcessorContext)
			      => Promise<any> | void,
			    sortOrder?: number
			  ): MarkdownPostProcessor;
			  ~~~
			- Call it from `onload()`. Anything registered through a `Plugin.register*` method is torn down when the plugin unloads, so there is no matching teardown call to write.
			- `sortOrder` is optional and positions this processor among the other markdown post processors.
		- ### Minimal working plugin
			- ~~~ts
			  import { Plugin } from 'obsidian';
			  export default class KvPlugin extends Plugin {
			    async onload() {
			      this.registerMarkdownCodeBlockProcessor('kv', (source, el, ctx) => {
			        const table = el.createEl('table');
			        for (const line of source.split('\n').filter((l) => l.trim())) {
			          const [key, ...rest] = line.split(':');
			          const row = table.createEl('tr');
			          row.createEl('th', { text: key.trim() });
			          row.createEl('td', { text: rest.join(':').trim() });
			        }
			      });
			    }
			  }
			  ~~~
			- Every fence tagged `kv` in the vault now renders as a two-column table. The official docs use the same shape for a `csv` example.
		- ### What the handler receives
			- **`source`** — the text between the fences. Anything after the language on the opening fence is **not** passed, so `kv title=Foo` style arguments have to be read back out of `ctx.getSectionInfo(el).text`.
			- **`el`** — an empty `div`, already placed correctly in the document. Build into it with `createEl` / `createDiv` / `createSpan` rather than assigning `innerHTML`.
			- **`ctx`** — a [MarkdownPostProcessorContext](https://docs.obsidian.md/Reference/TypeScript+API/MarkdownPostProcessorContext) carrying `sourcePath`, `frontmatter`, `docId`, `addChild()`, and `getSectionInfo()`.
			- The handler may be `async`; returning a promise lets Obsidian wait for asynchronous work before treating the render as finished.
		- ### Cleanup with `ctx.addChild`
			- Anything that must be torn down — DOM listeners, intervals, observers, a chart or diagram instance — belongs in a [MarkdownRenderChild](https://docs.obsidian.md/Reference/TypeScript+API/MarkdownRenderChild) handed to the context:
			- ~~~ts
			  import { MarkdownRenderChild } from 'obsidian';
			  class Clock extends MarkdownRenderChild {
			    onload() {
			      this.registerInterval(window.setInterval(() => {
			        this.containerEl.setText(new Date().toLocaleTimeString());
			      }, 1000));
			    }
			  }
			  // inside the handler:
			  ctx.addChild(new Clock(el));
			  ~~~
			- When the container element leaves the DOM the child's `onunload` runs. Live Preview re-runs the handler as the block is edited, so without this the leaks accumulate per keystroke.
		- ### Rendering markdown inside the block
			- To get `[[wikilinks]]`, embeds, and formatting inside the output, recurse through the renderer instead of building the HTML by hand:
			- ~~~ts
			  await MarkdownRenderer.render(this.app, markdown, el, ctx.sourcePath, child);
			  ~~~
			- Pass `ctx.sourcePath` rather than a guessed path — it is what resolves relative internal links. The `component` argument wants something that outlives the render, normally the same `MarkdownRenderChild` given to `ctx.addChild`.
			- `MarkdownRenderer.renderMarkdown()` is [deprecated](https://docs.obsidian.md/Reference/TypeScript+API/MarkdownRenderer/renderMarkdown) in favour of `render()`.
		- ### Writing back to the file
			- `ctx.getSectionInfo(el)` returns `{ text, lineStart, lineEnd }` — the full file text plus the line range this fence occupies — which is how a rendered widget can mutate its own source when clicked. The docs say to call it immediately before use and to handle a `null` return.
		- ### Where it renders, and where it doesn't
			- **Reading view and Live Preview.** A plain `registerMarkdownPostProcessor` [only fires in Reading view](https://forum.obsidian.md/t/registermarkdownpostprocessor-callback-not-called-with-live-preview-mode/56049); a registered code block processor is rendered in Live Preview as well, reverting to source while the cursor sits inside the block.
			- **Finer-grained editor work** — decorating inline text, gutters, or the fence mid-edit — needs a [CodeMirror 6 editor extension](https://docs.obsidian.md/Plugins/Editor/Editor+extensions) instead, which the docs are explicit is the harder path.
			- **Languages Obsidian already renders itself**, such as [[Mermaid]], are a different job: [beautiful-mermaid](https://github.com/timk75/obsidian-beautiful-mermaid) needs a code block processor for Reading view *and* a CodeMirror ViewPlugin to intercept the built-in Live Preview render.
			- **Obsidian Publish does not run community plugins** — a moderator's answer to the direct question is ["In brief, you can't"](https://forum.obsidian.md/t/how-do-you-include-community-plugins-when-you-publish-your-website/37629) — so custom fences degrade to plain code blocks on a published site. Relevant to [[Obsidian/Q/What options do I have for publishing my obsidian vault as a web application]].
			- **Mobile.** Nothing in this API is desktop-only; the constraints are the plugin's own, per [[Obsidian/Q/Can custom Obsidian plugins run on iPhone?]].
		- ### Shipping it
			- The plugin is an ordinary community plugin: `manifest.json` plus a bundled `main.js` under `.obsidian/plugins/<id>/`, with `"isDesktopOnly": false` if it should load on iOS. Layout and sync options are in [[Obsidian/Q/Can a custom Obsidian plugin live in the same repository as its vault and be installed locally on desktop and iPhone?]]; start from the [obsidian-sample-plugin](https://github.com/obsidianmd/obsidian-sample-plugin) template.
		- ### Prior art worth reading
			- The Obsidian Hub keeps a category list of [plugins with custom codeblock syntax](https://publish.obsidian.md/hub/02+-+Community+Expansions/02.01+Plugins+by+Category/Plugins+with+custom+codeblock+syntax) — the fastest way to find a plugin doing something close to what you want and read its handler.
			- [[Obsidian/Plugin/obsidian-tasks]] (`tasks` queries), [dataview](https://github.com/blacksmithgu/obsidian-dataview) (`dataview`, `dataviewjs`), and [obsidian-charts](https://github.com/phibr0/obsidian-charts) (`chart`) are all built on this one API.
