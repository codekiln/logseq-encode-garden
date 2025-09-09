tags:: [[c74/M4L]]

- [codekiln/kebricide: Ableton Max For Live (M4L) device to cut up samples with a drum rack](https://github.com/codekiln/kebricide)
- [[2025-02-07 Fri]]
	- TODO make a prototype of [[c74/M4L/Idea/Alits]] just for Track and Clip
- [[2025-02-06 Thu]]
	- DONE define [[CursorAI/Project Rule]] for Kebricide
	- DONE figure out why I'm getting #Error `js: index.js: Javascript ReferenceError: window is not defined, line 6`
		- I think it's because yesterday I did [[Ableton/Menu/File/Collect All and Save]], and now I'm not interacting with the right version of the patcher
	- DONE figure out why I'm STILL getting #Error `jsliveapi: get: no valid object set` even after loading the right device ANS see [[c74/max/Ref/How to only see max console messages for This Patcher]] and [[c74/M4L/obj/LiveAPI/prop/unquotedpath]]
		- ```
		  js: BANG   
		  js: initialize   
		  js: Track 0: 1-MIDI   
		  jsliveapi: get: no valid object set
		  js: Track 0 has 1 clips   
		  js: Track 1: 2-piano_clean_stereo_norm_join   
		  jsliveapi: get: no valid object set
		  js: Track 1 has 1 clips   
		  
		  ```
		- I just added some logging, and I ended up not being able to reproduce it after that, what is going on?
		- ```
		  js: BANG   
		  js: initialize   
		  js: Track 0: 1-MIDI   
		  js: About to try to call get('has_clip') on "live_set tracks 0" clip_slots 0   
		  js: Track 0 has 1 clips   
		  js: Track 1: 2-piano_clean_stereo_norm_join   
		  js: About to try to call get('has_clip') on "live_set tracks 1" clip_slots 0   
		  js: Track 1 has 1 clips   
		  
		  ```
		- Yep, toggling "**Messages for All Patchers**" vs **Messages for This Patcher** makes this go away
		- *even so*, why am I getting a  `jsliveapi` error *not* in this patcher? I think actually that will hide messages from the jsliveapi, which is global outside the patcher??
		- ## I figured it out
		- I had to use [[c74/M4L/Ref/LOM/Track]] property [[c74/M4L/obj/LiveAPI/prop/unquotedpath]] instead of [[c74/M4L/obj/LiveAPI/prop/path]]; the latter has quotes around it.
			- From the documentation:>
			- ### unquotedpath [String]>
				- > The path to the Live object referred to by the LiveAPI object, without any quoting (the path property contains a quoted path). These paths are dependent on the currently open Set in Live, but are otherwise stable: *live_set tracks 0 devices 0* will always refer to the first device of the first track of the open Live Set.This should give us the correct unquoted path format that the Live API expects.
	- DONE how can I guard against the case that [[c74/M4L/obj/LiveAPI]] returns no object at the given [[c74/M4L/obj/live.path]]?
	  collapsed:: true
		- [[c74/M4L/obj/live.object]] [live.object Reference - Max 8 Documentation](https://docs.cycling74.com/legacy/max8/refpages/live.object) states under `getid` that
			- > The current object's id is sent from the outlet, preceded by the word id. If there is no current object, id 0 will be sent.
			- #Learned **As it turns out, just accessing the object's id and seeing if it's zero is enough to determine if the path returned a valid reference**.
			- #Learned that [[c74/M4L/Ref/Live API Overview/Datatypes]] states [that](https://docs.cycling74.com/legacy/max8/vignettes/live_api_overview#Datatypes) `bool` is explicitly a `1` or a `0`
			  collapsed:: true
				- | Datatype | Description |
				  | bool | 0 for false and 1 for true |
				  | symbol | a string with unicode character set () - (Use double quotes in message boxes to create symbols with spaces: set name "Smooth Synth" Double quotes in symbols are to be *prefixed* by backslashes: set name "Smooth \"Baby\" Synth" Backslashes are to be included as double backslashes: alpha beta \"gamma\" \\x\\ creates the symbol alpha beta "gamma" \x\.) |
				  | int | a 32 bit signed integer |
				  | float | a 32 bit float value |
				  | double | a 64 bit float value (maily used for timing values) |
				  | beats | song beat time counted in quarter notes, represented as double |
				  | time | song time in seconds, represented as double ()Time is given in seconds: time = beats * 60 / tempo_in_bpm, or sometimes in milliseconds: time = 1000 * beats * 60 / tempo_in_bpm) |
				  | list | a space separated list of the types above |
			- got around this with the following function:
			- ```typescript
			  /**
			   * Checks if a LiveAPI object is invalid or doesn't exist.
			   * 
			   * In Max's JS environment, a LiveAPI object is considered invalid if:
			   * - Its id property is "0" (returned as a string primitive)
			   * - Its info property is "No object" (returned as a string primitive)
			   * 
			   * @param api The LiveAPI object to validate
			   * @returns true if the LiveAPI object is invalid/doesn't exist, false otherwise
			   * 
			   * @example
			   * const api = new LiveAPI(() => {}, 'live_set')
			   * if (isInvalidLiveApiPath(api)) {
			   *   warn('Invalid or nonexistent Live API path')
			   * }
			   */
			  export function isInvalidLiveApiPath(api: LiveAPI): boolean {
			    return Number(api.id) === 0 || String(api.info) === "No object"
			  }
			  ```
	- DONE how can I get the [[c74/M4L/Ref/LOM/Clip]]s in the [[c74/M4L/Ref/LOM/Track]]?** ans**: use [[c74/M4L/Ref/LOM/Track/arrangement_clips]], which is a children accessor
	  collapsed:: true
		- ```ts
		  function getClips(track: LiveAPI): LiveAPI[] {
		    const clips: LiveAPI[] = []
		    const clipCount = track.getcount('arrangement_clips')
		    const basePath = track.unquotedpath
		    
		    logger(`Checking ${clipCount} arrangement clips`)
		    
		    for (let clipIndex = 0; clipIndex < clipCount; clipIndex++) {
		      const clipPath = `${basePath} arrangement_clips ${clipIndex}`
		      
		      try {
		        const clip = createValidatedLiveApi(clipPath)
		        logger(`Found clip ${clipIndex}:`)
		        logger(`- name: ${clip.get('name')}`)
		        logger(`- length: ${clip.get('length')}`)
		        clips.push(clip)
		      } catch (error) {
		        warn(`Error accessing clip ${clipIndex}: ${error.message}`)
		        // Continue to next iteration
		      }
		    }
		  
		    return clips
		  }
		  ```
- [[2025-02-05 Wed]]
  id:: 67a32012-a455-4a23-825a-7fa91929ca9f
	- DONE list the clips in track in the console
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