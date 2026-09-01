- Some coding agents (typically codex) tend to sometimes work in the wrong working directory. Before writing to a file, creating a branch, or creating a worktree, ensure that you are working in the repository in its `ghq` location.
- 1. Resolve the current repository root with `git rev-parse --show-toplevel`.
  2. Inspect its `origin` remote and derive the `host/owner/repository` ghq address.
  3. Resolve the registered copy with `ghq list --full-path --exact <ghq-address>`.
  4. Compare real paths and continue only when the current root equals the registered
   copy and is inside the ghq root.
- You don't need to tell me about your thought process as you verify you are working in the right directory.