logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Zoom H5/UI/Mode/4-Audio-Interface]], [[c74/M4L/Ref/LOM]]

- # Can a script make [[Ableton/Live]] 11, 12, or 13 reselect the [[Zoom H5]] as its audio interface after I unplug and replug it?
	- ## [[AI Answer]]
		- **Short answer:** not through any Ableton API. The audio device lives in Live's Settings (`Preferences.cfg`), not in the Set, and nothing Ableton documents lets a script change it. The workarounds below avoid the reset or make it quicker.
		- **What Live 11.3.43 did on this Mac**, from `~/Library/Preferences/Ableton/Live 11.3.43/Log.txt`:
			- Unplugging the H5 at 18:49 on [[2026-11-18 Wed]] set both `Input Device` and `Output Device` to `No Device`. Live picked no fallback device.
			- Replugging it at 03:57 on [[2026-11-19 Thu]] logged `Device init: H5 (4 In, 2 Out)`, so Live saw the H5 come back, but it never selected it again. The same Live process had been running since [[2026-11-17 Tue]].
			- The H5 reports a different CoreAudio `UniqueId` in each audio interface mode: `…:H5:000000000000:2,1` in Stereo mode (2 in) and `…:H5:000000000000:1,2` in Multi Track mode (4 in). Live probably treats these as two different devices, so a setting saved in one mode would not match the other. This is inferred from the log, not tested.
		- **Why a script can't set it:**
			- The Live Object Model's `Application` object has version, dialog, CPU-load and control-surface members, and no audio device property ([LOM: Application](https://docs.cycling74.com/apiref/lom/application/)). Python remote scripts and Max for Live both go through this object model.
			- `Preferences.cfg` is a binary file with no published format. Editing it is unsupported and could reset all your Settings.
			- Ableton forum threads ask for Live to reconnect a returning interface or to remember a preferred device. Neither request has an Ableton answer saying the feature exists ([Always revert to preferred audio interface when connected?](https://forum.ableton.com/viewtopic.php?p=1624062), [Reconnect Audio Interface](https://forum.ableton.com/viewtopic.php?p=1793298)).
		- **Workarounds, most reliable first:**
			- **Keep the H5 in one mode.** Pick Multi Track or Stereo on the H5 and use it every time, so the H5 always shows Live the same device ([[Zoom H5/UI/Mode/4-Audio-Interface]]).
			- **Plug in the H5 before launching Live.** Settings were last saved at 18:48 on [[2026-11-18 Wed]] with the H5 selected, and Live reads them at launch. If the H5 drops mid-session, saving the Set and relaunching Live should restore it. Not yet tested here.
			- **Live 12 and later, output only:** the output chooser has a **Use System Device** option that follows the device chosen in macOS Sound settings ([Live 12 manual, 2.3.3 Audio](https://www.ableton.com/en/live-manual/12/first-steps/#audio)). macOS usually switches its output to a USB audio device when one is plugged in. Even then, the manual describes the option for output only, so the H5 input would still need picking by hand. Live 11 does not have this option.
			- **Live 12 and later, keyboard-driven Settings:** Live 12 lets you reach the Audio page with `Cmd+,`, the arrow keys and `Tab` ([[Ableton/Live/UG/41 Accessibility and Keyboard Nav/02 Audio Setup]]). An AppleScript that sends those keystrokes through System Events could choose the H5. It breaks whenever Ableton reorders the page, and nobody has written or tested one yet. Live 11's Settings window has no such keyboard navigation, so on Live 11 a script would have to click screen coordinates.
		- **Live 13** was announced on 2026-11-10 with a public beta and release planned for early 2027 ([Synthtopia](https://www.synthtopia.com/content/2026/11/11/ableton-announces-live-13-adding-step-sequencing-ara-2-support-new-sound-design-tools/)). None of the announcement coverage mentions audio device handling. Whether it adds a preferred-device setting is still open.
