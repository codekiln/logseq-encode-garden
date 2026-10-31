logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Zoom H5/UG/08 Recording]]
prev:: [[Zoom H5/UG/08 Recording/04 Folders and Files]]
next:: [[Zoom H5/UG/08 Recording/06 Recording]]
- # Selecting inputs and adjusting levels
	- Choose whether to record the L/R inputs, Inputs 1/2, or both.
	- In MULTI FILE mode, the L/R inputs record to the L/R tracks and Inputs 1/2 record to tracks 1 and 2.
	- Track buttons (steps 1 and 2) and input volume knobs (step 3)
		- ![01 Track buttons and input knobs](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Zoom%20H5___UG___08%20Recording___05%20Inputs%20and%20Levels___Asset___01-Track-buttons-and-input-knobs.png)
	- 1. Press the track buttons for the tracks you want to record.
		- The indicators of the selected buttons light red. Their input signals can then be monitored through the headphones and line outputs.
		- > [[Note/Info]] In STEREO FILE mode, **L** or **R** selects the L/R inputs, and **1** or **2** selects Inputs 1/2.
		- > [[Note/Info]] In STEREO FILE mode, inputs are selected in pairs. One input of a pair cannot be selected on its own.
		- In STEREO FILE mode, skip to step 3.
	- 2. In MULTI FILE mode, to record Inputs 1/2 as one stereo file, press **2** while holding **1**.
		- Press **2** while holding **1** again to turn the stereo link off.
		- With a combo-type input capsule on the L/R inputs, press **R** while holding **L** to link or unlink those tracks the same way.
	- 3. Turn the input volume knob of each selected input to set its level.
		- Level meters in MULTI FILE mode
			- ![02 Level meters](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Zoom%20H5___UG___08%20Recording___05%20Inputs%20and%20Levels___Asset___02-Level-meters.png)
		- Aim for peaks around −12 dB.
		- If the sound distorts even with the input level turned down, move the mics or lower the output level of connected devices.
		- The compressor/limiter can also control the level: [[Zoom H5/UG/13 Settings/02 Comp Limiter]].
		- Wind and other noise can be cut while recording: [[Zoom H5/UG/13 Settings/01 Low Cut]].
	- ## Files created
		- MULTI FILE mode creates one file per selected input. `nnnn` is the project number.
			- L/R input — `ZOOMnnnn_TrLR.WAV`, stereo
			- Input 1 — `ZOOMnnnn_Tr1.WAV`, mono
			- Input 2 — `ZOOMnnnn_Tr2.WAV`, mono
			- Inputs 1/2 with stereo link — `ZOOMnnnn_Tr12.WAV`, stereo
		- All files from one MULTI FILE recording are managed together as one project.
		- STEREO FILE mode creates one stereo file, `ZOOMnnnn.WAV` or `ZOOMnnnn.MP3`. Here `nnnn` is the file number, and each file is managed on its own.
