prev:: [[GitP/A/Log/26/11/25-Wed]]
next:: [[GitP/A/Log/26/11/27-Fri]]

- [[2026-11-26 Thu]]
	- AM resuming [Ableton Live 12]([[Ableton/Live/v/12]]) after the upgrade, in [[Ableton/Live/Log/26/11/26-Thu]].
	- [[AI/Response]] Moved the [[GitP/A/Template/LPP-Seq]] and [[GitP/A/Template/Pattern A and B]] Sets and the [[GitP/A/Session/26/11/06-Fri/Set]] Session View screenshot out of git and into B2 through DVC. Each has an asset page, and the pages that linked the old files link the mounted copies. [[My/AI/Rule/Logseq/Store binary files in B2 through DVC]]
	- [[My Note]]
		- ### Record the MicroFreak preset in the Set
			- Last night I had an idea that maybe we could use Launchpad custom modes to trigger program change or bank change messages for the Launchpad Pro that would end up being transmitted to the MicroFreak. If we did that, then we would be able to know in the Ableton set what MicroFreak preset was being used. We would have a record of it. That's one of the areas that's really annoying for me right now in Ghost in the Patch: I have to keep track of what preset I was using at what times. That's part of the reason why I'm working on the comments thing.
		- ### Custom views 2 through 8
			- I know I have 8 custom views that I can access using the bottom row, but the arrow keys don't do anything on the custom view, unfortunately. So if I were to use custom views 2 through 8, and each has 64 pads, that would be 448. Maybe that would work. I want to keep custom mode 1 as controlling Ableton.
		- ### Faders
			- It seems like I might be able to have a fader in the Launchpad Pro custom mode that could go through the presets. Maybe I could even have several faders. I actually have a record of all the presets in the garden, so in theory I could make a Max for Live patch that encoded this information so that I could have one fader for each preset type, whether it's bass or sequence or that kind of thing. Then I'd be able to sequence through it that way and really quickly land on a preset. I think that's kind of a pipe dream, though. I am wondering if there's a way to address more presets rather than making just one button for each preset.
		- ### Test the messages first
			- I think first we need to see if it's even possible to send the types of messages that the MicroFreak needs in the custom mode.
		- ### Colors and pad behavior
			- Ideally I'd have a different color for any preset that I've actually explored in detail in my various Ghost in the Patch episodes, and the colors should be more distinct the more times I use it. I'm not sure what type of button press it should be. I imagine it should be a toggle, but I don't know how to make the toggle correspond correctly.
		- [[Launchpad/Q/Can-Custom-Mode-select-MicroFreak-presets-by-bank-and-program-change]] · [#501 Record which MicroFreak preset is playing in GitP Sets, from Launchpad Custom Modes](https://github.com/codekiln/logseq-encode-garden/issues/501)
		- Launchpad Custom Modes could pick MicroFreak presets through a Max for Live device in Live, such as a number pad with Enter: [[Launchpad/Idea/Pick-MicroFreak-Presets-through-Live]]