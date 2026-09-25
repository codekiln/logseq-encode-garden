logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Microfreak/19 Appendix B Vocoder/07 Config]]
- # 19.7.1. Preset related Vocoder settings
	- Two settings under **Utility > Preset** are saved with each preset:
		- **Vocoder Hiss Mode**
		- **Vocoder Hiss Vol**
	- Older vocoders added high-frequency noise (“hiss”) to the lower, voiced “buzz” range to make consonants easier to understand.
	- ## Vocoder Hiss Mode
		- **Off:** Only the lower, vowel-like buzz range is heard.
		- **Switched:** A detector distinguishes voiced sections from unvoiced sections. During an unvoiced section, white noise replaces the carrier oscillator. Output is gated by the modulator and follows its level.
		- **Pass:** The vocoded synth signal is mixed with the part of the microphone signal above 5 kHz, allowing the high frequencies of the voice through.
	- ## Vocoder Hiss Vol
		- Sets the level of hiss mixed with the microphone signal and the white-noise replacement level in Switched mode, from -20 dB to 0 dB.
