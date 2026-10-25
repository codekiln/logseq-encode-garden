logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/22 Stem Separation]]
prev:: [[Ableton/Live/UG/22 Stem Separation/01 How Stem Separation Works in Live]]

- # [22.2 Separating Audio Files and Clips](https://www.ableton.com/en/live-manual/12/stem-separation/#separating-audio-files-and-clips)
	- Choose **Separate Stems to New Audio Tracks** from the context menu or Create menu, on a file in the browser or a clip in either view.
		- ![The Separate Stems dialog](https://ableton-production.imgix.net/live-manual/12/StemSeparationDialogL12.png?auto=&w=320)
	- In the dialog:
		- toggles pick which of the four stems to make;
		- **Merge to Single Track** combines two or three chosen stems into one;
		- the quality selector picks High Speed or High Quality;
		- **Separate** starts the process and stops playback.
	- Each stem gets its own track inside a new Group Track, coloured to match the dialog's toggles; the group takes the source track's colour. A single stem, or a merged one, goes on one track instead.
		- ![Separated stems in Arrangement View](https://ableton-production.imgix.net/live-manual/12/StemSeparationSeparatedStemsL12.png?auto=&w=320)
	- Only the clip's audible region is processed — between its start and end markers, or from the start marker through the loop of a looped warped clip.
	- In the Arrangement, **Separate Stems for Time Selection** on a clip splits it at the selection's edges and separates only that part.
	- Source track effects move to the Group Track; track automation is copied to the group, and clip envelopes and modulation to each stem clip.
	- The source clip is deactivated to avoid doubling; select it and press `0` to turn it back on.
	- From the browser, stems land in whichever view has focus. In an empty Set with warping on for samples, the Set tempo follows the source.
	- Files go to the Project's Samples/Processed/Stems folder (merged stems keep their individual files too), in the File Type from the Record, Warp & Launch Settings, at 44.1 kHz and the source's bit depth.
	- {{embed [[Ableton/Live/UG/22 Stem Separation/02 Separating Audio Files and Clips/01 Separation Speed vs. Quality]]}}
