tags:: [[Diataxis/How To]]
see-also:: [[My/AI/Agent/Fleet]], [[My/AI/Agent/Chief of Staff]]

- # Fleet — Browser
	- An agent doing browser work drives [[Person/codekiln]]'s own Chrome profile, so the pages it opens are the pages he would see. The handle for that profile is its **directory name, `Default`**.
	- ## Why the directory name is the handle
		- Profile directories and profile labels are different things, and the labels do not identify these profiles. Read from `~/Library/Application Support/Google/Chrome/Local State`, checked [[2026/08/24]]:
			- | Directory   | Label                    | Identity                       |
			  |-------------|--------------------------|--------------------------------|
			  | `Default`   | `Person 1`               | the HBS account — **use this** |
			  | `Profile 9` | a `g.harvard.edu` address | a separate Harvard account     |
			  | `Profile 3` | `HU extension g.harvard` | a third Harvard-adjacent one   |
		- `Default` is the `last_used` profile and the one holding the live sessions.
		- Its label is `Person 1` — Chrome's placeholder for a profile that was never renamed. The profile carrying the identity that matters is the one whose label says least about it, while the two labelled for Harvard accounts are the two to leave alone.
	- ## An isolated profile turns a locked door into an empty room
		- A fresh or isolated browser profile carries none of the signed-in sessions. An SSO-gated page opened in one does not report a refusal — it renders as though the content is not there.
		- The failure therefore arrives as **emptiness rather than as an error**: no exception, no status code worth noticing, no prompt. An agent reading that result concludes the search found nothing, and reports silence.
		- This is the shape [[My/AI/Agent/Chief of Staff]] records under a check that reports a break where none exists. Well-formed output carries no signal that it is a fragment, and a confident empty result earns no second look.
		- So before reporting that a page held nothing, establish that the client was signed in. An empty result from an unauthenticated client is not a measurement.
		- On [[2026/08/24]] this cost the fleet an entire Slack sweep, which came back as silence.
	- ## Working in someone else's live window
		- A Chrome profile directory opens in **one process at a time**. `Default` is also where his own browsing happens, so it can already be held by his running browser.
		- One browser-driven task at a time across the whole fleet, and the seat taking it says so.
		- The window is in use. Tabs that an agent did not open stay open, accounts stay signed in, and a tab he is working in is not navigated.
	- ## What is not settled
		- No invocation that attaches a session to that profile has been verified yet. The profile mapping above is measured; the command line to reach it is not, and an unverified one recorded here would read exactly like a measured one.
