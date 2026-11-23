alias:: [[producer-pal]]
logseq-entity:: [[Logseq/Entity/Software/Project]]
created-by:: [[Person/Adam Murray]]
see-also:: [[Ableton/Max for Live]], [[Ableton/Live/Report/26/09/Open-source options for controlling Live 11 from coding agents]]

- # [Producer Pal](https://producer-pal.org)
	- Repository: [adamjmurray/producer-pal](https://github.com/adamjmurray/producer-pal), 385 [[GitHub/Star]]s as of [[2026-11-22 Sun]]
	- An AI music production assistant for [[Ableton/Live]]. Its [[MCP]] server lets an AI agent read and edit the open Live Set: MIDI clips, playback, tracks, scenes, devices, and the arrangement.
	- Requires Live 12.3 or later.
	- Parts
		- A [[Ableton/Max for Live]] device that runs on a MIDI track in the Live Set.
		- A remote script in the Live User Library under `Remote Scripts/Producer_Pal`, chosen as a control surface in Live's Settings → Tempo & MIDI. It adds clip automation, plug-in and preset loading, audio-to-MIDI, and undo and redo.
		- The MCP server, installed as a [[Claude/Desktop/Extension]] or run with npx.
	- Written in [[TypeScript]].
	- ## [[My Notes]]
		- [[2026-11-22 Sun]] set up version 2.5.0 with Live 12.4.16 through the Claude Desktop extension
			- installed the remote script, restarted Live, and chose Producer Pal as a control surface with Input and Output set to None
			- added the Producer Pal device on a new MIDI track, which also updated the device in the User Library from 2.4.0 to 2.5.0
			- logged in [[GitP/A/Log/26/11/22-Sun]]
