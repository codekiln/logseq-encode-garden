author:: [[ChatGPT]]
date-created:: [[2026-10-27 Tue]]
see-also:: [[Ableton/File/.als]], [[Ableton/Live/Report/26/09/Open-source options for controlling Live 11 from coding agents]], [[Person/codekiln/GitHub/logseq-gardener]]

- # Declare a Live Set in Logseq
	- Describe an [[Ableton/Live]] performance setup as nested Logseq bullets and properties, then compile that page into a `.als` file, so a person or an AI agent can change the setup without touching Live's interface. codekiln brainstormed this with ChatGPT on [[2026-10-27 Tue]] while preparing [[GitP/A/Session/26/10/26-Mon]].
	- ## What is inside a Live Set
		- An `.als` file is one gzip-compressed XML document, not a ZIP archive of several files the way `.docx` and `.xlsx` are. It can be decompressed, edited, recompressed and reopened in Live. [UK National Archives PRONOM registry](https://www.nationalarchives.gov.uk/PRONOM/)
		- The XML holds tracks, clips, devices, automation, tempo, routing and other Set settings. Editing it is possible; the hard part is editing it without breaking the references between Ableton objects.
		- Proposed flow:
			- A Logseq page states the desired Set.
			- A Logseq Gardener parser turns it into a validated session specification.
			- An Ableton compiler edits Live 11 XML and recompresses it.
			- The result, such as `GitPa-017.als`, opens in Live 11.
	- ## Existing projects
		- [session_templater](https://github.com/kkojwang/session_templater) generates `.als` files from YAML or JSON, using an existing Set as the base. It applies track names, types, groups, colors, tempo and time signature. This is the closest precedent; only the source language differs.
		- [ableton-als](https://github.com/kevinkirsten/ableton-als) is a TypeScript library for reading, modifying and validating Sets.
		- [alsdiff](https://github.com/krfantasy/alsdiff) shows semantic differences between Sets, which would help test generated changes.
		- [PyAbleton](https://github.com/maranedah/pyableton) parses Sets and extracts MIDI. It is more useful for inspection than for writing.
		- [AbletonOSC](https://github.com/ideoforms/AbletonOSC) controls a running Live 11+ instance over OSC, an alternative to editing XML.
		- These are community projects with little adoption. Study them; test before depending on them.
		- Ableton publishes [Live Set Export](https://ableton.github.io/export/), an SDK that writes `.als` projects. It is an iOS-oriented library with restricted access and its own license, built for exporting new projects rather than transforming existing ones.
	- ## Start from a known-good template
		- Build a real template Set in Live 11 and have the compiler change a copy of it, rather than building the XML tree from nothing. Live already supports template Sets with tracks, effects, I/O routing and MIDI mappings.
		- For GitP the template would hold the usual setup: [[Microfreak]] MIDI and audio tracks, the commentary microphone, return effects and the usual device chains. The compiler specializes it for one episode.
		- The XML carries internal object IDs, automation references, device state and version-specific fields. Reverse-engineering projects report small edits that produced broken Sets. Copying working structures and changing a few properties is safer than creating devices from XML.
	- ## A Logseq page for one Set
		- Ableton vocabulary gets its own properties. Example page `GitPa/017/Ableton Setup` (proposed syntax, not a standard; device, port and chain names would need to match the real setup):
		  ~~~
		  - Ableton Session
		    spec-version:: 1
		    live-version:: 11
		    base-template:: gitpa-performance.als
		    tempo:: 96
		    time-signature:: 4/4
		    - Tracks
		      - MicroFreak MIDI
		        track-key:: microfreak-midi
		        type:: midi
		        midi-from:: Launchpad Pro MK3
		        midi-to:: MicroFreak
		        midi-channel:: 1
		        monitor:: auto
		        arm:: true
		      - MicroFreak Audio
		        track-key:: microfreak-audio
		        type:: audio
		        audio-from:: Ext. In 1
		        monitor:: auto
		        device-chain:: microfreak-effects
		      - Commentary
		        track-key:: commentary
		        type:: audio
		        audio-from:: Ext. In 2
		        monitor:: auto
		        device-chain:: voice-processing
		    - Scenes
		      - Introduction
		        scene-key:: intro
		        color:: blue
		      - Improvisation
		        scene-key:: improv
		        color:: purple
		      - Reflection
		        scene-key:: reflection
		        color:: green
		  ~~~
		- `track-key::` gives each track a stable, readable identity, so the compiler does not depend on position or display name.
		- The bullet nesting does not have to copy Ableton's object tree. In Live, tracks are columns and scenes are rows; in Logseq both can be sibling sections, and the compiler resolves which clip slots they fill.
		- An agent can propose a change to the Markdown instead of editing undocumented XML.
	- ## Keep the specification separate from execution
		- Parse and validate the page into an intermediate representation: typed objects for tracks, scenes, devices, routing and settings. Two adapters could consume it:
			- **Compile:** write a complete `.als` before Live starts.
			- **Reconcile:** inspect a running Set and apply supported changes through Live's object model, for example with AbletonOSC.
		- Build one adapter first, but keep the representation independent of both. Logseq Gardener's site generator then needs no Ableton knowledge; a separate plugin or CLI reads the parsed garden.
	- ## What a Set file can and cannot configure
		- In the `.als`: tempo, time signature, track names, colors and order. With template-based XML changes: MIDI and audio tracks, scenes and empty clip slots, and track I/O routing. Device chains are best taken from the template; device parameter values are possible with careful XML handling.
		- Outside the `.als`: audio interface selection and global MIDI port settings belong to Live's preferences, the [[Launchpad]] mode to the controller, and the MicroFreak's current preset to the instrument. A preflight check could compare the declared setup with the audio and MIDI devices actually present.
	- ## Risks
		- **Version compatibility:** compile against a Set saved by Live 11. XML from Live 12 may not load in 11.
		- **Internal references:** creating or duplicating tracks and devices can require coordinated ID and automation-reference changes. Valid XML is not necessarily a valid Set.
		- **External files:** samples are not embedded in the `.als`. Keep them in a self-contained project folder; Live's Collect All and Save does this.
		- **Concurrent editing:** never overwrite a Set that Live has open. Write a new file and let Live save its own.
		- Test every generated Set by opening, saving and reopening it in Live 11. Semantic diffs and hashes of the source template make regressions easier to find.
	- ## Smallest experiment
		- Make `gitpa-performance.als` by hand in Live 11 with three tracks and the usual routing.
		- Write a Logseq page declaring those tracks' names and colors and a tempo.
		- Write a standalone Python compiler that reads the page, validates it and makes those few XML changes to a copy of the template.
		- Open the result in Live 11 and check that everything survived.
		- Save it from Live and inspect the XML diff.
		- Reading the root element and Live version of a Set changes nothing:
		  ~~~python
		  import gzip
		  import xml.etree.ElementTree as ET
		  
		  with gzip.open("gitpa-performance.als", "rb") as f:
		      root = ET.fromstring(f.read())
		  print(root.tag)
		  print(root.attrib)
		  ~~~
	- ## Before and after a performance
		- GitP pages already describe what happened in a session. A Set declared in Logseq would describe what should exist before one: desired state before recording, observed state afterward. Logseq Gardener could eventually do both, generating Sets from Markdown and pulling information from finished Sets back into the garden.
