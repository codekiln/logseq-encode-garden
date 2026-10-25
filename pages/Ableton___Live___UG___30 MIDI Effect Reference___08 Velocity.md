logseq-entity:: [[Logseq/Entity/Book/Section/Level 2]]
up:: [[Ableton/Live/UG/30 MIDI Effect Reference]]
prev:: [[Ableton/Live/UG/30 MIDI Effect Reference/07 Scale]]
- # [30.8 Velocity](https://www.ableton.com/en/live-manual/12/live-midi-effect-reference/#velocity)
	- ![The Velocity Effect](https://ableton-production.imgix.net/live-manual/12/VelocityL12.png?auto=&w=320)
	- Velocity remaps incoming velocities (1–127) into a chosen output range.
	- The **Velocity Curve** grid maps the input range (**Lowest** and **Range**, X axis) onto the output range (**Out Low** and **Out Hi**, Y axis). Out Low 80 with Out Hi 127 makes even soft playing come out loud. Lowest and Out Low at 0 with Range and Out Hi at 127 leaves velocities nearly unchanged.
	- **Operation** applies the mapping to Note On velocity, Note Off (release) velocity, or both.
	- **Mode** handles velocities outside the input range:
		- **Clip** — clamps them into the range
		- **Gate** — removes those notes; an LED under the grid flashes
		- **Fixed** — every note gets the Out Hi velocity
	- **Random** moves each velocity up or down by up to the set amount, inside the output range. A gray band around the curve shows the random spread.
	- **Drive** pushes the curve toward one end: positive values make most notes loud, negative values soft.
	- **Compand** spreads velocities toward the extremes (positive) or squeezes them toward the middle (negative).