see-also:: [[Ableton/Live/Q/Can a script make Ableton Live 11, 12, or 13 reselect the Zoom H5 as its audio interface after I unplug and replug it?]]

- # [[Ableton/Live]] `Log.txt`
	- Plain-text log that [[Ableton/Live]] writes while it runs. Ableton describes it as documenting "activity during recent runs of Live" ([Reading Ableton Live Crash Reports](https://help.ableton.com/hc/en-us/articles/5301568366354)).
	- ## Location
		- Each Live version has its own preferences folder, and its own `Log.txt` in it.
			- **macOS:** `~/Library/Preferences/Ableton/Live x.x.x/Log.txt`
			- **Windows:** `C:\Users\[Username]\AppData\Roaming\Ableton\Live x.x.x\Preferences\Log.txt`
		- Both folders are hidden by default ([How to access hidden folders](https://help.ableton.com/hc/en-us/articles/209070509)).
		- On macOS the same folder holds `Preferences.cfg`, the binary file with Live's Settings, including the audio device.
		- To open the newest one from a terminal, read-only:
			- ~~~sh
			  nvim -R "$(ls -d ~/Library/Preferences/Ableton/Live\ * | sort -V | tail -1)/Log.txt"
			  ~~~
	- ## Line format
		- Each line is `timestamp: level: Component: message`, for example:
			- ~~~
			  2026-11-18T18:14:18.758157: info: Audio In Out: Input Device: H5 (4 In, 2 Out)
			  ~~~
		- **Timestamp:** ISO 8601 local time with microseconds.
		- **Level:** `info`, `warning` or `error`.
		- **Component:** the part of Live that wrote the line, such as `CoreAudio`, `Audio In Out`, `MidiDeviceManager`, `Default App`, `VST3` or `Python`.
		- Each launch starts with a `Started:` line between two rows of `#`, giving the Live version and build:
			- ~~~
			  info: #######################################
			  info: Started: Live 11.3.43 Build: 2025-10-06_b466d4f56c
			  info: #######################################
			  ~~~
		- Ableton suggests finding the most recent run by searching for the last row of `#` near the end of the file.
	- ## Useful lines
		- ### Audio device
			- `CoreAudio: Detected devicelist change` — macOS added or removed an audio device.
			- `CoreAudio: Device init: <name> (<n> In, <n> Out) (<vendor>, Id: <n>, UniqueId: <uid>)` — Live opened a device. The `UniqueId` is what tells two modes of one device apart; the [[Zoom H5]] reports `…:H5:000000000000:2,1` in Stereo mode and `…:H5:000000000000:1,2` in Multi Track mode.
			- `Audio In Out: Begin of UpdateAudioStateStatic` — start of a block listing the active `Input Device`, `Output Device`, channel counts, `Sample Rate`, buffer sizes and latencies. `No Device` in this block means Live has no interface selected.
		- ### Settings and launches
			- `Default App: Begin SavePrefs` / `End SavePrefs` — Live wrote `Preferences.cfg`.
			- `Live App: Start as first instance: yes` — this run is the first open copy of Live.
		- ### Crashes
			- After a crash, the last lines of the last run show what Live was doing, such as restoring a plug-in ([Reading Ableton Live Crash Reports](https://help.ableton.com/hc/en-us/articles/5301568366354)).
		- ### Noise
			- `Service Discovery:` errors such as `UdpSendException … Network is unreachable` can make up most of the file's `error` lines without anything going wrong in Live.
			- Ableton notes that errors logged for VST3 plug-ins are not always a cause for concern.
