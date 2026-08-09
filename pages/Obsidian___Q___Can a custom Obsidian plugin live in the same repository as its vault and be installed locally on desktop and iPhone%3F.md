logseq-entity:: [[Logseq/Entity/Question]]
- # Can a custom [[Obsidian]] plugin live in the same repository as its vault and be installed locally on desktop and iPhone?
	- ## [[AI Answer]]
		- [[Answer/Official]] from the [Obsidian sample plugin](https://github.com/obsidianmd/obsidian-sample-plugin#manually-installing-the-plugin), [Obsidian's Working Copy instructions](https://obsidian.md/help/Getting%20started/Sync%20your%20notes%20across%20devices#Working%20Copy), and the [Working Copy manual](https://workingcopy.app/manual/files-sync/#external-repositories):
			- **Short answer:** Yes, provided the repository is linked to the actual vault directory and contains the compiled plugin at `<vault>/<config-folder>/plugins/<plugin-id>/`. Obsidian does not load a plugin from an arbitrary source directory; its documented manual-install location is normally `VaultFolder/.obsidian/plugins/<plugin-id>/`.
			- **Simplest cross-platform layout:** keep the plugin project and its build output in the directory from which Obsidian loads it:
				- ~~~text
				  vault-repo/
				  ├── .obsidian/
				  │   └── plugins/
				  │       └── my-plugin/
				  │           ├── manifest.json
				  │           ├── main.js
				  │           ├── styles.css
				  │           ├── package.json
				  │           └── src/
				  └── Notes...
				  ~~~
				- Build on desktop, exclude `node_modules/`, and commit `main.js`, `manifest.json`, and `styles.css` so the iPhone receives runnable files.
			- **Cleaner monorepo alternative:** keep TypeScript source under `packages/my-plugin/` and have the desktop build copy only the runtime artifacts into `.obsidian/plugins/my-plugin/`. Both directories remain in the same repository, while Obsidian loads only the deployed copy.
			- **iPhone flow with Working Copy:** link the repository to the Obsidian vault folder, then pull the commit containing `.obsidian/plugins/my-plugin/`. Force-quit and reopen Obsidian, turn on community plugins, and enable the plugin. Working Copy performs the Git and folder synchronization; it does not run the Node.js/TypeScript build.
			- **Updates:** build on desktop or in CI, commit and push the new runtime artifacts, pull them with Working Copy, and restart Obsidian on the iPhone.
			- **Use a real plugin directory for the portable setup.** A symlink from `.obsidian/plugins/my-plugin` to another source directory may be convenient on desktop, but the iOS arrangement crosses app-managed storage. Committing the actual plugin directory works with both Obsidian and Working Copy.
			- The plugin must also follow the mobile runtime constraints in [[Obsidian/Q/Can custom Obsidian plugins run on iPhone?]], including `"isDesktopOnly": false` and avoiding Node.js or Electron APIs at runtime.
