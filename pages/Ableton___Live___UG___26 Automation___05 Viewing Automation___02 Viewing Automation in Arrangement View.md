logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/26 Automation/05 Viewing Automation]]
prev:: [[Ableton/Live/UG/26 Automation/05 Viewing Automation/01 Viewing Automation in Session View]]

- # [26.5.2 Viewing Automation in Arrangement View](https://www.ableton.com/en/live-manual/12/automation/#viewing-automation-in-arrangement-view)
	- Turn on [[Ableton/Live/UI/Arrangement View/Toggle/Automation Mode]] above the track headers, or press `A`, to open each track's main automation lane.
		- ![Automation Mode enabled](https://ableton-production.imgix.net/live-manual/12/AutomationModeButtonL12.png?auto=&w=320)
	- The Device and Automation Control choosers in the lane pick what to show; Device set to None hides the envelope. LEDs and dashed lines work as in Session View, and **Show Automated Parameters Only** / **Show All Parameters** shorten or restore the lists.
	- In Automation Mode, clicking a control shows its envelope. **Show Automation** or **Show Automation in New Lane** in a parameter's context menu turns on Automation Mode and focuses its lane.
	- ## More lanes
		- **Add Automation Lane** moves the current envelope to its own lane and sets the main lane to None, ready for another parameter.
			- ![The main automation lane and an additional lane](https://ableton-production.imgix.net/live-manual/12/MultipleAutomationLanesL12.png?auto=&w=320)
		- A toggle in the main lane hides or shows the extra lanes; drag to reorder them.
		- Up and down arrows move between lanes; left goes back to the main lane; left and right on the main lane hide or show extras.
		- `Option`-click (Mac) / `Ctrl`-click (Windows) Add Automation Lane duplicates the main lane's envelope, up to two duplicates. `Cmd`-click (Mac) / `Alt`-click (Windows) adds a lane for every automated parameter.
		- **Remove Automation Lane** removes a lane, or all selected lanes; `Cmd`/`Alt`-click removes it and every lane below.
		- See also [[Ableton/Clip/Q/How can I see all MIDI CC clip envelopes stacked in Arrangement View?]]
	- ## 26.5.2.1 Context Menu Options for Automation Lanes
		- Lane header context menus offer **Add Automation Lane** (main lane), **Add Lane for Each Automated Envelope**, **Remove Automation Lane** (extra lanes), and commands to clear all envelopes for the track or one of its devices.
