tags:: [[GitHub/Projects]], [[GitHub/Milestones]]

- # [What is the difference / relationship between GitHub Projects and Milestones? - Stack Overflow](https://stackoverflow.com/questions/39591795/what-is-the-difference-relationship-between-github-projects-and-milestones)
	- Top answer, from [[Person/Remi Lanvin]]
		- I'm wondering the exact same thing. Here is what I came up with.
		  
		  First, let's review the main similarities and differences:
		- An issue can belong to multiple Projects, but only one Milestone.
		- ~~Projects are never *complete*. There is no progress bar, or deadline.~~ Projects ~~have no progress bar or deadline~~ (they do now, though it is hidden inside the project's menu as a "Track project progress" checkmark, and there's no percentage calculation of progress), but can now be closed (as pointed out by @Sheen)
		- Milestones on the other hand have all that, but lack any form of organization. An issue is either in a milestone, or isn't. (They can be ordered as pointed out by @Nick McCurdy)
		- ~~Issues can be filtered by Milestone, but not by Project.~~ As pointed out by @cmonkey, issues can now be filtered by Project as well as Milestone.
		- Projects can contain *Notes* (which can be converted as issues) so it doesn't pollute the issue tracker with vague ideas
		- A Project can span over multiple Milestones, and a Milestone can contains parts of different Projects.
		- An Organization can have Projects as well. These projects can include tickets from any repository in the organization, which makes it quite useful.
		  
		  So the way I see it, is that **Projects** are a completely separate way to visualize and organize your work on an higher level (think "project management", multiple teams, multiple repository, etc.), while **Milestones** are a way to organize your deadlines and releases on a more basic level (think "release management", "versions", etc.). With this in mind, it makes sense that an issue only belongs to one Milestone (it's only released or pushed to production once) but can be part of different Projects.
		  
		  I'm sure they are other ways to look at it though, and I'm interested to hear other opinions.
		- ## Edit December 2017
		  
		  Some time ago, after working with Milestones and Projects for over a year, I realized there is another important aspect I had completely overlooked.
		- **Milestones** is a tool for [[Scrum]] methodology. Milestones are good for timeboxed iterations and working in sprints with batches of issues.
		- **Projects** is a tool for [[Kanban]] methodology. Projects are good for continuous delivery and steady flow of work.