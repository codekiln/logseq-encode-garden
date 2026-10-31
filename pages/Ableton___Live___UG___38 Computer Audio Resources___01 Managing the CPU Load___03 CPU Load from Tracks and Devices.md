logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/38 Computer Audio Resources/01 Managing the CPU Load]]
prev:: [[Ableton/Live/UG/38 Computer Audio Resources/01 Managing the CPU Load/02 CPU Load from Multichannel Audio]]
next:: [[Ableton/Live/UG/38 Computer Audio Resources/01 Managing the CPU Load/04 Track Freeze]]
- # [38.1.3 CPU Load from Tracks and Devices](https://www.ableton.com/en/live-manual/12/computer-audio-resources-and-strategies/#cpu-load-from-tracks-and-devices)
	- Tracks and devices cost CPU only while they process audio. Adding devices while stopped adds little load; an effect with no input is essentially idle, and a reverb or delay stays active until its tail finishes.
	- That lowers average load but not peak load. To stress-test a Set before a show, play a clip on every track with all devices on; if the CPU meter's Current value stays well under 100%, the Set should hold up.
	- The mixer's **Performance Impact** indicators show each track's share of the load as six rectangles. Turn them on from the Show/Hide Mixer Config menu at the bottom right, or View → Mixer Controls.
		- ![The Mixer's Performance Impact Indicators](https://ableton-production.imgix.net/live-manual/12/MixerPerformanceImpactSectionL12.png)
	- Freeze a heavy track, or turn off some of its devices, to lower its impact.
