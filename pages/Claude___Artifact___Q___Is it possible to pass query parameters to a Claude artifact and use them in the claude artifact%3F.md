logseq-entity:: [[Logseq/Entity/Question]]

- # Is it possible to pass query parameters to a Claude artifact and use them in the claude artifact?
	- ## [[AI Answer]]
		- **Short answer:** Not settled. Anthropic documents no way to pass query parameters into an artifact, and I did not test it. The documented constraints make a direct `window.location.search` read unlikely to work on a published artifact.
		- **What the docs establish**
			- The viewer on claude.ai loads each artifact from a sandboxed `*.claudeusercontent.com` origin, so the page does not run on the `claude.ai/...` URL you open. Source: [Claude Code Docs: Share session output as artifacts](https://code.claude.com/docs/en/artifacts).
			- An artifact is one static page with no backend, and relative links do not resolve. Same source.
			- Neither [Claude Code Docs: Artifacts](https://code.claude.com/docs/en/artifacts) nor [Publish and share artifacts](https://support.claude.com/en/articles/9547008-publish-and-share-artifacts) mentions query parameters, hash fragments, or reading the viewer's URL.
		- **Inference, unverified:** The page sits in a sandboxed frame on another origin, so a `?x=1` on the claude.ai link would not appear in the frame's own `window.location.search` unless the viewer forwards it. Nothing I found says it does. The test is cheap: publish a page that prints `location.href` and open it with `?x=1` appended.
		- **Third-party claim:** A [Chrome extension listing](https://chromeboard.com/extension/claude-artifacts-unlocker-pmphjmnhhcoofaidfldpacnaojpiigoi) says it hands parent-page URL parameters to artifacts through a `postMessage` bridge. That suggests the parameters do not arrive natively; the listing is not official behavior.
		- **Workarounds that are documented**
			- Per-viewer input: a form or controls on the page, held in memory or browser storage.
			- Shared or Claude-written input: the `db` runtime capability, where Claude seeds rows with `ArtifactData` and the page reads them.
			- A page that records its own state: the `artifact` capability republishes the page with the state embedded.
			- Pass values at publish time: Claude can write them into the HTML before publishing, one artifact per variant.
