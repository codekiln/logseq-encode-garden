logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Claude/Desktop/Q/How can I disable notifications for Claude Desktop?]]

- # How can I turn off the notification sound when a response finishes?
	- ## [[AI Answer]]
		- **Short answer:** the app's own setting governs *when* the turn-completion alert fires, not whether it makes a noise — `Settings` → `Notifications` → turn completion notifications → **Never** removes the ding along with the banner. To keep the banner and lose only the sound, silence it at the OS level instead: `System Settings` → `Notifications` → `ChatGPT` → off **Play sound for notification**.
		- ### The two levers
			- | Lever                                        | Turns off                | Keeps                                        |
			  | -------------------------------------------- | ------------------------ | -------------------------------------------- |
			  | App: turn completion notifications → Never   | the sound and the banner | nothing — no alert at all                    |
			  | [[MacOS]]: Play sound for notification → off | the sound only           | the banner and the Notification Center entry |
			- There is no sound-only toggle inside the app. If the banner itself is welcome and only the ding is not, the OS lever is the one that does the job.
		- ### In the app
			- `Cmd` `,` opens settings; the section is `Notifications`.
			- [[Answer/Official]] from [Notifications](https://learn.chatgpt.com/docs/notifications): you "choose whether turn-completion alerts appear never, only while ChatGPT is in the background, or always." **Only while in the background** is the middle setting worth knowing — it leaves the alert in place for long-running work you have tabbed away from, and stops it firing while you sit watching the response arrive.
			- Permission and question notifications are documented as separate controls, so turning turn-completion off does not suppress a [[Codex]] approval prompt.
		- ### In macOS
			- `System Settings` → `Notifications` → `ChatGPT`, then turn off **Play sound for notification**. `Alert Style` → **None** goes further and drops the banner while still logging the alert to Notification Center.
			- This is also the more dependable lever. The app's turn-completion alert has been reported as unreliable in both directions after the Codex → ChatGPT app consolidation — [openai/codex#36169](https://github.com/openai/codex/issues/36169) has macOS accepting the notification as `banner` + `sound` while the user perceives neither. An OS-level mute does not depend on the app's own setting landing correctly.
		- ### Account notifications are a different setting
			- The `Notifications` pane on the account side governs push for work that finishes while you are away — [[ChatGPT/Task]] runs and [[ChatGPT/Deep Research]] reports. Those toggles reach phone and browser push, not the desktop app's local turn-completion alert, and neither setting affects the other.
		- ### Scope of this answer
			- Setting names read from OpenAI's published documentation in September 2026. The macOS notification toggles are standard per-app options rather than anything ChatGPT-specific.
