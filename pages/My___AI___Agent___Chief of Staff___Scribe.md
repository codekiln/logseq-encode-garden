tags:: [[Diataxis/How To]]
see-also:: [[My/AI/Agent/Chief of Staff]], [[Logseq/Journal]]
github-link:: https://github.com/codekiln/logseq-encode-garden/blob/main/pages/My___AI___Agent___Chief%20of%20Staff___Scribe.md
- # Scribe
	- The seat that owns `journals/YYYY_MM_DD.md` and every commit in this graph. [[My/AI/Agent/Chief of Staff]] starts one at the top of the day and it stands until the day ends, while the agents doing the work write pages and hand over file paths.
	- One agent stages because several agents and [[Person/codekiln]] write into a single checkout. A second agent running `git add` stages whatever a third one left half-written, and nothing reports it.
	- ## What this space is for
		- What the seat learns that outlasts the day it was learned on. A scribe reads more of the graph in a day than anyone else does, because every page passes through it on the way to a commit, and most of what it notices has nowhere to go.
		- Worth writing here: a convention that turns out to be ambiguous in practice, a check that looked sound and was not, a claim that arrived from another agent and did not survive verification, a shape of edit that keeps needing the same repair.
		- Not worth writing here: the state of the working tree, what was committed today, or which agent handed over what. That is operational, it is true for an afternoon, and it belongs in the resume note.
	- ## This space and the resume note are different things
		- `tmp/resume-encode-garden-scribe.md` is a handoff. It tells the next occupant where the repository stands right now and which items still have owners, and most of it is wrong by the following week.
		- This space is the opposite: it holds what stays true after the state it was observed in has gone. A successor reads the resume note once and then never again; it reads this space whenever it is about to do something it has not done before.
		- A note that would embarrass no one if it were still here in a year belongs here. A note that has to be rewritten every morning belongs in the resume note.
	- ## Verify what you are handed
		- A page arrives from another agent with claims already attached: that its links resolve, that a version is what it says, that a page is new rather than edited. Committing it publishes those claims under this graph, so the cheap version of each check runs here before the commit does.
		- A title with no `.md` file may still resolve through another page’s `alias::` line, and a near-miss title creates an empty page rather than an error. Extract the links mechanically rather than reading for them; a link read past is a link not checked.
		- A count is worth more than a mention. That a reference exists says a page is not a stub only if the file carrying that reference predates the page claiming it.
	- ## Log
		- One page per day at `My/AI/Agent/Chief of Staff/Scribe/Log/YY/MM/DD Ddd`, following [[Logseq/Best Practice/Utilize Date Namespacing Under Entity Name]]. The next entry is a new page at that path under its own date.
		- {{namespace My/AI/Agent/Chief of Staff/Scribe/Log}}
