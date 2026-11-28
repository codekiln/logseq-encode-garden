logseq-entity:: [[Logseq/Entity/Term]]
see-also:: [[MIDI/Bank-Select-and-Program-Change]]

- # MIDI Bank
	- A **bank** is a number that a MIDI sender puts in front of a [[MIDI/Program-Change]], so that the program number can mean more than 128 different things. The sender sends it as Bank Select on [[MIDI/CC]] 0, CC 32, or both.
	- The MIDI standard defines the message, but not what the bank number corresponds to. Each instrument that receives it decides that for itself: a block of memory, a variation of a sound, a family of sounds, or nothing at all.
	- What the instruments below agree on: the bank number waits until a Program Change arrives, and only then does anything change. Yamaha and Roland both state this in their MIDI charts.
	- ## Examples
		- **A block of memory, chosen with CC 32.** The Sequential OB-6 stores 1000 programs in 10 banks of 100. Banks 0–4 hold user programs and 5–9 factory programs. It reads Bank Select from CC 32 only, and a Program Change of 0–99 picks a program inside the bank ([OB-6 Operation Manual](https://www.davesmithinstruments.com/wp-content/uploads/2016/03/OB-6-Operation-Manual.pdf), Appendix C).
		- **A block of memory, chosen with CC 0 and CC 32 together.** The Korg minilogue xd has 500 programs in 5 banks of 100. CC 0 stays at 0, CC 32 picks bank 0–4, and a Program Change of 0–99 picks the program ([minilogue xd MIDI Implementation](https://cdn.korg.com/us/support/download/files/5227b0b2f7c1da5acd0911ac3e8c4f38.txt)).
		- **A block of memory, chosen with CC 0 alone.** The [[Microfreak]] has 512 slots in 4 banks of 128: bank 0 is slots 1–128, bank 1 is 129–256, bank 2 is 257–384 and bank 3 is 385–512. Its user guide doesn't describe this; [[Microfreak/CLI/Upload a preset]] shows CC 0 = 2 and program 66 selecting slot 323.
		- **A variation of the same instrument sound.** On a Roland GS sound module such as the SC-88 Pro, the Program Change picks an instrument, such as piano, and CC 0 picks a variation of it. Bank 0 holds the basic sound and other banks hold variations: CC 0 = 8 with Program Change 2 is Piano 3w, a variation of Piano 3. CC 32 picks which generation's sound set to use ([SC-88 Pro Owner's Manual](https://cdn.roland.com/assets/media/pdf/SC-88PRO_OM.pdf), p. 126 and p. 188).
		- **A family of sounds.** On a Yamaha XG module such as the MU50, CC 0 picks the family: 0 for ordinary instruments, 64 for sound effects, and 126 or 127 for drum kits. CC 32 then picks a variation, and the Program Change picks the instrument or kit ([MU50 Sound List and MIDI Data](https://usa.yamaha.com/files/download/other_assets/2/318072/MU50E2.pdf)).
		- **No banks.** The Korg monologue has 100 programs, so a Program Change of 0–99 reaches all of them. Its MIDI chart lists no Bank Select ([monologue MIDI Implementation](https://cdn.korg.com/us/support/download/files/16ee9047b932f624ed640d98940ff798.txt)).
	- ## Other uses of the word
		- Synthesizers and their software also call any named collection a bank, and those collections have nothing to do with Bank Select.
		- [[Example]] Arturia's MIDI Control Center is a program for the Mac or Windows that connects to the MicroFreak over USB to copy presets and change settings ([[Microfreak/UG/14 Config/02 MIDI Control Center]]). It can also load two kinds of sound material into the MicroFreak:
			- **Wavetables:** sets of short single-cycle waveforms that the User Wavetable oscillator steps through as its Timbre knob turns ([[Microfreak/UG/06 Dig Osc/03 Types/17 WaveUser]]).
			- **Samples:** short audio recordings that the Sample and Grains oscillators play ([[Microfreak/UG/14 Config/02 MIDI Control Center/03 Samples Tab]]).
			- MIDI Control Center calls a named collection of wavetables, or of samples, a bank ([[Microfreak/UG/14 Config/02 MIDI Control Center/02 Wavetables Tab/01 Management]]). These banks hold sound material, not presets, and no MIDI message selects them.
