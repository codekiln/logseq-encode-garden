- Open this page in Logseq desktop to see whether Logseq shows an image and plays an MP3 linked by relative path under `assets/.remote/logseq-encode-garden/`. Git ignores these files, so a fresh checkout has none of them; the commands at the bottom of this page download them from B2.
- ## Image, name with spaces written as `%20`
	- ![CV and Gate outputs](../assets/.remote/logseq-encode-garden/Microfreak___UG___17%20Ext%20Gear___02%20CV%20Gate___01%20Pitch%20Gate%20and%20Pressure___Asset___01-CV-Gate-outputs.png)
- ## Image, name with spaces inside angle brackets
	- ![CV and Gate outputs](<../assets/.remote/logseq-encode-garden/Microfreak___UG___17 Ext Gear___02 CV Gate___01 Pitch Gate and Pressure___Asset___01-CV-Gate-outputs.png>)
- ## MP3
	- ![Synth Forward excerpt](../assets/.remote/logseq-encode-garden/GitP___A___Session___26___10___20-Tue___Asset___Audio___Synth-Forward___7559-7836.mp3)
- ## Plain link to the image
	- [Open the CV and Gate image](../assets/.remote/logseq-encode-garden/Microfreak___UG___17%20Ext%20Gear___02%20CV%20Gate___01%20Pitch%20Gate%20and%20Pressure___Asset___01-CV-Gate-outputs.png)
- ## Restore the files
	- ~~~bash
	  d=assets/.remote/logseq-encode-garden; b=https://s3.us-east-005.backblazeb2.com/logseq-encode-garden; mkdir -p "$d"
	  curl -fL -o "$d/Microfreak___UG___17 Ext Gear___02 CV Gate___01 Pitch Gate and Pressure___Asset___01-CV-Gate-outputs.png" "$b/Microfreak___UG___17%20Ext%20Gear___02%20CV%20Gate___01%20Pitch%20Gate%20and%20Pressure___Asset___01-CV-Gate-outputs.png"
	  curl -fL -o "$d/GitP___A___Session___26___10___20-Tue___Asset___Audio___Synth-Forward___7559-7836.mp3" "$b/GitP___A___Session___26___10___20-Tue___Asset___Audio___Synth-Forward___7559-7836.mp3"
	  ~~~
