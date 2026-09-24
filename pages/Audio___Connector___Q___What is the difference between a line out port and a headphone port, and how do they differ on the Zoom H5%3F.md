logseq-entity:: [[Logseq/Entity/Question]]
see-also:: [[Audio/Connector/Phone/TRS/3.5mm]]

- # What is the difference between an [[Audio/Connector/Line/Out/Port]] and an [[Audio/Connector/Headphone/Port]], and how do they differ on the [[Zoom H5]]?
	- ## [[AI Answer]]
		- **Short answer:** a line out hands a signal to another device's input; a headphone out hands a signal to a pair of transducers. A headphone jack is a line out with a small power amplifier and a volume control in front of it. On the [[Zoom H5]] the two are separate [[Audio/Connector/Phone/TRS/3.5mm]] jacks with independent level controls, so the recorder can feed a camera or an interface at a steady level while headphone volume moves freely.
		- ### The general difference
			- | Trait           | Line out                                                     | Headphone out                                              |
			  | --------------- | ------------------------------------------------------------ | ---------------------------------------------------------- |
			  | Meant to drive  | the input stage of another device, 10 kΩ and up              | headphone drivers, roughly 16–300 Ω                        |
			  | Behind the jack | a buffer, with no power amplifier                            | a buffer plus a small power amplifier                      |
			  | Rated in        | volts, against a nominal reference such as −10 dBV or +4 dBu | milliwatts into a stated load                              |
			  | Level control   | fixed, or a trim set once at setup                           | a volume knob, moved while listening                       |
			  | Signal shaping  | none; flat at a known reference level                        | varies with the load, and clips before the line stage does |
			- The distinction is about **current, not voltage**. Both jacks swing about a volt. Only the headphone amplifier can push that voltage into a 32 Ω load without collapsing, which is why a line out asked to drive headphones goes quiet and loses its bottom end: the low impedance of the headphones loads the output stage down.
		- ### What happens when the two are swapped
			- **Headphone out into a line in** works, and is the everyday field rig. The cost is that one knob now sets two things — turn the monitoring down and the recording gets quieter. A headphone amplifier is also noisier and clips earlier than the line stage on the same device.
			- **Line out into headphones** is quiet and thin, and on a high-impedance pair close to inaudible. Nothing is damaged; there is simply not enough current.
			- **Line out into a mic input** is the opposite problem. Line level runs roughly 30–40 dB hotter than a mic input expects, so it distorts unless something pads it down.
		- ### On the Zoom H5
			- The H5 carries both, as two separate unbalanced 1/8 in (3.5 mm) stereo jacks:
			- | Jack                       | Maximum output level    | Output impedance | Level set by                      |
			  | -------------------------- | ----------------------- | ---------------- | --------------------------------- |
			  | [[Zoom H5/Port/Line Out]]  | +1 dBu                  | 110 Ω or less    | the `LINE OUT LEVEL` menu setting |
			  | [[Zoom H5/Port/Headphone]] | 20 mW + 20 mW into 32 Ω | 10 Ω or less     | the physical volume buttons       |
			- [[Answer/Official]] from the [H5 Operation Manual](https://www.zoom.co.jp/sites/default/files/products/downloads/pdfs/E_H5_0.pdf): `LINE OUT LEVEL` sits under the `IN/OUT` menu and runs from −30 to 0 dB. Its stated purpose is feeding "the external mic input jack on an SLR camera or other jack with a high input gain" without an attenuator cable in the line — the H5 pads its own line out rather than asking for a resistive cable.
			- The manual is explicit that the two outputs are independent: the `LINE OUT LEVEL` setting "does not affect the level output from the PHONE jack." That independence is the practical payoff, and it is what makes a simultaneous send-and-monitor rig possible on this recorder.
			- Both jacks are live at once, so a single H5 can feed a camera or interface from `LINE OUT` while the performer or engineer monitors on `PHONE`.
		- ### Scope of this answer
			- Output specifications come from the H5 operation manual and Zoom's published spec sheet, read September 2026. The line-versus-headphone distinction itself is general audio practice rather than a Zoom rule.
