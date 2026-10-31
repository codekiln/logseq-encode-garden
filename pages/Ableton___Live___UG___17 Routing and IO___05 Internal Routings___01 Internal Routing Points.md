logseq-entity:: [[Logseq/Entity/Book/Section/Level 3]]
up:: [[Ableton/Live/UG/17 Routing and IO/05 Internal Routings]]
next:: [[Ableton/Live/UG/17 Routing and IO/05 Internal Routings/02 Making Use of Internal Routing]]

- # [17.5.1 Internal Routing Points](https://www.ableton.com/en/live-manual/12/routing-and-i-o/#internal-routing-points)
	- When a track's Audio From is another track, the Input Channel chooser picks where the signal is tapped:
		- **Pre FX** — straight from the track, before its devices and mixer.
		- **Post FX** — after the devices, before the mixer.
		- **Post Mixer** — the track's final output after volume and pan.
		- ![Tap points for track routing](https://ableton-production.imgix.net/live-manual/12/TrackRoutingTapPoints.png?auto=&w=320)
	- Soloing the tapping track lets you hear the tapped track at Pre FX and Post FX, but not at Post Mixer.
	- ## 17.5.1.1 Routing Points in Racks
		- Every chain of an Instrument or Effect Rack, and every return chain of a Drum Rack, offers the same three tap points, listed as `Rack | Chain | Pre FX`, `Post FX` or `Post Mixer`. Post Mixer is the chain's output just before the chains are summed.
		- ![Tap points for every chain in a track](https://ableton-production.imgix.net/live-manual/12/TrackRoutingChainTapPoints.png?auto=&w=320)
		- Soloing a track that taps a chain still lets you hear that point.
