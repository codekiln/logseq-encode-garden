# How to get a [[File/.ics]] of events this week in o365 Outlook
	- ## Temporarily Publish Your Calendar to a Private Link
		- Log in to Outlook on the Web.​ [1](https://answers.microsoft.com/en-us/msoffice/forum/all/export-calendar-online-version-to-csv-file/cede8f8a-29f3-4d58-b6b7-64250b1d86c7)
		- Click on the gear icon (Settings) and select **View all Outlook settings**. ​[2](https://answers.microsoft.com/en-us/msoffice/forum/all/export-calendar-online-version-to-csv-file/cede8f8a-29f3-4d58-b6b7-64250b1d86c7)
		- Navigate to **Calendar > Shared calendars**. ​[3](https://answers.microsoft.com/en-us/msoffice/forum/all/export-calendar-online-version-to-csv-file/cede8f8a-29f3-4d58-b6b7-64250b1d86c7)
		- Under **Publish a calendar**, select your calendar and choose the permissions you prefer. Click **Publish**. ​[4](https://answers.microsoft.com/en-us/msoffice/forum/all/export-calendar-online-version-to-csv-file/cede8f8a-29f3-4d58-b6b7-64250b1d86c7)
		- Two links will be generated: an HTML link and an ICS link. Copy the ICS link. ​[5](https://answers.microsoft.com/en-us/msoffice/forum/all/export-calendar-online-version-to-csv-file/cede8f8a-29f3-4d58-b6b7-64250b1d86c7)
		- Open it in a browser to download it.
		- Click the button to unpublish the calendar.
	- ## Use [[uvx]] and [[Py/Lib/ics-query]] to filter events down to just one week
		- The `.ics` file will be a fairly large text file if you have been using o365 outlook for a long time.
		- To filter it down to just this week, ensure you have [[uv]] installed, then run
			- `uvx ics-query between 2025-03-17 2025-03-23 calendar.ics > filtered_calendar.ics`
	- ## Potential Next Steps
		- [[Logseq/How To/Create an Agenda using Cursor and an ics file]]
	- ## Finally, remove `.ics` files
		- It's advisable to treat these as sensitive files containing [[Secrets]]. Remove `calendar.ics` and `filtered_calendar.ics` when done.
-