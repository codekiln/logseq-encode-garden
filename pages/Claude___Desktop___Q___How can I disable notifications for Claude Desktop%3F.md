tags:: [[Claude/Desktop]], [[Q]]
logseq-entity:: [[Logseq/Entity/Question]]

- # How can I disable notifications for [[Claude/Desktop]]?
	- ## [[AI Answer]]
		- **Short answer:** [[Claude/Desktop]] has no documented in-app toggle for its OS notifications — turn them off the same way you'd turn off any desktop app's notifications, through the operating system.
		- [[Answer/Official]] from [Desktop application docs](https://code.claude.com/docs/en/desktop): "The desktop app sends an OS notification when a Code session finishes a task and you aren't currently viewing that session." Anthropic's docs describe when the notification fires but don't document a Settings toggle inside the app to suppress it.
		- **macOS:** System Settings → Notifications → Claude → toggle off **Allow Notifications** (or set the alert style to **None**).
		- **Windows:** Settings → System → Notifications → Claude → toggle off.
		- **Distinct setting — mobile push, not Desktop OS notifications:** when [[Claude/Code]] Remote Control is connected, Claude can also send proactive push notifications to your phone. That's a separate toggle: `/config` → **Push when Claude decides** (`agentPushNotifEnabled` in settings, default `false`). It only affects phone push, not the Desktop app's own OS notification banners.
