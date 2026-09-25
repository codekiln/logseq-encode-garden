logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Microfreak/17 Ext Gear]]
prev:: [[Microfreak/17 Ext Gear/04 Control External Gear]]
next:: [[Microfreak/17 Ext Gear/06 MIDI Channels]]
- # 17.4 About Local Control
	- By default, the keyboard is connected to the sound engine (Local On), so pressing a key plays the MicroFreak. Turn Local Control off when controlling the MicroFreak externally over MIDI: the keyboard sends notes to MIDI out, but they do not reach the sound engine. The MicroFreak may then seem unresponsive.
	- > [[Note/Info]] If the MicroFreak seems unresponsive, check whether Local Control was turned off.
	- Local Off is useful when an external sequencer controls the MicroFreak. It prevents double triggering when the sequencer sends keyboard notes back to the MicroFreak sound engine, a condition called MIDI echo.
