---
name: feedback-gh-cli-for-repo-lookup
description: Use gh CLI to fetch GitHub repo info instead of spawning an agent or web-fetching
metadata:
  type: feedback
---

Use `gh repo view <owner/repo> --json name,description,homepageUrl,primaryLanguage,stargazerCount,repositoryTopics` to fetch GitHub repo metadata.

**Why:** User explicitly redirected mid-task when I spawned an agent to web-fetch a repo. `gh` is faster, stays in the terminal, and avoids unnecessary agent overhead.

**How to apply:** Whenever the task involves importing a GitHub repo as an entity or looking up repo details, use `gh repo view` directly instead of spawning an Explore agent or using WebFetch.
