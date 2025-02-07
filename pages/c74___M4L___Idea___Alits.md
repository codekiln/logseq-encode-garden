tags:: Idea, Typescript, [[c74/M4L]]

- # #Alits - #Ableton Live #Typescript #API
	- Alits stands for **A**bleton **Li**ve **T**ype**S**cript - it's an idiomatic, [[Functional Reactive Programming]] typescript library for Ableton Live.
	- ## Problem Introduction
		- The Max for Live API that's accessible in Javascript is not a typical JS or typescript API. Much if not most of the Max/MSP language is about sending messages to objects, and Ableton Live API designed for Max for Live (M4L) inherits the characteristics and assumptions of that approach. Fundamentally, the Ableton Live API in Max/MSP is a string manipulation and messaging API. In [[c74/max/obj/js]], the [[Ableton/Live Object Model]]relies heavily on instantiating [[c74/M4L/obj/LiveAPI]] with [[c74/M4L/obj/live.path]] strings, calling getters and setters with strings, and using callbacks rather than promises to receive updates to properties.
		- ### Getting an object reference that points to an Ableton Live entity
			- A typical API in js/ts would mirror the UML diagram or Entity Relationship Diagram in API objects that return references to each other. For example, a `Track` object would have a `get_clips()` function that returned `Clip` objects.
			- In the Max/MSP-centric M4L API, however, one needs to construct paths and validate them. For example, to get clips from a track, one needs to construct a [Live Object Model](https://docs.cycling74.com/legacy/max8/vignettes/live_object_model) path using a live object model string path, and then instantiate a new `LiveAPI` with that path. As described in the [[c74/M4L/Ref/Live API Overview]],
				- > Live objects are accessed using paths according to the Live Object Model. For example, the first clip in the third track can be accessed by the path `live_set tracks 2 clip_slots 0 clip`. Alternatively, it can be accessed via `live_set scenes 0 clip_slots 2 clip`. Or, if the clip is shown in the detail view, via `live_set view detail_clip`.
			- To get a reference to any object, one first needs to construct a string path and validate that it refers to anything.
		- ### Calling a method on an object that points to an Ableton Live entity
			- After obtaining a reference to an object that points to an entity in Ableton Live, calling methods on that object requires some string processing and validation to send messages to it. Quoting the [[c74/M4L/Ref/Live API Overview/Functions]] [section here](https://docs.cycling74.com/legacy/max8/vignettes/live_api_overview#Functions),
				- > Many Live objects have functions which can be called by sending call and the function name to [live.object](https://docs.cycling74.com/max8/refpages/live.object), like `call create_scene` for a `Song` object.
			- See also [[c74/M4L/Ref/Creating Devices that use the Live API/Calling a function]] section [here](https://docs.cycling74.com/legacy/max8/vignettes/live_api#Calling_a_function_in_the_Live_API_using_Max_for_Live_objects), which describes the Max/MSP Live API method of calling a function.
			- This `call` is mirrored in the [[c74/M4L/Ref/jsliveapi]]; see [call documentation here](https://docs.cycling74.com/legacy/max8/vignettes/jsliveapi#call):
				- > Arguments: `function [string]`, `arguments [anything]`
				- > Calls the given function of the current object, optionally with a list of arguments.
			- So, for example, to call [Clip.add_new_notes](https://docs.cycling74.com/legacy/max8/vignettes/live_object_model#live_obj_anchor_Clip), one must
				- `<ClipObjectReference>.call("add_new_notes", ...)`
		- ### Accessing properties of an object that points to an Ableton Live entity
			- A typical API in js/ts would allow access attributes directly, for example, `Clip.get_file_path()` or `Clip.get_length()`, rather than calling `.get(attribute)` and then validating if the attribute exists and coercing the results to types in javascript.
			- Accessing any of the object's members is also string- and messaging-centric; quoting [[c74/M4L/Ref/Creating Devices that use the Live API]] [here](https://docs.cycling74.com/legacy/max8/vignettes/live_api#Observing_a_property_in_the_Live_API_using_Max_for_Live_objects),
				- > The [live.path](https://docs.cycling74.com/max8/refpages/live.path) object is used to navigate to the Live objects whose functions you want to call. Each property of the Live object model in a session is associated with an id specific to that particular Song, Track, Clip, Clip Slot, Device, etc.
				- > **Sending a message to a [live.path](https://docs.cycling74.com/max8/refpages/live.path) object results in an object id being sent out the left outout** (where the id follows the object) or middle outlet (where the id follows the path).
			- This API is mirrored in the [[c74/M4L/Ref/jsliveapi/Methods/get]] (see [`get` reference documentation here](https://docs.cycling74.com/legacy/max8/vignettes/jsliveapi#get)), where to get a property, one needs to call the `<LiveAPIInstance>.get(property)`, where `property` here is, for example, in the case of [Clip](https://docs.cycling74.com/legacy/max8/vignettes/live_object_model#live_obj_anchor_Clip), `file_path`, `length`, or any other instance.
		- ### Callbacks and Observing Properties of an object that points to an Ableton Live entity
			- In addition to calling [[c74/M4L/Ref/jsliveapi/Methods/get]], there's another way to observe a changes to a property by using [[c74/M4L/Ref/jsliveapi/Properties/property]] -  [LiveAPI.property](https://docs.cycling74.com/legacy/max8/vignettes/jsliveapi#property), which is described as:
				- > The observed property, child or child-list of the object at the current path, if desired. For instance, if the LiveAPI object refers to "live_set tracks 1", setting the property to "mute" would cause changes to the "mute" property of the 2nd track to be reported to the callback function defined in the LiveAPI Constructor.
				- For example, the reference docs for [[c74/M4L/Ref/LOM/Track/Properties/color]] [here](https://docs.cycling74.com/legacy/max8/vignettes/live_object_model#live_obj_anchor_Track) is
					- ## color
						- **TYPE**: `int`
						- **ACCESS**: `get`, `set`, `observe`
						- **Description**:
							- The RGB value of the track's color in the form `0x00rrggbb` or `(2^16 * red) + (2^8) * green + blue`, where red, green, and blue are values from 0 (dark) to 255 (light).
							- When setting the RGB value, the nearest color from the track color chooser is taken.
					- Note that this has the `observe` access level, which means we can observe it.
				- So, to observe the [Track.color](https://docs.cycling74.com/legacy/max8/vignettes/live_object_model#live_obj_anchor_Track) property when the Ableton Live set user changes the color of a particular track, one would do something like:
					- ```ts
					  const childTrack = new LiveAPI((iargs: IArguments) => trackColorChangedCallback(iargs), "id " + childTrackId)
					  state.colors.push(childTrack.get('color'))
					  childTrack.property = 'color'
					  ```
						- Credit: adapted from [[GitHub/zsteinkamp/m4l-ChiasticSlide]] by [[Person/Zack Steinkamp]] [here](https://github.com/zsteinkamp/m4l-ChiasticSlide/blob/main/src/chiasticSlide.ts#L394-L399)
					- So after this snippet, whenever the user changes the color of a track, the `trackColorChangedCallback` function will be called with `IArguments`.
						- `IArguments` is the typescript interface for the JS-native `arguments` that any javascript function is called with; see also [[Typescript/tsconfig/noLib]] [here](https://www.typescriptlang.org/tsconfig/#noLib).
					- In order to turn `IArguments` into a [[JS/Array]], one first needs to call [[c74/max/js/Ref/JS Global Methods/jsthis Methods/arrayfromargs]] [here](https://docs.cycling74.com/legacy/max8/vignettes/jsglobal#arrayfromargs)
						- > The arrayfromargs() method will convert the arguments property to an `Array`, optionally with message as the zeroth element of the array.
						- While the documentation states "optionally with message as the zeroth element of the array," I couldn't find any way to disable this feature; ironically, the `arguments` to `arrayfromargs` is undocumented as far as I can tell.
					- So by calling `const args = arrayfromargs(iargs)`, now `args` contains the arguments that the callback was called with as a [[JS/Array]]. By looking at the `color` property documentation and combined with the `arrayfromargs` documentation above, we can presume that the arguments would be the of length two, and the first argument would be the name of the property, `color`, and the second would be the value of the property, the newly updated value of the `color` property as an `int`.
				- This is particularly unidiomatic. In a modern typescript application, one would observe a property using [Promises](https://www.codecademy.com/resources/docs/typescript/promises) and utilizing `async` and `await` in functions to process the resulting updates. Alternatively, and, in my perspective, ideally, some APIs are coded so as to assume a [[Functional Reactive Programming]] (FRP) paradigm, for example, using [[RxJS]]. For a description of #Observable and this paradigm, see [[Person/Tim Dwyer]]'s #Blog post [Functional Reactive Programming | Tim’s code stuff](https://tgdwyer.github.io/functionalreactiveprogramming/).
	- ## Problem Example
		- For example, a function to get all the [[c74/M4L/Ref/LOM/Clip]]s from a track (see also [Live Object Model - Clip](https://docs.cycling74.com/legacy/max8/vignettes/live_object_model)) could be written like the following,
			- ```ts
			  function getClips(track: LiveAPI): LiveAPI[] {
			    const clips: LiveAPI[] = []
			    const clipCount = track.getcount('arrangement_clips')
			    const basePath = track.unquotedpath
			      
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
		- After after obtaining an array of [Clip](https://docs.cycling74.com/legacy/max8/vignettes/live_object_model) object references with `getClips(track)`, accessing the members of the objects is also done using a string-based API, as one can see from these lines above:
			- ```ts
			  logger(`Found clip ${clipIndex}:`)
			  logger(`- name: ${clip.get('name')}`)
			  logger(`- length: ${clip.get('length')}`)
			  ```
		- Above, inside `createValidatedLiveApi` is a custom function to validate the path and raise an error if it doesn't refer to anything, or return a `LiveAPI` object if it is valid:
			- ```ts 
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
			  
			  /**
			   * Creates a LiveAPI object at the given path and verifies it exists.
			   * @param path The path to create the LiveAPI object at
			   * @param callback Optional callback function for the LiveAPI constructor
			   * @returns A valid LiveAPI object
			   * @throws InvalidLiveApiPathError if the path doesn't exist
			   */
			  export function createValidatedLiveApi(
			    path: string,
			    callback: () => void = () => {}
			  ): LiveAPI {
			    const api = new LiveAPI(callback, path)
			    if (isInvalidLiveApiPath(api)) {
			      warn('----------------------------------------')
			      warn('Invalid Live API Path Error:')
			      warn(`Path: ${path}`)
			      warn(`Info: ${api.info}`)
			      warn(`ID: ${api.id}`)
			      warn('----------------------------------------')
			      throw new Error(`Invalid Live API path: ${path}`)
			    }
			    return api
			  }
			  ```
	- ## Suggested API - An #Observable [[Typescript/Library]] for Live API
		- The core characteristics of a more idiomatic typescript library would be:
			- The library would be oriented towards a [[Functional Reactive Programming]] paradigm using [[RxJS]].
			- The library would abstract away and hide the details of using the [[Ableton/Live Object Model]] paths from [[c74/M4L/obj/live.path]] and treat that as a low-level implementation detail. Advanced users could still utilize methods that enabled using this functionality, but the core assumption of the Alits API is that it would no longer be necessary.
			- [Each object](https://docs.cycling74.com/legacy/max8/vignettes/live_object_model) in the [[Ableton/Live Object Model]] would have its own [Typescript class](https://www.typescriptlang.org/docs/handbook/2/classes.html).
				- Each object would have a `get_children()` function that would return an Array of objects of the appropriate Typescript classes in the API.
				- Each property
					- that has `get` access has a `<ObjectInstance>.get_<propertyname>()` method.
					- that has `set` access has a `<ObjectInstance>.set_<propertyname>(...)` method.
					- that has `observe` access has a `<ObjectInstance>.observe_<propertyname>(...)` method that returns an observable. Internally, this would call [[RxJS/subscribe]] (see also docs for [Subscription](https://rxjs.dev/guide/subscription)).
					  id:: 67a5f8ab-b96a-4f3a-978f-b0e9967e3531
				- Each method would be proxied appropriately onto the object. For example, the typescript class corresponding to [Clip](https://docs.cycling74.com/legacy/max8/vignettes/live_object_model#live_obj_anchor_Clip) would have a `Clip.add_new_notes(...)` method.
			- The library would come with first-class support for logging and error handling.
		- The library that implements this API could be written using the [[GitHub/Repo/Template]] that [[Person/Alessandro Petrone]] wrote for maxing max/msp libraries in #Typescript - [[GitHub/aptrn/maxmsp-ts-library-template]]. As the README from that template mentions,
			- > This is a [turborepo monorepo](https://turbo.build/repo/docs) ([[turborepo]]) template with the following structure:
				- ```
				  ├── apps
				  │   └── maxmsp-test
				  └── packages
				      └── my-library
				  ```
			- > `my-library`: Contains your TypeScript library
			- >`maxmsp-test`: Contains an instance of [this template](https://github.com/aptrn/maxmsp-ts-example)  ([[GitHub/aptrn/maxmsp-ts-example]]) with `my-library` as a dependency.
			- Since this is is a [[turborepo]] monorepo, the library could develop the core of this library in its own package, `alits-core`.
				- Most users will not need the entire API, which could be broken up to simplify versioning and minimize merge conflicts. Other sub-libraries could focus on isolated portions of the library:
					- `alits-max-device` -
						- [[Ableton/Max for Live/MIDI Effect]]
						- [[Ableton/Max for Live/Audio Effect]]
						- [[Ableton/Max for Live/Instrument]]
					- `alits-simpler-device` - Simpler support
					- `alits-rack-device` - Ableton Drum Rack support
					- `alits-control-surface` -  Ableton Control Surface support
					- `alits-logging` - logging utilities for Ableton Live
					- ...
				- `alits` itself could reference the entire collection of libraries.
			-
	-
	-
-