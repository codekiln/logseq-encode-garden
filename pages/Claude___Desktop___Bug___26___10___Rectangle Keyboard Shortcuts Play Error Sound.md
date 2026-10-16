tags:: [[Software/Bug]]

- # Claude Desktop Bug - [[Rectangle]] keyboard shortcuts play the system error sound
	- [[Observed Behavior]]
		- With [[Claude/Desktop]] in focus, pressing a [[Rectangle]] window-management keyboard shortcut plays the macOS system error (alert) sound instead of moving or resizing the window.
	- [[Expected Behavior]]
		- The shortcut moves or resizes the window, as it does in every other app.
	- Context
		- Noticed on [[2026-10-16 Fri]].
		- The same Rectangle shortcuts work in every other app I use.
		- Unclear whether the fault is in Claude Desktop (perhaps it consumes the key combination and rejects it) or in Rectangle (perhaps it cannot act on this app's window). Filed against both.
	- Not yet tried
		- Check whether the Rectangle menu bar items work on the Claude Desktop window.
		- Check whether another global-shortcut tool behaves the same way with Claude Desktop in focus.
