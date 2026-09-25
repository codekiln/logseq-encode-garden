logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Microfreak/09 Envelope Gen/06 Cycling Envelope]]
next:: [[Microfreak/09 Envelope Gen/06 Cycling Envelope/02 Changing Shapes]]
- # 09.6.1 The stages of the Cycling Envelope
	- The Cycling Envelope has three stages:
		- **Rise** sets how long the envelope takes to reach its maximum after a keyboard or Arp/Seq trigger.
		- **Fall/Shape** sets how long the envelope takes to fall to zero.
		- **Hold/Sustain**, part of the Fall/Shape control, sets the level held during the Hold stage.
	- The Mode button selects Env, Run, or Loop:
		- **Env:** The envelope runs once and stops at the end of Fall.
		- **Run:** The envelope free-runs as an LFO and resets when the MicroFreak receives a MIDI Start command.
		- **Loop:** A keyboard, sequencer, or arpeggiator trigger resets the envelope. It retriggers at the end of Fall in Run and Loop modes.
	- In Env mode, a keyboard or external gate starts Rise. Sustain stays high while the key is held; releasing the key ends the gate and starts Fall. In Run and Loop modes, Hold stays high for the time set with the Hold knob before Fall begins.
	- To hear the stages, connect CycEnv to oscillator Pitch in the Matrix and set the amount to about 20. Set Rise to about 200 ms, Hold to 0, Fall to 0 ms, and Amount to 50%. Pitch rises, then slowly falls; lowering Amount makes the rise less noticeable.
	- In Loop mode, very short Rise, Fall, and Hold settings make the Cycling Envelope cycle quickly as a complex LFO. Change these times to change its wave shape.
	- In Loop mode, trigger the envelope with the keyboard or Arp/Seq. Set the arpeggiator near 55 bpm and hold a chord to hear the envelope retrigger on each step.
