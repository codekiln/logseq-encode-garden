logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/38 Computer Audio Resources/01 Managing the CPU Load]]
next:: [[Ableton/Live/UG/38 Computer Audio Resources/01 Managing the CPU Load/02 CPU Load from Multichannel Audio]]
- # [38.1.1 The CPU Load Meter](https://www.ableton.com/en/live-manual/12/computer-audio-resources-and-strategies/#the-cpu-load-meter)
	- The CPU meter in the [[Ableton/Live/UI/Control Bar]] compares the time Live takes to compute one audio buffer with the time that buffer takes to play. 50% means computing runs twice as fast as playback; over 100% is possible.
	- The operating system schedules threads, so other applications can cause spikes. The meter counts audio processing only, not work such as drawing Live's interface.
	- The meter's menu, opened from its triangle button or by right-clicking:
		- ![The Drop-Down Menu for the CPU Meter](https://ableton-production.imgix.net/live-manual/12/CPUMeterOptionsL12.png)
		- **Average** (default) — average load from audio processing.
		- **Current** — total current, or peak, load. With both on, the menu shows both values and the meter shows average in a lighter shade and current in a darker one.
		- **Meter Text Shows** — which of the two values appears as a number.
		- **Warn on Current CPU Overload** — off by default; turns on CPU warnings in the Overload indicator.
