tags:: [[c74/M4L]]

- [codekiln/kebricide: Ableton Max For Live (M4L) device to cut up samples with a drum rack](https://github.com/codekiln/kebricide)
- [[2025-02-05 Wed]]
	- DONE list the clips in track in the console
		- LATER come up with a query to do a basic list of clips
			- DONE What are the best docs for the [[c74/M4L/Ref]]?
				- [[c74/M4L/Ref/Live API Overview]]
				- [[c74/M4L/Ref/LOM]]
		- DONE list tracks in console
			- [2025-02-05 10:25 - 23bfa327 - Modify track retrieval to log track names](https://github.com/codekiln/kebricide/commit/23bfa327) #git/commit
		- DONE list clips in each track
			- [2025-02-05 10:30 - c32f5f55 - Add clip retrieval function to track initialization](https://github.com/codekiln/kebricide/commit/c32f5f55) #git/commit
	- [[c74/max/js/Q/How do I get the line number of the error?]]
	- [[c74/max/js/Q/What is get the error get: no valid object set about?]]
	- [[c74/max/js/How To/Run a function when the js is recompiled or initialized]]
	-
- [[Feb 4th, 2025]]
	- `yarn dev` starts the watcher inside the [[VSCode/Dev Container]]
	- DONE how do I add `Project/Device.amxd` [[c74/M4L/.amxd]] to #Ableton ? ANS: drag and drop
	  collapsed:: true
		- DONE where is my repo? ANS: `Documents/GithHub/kebricide`
		- I think `.amxd` is a single max object
		- In order to add it, do I need to make sure it appears in my max path? Or is it simply a matter of dragging and dropping?
			- I thought [[Person/Zack Steinkamp]]  had a blog post about this, but it turned out I couldn't find one.
			- ## #Answer - yes, you just need to drag and drop [[c74/M4L/.amxd]]
	- DONE get some local examples of [[GitHub/zsteinkamp]] repos that use [[Typescript]]
		- here's a [[GitHub/Search]] for [all the typescript in the repos below](https://github.com/search?q=user%3Azsteinkamp+repo%3Azsteinkamp%2Fm4l-ChiasticSlide+OR+repo%3Azsteinkamp%2Fm4l-FibonacciNoteEcho+OR+repo%3Azsteinkamp%2Fm4l-FractalNoteEcho+OR+repo%3Azsteinkamp%2Fm4l-KeyStepper+OR+repo%3Azsteinkamp%2Fm4l-Knobbler4+OR+repo%3Azsteinkamp%2Fm4l-MoireArp+OR+repo%3Azsteinkamp%2Fm4l-typescript-base+path%3A*.ts&type=code)
		- [[GitHub/zsteinkamp/m4l-typescript-base]]  - This is the base template project that others are derived from
		- [[GitHub/zsteinkamp/m4l-ChiasticSlide]] 
		  [[GitHub/zsteinkamp/m4l-FibonacciNoteEcho]] 
		  [[GitHub/zsteinkamp/m4l-FractalNoteEcho]]
		- [[GitHub/zsteinkamp/m4l-KeyStepper]] - by far, the simplest example here
		- [[GitHub/zsteinkamp/m4l-Knobbler4]]
		- [[GitHub/zsteinkamp/m4l-MoireArp]]
		- Confirmed that these are all of them from [[Person/Zack Steinkamp]] here: [Feature request: filter plugins by those that use typescript · Issue #2 · zsteinkamp/plugins](https://github.com/zsteinkamp/plugins/issues/2) [[GitHub/zsteinkamp/plugins]]
	-