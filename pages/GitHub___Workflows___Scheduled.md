alias:: [[Github Scheduled Workflow]]

- https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#schedule
- The `schedule` event allows you to trigger a workflow at a scheduled time.
- ## Example
	- ```
	  on:
	    schedule:
	      - cron: "15 4,5 * * *"   # <=== Change this value
	  ```