logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/25 Racks/05 Zones]]
prev:: [[Ableton/Live/UG/25 Racks/05 Zones/03 Velocity Zones]]

- # [25.5.4 Chain Select Zones](https://www.ableton.com/en/live-manual/12/instrument-drum-and-effect-racks/#chain-select-zones)
	- ![The Chain Select Editor](https://ableton-production.imgix.net/live-manual/12/RackChainSelectZones.png?auto=&w=320)
	- Chain select zones let one parameter, the draggable **Chain selector** above the 0–127 scale, choose which chains can play. Only chains whose zone overlaps the selector's value produce output.
	- In Instrument and MIDI Effect Racks they filter only notes by default; **Chain Selector Filters MIDI Ctrl** in the ruler's context menu makes them filter all MIDI.
	- In MIDI Effect Racks fades lower note velocity. In Instrument and Audio Effect Racks fades lower each chain's output volume: moving the selector off a zone that ends in a fade silences the chain, while a zone without a fade lets reverb tails and delays ring out.
	- ## 25.5.4.1 Making Preset Banks Using Chain Select
		- Chain select zones default to a length of 1 at value 0. Place four chains with different effects at values 0, 1, 2 and 3 with no overlap, and map the Chain selector to a hardware encoder: turning it switches between four setups.
		- ![Using chain select zones as effect presets](https://ableton-production.imgix.net/live-manual/12/RackChainSelectPresets.png?auto=&w=320)
	- ## 25.5.4.2 Crossfading Preset Banks Using Fade Ranges
		- Lengthen the zones and add fade ranges so neighbouring presets overlap, keeping one value where each plays alone. Moving the selector then crossfades between presets; wider fades make smoother transitions.
		- ![Crossfading between effect presets with chain select zones](https://ableton-production.imgix.net/live-manual/12/RackChainSelectPresetsCrossfade.png?auto=&w=320)
