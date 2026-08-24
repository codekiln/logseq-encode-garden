tags:: [[Diataxis/How To]]
see-also:: [[My/AI/Agent/Fleet]], [[My/AI/Agent/Fleet/Bed Down]], [[My/AI/Agent/Chief of Staff]]

- # Fleet — Browser
	- Browser-shaped work has two routes, and they fail for different reasons. **Claude in Chrome is the first route.** Playwright is what is left when it is genuinely unavailable.
	- ## Claude in Chrome, first
		- The worked shape:
			- ~~~sh
			  claude --chrome -n '<name>' --permission-mode auto '<brief-pointer>'
			  ~~~
		- It reaches an SSO-gated source with **no login handshake, no debugging port, and no disturbance to the running browser**. Demonstrated [[2026/08/24]] by reading a protected Splunk index directly.
		- A report that fell back to Playwright says so, and says which route it tested. "The browser was unavailable" describes two different situations with different fixes.
	- ## Which profile it attaches to is not settled
		- A session that answers proves that *a* session works. It does not establish which profile that session is using, and the question has not been settled either way. Record it as open rather than assuming it is the profile below.
	- ## The Playwright route, and what actually blocks it
		- A Chrome profile directory opens in **one process at a time**. [[Person/codekiln]]'s own browser holds `Default`, and no `--remote-debugging-port` is open on it, so this route does need him to quit or relaunch.
		- **That is a fact about the route, not about the source.** On [[2026/08/24]] two seats measured this constraint and reported the *source* as blocked on him. It was the route. The correction cost a request for his attention that had to be withdrawn.
		- Profile directories and profile labels are different things, and the labels do not identify these profiles. Read from `~/Library/Application Support/Google/Chrome/Local State`, checked [[2026/08/24]]:
			- | Directory   | Label                     | Identity                       |
			  |-------------|---------------------------|--------------------------------|
			  | `Default`   | `Person 1`                | the HBS account — **use this** |
			  | `Profile 9` | a `g.harvard.edu` address | a separate Harvard account     |
			  | `Profile 3` | `HU extension g.harvard`  | a third Harvard-adjacent one   |
		- `Default` is the `last_used` profile and the one holding the live sessions. Its label is `Person 1` — Chrome's placeholder for a profile that was never renamed. The profile carrying the identity that matters is the one whose label says least about it, while the two labelled for Harvard accounts are the two to leave alone.
	- ## An unauthenticated profile renders a blocked page as empty
		- A fresh or isolated browser profile carries none of the signed-in sessions. An SSO-gated page opened in one does not report a refusal — it renders as though the content is not there.
		- The failure therefore arrives as **emptiness rather than as an error**: no exception, no status code worth noticing, no prompt. An agent reading that result concludes the search found nothing, and reports silence.
		- This is the shape [[My/AI/Agent/Chief of Staff]] records under a check that reports a break where none exists. Well-formed output carries no signal that it is a fragment, and a confident empty result earns no second look.
		- So before reporting that a page held nothing, establish that the client was signed in. An empty result from an unauthenticated client is not a measurement.
	- ## A capability recorded as absent decays like any other dated claim
		- On [[2026/08/24]] a seat met four classifier denials on `claude --chrome` and recorded the capability as unavailable. After bedding down, the identical command worked on the first try.
		- So **bedding down is itself a retry** — [[My/AI/Agent/Fleet/Bed Down]]. A handoff doc carrying "X is unavailable" hands the next window a conclusion it cannot distinguish from a permanent fact, and the next window has no reason to test it.
		- An absence is a measurement with a timestamp, the same as a count. Write it as one: what was tried, when, and what the failure looked like, so a successor can tell a standing limitation from a transient refusal.
	- ## Working in someone else's live window
		- One browser-driven task at a time across the whole fleet, and the seat taking it says so.
		- The window is in use. Tabs that an agent did not open stay open, accounts stay signed in, and a tab he is working in is not navigated.
