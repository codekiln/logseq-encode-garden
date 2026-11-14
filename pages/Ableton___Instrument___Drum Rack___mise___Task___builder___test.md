logseq-entity:: [[Logseq/Entity/Mise/Task]]
task-owner:: [[Person/codekiln/GitHub/logseq-encode-garden]]
task-config-root:: .
task-name:: ableton:drumrack:builder:test
source-link:: https://github.com/codekiln/logseq-encode-garden/blob/main/mise-tasks/ableton/drumrack/builder/test
see-also:: [[Ableton/Instrument/Drum Rack/mise/Task/builder/up]]

- # Test the Drum Rack builder
	- Runs Ruff (lint and format check), mypy and pytest for the builder package. The tests build their own samples and racks in temporary folders and never read the User Library.
	- ## Invocation
		- ~~~sh
		  mise run ableton:drumrack:builder:test
		  mise run ableton:drumrack:builder:test -k bracket
		  ~~~
		- Arguments go to pytest. `tests/unit` covers rack reading and writing, analysis, comparison, configuration and the Launchpad grid; `tests/integration` drives the HTTP API, the command line, and the Launchpad code through CoreMIDI virtual ports on macOS.
	- ## Dependencies
		- Mise supplies uv; uv installs the locked development dependencies into the package's ignored `.venv/`.
