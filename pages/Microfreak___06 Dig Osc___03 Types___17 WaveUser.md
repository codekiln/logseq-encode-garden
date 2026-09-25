logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Microfreak/06 Dig Osc/03 Types]]
prev:: [[Microfreak/06 Dig Osc/03 Types/16 HARM]]
next:: [[Microfreak/06 Dig Osc/03 Types/18 Sample]]
- # 06.03.17 User Wavetable Oscillator (WaveUser)
	- User Wavetable Oscillator Model
		- ![01 User Wavetable Oscillator Model](../assets/Microfreak___06-Dig-Osc___03-Types___17-WaveUser___01-User-Wavetable-Oscillator-Model.png)
	- **Description:** WaveUser works like the Wavetable oscillator, with two differences: MIDI Control Center can load user wavetables, and the Shape knob controls bit depth instead of chorus.
	- A user wavetable bank contains 16 tables, each with 32 cycles of 256 samples. When no user bank is present, the factory wavetable bank loads automatically.
	- **Table:** The Wave knob selects one of the 16 waves in the table.
	- **Position:** The Timbre knob browses the table's 32 cycles.
	- **Bitdepth:** The Shape knob changes the wave's bit depth for a digital lo-fi character.
	- MIDI Control Center instructions for loading wavetables are in the Wavetables tab.
