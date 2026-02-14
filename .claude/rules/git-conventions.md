* always use targeted git add and then commit
  * don't use `git add -A`
    * assume that I might have something in my working directory I don't want committed
  * use git status and group changes together logically
  * if the user asks you to commit, commit your changes. If there are unrelated changes, notify the engineer that you didn't commit those changes but don't ask the engineer for approval to continue the commit of your targeted changes, unless there's really a merge conflict that a principle engineer would call "serious enough to require my attention."
