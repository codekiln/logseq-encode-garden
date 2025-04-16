# How to filter for tasks assigned to a particular user after they become inactive in [[JIRA]]
	- 1 - find the user's profile
		- try to find a ticket that was assigned to the user
		- then click through to that user's profile
		- the profile will like `https://<YOURDOMAIN>.atlassian.net/jira/people/<ABOUT_SIX_NUMERIC_DIGITS>:<UUID_HERE>`
		- here the username is now `<ABOUT_SIX_NUMERIC_DIGITS>:<UUID_HERE>` for the purposes of filtering
		- for example, the [[JIRA/JQL]] to filter for the tickets assigned to this particular user would be
			- ```jql
			  assignee = <ABOUT_SIX_NUMERIC_DIGITS>:<UUID_HERE> order by created DESC
			  ```
			-
		-