tags:: JIRA, Atlassian

- [ohmyzsh/plugins/jira at master · ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/jira)
- This plugin provides command line tools for interacting with Atlassian's [JIRA](https://www.atlassian.com/software/jira) bug tracking software.
- ## Jira Commands
  
  `jira help` or `jira usage` will print the below usage instructions:
  
  | Command | Description |
  |---------|-------------|
  | `jira` | Performs the default action |
  | `jira new` | Opens a new Jira issue dialogue |
  | `jira ABC-123` | Opens an existing issue |
  | `jira ABC-123 m` | Opens an existing issue for adding a comment |
  | `jira dashboard [rapid_view]` | Opens your JIRA dashboard |
  | `jira mine` | Queries for your own issues |
  | `jira tempo` | Opens your JIRA Tempo |
  | `jira reported [username]` | Queries for issues reported by a user |
  | `jira assigned [username]` | Queries for issues assigned to a user |
  | `jira branch` | Opens an existing issue matching the current branch name |
  | `jira help` | Prints usage instructions |
-