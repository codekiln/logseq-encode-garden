# How to create a week agenda in Logseq using [[CursorAI]] and an [[.ics]] file
	- Given that `temp/w12.ics` has been populated from [[o365/outlook/How To/Get an .ics of events this week]],
	- > I'm trying to prepare an agenda for each day of week 12 in `@2025___t1___w12.md` using calendar data from `@w12.ics`.  Can you please fill in the agenda under the headings inside Week Days?
	- ## Important note
		- [[.ics]] files can contain sensitive secrets such as [[Zoom]] links. Use textual CLI tools or [[Py/Lib/ics]] to filter out information before using with Cursor. Alternatively, consider an intermediate step to just output the most needed information from each agenda event programmatically, while omitting the sensitive info.