logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Logseq/Logseq Dir/custom.css]], [[Logseq/config.edn]]

- # Can the [[Logseq]] graph view be disabled?
	- ## [[AI Answer]]
		- **Short answer:** No built-in setting disables the global graph view in the released file-based version. There is no Settings-UI toggle, `config.edn` flag, or feature flag for it. The accidental triggers can be removed instead — disable the keyboard shortcut and hide the sidebar link. The heavy Pixi.js/WebGL render only runs when you navigate to the `/graph` route, so removing the entry points avoids opening it (and the crash) by accident.
		- ### Disable the `g g` keyboard shortcut
			- In [[Logseq/config.edn]]:
				- ~~~edn
				  :shortcuts
				   {:go/graph-view false}
				  ~~~
			- A `false` value is treated as a disabled shortcut. `:go/graph-view` is the shortcut id; its default binding is `g g` (press G twice).
		- ### Hide the graph links with CSS
			- In [[Logseq/Logseq Dir/custom.css]] (applies to both the app and the published site):
				- ~~~css
				  /* Left-sidebar "Graph view" link (app + published). */
				  .graph-view-nav { display: none !important; }
				  /* Top-bar "Graph" button in the published site. */
				  .cp__header a.button[href$="#/graph"] { display: none !important; }
				  ~~~
			- `.graph-view-nav` is the class on the left-sidebar item that links to the graph route. The published static site also shows a top-bar "Graph" button (`<a class="… button" href="#/graph">`) inside `.cp__header`; that second rule hides it. Published routing uses fragment mode, so the href is `#/graph`.
		- ### Caveats
			- The `/graph` route still exists and remains reachable via search / cmdk. There is no config to remove the route itself without patching source.
			- The unreleased database version adds a sidebar-navigations show/hide UI for nav items; that does not exist in the file-based release, so do not rely on a sidebar toggle.
		- [[Answer/Official]] from [Logseq source — `0.10.15`](https://github.com/logseq/logseq) (`components/container.cljs`, `modules/shortcut/config.cljs`, `modules/shortcut/data_helper.cljs`)
