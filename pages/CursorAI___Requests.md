-
alias:: [[CursorAI/Docs/Account/Usage/Fast and Slow Requests]]

- https://docs.cursor.com/account/usage#fast-and-slow-requests
- There are two types of requests in Cursor,  [[CursorAI/Slow Requests]]  and  [[CursorAI/Fast Requests]] that have their own pool
- By default, Cursor servers try to give all users fast `premium` model requests.
- when users run out of fast `premium` credits, they are moved to a **slow pool**.
	- Wait times in the slow pool are **calculated proportionally to how many slow requests you’ve used**
- To bypass wait times entirely, you can enable [[CursorAI/Usage-Based Pricing]] pricing (you’ll only be charged for requests **beyond your included fast requests**)
	- See [[CursorAI/Settings/Models]] for an overview of which models are `premium` and their alternatives.
		- #note *All [[LLM Reasoning Model]]s currently require usage-based pricing*