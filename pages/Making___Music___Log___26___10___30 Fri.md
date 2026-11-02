prev:: [[Music/Making/Log/26/10/29 Thu - GitP Halloween event prep]]
next:: [[Making/Music/Log/26/10/31-Sat]]
- # [[2026-10-30 Fri]]
	- ## Ableton playback start
		- In [[Ableton/Live]], pressing `Space` kept starting playback at the beginning despite selecting a later point in Arrangement View. A locator at the beginning had **Set Song Start Time Here** enabled, which overrides the Arrangement selection or insertion marker as the playback start.
		- Turning off **Set Song Start Time Here** on the locator restored playback from the Arrangement selection or insertion marker.
		- [[Ableton/Live/UG/06 Arrangement View/04 Launching the Arrangement with Locators]]
	- ## 23:30 — GitP reflections on notation of performance
		- ### Logseq as a score
			- ![Somnia, a set template and Logseq as a score](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Music___Making___Log___26___10___29%20Thu%20-%20GitP%20Halloween%20event%20prep___Asset___Notebook___Yellow-12.jpg)
			- #### Transcription
				- The 2026-10-29 entry and the poem in the left column are on [[Music/Making/Log/26/10/29 Thu - GitP Halloween event prep]].
				- 2026-10-30 Fri 11:30 PM
				- Another bout of insomnia. 3 cups of coffee and a baggie of dark chocolates in the afternoon. Need to calm the body, then the mind.
				- Thinking about Logseq as a "score" for ableton improv, with microfreak.
				- What's the easiest notation for a melody with notation for cc changes? What if I wanted to use text? Something like 'music markdown'. I need a 'score' format for this… performance setup I have, with the launchpad and the microfreak.
				- yesterday, on the walk home, I realized that the GitP episode format I've been using (in Logseq) is a bit like a system of music notation. The "chapters" are like "staves." The whole page is
					- start
						- chapters
							- chapter heading (preset)
								- chapter heading (pattern)
			- #### Diagram
				- A grid with rows for scenes and columns "μF preset", "pattern A", "pattern B", "pattern C". Row "scene 1" holds "016 Voidom" under preset and a short staff with a natural sign and a few notes under pattern A.
				- An arrow turns the grid row into an outline: "scene 1" > "preset: 016 Voidom" > "pattern A" ''' > "pattern B" '''.
			- #### AI notes ([[Anthropic/Model/Claude/5/5/Opus]])
				- The GitP episode page already works like a score: chapters are staves, and each chapter heading names a preset and a pattern.
				- An Ableton Session grid of scenes × patterns, with the preset as the first column, converts directly into a Logseq outline. The example preset is [[Microfreak/Preset/016 Voidom]].
		- ### Scale-degree shorthand and machine commands
			- ![Notation of performance — scale-degree shorthand and machine commands](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Making___Music___Log___26___10___30%20Fri___Asset___Notebook___Yellow-13.jpg)
			- #### Transcription
				- music notation as music technology
				- it's crazy to think of how many handwritten staves there have been in the history of music; I've probably written less than 1000, but Bach, Mozart…
				- 2026-10-30 Fri 11:30 PM GitP reflections on notation of performance
				- Should I try to learn how to "see" music as MIDI? Instead of writing [a bar of staff notation in bass clef] I could write something like:
					- `scale/mode(natural minor, d)`
					- `rep((1_3, 1_3, 1_4, 1_4, 5_3, 6_3), 2x)`
					- arrows label the parts of `1_3` as scale/mode degree _ octave
					- why? then in latex, rendered: 1₃ 1₃ 1₄ 1₄ 5₃ 6₃
				- it would be better if we could have a system that's easy to write by hand and visually understand.
				- what if it was a system for choreography, specific to my instruments? for example, a system that described launchpad sequencer commands (store pattern, etc) and microfreak gestures (decrease wave)
				- logseq compat:
					- LP — launchpad
						- SEQ (Tr1) — sequencer, track 1
							- store pattern — store pattern
				- or maybe it could be a type of assembly language for 'machine commands' the human operator would perform
					- LPP — on the launchpad pro
						- seq
							- stp — store pattern
							- …
							- sps — set pattern setting
								- len 1 8 — 8 beats of whole notes
								- mod 1 d — 1st mode, root note of d on LPP, top left (nat minor)
			- #### AI notes ([[Anthropic/Model/Claude/5/5/Opus]])
				- Instead of staff notation, write melodies as scale degrees with octave subscripts inside a declared mode, plus a repeat count.
				- Extend that into a notation for performance gestures: Launchpad sequencer commands and MicroFreak knob turns, either as a nested Logseq outline or as terse assembly-like mnemonics (`stp`, `sps`, `len`, `mod`).
		- ### Columnar gesture notation (p. 3)
			- ![Columnar gesture notation for the Launchpad Pro and MicroFreak](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Making___Music___Log___26___10___30%20Fri___Asset___Notebook___Yellow-14.jpg)
			- #### Transcription
				- 2026-10-30 Fri p3
				- I like the logseq compat idea but in handwritten contexts, whitespace "aware" notation is not an efficient use of pages. So then, what about something more traditional in terms of programming languages? We could have delimiters, for example, semicolons. makes me want to learn Supercollider again, kind of, just to see what they do, or maybe sonic pi or any of the toplap languages. Now I'm resisting my curiosity. I really want to go into the other room and fire up the computer.
				- Isn't it funny; I've just yawned, but I've also just "caught the skilift" in terms of being so interested in this line of thinking I can't easily get off. I'm only writing in a notebook in the kitchen with a dim light, but I'm getting excited.
				- Part of me thinks that ideally there would be some way for columnar information to be stored. Wouldn't it be better if, in logseq,
					- `### First gesture`
						- ~~~lpp
						  seq/
						    pset/ mode(natmin., d) & len(8, 1) & kbd(2)
						    pat/ ... notation TBD ...
						  ~~~
						- ~~~mfk
						  utl/glb/mid/local(0)
						  osc/all speech   (crossed out)
						  preset/016 Voidom
						  osc/wav(50, 90)
						  ~~~
				- Annotations on the code:
					- `mode(natmin., d)` — natural minor with root note of d
					- `len(8, 1)` — 8 whole notes
					- `kbd(2)` — sequencer keyboard mode 2: drum or dia., or `kbd(chrom.)`
					- `local(0)` — local control off (0) or on (1)
					- pst for preset
					- `wav(50, 90, 7)` — start, end, sec
				- Margin: could these be rendered side by side to indicate simultaneity (then again, there's a limit to the number of simultaneous presses… usually 2!)
			- #### Diagram
				- A spiral doodle in the top right corner.
			- #### AI notes ([[Anthropic/Model/Claude/5/5/Opus]])
				- Indented outlines waste paper by hand, so this page tries delimiter-based syntax closer to live-coding languages like [[SuperCollider]] and Sonic Pi.
				- A "gesture" heading holds one code block per instrument, `lpp` for the [[Novation/Launchpad/Pro/Mk3]] and `mfk` for the [[Microfreak]]. Paths name menu locations and functions take values, with `wav(50, 90, 7)` sweeping the Wave knob from 50 to 90 over 7 seconds.
				- Blocks rendered side by side could show simultaneous actions, though two hands limit how many happen at once.
		- ### MicroFreak pressure through the Launchpad sequencer (p. 4)
			- ![Encoding MicroFreak pressure through the Launchpad sequencer](https://s3.us-east-005.backblazeb2.com/logseq-encode-garden/Making___Music___Log___26___10___30%20Fri___Asset___Notebook___Yellow-15.jpg)
			- #### Transcription
				- 2026-10-30 Fri p.4
				- I should use microfreak's pressure sensitivity more
				- or rather, I should take whatever steps that are needed in order to be able to ensure pressure differences are encoded in the microfreak synth via the launchpad sequencer, which might include performing on the LPP
			- #### AI notes ([[Anthropic/Model/Claude/5/5/Opus]])
				- When the Launchpad sequencer plays the MicroFreak, the keyboard's pressure expression is lost. The fix may be to play the parts in on the Launchpad Pro's pads, which are pressure-sensitive, so the sequence keeps the pressure data.
