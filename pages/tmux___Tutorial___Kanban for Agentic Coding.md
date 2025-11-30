# tmux as a Kanban for Agentic Coding (Minimal Tutorial)
- ## Goal
  Use tmux window/pane titles as live "cards" that reflect issue + agent status (e.g., `#342 auth-bug [working]`, `#517 deps [PR]`).
- ## 1) Absolute minimum tmux concepts
- **Session** = workspace
- **Window** = a card (one issue)
- **Pane** = subprocess in a card (Claude, tests, logs, etc.)
- **Prefix** = `Ctrl-b` (default)
- ## 2) Commands you actually need
- ### Create a card (window)
- Prefix `c` → new window
- ### Rename a card (set issue + status)
- Prefix `,` → rename window interactively
- ### Jump between cards
- Prefix `w` → list windows
- Prefix `0..9` → jump by index
- ### Close a card when merged
- Prefix `&` → kill window
- ## 3) Make titles automatic (one-time config)
  Add to `~/.tmux.conf`:
  - ~~~
    # Allow programs to rename panes/windows
    set -g allow-rename on
    
    # Prefer window name set by tmux when available
    set -g automatic-rename off
    
    # Show window name in status bar
    set -g set-titles on
    set -g set-titles-string "#S:#W"
    ~~~
  Reload config inside tmux:
  - ~~~
    tmux source-file ~/.tmux.conf
    ~~~
- ## 4) Update status from inside the terminal (no tmux commands needed)
  From **any shell** in a pane, change the *window name* (card title):
  - ~~~
    tmux rename-window "#342 auth-bug [working]"
    ~~~
  Change just the **pane title** (useful if you split panes later):
  - ~~~
    printf '\033]2;%s\007' "Claude: planning"
    ~~~
- ## 5) Minimal workflow pattern
- Prefix `c` → new window
- `tmux rename-window "#NNN short-title [todo]"`
- Start Claude Code in that window
- As it progresses:
  - ~~~
    tmux rename-window "#NNN short-title [working]"
    tmux rename-window "#NNN short-title [PR]"
    tmux rename-window "#NNN short-title [merged]"
    ~~~
- Prefix `&` → close when done
- You now have a tmux-based Kanban.
- ## 6) Optional: tiny helpers (quality of life)
  Put in your shell rc (`.bashrc` / `.zshrc` / `.fish`):
  - ~~~
    issue() {
    tmux rename-window "$1"
    }
    
    status() {
    local cur="$(tmux display-message -p '#W')"
    tmux rename-window "${cur%%[*}[$1]"
    }
    ~~~
  Usage:
  - ~~~
    issue "#342 auth-bug [todo]"
    status working
    status PR
    status merged
    ~~~
- ## 7) Mental model
- **Window name = card title + state**
- **Kill window = close card**
- **Window list = Kanban board**
- That's it. Nothing else required.