tags:: [[Claude/Desktop]], [[Q]]
logseq-entity:: [[Logseq/Entity/question]]
see-also:: [[Claude/Desktop]]

- # How do you focus the sidebar in [[Claude/Desktop]] so that keyboard shortcuts can be executed without opening the context menu?
	- ## [[AI Answer]]
		- [[AI/Response]]
			- **Short answer:** The sidebar letter shortcuts (P=Pin, R=Rename, F=Fork, A=Archive, D=Delete) only work when the context menu is already open — there is no built-in Claude Desktop shortcut to focus the sidebar panel directly. The closest workaround is macOS Full Keyboard Access.
			- **macOS Full Keyboard Access:**
				- Enable in **System Settings → Accessibility → Keyboard → Full Keyboard Access**.
				- Once on, Tab navigates through all UI controls in any app, including Electron apps like Claude Desktop.
				- Tab to a sidebar conversation item, then right-click (or trigger the context menu via the keyboard action key) to open the menu, at which point the letter shortcuts become active.
			- **Opening the context menu from the keyboard:**
				- With a sidebar item focused via Full Keyboard Access, the macOS "Perform Action" key (often mapped to Ctrl+F10 under Full Keyboard Access settings) can trigger a contextual menu.
				- Alternatively, Ctrl+click on the focused item.
			- **Current gap:**
				- Claude Desktop has no native shortcut to directly focus the sidebar; using Ctrl+Tab / Ctrl+Shift+Tab only cycles between open conversations — it does not give keyboard focus to the sidebar panel controls.
				- Keyboard-first sidebar navigation has been requested by users but is not yet a built-in feature.
