alias:: [[Project - Conway's Game of Life in GitHub Bio]]
tags:: Etude, [[Programming/Code Kata]]

- # Project - [[Game/Video/Conway's Game of Life]] in [[Github/Profile/Bio]]
	- [[Person/codekiln/GitHub/codekiln/Issue/01 increase resolution of life and package it up]]
		- ## Summary
		  id:: 67c04f1a-4aaa-4a4e-ace8-5e8901102982
			- **Goal**: enabling [https://github.com/codekiln](https://github.com/codekiln) - a [GitHub Profile Page](https://docs.github.com/en/get-started/start-your-journey/setting-up-your-profile#adding-a-profile-picture-and-bio) - to display **Conway's Game of Life** in the **Bio** field, updated at regular intervals.
			- The original solution developed a Python script that reads the current GitHub bio to extract an 18×8 Conway’s Game of Life board—or seeds a default board if none exists—then evolves the board one step according to Conway's rules, and finally updates the bio via the GitHub API. The script securely handles a personal access token through environment variables (using dotenv locally and GitHub Actions secrets in CI), enabling periodic, dynamic updates to the bio via a scheduled GitHub Action.
			- The GitHub bio field must display a precise 18×8 grid of characters despite lacking markdown support and using a variable-width font that complicates alignment, necessitating the use of UTF-8 block characters that render uniformly.