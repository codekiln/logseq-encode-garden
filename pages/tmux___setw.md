- # About tmux setw
- **`setw` is only meaningful inside a tmux context.**
- But there are *two different ways* it can be valid, depending on how you run it.
- ## 1. `setw` is a tmux command, not a shell command
  `setw` is short for:
  - ~~~
    set-window-option
    ~~~
  It is part of **tmux's command language**, not your shell's.
  So this:
  - ~~~
    setw -g pane-border-style fg=colour238
    ~~~
  is **not valid in `bash`, `zsh`, etc.**
  If you type it in a normal terminal that is *not inside tmux*, you'll get:
  - ~~~
    command not found
    ~~~
  because your shell has no idea what `setw` is.
- ## 2. When it *is* valid
  - ### ✅ Inside a tmux session, in command mode
    If you're inside tmux:
    - Press:
      - ~~~
        prefix + :
        ~~~
    - Type:
      - ~~~
        setw -g pane-border-style fg=colour238
        ~~~
    - Hit Enter
    That runs the command in tmux's command interpreter.
  - ### ✅ Outside tmux, if you prefix with `tmux`
    You can also run it from a normal shell like this:
    - ~~~
      tmux setw -g pane-border-style fg=colour238
      ~~~
    In this form:
    - `tmux` = client program
    - `setw` = subcommand passed to the tmux server
    tmux sends it to the running server and executes it.
- ## 3. Where it is *not* valid
  - ### ❌ Plain shell (unqualified)
    This will never work:
    - ~~~
      setw -g pane-border-style ...
      ~~~
    unless:
    - you're inside `prefix + :` command mode in tmux.
- ## 4. Rule of thumb
  - Inside tmux command mode: ✅ `setw ...`
  - Normal shell: ✅ `tmux setw ...`
  - Normal shell without `tmux`: ❌ `setw ...`
  - Inside tmux pane as shell command: ❌ unless prefixed
- ## 5. Mental model
  Think of tmux like `git`:
  - ~~~
    git commit     # works
    commit         # doesn't
    ~~~
  Same pattern:
  - ~~~
    tmux setw ...
    setw ...
    ~~~
- ## 6. Practical advice
  If you're experimenting:
  - Inside tmux live: → `prefix :` then type `setw ...`
  - Writing config or scripts: → use `tmux setw ...`
