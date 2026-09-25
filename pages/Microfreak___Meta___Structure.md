# [[Ghost Gardener]] Project - Turn the Microfreak namespace in a logseq translation of the docs pdf - [[2026-09-25 Fri]]
	- I'd like to try something relatively new. I have  `~/Downloads/microfreak_Manual_5_0_1_EN.pdf`, which is the latest version of the documentation for the arturia microfreak. I'd like to have this determine the structure of the Microfreak namespace in logseq that you should fill out.
	- I don't want the PDF to be imported into logseq assets. That just adds binary weight to the whole repo. Instead, AI should pull the text and images out into the logseq pages, mirroring the heading structure in logseq namespaces and following my preferences below.
	- So, for example, take a look at these pages, which I manually converted to match my needs.
		- [[Microfreak/06 Dig Osc]]
		- [[Microfreak/06 Dig Osc/01 as Soundgen]]
		- [[Microfreak/06 Digital Oscillator/03 Types/01 BasicWaves]]
	- ## my preferences
		- ### high level conversion principles
		  collapsed:: true
			- Translate what the source is communicating to a logseq-native representation.
			- We're not aiming at zero information loss or absolute fidelity to the original. My preference is to have a logseq-native representation that is easy to read and idiomatic inside of logseq.
			- use page embeds and avoid block embeds. Text should not be repeated.
		- ### two digit zero padded numbers
		  collapsed:: true
			- to preserve [[Lexicographic/Order]]
		- ### shorten and abbreviate namespace components
		  collapsed:: true
			- to save space in the filename and in the auto-complete menu of Logseq
		- ### use common logseq frontmatter used with tree structures
		  collapsed:: true
			- [[Logseq/Frontmatter/next]] - a link to the previous sequential item
			- [[Logseq/Frontmatter/prev]] - a link to the next sequential item
			- [[Logseq/Frontmatter/up]] - a link to the parent namespace
		- ### use typical loglevel namespaces in callouts
		  collapsed:: true
			- use block quotes with [[Note/Info]], [[Note/Warning]]
				- [[Example]]
					- ((6ab64abf-49ab-46af-8598-5e409a38d568))
		- ### use logseq links in place of page references or PDF links and adjust the text around it so it makes sense when read
		  collapsed:: true
			- [[Example]]
				- ((6ab64ab1-b770-448a-9708-979398d28b7e))
					- This appears on page 36, which originally had
						- > The LFO in the MicroFreak can generate signals in the range from 0.1Hz to 100Hz. Please refer to the `LFO chapter [p.57]` for details.
						- Where `LFO chapter [p57]` in the PDF to chapter 8 in the PDF.
					- I replaced the last sentence with
						- > Please refer to [[Microfreak/08 LFO]] for details.
						- So that the sentence is truly translated to Logseq properly.
		- ### place referenced images in logseq assets according to my sequential preferences for the filename and place the image underneath the caption
		  collapsed:: true
			- [[Example]]
				- {{embed ((6ab65191-5104-46a1-8f9a-0deb5920fed4))}}
					- Here, the original had this image with the caption `The Digital Oscillator` below it in the PDF. I created the image `../assets/Microfreak___06-Dig-Osc___01-as-Soundgen___01-The-Digital-Oscillator.png` and referenced it with `![01 The Digital Oscillator](../assets/Microfreak___06-Dig-Osc___01-as-Soundgen___01-The-Digital-Oscillator.png)` so it would appear correctly in logseq and the caption would become the alt text of the image. I also moved the image underneath its caption in logseq.
					- I also numbered the image within the section, so that as long as the image filepath is derived from the logseq page that the image was used in, if I look at the assets directory, all of the images in the PDF would be sorted in order of their appearance in the text, when sorted in [[Lexicographic/Order]].
		- ### intelligently translate tables to nested logseq markdown while preserving communicative purpose and respecting the need for concision
		  collapsed:: true
			- so that it can be opened in [[nvim]] easier. Clean up tables when converting them to logseq format by translating their communicative value into logseq hierarchy of nodes. That is, intelligently omit column names where they don't add communicative value; many times the actual purpose of the table is to convey information that should be hierarchical anyway. There's not a hard and fast rule here; just try to make it seem natural in logseq.
			- [[Examples]]
				- from [[Microfreak/18 Appendix A Speech Osc]], labeled page 125, pdf page 130
					- ## Wave categories, Waves and CC 10 + values
						- ### vowels, range of formants
							- wave: 0,0 - 42,4
							- CC 10: 0 - 53
				- from [[Microfreak/19 Appendix B Vocoder/07 Config]], labeled page 133 in the PDF (pdf page number 138)
					- Below an overview of the Utility settings that are specific for the Vocoder.
					- ## Mic Settings
						- ### Mic Gain
							- -12 dB to -59dB, Auto Gain (default)
						- ### Noise Gate
							- Off, -30dB to -90 dB (default -70 dB)
						- ### Mic Detection
							- Off, On (default)
				- from [[Microfreak/20 Appendix C - Cheat Sheet]] labeled p139, pdf p144
					- ## Preset
						- ### Shift + Preset Encoder
							- Quick select of “A”, “a”, "0 and “.” character ranges
					- ## Oscillator
						- Shift + Wave encoder
							- Encoder changes values at opposite speed (slow or
							  fast) of its setting in Utility > Browsing > Osc Knob
							  Speed
				- from [[Microfreak/21 Appendix D - CC Values]], labeled page 141, pdf page 146
					- ## Parameters and their CC numbers
						- Spice - 2
						- Glide - 5
						- Oscillator Type - 9
						- ...
		- ### use logseq bullet points for bullets
		  collapsed:: true
			- model the bullet, don't put the bullet as text, e.g. don't use • as it's redundant
			- [[Example]]
				- from [[Microfreak/19 Appendix B Vocoder/07 Config/01 Preset Settings]] labeled page 133 (pdf page 138)
					- Two menu items are preset related:
						- Vocoder Hiss mode
						- Vocoder Hiss Volume
					- You'll find them in Utility>Preset>Vocoder Hiss Mode and Utility>Preset>Vocoder Hiss Vol.
	- ## entities to define
		- It's my hope that you can define these entities such that any AI familiar with the entity system can convert any PDF sufficiently similar to thie particular PDF to this type of structure, matching my preferences, without needing a specific logseq skill.
		- [[Logseq/Entity/Book/Section]] - **General, shared** characteristics shared pages that model all section types
		- [[Logseq/Entity/Book/Section/Level 1]]
			- Additional characteristics **specific to** the topmost section in the book; do not repeat information
			  id:: 6ab65469-ff20-4224-921a-27133a79538a
		- [[Logseq/Entity/Book/Section/Level 2]] - same but for level 2
		- [[Logseq/Entity/Book/Section/Level 3]] - same but for level 3
		- [[Logseq/Entity/Book/Section/Level 4]] - same but for level 4
		- I didn't create an example of nesting inside a level two section, but I think you'll get the point.
	- ## Suggested order of operations
		- Commit these instructions
		- File a github parent issue for this task, with sequenced github child issues for:
			- Prototype book section entities
				- Convert a few pages or sections that represent my preferences
					- Store scripts in a sensible place in the repo, following my preferences
					- I do not expect a full scripted conversion to meet my preferences, however, I'm expecting that a single skill: `logseq-entity`, combined with entity definitions and access to scripts referenced in the entity definitions, should be sufficient for the conversion
					- After conversion, evaluate them against my preferences, update as necessary
			- Harden logseq-entity skill import of section
				- Test the conversion of a section using nothing but logseq entity skill using a fresh context uninformed by the rest of the work. Use a subagent with a CLI tool in tmux, for example, [[Codex/CLI]], [[GitHub/CoPilot/CLI]], [[CursorAI/CLI]], [[Claude/Code/CLI]] with appropriate auto mode settings, and as it "Please import logseq section entities from `<path to pdf>` for `<reference to section>`"
				- Update the text of [[Logseq/Entity/Book/Section]] and other entities, the scripts referenced in those entities.
					- There's a very small chance you may find yourself wanting to update the [[Rulesync/Skill/logseq-entity]] skill itself. I would prefer that you didn't. This is my single most important skill, and it has a wide blast radius in terms of how it operates. I aim to keep this small and compact. I will only support that if you explain to me how your change improves the entire entity system and it's not specific to this task and how that update won't degrade its performance on other entities. Think of this skill as the "linux kernel" of how I use AI with Logseq.
				- Iterate until using any harness with the `logseq-entity` skill produces results that are in line with my preferences
			- Import each section (create an issue for each)
	- ## Requests and Rules
		- standard request - agents should familiar with titles of files in [[My]] namespace and contents of selected files in [[My/AI/Rule]] namespace, [[My/Pref]], [[My/Principle]] and other namespaces you deem to be relevant to this task.
		- agents should work in a worktree and submit PRs; [[My/Pref/Dev/Tool/git/Worktree]].
		- agents should mark github issue as in progress in some consistent way if that's not too much trouble. the purpose of this is to help me see the progress of the project. you don't have access to github projects likely, so don't ask.
		- Each github issue should be one context window of an agent. Plan accordingly. I don't want agents using a large amount of context or solving more than one issue.
		- Your assignment has been adequately described in this document. Don't bother me too much with clarifications. I will only evaluate your output when I deem you to have iterated sufficiently on this problem yourself.
		- My target for this goal is to converge by [[2026-09-27 Sun]].
		- I'm going to try not editing the pages under [[Microfreak]] until you are done.
		- PRs can stack up. You are not blocked by me not merging.