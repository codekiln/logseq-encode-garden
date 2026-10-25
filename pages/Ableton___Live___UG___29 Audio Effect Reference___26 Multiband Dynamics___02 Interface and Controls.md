logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/29 Audio Effect Reference/26 Multiband Dynamics]]
prev:: [[Ableton/Live/UG/29 Audio Effect Reference/26 Multiband Dynamics/01 Dynamics Processing Theory]]
next:: [[Ableton/Live/UG/29 Audio Effect Reference/26 Multiband Dynamics/03 Sidechain Parameters]]
- # [29.26.2 Interface and Controls](https://www.ableton.com/en/live-manual/12/live-audio-effect-reference/#interface-and-controls)
	- **High** and **Low** switch those bands on; with both off it works as a single-band device using only the Mid controls. The sliders below them set the crossovers: at 500 Hz and 2000 Hz the bands are 0–500 Hz, 500–2000 Hz and above 2000 Hz.
	- Each band has an activator (off bypasses its processing and gain) and a solo button. **Input** knobs set each band's level before processing, **Output** knobs after.
	- In the display, large bars show each band's output and small bars its input; with no processing the input meters line up with the tops of the output meters. The scale is in dB.
	- Thresholds: the blocks at the left and right of each band are the levels below the **Below** threshold and above the **Above** threshold. Drag their edges sideways to move the thresholds.
		- `Cmd` (Mac) / `Ctrl` (Windows) — same threshold on all bands
		- `Option` (Mac) / `Alt` (Windows) — Above and Below together for one band
		- `Shift` — finer steps
	- Ratios: drag up or down in the middle of a block to make that level range louder or quieter; the same modifier keys apply, and double-click resets.
		- Above the Above threshold: down is downward compression, up is upward expansion.
		- Below the Below threshold: down is downward expansion, up is upward compression.
	- The column to the right of the display also shows the values. Buttons **T**, **B** and **A** switch it between Time (attack and release), Below (threshold and ratio) and Above (threshold and ratio).
	- Attack and release:
		- Above thresholds — Attack is the time to full effect once the signal rises past the threshold; Release the time to recover after it falls back
		- Below thresholds — Attack is the time to full effect once the signal drops below; Release the time to recover after it rises again
	- **Soft Knee** — processing starts gradually near the threshold
	- **RMS/Peak** — Peak reacts to short peaks; RMS waits until the level has stayed past the threshold a little longer
	- **Output** — overall output gain
	- **Time** — scales all attack and release times together
	- **Amount** — scales the strength of all processing; at 0% every ratio is effectively 1