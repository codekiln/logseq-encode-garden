logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Microfreak/05 Connections]]
next:: [[Microfreak/05 Connections/02 Matrix and Encoder]]
- # 05.1 Control Signals
	- The Matrix connects control signals from the MicroFreak's modules. These signals move more slowly than audio and are suited to controlling sound.
	- The MicroFreak Matrix
		- ![01 The MicroFreak Matrix](../assets/Microfreak___05-Connections___01-Control-Signals___01-The-MicroFreak-Matrix.png)
	- Control signals usually move between 0 and 100 Hz. They can modulate the Digital Oscillator, Analog Filter, and other destinations. The Matrix encoder sets their amount from -100% to +100%.
	- The MicroFreak's modules generate control signals in different ways.
		- The LFO makes slow, regular waves. Routed to oscillator pitch, it makes the pitch rise and fall; it can reach 100 Hz.
		- An envelope rises once, then gradually fades. Routed to oscillator pitch, it creates a quick rise followed by a descent. The Cycling Envelope can repeat, acting as a second LFO with more complex modulation waves.
	- A gate rises at Note On and falls at Note Off. The keyboard sends gates that start the MicroFreak's envelope.
	- Three kinds of control signals are used: triggers, gates, and waves.
		- **Triggers** are very short spikes that start an envelope, LFO, or sequencer. Clocks generate triggers.
		- **Gates** last longer and keep something active, such as an envelope's hold stage. A keyboard sends a gate while a key is held.
		- **Waves** can last any length and usually cycle from high to low and back. The MicroFreak's LFO and two envelopes create slow waves.
	- Control signals give a MicroFreak performer room to develop a personal style, as color and line do for a painter.
	- **Note for advanced users:** Analog synthesizers and modular systems use control voltages for modulation. Mostly digital synthesizers such as the MicroFreak use digital signals that mimic those voltages; this manual calls them control signals.
