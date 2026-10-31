logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/16 Launching Clips]]
prev:: [[Ableton/Live/UG/16 Launching Clips/06 Clip Offset and Nudging]]

- # [16.7 Follow Actions](https://www.ableton.com/en/live-manual/12/launching-clips/#follow-actions)
	- A Follow Action decides what happens next in a clip's group after it plays. A group is the run of clips in adjacent slots of one track; empty slots separate groups. Scenes have Follow Actions too, in the Scene View.
		- ![The Follow Action controls](https://ableton-production.imgix.net/live-manual/12/FollowActionControls11.1.png?auto=&w=232)
	- ## Controls
		- **Follow Action** button — turns Follow Actions on for the selected clip or scene; off by default; `Shift+Enter`.
		- **Follow Action A and B** — two actions to choose between.
		- **Chance A and Chance B** — the relative probability of each. A at 100% and B at 0% always picks A; raising B to 90% makes A happen about one launch in ten. The slider between them adjusts both.
		- **Linked/Unlinked** (clips only) — Linked fires at the end of the clip, or after the number of loops in the Multiplier field. Unlinked fires after the Follow Action Time.
		- **Follow Action Time** — bars-beats-sixteenths from where play starts; one bar by default. A draggable marker shows it in the clip editor.
	- ## The ten Follow Actions
		- **No Action** — nothing happens, and once chosen, the other action no longer gets a chance.
		- **Stop** — stops the clip after the Follow Action Time, overriding its loop settings.
		- **Play Again** — restarts the clip.
		- **Previous** — plays the clip above.
		- **Next** — plays the clip below, wrapping from the last to the first.
		- **First** and **Last** — play the top or bottom clip of the group.
		- **Any** — plays any clip in the group.
		- **Other** — like Any, but never repeats the current clip while there are others.
		- **Jump** — plays a chosen slot or scene, set with the Jump Target slider.
	- Clips and scenes with Follow Actions show a striped launch button.
		- ![A clip launch button with a Follow Action assigned](https://ableton-production.imgix.net/live-manual/12/ClipLaunchButtonFollowAction.png?auto=&w=314)
	- Follow Actions bypass global quantization but respect clip quantization other than None or Global.
	- The **Enable Follow Actions Globally** button, next to [[Ableton/Live/UI/Arrangement View/Button/Back to Arrangement]], turns every Follow Action in the Set on or off, which is handy for editing a running clip. It is greyed out when the Set has none.
		- ![The Enable Follow Actions Globally button](https://ableton-production.imgix.net/live-manual/12/EnableFollowActionsGloballyButton.png?auto=&w=214)
	- Clip Follow Actions keep running when a scene Follow Action is scheduled, but scene Follow Actions win once they fire.
	- Follow Actions let loop-based music repeat yet still surprise; recording the results gives new material.
	- {{embed [[Ableton/Live/UG/16 Launching Clips/07 Follow Actions/01 Looping Parts of a Clip]]}}
	- {{embed [[Ableton/Live/UG/16 Launching Clips/07 Follow Actions/02 Creating Cycles]]}}
	- {{embed [[Ableton/Live/UG/16 Launching Clips/07 Follow Actions/03 Temporarily Looping Clips]]}}
	- {{embed [[Ableton/Live/UG/16 Launching Clips/07 Follow Actions/04 Adding Variations in Sync]]}}
	- {{embed [[Ableton/Live/UG/16 Launching Clips/07 Follow Actions/05 Mixing up Melodies and Beats]]}}
	- {{embed [[Ableton/Live/UG/16 Launching Clips/07 Follow Actions/06 Creating Nonrepetitive Structures]]}}
