- # Project Brief: Live Object Model Observability and RxJS
	- ## Purpose
		- This brief explores how Ableton Live's Live Object Model (LOM) supports observation, and how those semantics can be mapped to **Functional Reactive Programming (FRP)** patterns using **RxJS**. It highlights the quirks and constraints developers must understand when designing reactive abstractions on top of Max for Live's `LiveAPI`.
	- ## Native Observability in the LOM
		- **Property Access Flags**: In the LOM documentation, each property specifies access modes: `get`, `set`, `observe`.
			- Example: `Track.color` → access: `get`, `set`, `observe`.
			- `observe` means the Live API can notify you when the value changes.
		- **LiveAPI `.property` Attribute**:
			- Assigning `.property = "foo"` tells a `LiveAPI` instance to observe the property named `foo`.
			- Updates are delivered to the constructor's callback function (Max patcher outlet or JS callback).
			- Each update arrives as an argument list, e.g. `["mute", 1]`.
		- **One-at-a-Time Limitation**:
			- A single `LiveAPI` object can only observe *one property at a time*.
			- To observe multiple properties of the same LOM object, you must create multiple `LiveAPI` instances pointing at the same path/ID.
	- ## Implications for FRP
		- **Observable Sources**
			- Every `observe`-able property in the LOM is a natural source stream.
			- Examples: `Track.mute`, `Clip.playing_status`, `DeviceParameter.value`, `Song.tempo`.
		- **Subscription Pattern**
			- Each property observation requires a dedicated `LiveAPI` instance.
			- Subscriptions must be explicitly cleaned up (unset `.property` or release the object).
		- **Event Payloads**
			- Values are delivered as arrays like `[propertyName, newValue]`.
			- Conversion is required: `arrayfromargs(arguments)` in Max JS, or typed translation in higher-level wrappers.
		- **Unsubscription**
			- FRP systems require a teardown path. In Max JS this means clearing `.property` and freeing the `LiveAPI` object.
	- ## Mapping to RxJS
		- **Raw pattern in Max JS:**
			- ~~~
			  var track = new LiveAPI(callback, "live_set tracks 0");
			  track.property = "mute";  // observe mute
			  ~~~
		- **Wrapped as an RxJS Observable:**
			- ~~~
			  function observeProperty(path: string, prop: string): Observable<any> {
			  return new Observable(subscriber => {
			    const api = new LiveAPI(args => {
			      const [p, value] = arrayfromargs(args);
			      subscriber.next(value);
			    }, path);
			  
			    api.property = prop;  // start observing
			  
			    return () => {
			      api.property = ""; // stop observing
			      api.free();
			    };
			  });
			  }
			  ~~~
		- **Composed usage:**
			- ~~~
			  const mute$ = observeProperty("live_set tracks 0", "mute");
			  const solo$ = observeProperty("live_set tracks 0", "solo");
			  
			  combineLatest([mute$, solo$]).subscribe(([mute, solo]) => {
			  console.log(`Mute: ${mute}, Solo: ${solo}`);
			  });
			  ~~~
	- ## Quirks to Keep in Mind
		- **One property per `LiveAPI`**: Multiproperty observation requires multiple handles.
		- **Push vs Pull**: `observe` properties push events; `get` must be called explicitly for snapshots.
		- **ID Validation**: Before observing, always confirm the `LiveAPI.id` is valid (`!= 0`).
		- **Threading**: Observers operate in Max's low-priority thread — timing is reliable for UI/automation, but not for DSP-rate processes.
		- **Message Format**: Callbacks receive raw argument arrays, not typed values.
	- ## FRP Fit in the LOM
		- **Great fit:** Any property with `observe` access (Track, Clip, Device, Song, DrumPad, DeviceParameter).
		- **Partial fit:** Collections (e.g., `get_devices()`) — snapshots only, unless higher-level abstractions watch for children changes.
		- **Not a fit:** One-time actions (`call create_scene`, `call duplicate_clip`, etc.) → better modeled as async functions.
	- ## Summary
		- The LOM already provides a subscription primitive: the `.property` field of `LiveAPI`. This allows any `observe`-able property to become a push-stream of events. The main quirks are:
			- Only one observed property per `LiveAPI` object.
			- Multiple properties require multiple `LiveAPI` handles.
			- Event payloads need translation from raw Max-style arguments.
		- RxJS (or any FRP library) fits naturally on top of this model, providing composition, transformation, and lifecycle management. By wrapping LOM properties as Observables, developers gain the full expressive power of functional reactive programming within Ableton Live.