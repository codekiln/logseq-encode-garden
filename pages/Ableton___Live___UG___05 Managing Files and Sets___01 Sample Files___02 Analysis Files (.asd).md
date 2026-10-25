logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/05 Managing Files and Sets/01 Sample Files]]
prev:: [[Ableton/Live/UG/05 Managing Files and Sets/01 Sample Files/01 The Decoding Cache]]
next:: [[Ableton/Live/UG/05 Managing Files and Sets/01 Sample Files/03 Exporting Audio and Video]]

- # [5.1.2 Analysis Files (.asd)](https://www.ableton.com/en/live-manual/12/managing-files-and-sets/#analysis-files-asd)
	- An analysis file ([[Ableton/File/.asd]]) sits next to its sample with the same name. It improves warping quality, detects the tempo of long samples, and speeds up waveform drawing. Long samples stay grayed out and unplayable until analysis finishes.
	- `.asd` files don't show in the browser; a checkmark on a sample's icon means one exists.
	- The Save Default Clip button in a clip's title bar stores the clip's settings, such as Warp Markers, in the `.asd`, so the sample loads that way in future Sets. It doesn't change clips already in other Sets, and unlike a Live Clip it stores no devices.
	- A sample with an `.asd` isn't analyzed again. Long samples aren't analyzed when Auto-Warp Long Samples is off.
	- Create Analysis Files = Off in File & Folder Settings stops writing `.asd` files, so samples are analyzed on every load. Existing files stay, and Save Default Clip still writes one.
