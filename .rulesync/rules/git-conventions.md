---
root: false
targets:
  - '*'
description: 'High level rules for using git'
---

* always use targeted git add and then commit
  * don't use `git add -A`
    * assume that I might have something in my working directory I don't want committed
  * use git status and group changes together logically
