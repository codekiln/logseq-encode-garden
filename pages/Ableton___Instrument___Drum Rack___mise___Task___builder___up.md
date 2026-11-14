logseq-entity:: [[Logseq/Entity/Mise/Task]]
task-owner:: [[Person/codekiln/GitHub/logseq-encode-garden]]
task-config-root:: .
task-name:: ableton:drumrack:builder:up
source-link:: https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/ableton/drumrack/builder/up
see-also:: [[Ableton/Instrument/Drum Rack/mise/Task/builder/verify]], [[Ableton/Instrument/Drum Rack/mise/Task/builder/test]]

- # Build Drum Racks in a local web page
	- Opens a browser page for curating samples into [[Ableton/Instrument/Drum Rack]] presets without Live's Drum Rack view: search and audition samples, exclude the unwanted ones, keep named shortlists per pad, choose between candidates in pairs or in a bracket, and export an `.adg` that Live loads.
	- ## Invocation
		- Run from the garden checkout. The page opens at `http://127.0.0.1:8377/`.
			- ~~~sh
			  mise run ableton:drumrack:builder:up
			  mise run ableton:drumrack:builder:up --port 8400 --no-browser
			  ~~~
		- `--no-launchpad` skips the optional MIDI and audio packages.
	- ## Workflow
		- The left column lists every sample under the configured sample folders, plus every sample an existing Drum Rack uses. It filters by text, folder and source rack, sorts by name, duration, pitch, loudness or brightness, and groups by folder, duration, pitch class, octave, loudness or brightness. Keys: ↑/↓ select and play, Space plays, X excludes, A assigns to the selected pad, S adds to the open shortlist.
		- **New** starts a rack from a default Simpler pad. **Duplicate** copies an existing rack's pads into a new builder rack; the source file is only read.
		- The pad grid shows 64 notes in Live's Launchpad drum layout. A pad from a duplicated rack keeps its devices, choke group, mixer and Simpler settings when it gets a new sample or moves to another note; **Revert to source sample** puts its original sample back.
		- Each pad can hold several named shortlists. **Compare in pairs** offers the least-compared pair and ranks candidates with a Bradley–Terry fit of the votes. **Bracket** seeds a single-elimination bracket from that ranking; each bracket pick also counts as a pairwise vote.
		- **Export .adg** writes into the output folder, rereads the file and reports kept, replaced, added and removed pads, missing samples and any change to rack-level settings.
	- ## Launchpad audition
		- With a [[Novation/Launchpad/Pro/Mk3]] connected, **Connect** reads the current layout, switches the device to [[Launchpad/PRG/05 Software Integration/10 Programmer Mode]], lights the open rack's pads and plays them through this computer's audio output. The grid matches [[Launchpad/PRG/05 Software Integration/06 DAW Drumrack]]; the Up and Down arrows shift it by 16 notes. While a pairwise comparison is open, the pad plays whichever candidate was played last in the browser.
		- **Disconnect** turns the lights off and restores the layout that was showing before. Live also listens to the Launchpad's MIDI port, so an armed track in Live can sound at the same time.
	- ## Files and side effects
		- `config.toml` beside the task holds the defaults, with `~` for the home folder. `config.local.toml` (ignored by git) overrides any key on one machine.
		- The ignored `.local/` folder holds `analysis.sqlite3` (a cache that can be deleted), `curation.sqlite3` (exclusions, racks, shortlists and votes), `resolved-config.json` and overwrite backups.
		- Exports go to `~/Music/Ableton/User Library/Presets/Instruments/Drum Rack/Builder/`, which Live's browser lists under Drum Rack. An existing file is replaced only after confirmation, and a copy goes to `.local/backups/` first. Source racks and sample files are never written.
		- The server listens on 127.0.0.1 only and serves audio by index id, not by path.
	- ## Dependencies and limits
		- Mise supplies uv; uv supplies Python 3.15 and the package's locked dependencies (FastAPI, NumPy, SciPy, soundfile, and mido, python-rtmidi and sounddevice for the Launchpad).
		- Samples in Live's Factory Packs are encoded for Live only. The builder lists them and keeps them on duplicated pads, but cannot analyze or play them, or place them on a new pad.
		- Pitch comes from YIN on the first two seconds and is reported only above 0.6 confidence; loudness is BS.1770 integrated loudness (ungated under 400 ms); brightness is the spectral centroid.
		- A pad holding a nested rack or several samples is kept as it is; assigning a sample replaces it with a default Simpler and keeps only its choke group.
		- New pads start from a Live 11.3 Simpler. An export is checked by rereading the file and comparing it with its source; the check does not load it in Live.
	- ## Recovery and help
		- "already exists": choose another preset name, or confirm the overwrite.
		- "no MIDI port matching": connect the Launchpad, or set `[launchpad] port` in `config.local.toml`.
		- Wrong or stale analysis: delete `.local/analysis.sqlite3` and restart.
		- ~~~sh
		  mise run ableton:drumrack:builder:up --help
		  ~~~
