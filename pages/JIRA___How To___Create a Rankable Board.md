tags:: [[Diataxis/How To]]

- # How to Create a [[JIRA/Board]] that's Rankable from a [[JIRA/Filter]]
	- create the saved filter
	- select / go into the project
	- 3 dots menu -> create board
		- Board from an existing Saved Filter
	- Select the saved filter
	- in the board
		- three dots menu -> settings
			- General
				- Board filter
					- Filter Details (expand disclosure item)
						- Issue Rank on Board
							- > Drag and drop issues to rank them by importance or urgency. “Order by rank” is applied to the board filter query, and is removed by editing the filter directly. See also [[JIRA/Docs/Rank an Issue]]
							- click button **Allow issue ranking**
								- dialog:
									- > This will add “Order by Rank” to your filter and remove any other “Order By” sorting. It will affect all boards using this filter.
									- click CONFIRM
						-