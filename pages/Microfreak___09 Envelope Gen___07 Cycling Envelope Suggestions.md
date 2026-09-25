logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Microfreak/09 Envelope Gen]]
prev:: [[Microfreak/09 Envelope Gen/06 Cycling Envelope]]
- # 09.7 Freaky Cycling Envelope Suggestions
	- Use the Matrix to modulate the Cycling Envelope's Rise, Hold, and Fall with the LFO or pressure. Pressure gives direct control over the Rise and Fall stages.
	- Matrix modulation can be positive or negative. A negative signal to Fall shortens the Fall stage as pressure increases.
	- Amount controls how strongly the Cycling Envelope affects its destinations. Adjust it carefully, especially when modulating the analog filter. A control that reduces signal strength is an attenuator.
	- The Matrix can combine the Cycling Envelope with stages of the Main Envelope. For example, modulating Attack changes its slope; modulating Decay changes its length. Further Matrix routings can build longer modulation chains.
	- Patch ideas:
		- Use a slow sine LFO to control Cycling Envelope Rise, then use CycEnv to control Main Envelope Sustain.
		- Use a random LFO to control Cycling Envelope Amount, then use CycEnv to control Main Envelope Decay/Release or Sustain.
