tags:: [[LangSmith Annotation Queues]]
date-completed:: [[2025-02-19 Wed]]

- https://academy.langchain.com/courses/take/intro-to-langsmith/lessons/60631062-lesson-2-annotation-queues
- ## [[LangSmith Annotation Queues]] overview
	- can have feedback applied to them
	- can be individually added to a dataset
		- #Q when should we encourage SMEs to add to a distinct [[LangSmith/Dataset]] vs when to apply a #Rubric ?
			- The annotation queue has a "D" hotkey for adding to the default dataset, so it might be simplest if we were going to only use datasets for the "golden" dataset - the "reference" of a good response.
- ## Creating [[LangSmith Annotation Queues]]
	- ### Selecting Default [[LangSmith/Dataset]]
		- in the example, they select `RAG Application Golden Dataset`
	- ### Creating [[LangSmith/Annotation/Rubric]]
		- we can leave high level instructions, e.g. "Please only score fields you are comfortable with"
		- full list of feedback tags from our [[LangSmith/Workspace]]
			- See also
				- [Set up feedback criteria | 🦜️🛠️ LangSmith](https://docs.smith.langchain.com/evaluation/how_to_guides/set_up_feedback_criteria)
					- https://smith.langchain.com/settings/workspaces/feedbacks -> link to edit feedback for workspace
				- [Feedback data format | 🦜️🛠️ LangSmith](https://docs.smith.langchain.com/reference/data_formats/feedback_data_format)
					- this is the data format for each "feedback item"
						- continuous
						- categorical
							- could be yes/no (binary)
		- For each field we can define special instructions *specifically in the context of this annotation* #Cool
	- Reservation Locks
		- ensures that multiple people don't provide feedback for the same run at the same time
- ## Going through the Annotation Queue
	-