logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Ableton/Live/UI/Arrangement View/Scrub Area/Marker/Locator]]

- # How can I set a locator and rename it without the mouse in [[Ableton/Live]] on Mac?
	- ## [[My Answer]]
		- After making some mappings:
			- `;` to set locator
			- `j` to prev locator
			- `k` to next locator
		- Then use `;` to create the locator, then `kj` to go to the prev locator then back really quickly, at which time the Cmd+R rename will work
		- ### Note - it seems to only sometimes work
			- If the cursor is on a track that has a clip in the arrangement view, sometimes I find that Cmd+R renames the clip rather than the Locator.
			- Yeah, actually, now I can't seem to get it to work.
	- ## [[AI Answer]]
		- [[Answer/Official]] from [Live 12 Manual: Launching the Arrangement with Locators](https://www.ableton.com/en/live-manual/12/arrangement-view/#launching-the-arrangement-with-locators)
		- **Short answer:** press your Set Locator key (`;`), then `Cmd+R`, type the name, and press `Return`.
		- **Why it works:** the manual says selected locators can be renamed with the Rename command, `Cmd+R` on Mac (`Ctrl+R` on Windows). It also says that once a locator exists, the [[Ableton/Live/UI/Arrangement View/Button/Set Locator]] button becomes the Delete Locator button, which only happens while a locator is selected. So a locator you just set should already be selected and ready for `Cmd+R`.
		- **Not confirmed in the manual:** that `Cmd+R` lands on the new locator and not on a track. Rename also applies to tracks (`Cmd+R` is "Rename Selected Track" in the shortcut list), so test it once in your set.
		- **Keys that help afterwards:**
			- Arrow keys move the selected locator.
			- `Delete` removes it.
			- Pressing the Set Locator key again while a locator is selected deletes it instead of adding a second one.
		- **Selecting an existing locator without the mouse:** the manual gives no key for this. Mapping [[Ableton/Live/UI/Arrangement View/Button/Previous Locator]] and [[Ableton/Live/UI/Arrangement View/Button/Next Locator]] to keys jumps playback to a locator, but the manual does not say whether that also selects it for `Cmd+R`.